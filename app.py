from flask import Flask, render_template,request
from SDany5 import create_image
from translate import create_prompt

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prompt',methods=['GET','POST'])
def result():
    A=0
    if request.method == "GET":
        return render_template('prompt.html')
    elif request.method == "POST":
        Input_Chara = request.form['Input_Chara']
        Input_Job = request.form['Input_Job']
        Input_Do = request.form['Input_Do']
        prompt = create_prompt(Input_Chara,Input_Job,Input_Do)
        A=1
        result_img = create_image(prompt)
        return render_template('prompt.html',A=A)
        #return render_template('result.html',prompt=prompt,A=A)

if __name__ == "__main__": 
    app.run(debug=True)