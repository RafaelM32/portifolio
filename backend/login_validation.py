import json
import pandas as pd
import hashlib
def verify_login(login):
    #open users data file

    data = pd.read_csv("users_data.csv")
    
    #verifying login
    if login["email"] in data["email"].unique():
        hash_user = data[(data["email"] == login["email"])]["hash"].unique()[0]
        if hash_user_login(login) == hash_user:
            name = data[(data["email"] == login["email"])]["name"].unique()[0]
            return {"resp": True, "name": name}
        else:
            return {"resp": False}
    else:
        return {"resp": "user_not_found"}





#create a new account

def create_new_account(user_data):
    data = pd.read_csv("users_data.csv", dtype={"id":str})
    if len(data) == 0:
        user_data["id"] = '0000000'
        user_data["status"] = "admin"
        user_data['hash'] = hash_user_login(user_data)
        data.loc[len(data)] = user_data
        data.to_csv("users_data.csv", index=False)
        return {"resp": True}
    else:
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
            user_data["hash"] = hash_user_login(user_data)
            data.loc[len(data)] = user_data
            data.to_csv("users_data.csv", index=False)
            return {"resp": True}
        else:
            return {"resp": False, "notification": "username alrely registred"}


#making a hash of login and password


def hash_user_login(user_data):
    login = user_data['email'] + user_data['password']
    hash_login = hashlib.sha256(login.encode('utf-8'))
    return hash_login.hexdigest()
