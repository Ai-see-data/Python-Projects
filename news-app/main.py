import os
import requests
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from send_email import send_email
load_dotenv()


topic = "AI OR artificial intelligence OR machine learning"
sources = "techcrunch,the-verge,wired,ars-technica"
News_api_key=os.getenv("News_api_key")
Gemini_api_key=os.getenv("Gemini_api_key")

URL=("https://newsapi.org/v2/everything?"\
    f"sources={sources}&"\
    f"q={topic}&" \
    "sortBy=publishedAt&"\
    "language=en&"\
    "pageSize=8&"\
    + News_api_key
)
#make request
request = requests.get(URL) #sends http get req to newsapi and newsapi prepares the response in JSON
#get a dict w data
content = request.json() # parses json data into something python can work with ( dict DS )
#print(type(content)) o/p is 'dict' after including json() - to extract data, we need a data structure
articles= content["articles"]
#print(articles)
#Access the article's content like title and desc
#Build email body
def top_headlines():
    mail=" "
    for article in content["articles"][:20]:
        if article['title'] is not None:
            mail += f"{article['title']}\n"
            mail += f"{article['description']}\n"
            mail += f"{article['url']}\n"
            mail += "-"*100 + "\n\n"
#calling the custom send_email func        
    send_email(subject="What's happening in AI today?", body=mail, to_email="aishuk3@gmail.com")

#instead of sending all the articles to the user, we're gonna have AI analyze the Json data in content & mail it

#AI summarizing the news
def headlines_summary():

    model =init_chat_model(
        model="gemini-3-flash-preview", 
        model_provider="google-genai", 
        api_key=Gemini_api_key
    )
    prompt = f"""You're a news summarizer.
    Write two short paragraphs analyzing those news, aiding someone to go over the news during their morning coffee.
    Here are the news articles: {articles}
    """
    response = model.invoke(prompt)
    response_str=response.content[0]['text']

    send_email(subject="Good Morning, Today's AI news summary", body=response_str, to_email="aishuk3@gmail.com") #calling the custom send_email func


top_headlines()
headlines_summary()

