
#1. append() - adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
print(fruits.append("orange"))

#2. clear() - removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
print(fruits.clear())

#3. copy() - returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

#4. count() - returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

#5. extend() - add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
print(fruits.extend(cars))
print(fruits)

#6. index() - returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#7. insert() - adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#8. pop() - removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#9. remove() - removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#10. reverse() - reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#11. sort() - sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)