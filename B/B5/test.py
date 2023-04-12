# def check_win():
#     win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
#                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
#                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
#     for cord in win_cord:
#         symbols = []
#         for c in cord:
#             symbols.append(m[c[0]][c[1]])
#         if symbols == ["X", "X", "X"]:
#             print("Выиграл X!!!")
#             return True
#         if symbols == ["0", "0", "0"]:
#             print("Выиграл 0!!!")
#             return True
#     return False

m = [["X", "1", "1"],
     [" ", " ", " "],
     [" ", " ", " "]]


def win():
    m = list(map(int, m))
    if m[0][0] == 1:
        return "Win X"

win()
print(m[0][0])
