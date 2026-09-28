"""
Программа 2 (worker2), вариант 3.

Ищет наименьшее число из файла /var/data/data.txt и сохраняет его
третью степень (куб) в /var/result/result.txt.

Результат дополнительно выводится на экран (требование задания).
"""

import os

DATA_DIR = "/var/data"
RESULT_DIR = "/var/result"
INPUT_FILE = os.path.join(DATA_DIR, "data.txt")
OUTPUT_FILE = os.path.join(RESULT_DIR, "result.txt")


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as fh:
        nums = [int(x) for x in fh.read().split() if x.strip()]

    if not nums:
        print("worker2: файл data.txt пуст, чисел не найдено.")
        return

    minimum = min(nums)
    cube = minimum ** 3

    os.makedirs(RESULT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(str(cube) + "\n")

    print(f"worker2: наименьшее число = {minimum}, куб = {cube}")


if __name__ == "__main__":
    main()
