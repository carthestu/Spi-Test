import time
start = 0

run = True
while run == True:        
    try :
        # Loop Code Snippet
        for i in range(start,100):
            time.sleep(2)
            print(i)
            start = i+1
    except :
        print("""~~~~~~~Code interupted~~~~~~~ 
        \n Press 1 to resume 
        \n Press 2 to quit""")
        res = input()
        if res == "1" :
            print("1")
            # pass and resume code
            pass
        if res == "2" :
            print("2") 
            #Save output and quit code
            run = False
        pass  #Safety pass if case user press invalid input
