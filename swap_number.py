print("**---Welcome To Adla Badli Program---**")
print("\n\n")
# Method No.1
# By Using Third Varibale 
def swap1 (num1, num2):
    #num1 = 18 num2 = 60
    temp_num = num1 #18
    num1 = num2 #60
    num2 = temp_num #18
    return f"First Vaibale Is Changed to {num1} and Second Number Is Changed To {num2}"

print("Swapping Number By Using Third Variable")
print(swap1(18,60))
print("\n\n")



#Method No.2
#By Using Arithmetic Operator
def swap2_1(num1,num2):
    #num1 = 20 ,num2 =8 
    num1 = num1+num2 #20 + 8 = 28
    num2 = num1 - num2 #28 - 8 = 20 = num1
    num1 = num1 - num2 #28 - 20 = 8 = num2
    return f"First Vaibale Is Changed to {num1} and Second Number Is Changed To {num2}"


def swap2_2(num1,num2):
    #num1 = 20 ,num2 =10
    num1 = num1 * num2 #20 * 10 = 200
    num2 = num1 / num2 #200 / 10 = 20 = num1
    num1 = num1 / num2 #200 / 20 = 10 = num2
    return f"First Vaibale Is Changed to {num1} and Second Number Is Changed To {num2}"
    
print("Swapping Number By Using Arithmetic Variable (Addition Subtraction)")
print(swap2_1(20, 8))
print("\n\n")

print("Swapping Number By Using Arithmetic Variable (Multiply Division)")
print(swap2_2(20,10))
print("\n\n")


#Method No.3
#By Using XOR Operators
def swap3(num1,num2):
    num1 = num1^num2
    num2 = num1^num2
    num1 = num1^num2
    return f"First Vaibale Is Changed to {num1} and Second Number Is Changed To {num2}"


print("Swapping Number By Using XOR Operators")
print(swap3(20,10))
print("\n\n")
print("Press Enter To Exit The Program")
input("")
