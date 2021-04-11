logs = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a = line.replace('"', '').split(sep=' ', maxsplit=7)
        logs.append((a[0], a[5], a[6]))

logs_unique = list(set(logs))

suspicious_user = 100
for a in logs_unique:
    number_of_connections = logs.count(a)
    if number_of_connections > suspicious_user:
        print(a, ": ", number_of_connections)
