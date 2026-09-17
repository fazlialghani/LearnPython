#Note: we cannot combine string and numbers.
#ex:
#age = 36
#This will produce an error:
#txt = "My name is John, I am " + age
#print(txt)

###Thus, F-Strings exists.
#Idea: f & {...}
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#example 1:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#example 2:
txt = f"The price is {20 * 59} dollars"
print(txt)


