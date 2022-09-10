num_1 = int(input('ВВедите число 1'))
num_2 = int(input('ВВедите число 2'))

def divide(num_1, num_2):
        return num_1 / num_2

if num_2 == 0:
        print('На ноль делить нельзя, введите другое число')
        num_2 = int(input('ВВедите число 2'))

print(divide(num_1, num_2))