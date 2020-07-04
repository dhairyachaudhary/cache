#Name: Dhairya Chaudhary
#Roll No.: 2019035
#Group: 7

#Computer Organization End-Semester Assignment (Fully Associative)

import math

def read(tval,binadd,tag,data):
    #Dataread
    global offsize
    if (tag.count(tval)>0):
        #print(tval)
        #print(offsize)
        bi=int(binadd[-(offsize):],2)
        #print(bi)
        print(data[tag.index(tval)][bi])
    else:
        print("cache miss")

def write(address,dat,tag,data):
    #Datawrite
    #Implemented FIFO configurayion
    global CL
    if (len(tag)==CL):
        tag.pop()
        data.pop()
    if (tag.count(address)>0):
        i=tag.index(address)
        tag.remove(address)
        data.remove(data[i])
    tag.insert(0,int(address))
    data.insert(0,dat)


#assuming 32-bit machine
print("End-Semester Assignment: Fully Assocative Cache")
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
data=[]


#Loop terminates when user types "exit"
while (True):

    inp=input("Next task\n").strip();


    if (inp=="read"):
        binadd=(input("Please provide address: "))
        add=int(binadd,2)
        tval=add//B
        read(tval,binadd,tag,data)


    elif (inp=="write"):
        binadd=(input("Please provide block address (tag for the block): "))
        add=(int(binadd,2))
        i=B
        print("Please enter the data to be present in this block:")
        dat=[]
        while (i!=0):
            d=input()
            dat.append(d)
            i=i-1
        write(add,dat,tag,data)


    elif (inp=="exit"):
        quit()


    else:
        print("Invalid command")
