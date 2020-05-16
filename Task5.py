def most_frequent(str1):
    dict1={}
    for i in range(0,len(str1)):
        dict1[str1[i]]=str1.count(str1[i])
    dict1=sorted(dict1.items(), key=lambda item: item[1],reverse=True)
    for i in dict1:
        print(i)
    
list1=input("Please enter the string:")
most_frequent(list1)
