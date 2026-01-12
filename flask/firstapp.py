from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/games')
def games ():
    return render_template('Games.html')

@app.route('/promos')
def promos ():
    return render_template('Promo.html')

@app.route('/register')
def register ():
    return render_template('Register.html')

@app.route('/about')
def about ():   
    return render_template('About.html')

@app.route('/contact')
def contact ():
    return render_template('Contact.html')

@app.route('/guide')
def guide ():
    return render_template('Guide.html')

@app.route('/ml')
def ml ():
    return render_template('MlTopUp.html')

@app.route('/codm')
def codm ():
    return render_template('CodmTopUp.html')

@app.route('/valorant')
def valorant ():
    return render_template('ValorantTopUp.html')

@app.route('/lol')
def lol ():
    return render_template('LolTopUp.html')

@app.route('/bs')
def bs ():
    return render_template('BsTopup.html')

@app.route('/genshin')
def genshin ():
    return render_template('genshintopup.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)