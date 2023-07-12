import json
import pandas as pd
def verify_login(login):
    #open users data file

    data = pd.read_csv("users_data.csv")
    
    #verifying login
    if login["email"] in data["email"].unique():
        senha = data[(data["email"] == login["email"])]["password"].unique()[0]
        if login["password"] == senha:
            name = data[(data["email"] == login["email"])]["name"].unique()[0]
            return {"resp": True, "name": name}
        else:
            return {"resp": False}
    else:
        return {"resp": "user_not_found"}





#create a new account

def create_new_account(user_data):
    data = pd.read_csv("users_data.csv", dtype={"id":str})
    if not (user_data["email"] in data["email"].unique()):
        user_data["status"] = "user"
        id = int(data.loc[len(data) - 1]["id"]) + 1
        if id/10 < 1:
            id = f"000000{id}"
        elif id/100 < 1:
            id = f"00000{id}"
        elif id/1000 < 1:
            id = f"0000{id}"
        elif id/10000 < 1:
            id = f"000{id}"
        elif id/100000 < 1:
            id = f"00{id}"
        elif id/1000000 < 1:
            id = f"0{id}"
        user_data["id"] = id
        data.loc[len(data)] = user_data
        data.to_csv("users_data.csv", index=False)
        return {"resp": True}
    else:
        return {"resp": False, "notification": "email alrely registred"}