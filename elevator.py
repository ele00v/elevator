def find_solution(initial_state,goal,method):
    if method=="DFS":
        print("--1.DFS--")
    elif method=="BFS":
        print("--2.BFS--")
    elif method=="--":
        print("--3.-----")

def main():

    initial_state = [0, 9, 4, 12, 7, 0]
    goal = [5, 0, 0, 0, 0, 0]

    while 1:
        print("Select between the given searching algorithms:")
        print("1.DFS\n2.BFS\n3.---")
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