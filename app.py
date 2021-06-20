
from mlModel import modelFile
import json
from flask import Flask, request, url_for, redirect, render_template
# import os
# os.environ["EAI_USERNAME"] = "devansh.sharma110@gmail.com"
# os.environ["EAI_PASSWORD"] = 'Devansh170501!'

myList=[]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Welcome():
    return render_template('Welcome_HTML.html')

@app.route('/templates/Form_HTML.html', methods=['GET', 'POST'])
def Form():
    if request.method == 'POST':
        return redirect(url_for('Welcome_HTML'))
        

    # show the form, it wasn't submitted
    return render_template('Form_HTML.html')

@app.route('/templates/result.html',methods = ['POST', 'GET'])
def result():

    text1 = request.form.get('text1')
    myList.append(text1)

    text2 = request.form.get('text2')
    myList.append(text2)

    text3 = request.form.get('text3')
    myList.append(text3)

    text4 = request.form.get('text4')
    myList.append(text4)

    text5 = request.form.get('text5')
    myList.append(text5)
    
    LIST= myList 
    A= modelFile(LIST)  
    return render_template("result.html",result = A)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
