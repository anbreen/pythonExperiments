
    
def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
       return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)



# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if 2>4 and 2==4:    # Start coding here!
        return False    
    elif False or False:
        return False
    else:
        return True
        # Keep going here.
        # You'll want to add the else statement, too!