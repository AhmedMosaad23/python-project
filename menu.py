import signup
import login
import create
import showProject
import edit
import delete
import search
while True:
    print ("""
    1.Signup
    2.Login
    3.Create Project 
    4.show project
    5.edit data
    6.delete
    7.search by date
    """)
    ans=input("What would you like to do?")
    if ans=="1": 
      print(signup.signup()) 
    elif ans=="2":
      print(login.login()) 
    elif ans=="3":
      print(create.create()) 
    elif ans=="4":
      print(showProject.show())
    elif ans=="5":
      print(edit.edit()) 
    elif ans=="6":
      print(delete.delete()) 
    elif ans=="7":
      print(search.search())        
        