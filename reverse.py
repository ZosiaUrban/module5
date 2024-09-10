x=[]

for _ in range (100):
    i=input("enter a number or press eneter to quit")

    if i == "":
      print("quiting")
      break

    try:
        num=int(i)
        x.append(num)
    except ValueError:
        print("invalid input")

x.sort(reverse=True)
print(x[:5])