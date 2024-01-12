from flask import Flask, render_template,request, jsonify
from SDany5 import create_image
from translate import create_prompt

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prompt',methods=['GET','POST'])
def prompt():
    if request.method == "GET":
        return render_template('prompt.html')
    elif request.method == "POST":
        return render_template('prompt.html')

@app.route('/result',methods=['POST'])
def result():
        Input_Chara = request.form['Input_Chara']
        Input_Job = request.form['Input_Job']
        Input_Do = request.form['Input_Do']
        prompt = create_prompt(Input_Chara,Input_Job,Input_Do)
        return render_template('result.html',prompt=prompt)


@app.route("/generate_image", methods=["POST"])
def generate_image():
    prompt = request.form["prompt"]
    successFlag, file_name = create_image(prompt=prompt)
    if successFlag:
        return jsonify({"file_name": file_name})
    else:
        return jsonify({"error": f"Error: {file_name}"})

if __name__ == "__main__": 
    app.run(debug=True)