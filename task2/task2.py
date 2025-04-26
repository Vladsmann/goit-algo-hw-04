from pathlib import Path

def get_cats_info():
    try:
        current_dir = Path(__file__).parent
        file_path = current_dir / 'cats_file.txt'
        
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

cats_info = get_cats_info()
print(cats_info)