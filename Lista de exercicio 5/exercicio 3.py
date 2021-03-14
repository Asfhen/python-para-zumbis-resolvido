x = 0

for i in range(1067, 3628):
    if i % 2 == 0 and i % 7 == 0:
        x += 1

print(x)