import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_collection'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    data = []
    with open("data/dish.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("recipes.html", page_title='Recipes', dish=data, recipes=mongo.db.recipes.find())
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())   


@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)