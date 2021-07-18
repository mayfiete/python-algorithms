

choice = '1'
made_payment = False

if choice=='1' and made_payment: 
    print("You have chosen option 1") 
elif choice=='2':
    print("You have chosen option 2")
else:
    print("You have made an invalid choice")



made_payment = True 
a = 'Please pay monthly premium' 
b = 'Welcome to your homepage' 

if not made_payment: 
    print(a) 
else:
    print(b)




i = 20 
j = 20
k = 20 

if i < j and i < k:
    print("i is less than j and k") 
elif i == j and i == k:
    print ("i is equal to j and k") 
elif i == j or i == k: 
    print("i is equal to either j or k")
else:
    print("something else")


# Ternary operators 

course = 'java' 
a = 'enrolled in python course' 
b = 'enrolled in some other course'

print(a) if course == 'python' else print(b)


account = "verified"
payment_status = "pending"
## Write your code below (variable number of lines)
if account=="verified" and payment_status=="paid":
    print("Temporary access granted, check payment status")
elif payment_status != "pending" or payment_status != "paid": 
    print("Access denied, check payment")
else:
    print("Access denied")