>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words :
...     print(w, len(w))
...
>>> print('hello, world')
hello, world
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> a = 10
>>> b = 20
>>> c = a + b
>>> print(c)
30
>>> if a < b:
...     print("a is less than b")
...
a is less than b
>>> def greet(name):
...     return "Hello, " + name + "!"
...
>>> print(greet("Alice"))
Hello, Alice!
>>> class Dog:
...     def __init__(self, name):
...         self.name = name
...     def bark(self):