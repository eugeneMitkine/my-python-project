from datetime import datetime ## Для получения текущей даты и времени


name = str(input('как вас зовут? '))
birth_year = int(input('в каком году вы родились? '))

current_year = datetime.now().year #текущий год
age = current_year - birth_year # Вычисляем возраст


print('привет ', name + '!')
print(f'вам {[age]} лет')