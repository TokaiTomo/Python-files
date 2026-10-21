import os
s=open("science_class_notes.txt","w")
s.write("Science is stuff\n")
s.write("2Hydrogen + Oxygen = Water\n")
s.write("Hydrogen can be made by dissolving metal with acid\n")
s.close()
s=open("math_class_notes.txt","w")
s.write("Math is stuff\n")
s.write("1+1=2\n")
s.write("2x+2y=20 y+x=10\n")
s.close()
print("~===Science notes===~")
with open("science_class_notes.txt","r")as f:
    for line in f:
        print(line.strip())
print()
print("~===Math notes===~")
with open("math_class_notes.txt","r")as f:
    for line in f:
        print(line.strip())
print()

print("~===MERGED NOTES===~")
if os.path.exists("super_merged_notes.txt"):
    print("file exists this program is gonna overwrite it and there is nothing you can do about that.")
else:
    print("why do you not have it im gonna make it")

content=""
with open("science_class_notes.txt","r") as f:
    content+="science notes:\n"
    content+=f.read()+"\n"
with open("math_class_notes.txt","r") as f:
    content+="math notes:\n"
    content+=f.read()+"\n"

with open("super_merged_notes.txt","w") as out:
    out.write(content)
print("Saved")