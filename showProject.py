import signup
import create
def show():
   em=input("Enter your email :") 
   file= open("data","r")
   users=file.readlines()
   for u in users:
      signup.userinfo=u.strip("\n")
      signup.userinfo=signup.userinfo.split(":")
      if signup.userinfo[1]==em:
         print("Hello",signup.userinfo[0])
         break
   else:
     print("not found user name")  
   file.close() 

   f = open("projects","r")
   data = f.read()
   print(data)