file_path=input("Enter the Path :")
file=open(file_path,'r')
lines=file.readlines()
file.close()
print("Number of lines :",len(lines))
for line in lines:
    words=line.split()
    print("Words :",len(words))
