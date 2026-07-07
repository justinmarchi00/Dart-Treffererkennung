const API_URL = "http://localhost:5050";

export { API_URL };

export async function getCameras() {
    const res = await fetch(`${API_URL}/api/cameras`);
    return await res.json();
}

export async function createGame(players) {
    const res = await fetch(`${API_URL}/api/game/new`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            players,
        }),
    });

    return await res.json();
}

export async function throwPoints(points) {
    const res = await fetch(`${API_URL}/api/game/throw`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            points,
        }),
    });

    return await res.json();
}

export async function nextPlayer() {
    const res = await fetch(`${API_URL}/api/game/next`, {
        method: "POST",
    });

    return await res.json();
}

export async function getGameState() {
    const res = await fetch(`${API_URL}/api/game/state`);
    return await res.json();
}