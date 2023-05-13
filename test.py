with open('data.txt', encoding='utf-8') as file:
    print('Input file contains:')
    letters = 0
    text = (file.read().strip('\n').split())
    for w in text:
        for l in w:
            if l.isalpha():
                letters += 1
    print(letters, 'letters')

    file.seek(0)

    word = len(file.read().split())
    print(word, 'words')

    file.seek(0)

    sentense = len(file.readlines())
    print(sentense, 'lines')