"""Initialize database with sample data"""
from database import init_db, add_game

# Initialize the database
init_db()

# Add sample games
games = [
    ('Mobile Legends', 'Mobile'),
    ('Call of Duty Mobile', 'Mobile'),
    ('Valorant', 'PC'),
    ('League of Legends', 'PC'),
    ('Brawl Stars', 'Mobile'),
    ('Genshin Impact', 'Multiplatform')
]

for game_name, category in games:
    result = add_game(game_name, category)
    if result['success']:
        print(f"Added game: {game_name}")
    else:
        print(f"Game {game_name} already exists or error: {result.get('error')}")

print("Database setup complete!")
