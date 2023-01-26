from user import *
from post import *

print("All about User Class")
app_user_one =  User("emilio@yahoo.es", "Emilio Barrera", "pwd1","DevOps Engineer")     
app_user_one.get_user_info()
print()

app_user_one.change_job_title("DevOps trainer")
app_user_one.get_user_info()
print()
app_user_three = User("eeeee@ya.com","jaime  loca","dasdasdsad","Python")
app_user_three.get_user_info()
print()

print("all about Post Class")
app_post_one = Post("Los pero pocos","Emilio")
app_post_one.get_post_info()
print()
app_post_two = Post("The lord of the ring", app_user_one.name)
app_post_two.get_post_info()
