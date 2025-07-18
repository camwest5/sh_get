import requests

r = requests.get("https://api.library.uq.edu.au/v1/training_events?take=100&filterIds[]=104&ts=1745812216416")

body = r.content

with open("payload.json", "w") as f:
  f.write(body)
