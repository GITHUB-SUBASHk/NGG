from .filters import is_prime, is_perfect_square, is_perfect_cube
from .levels import get_level
from .smart_ai import SmartAI
import random

class NumberGuessingGame:
    def __init__(self, mode='SINGLE'):
        self.level = 1
        self.mode = mode.upper()
        self._init_level()
        self.scores = {'A': 0, 'B': 0}
        self.winner = None
        self.last_hint = ""
        self.retry_used = False
        self.computer_guesses = set()

    def _init_level(self):
        low, high, attempts, filter_type = get_level(self.level)
        self.low = low
        self.high = high
        self.max_attempts = attempts
        self.filter_type = filter_type
        self.valid_numbers = [n for n in range(low, high + 1) if self._is_valid(n)]
        self.secret = random.choice(self.valid_numbers)
        self.attempts_a = self.max_attempts
        self.attempts_b = self.max_attempts
        self.min_bound = low
        self.max_bound = high
        self.winner = None
        self.last_hint = ""
        self.computer_guesses = set()
        self.ai = SmartAI(self.low, self.high)

    def _is_valid(self, n):
        f = self.filter_type
        if f == 'all':
            return True
        if f == 'even':
            return n % 2 == 0
        if f.startswith('multiple'):
            return n % int(f.replace('multiple', '')) == 0
        if f == 'prime':
            return is_prime(n)
        if f == 'squareroot':
            return is_perfect_square(n)
        if f == 'cuberoot':
            return is_perfect_cube(n)
        return True

    def player_guess(self, player, guess):
        if self.winner:
            return "Game over!"
        if not self._is_valid(guess):
            return f"Invalid guess for this level's filter!"
        if player == 'A':
            if self.attempts_a <= 0:
                return "No attempts left for Player A."
            self.attempts_a -= 1
        else:
            if self.attempts_b <= 0:
                return "No attempts left for Player B."
            self.attempts_b -= 1
        if guess == self.secret:
            self.winner = player
            self.scores[player] += 1
            return f"🎉 Player {player} guessed correctly!"
        # Only "Higher"/"Lower" hint, no difference
        if guess < self.secret:
            self.last_hint = f"⬆️ Try higher!"
        else:
            self.last_hint = f"⬇️ Try lower!"
        # End of attempts: set winner to None (for retry)
        if self.mode == 'SINGLE' and self.attempts_a == 0:
            if self.winner is None:
                self.winner = None
        elif self.mode == 'TWO' and self.attempts_a == 0 and self.attempts_b == 0 and self.winner is None:
            self.winner = None
        return f"❌ {self.last_hint}"

    def computer_turn(self):
        guess = self.ai.guess()
        if guess is None:
            return "🤖 Computer has no valid guesses left."
        self.computer_guesses.add(guess)
        self.attempts_b -= 1
        if guess == self.secret:
            self.winner = 'B'
            self.scores['B'] += 1
            return f"🤖 Computer guessed {guess} and won!"
        if guess < self.secret:
            self.ai.observe(guess, "higher")
            self.min_bound = max(self.min_bound, guess + 1)
            return f"🤖 Computer guessed {guess}. Hint: Higher."
        else:
            self.ai.observe(guess, "lower")
            self.max_bound = min(self.max_bound, guess - 1)
            return f"🤖 Computer guessed {guess}. Hint: Lower."

    def retry_level(self):
        if self.retry_used:
            return
        self.retry_used = True
        self._init_level()

    def next_level(self):
        self.level += 1
        self.retry_used = False
        self._init_level()

    def to_dict(self):
        return {
            'level': self.level,
            'mode': self.mode,
            'low': self.low,
            'high': self.high,
            'max_attempts': self.max_attempts,
            'filter_type': self.filter_type,
            'secret': self.secret,
            'attempts_a': self.attempts_a,
            'attempts_b': self.attempts_b,
            'winner': self.winner,
            'last_hint': self.last_hint,
            'scores': self.scores,
            'retry_used': self.retry_used,
            'min_bound': self.min_bound,
            'max_bound': self.max_bound,
            'computer_guesses': list(self.computer_guesses),
            'ai': self.ai.to_dict()
        }

    @staticmethod
    def from_dict(data):
        game = NumberGuessingGame(data['mode'])
        game.level = data['level']
        game.low = data['low']
        game.high = data['high']
        game.max_attempts = data['max_attempts']
        game.filter_type = data['filter_type']
        game.secret = data['secret']
        game.attempts_a = data['attempts_a']
        game.attempts_b = data['attempts_b']
        game.winner = data['winner']
        game.last_hint = data['last_hint']
        game.scores = data['scores']
        game.retry_used = data['retry_used']
        game.min_bound = data['min_bound']
        game.max_bound = data['max_bound']
        game.computer_guesses = set(data['computer_guesses'])
        game.ai = SmartAI.from_dict(data['ai'])
        return game

    def get_game_state(self):
        return {
            'level': self.level,
            'mode': self.mode,
            'low': self.low,
            'high': self.high,
            'max_attempts': self.max_attempts,
            'filter_type': self.filter_type,
            'attempts_a': self.attempts_a,
            'attempts_b': self.attempts_b,
            'winner': self.winner,
            'last_hint': self.last_hint,
            'scores': self.scores,
            'retry_used': self.retry_used
        }
