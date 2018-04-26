from random import randint
row = 5
col = 5

data = []
for i in range(row):
    sub_arr = []
    for j in range(col):
        sub_arr.append(randint(1, 100))
    data.append(sub_arr)
print(data)
print()
print()

# row-fashion
print_out = []
for i in range(row):
    sub_printout = []
    for j in range(col):
        sub_printout.append(str(data[i][j]))
    print_out.append(" ".join(sub_printout))
print("\n".join(print_out))
print()
print()

# col-fashion
print_out = []
for i in range(col):
    sub_printout = []
    for j in range(row):
        sub_printout.append(str(data[j][i]))
    print_out.append(" ".join(sub_printout))
print("\n".join(print_out))
print()
print()

# halves row fashion
print_out = []
for i in range(row):
    sub_printout = []
    for j in range(col):
        if i > j: continue
        sub_printout.append(str(data[i][j]))
    print_out.append(" ".join(sub_printout))
print("\n".join(print_out))
print()
print()
