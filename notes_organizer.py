import os
s=open("note1.txt","w")
i=input("Type anything to put in note 1: ")
s.write(f"{i}\n")
i=input("Type another thing to put in note 1: ")
s.write(f"{i}\n")
i=input("Type the last thing to put in note 1: ")
s.write(f"{i}\n")
s.close()
s=open("note2.txt","w")
x=input("Type anything to put in note 2: ")
s.write(f"{x}\n")
x=input("Type another thing to put in note 2: ")
s.write(f"{x}\n")
x=input("Type the last thing to put in note 2: ")
s.write(f"{x}\n")
print("~===Note 1===~")
with open("note1.txt","r")as f:
    for line in f:
        print(line.strip())
print()
print("~===Note 2===~")
with open("note2.txt","r")as f:
    for line in f:
        print(line.strip())
print()


print("~===MERGED NOTES===~")
if os.path.exists("notes1+2.txt"):
    print("file exists this program is gonna overwrite it and there is nothing you can do about that.")
else:
    print("why do you not have it im gonna make it")

content=""
with open("note1.txt","r") as f:
    content+="science notes:\n"
    content+=f.read()+"\n"
with open("note2.txt","r") as f:
    content+="math notes:\n"
    content+=f.read()+"\n"

with open("notes1+2.txt","w") as out:
    out.write(content)
print("Saved")