#QUEUES MENU
def isemptyq(q):
    if q==[]:
        return True
    else:
        return False

def enqueue(q,ele):
    q.append(ele)
    if len(q)==1:
        front=rear=0
    else:
        rear=len(q)-1

def dequeue(q):
    if isemptyq(q)==True:
        print('underflow')
    else:
        ele=q.pop(0) 
        if len(q)==0:
            front=rear=None
        print('removed element:',ele)
        
def peak(q):
    if isemptyq(q)==True:
        print('queue empty')
    else:
        print('peak:',q[0])
        
def display(q):
    if isemptyq(q)==True:
        print('queue empty')
    else:
        rear=len(q)-1
        print(q[0],'<--front')
        for i in range(1,rear):
            print(q[i])
        print(q[rear],'<--rear')
        
q=['dog','cat','fox','lion','bear']
enqueue(q,'panda')
peak(q)
dequeue(q)
display(q)