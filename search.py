import re;
def search():
 try:
    file_read = open("projects", "r")
    text = input("Enter date: ")
    lines = file_read.readlines()
    new_list = []
    idx = 0
    for line in lines:

        if text in line:
            new_list.insert(idx, line)
            idx += 1
    file_read.close()
    if len(new_list)==0:
       print("\n\"" +text+ "\" is not found in \"" +"projects"+ "\"!")
    else:
        lineLen = len(new_list)
        for i in range(lineLen):
            print(end=new_list[i])
        print()
 except :
  print("\nThe file doesn't exist!")