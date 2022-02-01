def Convert(string):
    li = list(string.split(" "))
    return li
import ast
import json
with open('dictionary.txt') as f:
    datas = f.read()
print("ΑΡΧΕΙΟ ΕΙΣΗΧΘΕΙ... \n \n")
data=datas.replace("{","").replace("}","").replace('"',"").replace(":"," ").replace(","," ").replace("\n"," ")
ndata=Convert(data)
new_m=len(ndata)
dictionary={}
a_list=[]
dictionary_copy=dictionary.copy()
count=-1
for i in range(0,new_m,2):
    count=count+1
    outpout=ndata[i+1]
    dictionary[ndata[i]]=ndata[i+1]
    a_list.append(dictionary[ndata[i]])
print("TA ΔΙΑΘΕΣΙΜΑ ΚΛΕΙΔΙΑ ΘΑ ΕΜΦΑΝΙΣΤΟΥΝ ΠΑΡΑΚΤΩ... \n",dictionary.keys())
maxX=-10**11
maxY=maxX
minX=10**10
minY=minX
maxN="zzzzzzzzzzzz"
minN="AAAAAAAAAAAA"
ndataa={}
while True:
    inp = input('ΠΟΙΟ ΑΠΟ ΤΑ ΔΙΑΘΕΣΙΜΑ ΚΛΕΙΔΙΑ ΣΑΣ ΕΝΔΙΑΦΕΡΕΙ ;\n\n')
    if inp=="x": #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
        print("AΠΑΝΤΗΣΗ ΔΕΚΤΗ \n\n\n")
        for i in range(1,new_m,6):
            num=int(ndata[i])
            if maxX<num:
                maxX=num
            if minX>num:
                minX=num
        print("ΤΟ ΜΕΓΙΣΤΟ Χ ΕΧΕΙ ΤΗΝ ΤΙΜΗ:",maxX,"\n ΕΝΩ ΤΟ ΕΛΑΧΙΣΤΟ ΤΗΝ ΤΙΜΗ:",minX)
        for i in range(1,new_m,6):
            ndataa[i]=ndataa.get(i,0)+1
        freqx=[]
        for key, w in ndataa.items():
            freqx.append((w,key))
        freqx.sort(reverse=True)
        print("Ο ΑΡΙΘΜΟΣ ΠΟΥ ΕΜΦΑΝΙΖΕΤΑΙ ΤΙΣ ΠΕΙΡΙΣΣΟΤΕΡΕΣΓΟΡΕΣ ΕΙΝΑΙ Ο:",ndata[freqx[0][1]])
        break
    elif inp=="y": #YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYyy
        print("ok")
        for i in range(3,new_m,6):
            num=int(ndata[i])
            if maxY<num:
                maxY=num
            if minY>num:
                minY=num
        print("ΤΟ ΜΕΓΙΣΤΟ Y ΕΧΕΙ ΤΗΝ ΤΙΜΗ:",maxY,"\nΕΝΩ ΤΟ ΕΛΑΧΙΣΤΟ ΤΗΝ ΤΙΜΗ:",minY)
        for i in range(3,new_m,6):
            ndataa[i]=ndataa.get(i,0)+1
        freqy=[]
        for key, w in ndataa.items():
            freqy.append((w,key))
        freqy.sort(reverse=True)
        print("Ο ΑΡΙΘΜΟΣ ΠΟΥ ΕΜΦΑΝΙΖΕΤΑΙ ΤΙΣ ΠΕΙΡΙΣΣΟΤΕΡΕΣΓΟΡΕΣ ΕΙΝΑΙ Ο:",ndata[freqy[0][1]])
        break
    elif inp=="name": #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        print("ok")
        for i in range(5,new_m,6):
            if maxN>ndata[i]:
                maxN=ndata[i]
            if minN<ndata[i]:
                minN=ndata[i]
        print("ΤΟ 'ΜΕΓΑΛΥΤΕΡΟ' ΟΝΟΜΑ ΕΙΝΑΙ :",maxN,"\n ΕΝΩ ΤΟ 'ΜΙΚΡΟΤΕΡΟ':",minN)
        for i in range(5,new_m,6):
            ndataa[i]=ndataa.get(i,0)+1
        freqn=[]
        for key, w in ndataa.items():
            freqn.append((w,key))
        freqn.sort(reverse=True)
        print("ΤΟ ΟΝΟΜΑ ΠΟΥ ΕΜΦΑΝΙΖΕΤΑΙ ΤΙΣ ΠΕΙΡΙΣΣΟΤΕΡΕΣΓΟΡΕΣ ΕΙΝΑΙ TΟ:",ndata[freqn[0][1]])
        break
    else:
        print("ΤΟ ΚΛΕΙΔΙ ΠΟΥ ΠΛΗΚΤΡΟΠΟΓΗΣΑΤΕ ΔΕΝ ΥΠΑΡΧΕΙ! \n")
        break
