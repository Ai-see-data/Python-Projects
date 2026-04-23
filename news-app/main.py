import requests
from send_email import send_email

topic = "AI OR artificial intelligence OR machine learning"
sources = "techcrunch,the-verge,wired,ars-technica"
api_key="85fbf459e010401a99c6dc767d4db97b"
URL="https://newsapi.org/v2/everything?"\
    f"sources={sources}&"\
    f"q={topic}&" \
    "sortBy=publishedAt&"\
    "language=en&"\
    "apiKey=85fbf459e010401a99c6dc767d4db97b"


#make request
request = requests.get(URL) #sends http get req to newsapi and newsapi prepares the response in JSON

#get a dict w data
content = request.json() # parses json data into something python can work with ( dict DS )
#print(content)

#print(type(content)) shows dict after including json - to extract data, we need a data structure
#Access the article's content like title and desc
#Build email body
mail=" "
for article in content["articles"][:20]:
    if article['title'] is not None:
        mail += f"{article['title']}\n"
        mail += f"{article['description']}\n"
        mail += f"{article['url']}\n"
        mail += "-"*100 + "\n\n"

#mail = mail.encode("utf-8")
send_email(subject="What's happening in AI today?", body=mail, to_email="aishuk3@gmail.com")

#img="https://upload.wikimedia.org/wikipedia/commons/6/64/Dall-e_3_%28jan_%2724%29_artificial_intelligence_icon.png"
#res=requests.get(img)
#with open("img.jpg", 'wb') as file:
    #file.write(res.content)


