para="""This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file."""
lines=para.split("\n")
print("Lines :",lines)
print("Number of lines :",len(lines))
for line in lines:
    words=line.split()
    print("Words :",len(words))
