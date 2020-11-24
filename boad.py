print("WELCOME TO DISK-BATTLE")
text = ""
for i in range(1,7):
    text = text + " " +str(i)

print(text,end="")
def Thedisk(sign):
    lst =[]
    rows = 6
    cols = 6
    for i in range(rows):
        lst.append([])
    for i in range(rows):
        for j in range(cols):
            lst[i].append(sign)
    return lst


print(Thedisk(0))