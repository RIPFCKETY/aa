from user_agent import generate_user_agent

with open("UserAgent.txt", "w+") as file:
    for i in range(10000000): 
        file.write(generate_user_agent() + "\n") 
    
    with open("UserAgent.txt", "r") as file:
        lists = file.readlines()
        
#print("\n"+str(lists)+"\n")
    #داره میسازه
    # که اینطور