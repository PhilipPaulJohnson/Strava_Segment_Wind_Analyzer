import pycurl
from io import BytesIO
import json 

client_id = '105518'
client_secret = '9096adc148e8a82c9d90a648c6814214c76129e3'
grant_type = 'authorization_code'
auth_code = 'bb18afb6238943a0ff8b4d657094a5571a6fb5c8'

if __name__ == "__main__":
    def nu_token(client_id,client_secret,grant_type,auth_code):
        data = {'client':client_id, 'client_secret':client_secret, 'code':auth_code, 'grant_type':grant_type}
        resp_data = json.dumps(data)

        url = 'https://www.strava.com/oauth/token?client_id=' + client_id + '&client_secret=' + client_secret + '&code=' + auth_code + '&grant_type=' + grant_type
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(pycurl.HTTPHEADER, ['Accept: application/json','Content-Type: application/json'])
        c.setopt(pycurl.POSTFIELDS, resp_data)
        c.setopt(c.WRITEDATA, buffer)
        #c.setopt(c.VERBOSE, 1)
        c.perform()
        c.close()

        body = buffer.getvalue()
        body.decode('iso-8859-1')
        body = json.loads(body)
        # print(body)
        print('\n')
        print('SAVE THESE TOKENS')
        print('\n')
        refresh_token = body.get('refresh_token')
        print('refresh token: ' + str(refresh_token)) 
        print('\n')
        access_token = body.get('access_token')
        print('access_token: ' + str(access_token)) 
        print('\n')

    nu_token(client_id,client_secret,grant_type,auth_code)

refresh_token = 'f431f2d9917dedc8ad371253f1f53c47f0336cca'

access_token =  'f5b5d6090cde2d7c4978ce04d86fd1d00690171d'