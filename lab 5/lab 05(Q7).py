#STACKS MENU
def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
        
def push(stk,ele):
    global top
    stk.append(ele)
    top=len(stk)-1
    
    
def pop(stk):
    if stk==[]:
        print('underflow')
    else:
        ele=stk.pop()
        global top
        top=len(stk)-1
        print('popped element:',ele)
        
def display(stk):
    if isempty(stk)==True:
        print('empty stack')
    else:
        top=len(stk)-1
        print(stk[top],'<--top')
        for a in range(top-1,-1,-1):
            print(stk[a])
            
stk=['dog','cat','fox','lion']
push(stk,'panda')
pop(stk)
display(stk)