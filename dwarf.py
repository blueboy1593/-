list_dwarf = []
for i in range(9):
    list_dwarf.append(int(input()))

age_sum = sum(list_dwarf)

for i in list_dwarf:
    for j in list_dwarf:
        if age_sum - (i + j) == 100 and i != j:
            list_dwarf.remove(i)
            list_dwarf.remove(j)
            break

for i in sorted(list_dwarf):
    print(i)

# print(list_dwarf.sort())

# for i in final:
#     print(i)

# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13