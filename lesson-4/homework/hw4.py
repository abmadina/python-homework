#1
# Original dictionary
d = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort ascending by value
asc = dict(sorted(d.items(), key=lambda item:

#2
d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Merge all into one dictionary
combined = {}
for d in (dic1, dic2, dic3):
    combined.update(d)

print("Concatenated dictionary:", combined)

#4
n = int(input("Enter a number: "))
squares = {x: x*x for x in range(1, n+1)}
print("Dictionary with squares:", squares)

#5
squares_15 = {x: x*x for x in range(1, 16)}
print("Squares from 1 to 15:", squares_15)

