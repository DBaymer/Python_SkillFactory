# Задан список
L = ["а", "б", "в", 1, 2, 3, 4]
# Получаем срез [] от 4 символа, но в обратном порядке ::-1
print(L[3::-1])
# [1, "в", "б", "а"]

# Получаем список от последнего символа до 3 с конца
# -4 не включается в выборку и всё это в обратном порядке [:-1]
print(L[-1:-4:-1])
# [4, 3, 2]
