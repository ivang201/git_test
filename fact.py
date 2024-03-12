x = int(input())
y = ''
while x > 0:
    y = str(x % 2) + y
    x = x // 2
 
print(y)