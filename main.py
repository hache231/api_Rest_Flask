from flask import Flask
import json
import random

app = Flask(__name__)

@app.route("/get-fruit", methods= ['GET'])
def getFruit():
    listFruit = ['mangue','avocat','orange','banane']
    choiseFruit = listFruit[random.randint(0,3)]
    return json.dumps({"fruit":choiseFruit})


if __name__ == '__main__':
    app.run(debug=True)


