# the first I nedd to install this  package https://pypi.org/project/requests/ for use the api in Python:
import requests

print
response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
print()
#print(f"{response.json()}")
#print()
#print(type(response.json()))
#print()
#print(response.json()[0])
my_projects = response.json()

for project in my_projects:
    print(f" Project Name: {project['name']}\n and Project Url: {project['web_url']}\n")
