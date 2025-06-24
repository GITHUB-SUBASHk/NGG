from flask import Flask, render_template, request, jsonify, session
from logic.game_engine import NumberGuessingGame
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('game.html')

@app.route('/start', methods=['POST'])
def start():
    mode = request.json['mode']
    g = NumberGuessingGame(mode)
    session['game'] = g.to_dict()
    return jsonify(g.get_game_state())

@app.route('/guess', methods=['POST'])
def guess():
    if 'game' not in session:
        return jsonify({'error': 'No game in progress.'}), 400
    data = request.get_json()
    if not data or 'player' not in data or 'guess' not in data:
        return jsonify({'error': 'Missing player or guess'}), 400
    g = NumberGuessingGame.from_dict(session['game'])
    player = data['player'].upper()
    guess = int(data['guess'])
    feedback = g.player_guess(player, guess)
    ai_feedback = None
    if g.mode == 'SINGLE' and not g.winner:
        ai_feedback = g.computer_turn()
    session['game'] = g.to_dict()
    state = g.get_game_state()
    state['feedback'] = feedback
    state['ai_feedback'] = ai_feedback
    return jsonify(state)

@app.route('/retry', methods=['POST'])
def retry():
    if 'game' not in session:
        return jsonify({'error': 'No game in progress.'}), 400
    g = NumberGuessingGame.from_dict(session['game'])
    g.retry_level()
    session['game'] = g.to_dict()
    return jsonify(g.get_game_state())

@app.route('/next', methods=['POST'])
def next_level():
    if 'game' not in session:
        return jsonify({'error': 'No game in progress.'}), 400
    g = NumberGuessingGame.from_dict(session['game'])
    g.next_level()
    session['game'] = g.to_dict()
    return jsonify(g.get_game_state())

if __name__ == '__main__':
    app.run(debug=True)
