# 📊 Log Analyzer CLI

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**Auteur**: [VOTRE NOM COMPLET]  
**Version**: 1.0.0  
**Date**: Janvier 2025  
**Contexte**: Projet DevOps - Analyse automatique de logs

---

## 📋 Description

Outil CLI professionnel pour analyser automatiquement les fichiers journaux générés par des serveurs. Le programme effectue une analyse statistique complète et génère des rapports détaillés avec des combinaisons de numéros aléatoires.

### 🎯 Fonctionnalités principales

- ✅ **Lecture automatique** des fichiers `log.txt`
- ✅ **Comptage intelligent** des ERROR, WARNING, INFO
- ✅ **Génération de rapport** détaillé au format `rapport.txt`
- ✅ **Numéros aléatoires** : loterie, simples, hexadécimaux, combinaisons
- ✅ **Affichage coloré** pour une meilleure lisibilité
- ✅ **Gestion d'erreurs** robuste avec codes de sortie appropriés
- ✅ **Compatible CI/CD** avec condition d'échec configurable

---

## 🚀 Installation et Usage

### Prérequis
```bash
Python 3.7 ou supérieur
Aucune dépendance externe requise
Installation
bash# Clonage du repository
git clone https://github.com/[VOTRE-USERNAME]/log-analyzer
cd log-analyzer

# Rendre le script exécutable (Linux/Mac)
chmod +x log_analyzer.py
Utilisation basique
bash# Analyse avec fichier log.txt (défaut)
python log_analyzer.py

# Analyse avec fichier personnalisé  
python log_analyzer.py mon_fichier.log

# Exécution directe (Linux/Mac)
./log_analyzer.py

📊 Exemple de sortie
==================================================
🚀 LOG ANALYZER CLI - DÉMARRAGE
==================================================
📝 Génération du fichier log d'exemple...
✅ Fichier log.txt généré avec 25 entrées
🔍 Analyse du fichier log.txt...
📊 Statistiques calculées:
   ERROR: 3
   WARNING: 7
   INFO: 15
🎲 Génération de numéros aléatoires...
✅ Numéros générés avec succès
📄 Génération du rapport...
✅ Rapport généré: rapport.txt
==================================================
✅ ANALYSE TERMINÉE AVEC SUCCÈS
==================================================

📁 Structure du projet
log-analyzer/
├── log_analyzer.py      # Script principal
├── README.md           # Documentation (ce fichier)
├── log.txt            # Fichier de logs (généré automatiquement)
├── rapport.txt        # Rapport d'analyse (sortie du programme)
└── .gitignore         # Fichiers Git à ignorer

🔧 Configuration
Condition d'échec Jenkins
Le script retourne un code d'erreur (exit 1) si :

Plus de 5 erreurs ERROR sont détectées
Erreur de lecture du fichier de logs
Erreur de génération du rapport

Personnalisation
Vous pouvez modifier les seuils dans la classe LogAnalyzer :
python# Ligne ~180 dans generate_report()
if self.stats['ERROR'] > 5:  # Changer le seuil ici

🔄 Intégration CI/CD
GitHub Actions
Le projet inclut un workflow automatique qui :

✅ Teste le script à chaque push/PR
✅ Vérifie la génération du rapport
✅ Archive les artefacts

Jenkins
Compatible avec :

✅ Jobs Freestyle
✅ Pipelines scriptés (Jenkinsfile)
✅ Déclencheurs programmés
✅ Builds conditionnels


🧪 Tests
Test local
bashpython log_analyzer.py
echo $?  # Doit retourner 0 en cas de succès
Test avec condition d'échec
Modifiez temporairement le seuil ou ajoutez plus d'erreurs dans le fichier log pour tester la condition d'échec.

🤝 Contribution

Fork le projet
Créer une branche feature (git checkout -b feature/AmazingFeature)
Commit les changements (git commit -m 'Add some AmazingFeature')
Push vers la branche (git push origin feature/AmazingFeature)
Ouvrir une Pull Request


📝 Changelog
Version 1.0.0 (Janvier 2025)

✅ Première version stable
✅ Analyse de logs avec statistiques
✅ Génération de numéros aléatoires
✅ Interface colorée
✅ Compatible CI/CD


📄 License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

👨‍💻 Auteur
[VOTRE NOM]

GitHub: @BhlHk
Email: bahyoul.amine@gmail.com
Projet DevOps -  May 2025


🔗 Liens utiles

Documentation Python
Guide Git
Jenkins Documentation
GitHub Actions