import requests

url = 'http://www.iheartquotes.com/api/v1/random'
resp = requests.get(url)
print(resp, resp.text)

resp = requests.get('http://localhost:9999/echo/Mothra')
if resp.status_code == 200 and resp.text == 'Say hello to my little friend: Mothra!':
    print("It worked! That almost never happens!")
else:
    print(f"Argh, got this: {resp.text}")
