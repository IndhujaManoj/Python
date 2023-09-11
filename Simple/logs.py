# users={}
# def register(username,password):
#     if (username in users) and (password in users):
#         print('this user is already exist')
#     else:
#         users[username]=password
#         print('user Added success fully')

# name = input('Enter your Name: ')
# password = input('Enter your Password: ')

# register(name,password)
# print(users)

users=[]

def registers(username,password):
    for user in users:
        if user['username']:username
        print('This user is alredy exist')
        return
    users.append({'username':username,'password':password})
    print('User Added Successfully')
name = input('Enter your Name: ')
password = input('Enter your Password: ')
registers(name,password)
print(users)
def login(username,password):
    for n in users:
        if n['username']==username and n['password']==password:
            print('login successfully')
        else:
            print('you entered wrong usename or password')
name1=input('Enter your name')
pass1=input('Enter your pass')
login(name1,pass1)
