""" ----------------------------------------------------------------------------
****        Πανεπιστήμιο Δυτικής Αττικής
****        Σχολή Μηχανικών        
****        Τμήμα Μηχανικών Πληροφορικής & Υπολογιστών
****        Ακαδημαϊκό έτος: 2023-2024 | 5ο εξάμηνο

****        Τεχνητή Νοημοσύνη 
****        Απαλλακτική Εργασία Εξαμήνου
****        Μέρος Ι: Ομαδικη Εργασία, 2 ατόμων 
****        "Το πρόβλημα της εκκένωσης κτηρίου προς την ταράτσα"
****
****        Μέλη Ομάδας:
****        Ελένη Βέρα                   18390152 
****        Χριστίνα Αχιλλεοπούλου       18390182
------------------------------------------------------------------------------"""
import copy

#Υπολογισμός αθροίσματος των ενοίκων που απομένουν στους ορόφους (1ος έως 4ος όροφος)
def tenants(state):
    total = sum(state[1:5])
    return total

#Συνάρτηση  ευρεσης απογόνων (find_children)
def find_children(state):
    children=[]
    #Κλήση τελεστή μετάβασης "Πήγαινε στον πρώτο όροφο"
    floor1_state=copy.deepcopy(state)
    floor1_child=go_to_floor1(floor1_state)
    #Κλήση τελεστή μετάβασης "Πήγαινε στον δεύτερο όροφο"
    floor2_state=copy.deepcopy(state)
    floor2_child=go_to_floor2(floor2_state)
    #Κλήση τελεστή μετάβασης "Πήγαινε στον τρίτο όροφο"
    floor3_state=copy.deepcopy(state)
    floor3_child=go_to_floor3(floor3_state)
    #Κλήση τελεστή μετάβασης "Πήγαινε στον τέταρτο όροφο"
    floor4_state=copy.deepcopy(state)
    floor4_child=go_to_floor4(floor4_state)
    #Κλήση τελεστή μετάβασης "Πήγαινε στην ταράτσα όροφο"
    roof_state=copy.deepcopy(state)
    roof_child=go_to_roof(roof_state)
    #Προσθήκη των παιδιών που δημιουργήθηκαν (αν δημιουργήθηκαν) απο τους τελεστές μετάβασης στην λίστα children
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

#Αρχικοποίηση ουράς
def make_queue(state):
    return [[state]]

#Επέκταση ουράς
def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")                                     #Εμφάνιση ουράς         
        print(queue)            
        node=queue.pop(0)                                   #Αφαίρεση της πρώτης κατάστασης απο την ουρά
        queue_copy=copy.deepcopy(queue)                     #Δημιουργία αντίγραφου της ουράς (queue_copy)
        children=find_children(node[-1])                    #Κλήση της συνάρτησης εύρεσης απογόνων 
        for child in children:                              #Επέκταση της ουράς 
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)                       #Εισαγωγή της διαδρομής στην αρχή της ουράς
    elif method=='BFS':
        print("Queue:")                                     #Εμφάνιση ουράς  
        print(queue)
        node = queue.pop(0)                                 #Αφαίρεση της πρώτης κατάστασης απο την ουρά
        queue_copy = copy.deepcopy(queue)                   #Δημιουργία αντίγραφου της ουράς (queue_copy)
        children = find_children(node[-1])                  #Κλήση της συνάρτησης εύρεσης απογόνων 
        for child in children:                              #Επέκταση της ουράς 
            path = copy.deepcopy(node)                      
            path.append(child)
            queue_copy.append(path)                         #Προσθήκη της διαδρομής στο τέλος της ουράς
    elif method=='HC':
        print("Queue:")                                     #Εμφάνιση ουράς  
        print(queue)    
        node = queue.pop(0)                                 #Αφαίρεση της πρώτης κατάστασης απο την ουρά
        queue_copy = copy.deepcopy(queue)                   #Δημιουργία αντίγραφου της ουράς (queue_copy)
        children = find_children(node[-1])                  #Κλήση της συνάρτησης εύρεσης απογόνων
        for child in children:                              #Επέκταση της ουράς 
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)                      #Εισαγωγή της διαδρομής στην αρχή της ουράς
    return queue_copy

#Αρχικοποίηση μετώπου
def make_front(state):
    return [state]

#Επέκταση μετώπου
def expand_front(front, method):  
    if method=='DFS':                                       #DFS
        if front:                                           #Αν το μέτωπο δεν είναι κενό 
            print("Front:")
            print(front)                                    #Εμφάνιση μετώπου 
            node=front.pop(0)                               #Βγάζω την κατάσταση node απο το μέτωπο 
            for child in find_children(node):               #Κλήση συνάρτησης εύρεσης απογόνων (βρίσκω τα παιδία της κατάστασηε node)
                front.insert(0,child)                       #Προσθέτω τα παιδιά της node στην αρχή του μετώπου 
    elif method=='BFS' :                                    #BFS
        if front:                                           #Αν το μέτωπο δεν είναι κενό 
            print("Front:")                         
            print(front)                                    #Εμφάνιση μετώπου 
            node = front.pop(0)                             #Βγάζω την κατάσταση node απο το μέτωπο
            for child in find_children(node):               #Κλήση συνάρτησης εύρεσης απογόνων (βρίσκω τα παιδία της κατάστασηε node)
                front.append(child)                         #Προσθέτω τα παιδιά της node sto τέλος της λίστας.
    elif method=='HC':                                      #HC
        if front:                                           #Αν το μέτωπο δεν είναι κενό 
            print("Front:")
            print(front)                                    #Εμφάνιση μετώπου 
            children = []                           
            node = front.pop(0)                             #Βγάζω την κατάσταση node απο το μέτωπο
            for child in find_children(node):               #Κλήση συνάρτησης εύρεσης απογόνων (βρίσκω τα παιδία της κατάστασης node)
                children.append(child)                      #Αποθεκεύω τα παιδία της κατάστασης node στην λίστα children
            if children != 0:                               #Αν η λίστα children δεν είναι κενή 
                i = len(children)                           #Βρίσκω το μέγεθος της λίστας 
                sort_children=sorted(children,key=tenants)  #Ταξινομώ τα παιδία με βάση της συνάρτηση tenants και τυα αποθηκεύω στην λίστα sort_children
                for z in range(i):                          
                    front.insert(z, sort_children[z])       #Προσθέτω τα ταξινομημένα παιδια στο μέτωπο 
    return front

