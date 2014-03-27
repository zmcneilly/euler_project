#!env/bin/python

amount = 100000
coins = [1,2,5,10,20,50,100,200]
ways = [0 for x in xrange(amount+1)] 
ways[0] = 1

for i in range(0, 8):
    for j in range(coins[i],amount+1):
        ways[j] = ways[j] + ways[j-coins[i]]

print ways[amount]
              
                
                
                          
                                
           
                      
                                      
                                    
                      
              

                     
