"""
Программа 1 (worker1), вариант 3.

Формирует файл /var/result/data.txt из первых строк всех файлов
каталога /var/data.

Каждая первая строка каждого файла записывается в выходной файл
отдельной строкой.
"""

import os

DATA_DIR = "/var/data"
RESULT_DIR = "/var/result"
OUTPUT_FILE = os.path.join(RESULT_DIR, "data.txt")


def main():
    os.makedirs(RESULT_DIR, exist_ok=True)

    # Собираем все файлы (не каталоги) из /var/data
    files = sorted(
        f for f in os.listdir(DATA_DIR)
        if os.path.isfile(os.path.join(DATA_DIR, f))
    )

    lines = []
    for name in files:
        path = os.path.join(DATA_DIR, name)
        with open(path, "r", encoding="utf-8") as fh:
            first_line = fh.readline().rstrip("\n").rstrip("\r")
        lines.append(first_line)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(lines) + "\n")

    print(f"worker1: записано {len(lines)} первых строк в {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
