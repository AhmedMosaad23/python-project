import signup
import create
def edit():
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
   old=input("Enter data want edit it :") 
   new=input("Enter new data want replace it :")
   with open("projects","r") as f:
    newline=[]
    for word in f.readlines():        
        newline.append(word.replace(old,new)) 

   with open("projects","w") as f:
    for line in newline:
        f.writelines(line)
    file.close()    


