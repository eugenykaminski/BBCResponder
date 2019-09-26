#
# Usage:
# python flask_ex1.py 
# Examples:
# http://localhost?chapter=XXX&news=YYY
# http://localhost?chapter=sport&news=15
# http://localhost?chapter=travel&news=5
# http://localhost/?chapter=news&news=51
# http://localhost/?chapter=news&news=2


from flask import Flask
from flask import request
from subprocess import call
import subprocess
import json


from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from scrapy.crawler import CrawlerProcess



  # Format buffer like needed
def formatBUFF(chapter, bufferSTDOUT):

  # Create "news" list of dictionaries
  news=bufferSTDOUT.decode("utf-8").replace('url','URL').split('\r\n')

  # Create json like structure
  #  result={"chapter" : chapter, "news" : news }
  outStr='{"chapter" : "%s", "news" : %s }' %  (chapter, news[:-1])


  # Replace ordinary qoutes to double & etc,
  outStr='<pre>'+outStr.replace('\'','"').replace('"{','{').replace('"}','}')+'</pre>'
  # Create beauty output
  outStr=outStr.replace('[{','[\r\n{').replace( '}",' , '}",\r\n\r\n' ).replace('[{','[\r\n{')
  outStr=outStr.replace('", "','",\r\n  "').replace('] }',']\r\n}')

  return outStr



# Create flask application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():

    chapter=request.values['chapter']
    news   =request.values['news']

    # Set spider name for call
    spiderName = "BBC_Responder"

    # Get stdout and return to browsers
    # bufferSTDOUT=subprocess.check_output(['scrapy', 'crawl', spiderName])
    bufferSTDOUT=subprocess.check_output(['scrapy', 'crawl', spiderName,'-a','chapter='+chapter,'-a','news='+news])

    # format buffer like needed
    formattedBuffer=formatBUFF(chapter, bufferSTDOUT)
    return formattedBuffer





if __name__ == '__main__':
  app.run(host='127.0.0.1', port=80)
