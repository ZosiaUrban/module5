def num(x):
    if x <= 1:
      return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
number=int(input("Enter a number: "))

if num(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")