a = input("Enter the expression:")
list=[]
list1=[]
temp =""
j=1;invalid=False


for i in a:
    try:
        if i not in "+-/*":  #separated numbers and symbols
            temp+=i
        
        else:
            if(len(temp)==0):             #Handling expresion like -1+4
                temp+=i
                continue
            list.append(float(temp))
            list.append(i)
            temp=""
    except:
        print("Enter a valid expression")
        invalid=True
        break

list.append(float(temp))
if(invalid!=True):   #Multiplying and dividing fist according to BODMAS
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
    while(j<len(list)):  #ADD and substraction
        if(list[j]=="+"):
            r=list[j-1]+list[j+1]
            list = list[:j-1]+[r]+list[j+2:]
        elif(list[j]=="-"):    
            r=list[j-1]-list[j+1]
            list = list[:j-1]+[r]+list[j+2:]
        else:
            j+=2
            
print(list[0])



        
