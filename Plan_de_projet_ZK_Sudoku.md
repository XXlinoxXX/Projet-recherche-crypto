# Plan de gestion du projet
## Preuve à divulgation nulle de connaissance — Sudoku

*Projet de recherche en cryptographie • Équipe A, B, C, D*
**Deadline officielle : 8 décembre**

---

## Sommaire

1. [Objectif du document](#1-objectif-du-document)
2. [Périmètre du projet](#2-périmètre-du-projet)
3. [Principes d'organisation](#3-principes-dorganisation)
4. [Répartition des responsabilités principales](#4-répartition-des-responsabilités-principales)
5. [Work Breakdown Structure (WBS)](#5-work-breakdown-structure-wbs)
6. [Planning global](#6-planning-global)
7. [Planning détaillé par semaine](#7-planning-détaillé-par-semaine)
8. [Gantt synthétique](#8-gantt-synthétique)
9. [Jalons et critères de réussite](#9-jalons-et-critères-de-réussite)
10. [Méthode de travail et Git](#10-méthode-de-travail-et-git)
11. [Réunions et suivi](#11-réunions-et-suivi)
12. [Prochaine étape](#12-prochaine-étape)
13. [Journal des décisions et de l'avancement](#13-journal-des-décisions-et-de-lavancement)
14. [Notes libres](#14-notes-libres)

---

## 1. Objectif du document

Ce document centralise les décisions prises pour organiser le projet : objectifs, répartition des responsabilités, tâches, planning, jalons, méthode de travail, architecture envisagée et règles de collaboration.

Il doit être **mis à jour au fil de l'avancement** afin de conserver une trace du projet.

---

## 2. Périmètre du projet

Le projet porte sur l'implémentation en **Python** d'un protocole interactif simple de **preuve à divulgation nulle de connaissance (ZK)**, basé sur un Sudoku. Le prouveur doit convaincre le vérificateur qu'il connaît une solution valide **sans révéler cette solution**.

Le projet doit également étudier expérimentalement la diminution de la probabilité de succès d'un tricheur lorsque le nombre de tours augmente.

**Livrables et tâches attendus :**

- Implémenter un *prover* et un *verifier*.
- Utiliser des fonctions de hachage / engagements conformément au protocole retenu.
- Faire intervenir des défis aléatoires du vérificateur.
- Répéter le protocole sur plusieurs tours.
- Construire un scénario de triche et mesurer sa probabilité de succès.
- Analyser *completeness*, *soundness* et *zero-knowledge*.
- Comparer les résultats expérimentaux aux attentes théoriques.
- Produire un rapport et une démonstration finale.

---

## 3. Principes d'organisation

- Tout le monde touche à toutes les grandes parties du projet.
- Chaque tâche possède néanmoins un **responsable principal** clairement identifié.
- Le responsable pilote la tâche, mais les autres membres participent aux revues, tests, conception ou intégration.
- Les responsabilités principales ne constituent pas des spécialisations exclusives.
- Le code et les résultats importants doivent être relus par **au moins un autre membre**.
- Une réunion d'équipe hebdomadaire permet de suivre l'avancement et de débloquer les problèmes.
- La **deadline interne** de fin de projet est fixée au **30 novembre** ; la période du 1er au 8 décembre sert de marge de sécurité.

---

## 4. Répartition des responsabilités principales

| Membre | Responsabilité principale | Contributions attendues |
|:------:|---------------------------|-------------------------|
| **A** | Conception du protocole + théorie | Protocole Sudoku, propriétés cryptographiques, conception, revue du code et des résultats. |
| **B** | Architecture Python + implémentation | Structure du projet, prover/verifier, intégration, revue de la conception et des tests. |
| **C** | Tests + expérimentation + statistiques | Tests, tricheur, campagnes expérimentales, données, graphiques, analyse quantitative. |
| **D** | Documentation + rédaction + coordination | Planning, documentation, rapport, intégration, tests et préparation de la présentation. |

> **Règle de fonctionnement :** A, B, C et D doivent tous comprendre le protocole complet, le code principal et les résultats. Les rôles ci-dessus servent surtout à déterminer **qui est responsable** lorsque plusieurs personnes travaillent sur la même tâche.

---

## 5. Work Breakdown Structure (WBS)

### Lot 1 — Gestion du projet

- **L1.1** Organisation de l'équipe
- **L1.2** Gantt
- **L1.3** Répartition des tâches
- **L1.4** Suivi hebdomadaire
- **L1.5** Gestion Git
- **L1.6** Validation des jalons

### Lot 2 — Recherche cryptographique

- **L2.1** Comprendre les preuves ZK
- **L2.2** Comprendre prover / verifier
- **L2.3** Comprendre completeness
- **L2.4** Comprendre soundness
- **L2.5** Comprendre zero-knowledge
- **L2.6** Étudier le protocole Sudoku
- **L2.7** Étudier les engagements par hash
- **L2.8** Étudier les références du sujet

### Lot 3 — Conception du protocole

- **L3.1** Définir le secret du prover
- **L3.2** Définir l'engagement
- **L3.3** Définir le challenge du verifier
- **L3.4** Définir la réponse
- **L3.5** Définir la vérification
- **L3.6** Définir un tour complet
- **L3.7** Définir la répétition des tours
- **L3.8** Analyser la probabilité de triche
- **L3.9** Vérifier que rien ne révèle la solution

### Lot 4 — Architecture Python

- **L4.1** Architecture du projet
- **L4.2** Génération / chargement d'un Sudoku
- **L4.3** Représentation du Sudoku
- **L4.4** Gestion des permutations
- **L4.5** Fonction de hash
- **L4.6** Prover
- **L4.7** Verifier
- **L4.8** Génération du challenge
- **L4.9** Réponse au challenge
- **L4.10** Vérification
- **L4.11** Répétition automatique

### Lot 5 — Tests

- **L5.1** Tests du Sudoku
- **L5.2** Tests du hash
- **L5.3** Tests du prover
- **L5.4** Tests du verifier
- **L5.5** Tests d'acceptation
- **L5.6** Tests de rejet
- **L5.7** Tests de cas limites
- **L5.8** Tests d'un tricheur

### Lot 6 — Expérimentation

- **L6.1** Définir les expériences
- **L6.2** Définir le tricheur
- **L6.3** Tester 1 tour
- **L6.4** Tester 2 tours
- **L6.5** Tester 3 tours
- **L6.6** Continuer pour davantage de tours
- **L6.7** Répéter les expériences
- **L6.8** Collecter les résultats
- **L6.9** Générer les graphiques
- **L6.10** Comparer théorie / expérience

### Lot 7 — Analyse

- **L7.1** Pourquoi le protocole fonctionne
- **L7.2** Completeness
- **L7.3** Soundness
- **L7.4** Zero-knowledge
- **L7.5** Probabilité de triche
- **L7.6** Limites du protocole
- **L7.7** Limites de l'implémentation

### Lot 8 — Rapport / présentation

- **L8.1** Introduction
- **L8.2** État de l'art
- **L8.3** Explication du protocole
- **L8.4** Implémentation
- **L8.5** Expérimentation
- **L8.6** Résultats
- **L8.7** Analyse
- **L8.8** Conclusion
- **L8.9** Relecture
- **L8.10** Présentation / démonstration

---

## 6. Planning global

| Période | Phase | Objectif principal |
|---------|-------|--------------------|
| 7–11 oct. | Lancement | Comprendre le sujet et organiser l'équipe |
| 12–18 oct. | Recherche | Comprendre ZK, soundness et le protocole Sudoku |
| 19–25 oct. | Conception | Définir précisément le protocole |
| 26 oct.–1 nov. | Implémentation 1 | Première version du protocole |
| 2–8 nov. | Implémentation 2 | Version fonctionnelle complète |
| 9–15 nov. | Tests | Tests honnêtes et tests de triche |
| 16–22 nov. | Expérimentation | Mesurer la soundness expérimentalement |
| 23–29 nov. | Analyse + rédaction | Rapport et interprétation des résultats |
| 30 nov.–6 déc. | Finalisation | Relecture, corrections, présentation |
| 7–8 déc. | Marge de sécurité | Corrections de dernière minute et rendu |

---

## 7. Planning détaillé par semaine

### Semaine 1 — 7 → 11 octobre
**Lancement + compréhension**

- **A** : étudier les preuves ZK et le protocole Sudoku.
- **B** : étudier les engagements par hash et réfléchir à l'architecture Python.
- **C** : étudier completeness / soundness et préparer les futures expérimentations.
- **D** : mettre en place Git, structure du projet, planning et début du rapport.

🎯 **Jalon :** toute l'équipe doit pouvoir expliquer l'idée d'une preuve ZK appliquée au Sudoku.

### Semaine 2 — 12 → 18 octobre
**Comprendre précisément le protocole**

- **A** : formalisation du protocole Sudoku.
- **B** : proposition de l'architecture Python.
- **C** : analyse mathématique de la soundness.
- **D** : documentation du protocole et des références.

✅ **Validation collective :** secret, engagement, challenge, réponse, vérification, répétition.

### Semaine 3 — 19 → 25 octobre
**Conception finale**

- **A** : finaliser le protocole.
- **B** : implémenter les premières briques Python.
- **C** : préparer les tests théoriques et les expériences.
- **D** : commencer la rédaction et documenter le protocole.

🎯 **Jalon 1 — 25 octobre :** spécification complète du protocole validée par les quatre membres.

### Semaine 4 — 26 octobre → 1er novembre
**Développement V1**

- **A** : implémentation d'une partie du prover et contrôle de conformité.
- **B** : architecture et implémentation principale.
- **C** : écriture des tests.
- **D** : implémentation d'une partie du verifier et documentation.

**Objectif :** prover honnête → verifier honnête → `ACCEPT`.

### Semaine 5 — 2 → 8 novembre
**Développement V2**

Compléter : challenge aléatoire, hash, engagements, réponses, vérification et plusieurs tours.

- **A** : protocole + prover
- **B** : verifier + architecture
- **C** : tests automatisés
- **D** : intégration + documentation

🎯 **Jalon 2 — 8 novembre :** protocole Sudoku ZK automatisé et exécutable sur plusieurs tours.

### Semaine 6 — 9 → 15 novembre
**Tests + triche**

- **A** : rechercher des failles théoriques.
- **B** : corriger les problèmes d'implémentation.
- **C** : construire le tricheur.
- **D** : documenter les scénarios de test et résultats.

**Objectif :** essayer de casser le protocole avant l'expérimentation finale.

### Semaine 7 — 16 → 22 novembre
**Expérimentation**

Mesurer la probabilité de succès du tricheur en fonction du nombre de tours.

- **A** : analyse théorique
- **B** : automatisation
- **C** : statistiques + graphiques
- **D** : interprétation + rédaction

🎯 **Jalon 3 — 22 novembre :** données, résultats, graphiques et comparaison théorie / expérience disponibles.

### Semaine 8 — 23 → 29 novembre
**Analyse + rapport**

Répondre clairement à ces questions :

1. Pourquoi le protocole fonctionne-t-il ?
2. Pourquoi le tricheur est-il détecté ?
3. Pourquoi la solution n'est-elle pas révélée ?
4. Que montrent les expériences ?

Répartition :

- **A** : analyse cryptographique
- **B** : implémentation
- **C** : résultats
- **D** : assemblage du rapport

🎯 **Jalon 4 — 29 novembre :** version quasi finale du rapport.

### Semaine 9 — 30 novembre → 6 décembre
**Finalisation**

Corriger le code, nettoyer, vérifier les résultats, relire le rapport, vérifier les références, préparer la démonstration et la présentation.

🎯 **Jalon final interne — 6 décembre :** projet terminé techniquement.

### 7–8 décembre
**Marge de sécurité**

- Aucune nouvelle fonctionnalité importante.
- Réserver cette période aux corrections mineures, problèmes imprévus et dépôt final.

---

## 8. Gantt synthétique

| Tâches | 7–11 | 12–18 | 19–25 | 26–1 | 2–8 | 9–15 | 16–22 | 23–29 | 30–6 |
|--------|:----:|:-----:|:-----:|:----:|:---:|:----:|:-----:|:-----:|:----:|
| Organisation | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| Recherche ZK | ■ | ■ | ■ | | | | | | |
| Protocole Sudoku | ■ | ■ | ■ | V | | | | | |
| Architecture Python | | ■ | ■ | ■ | ■ | | | | |
| Implémentation | | | ■ | ■ | ■ | ■ | V | | |
| Tests | | | | ■ | ■ | ■ | ■ | | |
| Tricheur | | | | | | ■ | ■ | | |
| Expérimentation | | | | | | ■ | ■ | V | |
| Analyse | | ■ | ■ | | | ■ | ■ | ■ | ■ |
| Rapport | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| Présentation | | | | | | | | ■ | ■ |
| Corrections finales | | | | | | | | | ■ |

**Légende :** ■ = travail principal ; V = validation / jalon.

---

## 9. Jalons et critères de réussite

| Jalon | Date | Critère de réussite |
|:-----:|------|---------------------|
| **J1** | 18 oct. | Toute l'équipe comprend et sait expliquer le protocole envisagé. |
| **J2** | 25 oct. | Spécification complète du protocole Sudoku validée sur papier. |
| **J3** | 8 nov. | Version fonctionnelle : prover honnête → verifier honnête → `ACCEPT`, sur plusieurs tours. |
| **J4** | 22 nov. | Expérimentation terminée : tricheur, données, graphiques et comparaison théorie / expérience. |
| **J5** | 30 nov. | Projet techniquement terminé : code, analyse, expériences et rapport quasi finalisés. |
| **Final** | 8 déc. | Rendu officiel du projet. |

---

## 10. Méthode de travail et Git

### Organisation Python envisagée

```text
projet-zk-sudoku/
├── src/
│   ├── prover.py
│   ├── verifier.py
│   ├── sudoku.py
│   ├── commitment.py
│   └── protocol.py
├── tests/
│   ├── test_sudoku.py
│   ├── test_commitment.py
│   ├── test_prover.py
│   └── test_verifier.py
├── experiments/
│   ├── experiment.py
│   ├── results/
│   └── plots/
├── docs/
│   ├── protocole.md
│   └── references.md
├── report/
│   └── rapport.pdf
└── README.md
```

### Règles Git

- Ne pas développer directement sur `main`.
- Créer **une branche par fonctionnalité**, par exemple `feature/prover`, `feature/verifier`, `feature/tests`, `feature/experiments`.
- Faire relire les fonctionnalités importantes par un autre membre avant intégration.
- Commiter régulièrement avec des messages explicites.
- Conserver les résultats expérimentaux et les données brutes.

---

## 11. Réunions et suivi

- Une réunion d'équipe par semaine, idéalement 30 à 45 minutes.
- Chaque membre indique : **réalisé / en cours / blocages / prochaine tâche**.
- Le responsable de chaque tâche met à jour son état.
- Les décisions importantes sont ajoutées à ce document.
- Un problème bloquant doit être signalé rapidement, sans attendre la réunion suivante.

---

## 12. Prochaine étape

La prochaine étape technique recommandée est de **définir précisément le protocole ZK Sudoku** avant de développer les fonctionnalités principales.

Il faut formaliser :

- le secret du prover,
- la construction des engagements,
- le challenge aléatoire du verifier,
- la réponse du prover,
- la vérification,
- la répétition des tours,
- la probabilité de succès d'un tricheur.

Cette spécification servira ensuite directement de cahier des charges pour le code Python.

---

## 13. Journal des décisions et de l'avancement

| Date | Décision / action | Responsable | État | Commentaires |
|------|-------------------|:-----------:|:----:|--------------|
| 7 oct. | Choix du Sudoku comme problème ZK | Équipe | Fait | |
| 7 oct. | Choix de Python | Équipe | Fait | |
| 7 oct. | Deadline officielle : 8 décembre | Équipe | Fait | |
| 7 oct. | Organisation A/B/C/D avec polyvalence + responsabilité principale | Équipe | Fait | |
| | | | | |
| | | | | |
| | | | | |

---

## 14. Notes libres

<!-- Espace réservé pour les notes de l'équipe -->

