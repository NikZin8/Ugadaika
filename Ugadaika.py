import random
num=random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if n in range(1,100):
        return True
    else:
        return False
print('Введите число от 1 до 100')
n=int(input())
counter=0
while n!=num:
    if is_valid(n)==False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if is_valid(n)==True:
        n=int(n)
    if n<num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        n=int(input())
        counter+=1
    if n>num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        n=int(input())
        counter+=1
    if n==num:
        print('Вы угадали с', counter, 'попытки, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

