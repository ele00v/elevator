""" ----------------------------------------------------------------------------
****        Τεχνητή Νοημοσύνη 
****        Απαλλακτική Εργασία Εξαμήνου
****        Μέρος Ι: Ομαδικη Εργασία 
****        "Το πρόβλημα της εκκένωσης κτηρίου προς την ταράτσα"
****        Μέλη Ομάδας:
****        Ελένη Βέρα                   18390152
****        Χριστίνα Αχιλλεοπούλου       18390182
------------------------------------------------------------------------------"""
import copy
 
def tenants_sum(state):
    total=sum(state[1:5])
    #print("\ntotal:",total)
    return total

def find_children(state):
    children=[]
    
    floor1_state=copy.deepcopy(state)
    floor1_child=go_to_floor1(floor1_state)
    
    floor2_state=copy.deepcopy(state)
    floor2_child=go_to_floor2(floor2_state)
    
    floor3_state=copy.deepcopy(state)
    floor3_child=go_to_floor3(floor3_state)
    
    floor4_state=copy.deepcopy(state)
    floor4_child=go_to_floor4(floor4_state)
    
    roof_state=copy.deepcopy(state)
    roof_child=go_to_roof(roof_state)

    if floor1_child!=None: 
        children.append(floor1_child)
        
    if floor2_child!=None: 
        children.append(floor2_child)

    if floor3_child!=None: 
        children.append(floor3_child)

    if floor4_child!=None: 
        children.append(floor4_child)

    if roof_child!=None: 
        children.append(roof_child)
    
    return children 

#Initialization of queue
def make_queue(state):
    return [[state]]

#Expanding queue
def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    elif method=='BFS':
        print("Queue:")
        print(queue)
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
    #elif method=='BestFS':
       
    return queue_copy

#Initialization of front
def make_front(state):
    return [state]

#Expanding front
def expand_front(front, method):  
    if method=='DFS':    
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)
    elif method=='BFS' :
        if front:
            print("Front:")
            print(front)
            node = front.pop(0)
            for child in find_children(node):     
                front.append(child)
    #elif method=='BestFS':   
    
    return front

def go_to_floor1(state):
    if state[5]<8 and state[1]>0 and state[0]!=1:
        if state[1]>8-state[5]:
            new_state = [1] + [state[1] + state[5] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[5]]
        return new_state
        
def go_to_floor2(state):
    if state[5]<8 and state[2]>0 and state[0]!=2:
        if state[2]>8-state[5]:
            new_state = [2] + [state[1]] + [state[2] + state[5] - 8] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2]+ [state[1]] + [0] + [state[3]] + [state[4]] + [state[2] + state[5]]
        return new_state

def go_to_floor3(state):
    if state[5]<8 and state[3]>0 and state[0]!=3:
        if state[3]>8-state[5]:
            new_state = [3] + [state[1]] + [state[2]] + [state[3] + state[5] - 8] + [state[4]] + [8]
        else:
            new_state = [3] + [state[1]] + [state[2]] + [0] + [state[4]] + [state[3] + state[5]]
        return new_state

def go_to_floor4(state):
    if state[5]<8 and state[4]>0 and state[0]!=4:
        if state[4]>8-state[5]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4] + state[5] - 8] + [8]
        else:
            new_state = [4]  + [state[1]] + [state[2]] + [state[3]] + [0] + [state[4] + state[5]]
        return new_state

def go_to_roof(state):
    if state[5]==8 or (state[1]==0 and state[2]==0 and state[3]==0 and state[4]==0) and state[1]!=5:
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
    else :
        new_state=None    
    return new_state

def find_solution(front, queue, closed, goal, method):
   
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
    elif front[0]==goal:
        print('_GOAL_FOUND_')
        print(front[0])
        print(queue[0])
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)

def main():

    initial_state = [0, 9, 4, 12, 7, 0]
    goal = [5, 0, 0, 0, 0, 0]

    while 1:
        print("This program solves the problem of evacuating a building to the roof using different searching algorithms.")
        print("Select between the given searching algorithms:")
        print("1. DFS (Depth First Search)\n2. BFS (Breadth First Search)\n3. BestFS (Best-First)\n4. Exit")
        print("Select option:")
        option= input()
        if option=="1" :
            method="DFS"
            break
        elif option=="2":
            method="BFS"
            break
        elif option=="3":
            method="BestFS"
            #break
            exit()
        elif option=="4":
            print("Exiting...")
            exit()
        else:
            print("Wrong input")    
    print("Begin Searching\n---",method,"---")
    find_solution(make_front(initial_state),make_queue(initial_state),[],goal,method)
        
if __name__ == "__main__":
    main()