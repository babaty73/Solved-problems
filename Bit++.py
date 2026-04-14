#codeforce problem 282 A
n = int(input())
x = 0
for i in range(n):
    k = input()
    if "++" in k:
        x += 1
    else:
        x -= 1
print(x)