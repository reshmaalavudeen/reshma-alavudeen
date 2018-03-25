r=int(input("Enter number: "))
if(r>1):
  for i in range(2,r):
    if(r%i==0):
      print("given number not is prime")
      break
    else:
      print("given number  prime number")
