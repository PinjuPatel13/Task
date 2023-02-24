 # Gmail verification----

Email= input("Enter your Gmail id....")
print(Email)
k,j,b = 0,0,0
if  len(Email)>=6:
    

    if Email[0].isalpha():    
       
        if("@" in Email) and (Email.count("@")==1) :  

            
            if (Email[-10:-4]=="@gmail") ^ (Email[-9:-3]=="@gmail") and  (Email[-4]==".") ^ (Email[-3]=="."):  
              
                       
                
                    
                for i in Email:
                    if (i==i.isspace()):
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                         continue
                    elif i=="_" or i=="." or i=="@":
                         continue
                    elif i.isalnum():
                         continue
                    else:
                        b=1


                if k==1 or j==1 or b==1:
                    print("Wrong Email...first later is capital..")  
                else:
                    print("Right Email...")   
            else:
                print("Wrong Email, Enter valid Email id...")
        else:
            print("wrong Email,@ is reqiure...")
    
    else:
        print("Wrong Email frist charcter will be small later...")

else:
        print("Wrong Email Length is not statidfying...")

