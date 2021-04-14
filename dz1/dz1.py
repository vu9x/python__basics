import os

with open('starter.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cleared_line = line.strip('|- \n\r')
        if line.startswith('|--'):
            os.mkdir(cleared_line)
            root_dir = os.path.abspath(cleared_line)
            print(root_dir)
        elif line.startswith('   |--'):
            os.mkdir(os.path.join(root_dir, cleared_line))
