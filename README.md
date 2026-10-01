# 🧬 Projet de Bio‑Informatique  
### Analyse, traitement et exploration de données génomiques

## Présentation
Ce projet de bio‑informatique a été réalisé dans le cadre d’un module universitaire dédié à l’**analyse de données biologiques** et à l’**apprentissage des méthodes computationnelles appliquées au vivant**.  
Il regroupe une série de **TME (Travaux Mises en Main)** allant de l’exploration de séquences ADN à l’analyse statistique de données omiques, en passant par la manipulation d’outils bioinformatiques standards.

L’ensemble du projet est structuré en **notebooks Jupyter**, permettant une approche progressive, interactive et reproductible.

---

## 🎯 Objectifs pédagogiques
- Comprendre les bases de la **représentation des séquences biologiques** (ADN, ARN, protéines).  
- Manipuler des **fichiers biologiques standards** : FASTA, FASTQ, GFF, etc.  
- Implémenter des **algorithmes classiques** en bio‑informatique (alignement, scoring, recherche de motifs).  
- Explorer des **données génomiques réelles** via Python et bibliothèques scientifiques.  
- Développer une démarche d’analyse reproductible via Jupyter Notebook.  
- Introduire les concepts de **statistiques appliquées au vivant** et de **visualisation de données**.

---

## Contenu du projet
Le dépôt contient 8 TME, chacun couvrant une thématique clé :

### **TME1 — Introduction & manipulation de séquences**
- Représentation des séquences biologiques  
- Calculs simples : GC%, transcriptions, traductions  
- Premiers scripts Python pour manipuler l’ADN

### **TME2 — Formats biologiques & parsing**
- Lecture/écriture de fichiers FASTA & FASTQ  
- Extraction de métadonnées  
- Nettoyage et validation des séquences

### **TME3 — Alignement de séquences**
- Alignement global (Needleman–Wunsch)  
- Alignement local (Smith–Waterman)  
- Matrices de scoring (PAM, BLOSUM)  
- Implémentation et visualisation des résultats

### **TME4 — Recherche de motifs**
- Motifs consensus  
- Expressions régulières appliquées au génome  
- Détection de promoteurs / sites fonctionnels

### **TME5 — Analyse statistique**
- Distribution des nucléotides  
- Tests statistiques appliqués aux séquences  
- Introduction à la modélisation probabiliste (Markov, HMM)

### **TME6 — Données génomiques réelles**
- Manipulation de jeux de données publics (NCBI, Ensembl)  
- Extraction de régions génomiques  
- Annotation fonctionnelle

### **TME7 — Visualisation & interprétation**
- Graphiques biologiques (coverage, heatmaps, motifs)  
- Utilisation de Matplotlib / Seaborn  
- Analyse exploratoire

### **TME8 — Mini‑projet final**
- Analyse complète d’un jeu de données  
- Pipeline d’analyse reproductible  
- Interprétation biologique des résultats

---

## Technologies & outils
| Outil | Usage |
|-------|-------|
| **Python** | Traitement des données, algorithmes |
| **Jupyter Notebook** | Analyse interactive, reproductibilité |
| **Biopython** | Manipulation de séquences & formats |
| **NumPy / Pandas** | Analyse statistique |
| **Matplotlib / Seaborn** | Visualisation |
| **NCBI / Ensembl** | Sources de données biologiques |

---

## 📂 Structure du dépôt
```
Bio-Informatique/
│
├── TME1/
├── TME2/
├── TME3/
├── TME4/
├── TME5/
├── TME6/
├── TME7/
└── TME8/
```

Chaque dossier contient un ou plusieurs notebooks correspondant au TME associé.

---

## Installation & exécution
### 1. Cloner le dépôt
```bash
git clone https://github.com/KasselFelix/Bio-Informatique.git
cd Bio-Informatique
```

### 2. Créer un environnement Python
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

*(Si aucun fichier `requirements.txt` n’existe, installer Biopython et les libs scientifiques standard.)*

### 4. Lancer les notebooks
```bash
jupyter notebook
```

---

## 📖 Notes pédagogiques
Ce projet illustre une progression typique en bio‑informatique :  
partir de la manipulation de séquences simples pour aller vers l’analyse de données génomiques complexes.  
Il constitue une base solide pour des travaux plus avancés :  
- Analyse transcriptomique (RNA‑seq)  
- Métagénomique  
- Phylogénie  
- Machine learning appliqué au vivant  

---

## Auteur
Projet réalisé par **Kassel Felix** dans le cadre de l'UE bio‑informatique de Sorbonne Universite .  
Développement, analyses : **Python + Jupyter Notebook**.
