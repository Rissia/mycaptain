str=input("Input the filename:")
n=str.find(".")
if(str[n+1:-1]=="py"):
    print("python")
elif(str[n+1:-1]=="java"):
    print("Java")
elif(str[n+1:-1]=="txt"):
    print("Text")
elif(str[n+1:-1]=="doc"or"docx"):
    print("Word")
