#a-z , 0-9 , ._time , @ must 1, . 2and 3 pos
import re 
#^ condtion for start position
#+ merge condition
#\ search character
#? 1=true else false i.e work with 0 and 1 so 2==false
#\w search string 
#{} position
#$ from last postion
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter Email: ")
if re.search(email_condition,user_email):
    print("right email")
else:
    print("Wrong email")
