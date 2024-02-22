import time

def converting_into_fr(formula2 , formula1):
    fr = float (input("enter the value of Fahrenheit that you want to convert into celsius "))
    ce = (fr - formula2 ) * formula1
    print('converting....')
    time.sleep(0.6)
    print ("the temprature in celsius is :" , ce)
    asking()

def converting_into_cs(formula3 , formula2) :
    cs = float(input("enter the value of Celsius that you want to convert into Fahrenheit"))
    fa = (cs * formula3) + formula2
    print('converting....')
    time.sleep(0.6)
    print ("the temprature in fahrenheit is :" , fa)
    asking()

def asking() :
    formula1 = 5/9
    formula2 = 32
    formula3 = 9/5
    choice = input("press (f) if you want to convert fahrenheit into celsius or press (c) if you want to convert celsius into fahrenheit or press (q) to quite :  ")
    if choice.lower() == "f" :
        converting_into_fr(formula2 , formula1)
    elif choice.lower() == "c" :
        converting_into_cs(formula3 , formula2)
    elif choice.lower() == 'q':
        pass
    else : 
        print ("invalid input , pls try again ")
        asking()
asking()