
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenue sur Moayé Boutique - Paradis des enfants</h1><p>Nos produits mixtes arrivent bientôt !</p>"

#if __name__ == "__main__":
    #app.run(debug=True)
