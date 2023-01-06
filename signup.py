import hashlib
import re
import menu
import create
def signup():   
#----------------------open file to append data---------------
  f = open("data","a")
#--------------------name-------------------------------------
  f_name = input("Enter Your First Name:")
  l_name = input("Enter Your Last Name:")
  while not f_name.isalpha() & l_name.isalpha():
      print("Enter String ")
      f_name = input("Enter Your First Name:")
      l_name = input("Enter Your Last Name:")
  else: 
      print("successaful name",f_name+" "+l_name)
   #------------------------email--------------------------------
  email = input("Enter Your Email:")
  while not (re.fullmatch("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email)):
    print("Enter Valid Email")
    email = input("Enter Your Email:")
  else:
    print("valid mail")
   #-----------------------------password---------------------------
  password = input("Enter Your Password:")
  conPassword = input("Enter Confirm password:")
  while password == conPassword :
      enc = conPassword.encode()
      hash = hashlib.md5(enc).hexdigest()
      print("Valid Password")
      break
  else:
      print("Please Enter Valid Password") 
   #------------------------------phone_Number--------------------------
  mob = input ("Enter Phone Number:")
  while not (re.fullmatch("^(\+201|01|00201)[0-2,5]{1}[0-9]{8}",mob)) and mob.isdigit() != True:
    print("Enter Egyption Num")
    mob = input ("Enter Phone Number:")
  else:
      print(" -_- Egyption Num -_- ") 
   #--------------------add data in file------------------------------------
  name = f_name +" "+ l_name   
  userinfo= f"{name}:{email}:{hash}:{mob}\n"    
  f.write(userinfo)   
  f.close()