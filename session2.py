your_name = input("whats your name :")
print("your name:",your_name.title())


from sketchpy import library as lib
obj = lib.rdj()
obj.draw()



Name = input("welcome to our website enter your name : ")
message = input("enter your message : ")
print(f"your name is {Name} your message is {message} and welcome nice to see")



Name = input("welcome to our website enter your name : ")
message = input("enter your message : ")
print(f"your name is {0} your message is {1} and welcome nice to see".format(your_name,message))


num = " alireza" * 100
print(num) 


number = 73246784309874023897 * 3879489213708409231840923
print(number)

number1 = 5000 / 38
print(number1)

number2 = 5000 // 38
print(number2)

number2 = 5 ** 2
print(number2)

mine = 16
father = 42
mother = 40
sister = 6
result = mine + father + mother + sister
print(result//4)

print((mine + father + mother + sister) / 4)


number1 = int(input("tol : "))
number2 = int(input("arz : "))
result = number1 * number2
result2 = (number1 + number2) * 2
print(f"tol : {number1} zel : {number2} masahat = {result} mohit = {result2}")

p = 3.14
num1 = float(input("shoa : "))
result = 4 * p * num1**2
result2 = (4.3) * (p * num1**2) 
print(f"shoa : {num1} masahat : {result} hajm : {result2}")


letter = input("your letter : ")
num2 = int(input("number : "))
result3 = letter * num2
print(result3)

mylist = ["pouya","ali","mohamad"]
esition = mylist.append(input("esm : "))
print(mylist)

mylist = ["pouya","ali","mohamad"]
mylist.append("ali")
mylist.clear()
mylist.remove("pouya")
print(mylist)

list1 = []
name1 = input("first name : ")
name2 = input("second name : ")
list1.append(name1)
list1.append(name2)
list1.remove(name1)
list1.insert(0, "pouya")
print(list1)