keimeno=open("two_cities_ascii.txt","r")
data=keimeno.read()
print(data)
list=data.split(" ")
keimeno.close()
#print(list)
mikos=len(list)
print("ΤΟ ΑΡΧΙΚΟ ΜΗΚΟΣ ΤΗΣ ΛΙΣΤΑΣ ΕΙΝΑΙ:",mikos)
for i in range (mikos):
    for j in range(len(list[i])) :
        special='''!#@$%^&*()_+1234'567890-=[]{}\|;:",./<>?'''
        string=list[i]
        for z in special:
            string=string.replace(z,"").replace('\n'," ") #ΕΚΚΑΘΑΡΙΣΗ ΤΟΥ ΚΕΙΜΕΝΟΥ ΑΠΟ
                                                          #ΕΙΔΙΚΟΥΣ ΧΑΡΑΚΤΗΡΕΣ
    list[i]=string
print("ΠΛΕΟΝ ΣΤΗΝ ΛΙΣΤΑ ΕΧΟΥΝ ΜΕΙΝΕΙ ΜΟΝΟ ΟΙ ΑΠΑΡΑΙΤΗΤΟΙ (γράμματα και κενά) ΧΑΡΑΚΤΗΡΕΣ")
print(list)
new_list=[] #ΔΗΜΙΟΥΡΓΙΑ ΜΙΑΣ ΝΕΑΣ ΚΕΝΗΣ ΛΙΣΤΑΣ ΠΟΥ ΘΑ ΠΕΡΙΕΧΕΙ ΤΙΣ ΚΑΤΑΛΛΗΛΕΣ ΛΕΞΕΙΣ
for z in range(0,mikos-1,2):
    if len(list[z])!=len(list[z+1]): #ΕΝΤΑΞΗ ΖΕΥΓΟΥΣ ΛΕΞΕΩΝ ΟΠΟΥ ΤΟ ΑΘΡΟΙΣΜΑ!=20
        new_list.append(list[z])
        new_list.append(list[z+1])
list=new_list
print("Η ΝΕΑ ΛΙΣΤΑ ΜΕΤΑ ΤΗΝ ΑΦΑΙΡΕΣΗ ΤΩΝ ΖΕΥΓΑΡΙΩΝ ΛΕΞΕΩΝ:") #(Λ1+Λ2=20)
print(list)
new_mikos=len(list)
print("ΚΑΙ ΤΟ ΝΕΟ ΜΗΚΟΣ ΤΗΣ ΛΙΣΤΑΣ ΕΙΝΑΙ: ", new_mikos)
max=0
stats=[]
for w in range (new_mikos):
    if len(list[w])>max :
        max=len(list[w])


#print ("η μεγαλυτερη λεξη περιεχει " ,max ,"γραμματα και ειναι η:", onmax)
# ΠΑΡΑΚΑΤΩ ΔΗΜΙΟΥΡΓΟΥΜΕ ΕΝΑΝ ΠΙΝΑΚΑ ΟΠΟΥ: ΣΤΗΝ ΘΕΣΗ (ν) ΠΑΡΟΥΣΙΑΖΕΤΑΙ ΤΟ ΠΛΗΘΟΣ
#ΤΩΝ ΛΕΞΕΩΝ ΠΟΥ ΠΕΡΙΕΧΟΥΝ (ν) γραμματα .πχ στην 1η θεση παρουσιαζεται το πληθος
# των λεξεων που περιεχουν 1 γραμμα, στην 7η θεση οι λεξεις που περιεχουν 7 γραμματα κοκ
for w in range(0,new_mikos):
    for n in range (1,max+1):
        #print (len(list[w]))
        thesi=len(list[w])
    stats.append(thesi)
print("ΑΝΑΛΥΤΙΚΑ ΤΑ ΣΤΑΤΙΣΤΙΚΑ ΓΙΑ ΤΙΣ ΕΝΑΠΟΜΕΙΝΑΝΤΕΣ ΛΕΞΕΙΣ:")
for n in range (1,max+1):
    print("ΟΙ ΛΕΞΕΙΣ ΠΟΥ ΠΕΡΙΕΧΟΥΝ ",n ," ΓΡΑΜΜΑΤΑ ΕΙΝΑΙ : ",stats[n])
