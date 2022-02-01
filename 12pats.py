import requests
import math
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
prosfatos=data['round']
last_100=prosfatos-100
numbers=[]
link=[]
url = "https://drand.cloudflare.com/public/"
for i in range(0,100):
    for w in range(last_100,prosfatos+1):
        link.append(url + str(w))
print ("\n \n Ο ΤΕΛΕΥΤΑΙΟΣ ΓΥΡΟΣ ΕΧΕΙ ΑΡΙΘΜΟ:",prosfatos)
print ("\n Ο 100στος ΤΕΛΕΥΤΑΙΟΣ ΓΥΡΟΣ ΕΧΕΙ ΑΡΙΘΜΟ:",last_100)
print ("\n E Π Ε Ξ Ε Ρ Γ Α Σ Ι Α  ΣΕ  Ε Ξ Ε Λ Ι Ξ Η . . . \n \n \n \n ")#στην θεση numbers[0]=θεση 1 βρισκεται ο πιο παλιος γυρος
#ενω στν θεση numbers[99]=θεση 100 βρισκεται ο νεοτεροσ γυρος
for i in range(0,100):
    rr = requests.get(link[i], headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    dataa= rr.json()
    numbers.append(dataa['randomness'])
mikos_numbers=100
binary=[]
for i in range(0,100):
    number=numbers[i]
    num=int(number,16)
    bstr=''
    while num>0:
        bstr=str(num%2)+bstr
        num=num>>1
    res=bstr
    ari8mos=str(res)
    binary.append(ari8mos)
zero=[]
ace=[]
for i in range(100):
    zero.append(0)
    ace.append(1)
for i in range(100):
    inputt=binary[i]
    ace[i]=max(map(len, inputt.split('0'))) #συνεχομενοι ασσοοι
    zero[i]=max(map(len, inputt.split('1'))) #συνεχομενa μηδεν
max0=0
max1=0
for i in range(100):
    if ace[i]>max1:
        max1=ace[i]
        name_max1=i
    if zero[i]>max0:
        max0=zero[i]
        name_max0=i
print("Ο ΑΡΙΘΜΟΣ ΜΕ ΤΗΝ ΜΕΓΑΛΥΤΕΡΗ ΑΚΟΛΟΥΘΙΑ [",max1,"] ΑΣΣΩΝ ΕΙΝΑΙ Ο: \n",
numbers[name_max1],"\n ( ",binary[name_max1],") \n \n")
print("ΕΝΩ ΑΝΤΙΣΤΟΙΧΑ ΜΕ ΤΗΝ ΜΕΓΑΛΥΤΕΡΗ ΑΚΟΛΟΥΘΙΑ [",max0,"] ΜΗΔΕΝΙΚΩΝ ΕΙΝΑΙ Ο: \n",
numbers[name_max0],"\n (",binary[name_max0],")  \n")
