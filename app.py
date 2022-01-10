from flask import Flask, render_template, request, redirect, url_for
from skimage.io import imread
from PIL import Image
import pytesseract
import re

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = './vendor/tesseract-ocr/bin/tesseract'

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = './vendor/tesseract-ocr/bin/tesseract'

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print('file uploaded')
        img=Image.open(uploaded_file)
        data=pytesseract.image_to_string(img,lang='eng',config='--psm 6')
        pattern1=re.findall(r'[0-9]+ [0-9]+ [0-9]+',data)  
        print(pattern1)

        return render_template('index.html',
                                   msg='Successfully processed',
                                   extracted_text=pattern1)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)


