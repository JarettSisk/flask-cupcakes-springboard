"""Flask app for Cupcakes"""
import json
import re
from flask import Flask, request, render_template, redirect, flash, session, abort, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
# Debugging turned off
app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'MySecretKey123'

connect_db(app)

# Routes
@app.route('/')
def render_front_end():
    return render_template('index.html')
    
@app.route('/api/cupcakes', methods=['GET'])
def get_all_cupcakes():
    """Return JSON data for all cupcakes in database"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes', methods=['POST'])
def create_new_cupcake():
    """Create a new cupcake then return data about the new cupcake"""
    data = request.json
    new_cupcake = Cupcake(flavor=data['flavor'], size=data['size'], rating=data['rating'], image=data['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<cupcake_id>', methods=['GET'])
def get_single_cupcake(cupcake_id):
    cupcakeid = int(cupcake_id)
    cupcake = Cupcake.query.get_or_404(cupcakeid)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<cupcake_id>', methods=['PATCH'])
def update_single_cupcake(cupcake_id):
    cupcakeid = int(cupcake_id)
    cupcake = Cupcake.query.get_or_404(cupcakeid)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<cupcake_id>', methods=['DELETE'])
def delete_single_cupcake(cupcake_id):
    cupcakeid = int(cupcake_id)
    cupcake = Cupcake.query.get_or_404(cupcakeid)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=f"Deleted cupcake with id of {cupcake_id}")



    




