import random


schar_for_pass=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cchar_for_pass=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_for_pass=['1','2','3','4','5','6','7','8','9','0']
sp_for_pass=['@','!','#','$']

pass_len=0

while pass_len<6:
    pass_len= int(input('Enter the length of your password: '))
       
    if pass_len<6:
        print('\nPassword would be too weak. Atleast greater than 6\n')


def pass_sel():
    return random.randint(1,4)

def pass_select():
    n=pass_sel()
    
    if n==1:
        return random.choice(schar_for_pass)
    elif n==2:
        return random.choice(cchar_for_pass)
    elif n==3:
        return random.choice(num_for_pass)
    else:
        return random.choice(sp_for_pass)




password=[]

def pass_creater():
   
    for i in range(pass_len):
        password.append(pass_select())

pass_creater()

final_pass=''

for j in password:
    final_pass +=j

print(f'\n\nYour password is: {final_pass}')
