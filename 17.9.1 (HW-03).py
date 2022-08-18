def str_to_list(param):
    result = param.split()
    for i in range(len(result)):
        result[i] = type_correct(result[i])
    return result
def type_correct(param):
    x = param
    try:
        y = int(x)
        return y
    except ValueError:
        print('Не верно. Вы ввели', x, 'Введите число!')
        y = input()
        return type_correct(y)
def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array
def binary_search(array, element, left, right):
    if left > right:
        print('Число вне диапазона')
        return False
    middle = (right + left) // 2
    try:
        if array[middle] < element <= array[middle + 1]:
            print('Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу', (middle+1))
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        print('Число вне диапазона')
        return False


st = input('Введите числа через пробел: ')
co = input('Введите контрольное число: ')
co = type_correct(co)
st = sort(str_to_list(st))
binary_search(st, co, 0, len(st))
print("Список: \n", st)