my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

for my_ver in my_list:
    print(my_ver)

for i in "abc":
    print(i)

for x in range(0, 10):
    print(x)

user_1 = {'username': 'bolognahead', 'id': 1}
user_2 = {'username': 'smichae5', 'id': 2}
user_3 = {'username': 'harlan', 'email': 'harlan@wd34.com', 'id': 3}


my_users = [user_1, user_2, user_3]
for user in my_users:
    print(user)

for user in my_users:
    print(user['username'])

for user in my_users:
    if 'email' in user:
        print(user['email'])

selected_user = {}
my_user_lookup = 2
for user in my_users:
    if 'id' in user:
        if user['id'] == my_user_lookup:
            selected_user = user
print(selected_user)

for x in range(0, 10):
    for user in my_users:
        if user['id'] == x:
            print(user)