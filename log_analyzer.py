#!/usr/bin/env python3
"""
Log Analyzer CLI Tool
Auteur: Amine Bahyoul
Description: Analyse automatique de fichiers journaux
"""

import argparse
import random
import sys
from datetime import datetime


class LogAnalyzer:
    def __init__(self, log_file: str):
        self.log_file = log_file
        self.stats = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    def generate_sample_log(self):
        """Génère un fichier log d'exemple si le fichier n’existe pas."""
        log_entries = [
            "2024-01-15 10:30:15 INFO Application started successfully",
            "2024-01-15 10:31:22 WARNING Configuration file not optimized",
            "2024-01-15 10:32:10 ERROR Database connection failed",
            "2024-01-15 10:33:05 INFO User authentication successful",
            "2024-01-15 10:34:18 ERROR File not found: /tmp/data.txt",
            "2024-01-15 10:35:30 WARNING Memory usage at 85%",
            "2024-01-15 10:36:12 INFO Data processing completed",
            "2024-01-15 10:37:45 ERROR Network timeout occurred",
        ]

        # Ajout d'entrées aléatoires
        for _ in range(random.randint(5, 15)):
            h = random.randint(10, 23)
            m = random.randint(0, 59)
            s = random.randint(0, 59)
            level = random.choice(["INFO", "WARNING", "ERROR"])
            random_msg = f"Random log entry {random.randint(1000,9999)}"
            log_entries.append(f"2024-01-15 {h:02d}:{m:02d}:{s:02d} {level} {random_msg}")

        with open(self.log_file, "w", encoding="utf-8") as f:
            f.write("\n".join(log_entries))
        print(f"📝 Exemple de log généré dans `{self.log_file}`")

    def analyze_logs(self) -> bool:
        """Analyse le fichier de logs ligne par ligne."""
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                for line in f:
                    # Pour chaque ligne, on regarde si elle contient ERROR/WARNING/INFO
                    for level in self.stats:
                        if level in line:
                            self.stats[level] += 1
            return True
        except FileNotFoundError:
            print(f"❌ Fichier `{self.log_file}` non trouvé")
            return False

    def generate_report(self):
        """Génère le rapport d'analyse (`rapport.txt`)."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = sum(self.stats.values())

        report_lines = [
            "=== RAPPORT D'ANALYSE DES LOGS ===",
            f"Généré le         : {timestamp}",
            f"Fichier analysé   : {self.log_file}",
            "",
            "📊 STATISTIQUES:",
            f"- Erreurs (ERROR)       : {self.stats['ERROR']}",
            f"- Avertissements (WARNING): {self.stats['WARNING']}",
            f"- Informations (INFO)   : {self.stats['INFO']}",
            f"- Total des entrées     : {total}",
            "",
            "🎲 NUMÉROS GÉNÉRÉS ALÉATOIREMENT:",
            ", ".join(str(random.randint(1, 100)) for _ in range(10)),
            "",
            "=== FIN DU RAPPORT ===",
        ]
        report_content = "\n".join(report_lines)

        # On force l'encodage en UTF-8 pour éviter l'erreur "charmap codec"
        with open("rapport.txt", "w", encoding="utf-8") as f:
            f.write(report_content)

        print("✅ Rapport généré: `rapport.txt`")

        # Condition d'échec pour CI/CD si trop d'erreurs
        if self.stats["ERROR"] > 5:
            print(f"❌ ERREUR: Trop d'erreurs détectées ({self.stats['ERROR']} > 5)")
            sys.exit(1)

    def run(self):
        """Exécute l’analyse complète."""
        print("🔍 Démarrage de l’analyse des logs...")

        # Si le fichier n'existe pas, on génère un log d'exemple
        try:
            with open(self.log_file, "r", encoding="utf-8"):
                pass
        except FileNotFoundError:
            self.generate_sample_log()

        # Analyse et génération du rapport
        if self.analyze_logs():
            self.generate_report()
            print("✅ Analyse terminée avec succès!")
        else:
            sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Log Analyzer CLI Tool - Compte ERROR, WARNING, INFO dans un fichier log."
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default="log.txt",
        help="Chemin vers le fichier de log à analyser (par défaut `log.txt`)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    analyzer = LogAnalyzer(log_file=args.file)
    analyzer.run()
