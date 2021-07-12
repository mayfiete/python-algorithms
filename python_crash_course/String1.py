# This is a test file 

import string

hw="Hello World"

print(hw)


string1 = "my Name is "
string2 = "Terry"
print(string1.upper().strip() + string2) # note we can do method chaining 

# tells the memory location of our object
print(id(string1) + id(string2)) # see the id value for the variable


#indexing 
name = "Interstellar"

print(name[1]) ## n 

print(name[-2]) ## returns second to last character

# reassign character 
# strings are immutable 

# slicing 
print(name[0:5])

print(name[5:])


nums = "012345678"

print(nums[0:6:2]) 

# len includes white spaces
print(len(nums))

# what is the data type?
print(type(nums))

message = "Blah Blah Findme Blah" 

print(message.find('Findme'))

split_message = message.split()

print(split_message) #separates words based on whitespace 

print("-".join(split_message))


print(string.ascii_lowercase) #import all lowercase letters

stock_price = "1100"  
#string interpolation
print("Today's price for google stock is: {}".format(stock_price))

print(f"Today's price for google stock is: {stock_price}")


print ("My name is \n Terry \t the great")

print("Hello friend see this special \\n character")