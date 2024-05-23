kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
output = []

for i in kata:
    if len(i) >= 5:
        output.append(i)
output.sort()  
print(output)