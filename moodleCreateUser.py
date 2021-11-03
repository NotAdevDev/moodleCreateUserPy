import requests

token = 'YOUR_TOKEN_HERE'
function='core_user_create_users'
url = 'https://YOUR_URL_HERE/webservice/rest/server.php?wstoken={0}&wsfunction={1}'.format(token, function) #&moodlewsformat=json
users = {"users[0][username]": "newusername",
           "users[0][email]": "new@user.com",
           "users[0][lastname]": "UserLastName",
           "users[0][firstname]": "UserFirstName",
            "users[0][auth]": "shibboleth",
            "users[0][customfields][0][type]": "FieldId",
            "users[0][customfields][0][value]": "FieldValue",
     }

response = requests.post(url,params=users)
print(response.status_code)
print(response.content)
