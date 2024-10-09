import random

a1, a2, a3,b1, b2, b3,c1, c2, c3 = ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' '

c = 'x'
h = 'o'

while True:
    print(a1,"|",a2,"|",a3)
    print(b1,"|",b2,"|",b3)
    print(c1,"|",c2,"|",c3)
    print('-' * 10)

    pos = [(a1, a2, a3), (b1, b2, b3), (c1, c2, c3),  
           (a1, b1, c1), (a2, b2, c2), (a3, b3, c3),  
           (a1, b2, c3), (a3, b2, c1)]
    
    win = False
    for condition in pos:
        if condition[0] == condition[1] == condition[2] and condition[0] != ' ':
            win = True
            break

    if win:
        if c=="x":
            print("Computer Wins")
        else:
            print("Human wins")
        break
       
    if all(pos != ' ' for pos in (a1, a2, a3, b1, b2, b3, c1, c2, c3)):
        print("Draw")
        break

    while True:
        p = random.randint(1, 9)
        if p == 1 and a1 == ' ':
            a1 = c
            break
        elif p == 2 and a2 == ' ':
            a2 = c
            break
        elif p == 3 and a3 == ' ':
            a3 = c
            break
        elif p == 4 and b1 == ' ':
            b1 = c
            break
        elif p == 5 and b2 == ' ':
            b2 = c
            break
        elif p == 6 and b3 == ' ':
            b3 = c
            break
        elif p == 7 and c1 == ' ':
            c1 = c
            break
        elif p == 8 and c2 == ' ':
            c2 = c
            break
        elif p == 9 and c3 == ' ':
            c3 = c
            break

    print(a1,"|",a2,"|",a3)
    print(b1,"|",b2,"|",b3)
    print(c1,"|",c2,"|",c3)
    print('-' * 10)

    win = False
    for condition in pos:
        if condition[0] == condition[1] == condition[2] and condition[0] != ' ':
            win = True
            break

    if win:
        if c=="x":
            print("Computer Wins")
        else:
            print("Human wins")
        break
    
            

    if all(pos != ' ' for pos in (a1, a2, a3, b1, b2, b3, c1, c2, c3)):
        print("Draw")
        break

    while True:
        p = int(input("Enter position (1-9): "))
        if p == 1 and a1 == ' ':
            a1 = h
            break
        elif p == 2 and a2 == ' ':
            a2 = h
            break
        elif p == 3 and a3 == ' ':
            a3 = h
            break
        elif p == 4 and b1 == ' ':
            b1 = h
            break
        elif p == 5 and b2 == ' ':
            b2 = h
            break
        elif p == 6 and b3 == ' ':
            b3 = h
            break
        elif p == 7 and c1 == ' ':
            c1 = h
            break
        elif p == 8 and c2 == ' ':
            c2 = h
            break
        elif p == 9 and c3 == ' ':
            c3 = h
            break
        else:
            print("Not Free. Please enter another position (1-9): ")
