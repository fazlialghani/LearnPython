###CREDIT: W3SCHOOLS

# PRINT
print("Hello")
print('Hello')

print("It's")
print('It\'s')

a = "Hello"
print(a)

#Multiline Strings
b = """Lorem lorem
ipsum ipsum
dolor dolor"""
print(b)

b = '''Lorem lorem
ipsum ipsum
dolor dolor'''
print(b)

###NOTE: Strings are Arrays in Python. There is no char data type in Python.
a = "Hello World!"
print(a[1])

#Looping Through a String
for x in "banana":
    print(x)

#String Length
a = "Hello World!"
print(len(a))

#Check String
txt = "The best freestyle"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)