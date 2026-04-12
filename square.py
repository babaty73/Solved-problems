
#codeforce problem 2167 A
t =int(input())
for i in range(t):
    a ,b ,c , d = (map(int , input().split()))
    if a == b == c == d:
        print("YES")
    else:
        print("NO")    