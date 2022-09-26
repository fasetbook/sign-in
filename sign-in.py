a=3
name=["jack","mili","james","meiya","Hacker","king"]
pwd=["jack888","mili777","james666","meiya555","king1474457##$"]
jack1='888'
mili='777'
james='666'
meiya='555'

for i in range(3):
    namesr=input('Please enter your username:')
    if namesr in name:  #The user name exists and continues to enter the password.
        pwdsr=input('Please enter password:')
        if namesr+pwdsr in pwd:
            print('Welcome to the popular server')
            break
        else:
            a-=1
            print('Account or password error,You have '+str(a)+' more opportunities\n')

    else:
        a-=1
        print('The account doesn't exist! You have'+str(a)+'more opportunities\n')
