from app import create_app, db
from models import User, Post
from datetime import datetime, timedelta
import random

app = create_app()

sample_posts = [
    {
        "title": "The global economy's strange new rules",
        "content": "As the world economy enters uncharted waters, old assumptions are being challenged..."
    },
    {
        "title": "The promise and perils of AI in medicine",
        "content": "Artificial intelligence could revolutionize healthcare, but concerns about privacy and bias remain..."
    },
    {
        "title": "Climate change and the future of agriculture",
        "content": "Farmers around the world are adapting to changing weather patterns and new technologies..."
    },
    {
        "title": "The rise of digital currencies",
        "content": "Central banks are exploring digital currencies, potentially reshaping the global financial system..."
    },
    {
        "title": "The future of work in a post-pandemic world",
        "content": "Remote work and automation are transforming labor markets and challenging traditional employment models..."
    },
    {
        "title": "Geopolitical tensions and global trade",
        "content": "Rising tensions between major powers are reshaping global supply chains and trade relationships..."
    },
    {
        "title": "The ethics of gene editing",
        "content": "Advances in CRISPR technology raise profound ethical questions about the future of human genetics..."
    },
    {
        "title": "Urbanization and sustainable cities",
        "content": "As more people move to cities, urban planners are rethinking how to create sustainable, livable spaces..."
    },
    {
        "title": "The future of energy: beyond fossil fuels",
        "content": "Renewable energy sources are becoming increasingly competitive, challenging the dominance of fossil fuels..."
    },
    {
        "title": "Inequality and the global economy",
        "content": "Economic disparities within and between countries are shaping political landscapes and policy debates..."
    }
]

def add_sample_posts():
    with app.app_context():
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            print("Error: Admin user not found. Please run init_db.py first.")
            return

        for post_data in sample_posts:
            post = Post(
                title=post_data['title'],
                content=post_data['content'],
                author=admin_user,
                date_posted=datetime.utcnow() - timedelta(days=random.randint(0, 30))
            )
            db.session.add(post)
        
        db.session.commit()
        print("Sample posts have been added successfully.")

if __name__ == "__main__":
    add_sample_posts()