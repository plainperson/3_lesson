name = input('Введите ваше имя')
surname = input('Введите вашу фамилию')
age = int(input('Введите ваш год рождения'))
city = input('ВВедите ваш город проживания')
email = input('Введите ваш почтовый адрес')
phone_number = int(input('ВВедите ваш номер телефона'))

def my_func(**personal_data):
    return personal_data

print(my_func(el_1=name, el_2=surname, el_3=age, el_4=city, el_5=email, el_6=phone_number))


