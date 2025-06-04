import subprocess
from datetime import datetime, timedelta

# Получаем историю коммитов (дата автора + email)
cmd = ['C:\\Program Files\\Git\\bin\\git.exe', 'log', '--format=%aI %ae %s']
result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, encoding='utf-8')
lines = result.stdout.strip().split('\n')

# Текущая дата и дата год назад
now = datetime.now()
year_ago = now - timedelta(days=365)

print("Проверка коммитов:\n")

for line in lines:
    if not line.strip():
        continue

    # Парсим дату и email
    parts = line.strip().split(' ')
    commit_date_str = parts[0]  # ISO-формат даты: 2023-10-15T12:30:00
    commit_email = parts[1]
    commit_message = ' '.join(parts[2:])  # Сообщение может содержать пробелы

    # Преобразуем дату в объект datetime
    commit_date = datetime.fromisoformat(commit_date_str)

    # Убираем информацию о временной зоне
    commit_date = commit_date.replace(tzinfo=None)

    # Проверяем диапазон дат
    if year_ago <= commit_date <= now:
        status = "[✅] Будет отображён"
    else:
        status = "[❌] Не будет отображён"

    print(f"{status} | {commit_date.date()} | Email: {commit_email} | Комментарий: {commit_message}")
