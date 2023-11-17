def dfs_function():
    print("DFS FUNCTION")

def bfs_function():
    print("BFS FUNCTION")

while 1:
    print("Select between the given searching algorithms:")
    print("1.DFS\n2.BFS")
    print("Select option:")
    option= input()
    if option=="1" :
        dfs_function()
        break
    elif option=="2" :
        bfs_function()
        break
    else:
        print("Wrong input")





