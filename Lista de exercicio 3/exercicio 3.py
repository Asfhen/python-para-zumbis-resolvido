A = 80000
B = 200000
anos = 0
while A < B:
    A = A + (A * 0.03)
    B = B + (B * 0.015)
    anos = anos + 1
print(anos)