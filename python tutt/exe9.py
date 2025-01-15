# akbhar padke sunao
import requests
from win32com.client import Dispatch

news = requests.get("https://newsapi.org/v2/everything?q=Apple&from=2022-11-16&sortBy=popularity&apiKey=f52de4feb7534261a5f31836dbbc947d")
newreq = news.json()
allArticle = newreq['articles']

result = []

for i in allArticle:
    result.append(i['title'])

# for item in result:
#     print(item)

for j in range(len(result)):
    print(f"({j+1}", result[j])

if __name__ == '__main__':
    i = 0
    while (i < len(result)):
        speak = Dispatch("SAPI.SpVoice")
        speak.speak(f"{str(i+1)} news is {result[i]}")
        i= i+1


# print(r.text)
# print(r.content)
# print(r.)



# def speak(str):
#     from win32com.client import Dispatch
#
#     speak = Dispatch("SAPI.SpVoice")
#
#     speak.speak(str)
#
# if __name__ == '__main__':
#     speak("what are you doing now")