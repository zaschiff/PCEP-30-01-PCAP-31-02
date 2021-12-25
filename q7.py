z, y, x = 2, 1, 0 # z = 2 y = 1 x = 0
x, z = z, y # x = 2 z = 1
y = y - z # y = 0
x, y, z = y, z, x

print(x, y, z)
# expected out put shold be 0, 1, 2