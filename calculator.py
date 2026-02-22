import math 
import sys


title= "*----calculator----*"
print(title.upper().center(30))
print("\n")


def valuechecking(a):
    
    if a.isdigit() :
        print(f"your digit is {a}\n")
    else:
        sys.exit('non-digit entered,exiting...\n')    
      

cond=input("(\"ON\" for using calci)(\"OFF\" for exiting):")
cond.lower()


while cond!="off":
    #input syntax for digits

    first=input("enter your first digit:")
    valuechecking(first)
    
    second=input("enter your second digit:")
    valuechecking(second)




    #syntax for input of symbols
    sym=input("enter your symbol:")
    print(f"your symbol is: {sym}\n")
    

    if sym=="/" or sym=="*" or sym=="+" or sym=="-" or sym=="**":
        print("your equation is:",first,sym,second)
    else:
        print("the",sym,"of numbers are:" )   



    sys.set_int_max_str_digits(1000000000)


    #simple functions
    if sym=="/":
        print("answer is:",int(first)/int(second)) #division
    elif sym=="*":
        print("answer is:",int(first)*int(second))        #multiplication
    elif sym=="+":
        print("answer is:",int(first)+int(second))        #addition 
    elif sym=="-":
        print("answer is:",int(first)-int(second))        #substraction  
    elif sym=="percentage":
        print("answer is:",(int(first)/int(second))*100)    #percentage 



    #extra functions
    #for making calculator scientific
    elif sym=="mean" :
        print("answer is:",(int(first)+int(second))/2)     #mean    
    elif sym=="**":
        print("answer is:",int(first)**int(second))        #power 
    elif sym=="reminder":
        print("answer is:",int(first)%int(second))        #reminder batana



    # syntax area for square root
    if sym=="square root":
        
        
        if second==0:
            print("√",first,"is:", math.sqrt(int(first)))
        elif first==0:
            print("√",second,"is:", math.sqrt(int(second)))
        else:
            print("√",first,"is:", math.sqrt(int(first)))
            print("√",second,"is:", math.sqrt(int(second)))


    #for log
    elif sym=="log":        
                
        if second==0:
            print("log",first,"is:", math.log10(int(first)) )
        elif first==0:
            print("log",second,"is:", math.log10(int(second)) )
        else:
            print("log",first,"is:", math.log10(int(first)) )
            print("log",second,"is:", math.log10(int(second)) )


        
    #factorial
    if sym=="factorial":
        
        
        if second==0:
            print("factorial",first,"is:", math.factorial(int(first)))
        elif first==0:
            print("factorial",second,"is:", math.factorial(int(second)))
        else:
            print("factorial",first,"is:", math.factorial(int(first)))
            print("factorial",second,"is:", math.factorial(int(second)))

    
    ext=input("want to exit :")
    ext.lower()
    if ext=="yes":
        print("thnx for using💐")
        exit()
        print('\n')
    else:
        pass

else:
    exit()

    # trignometric functions
    # if cc=="sin":
        
        
    #     if bb==0:
    #           print("sin of",aa,"is:", math.sin(math.radians(float(aa))))
    #     elif aa==0:
    #     else:
    #           print("sin of",aa,"is:", math.sin(math.radians(float(aa))))
    #           print("sin of",bb,"is:", math.sin(math.radians(float(bb))))
            
              #power finding       