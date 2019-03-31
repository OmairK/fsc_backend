import random

def cien_id_generator(name,dob, *args): ## DOB FORMAT : DDMMYYYY
    name = name.split()
    namecode ="{}{}".format(name[0][0],name[1][0]) 
    c1 = int(dob/100000)
    c2 = int(dob%100)
    c3 = int(dob/10000)%10
    numstr = random.randint(1000,9999)
    cien ="{}{}{}{}{}".format(c1,numstr,c3,c2,namecode)
    return(cien)








