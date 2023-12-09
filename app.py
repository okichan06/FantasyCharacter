from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def prompt():
    return render_template('index.html')

@app.route('/result')
def result():
    #この後画像を生成
    message = '準備中です。ちょっと待ってね'
    return render_template('result.html',msg=message)

if __name__ == "__main__": 
    app.run(debug=True)