How to install/start

Must be installed:

Python 3.6.2

git clone https://github.com/eugenykaminski/BBCResponder.git

cd BBCResponder/BBCResponder/spiders


Usage (start server):

python flask_ex1.py 

Examples:

http://localhost?chapter=XXX&news=YYY

http://localhost?chapter=sport&news=15

http://localhost?chapter=travel&news=5

http://localhost/?chapter=news&news=51

http://localhost/?chapter=news&news=2



# BBCResponder

BBC scrapping service

Need to create web service to get news titles and links from BBC website.

The endpoint of the service will receive following request by GET HTTP method:

http://localhost?chapter=XXX&news=YYY

Then it should get html page from the URL: 

https://www.bbc.com/XXX

Parce it given html to get YYY number of top news from the page and then return following JSON:

{
    "chapter" : "XXX",
    "news" : [
    {
      "title" : "<title of the news>",
      "URL" : "<link to the news>"
    }
    
}
For example for the request:

http://localhost?chapter=sport&news=3

The service will return a response like this:

{
    "chapter" : "sport",
    "news" : [
    {
      "title" : "Liam Williams: Full-back fit as Wales unchanged to face Ireland",
      "URL" : "https://www.bbc.com/sport/rugby-union/47568773"
    },
    {
      "title" : "Bayern Munich 1-3 Liverpool: Jurgen Klopp says Reds are among Europe's elite again",
      "URL" : "https://www.bbc.com/sport/football/47564048"
    },
    {
      "title" : "Sky Brown: The 10-year-old British skateboarder aiming to make history at Tokyo",
      "URL" : "https://www.bbc.com/sport/olympics/47523698"
    },
    
}

