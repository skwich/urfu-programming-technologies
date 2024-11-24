a = "[[10 4 7], [2 7 5], [7 10 5]]"[1:]
a = a.replace("[", "").replace("]]", "").split("], ")
a = [list(map(int, b.split())) for b in a]
print(a)
