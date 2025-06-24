let currentPlayer = 'A';
let mode = 'SINGLE';

function startGame() {
    mode = document.getElementById('mode').value;
    fetch('/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: mode })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('setup').style.display = 'none';
        document.getElementById('game').style.display = '';
        updateUI(data, true);
    });
}

function submitGuess() {
    const guessInput = document.getElementById('guess-input');
    const guess = parseInt(guessInput.value);
    if (isNaN(guess)) {
        showHint("Please enter a valid number.", true);
        return;
    }
    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player: currentPlayer, guess: guess })
    })
    .then(res => res.json())
    .then(data => {
        updateUI(data);
        if (mode === 'TWO' && !data.winner) {
            currentPlayer = currentPlayer === 'A' ? 'B' : 'A';
            showHint(`Player ${currentPlayer}'s turn!`);
        }
    });
}

function retryLevel() {
    fetch('/retry', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
        currentPlayer = 'A';
        updateUI(data, true);
    });
}

function nextLevel() {
    fetch('/next', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
        currentPlayer = 'A';
        updateUI(data, true);
    });
}

function restartGame() {
    location.reload();
}

function updateUI(data, resetInput=false) {
    document.getElementById('level-info').textContent = `Level: ${data.level} (Range: ${data.low}-${data.high})`;
    document.getElementById('filter-info').textContent = `Filter: ${data.filter_type}`;
    document.getElementById('attempts-info').textContent = `Attempts Left - Player A: ${data.attempts_a} | Player B: ${data.attempts_b}`;
    document.getElementById('score').textContent = `Score - Player A: ${data.scores.A} | Player B: ${data.scores.B}`;
    document.getElementById('ai-feedback').textContent = data.ai_feedback || '';
    showHint(data.last_hint || '');

    // Winner display
    const winnerDiv = document.getElementById('winner');
    // Only show winner/draw after round ends
    if (data.winner === null && (data.attempts_a === 0 || data.attempts_b === 0)) {
        winnerDiv.textContent = "No winner this round!";
        winnerDiv.className = "winner loser";
    } else if (data.winner) {
        winnerDiv.textContent = (data.winner === 'A' ? "🎉 You win!" : (data.winner === 'B' ? "🤖 Computer wins!" : `Winner: ${data.winner}`));
        winnerDiv.className = "winner" + (data.winner === 'B' ? " loser" : "");
    } else {
        winnerDiv.textContent = "";
        winnerDiv.className = "winner";
    }

    // Button logic:
    const nextBtn = document.getElementById('next-btn');
    const retryBtn = document.getElementById('retry-btn');
    const guessBtn = document.getElementById('guess-btn');
    const guessInput = document.getElementById('guess-input');

    // Single player: if AI wins, only show restart/retry
    if (data.mode === 'SINGLE' && data.winner === 'B') {
        nextBtn.style.display = 'none';
        retryBtn.style.display = '';
        guessBtn.disabled = true;
        guessInput.disabled = true;
    }
    // Two player: only show next/retry if level is over
    else if (data.mode === 'TWO' && (data.winner || (data.attempts_a === 0 && data.attempts_b === 0))) {
        nextBtn.style.display = data.winner ? '' : 'none';
        retryBtn.style.display = data.winner ? 'none' : '';
        guessBtn.disabled = true;
        guessInput.disabled = true;
    }
    // Single player: player wins, show next/retry
    else if (data.mode === 'SINGLE' && data.winner === 'A') {
        nextBtn.style.display = '';
        retryBtn.style.display = '';
        guessBtn.disabled = true;
        guessInput.disabled = true;
    }
    // Otherwise, playing
    else {
        nextBtn.style.display = 'none';
        retryBtn.style.display = 'none';
        guessBtn.disabled = false;
        guessInput.disabled = false;
    }

    if (resetInput) guessInput.value = '';
}

function showHint(msg, isError=false) {
    const hintDiv = document.getElementById('hint');
    hintDiv.textContent = msg;
    hintDiv.style.color = isError ? "#ff5252" : "#ffd600";
}
