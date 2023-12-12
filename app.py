from flask import Flask, render_template,request
from SDany5 import create_image
from translate import create_prompt

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
    A=0
    if request.method == "GET":
        return render_template('result.html')
    elif request.method == "POST":
        Input_prompt = request.form['Input_prompt']
        prompt = create_prompt(Input_prompt)
        A=1
        result_img = create_image(prompt)
        return render_template('result.html',result = result_img,A=A)
        #return render_template('result.html',prompt=prompt,A=A)

if __name__ == "__main__": 
    app.run(debug=True)