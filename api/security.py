from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password): # checks if the user entered the correct password for a username
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): # 'safe_str_cmp' is used to compare different character encodings simply: comparing ASCII with Unicode will cause issues
        return user

def identity(payload): # returns the user details, acquired by ID
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)





### Udemy Section 5
# def authenticate(username, password): # checks if the user entered the correct password for a username
    # user = User.find_by_username(username)
    # if user and safe_str_cmp(user.password, password): # 'safe_str_cmp' is used to compare different character encodings simply: comparing ASCII with Unicode will cause issues
        # return user

# def identity(payload): # returns the user details, acquired by ID
    # user_id = payload['identity']
    # return User.find_by_id(user_id)





### Udemy Section 4
# users = [
    # User(1, 'bob', 'asdf')
# ]

# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

# def authenticate(username, password): # checks if the user entered the correct password for a username
    # user = username_mapping.get(username, None)
    # if user and safe_str_cmp(user.password, password): # 'safe_str_cmp' is used to compare different character encodings simply: comparing ASCII with Unicode will cause issues
        # return user

# def identity(payload): # returns the user details, acquired by ID
    # user_id = payload['identity']
    # return userid_mapping.get(user_id, None)
