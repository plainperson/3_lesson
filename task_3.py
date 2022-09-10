arg_1 = int(input('ВВедите аргумент 1'))
arg_2 = int(input('ВВедите аргумент 2'))
arg_3 = int(input('Введите аргумент 3'))

def my_func(arg_1, arg_2, arg_3):
    if arg_1 == min([arg_1, arg_2, arg_3]):
        return arg_2 + arg_3
    elif arg_2 == min([arg_1, arg_2, arg_3]):
        return arg_1 + arg_3
    elif arg_3 == min([arg_1, arg_2, arg_3]):
        return arg_1 + arg_2

print(my_func(arg_1, arg_2, arg_3))





