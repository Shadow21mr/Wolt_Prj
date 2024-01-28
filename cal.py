import math 
from datetime import datetime



#ds stands for distance and shows the totall delivery cost 
#ds stands for delivery service and is equal to the cost of the delivery 
ds = []
#Cost is the cost of the whole shopping card / if more than 200€ then the delivery would be free
cost = 250

item_num = 5


#Here will determine based on the totall card "cost" if will have free delivery (if totall is equal or more than 200€ then will have free delivery)

if cost >=200:
    print("No Charges")
else:
    
#the delivery cost with the base 2€ and extra 1€ for each 500m after the first 1km will be calculated
    def cal(inp):
    
#Here will calculate if it only needs the base delivery charge 
        if (inp-1000) == 0 :
         ds.append(2)
#Here will be calculated if the distance is more than 1km and for each 500m will calculate an extra 1€         
        else:
            base=1
        for x in range(13) :
            if (int(inp)-1000-(int(x)*500)) >= 1 :
                ds.append(base)
                
        else:
            ds.append(2)
            
        print(sum(ds),"€")            
    









    cal(900)


print(datetime.utcnow())


