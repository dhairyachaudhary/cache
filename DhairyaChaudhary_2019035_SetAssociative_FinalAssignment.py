#Name: Dhairya Chaudhary
#Roll No.: 2019035
#Group: 7

#Computer Organization End-Semester Assignment (Set Associative)

import math

def read(bitadd,data,tag):
    global offsize
    global setbits
    global N
    global CL

    sl=bitadd[-int(offsize)-int(setbits):-int(offsize)]
    si=int(sl,2)

    offi=bitadd[-int(offsize):]
    off=int(offi,2)

    ti=bitadd[0:-int(offsize)-int(setbits)]
    t=int(ti,2)

    if (tag[si].count(t)>0):
        ind=tag[si].index(t)
        print(data[si][ind][off])
    else:
        print("cache miss")

def write(bitadd,dat,data,tag):
    global offsize
    global setbits
    global N
    global CL

    #sl=bitadd[-int(offsize)-int(setbits):-int(offsize)]
    sl=bitadd[-int(setbits):]
    si=int(sl,2)
    #print(si)


    finbit=bitadd[0:-int(setbits)]
    finadd=int(finbit,2)
    #print(finadd)

    if (len(tag[si])==N):
        #print("hey")
        data[si].pop()
        tag[si].pop()

    if (tag[si].count(finadd)>0):
        #print("hi")
        lv=tag[si].index(finadd)
        tag[si].remove(finadd)
        data[si].remove(data[si][lv])
    #print(data)
    #print(tag)
    data[si].insert(0,dat)
    tag[si].insert(0,finadd)

    #print(data)
    #print(tag)

#assuming 32-bit machine
print("End-Semester Assignment: Set Associative Cache")
print("The cache is for a 32-bit machine. Addresses are expected in binary.\n")


#Basic inputs
CL=int(input("Enter no of cache lines:\n")) #128
B=int(input("Enter Block Size:\n")) #64 bytes
N=int(input("Enter associativity (no. of ways):\n"))


#Derivations from inputs; used in helper functions
offsize=math.log(B,2)
nsets=CL//N
setbits=int(math.log(nsets,2))


print("\nAfter every task there will be prompt for a new task. To quit, write 'exit'\n")
print("Tasks include writing to the cache and reading from it.\n")
print("For write operation, enter'write'. Then enter block address and data to be stored in block when prompted.\n")
print("For read operation, enter'read'. Then enter address to be searched for in cache. If found, data stored is printed or we print 'cache miss'.\n")


i=0
data=[]
while (i!=nsets):
    a=[]
    data.append(a)
    i+=1
i=0
tag=[]
while (i!=nsets):
    b=[]
    tag.append(b)
    i+=1

#print(tag)
#print(data)

while (True):

    inp=input("Next task\n").strip();


    if (inp=="read"):
        binadd=(input("Please provide address: "))
        read(binadd,data,tag)

    elif (inp=="write"):
        binadd=(input("Please provide block address (address minus offset bits): "))
        i=B
        print("Please enter the data to be present in this block:")
        dat=[]
        while (i!=0):
            d=input()
            dat.append(d)
            i=i-1
        write(binadd,dat,data,tag)

    elif (inp=="exit"):
        quit()


    else:
        print("Invalid command")
