import random
sum=0

i=int(input("Enter the number of dice you want to roll "))



for _ in range(i):
 dice=random.randint(1,6)
 sum+=dice
 print(sum)