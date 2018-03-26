a=int(input("enter your  input 1"))
b=int(input("enter your input 2"))
for i in range (a,b+1):
  sum = 0
  temp=i
  while temp>0:
    digit = temp % 10
    sum = sum+digit ** 3
    temp =temp// 10
  if(i==sum):
    print(i)
