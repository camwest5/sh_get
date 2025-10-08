import requests

r = requests.get("https://api.library.uq.edu.au/v1/training_events?take=100&filterIds[]=104&ts=1745812216416",
                 headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0"})

body = r.content.decode()

with open("payload.json", "w") as f:
  f.write(body)
