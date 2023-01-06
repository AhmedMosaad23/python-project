import signup
import re
def create():
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
   
    
   f = open("projects","a")       
   title=input("Enter Title for project :")
   details=input("Enter details about project :")
   total=input("Enter Target for project :")
   startdate = input("Enter start date for project>>yyyy-mm-dd : ") 
   while not (re.fullmatch("^(19|20)\d\d[-/.](0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])$",startdate)):
      print("Enter valid date")
      startdate = input("Enter start date for project>>yyyy-mm-dd : ")
   else:
      print("you enter start date -__-")
   enddate=input("Enter end date for project>>yyyy-mm-dd : ") 
   while not (re.fullmatch("^(19|20)\d\d[-/.](0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])$",enddate)):
      print("Enter valid date")
      enddate= input("Enter start date for project>>yyyy-mm-dd : ")
   else:
      print("you enter start date -__-") 
   projectinfo= f"email_user>{em}:Title>{title}:Details>{details}:Target>{total}:StartDate>{startdate}:EndDate>{enddate}\n"
   f.write(projectinfo)
   f.close()

