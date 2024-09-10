Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# data types
# numeric
# int, float, complex, bool
num = 2.5
typu(num)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    typu(num)
NameError: name 'typu' is not defined. Did you mean: 'type'?
type(num)
<class 'float'>
num = 5
type(num)
<class 'int'>
num = 6 + 9j
type(num)
<class 'complex'>
a = 5.6
b = int(a)
type(b)
<class 'int'>
b
5
# I have changed float to int
k = float(b)
k
5.0
#I have changed int to float
k = 6
c = complex(b,k)
c
(5+6j)
# I have changed normal number into a complex number by using complex function
#
b<k
True
bool = b < k
bool
True
type(bool)
<class 'bool'>
b > k
False
int(True)
1
int(False)
0
#bool type is in a numeric group because True is 1 and False is 0

# different types are Sequence: List, Tuple, Set, String and Range

lst = [25,36,45,12]
type(lst)
<class 'list'>

s = {25,36,35,15,12,25}
s
{35, 36, 25, 12, 15}
type(s)
<class 'set'>

t = (25,36,4,57,12)
typ(t)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    typ(t)
NameError: name 'typ' is not defined. Did you mean: 'type'?
>>> type(t)
<class 'tuple'>
>>> 
>>> str = "Jakub"
>>> st = 'a'
>>> type(st)
<class 'str'>
>>> type(str)
<class 'str'>
>>> #str is string
>>> 
>>> range(10)
range(0, 10)
>>> 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # I'm converting a range to a list
>>> 
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> #this is a range of even numbers from 1 to 10
>>> # it starts from to and ends on 10 and the difference is by 2
>>> type(range(10))
<class 'range'>
>>> 
>>> # another type is mapping = dictionary
>>> 
>>> d = {'Jakub':'IPhone','Tom':'Samsung','Mark':'Oneplus'}
>>> d
{'Jakub': 'IPhone', 'Tom': 'Samsung', 'Mark': 'Oneplus'}
>>> d.keys()
dict_keys(['Jakub', 'Tom', 'Mark'])
>>> d.values()
dict_values(['IPhone', 'Samsung', 'Oneplus'])
>>> d['Jakub']
'IPhone'
>>> d.get('Tom')
'Samsung'
>>> 
>>> # summarising: there are different data types, none, numeric: int, float, complex, bool;
>>> #sequence: list, tuple, set, string, range; and mapping: dictionary
>>> #int - whole numbers num = 5; float - 4.5; complex - num = 5+6j; bool - True or False;
>>> #list - lst = []; set - s = {}; t = (); string - str = "" or str = ''; range - rannge(10);
>>> #mapping/dictionary - d = {'':'','':'','':''}.
>>> 
>>> 
