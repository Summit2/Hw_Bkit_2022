1#
#from readline import append_history_file
import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        
    # Переводим строку в действительное число
        
        while True:

            try:

                coef = float(input())
                break
            except:
                print("Преобразование во float не прошло, повторите ввод:")
                


        

    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    print('Уравнение типа Ax^4+Bx^2+C=0')
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    bi_roots=get_bi_roots(roots)
    # Вывод корней
    # print(len(bi_roots))

    # for i in bi_roots:
    #     print(i)
    len_bi_roots=len(bi_roots)

    if len_bi_roots == 0:
        print('Нет корней')
    
    elif len_bi_roots == 2:
        print('Два корня: {} и {}'.format(bi_roots[0], bi_roots[1]))
    

    elif len_bi_roots == 4:
        print('Четыре корня: {} и {},{} и {}'.format(bi_roots[0], bi_roots[1],bi_roots[2],bi_roots[3]))
    

def get_bi_roots(roots):
    '''
    Вычисляем корни биквадратного уравения, входные данные типа list
    '''
    result=[]
    for i in roots:
        if i>0.0:
            result.append((-1)*i**(1/2))
            result.append(i**(1/2))
    
    return result
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
