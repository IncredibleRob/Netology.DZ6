i = 0
purchases = {}
with open('Downloads/purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        log = json.loads(line)
        key = log['user_id']
        value = log['category']
        purchases[key] = value
        i += 1
        if i > 2: #для проверки 6 строк смотрим
            break
print(purchases)
