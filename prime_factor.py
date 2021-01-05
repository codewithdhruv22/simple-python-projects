print("***---PRIME FACTOR FINDER---***\n")
num = int(input("Enter the number:\n"))

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
print("\n\nPress Enter To Exit The Program")
input("")