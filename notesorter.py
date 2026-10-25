file= open("notesorter.txt","w")
file.write("Todo: Math homework")
file.write("\nImportant: Test on monday")
file.write("\nTodo: English homework")
file.write("\nTodo: Quiz")
file.write("\nJunk: ~^=-~-~-(Junk)")
file.close()
file=open("notesorter.txt","r")
lines =file.readlines()
for i in range(len(lines)):
    print(i+1,"->",lines[i].strip())
file.close()
letter="J"
file=open("notesorter.txt","r")
for line in file:
    if line.startswith(letter.upper()):
        print("Skip -->>", line.strip())
    else:
        print("Keep -->>",line.strip())
file.close()
file=open("notesorter.txt","r")
lines=file.readlines()
file.close()
