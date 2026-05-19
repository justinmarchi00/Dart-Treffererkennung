async function updateGame() {

    const response = await fetch('/api/game');
    const data = await response.json();

    document.getElementById('last-hit').innerText = data.last_hit;
    document.getElementById('points').innerText = '+' + data.points + ' Punkte';

    // Spieler

    const playersContainer = document.getElementById('players-container');
    playersContainer.innerHTML = '';

    data.players.forEach(player => {

        const div = document.createElement('div');
        div.classList.add('player-card');

        if(player.name === data.current_player) {
            div.classList.add('active');
        }

        div.innerHTML = `
            <div class="player-top">
                <h2>${player.name}</h2>
                ${player.name === data.current_player ? '<span>AM ZUG</span>' : ''}
            </div>

            <div class="player-score">
                ${player.score}
            </div>

            <div class="darts">
                ${player.darts.map(d => `<div class="dart">${d}</div>`).join('')}
            </div>

            <div class="player-footer">
                <span>Average: ${player.average}</span>
                <span>${player.checkout}</span>
            </div>
        `;

        playersContainer.appendChild(div);
    });

    // Historie

    const historyContainer = document.getElementById('history-container');
    historyContainer.innerHTML = '';

    data.history.forEach(entry => {

        const div = document.createElement('div');
        div.classList.add('history-entry');
        div.innerText = entry;

        historyContainer.appendChild(div);
    });
}

setInterval(updateGame, 1000);
updateGame();