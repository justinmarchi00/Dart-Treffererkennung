export function calculateScore(hit) {

    hit = hit.toUpperCase()

    if (hit.startsWith('T')) {
        return parseInt(hit.replace('T', '')) * 3
    }

    if (hit.startsWith('D')) {
        return parseInt(hit.replace('D', '')) * 2
    }

    if (hit === 'BULL') {
        return 50
    }

    if (hit === '25') {
        return 25
    }

    return parseInt(hit)
}

export function nextPlayer(current, players) {

    if (current + 1 >= players.length) {
        return 0
    }

    return current + 1
}