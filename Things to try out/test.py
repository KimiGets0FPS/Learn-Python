'''
Name: Kimi Wan
Teacher: Mr. Reid
Period: 2
Date: 10/13/22
'''

# creates a new list with 5 elements
groceries = ['eggs', 'milk', 'bread', 'fruit', 'cookies', 'milk']

print(groceries)

groceries.append("diet coke")
print(groceries)

groceries.remove("cookies")
print(groceries)


print(groceries.count("milk"))

groceries.sort()
print(groceries)

groceries.insert(len(groceries) // 2, "ground beef")
print(groceries)

groceries.pop(-2)
print(groceries)

print(groceries.index("bread"))

groceries.reverse()
print(groceries)

groceries.clear()
print(groceries)
