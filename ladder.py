def my_steps(n): 
    if n < 1 or n > 25:
        raise ValueError("Input out of bounds.")
    
    def recMySteps(n):
        if n <= 1:
            return 1
        return recMySteps(n-1) + recMySteps(n-2)
    
    return recMySteps(n)

#print(my_steps(4))