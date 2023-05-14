with open('class_scores.txt', 'r', encoding='utf-8') as file_in, open('new_scores.txt', 'w', encoding='utf-8') as file_out:
    for line in file_in:
        parts = line.strip().split()
        name, score = parts[0], parts[1]
        new_score = min(100, (int(score) + 5))
        file_out.write(name + ' ' + str(new_score) + '\n')