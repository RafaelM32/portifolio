import json

def send_projects(user_data):
    if user_data["email"] == "visitant":
        data = open("projects_visitant.json","r")
        projects_data = json.load(data)
        return projects_data



