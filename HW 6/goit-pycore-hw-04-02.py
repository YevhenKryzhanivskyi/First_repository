def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    continue  # пропускаємо рядки з некоректною кількістю елементів
                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})
    except (FileNotFoundError, IOError) as e:
        print(f"Помилка при відкритті файлу: {e}")
    return cats
cats_info = get_cats_info("cats_file.txt")
print(cats_info)