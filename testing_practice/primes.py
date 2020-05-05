def is_prime(number):
    if number <= 1:
        return False
    if type(number) != int:
        raise ValueError
    else:
        for element in range(2,number):
        
            if number % element ==0:
                return False
    
    return True