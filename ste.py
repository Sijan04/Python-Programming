num1={1,2,3,90,5}
num2=set([80,90,100])
num2.add(200)
print(num2)
print(80 in num2)
print(num1 | num2) #union
print(num1 & num2) #intersection