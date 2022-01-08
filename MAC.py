mac = "EC:B0:8T:E4"
mapper = {"E":0,"T":0}
newMac = ""
for item in mac:
    if item == "E" or item == "T":
        newMac += str(mapper[item])
    else:
        newMac += item
print(newMac)

