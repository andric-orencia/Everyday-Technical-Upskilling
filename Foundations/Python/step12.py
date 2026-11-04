age = 16
has_id = True
name = ""

if age >= 18 and has_id:
    print("A")
elif age >= 13 or not has_id:
    print("B")
else:
    print("C")

if name:
    print("D")
else:
    print("E")
