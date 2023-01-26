
class User:      
    def __init__(self,user_email,name, password, currentt_job_title):
        self.email = user_email 
        self.name = name 
        self.password = password
        self.current_job_title = currentt_job_title 

    def change_password(self, new_password):
        self.password  = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"{self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}, with password: {self.password}")


