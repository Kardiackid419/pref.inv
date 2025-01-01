from app import app, db
from models.user import User
from models.product import Product
from models.transaction import Transaction

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Create an admin user if it doesn't exist
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                email='admin@example.com',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

if __name__ == '__main__':
    init_db() 