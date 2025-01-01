from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.product import Product
from app import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'quantity': p.quantity,
        'location': p.location,
        'barcode': p.barcode
    } for p in products]), 200

@products_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        quantity=data.get('quantity', 0),
        location=data.get('location'),
        barcode=data.get('barcode'),
        min_threshold=data.get('min_threshold', 0)
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({
        'message': 'Product created successfully',
        'product_id': new_product.id
    }), 201