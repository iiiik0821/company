from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/structure')
def structure():
    return render_template('structure.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/support')
def support():
    return render_template('support.html')

if __name__ == '__main__':
    app.run(debug=True)