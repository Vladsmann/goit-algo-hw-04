from pathlib import Path

def total_salary():
    current_dir = Path(__file__).parent
    file_path = current_dir / 'salary_file.txt'

    try:
        with file_path.open('r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    continue
                name, salary_str = parts
                try:
                    salary = float(salary_str)
                    salaries.append(salary)
                except ValueError:
                    continue

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)

    except FileNotFoundError:
        print(f"Файл salary_file.txt не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

total, average = total_salary()
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
