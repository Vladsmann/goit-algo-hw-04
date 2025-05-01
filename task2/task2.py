from pathlib import Path

def get_cats_info(path):
    try:
        file_path = Path(path)
        cats = []

        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    continue  
                cat_id, name, age = parts
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print(f"Файл cats_file.txt не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

if __name__ == "__main__":
    path = Path(__file__).parent / 'cats_file.txt'
    cats_info = get_cats_info(path)
    cats_str = "[\n" + ",\n".join(str(cat) for cat in cats_info) + "\n]"
    print(cats_str)