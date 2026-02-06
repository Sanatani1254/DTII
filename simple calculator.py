a = input("Enter the expression:")
list=[]
print("YO")
list1=[]
temp =""
j=1;invalid=False


for i in a:
    try:
        if i not in "+-/*":
            temp+=i
        
        else:
            list.append(float(temp))
            list.append(i)
            temp=""
    except:
        print("Enter a valid expression")
        invalid=True
        break

list.append(float(temp))
if(invalid!=True):
    while(j<len(list)):
        if(list[j]=="*"):
            r=list[j-1]*list[j+1]
            list = list[:j-1]+[r]+list[j+2:]
        elif(list[j]=="/"):    
            r=list[j-1]/list[j+1]
            list = list[:j-1]+[r]+list[j+2:]
        else:
            j+=2
        
        
        
    j=1
    while(j<len(list)):
        if(list[j]=="+"):
            r=list[j-1]+list[j+1]
            list = list[:j-1]+[r]+list[j+2:]
        elif(list[j]=="-"):    
            r=list[j-1]-list[j+1]
            list = list[:j-1]+[r]+list[j+2:]
        else:
            j+=2
            
print(list[0])



        
