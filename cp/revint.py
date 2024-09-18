def reverse_integer(num):
    reversed_num = 0
    is_negative = num < 0
    
    if is_negative:
        num = -num  
    
    while num > 0:
        digit = num % 10  
        reversed_num = reversed_num * 10 + digit 
        num //= 10  
    
    if is_negative:
        reversed_num = -reversed_num  
    
    return reversed_num


user_input = int(input('Enter an integer: '))
result = reverse_integer(user_input)
print('Reversed integer:', result)


