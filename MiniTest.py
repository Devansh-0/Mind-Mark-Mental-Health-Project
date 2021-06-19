from flask import Flask, request, url_for, redirect, render_template
from mental_health_analyser import *


list=[]
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Welcome():
    return render_template('Welcome_HTML.html')

@app.route('/templates/Form_HTML.html', methods=['GET', 'POST'])
def Form():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
         return redirect(url_for('Welcome_HTML'))
    # show the form, it wasn't submitted
    return render_template('Form_HTML.html')

@app.route('/templates/result.html',methods = ['GET', 'POST'])
def result():

        text1 = request.form.get('text1')
        x= ABC(text1)
        return render_template("result.html",result = x)
    
      

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
