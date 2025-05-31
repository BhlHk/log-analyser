#!/usr/bin/env python3
"""
Log Analyzer CLI Tool avec couleurs dans la console
Auteur: Amine Bahyoul
Description: Analyse automatique de fichiers journaux avec sorties colorées
"""

import argparse
import random
import sys
from datetime import datetime

# Ajout de colorama pour gérer les couleurs dans la console
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    # Si colorama n'est pas installé, afficher un avertissement et poursuivre sans couleurs
    Fore = Style = type('', (), {'RED': '', 'YELLOW': '', 'GREEN': '', 'CYAN': '', 'RESET_ALL': ''})
    def init(**kwargs): pass
    print("⚠️  colorama non installé, l'affichage ne sera pas coloré. Pour ajouter les couleurs, installez colorama via 'pip install colorama'.")


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
        print(f"{Fore.GREEN}📝 Exemple de log généré dans `{self.log_file}`{Style.RESET_ALL}")

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
            print(f"{Fore.RED}❌ Fichier `{self.log_file}` non trouvé{Style.RESET_ALL}")
            return False

    def display_stats(self):
        """Affiche les statistiques avec couleurs."""
        print(f"{Fore.CYAN}\n📊 STATISTIQUES DE L'ANALYSE :{Style.RESET_ALL}")
        print(f"{Fore.RED}- Erreurs (ERROR)       : {self.stats['ERROR']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}- Avertissements (WARNING): {self.stats['WARNING']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}- Informations (INFO)   : {self.stats['INFO']}{Style.RESET_ALL}")
        total = sum(self.stats.values())
        print(f"{Fore.CYAN}- Total des entrées     : {total}{Style.RESET_ALL}\n")

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

        print(f"{Fore.GREEN}✅ Rapport généré: `rapport.txt`{Style.RESET_ALL}")

        # Condition d'échec pour CI/CD si trop d'erreurs
        if self.stats["ERROR"] > 5:
            print(f"{Fore.RED}❌ ERREUR: Trop d'erreurs détectées ({self.stats['ERROR']} > 5){Style.RESET_ALL}")
            sys.exit(1)

    def run(self):
        """Exécute l’analyse complète."""
        print(f"{Fore.CYAN}🔍 Démarrage de l’analyse des logs...{Style.RESET_ALL}")

        # Si le fichier n'existe pas, on génère un log d'exemple
        try:
            with open(self.log_file, "r", encoding="utf-8"):
                pass
        except FileNotFoundError:
            self.generate_sample_log()

        # Analyse et affichage des statistiques couleur
        if self.analyze_logs():
            self.display_stats()
            self.generate_report()
            print(f"{Fore.GREEN}✅ Analyse terminée avec succès!{Style.RESET_ALL}")
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
