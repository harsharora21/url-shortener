from flask import Flask, redirect, request, render_template
from urllib.parse import urlparse
import string
import random

app = Flask(__name__)

mymap={}
#mymapback={}

def genUniqueHash():
    out = ''.join(random.choices(string.ascii_letters,k=6))
    while out in mymap:
        out = ''.join(random.choices(string.ascii_letters,k=6))
    return out

def shorten(bigUrl):
    smallUrl=genUniqueHash()
    mymap[smallUrl]=bigUrl
    return smallUrl

def longen(smallUrl):
    return mymap[smallUrl]

@app.route('/',methods=['GET','POST'])
def front():
    if request.method == 'POST':
        link = request.host + '/' + shorten(request.form['inpurl'])
        return 'The link is: ' + link
    return render_template('./index.html')

@app.route('/<code>')
def decode(code):
    code = str(code)
    if code in mymap:
        return redirect(longen(code))
    else :
        return '404 Not Found'

if __name__ == '__main__':
    app.run(port=5500,debug=True)