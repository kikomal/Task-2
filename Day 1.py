
# take two numbers and add.
#Add two numbers after converting the data type
first= input("Enter 1st no: ")
second = input("Enter 2nd no: ")
Sum= float(first)+ float(second) # we are converting the data type as input function returns string
print("Sum of two numbers is:" ,Sum)

#we can also write this code like this by directly converting data type in input function
first= float(input("Enter 1st no: "))
second = float(input("Enter 2nd no: "))
Sum= first+second # we are converting the data type as input function returns string
print("Sum of two numbers is:" ,Sum)

#check if sum is odd or even
if Sum%2==0:
    print(Sum, "is even number")
else:
    print(Sum, "is odd number")
Sum=int(Sum)

#check if number is prime:
for i in range(2,Sum):
    rem=Sum%i
    if rem==0:
        print(Sum, " is not a prime number")
        break
    else:
        print(Sum, " is a prime number")
        break


#to print the table of number
for i in range(1,10):  #by default range starts with 0
    print (Sum*i)


#to get the string value in lower case we can use the built in function lower()
abc=input("Enter your full name ")
print(abc.lower())


#to get the string value in lower case we can use the built in function upper()
print(abc.upper())

#replace function is used to replace one value with other value
a="Hello World!"
print(a.replace("Hello", "Bye"))

# in is a special keyword in python is used to chcek if certain value is in the string
print('Hello' in a)




