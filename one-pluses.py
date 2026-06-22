t = int(input())
for i in range(t):
    num =  sorted(map(int , input().split()))
    for i in range(5):
        num[0] +=  1
        num.sort()
    ans = num[0] * num[1] * num[2]
    print(ans)