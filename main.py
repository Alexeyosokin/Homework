def draw_area():

 for i in area:
    print(*i)

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в крестики нолики")
print("----------------------------------")
draw_area()
for turn in range(1, 10):
    print(f'Ход{turn}')
    if turn % 2 == "0":
        print("ходят нолики")
    else:
        turn_char = "x"
        print('{ходят нолики}')
row = int(input("Введите номер строки(1,2,3)")) - 1
column = int(input("ведите номер столбца (1,2,3)")) - 1

draw_area()