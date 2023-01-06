import hashlib
import signup
def login():
   em=input("Enter email:")
   pa=input("Enter pass:")
   auth = pa.encode()
   hash = hashlib.md5(auth).hexdigest()
   file= open("data","r")
   users=file.readlines()
   for u in users:
      signup.userinfo=u.strip("\n")
      signup.userinfo=signup.userinfo.split(":")
      if signup.userinfo[1]==em and signup.userinfo[2]==hash:
         print("Hello",signup.userinfo[0])
         break
   else:
     print("not found user name")  
   file.close() 