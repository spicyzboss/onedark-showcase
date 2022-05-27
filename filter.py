with open('./color.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    lines = set(lines)
    for line in lines:
        print(line)