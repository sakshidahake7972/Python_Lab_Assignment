#1
f1 = open("input.txt", "r")
data = f1.read()
upper_data = data.upper()
f2 = open("output.txt", "w")
f2.write(upper_data)
f1.close()
f2.close()

print("File converted to uppercase successfully!")
