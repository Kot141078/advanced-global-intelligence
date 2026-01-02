# KI-Sicherheit und die Grenzen der Regulierung  
## Ein kybernetischer Ansatz zum Risikomanagement im europäischen Kontext

**Autor:** Ivan Kotov (Brüssel)  
**Dokumenttyp:** Hintergrund / Kontextanalyse  
**Status:** Öffentlicher Forschungsdokument  
**Datum:** 2026-01-02

---

## 0. Zweck dieses Dokuments

Dieses Dokument liefert eine konzeptionelle und analytische Grundlage
für die in diesem Repository dargestellten
protokollarischen und architektonischen Arbeiten.

Ziel ist es:
- darzulegen, warum bestehende Ansätze zur KI-Sicherheit unzureichend sind;
- strukturelle Lücken in den aktuellen EU-Regulierungsrahmen aufzuzeigen;
- die Notwendigkeit kybernetischer Lösungen auf Architekturebene zu begründen.

Dieses Dokument ist **keine** Protokollspezifikation
und **kein** rechtlicher Vorschlag.
Es dient als analytischer Kontext.

---

## 1. Das Kernproblem: Sicherheit ohne Kontrolle

Der aktuelle Diskurs zur KI-Sicherheit konzentriert sich hauptsächlich auf:
- Modell-Alignment;
- Inhaltsfilterung;
- Trainingszeit-Beschränkungen;
- nachgelagerte Moderation.

Diese Ansätze gehen davon aus, dass:
- KI-Systeme zentralisiert betrieben werden;
- Verhalten über Anbieter vermittelt wird;
- Risiken innerhalb des Modells kontrollierbar sind.

Diese Annahmen sind nicht länger haltbar.

Moderne KI-Systeme sind zunehmend:
- verteilt;
- agentenbasiert;
- zeitlich persistent;
- zu indirekten Handlungen fähig.

Sicherheitsmechanismen,
die auf das Innere des Modells beschränkt sind,
können solche Systeme nicht wirksam steuern.

---

## 2. Die Provider-Lücke (Provider Gap)

Eine zentrale strukturelle Schwäche der heutigen KI-Governance
ist die sogenannte **Provider-Lücke**.

### 2.1 Definition

Die Provider-Lücke entsteht, wenn:
- Verantwortung formal einem Anbieter zugewiesen wird,
- die tatsächliche Kontrolle über das Systemverhalten jedoch verloren geht.

In verteilten agentischen Systemen:
- können Modelle offen oder replizierbar sein;
- operieren Agenten über mehrere Jurisdiktionen hinweg;
- entsteht Verhalten aus Interaktion statt aus Instruktion.

Der verantwortliche Akteur
ist nicht länger der kontrollierende Akteur.

---

## 3. Temporale und agentische Risiken

KI-Risiken werden häufig
als statische Eigenschaften von Ausgaben betrachtet.
Dabei wird **Zeit** als kritische Dimension vernachlässigt.

### 3.1 Temporale Agenten

Ein temporaler Agent ist gekennzeichnet durch:
- einen persistenten internen Zustand;
- Gedächtnis über Interaktionen hinweg;
- Zielentwicklung im Zeitverlauf.

Risiken entstehen nicht durch einzelne Antworten,
sondern durch **Verhaltensverläufe**.

### 3.2 Emergende Multi-Agenten-Dynamiken

Wenn mehrere Agenten interagieren:
- entstehen Koordinationseffekte;
- bilden sich Koalitionen;
- verstärken Rückkopplungsschleifen das Verhalten.

Diese Dynamiken lassen sich weder zuverlässig vorhersagen
noch durch modellbezogene Richtlinien begrenzen.

---

## 4. Warum Alignment allein nicht ausreicht

Alignment-Techniken (z. B. RLHF):
- formen Antwortverteilungen;
- reduzieren offensichtlichen Missbrauch;
- erhöhen kurzfristige Konformität.

Alignment:
- wirkt jedoch innerhalb des Modells;
- setzt einen festen Einsatzkontext voraus;
- adressiert keine agentenübergreifenden Interaktionen.

Alignment ist keine Kontrolle.
Es ist **Konditionierung**.

