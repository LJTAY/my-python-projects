print ("welcome to calculator")
print ("")

while True:
    
    print ("")
    
    print ("first digit[s]")
    try: Variable2 = int(input())
    except ValueError:
        print("input error")
        continue

    print ("choose function: + / x -")
    Variable1 = input()

    print ("second number")
    try: Variable3 = int(input())
    except ValueError:
        print("input error")
        continue

    if Variable1 == "+":
        print ("=",Variable2 + Variable3)
        
    elif Variable1 == "-":
        print ("=",Variable2 - Variable3)
        
    elif Variable1 == "x":
        print ("=",Variable2 * Variable3)
        
    elif Variable1 == "/":
        if Variable3 == 0:
            print  ("syntax error")
        else:
             print ("=",Variable2 / Variable3)
    else:
        print ("syntax error")