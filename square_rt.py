print("***---SQUARE ROOT FINDER---***\n")
import math
num = int(input("Enter the number:\n"))
print('\n')
#BY USING MATH MODULE
print("From Math Module")
print(f"Square root is {math.sqrt(num)}\n\n")

#BY USING ARITHMETIC OPERATOR
print("BY USING ARITHMETIC OPERATOR")
print(f"Square root is {num**(0.5)}\n\n")


#USING PRIME FACTORS
print("BY USING PRIME FACTORS")
def prime_num(num):
    prime_num_list = []
    for i in range(2,int(num/2)):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            prime_num_list.append(i)
    return prime_num_list

pn = prime_num(num)
prime_factor_list = []
for i in pn:
    if num%i == 0:
        prime_factor_list.append(i)
    
print(f"Prime Factor Of The Given Number Is:\n")
print(prime_factor_list)
answer = 1
for i in prime_factor_list:
    count = 0
    while num%i==0:
        count+=1
        num=num//i
    for j in range(count//2):
        answer = answer*i
print(f"\n\nSquare Root is {answer}")


print("\n\nPress Enter To Exit The Program")
input("")