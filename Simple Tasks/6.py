'''
Выведите на консоль текущее время - час, минуту и секунду в следующем виде:
11 : 22 : 21
'''
from datetime import datetime
current_time = datetime.now()
print(current_time.hour, ":", current_time.minute, ":", current_time.second)

'''
Выведите на консоль текущую дату - день, месяц и год в следующем виде:
День:  16
Месяц:  1
Год:  2024
'''
temp_date = datetime.now()
# вывод даты
print("День: ", temp_date.day)
print("Месяц: ", temp_date.month)
print("Год: ", temp_date.year)