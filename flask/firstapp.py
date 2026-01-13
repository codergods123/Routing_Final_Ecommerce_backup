from flask import Flask, render_template, request, jsonify
from database import init_db, add_user, record_topup_transaction, get_db_connection

app = Flask(__name__, template_folder='templates')

# Initialize database on startup
init_db()

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/games')
def games ():
    return render_template('Games.html')

@app.route('/promos')
def promos ():
    return render_template('Promo.html')

@app.route('/register')
def register ():
    return render_template('Register.html')

@app.route('/about')
def about ():   
    return render_template('About.html')

@app.route('/contact')
def contact ():
    return render_template('Contact.html')

@app.route('/guide')
def guide ():
    return render_template('Guide.html')

@app.route('/ml')
def ml ():
    return render_template('MlTopUp.html')

@app.route('/codm')
def codm ():
    return render_template('CodmTopUp.html')

@app.route('/valorant')
def valorant ():
    return render_template('ValorantTopUp.html')

@app.route('/lol')
def lol ():
    return render_template('LolTopUp.html')

@app.route('/bs')
def bs ():
    return render_template('BsTopup.html')

@app.route('/genshin')
def genshin ():
    return render_template('genshintopup.html')

@app.route('/api/record-topup', methods=['POST'])
def record_topup():
    """API endpoint to record topup transaction"""
    try:
        data = request.json
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        game_name = data.get('game', '').strip()
        amount = float(data.get('amount', 0))
        payment_method = data.get('payment_method', '')
        game_user_id = data.get('game_user_id', '')
        zone_id = data.get('zone_id', '')
        
        # Validation
        if not all([username, email, game_name, amount, payment_method]):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        if amount <= 0:
            return jsonify({'success': False, 'error': 'Amount must be greater than 0'}), 400
        
        # Add or get user
        user_result = add_user(username, email)
        if not user_result['success']:
            if 'UNIQUE constraint failed' in user_result.get('error', ''):
                # User already exists, get their ID
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
                user = cursor.fetchone()
                conn.close()
                if user:
                    user_id = user[0]
                else:
                    return jsonify({'success': False, 'error': 'User creation failed'}), 400
            else:
                return jsonify({'success': False, 'error': user_result.get('error')}), 400
        else:
            user_id = user_result['user_id']
        
        # Get game ID
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM games WHERE name = ?', (game_name,))
        game = cursor.fetchone()
        
        # If game doesn't exist, create it
        if not game:
            cursor.execute('INSERT INTO games (name, category) VALUES (?, ?)', (game_name, 'Unknown'))
            conn.commit()
            game_id = cursor.lastrowid
        else:
            game_id = game[0]
        
        conn.close()
        
        # Record transaction
        trans_result = record_topup_transaction(user_id, game_id, amount, 'PHP')
        
        if trans_result['success']:
            return jsonify({
                'success': True,
                'transaction_id': trans_result['transaction_id'],
                'message': f'Top-up recorded successfully! Transaction ID: {trans_result["transaction_id"]}'
            }), 200
        else:
            return jsonify({'success': False, 'error': trans_result.get('error')}), 400
            
    except ValueError as e:
        return jsonify({'success': False, 'error': 'Invalid amount format'}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)