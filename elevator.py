import copy
import sys 


def find_children(state):
    
    children=[]
    
       
    floor1_state=copy.deepcopy(state)
    floor1_child=go_to_floor1(floor1_state)
    
    

    

    if floor1_child!=None: 
        children.append(floor1_child)
        
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
    elif method=='---':
        print(".......")
    
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
    elif method=='---':      
        print("......")

    return front

def go_to_floor1(state):
    if state[5]<8 and state[1]>0:
        if state[1]>8-state[5]:
            new_state = [1] + [state[1] + state[5] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[5]]
        return new_state

def go_to_floor2(state):
    if state[5]<8 and state[2]>0:
        if state[2]>8-state[5]:
            new_state = [2] + state[1] + [state[2] + state[5] - 8] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2] + state[1] + [0] + [state[3]] + [state[4]] + [state[2] + state[5]]
        return new_state

def go_to_floor3(state):
    if state[5]<8 and state[3]>0:
        if state[3]>8-state[5]:
            new_state = [3] + state[1] + [state[2]] + [state[3] + state[5] - 8] + [state[4]] + [8]
        else:
            new_state = [3] + state[1] + [state[2]] + [0] + [state[4]] + [state[3] + state[5]]
        return new_state

def go_to_floor4(state):
    if state[5]<8 and state[4]>0:
        if state[4]>8-state[5]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4] + state[5] - 8] + [8]
        else:
            new_state = [4]  + [state[1]] + [state[2]] + [state[3]] + [0] + [state[4] + state[5]]
        return new_state

def go_to_roof(state):
    if state[5]>8 :
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]    
    return new_state

def find_solution(initial_state,goal,method):
    if method=='DFS':
        print("--1.DFS--")
    elif method=='BFS':
        print("--2.BFS--")
    elif method=='---':
        print("--3.-----")

def main():

    initial_state = [0, 9, 4, 12, 7, 0]
    goal = [5, 0, 0, 0, 0, 0]

    while 1:
        print("This program solves the problem of evacuating a building to the roof using different searching algorithms.")
        print("Select between the given searching algorithms:")
        print("1.DFS (Depth First Search)\n2.BFS (Breadth First Search)\n3.---")
        print("Select option:")
        option= input()
        if option=="1" :
            method="DFS"
            break
        elif option=="2":
            method="BFS"
            break
        elif option=="3":
            method="---"
            break
        else:
            print("Wrong input")
            
    find_solution(initial_state,goal,method)
        
if __name__ == "__main__":
    main()