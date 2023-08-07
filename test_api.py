import requests

print(requests.get("http://127.0.0.1:8000/").json())

# print(requests.get("http://127.0.0.1:8000/genero/2015").json())

# print(requests.get("http://127.0.0.1:8000/juegos/2017").json())

# print(requests.get("http://127.0.0.1:8000/specs/2000").json())

# print(requests.get("http://127.0.0.1:8000/earlyaccess/2018").json())

# print(requests.get("http://127.0.0.1:8000/sentiment/2005").json())

# print(requests.get("http://127.0.0.1:8000/metascore/2000").json())

# prediccion_url = "http://127.0.0.1:8000/prediccion/?earlyaccess=true&sentiment=%27Mostly%20Positive%27&year=2018&genre=Action&genre=Casual&genre=Indie&genre=Simulation&genre=Strategy&tags=Strategy&tags=Action&tags=Indie&tags=Casual&tags=Strategy&specs=Single-Player"
# prediccion_url = "http://127.0.0.1:8000/prediccion/?earlyaccess=true&sentiment=%27Mostly%20Positive%27&year=2018&genre=Casual&genre=Indie&genre=Simulation&genre=Strategy&tags=Strategy&tags=Action&tags=Indie&tags=Casual&tags=Strategy&tags=Free%20to%20Play&specs=Single-Player"
prediccion_url = "http://127.0.0.1:8000/prediccion/?earlyaccess=true&sentiment=%27Mostly%20Positive%27&year=2018&genre=Casual&genre=Indie&genre=Simulation&genre=Strategy"
print(requests.get(prediccion_url).json())