#Τελεστές μετάβασης 
#Τελεστής μετάβασης Πήγαινε στον πρώτο όροφο
def go_to_floor1(state):
    if state[5]<8 and state[1]>0 and state[0]!=1:
        if state[1]>8-state[5]:
            new_state = [1] + [state[1] + state[5] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[5]]
        return new_state
#Τελεστής μετάβασης Πήγαινε στον δεύτερο όροφο        
def go_to_floor2(state):
    if state[5]<8 and state[2]>0 and state[0]!=2:
        if state[2]>8-state[5]:
            new_state = [2] + [state[1]] + [state[2] + state[5] - 8] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2]+ [state[1]] + [0] + [state[3]] + [state[4]] + [state[2] + state[5]]
        return new_state
#Τελεστής μετάβασης Πήγαινε στον τρίτο όροφο
def go_to_floor3(state):
    if state[5]<8 and state[3]>0 and state[0]!=3:
        if state[3]>8-state[5]:
            new_state = [3] + [state[1]] + [state[2]] + [state[3] + state[5] - 8] + [state[4]] + [8]
        else:
            new_state = [3] + [state[1]] + [state[2]] + [0] + [state[4]] + [state[3] + state[5]]
        return new_state
#Τελεστής μετάβασης Πήγαινε στον τέταρτο όροφο
def go_to_floor4(state):
    if state[5]<8 and state[4]>0 and state[0]!=4:
        if state[4]>8-state[5]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4] + state[5] - 8] + [8]
        else:
            new_state = [4]  + [state[1]] + [state[2]] + [state[3]] + [0] + [state[4] + state[5]]
        return new_state
#Τελεστής μετάβασης Πήγαινε στην ταράτσα
def go_to_roof(state):
    if state[5]==8 or (state[1]==0 and state[2]==0 and state[3]==0 and state[4]==0) and state[1]!=5:
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
    else :
        new_state=None    
    return new_state

def find_solution(front, queue, closed, goal, method):
    if not front:                                                                   #Αν τον μέτωπο είναι κενό
        print('_NO_SOLUTION_FOUND_')                                                #Δεν βρέθηκε λύση
    
    elif front[0] in closed:                                                        #Αν η πρώτη κατάσταση του μετώπου είναι στις κλειστές καταστάσεις
        new_front=copy.deepcopy(front)                                              
        new_front.pop(0)                                                            #Αφαίρεση της πρώτης κατάστασης απο το μέτωπο 
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)                                                            #Αφαίρεση της πρώτης κατάστασης απο την ουρά
        find_solution(new_front, new_queue, closed, goal, method)                   #Κλήση της συνάρτησης με το μειωμένο μέτωπο
    elif front[0]==goal:                                                            #Αν το μέτωπο ισούται με τον goal 
        print('_GOAL_FOUND_')                                                       #Βρέθηκε λύση   
        print()                                                             
        print(front[0])                                                             #Εμφάνισε το μέτωπο και την ουρά
        print(queue[0])
    else:
        closed.append(front[0])                                                     #Προσθήκη της πρώτης κατάστασης του μετώπου στις κλειστές
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)                             #Επέκταση μετώπου 
        queue_copy=copy.deepcopy(queue)                             
        queue_children=extend_queue(queue_copy, method)                             #Επέκταση ουράς
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)    #Κλήση της συνάρτησης με τα νέα μετώπο και ουρά

#Συνάρτηση επιλογής μεθόδου αναζήτησης
def select_method(): 
    while(1):
        #Επιλογή απο τον χρήστη μεταξύ των αλγορίθμων BFS,DFS και HC για την επίλυση του προβλήματος.
        print("This program solves the problem of evacuating a building to the roof using different searching algorithms.")
        print("Select between the given searching algorithms:")
        print("1. DFS (Depth First Search)\n2. BFS (Breadth First Search)\n3. HC (Hill Climbing)\n4. Exit")
        print("Select option:")
        option= input()
        if option=="1" :
            method="DFS"
            break
        elif option=="2":
            method="BFS"
            break
        elif option=="3":
            method="HC"
            break
        elif option=="4":
            print("Exiting...")
            exit()
        else:
            print("Wrong input.") 
    return method

def main():
    #Αρχική κατάσταση 
    initial_state = [0, 9, 4, 12, 7, 0] 
    #Τελική Κατάσταση (Στόχος)
    goal = [5, 0, 0, 0, 0, 0] 

    #Κλήση συνάρτησεις επιλογής μεθόδου
    method=select_method()
      
    print("Begin Searching\n---",method,"---")
    #Κλήση της συνάρτησης find_solution για την εύρεση λύσης 
    find_solution(make_front(initial_state),make_queue(initial_state),[],goal,method)
        
if __name__ == "__main__":
    main()