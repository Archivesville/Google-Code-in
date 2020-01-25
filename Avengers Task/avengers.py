import math

T = int(input(""))
for i in range(T):
    P = int(input(""))
    N = math.floor(math.sqrt(8*P)/2)
    n_values = []

    if P == 1 or P == 2:
        print('IRON MAN')


    elif P == 3 or P == 4:
        print('CAPTAIN AMERICA')


    else:
        for n in range(N - 2, N + 2):
            score1 = 2*((n/2)**2)-1 + n
            score2 = ((n**2)-1)/2 + n

            if score1.is_integer() == True:
                if score1 >= P or score1 + 1 >= P:
                    n_values.append(n)

            if score2.is_integer() == True:
                if score2 >= P or score2 + 1 >= P:
                    n_values.append(n)  

  
        if n_values[0] % 2 == 0:
            print('CAPTAIN AMERICA')


        elif n_values[0] % 2 == 1:
            print('IRON MAN')
