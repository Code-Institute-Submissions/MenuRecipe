import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_collection'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    

@app.route('/get_images')
def get_images():
    return render_template('gallery.html', images=mongo.db.images.find())
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())   


@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

    
"""@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)
    
    
@app.route('/gallery')   
def get_gallery():
    image_names = os.listdir('./images')
    return render_template ("gallery.html", image_names=image_names)"""
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)