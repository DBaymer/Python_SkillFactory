# Указать позицию в коде куда вставить фрагмент:
# if i % 2 == 0:
#        continue
# Чтобы при переборе всех чисел от 1 до 99 выводилось “число % 3”, если число кратно 3;
# “число % 5”, если число кратно 5; при этом все четные числа бы игнорировались

for i in range(1, 100):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        print(f'{i} % 3')
    if i % 5 == 0:
        print(f'{i} % 5')
