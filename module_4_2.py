def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() # вызов функции внутри test_function -  ничего не выводит

#inner_function() # вызов функции вне test_function -  ошибка

test_function() # выводит результат выполнения функций