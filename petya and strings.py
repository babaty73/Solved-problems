#codeforces problem 112A
list1 = input().lower()
list2 = input().lower()

for a, b in zip(list1, list2):
    if a < b:
        print("-1")
        break
    elif a > b:
        print("1")
        break
else:
    print("0")
        