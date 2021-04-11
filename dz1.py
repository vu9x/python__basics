logs = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a = line.replace('"', '').split(sep=' ', maxsplit=7)
        logs.append((a[0], a[5], a[6]))

print(logs)
