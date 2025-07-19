**Number Guessing Game Web App**

A fun, colorful, and adaptive number guessing game for kids and families!  
Play in **Single Player** (vs Computer AI) or **Dual Player** (A vs B) mode.  
Built with Flask (Python), HTML, CSS, and JavaScript.
---
🚀 Features

- **Single Player Mode:**  
  - Guess the secret number with hints ("Higher"/"Lower").
  - Computer AI guesses too—can you beat it?
  - If the AI wins, you can retry the level.

- **Dual Player Mode:**  
  - Take turns guessing.  
  - Each player has their own attempts per level.
  - Points are tracked for each player.
  - Retry only if both fail; next level if someone wins.

- **Levels & Filters:**  
  - Each level has a new number range and filter (even, multiples, prime, square, cube, etc).

- **Child-Friendly UI:**  
  - Playful fonts, bright colors, and big buttons.
  - Responsive and mobile-friendly.
---
🖥️ How to Run
**PULL THE REPO**
Use render for on the go hosting

**Start Command**
Render runs this command to start your app with each deploy.

$gunicorn app:app

**Build Command**
Render runs this command to build your app before each deploy.

$pip install -r requirements.txt

else;

1. **Clone or Download this Repository**

2. **Install Requirements**
   ```bash
   pip install flask
   ```

3. **Run the App**
   ```bash
   python app.py
   ```

4. **Open in Browser**
   - Go to [http://localhost:5000]

---

🕹️ How to Play

1. **Choose Mode:**  
   - Single Player (You vs Computer)  
   - Dual Player (A vs B)

2. **Guess the Number:**  
   - Enter your guess and click "Guess".
   - Hints will tell you "Higher" or "Lower".

3. **Win, Lose, or Retry:**  
   - If you win, move to the next level!
   - If the AI wins (single player), you can retry the level.
   - In dual mode, retry only if both fail.

4. **Track Your Score:**  
   - Points are shown for each player in dual mode.

---

📁 Project Structure

```
guessing_web_app/
│
├── app.py
├── logic/
│   ├── game_engine.py
│   ├── smart_ai.py
│   ├── filters.py
│   └── levels.py
├── templates/
│   └── game.html
├── static/
│   ├── game.js
│   └── styles.css
```

---

👦👧 For Kids- early teens!

- Big, bold, and friendly fonts
- Fun colors and easy controls
- No math stress—just play and learn!

---

📝 License

MIT License @2025 (SUBASH K)

---

**Enjoy the game!**
🙌 Contributions are welcome. Please fork the repo and create a pull request. For major changes, please open an issue first to discuss the proposed change.

**Customization**

You can extend the game by editing logic/game_engine.py:

Add more levels or filters

Adjust max attempts per level

Modify AI behavior (e.g., make it smarter/faster)

Track high scores or session data

💡 **Future Improvements**
🌐 Online multiplayer (via WebSockets)

🏆 Leaderboard and stats tracking

🔊 Sound effects

📱 Mobile responsive UI

👨‍💻 Created by
SUBASH K – powered by Flask, logic, and learning 🚀

Feel free to fork, customize, and expand!
we enchance :)
