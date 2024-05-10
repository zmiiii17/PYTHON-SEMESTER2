list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]

combined_list = list1 + list2

unique_fruits = []
for fruit in combined_list:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

unique_fruits.sort()

print(unique_fruits)