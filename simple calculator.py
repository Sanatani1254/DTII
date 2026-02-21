a = input("Enter the expression:")
list=[]
list1=[]
temp =""
j=1;invalid=False

for i in a:
    if i not in "0123456789+-*/()":    #not accepting anything otherthan allowed characters
        invalid = True
        break
    try: 
        if i not in "+-/*()":  #separating numbers and symbols
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

try:
    list.append(float(temp))
except:
    pass
if(invalid!=True):    
    while range(len(list)-1):
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
if (invalid!=True):
    print(list[0])
else:
    print("This program only accepts numbers ,*,/,+,- Be sure to not add spaces")



        
