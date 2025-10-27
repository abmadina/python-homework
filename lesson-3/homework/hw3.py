#1
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("The third fruit is:", fruits[2])

#2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)

#3
numbers = [10, 20, 30, 40, 50, 60]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print("New list:", new_list)

#4
movies = ["Inception", "Titanic", "Avatar", "Matrix", "Interstellar"]
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)

#5
cities = ["London", "Paris", "Tokyo", "New York"]
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

#6
numbers = [1, 2, 3]
duplicate = numbers * 2
print("Duplicated list:", duplicate)

#7
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swapping:", nums)

#8
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Slice (index 3 to 7):", numbers_tuple[3:8])

#9
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count = colors.count("blue")
print("Number of times 'blue' appears:", count)

#10
animals = ("tiger", "lion", "zebra", "elephant")
index = animals.index("lion")
print("Index of 'lion':", index)

#11
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print("Merged tuple:", merged)

#12
my_list = [10, 20, 30, 40]
my_tuple = (100, 200, 300)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

#13
numbers_tuple = (5, 10, 15, 20, 25)
numbers_list = list(numbers_tuple)
print("Converted list:", numbers_list)

#14
values = (4, 9, 1, 7, 3, 6)
print("Maximum:", max(values))
print("Minimum:", min(values))

#15
words = ("apple", "banana", "cherry", "date")
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)

