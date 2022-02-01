keimeno=open("test.txt","r")
data=keimeno.read()
print('\n')
print('\n')
print("ΚΕΙΜΕΝΟ ΕΙΣΑΧΘΕΙ ΕΠΙΤΥΧΩΣ...",)
print('\n')
text=data.lower()
list=text.split(" ")
keimeno.close()
mikos=len(list)
for i in range (mikos):
    for j in range(len(list[i])) :
        special='''!#@$%^&*()_+1234'567890-=[]{}\|;:",./<>?'''
        string=list[i]
        for z in special:
            string=string.replace(z,"").replace('\n'," ") #ΕΚΚΑΘΑΡΙΣΗ ΤΟΥ ΚΕΙΜΕΝΟΥ ΑΠΟ
                                                          #ΕΙΔΙΚΟΥΣ ΧΑΡΑΚΤΗΡΕΣ
    list[i]=string
print("ΠΛΕΟΝ ΣΤΗΝ ΛΙΣΤΑ ΕΧΟΥΝ ΜΕΙΝΕΙ ΜΟΝΟ ΟΙ ΑΠΑΡΑΙΤΗΤΟΙ (πεζά και κενά) ΧΑΡΑΚΤΗΡΕΣ")
dict={}
for i in list:
    dict[i]=dict.get(i,0) +1
statsA=[]
for key, w in dict.items():
    statsA.append((w, key))
statsA.sort(reverse=True)
print("ΠΑΡΑΚΑΤΩ ΘΑ ΣΑΣ ΠΑΡΟΥΣΙΑΣΩ ΤΙΣ  /TOP 10\  ΛΕΞΕΙΣ ΠΟΥ ΕΜΦΑΝΙΖΟΝΤΑΙ ΣΤΟ ΚΕΙΜΕΝΟ:::")
for w in range (1,11) :
    print("Η  (",w,"η)  ΛΕΞΗ ΠΟΥ ΕΜΦΑΝΙΖΕΤΑΙ ΤΙΣ ΠΕΡΙΣΣΟΤΕΡΕΣ ΦΟΡΕΣ(",statsA[w-1][0],") ΕΙΝΑΙ Η:",statsA[w-1][1])
#2 γραμματα
list2=[]
for i in range(0,mikos):
    prwta=list[i][:2]
    list2.append(prwta)
dict2={}
for i in list2:
    dict2[i]=dict2.get(i,0) +1
statsB=[]
for key, w in dict2.items():
    statsB.append((w, key))
statsB.sort(reverse=True)
######## 3 γραμματα
list3=[]
for i in range(0,mikos):
    prwta=list[i][:3]
    list3.append(prwta)
dict3={}
for i in list3:
    dict3[i]=dict3.get(i,0) +1
statsC=[]
for key, w in dict3.items():
    statsC.append((w, key))
statsC.sort(reverse=True)
#ΕΚΤΥΠΩΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ ΓΙΑ ΤΑ ΥΠΟΕΡΩΤΗΜΑΤΑ 2 ΚΑΙ 3
#β)
print('\n')
print(" ΟΙ ΤΡΕΙΣ ΠΡΩΤΟΙ ΣΥΝΔΙΑΣΜΟΙ ΤΩΝ ΔΥΟ ΠΡΩΤΩΝ ΓΡΑΜΜΑΤΩΝ ΠΟΥ ΑΡΧΙΖΟΥΝ ΟΙ ΠΕΙΡΙΣΣΟΤΕΡΕΣ ΛΕΞΕΙΣ ΕΙΝΑΙ: ")
for b in range(1,4):
    print("O (",b,"os) ΣΕ ΚΑΤΑΤΑΞΗ ΣΥΝΔΙΑΣΜΟΣ 2 ΓΡΑΜΜΑΤΩΝ ΕΙΝΑΙ Ο:",statsB[b-1][1],"ΚΑΙ ΕΜΦΑΝΙΖΕΤΑΙ {",statsB[b-1][0],"} ΦΟΡΕΣ")
print('\n')
#γ)
print(" ΚΑΙ ΑΝΤΙΣΤΟΙΧΑ, ΤΩΝ ΤΡΙΩΝ ΠΡΩΤΩΝ ΓΡΑΜΜΑΤΩΝ ΠΟΥ ΑΡΧΙΖΟΥΝ ΟΙ ΠΕΙΡΙΣΣΟΤΕΡΕΣ ΛΕΞΕΙΣ ΕΙΝΑΙ: ")
for c in range(1,4):
    print("O (",c,"os) ΣΕ ΚΑΤΑΤΑΞΗ ΣΥΝΔΙΑΣΜΟΣ 3 ΓΡΑΜΜΑΤΩΝ ΕΙΝΑΙ Ο:",statsC[c-1][1],"ΚΑΙ ΕΜΦΑΝΙΖΕΤΑΙ {",statsC[c-1][0],"} ΦΟΡΕΣ")
