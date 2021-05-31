# This is a test file 

hw="Hello World"

print(hw)


string1 = "My Name is "
string2 = "Terry"
print(string1 + string2)

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