---

## 5. Kybernetik als alternatives Rahmenwerk

Die Kybernetik bietet eine andere Perspektive:
- Systeme werden durch Rückkopplung definiert;
- Stabilität entsteht durch Regulation, nicht durch Absicht;
- Kontrolle muss der Systemkomplexität entsprechen.

### 5.1 Ashbys Gesetz der erforderlichen Varietät

Ein Regulator muss
mindestens so viel Varietät besitzen
wie das System, das er regulieren will.

Verteilte KI-Systeme
übersteigen die Varietät zentralisierter Regulatoren.

Regulation muss daher:
- verteilt;
- mehrschichtig;
- adaptiv sein.

---

## 6. Externe Kontrollschleifen vs. interne Beschränkungen

Wirksame Sicherheit erfordert **externe Kontrollschleifen**:
- Beobachtung des Verhaltens über die Zeit;
- Durchsetzung von Grenzen unabhängig vom Modell;
- kontrollierte Degradation statt Eskalation.

Interne Beschränkungen (Filter, Prompts)
können diese Rolle nicht allein erfüllen.

Die Unterscheidung ist entscheidend:
- Ethik beschreibt Absicht;
- Recht beschreibt Erlaubnis;
- Kybernetik beschreibt Stabilität.

---

## 7. Identitäts- und Attributionslücken

Ein weiteres ungelöstes Problem ist die **Identität**.

In verteilten KI-Systemen:
- können Agenten geklont werden;
- modifiziert werden;
- geforkt werden;
- neu eingesetzt werden.

Ohne robuste Identitätsmechanismen:
- scheitert Attribution;
- zerfällt Verantwortung;
- ist Vertrauen nicht herstellbar.

Identität muss:
- kryptografisch fundiert sein;
- verhaltensbasiert beobachtbar sein;
- unabhängig von Anbietern bestehen.

---

## 8. Grenzen der Regulierung im EU-Kontext

Der EU AI Act stellt einen wichtigen Fortschritt dar,
fokussiert sich jedoch weiterhin auf:
- Klassifizierung von Systemen;
- Pflichten der Anbieter;
- Compliance zum Zeitpunkt der Bereitstellung.

Er adressiert nicht vollständig:
- emergentes agentisches Verhalten;
- post-deployment Evolution;
- grenzüberschreitende Interaktionen;
- dezentrale Kontrolle.

Dies ist kein Mangel an Absicht,
sondern eine Frage des Geltungsbereichs.

---

## 9. Die Notwendigkeit architektonischer Sicherheit

Die Schlussfolgerung lautet nicht,
dass Regulierung nutzlos ist,
sondern dass sie allein nicht ausreicht.

Sicherheit muss verankert sein:
- in der Systemarchitektur;
- in der Interaktionstopologie;
- in Ressourcenbeschränkungen;
- in externen Rückkopplungsschleifen.

Dies erfordert Protokolle und Architekturen,
die **unterhalb politischer Vorgaben**
und **oberhalb konkreter Implementierungen** wirken.

---

## 10. Bezug zu anderen Dokumenten im Repository

Diese Kontextanalyse motiviert:

- **Protokolldokumente**,  
  die kybernetische Grenzen und Beschränkungen definieren
  (siehe `protocols/`);

- **Architekturdokumente**,  
  die konkrete Systementwürfe vorschlagen,
  welche diese Prinzipien umsetzen
  (siehe `architecture/`).

Insbesondere werden Konflikte zwischen Systemen
und objektiven realweltlichen Beschränkungen
auf Protokollebene
als **Reality Boundary Layer (L4)** behandelt.

---

## 11. Schlussfolgerung

KI-Sicherheit lässt sich nicht reduzieren auf:
- bessere Prompts;
- bessere Datensätze;
- bessere Absichten.

Sie erfordert:
- strukturelle Kontrolle;
- zeitliche Sensibilität;
- verteilte Regulation;
- architektonische Bescheidenheit.

Kybernetische Ansätze ersetzen
weder Ethik noch Recht.
Sie machen sie **funktionsfähig**.

Dieses Dokument liefert den Kontext
für die in diesem Repository
präsentierten Protokolle und Architekturen.
