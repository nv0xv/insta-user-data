import requests
import time
import os , sys


ss = requests.Session()
os.system('clear')
username = input('Enter Username -> ')
print('\n')
password = input('Enter Password -> ')
print('\n')

login_req_url = 'https://www.instagram.com/accounts/login/ajax/'


Login_Head = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '314',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=0HPX3KolK8ts5bweSn0eUT08PszgMa2J; mid=YPgcDAAEAAG23Wh45_CuLNCe8aiV; ig_did=FAF36BAA-4266-40B2-9EF9-BABEF060580E; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/?',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'x-asbd-id': '437806',
    'x-csrftoken': '0HPX3KolK8ts5bweSn0eUT08PszgMa2J',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'f3dd76b0436a',
    'x-requested-with': 'XMLHttpRequest',
}


Login_Data = {
    'username': username,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password
}


Login_SendR = ss.post(url=login_req_url, data=Login_Data, headers=Login_Head)
if '"authenticated":true' in Login_SendR.text:
    print('Login Done ; ')
    user_id = Login_SendR.cookies['ds_user_id']
    se = Login_SendR.cookies['sessionid']
    cr = Login_SendR.cookies['csrftoken']
    print('\n')
    print(f'Csrftoken -> : {cr}')
    print('\n')
    print(f'Sessionid -> : {se}')
    print('\n')
    print(f'user_id  -> : {user_id}')
    print('\n')
else:
    print('Login Faild ; ')
