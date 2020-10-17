from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    username = request.form['username']
    processed_text = username.upper()
    return f'Hi {processed_text}'



if __name__ == '__main__':
    app.run(debug=True, port=8083)

