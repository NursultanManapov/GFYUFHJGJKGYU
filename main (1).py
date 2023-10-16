# Задание 1
a = int(input())  
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Простое")
else:
    print("Не простое")

# Задание 2
a = float(input())
b = float(input())
c = float(input())

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
    
print (a, "<", b, "<", c)

# Задание 3
def hight(number, n):
    return max(number);
 
if __name__ == '__main__':
    number = [230, 228, 47, 46, 227]
    n = len(number)
    print(hight(number, n))
    
# Задание 4
def fib(n):
    if n <= 0:
        return 
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

n = int(input())
result = fib(n)
print(f"Число Фибоначчи {n} равняется {result}")

# Задание 5
b = ['aidarloh', 'aidar', 'andreymolodec', 'alexander', 'uwu', 'islam', 'sas', 'hoho', 'gg']
di = {}
for word in b:
    if word in di.keys():
        di[word] += 1
    else:
        di[word] = 1
key = max(di, key=di.get)
print(key, di[key])