import signup
def delete():
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
   t=input("Enter Title project:")
   with open("projects", "r") as f:
      data = f.readlines()
        # open file in write mode
   with open("projects", "w") as f:
        for line in data :
            if line.strip(":") == t :
                f.write(line)