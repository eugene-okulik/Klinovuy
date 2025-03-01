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
    words = line_text.split()
    found_index = words.index(args.text)
    start_index = max(0, found_index - 5)
    end_index = min(len(words), found_index + 6)
    words_before = words[start_index:found_index]
    words_after = words[found_index:end_index]
    new_str1 = ("..." if start_index > 0 else "") + ' '.join(words_before)
    new_str2 = ' '.join(words_after) + ("..." if end_index < len(words) else "")
    print(f"Найдено в строке {line_number}: {new_str1} {new_str2}")
