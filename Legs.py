#codeforce problem 1996 A
t = int(input())
for i in range(t):
    n = int(input())
    max_cows = n // 4
    remaining_legs = n - (max_cows * 4)
    chickens = remaining_legs // 2
    total_animals = max_cows + chickens
    print(total_animals)
    