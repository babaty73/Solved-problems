name = input("What is your name? ")
numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]

print(f"Hello, {name}!")
print("Numbers:", numbers)
print("Squares:", squares)

for i, square in enumerate(squares, start=1):
    print(f"{i}. {square}")

    