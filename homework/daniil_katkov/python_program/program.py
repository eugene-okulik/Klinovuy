import argparse
import glob


def search_log_file(file_path, search_text=None):
    for every_file in file_path:
        with open(every_file, encoding="utf-8") as file:
            name_file = file.name
            print(f'Название файла: {name_file}')
            for line_number, line in enumerate(file, start=1):
                line_text = line.strip()
                if search_text and search_text in line_text:
                    yield line_number, line_text


parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Укажите полный путь к файлам с логами")
parser.add_argument("--text", help="Укажите текст для поиска")
args = parser.parse_args()
all_files = glob.glob(f"{args.folder}/*")

for line_number, line_text in search_log_file(all_files, args.text):
    print(f"Найдено в строке {line_number}: {line_text}")
