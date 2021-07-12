
import math

import random # using randomizer functions 

print(type(4)) 

print (type(3.5))

result = 4 + 3.5  
print(type(result))

#abs > absolute value 
print(abs(-4))


std_div = 10/3  
print(std_div)

floor_division = 10//4  
print(floor_division)

mod_op = 10 % 3  
print(mod_op) ##result is 1

## using powers 
use_power = 5 ** 2  
print(use_power) ##result

use_math_pow = math.pow(10,5)  #1
print(use_math_pow) 

log_math = math.log2(1000000)   #1
print(log_math)


## generate random number
randomizer = random.randint(0,1000)  #1 
print(randomizer) ##result

print(type("10" + "10"))

print(("10" + "10"))

#type casting
print(int("10") + int("10")) #1

num_1 ="10" 
num_2 = "20" 
result = int(num_1) + int(num_2)  #
print(result)

print(type(str(result))) #1


num_1 = int(input("Enter a number to multiply -> "))
num_2 = int(input("Einter a second number ")) 

result = num_1 * num_2 
print(result)


num_1 = 2510876961
num_2 = 7
result = num_1 %5 num_2
print(result)
