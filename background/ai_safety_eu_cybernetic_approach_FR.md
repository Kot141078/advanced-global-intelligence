# Sécurité de l’IA et limites de la régulation  
## Une approche cybernétique de la gestion des risques dans le contexte européen

**Auteur :** Ivan Kotov (Bruxelles)  
**Type de document :** Document de contexte / Analyse de fond  
**Statut :** Recherche publique  
**Date :** 2026-01-02

---

## 0. Objet du présent document

Ce document fournit une analyse de contexte et une justification conceptuelle
des travaux architecturaux et protocolaires présentés ailleurs
dans ce dépôt.

Il vise à :
- expliquer pourquoi les approches actuelles de la sécurité de l’IA sont insuffisantes ;
- mettre en évidence les lacunes structurelles des cadres réglementaires européens ;
- motiver la nécessité de solutions cybernétiques au niveau architectural.

Ce document **n’est pas** une spécification de protocole
et **n’est pas** une proposition juridique.
Il constitue une base analytique et contextuelle.

---

## 1. Problème central : sécurité sans contrôle

Le discours dominant sur la sécurité de l’IA se concentre principalement sur :
- l’alignement des modèles,
- le filtrage des contenus,
- les contraintes au moment de l’entraînement,
- la modération a posteriori.

Ces approches supposent que :
- les systèmes d’IA sont déployés de manière centralisée ;
- le comportement est médié par un fournisseur ;
- le risque peut être géré à l’intérieur du modèle.

Cette hypothèse n’est plus valide.

Les systèmes d’IA modernes sont de plus en plus :
- distribués,
- agentiques,
- persistants dans le temps,
- capables d’actions indirectes.

Des mécanismes de sécurité limités à l’intérieur du modèle
ne peuvent pas gouverner efficacement de tels systèmes.

---

## 2. Le « Provider Gap »

Une faiblesse structurelle majeure de la gouvernance actuelle de l’IA
réside dans ce que l’on peut appeler le **Provider Gap**.

### 2.1 Définition

Le Provider Gap apparaît lorsque :
- la responsabilité est formellement attribuée à un fournisseur,
- mais le contrôle effectif du comportement n’est plus centralisé.

Dans des systèmes distribués et agentiques :
- les modèles peuvent être ouverts ou répliqués ;
- les agents peuvent opérer à travers plusieurs juridictions ;
- le comportement émerge de l’interaction, et non de l’instruction.

L’entité tenue pour responsable
n’est plus l’entité qui exerce le contrôle.

---

## 3. Risques temporels et agentiques

Les risques liés à l’IA sont souvent modélisés
comme des propriétés statiques des sorties.
Cela ignore **le temps** comme dimension critique.

### 3.1 Agents temporels

Un agent temporel se caractérise par :
- un état interne persistant ;
- une mémoire entre les interactions ;
- une évolution des objectifs dans le temps.

Le risque n’émerge pas d’une réponse isolée,
mais de **trajectoires comportementales**.

### 3.2 Dynamiques multi-agents émergentes

Lorsque plusieurs agents interagissent :
- des effets de coordination apparaissent ;
- des coalitions peuvent se former ;
- des boucles de rétroaction amplifient les comportements.

Ces dynamiques ne peuvent être ni prédites de manière fiable,
ni contraintes par des politiques appliquées modèle par modèle.

---

## 4. Pourquoi l’alignement seul est insuffisant

Les techniques d’alignement (par ex. RLHF) :
- façonnent les distributions de réponses ;
- réduisent certains usages abusifs évidents ;
- améliorent la conformité à court terme.

Cependant, l’alignement :
- opère à l’intérieur du modèle ;
- suppose un contexte de déploiement fixe ;
- n’aborde pas les interactions inter-agents.

L’alignement ne constitue pas un contrôle.
Il constitue une **conditionnement**.

---

## 5. La cybernétique comme cadre alternatif

La cybernétique offre une perspective différente :
- les systèmes sont définis par des boucles de rétroaction ;
- la stabilité résulte de la régulation, non de l’intention ;
- le contrôle doit correspondre à la complexité du système.

### 5.1 Loi de la variété requise (Ashby)

Un régulateur doit posséder
au moins autant de variété
que le système qu’il cherche à contrôler.

Les systèmes d’IA distribués
dépassent la variété des régulateurs centralisés.

La régulation doit donc être :
- distribuée ;
- multi-niveaux ;
- adaptative.

---

## 6. Boucles de contrôle externes et contraintes internes

Une sécurité effective nécessite des **boucles de contrôle externes** :
- observation du comportement dans le temps ;
- application de limites indépendantes du modèle ;
- capacité de dégradation contrôlée plutôt que d’escalade.

Les contraintes internes (filtres, prompts)
ne peuvent pas remplir seules ce rôle.

Cette distinction est essentielle :
- l’éthique décrit l’intention ;
- le droit décrit la permission ;
- la cybernétique décrit la stabilité.

---

## 7. Lacunes d’identité et d’attribution

Un autre problème non résolu concerne **l’identité**.

Dans les systèmes d’IA distribués :
- les agents peuvent être clonés ;
- modifiés ;
- forkés ;
- redéployés.

Sans mécanismes d’identité robustes :
- l’attribution échoue ;
- la responsabilité s’effondre ;
- la confiance ne peut être établie.

L’identité doit être :
- fondée cryptographiquement ;
- observable comportementalement ;
- indépendante des fournisseurs.

---

## 8. Limites de la régulation dans le contexte de l’UE

L’AI Act de l’UE constitue une avancée majeure,
mais il reste centré sur :
- la classification des systèmes ;
- les obligations des fournisseurs ;
- la conformité au moment du déploiement.

Il ne traite pas pleinement :
- les comportements émergents des agents ;
- l’évolution post-déploiement ;
- les interactions transfrontalières ;
- le contrôle décentralisé.

Il ne s’agit pas d’un défaut d’intention,
mais d’une limite de périmètre.

---

## 9. Nécessité d’une sécurité architecturale

La conclusion n’est pas que la régulation est inutile,
mais qu’elle est insuffisante à elle seule.

La sécurité doit être intégrée :
- dans l’architecture des systèmes ;
- dans la topologie des interactions ;
- dans les contraintes de ressources ;
- dans des boucles de rétroaction externes.

Cela requiert des protocoles et des architectures
opérant **en dessous des politiques**
et **au-dessus des détails d’implémentation**.

---

## 10. Lien avec les autres documents du dépôt

Cette analyse de contexte motive :

- les **documents protocolaires**  
  définissant des contraintes et des frontières cybernétiques
  (voir `protocols/`) ;

- les **documents architecturaux**  
  proposant des conceptions concrètes
  mettant en œuvre ces principes
  (voir `architecture/`).

En particulier, les conflits entre les systèmes
et les contraintes objectives du monde réel
sont traités au niveau protocolaire
comme la **Reality Boundary Layer (L4)**.

---

## 11. Conclusion

La sécurité de l’IA ne peut être réduite à :
- de meilleurs prompts ;
- de meilleurs jeux de données ;
- de meilleures intentions.

Elle exige :
- un contrôle structurel ;
- une conscience temporelle ;
- une régulation distribuée ;
- une humilité architecturale.

Les approches cybernétiques ne remplacent
ni l’éthique ni le droit.
Elles les rendent **opérationnels**.

Ce document constitue le contexte
des protocoles et architectures
présentés dans ce dépôt.
