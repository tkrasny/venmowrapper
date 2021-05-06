from venmo_api import Client

if __name__ == '__main__':
    userList = []

    venmo = Client(access_token="")

    my_user_id = venmo.user.get_my_profile().id
    print(my_user_id)
    users = venmo.user.get_user_friends_list(user_id=my_user_id)
    for user in users:
        userList.append(user)

    for user in userList:
        print(user.username, user.first_name, user.last_name)