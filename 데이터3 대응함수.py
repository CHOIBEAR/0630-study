import csv

def draw_shape(path=r"app01\data3.csv", encoding="utf-8"):
    with open(path, "r", encoding=encoding) as f:
        for row in csv.reader(f):
            print("".join("O" if c.strip() == "O" else " " for c in row))

draw_shape()
