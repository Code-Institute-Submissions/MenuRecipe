import os
import json
import math
from flask import Flask, render_template, redirect, request, url_for
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_collection'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
        data = []
        with open("data/dish.json", "r") as json_data:
            data = json.load(json_data)
        return render_template("recipes.html", page_title='Index', dish=data, recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find())
                            
                            
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())
                           

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'recipe_author':request.form.get('recipe_author'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_date': request.form.get('recipe_date'),
        'recipe_desc': request.form.get('recipe_desc'),
        'recipe_ing': request.form.get('recipe_ing'),
        'recipe_prep': request.form.get('recipe_prep'),
        'recipe_inst': request.form.get('recipe_inst'),
        'recipe_notes': request.form.get('recipe_notes')
    })
    return redirect(url_for('index'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))


@app.route('/reviews')
def reviews():
        return render_template("reviews.html", page_title='Reviews', reviews=mongo.db.reviews.find()) 


@app.route('/add_review')
def add_review():
    return render_template('addreview.html',
                           categories=mongo.db.categories.find(), recipes=mongo.db.recipes.find(), reviews=mongo.db.reviews.find())
                           

@app.route('/submit_review', methods=['POST'])
def submit_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('reviews'))
    
    
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('reviews'))
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)