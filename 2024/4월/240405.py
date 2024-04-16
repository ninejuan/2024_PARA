def printf(a):
    print(a)
import random

tp: tuple = (i+1 for i in range(0, 5))
# tp[0] = 3
_dict = {'name': 'chaeho'}

srihs = {
    'name':'hello',
    'age':'world',
    'principle': 'park',
    'club': 'ily para'
}
printf(srihs['name'])

# 삼항연산자
printf("cham") if True else printf("false")

li = [i for i in range(0, random.randint(1, 100))]
if 47 in li:
    print('good')
else:
    print('bad')
    
print(list(i for i in range(2, 20+1, 2)))

_srihs = 'sunrin'
moeum = ['a', 'e', 'i', 'o', 'u']
new_srihs = '';
for i in _srihs:
    if i in moeum: continue
    else: print(i, end=""); 
print()

li = [i+1 for i in range(0, 5)]
li_iter = iter(li) 

print('li_iter type : ', type(li_iter))
print('li_iter value : ', li_iter)

print(li_iter.__next__())
print(li_iter.__next__())
print(li_iter.__next__())
print(li_iter.__next__())
print(li_iter.__next__())
# print(li_iter.__next__())

def ichahamsu(x):
    return x**2

print(ichahamsu(2))

def talk(x):
    if x == "안녕":
        return "잘가"
print(talk("안녕"))

def gugudan(n: int):
    if (n > 2 or n < 9):
        for i in range(1, 10):
            printf(f"{n} * {i} = {n*i}")
    else:
        printf("오류");


gugudan(3);