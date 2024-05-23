buah1=["apel", "jeruk", "mangga"]
buah2= ["apel", "anggur", "nanas"]

buah1.extend(buah2)
buah = []

for i in buah1:
    if i not in buah:
        buah.append(i)
buah.sort()
print(buah)