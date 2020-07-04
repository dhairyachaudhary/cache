#Name: Dhairya Chaudhary
#Roll No.: 2019035
#Group: 7

#Computer Organization End-Semester Assignment (Direct Mapping)

import math

def read(binadd,add,tag,data):
    #Dataread
    global B
    global CL
    global offsize

    blockadd=add//B
    bladd=bin(blockadd).replace("0b", "")

    broski=int(binadd[-(int(offsize)):],2)

    loc=(int(blockadd%CL))

    a=int(math.log(CL,2))
    bi=binadd[0:a]
    a=int(bi,2)

    #print(loc)
    #print(tag[loc])
    #print(a)

    if (tag[loc]==a):
        print(data[loc][broski])

    else:
        print("cache miss")



def write(binadd,add,dat,tag,data):
    #Datawrite
    global CL

    loc=int(int(add%CL))

    a=int(math.log(CL,2))
    bi=binadd[0:a]
    a=int(bi,2)

    tag[loc]=a
    data[loc]=dat

    #print(tag)
    #print(data)




#assuming 32-bit machine
print("End-Semester Assignment: Direct Mapped Cache")
print("The cache is for a 32-bit machine. Addresses are expected in binary.\n")


#Basic inputs
CL=int(input("Enter no of cache lines:\n")) #128
B=int(input("Enter Block Size:\n")) #64 bytes


#Derivations from inputs; used in helper functions
blocksinmachine=(2**32)/B
tagsize=int(math.log(blocksinmachine,2))
adsize=int(math.log(2**32,2))
offsize=adsize-tagsize


print("\nAfter every task there will be prompt for a new task. To quit, write 'exit'\n")
print("Tasks include writing to the cache and reading from it.\n")
print("For write operation, enter'write'. Then enter block address and data to be stored in block when prompted.\n")
print("For read operation, enter'read'. Then enter address to be searched for in cache. If found, data stored is printed or we print 'cache miss'.\n")


#Initialization
tag=[]
i=0
while (i!=CL):
    tag.append(-1)
    i+=1

data=[]
i=0
while (i!=CL):
    data.append(0)
    i+=1


while (True):

    inp=input("Next task\n").strip();


    if (inp=="read"):
        binadd=(input("Please provide address: "))
        add=int(binadd,2)
        read(binadd,add,tag,data)


    elif (inp=="write"):
        binadd=(input("Please provide block address (tag+index for the block): "))
        add=(int(binadd,2))
        i=B
        print("Please enter the data to be present in this block:")
        dat=[]
        while (i!=0):
            d=input()
            dat.append(d)
            i=i-1
        write(binadd,add,dat,tag,data)

    elif (inp=="exit"):
        quit()


    else:
        print("Invalid command")
