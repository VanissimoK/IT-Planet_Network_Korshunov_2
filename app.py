from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f'Привет, {name}! Ваш email: {email}'

@app.route('/about')
def about():
    return 'Это страница "О нас"'

if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0')
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True, host='0.0.0.0', port=5000)