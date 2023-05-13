# Функция для транслитерации символа
def transliterate_char(char):
    # Словарь для транслитерации
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': "'", 'э': 'je', 'ю': 'ju',
        'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Jo',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
        'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shh', 'Ъ': '*', 'Ы': 'Y', 'Ь': "'", 'Э': 'Je',
        'Ю': 'Ju', 'Я': 'Ya'
    }

    # Если символ кириллицы, то транслитерируем его
    if char in translit_dict:
        return translit_dict[char]
    # Иначе оставляем его без изменений
    else:
        return char


# Открываем файл на чтение
with open('cyrillic.txt', 'r', encoding='utf-8') as f:
    # Считываем текст из файла
    text = f.read()

# Транслитерируем каждый символ текста и записываем результат в файл
with open('transliteration.txt', 'w', encoding='utf-8') as f:
    for char in text:
        f.write(transliterate_char(char))
