from ursina import *

app = Ursina()

def test_func(item, x=None, y=None):
    print(item, x, y)

test_func('test')
invoke(test_func, 'test', delay=.1)
invoke(test_func, 'test1', 1, 2, delay=.2)
invoke(test_func, 'test2', x=1, y=2, delay=.3)

def input(key):
    if key == 'space':
        print_on_screen('debug message', position=(0,0), origin=(0,0), scale=2)


app.run()