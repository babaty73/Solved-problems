# codeforce problem B maximum multiple sum
t = int(input())
for i in range (t):
    n = int(input())
    best_sum = 0
    for x in range(2,n+1):
        current = x
        total = 0
        while current <= n:
               total += current
               current += x
        if total > best_sum :
            best_sum = total
            best_x = x

    print(best_x)        