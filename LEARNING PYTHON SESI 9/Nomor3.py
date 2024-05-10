kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]

i = 0
while i < len(kata):
    if len(kata[i]) < 5:
        del kata[i]
    else:
        i += 1

kata.sort()

print(kata)