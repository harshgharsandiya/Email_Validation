email=input("Enter Email: ")
#g@g.in , harshgharsandiya@gmail.com
k=0
if len(email)>=6:
    if email[0].isalpha():
        if ('@'in email) and (email.count('@')==1):
            if (email[-4]=='.') ^ (email[-3]=='.'):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper(): 
                           k=1
                    elif i.isdigit(): 
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        k=1    
                if k==1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1 ")