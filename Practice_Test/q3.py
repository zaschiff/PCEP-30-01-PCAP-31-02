i = 250
print(len(str(i)))
while len(str(i)) > 72:
    i *= 2
else:
    i //= 2

print(i)