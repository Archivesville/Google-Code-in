try:
    def divisorCheck(inp):
        rng = range(1, 1000001)
        dNums = []
        
        if inp in rng:
            for i in rng:
                if inp % i == 0:
                    dNums.append(1)    
            out = len(dNums)
            print(str(inp)+ " is divisible by " + str(out) + " numbers")
        else:
            print(str(inp) + " is not in range, try a different number")

    divisorCheck(int(input("Enter a Natural Number between 1 and 1,000,000: ")))

except ValueError:
    print("Only integers are accepted")