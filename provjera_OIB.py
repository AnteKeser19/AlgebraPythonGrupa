#emil

oib2=69588154538
kontrolni_oib=69435151530
oib1="02864160744" # preporučena verzija variable OIB

def oib_tester(oib: int) ->bool:
    """
    takes OIB as integer, 11digits,
    returns is it legitimate or not with bool (True/False)
    """
    try:
        oib_s=str(int(oib)) #tries if number can be interpreted as integer and after that string
        oib_s=str(oib)
    except: #if its not, print a message and returns False
        print("oib nije broj")
        return False
    
    if len(oib_s)==11: #tries if there is correct number of digits
        f=0 #last column defined as 0
        for a in range(len(oib_s)-1): 
            b=oib_s[a]
            b=int(b)+f
            c=b+10
            d=c%10
            if d==0:
                d=10
            e=d*2
            f=e%11
            #print(f)
        kont_znam=(11-f)%10
        if kont_znam==int(oib_s[10]):
            return True
        else:
            return False
    else:
        print("neispravna duljina OIBa")
        return False
    



if __name__=="__main__":
    print(f"{kontrolni_oib} je {oib_tester(kontrolni_oib)}")
    print(f"{oib1} je {oib_tester(oib1)}")
