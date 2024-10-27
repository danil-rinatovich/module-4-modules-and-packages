def test_function():
    comprehensive = 'Я в области видимости функции test_function'
    def inner_function():
        nonlocal comprehensive
        print(comprehensive)
    inner_function()

test_function()