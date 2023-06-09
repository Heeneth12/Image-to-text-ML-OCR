from flask import Flask, render_template,request,redirect,url_for
import random
import urllib.request
import pytesseract
from os import getenv

app = Flask(__name__)

@app.route('/')
def sai():
    return render_template('index.html')

@app.route('/submit', methods=['POST','GET'])
def url_reader():
    text= ''
    if request.method=='POST':
        url_str=request.form['URL']
        code = random.random()
        image_url = url_str
        filename = (f'img{code}.png')
        req = urllib.request.build_opener()
        req.addheaders = [('user-Agent','Mozilla/5.0 (Windows NT 6.1; wow64)')]
        urllib.request.install_opener(req)
        urllib.request.urlretrieve(image_url,filename)

        # pytesseract.pytesseract.tesseractcmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        #print(pytesseract.image_to_string(filename))
        text = pytesseract.image_to_string(filename)
        #return 0

        return str(text)
        #return pytesseract.image_to_string(image_url)
    
if __name__==('__main__'):
    isDebug= True if getenv('Prod')=='Yes' else False
    app.run(debug=isDebug,host='0.0.0.0')