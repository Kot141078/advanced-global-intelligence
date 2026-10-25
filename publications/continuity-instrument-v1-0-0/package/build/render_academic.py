#!/usr/bin/env python3
"""Render the CI academic edition with Pandoc AST and ReportLab.

Copyright 2026 Ivan Kotov. All rights reserved. No license grant.
Requires Python 3.10+, reportlab, and pandoc. Does not execute CI experiments.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfdoc import PDFString
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, KeepTogether, LongTable, PageBreak,
    PageTemplate, Paragraph, Spacer, Table, TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

PAGE_W, PAGE_H = A4
MARGIN = 22 * mm
WIDTH = PAGE_W - 2 * MARGIN
NAVY = colors.HexColor('#20364B')
INK = colors.HexColor('#202428')
MUTED = colors.HexColor('#57616B')
RULE = colors.HexColor('#BAC3CB')
PALE = colors.HexColor('#F0F3F5')


def font_directory(requested: str | None) -> Path:
    candidates = []
    if requested:
        candidates.append(Path(requested))
    candidates.append(Path('/usr/share/fonts/truetype/dejavu'))
    try:
        import matplotlib
        candidates.append(Path(matplotlib.get_data_path()) / 'fonts' / 'ttf')
    except ImportError:
        pass
    names = ['DejaVuSerif.ttf', 'DejaVuSerif-Bold.ttf',
             'DejaVuSerif-Italic.ttf', 'DejaVuSerif-BoldItalic.ttf']
    for candidate in candidates:
        if all((candidate / x).is_file() for x in names):
            return candidate
    raise RuntimeError('Provide --font-dir containing the DejaVu font family.')


def register_fonts(directory: Path) -> None:
    families = {
        'Academic': ['DejaVuSerif.ttf', 'DejaVuSerif-Bold.ttf',
                     'DejaVuSerif-Italic.ttf', 'DejaVuSerif-BoldItalic.ttf'],
        'Sans': ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf',
                 'DejaVuSans-Oblique.ttf', 'DejaVuSans-BoldOblique.ttf'],
        'Mono': ['DejaVuSansMono.ttf', 'DejaVuSansMono-Bold.ttf',
                 'DejaVuSansMono-Oblique.ttf', 'DejaVuSansMono-BoldOblique.ttf'],
    }
    for family, files in families.items():
        for suffix, filename in zip(['', '-Bold', '-Italic', '-BoldItalic'], files):
            source = directory / filename
            if not source.exists():
                source = directory / files[0]
            pdfmetrics.registerFont(TTFont(family + suffix, str(source)))
        pdfmetrics.registerFontFamily(family, normal=family, bold=family+'-Bold',
                                      italic=family+'-Italic', boldItalic=family+'-BoldItalic')


def clean(text: str) -> str:
    for old in ['\u2010', '\u2011', '\u2012', '\u2013', '\u2014', '\u2212']:
        text = text.replace(old, '-')
    return text.replace('\u00a0', ' ').replace('\u202f', ' ')


def esc(text: str) -> str:
    return html.escape(clean(str(text)), quote=False)


def plain(inlines: list) -> str:
    out = []
    for item in inlines:
        kind, content = item['t'], item.get('c')
        if kind == 'Str':
            out.append(content)
        elif kind in ['Space', 'SoftBreak', 'LineBreak']:
            out.append(' ')
        elif kind in ['Code', 'Math']:
            out.append(content[-1])
        elif kind == 'Link':
            out.append(plain(content[1]))
        elif kind in ['Strong', 'Emph', 'Strikeout', 'SmallCaps', 'Superscript', 'Subscript']:
            out.append(plain(content))
        elif kind == 'Quoted':
            out.append(plain(content[1]))
        elif kind == 'Span':
            out.append(plain(content[1]))
    return clean(''.join(out))


def inline(inlines: list) -> str:
    out = []
    for item in inlines:
        kind, content = item['t'], item.get('c')
        if kind == 'Str':
            out.append(esc(content))
        elif kind in ['Space', 'SoftBreak']:
            out.append(' ')
        elif kind == 'LineBreak':
            out.append('<br/>')
        elif kind == 'Code':
            out.append('<font name="Mono" size="8.5">' + esc(content[1]) + '</font>')
        elif kind == 'Strong':
            out.append('<b>' + inline(content) + '</b>')
        elif kind == 'Emph':
            out.append('<i>' + inline(content) + '</i>')
        elif kind in ['SmallCaps', 'Strikeout']:
            out.append(inline(content))
        elif kind == 'Superscript':
            out.append('<super>' + inline(content) + '</super>')
        elif kind == 'Subscript':
            out.append('<sub>' + inline(content) + '</sub>')
        elif kind == 'Link':
            target = content[2][0]
            label = inline(content[1])
            if target.startswith(('https://', 'http://', 'mailto:')):
                out.append('<a href="' + html.escape(target, quote=True) + '" color="#20364B">' + label + '</a>')
            else:
                out.append(label)
        elif kind == 'Quoted':
            out.append('&quot;' + inline(content[1]) + '&quot;')
        elif kind == 'Span':
            out.append(inline(content[1]))
        elif kind == 'Math':
            out.append('<font name="Mono" size="8.5">' + esc(content[1]) + '</font>')
        elif kind == 'RawInline':
            if content[1].lower() in ['<br>', '<br/>', '<br />']:
                out.append('<br/>')
        elif kind == 'Note':
            out.append(' [note]')
    return ''.join(out)


STYLES = {}


def make_styles() -> None:
    base = dict(fontName='Academic', fontSize=10.25, leading=15.2,
                textColor=INK, spaceAfter=7, allowWidows=0, allowOrphans=0,
                splitLongWords=1, uriWasteReduce=0.1)
    STYLES['body'] = ParagraphStyle('body', alignment=TA_JUSTIFY, **base)
    STYLES['left'] = ParagraphStyle('left', alignment=TA_LEFT, **base)
    STYLES['small'] = ParagraphStyle('small', fontName='Academic', fontSize=9,
                                    leading=12.6, textColor=MUTED, spaceAfter=6,
                                    splitLongWords=1, allowWidows=0, allowOrphans=0)
    STYLES['h1'] = ParagraphStyle('h1', fontName='Academic-Bold', fontSize=15,
                                 leading=19.5, textColor=NAVY, spaceBefore=14,
                                 spaceAfter=9, keepWithNext=1)
    STYLES['h2'] = ParagraphStyle('h2', fontName='Academic-Bold', fontSize=11.8,
                                 leading=16, textColor=INK, spaceBefore=10,
                                 spaceAfter=6, keepWithNext=1)
    STYLES['h3'] = ParagraphStyle('h3', fontName='Academic-Bold', fontSize=10.4,
                                 leading=14.8, spaceBefore=9, spaceAfter=5,
                                 keepWithNext=1, textColor=INK)
    STYLES['table'] = ParagraphStyle('table', fontName='Academic', fontSize=8.6,
                                    leading=11.8, textColor=INK, spaceAfter=0,
                                    splitLongWords=1, allowWidows=1, allowOrphans=1)
    STYLES['tablehead'] = ParagraphStyle('tablehead', parent=STYLES['table'],
                                        fontName='Sans-Bold', fontSize=8,
                                        leading=10.6, textColor=NAVY)
    STYLES['caption'] = ParagraphStyle('caption', fontName='Academic', fontSize=9,
                                      leading=12.3, textColor=MUTED, spaceBefore=4,
                                      spaceAfter=12, keepWithNext=0)
    STYLES['code'] = ParagraphStyle('code', fontName='Mono', fontSize=8,
                                   leading=11.5, textColor=INK, spaceAfter=1,
                                   splitLongWords=1, backColor=PALE,
                                   borderPadding=5, allowWidows=1, allowOrphans=1)
    STYLES['quote'] = ParagraphStyle('quote', parent=STYLES['body'],
                                    leftIndent=12, rightIndent=8, fontSize=10,
                                    borderColor=RULE, borderWidth=0,
                                    textColor=NAVY)


class Timeline(Flowable):
    def __init__(self, russian=False):
        Flowable.__init__(self)
        self.width, self.height, self.russian = WIDTH, 208, russian

    def draw(self):
        c = self.canv
        x0, x1 = 105, WIDTH - 8
        scale = (x1 - x0) / 60
        def tx(s, x, y, size=8.5, bold=False):
            c.setFont('Sans-Bold' if bold else 'Sans', size)
            c.setFillColor(INK)
            c.drawString(x, y, s)
        def bar(a, b, y, color, label=None):
            c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(.5)
            c.rect(x0+a*scale, y, (b-a)*scale, 15, fill=1, stroke=1)
            if label:
                c.setFillColor(colors.white if color == NAVY else INK)
                c.setFont('Sans', 7.2)
                c.drawCentredString(x0+(a+b)*scale/2, y+4.5, label)
        ru = self.russian
        tx('Учебное окно: 60 минут' if ru else 'Illustrative window: 60 minutes', 0, 192, 10, True)
        tx('Интервал A' if ru else 'Interval A', 0, 164)
        tx('Интервал B' if ru else 'Interval B', 0, 141)
        tx('Интервал C' if ru else 'Interval C', 0, 118)
        bar(0,20,160,colors.HexColor('#CFDCE7'),'0-20')
        bar(10,30,137,colors.HexColor('#CFDCE7'),'10-30')
        bar(50,60,114,colors.HexColor('#CFDCE7'),'50-60')
        tx('Итоговое покрытие' if ru else 'Combined coverage',0,84,7.8,True)
        bar(0,30,79,NAVY,'30')
        bar(30,40,79,colors.HexColor('#C9CFD4'),'10')
        bar(40,50,79,colors.white,'10')
        bar(50,60,79,NAVY,'10')
        c.setStrokeColor(RULE)
        for t in range(0,61,10):
            x=x0+t*scale; c.line(x,74,x,70)
            c.setFont('Sans',7.5);c.setFillColor(MUTED);c.drawCentredString(x,58,str(t))
        tx('Подтверждено 40 | Пауза 10 | Неизвестно 10' if ru else 'Verified 40 | Known pause 10 | Unexplained 10',0,31,9,True)
        tx('Перекрытие считается один раз. Это не эмпирический результат.' if ru else 'Overlap is counted once. This is not an empirical result.',0,11,8)


class Workflow(Flowable):
    def __init__(self, russian=False):
        Flowable.__init__(self);self.width=WIDTH;self.height=172;self.russian=russian

    def draw(self):
        c=self.canv;ru=self.russian;gap=18;w=(WIDTH-2*gap)/3
        heads=['Внешний контур','CI v1.0.0','Профиль результата'] if ru else ['External preparation','CI v1.0.0','Result profile']
        lines=[['Сбор записей','Привязка свидетельств','Решения о допуске'],['Проверка структуры','Интервалы и пробелы','Сортировка записей'],['Вектор + ветвь','Неопределённость','Границы утверждений']] if ru else [['Collect records','Bind evidence','Decide admissibility'],['Validate structure','Intervals and gaps','Order supplied records'],['Vector and branch','Structured uncertainty','Explicit claim ceiling']]
        for j in range(3):
            x=j*(w+gap);c.setFillColor(PALE if j!=1 else colors.HexColor('#E4EBF1'))
            c.setStrokeColor(RULE);c.rect(x,48,w,109,fill=1,stroke=1)
            p=Paragraph(esc(heads[j]),ParagraphStyle('figh',fontName='Sans-Bold',fontSize=8.8,leading=11.5,textColor=NAVY,alignment=TA_CENTER))
            _,ph=p.wrap(w-12,40);p.drawOn(c,x+6,135-ph)
            for k,s in enumerate(lines[j]):
                p=Paragraph(esc(s),ParagraphStyle('figt',fontName='Sans',fontSize=7.5,leading=10,textColor=INK,alignment=TA_CENTER))
                _,ph=p.wrap(w-10,30);p.drawOn(c,x+5,110-k*18-ph)
            if j<2:
                ax=x+w+3;ay=101;c.setStrokeColor(NAVY);c.line(ax,ay,ax+12,ay)
                c.line(ax+12,ay,ax+8,ay+3);c.line(ax+12,ay,ax+8,ay-3)
        c.setFillColor(MUTED);c.setFont('Sans',7.8)
        c.drawString(0,28,'Допуск и истинность свидетельств не вычисляются преобразователем.' if ru else 'The transformer does not establish evidence truth or admissibility.')
        c.drawString(0,13,'Распознавание и предоставление полномочий требуют отдельных процедур.' if ru else 'Recognition decisions and authority grants require separate procedures.')


class AcademicDoc(BaseDocTemplate):
    def __init__(self, filename, spec, **kwargs):
        self.spec=spec;self.head_count=0;self.heading_registry=[]
        super().__init__(filename, pagesize=A4, leftMargin=MARGIN,rightMargin=MARGIN,
                         topMargin=24*mm,bottomMargin=23*mm,
                         title=spec['title']+': '+spec['subtitle'],author='Ivan Kotov',
                         subject=spec['subject'],creator='CI academic edition / ReportLab',
                         pageCompression=1,invariant=1,**kwargs)
        frame=Frame(MARGIN,23*mm,WIDTH,PAGE_H-47*mm,id='body',leftPadding=0,
                    rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id='academic',frames=frame,onPage=self.decorate))

    def beforeDocument(self):
        self.head_count=0;self.heading_registry=[]

    def decorate(self,canvas,doc):
        canvas.saveState()
        canvas.setAuthor('Ivan Kotov')
        canvas.setTitle(self.spec['title']+': '+self.spec['subtitle'])
        canvas._doc.Catalog.Lang=PDFString('ru-RU' if self.spec.get('lang')=='ru' else 'en-GB')
        if doc.page>1:
            canvas.setFont('Sans',7.6);canvas.setFillColor(MUTED)
            canvas.drawString(MARGIN,PAGE_H-14*mm,self.spec['short_title'])
            canvas.drawRightString(PAGE_W-MARGIN,PAGE_H-14*mm,'CI 1.0.0 | Academic edition')
            canvas.setStrokeColor(RULE);canvas.setLineWidth(.45)
            canvas.line(MARGIN,PAGE_H-16.5*mm,PAGE_W-MARGIN,PAGE_H-16.5*mm)
            canvas.line(MARGIN,17.5*mm,PAGE_W-MARGIN,17.5*mm)
            canvas.setFont('Sans',7.4)
            canvas.drawString(MARGIN,12.5*mm,'Ivan Kotov | ORCID 0009-0009-6002-9845')
            canvas.drawRightString(PAGE_W-MARGIN,12.5*mm,str(doc.page))
        canvas.restoreState()

    def afterFlowable(self,flowable):
        if isinstance(flowable,Paragraph) and getattr(flowable,'_heading_level',None) is not None:
            level=flowable._heading_level
            self.head_count+=1
            key='section-%04d'%self.head_count
            text=flowable.getPlainText()
            self.canv.bookmarkPage(key)
            # Only top-level sections are listed, keeping the contents concise.
            if level==0:
                self.canv.addOutlineEntry(text,key,0,False)
                self.notify('TOCEntry',(0,text,self.page,key))
            self.heading_registry.append({'text':text,'page':self.page,'level':level})


def heading(text,level=1):
    h=Paragraph(esc(text),STYLES['h'+str(min(level,3))])
    h._heading_level=level-1
    return h


def cell_text(blocks):
    texts=[]
    for b in blocks:
        if b['t'] in ['Para','Plain']:
            texts.append(inline(b['c']))
        elif b['t']=='CodeBlock':
            texts.append(esc(b['c'][1]))
        elif b['t']=='BulletList':
            texts.extend(cell_text(item) for item in b['c'])
    return '<br/>'.join(texts)


def read_table(content):
    head=content[3][1]
    rows=[]
    for body in content[4]:
        rows.extend(body[2]);rows.extend(body[3])
    rows.extend(content[5][1])
    heads=[[cell_text(c[4]) for c in row[1]] for row in head]
    data=[[cell_text(c[4]) for c in row[1]] for row in rows]
    return (heads[0] if heads else []),data


def table_flow(content):
    header, rows=read_table(content)
    if not rows:
        return []
    n=max(len(header),len(rows[0]))
    raw=lambda s:re.sub('<[^>]+>','',s)
    # Wide technical pin tables and dense claim matrices become readable records.
    record_style=n>=5 or (n>=4 and max(len(raw(s)) for r in rows for s in r)>220)
    if record_style:
        out=[]
        for row in rows:
            out.append(Paragraph(row[0],STYLES['h3']))
            for j,s in enumerate(row[1:],1):
                label=header[j] if j<len(header) else str(j+1)
                out.append(Paragraph('<b>'+label+':</b> '+s,STYLES['left']))
            out.append(Spacer(1,5))
        return out
    if n==2:
        widths=[.31*WIDTH,.69*WIDTH]
    elif n==3:
        widths=[.22*WIDTH,.37*WIDTH,.41*WIDTH]
    elif n==4:
        widths=[.20*WIDTH,.23*WIDTH,.24*WIDTH,.33*WIDTH]
    else:
        widths=[WIDTH/n]*n
    data=[]
    if header:
        data.append([Paragraph(x,STYLES['tablehead']) for x in header])
    data.extend([[Paragraph(x,STYLES['table']) for x in row] for row in rows])
    t=LongTable(data,colWidths=widths,repeatRows=1 if header else 0,
                hAlign='LEFT',splitByRow=1,splitInRow=0,spaceBefore=5,spaceAfter=11)
    style=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),
           ('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),
           ('BOTTOMPADDING',(0,0),(-1,-1),6),
           ('LINEBELOW',(0,0),(-1,0),.7,RULE),
           ('LINEBELOW',(0,-1),(-1,-1),.5,RULE)]
    if header:
        style.append(('BACKGROUND',(0,0),(-1,0),PALE))
    for i in range(1,len(data)):
        style.append(('LINEBELOW',(0,i),(-1,i),.3,colors.HexColor('#DBE0E4')))
    t.setStyle(TableStyle(style))
    return [t]


def blocks_to_flow(blocks, spec, level_shift=0):
    out=[]
    for b in blocks:
        kind,c=b['t'],b.get('c')
        if kind=='Header':
            level=max(1,c[0]+level_shift)
            out.append(heading(plain(c[2]),level))
        elif kind in ['Para','Plain']:
            t=plain(c)
            if t=='[[TIMELINE]]':
                out.append(KeepTogether([Timeline(spec.get('lang')=='ru'),Paragraph(
                    'Рисунок 2. Учебная интервальная реконструкция. Все значения заданы для иллюстрации.' if spec.get('lang')=='ru' else
                    'Figure 2. Illustrative interval reconstruction. All values are stipulated for this example.',STYLES['caption'])]))
            elif t=='[[WORKFLOW]]':
                out.append(KeepTogether([Workflow(spec.get('lang')=='ru'),Paragraph(
                    'Рисунок 1. Граница текущего преобразователя и внешних процедур.' if spec.get('lang')=='ru' else
                    'Figure 1. The boundary between the current transformer and external procedures.',STYLES['caption'])]))
            else:
                out.append(Paragraph(inline(c),STYLES['body']))
        elif kind=='BulletList':
            for item in c:
                fs=blocks_to_flow(item,spec,level_shift)
                if fs and isinstance(fs[0],Paragraph):
                    st=ParagraphStyle('bullet',parent=STYLES['left'],leftIndent=12,
                                      firstLineIndent=-10,spaceAfter=4)
                    fs[0]=Paragraph('• '+fs[0].text,st)
                out.extend(fs)
            out.append(Spacer(1,3))
        elif kind=='OrderedList':
            start=c[0][0]
            for idx,item in enumerate(c[1],start):
                fs=blocks_to_flow(item,spec,level_shift)
                if fs and isinstance(fs[0],Paragraph):
                    st=ParagraphStyle('number',parent=STYLES['left'],leftIndent=17,
                                      firstLineIndent=-17,spaceAfter=4)
                    fs[0]=Paragraph(str(idx)+'. '+fs[0].text,st)
                out.extend(fs)
            out.append(Spacer(1,3))
        elif kind=='CodeBlock':
            out.append(Spacer(1,7))
            rendered_lines=[]
            for line in c[1].splitlines():
                line=clean(line).replace(' ','&#160;')
                line=html.escape(line,quote=False).replace('&amp;#160;','&#160;')
                rendered_lines.append(line or '&#160;')
            out.append(Paragraph('<br/>'.join(rendered_lines),STYLES['code']))
            out.append(Spacer(1,11))
        elif kind=='BlockQuote':
            for item in c:
                if item['t'] in ['Para','Plain']:
                    out.append(Paragraph(inline(item['c']),STYLES['quote']))
                else:
                    out.extend(blocks_to_flow([item],spec,level_shift))
        elif kind=='Table':
            out.extend(table_flow(c))
        elif kind=='HorizontalRule':
            out.append(Spacer(1,10))
        elif kind=='Div':
            out.extend(blocks_to_flow(c[1],spec,level_shift))
        elif kind=='RawBlock':
            if c[1].strip()=='<!-- PAGEBREAK -->':
                out.append(PageBreak())
        elif kind=='DefinitionList':
            for term,definitions in c:
                out.append(Paragraph('<b>'+inline(term)+'</b>',STYLES['left']))
                for definition in definitions:
                    out.extend(blocks_to_flow(definition,spec,level_shift))
        else:
            raise ValueError('Unsupported Pandoc block: '+kind)
    return out


def cover(spec):
    ru=spec.get('lang')=='ru'
    title_style=ParagraphStyle('cover-title',fontName='Academic-Bold',fontSize=23,
                                leading=30,textColor=NAVY,alignment=TA_CENTER,
                                spaceAfter=18)
    subtitle_style=ParagraphStyle('cover-subtitle',fontName='Academic',fontSize=12,
                                   leading=18,textColor=MUTED,alignment=TA_CENTER,
                                   spaceAfter=18)
    center=ParagraphStyle('cover-center',fontName='Academic',fontSize=12,
                           leading=18,alignment=TA_CENTER,spaceAfter=7,textColor=INK)
    small=ParagraphStyle('cover-small',fontName='Sans',fontSize=9,leading=13.8,
                          alignment=TA_CENTER,spaceAfter=7,textColor=MUTED)
    result=[Spacer(1,30*mm),Paragraph('CONTINUITY INSTRUMENT',small),
            Spacer(1,7*mm),Paragraph(esc(spec['title']),title_style),
            Paragraph(esc(spec['subtitle']),subtitle_style),Spacer(1,9*mm),
            Paragraph('<b>Иван Котов / Ivan Kotov</b>' if ru else '<b>Ivan Kotov</b>',center),
            Paragraph('Независимый исследователь<br/>Брюссель, Бельгия' if ru else
                      'Independent researcher<br/>Brussels, Belgium',center),
            Paragraph('<a href="https://orcid.org/0009-0009-6002-9845" color="#20364B">ORCID 0009-0009-6002-9845</a>',small),
            Paragraph('<a href="https://ivankotov.eu" color="#20364B">ivankotov.eu</a>',small),
            Spacer(1,18*mm),Paragraph('CI 1.0.0 | Academic publication edition '+str(spec.get('reading_edition_number', 1)),small),
            Paragraph('25 октября 2026' if ru else '25 October 2026',center),
            Spacer(1,8*mm),Paragraph(esc(spec['cover_note']),small),PageBreak()]
    return result


def render(root: Path, spec: dict):
    source=root/'editorial_sources'/spec['source']
    target=root/'PDFs'/spec['filename']
    target.parent.mkdir(parents=True,exist_ok=True)
    ast=json.loads(subprocess.run(['pandoc','-f','gfm','-t','json',str(source)],
                                  check=True,capture_output=True,text=True).stdout)
    blocks=ast['blocks']
    if blocks and blocks[0]['t']=='Header' and blocks[0]['c'][0]==1:
        blocks=blocks[1:]
    doc=AcademicDoc(str(target),spec)
    story=cover(spec)
    if spec.get('front_note'):
        story.append(Paragraph(spec['front_note'],STYLES['small']))
    toc=TableOfContents()
    toc.levelStyles=[ParagraphStyle('toc',fontName='Academic',fontSize=10,
                                    leading=15,spaceBefore=4,leftIndent=0,
                                    firstLineIndent=0,textColor=INK)]
    story.append(Paragraph('Содержание' if spec.get('lang')=='ru' else 'Contents',STYLES['h1']))
    story.extend([Spacer(1,5),toc,PageBreak()])
    story.extend(blocks_to_flow(blocks,spec,spec.get('heading_shift',0)))
    doc.multiBuild(story)
    return {'filename':spec['filename'],'pages':doc.page,'headings':doc.heading_registry}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('package_root',type=Path)
    parser.add_argument('--font-dir')
    parser.add_argument('--only',help='Optional PDF filename to render')
    parser.add_argument('--language',choices=['en','ru'],help='Render only the selected language')
    args=parser.parse_args()
    os.environ.setdefault('SOURCE_DATE_EPOCH',str(int(datetime(2026,10,25,tzinfo=timezone.utc).timestamp())))
    register_fonts(font_directory(args.font_dir));make_styles()
    specs=json.loads((args.package_root/'editorial_sources'/'PDF_EDITION.json').read_text())['documents']
    results=[]
    for spec in specs:
        if args.only and args.only!=spec['filename']:
            continue
        if args.language and args.language!=spec.get('lang'):
            continue
        result=render(args.package_root,spec);results.append(result)
        print(json.dumps(result,ensure_ascii=False),flush=True)
    return 0


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError,ValueError,RuntimeError,subprocess.CalledProcessError) as exc:
        print('PDF build failed: '+str(exc),file=sys.stderr)
        raise SystemExit(2)
