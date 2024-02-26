from os import system
user ={
    'username': 'johny777',
    'online'  : True,
    'email'   : 'johny777@lucky.me',
    'rating'  : 9345000609,
    'friends' :[
        'marry888',
        'candy001',
    ]
}

# Add some more friends from keyboard <- input +loop
# hint:  list.append(value)
# HW2: if+else  - arithmetic:
#       user['rating'] 0 ...10 000 000 000
#       0 -> No likes
#       1 ... 999 -> 999Likes
#       1000 ... 1000000 -> (123456 likes) -> 123 k
#       1000000 ... 1000000000 -> M xx.xxLikes
#       1 000 000 000 ... 10 000 000 000 -> T xx.xxLikes





# print user data

print(user['username'])
print(user['email'])
print('RATING')
if user['rating'] == 0:
    print('No likes')
elif 1<= user['rating'] <= 999:
    print(user['rating'])
elif 1000<= user['rating'] <= 1000000:
    likes = int(user['rating'] / 1000)
    print(likes, 'k')
elif 1000000<= user['rating'] <= 1000000000:
    likes = user['rating'] / 1000000
    print('M', round(likes,2), 'likes')
elif 1000000000<= user['rating'] <= 10000000000:
    likes = user['rating'] / 1000000000
    print('T', round(likes,2), 'likes')
#add friends to the list
while True:
    answer = input("Insert your friend's name ")
    if answer == "":
        break
    else:
        user['friends'].append(answer)
print('FRIENDS LIST')
for i in range(len(user['friends'])):
    print('>>>',user['friends'][i])


