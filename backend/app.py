import json
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/api/pokemon')
def index():
	data = {}
	name = ["bulbasaur", "charmander", "squirtle"]
	data["pokemon"] = name
	json_data = json.dumps(data)
	return json_data

@app.route('/api/pokemon/pokedex/<name>')
def pokedex(name):
    return render_template("pokedex.html",name=name)


if __name__ == '__main__':
    app.run(port=8006)