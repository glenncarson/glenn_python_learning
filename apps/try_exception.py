def spam(a):
    try:
        42 / a
    except ZeroDivisionError:
        print('cannot divide by 0')
    except TypeError:
        print('int and string issue')
a = 0
spam(a)
a = 'a'
spam(a)