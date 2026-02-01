import os
import re
from datetime import datetime

class AgentSelfOptimizer:
    def __init__(self, archive_dir):
        self.archive_dir = archive_dir
        self.archive_file = os.path.join(archive_dir, "0000-agent--archive.md")
        self.lessons_file = os.path.join(archive_dir, "LESSONS_LEARNED.md")
        self.report_file = os.path.join(archive_dir, "OPTIMIZATION_REPORT.md")

    def ensure_lessons_file(self):
        """Создает файл уроков, если он не существует."""
        if not os.path.exists(self.lessons_file):
            with open(self.lessons_file, "w", encoding="utf-8") as f:
                f.write("# Журнал Уроков и Ошибок (Self-Learning Database)\n\n")
                f.write("Этот файл используется скриптом для автоматического улучшения архива.\n\n")
                f.write("## Недавние инциденты\n")
                f.write("- [Пример] 2026-02-01: Агент выбрал Python для задачи реального времени, что привело к задержке. Рекомендация: обновить модуль Stack Selection.\n")

    def analyze_archive(self):
        """Анализирует архив на наличие дубликатов и структуры."""
        print(f"[*] Анализ архива в {self.archive_dir}...")
        files = [f for f in os.listdir(self.archive_dir) if f.endswith(".md") and f != "0000-agent--archive.md"]
        
        report_content = [f"# ОТЧЕТ ПО ОПТИМИЗАЦИИ СИСТЕМЫ ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n"]
        report_content.append("## 🔍 1. Инвентаризация модулей")
        for f in files:
            report_content.append(f"*   **{f}**: Обнаружен и проиндексирован.")

        report_content.append("\n## 🧠 2. Анализ уроков (Self-Enhancement)")
        if os.path.exists(self.lessons_file):
            with open(self.lessons_file, "r", encoding="utf-8") as f:
                lessons = f.readlines()
                new_lessons = [l.strip() for l in lessons if l.startswith("- ") and "Пример" not in l]
                if new_lessons:
                    report_content.append(f"Найдено новых уроков: {len(new_lessons)}")
                    for l in new_lessons:
                        report_content.append(f"*   [КРИТИЧНО] Требуется интеграция: {l}")
                else:
                    report_content.append("Новых инцидентов не зафиксировано. Система стабильна.")

        report_content.append("\n## 🛠️ 3. Предлагаемые действия")
        report_content.append("1. **Синхронизация:** Проверьте, все ли новые .md файлы отражены в 0000-agent--archive.md.")
        report_content.append("2. **Очистка:** Удаление устаревших рекомендаций, если они противоречат новым урокам.")
        report_content.append("3. **Эволюция:** Если уроков > 5, инициируйте создание нового специализированного модуля.")

        with open(self.report_file, "w", encoding="utf-8") as f:
            f.write("\n".join(report_content))
        
        print(f"[+] Отчет создан: {self.report_file}")

    def run(self):
        self.ensure_lessons_file()
        self.analyze_archive()
        print("\n--- СЛЕДУЮЩИЙ ШАГ ---")
        print("Скопируйте содержимое OPTIMIZATION_REPORT.md и отправьте агенту с командой:")
        print("'Оптимизируй архив на основе этого отчета'.")

if __name__ == "__main__":
    archive_path = os.path.dirname(os.path.abspath(__file__))
    optimizer = AgentSelfOptimizer(archive_path)
    optimizer.run()
