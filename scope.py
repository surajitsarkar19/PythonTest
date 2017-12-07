def outer_function():
    #global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('inner a =', a)

    inner_function()
    print('outer a =', a)


a = 10
outer_function()
print('module a =', a)