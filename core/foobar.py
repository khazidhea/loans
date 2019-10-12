def foobar(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FooBar'
    elif n % 3 == 0:
        return 'Foo'
    elif n % 5 == 0:
        return 'Bar'
    else:
        return str(n)


def division(a, b):
    return a / b


def positive(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
    return result

