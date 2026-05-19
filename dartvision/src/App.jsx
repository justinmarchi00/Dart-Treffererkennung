import { useState } from 'react'
import { calculateScore, nextPlayer } from './utils/dartLogic'
import { checkouts } from './data/checkouts'

export default function App() {

  // SETTINGS

  const [gameMode, setGameMode] = useState(501)
  const [doubleIn, setDoubleIn] = useState(false)
  const [doubleOut, setDoubleOut] = useState(true)

  // PLAYERS

  const [playerName, setPlayerName] = useState('')
  const [players, setPlayers] = useState([])

  // GAME

  const [currentPlayer, setCurrentPlayer] = useState(0)

  // LIVE HIT

  const [lastHit, setLastHit] = useState('-')

  // MATCH

  const [legs, setLegs] = useState({})
  const [sets, setSets] = useState({})
  const [bestOf, setBestOf] = useState(5)

  // HISTORY

  const [history, setHistory] = useState([])

  // OPENCV READY

  function receiveOpenCVHit(hit) {

    if (!hit) return

    const updatedPlayers = [...players]

    if (updatedPlayers.length <= 0) return

    const player = updatedPlayers[currentPlayer]

    const finalHit = hit.toUpperCase()

    setLastHit(finalHit)

    const points = calculateScore(finalHit)

    // DOUBLE IN

    if (doubleIn && !player.started) {

      if (
        !finalHit.startsWith('D') &&
        finalHit !== 'BULL'
      ) {

        setHistory(prev => [
          `${player.name} → Double-In verpasst`,
          ...prev
        ])

        nextTurn(updatedPlayers)

        return
      }

      player.started = true
    }

    const remaining = player.score - points

    // BUST

    if (
      remaining < 0 ||
      remaining === 1
    ) {

      player.score = player.turnStartScore

      setHistory(prev => [
        `${player.name} → BUST`,
        ...prev
      ])

      nextTurn(updatedPlayers)

      return
    }

    // DOUBLE OUT

    if (remaining === 0 && doubleOut) {

      if (
        !finalHit.startsWith('D') &&
        finalHit !== 'BULL'
      ) {

        player.score = player.turnStartScore

        setHistory(prev => [
          `${player.name} → Double-Out verpasst`,
          ...prev
        ])

        nextTurn(updatedPlayers)

        return
      }
    }

    // SCORE UPDATE

    player.score = remaining

    player.darts[player.currentDart - 1] = finalHit

    player.throws.push(points)

    // AVERAGE

    const total = player.throws.reduce((a, b) => a + b, 0)

    player.average = (
      (total / player.throws.length) * 3
    ).toFixed(1)

    // CHECKOUT

    if (checkouts[remaining]) {
      player.checkout = checkouts[remaining]
    } else {
      player.checkout = '-'
    }

    // HISTORY

    setHistory(prev => [
      `${player.name} → ${finalHit} (${points})`,
      ...prev
    ])

    // WIN

    if (remaining === 0) {

      const updatedLegs = {
        ...legs,
        [player.name]: (legs[player.name] || 0) + 1
      }

      setLegs(updatedLegs)

      setHistory(prev => [
        `🏆 ${player.name} gewinnt das Leg!`,
        ...prev
      ])

      // MATCH WIN

      if (updatedLegs[player.name] >= Math.ceil(bestOf / 2)) {

        alert(`${player.name} gewinnt das Match!`)

        setHistory(prev => [
          `👑 ${player.name} gewinnt das Match!`,
          ...prev
        ])

        return
      }

      // NEW LEG

      const resetPlayers = updatedPlayers.map(p => ({
        ...p,
        score: gameMode,
        darts: ['-', '-', '-'],
        currentDart: 1,
        checkout: '-',
        started: !doubleIn,
        turnStartScore: gameMode
      }))

      setPlayers(resetPlayers)

      setCurrentPlayer(0)

      return
    }

    // NEXT DART

    player.currentDart++

    // NEXT PLAYER

    if (player.currentDart > 3) {

      nextTurn(updatedPlayers)

    } else {

      setPlayers(updatedPlayers)
    }
  }

  // ADD PLAYER

  function addPlayer() {

    if (!playerName.trim()) return

    const newPlayer = {

      name: playerName,

      score: gameMode,

      average: 0,

      checkout: '-',

      darts: ['-', '-', '-'],

      throws: [],

      started: !doubleIn,

      currentDart: 1,

      turnStartScore: gameMode
    }

    setPlayers([...players, newPlayer])

    setPlayerName('')
  }

  // START GAME

  function startGame() {

    const resetPlayers = players.map(player => ({
      ...player,
      score: gameMode,
      average: 0,
      checkout: '-',
      darts: ['-', '-', '-'],
      throws: [],
      currentDart: 1,
      started: !doubleIn,
      turnStartScore: gameMode
    }))

    const legData = {}
    const setData = {}

    resetPlayers.forEach(player => {

      legData[player.name] = 0
      setData[player.name] = 0
    })

    setLegs(legData)
    setSets(setData)

    setPlayers(resetPlayers)

    setCurrentPlayer(0)

    setLastHit('-')

    setHistory([
      `🎯 Spiel gestartet (${gameMode})`
    ])
  }

  // NEXT TURN

  function nextTurn(updatedPlayers) {

    updatedPlayers[currentPlayer].currentDart = 1

    updatedPlayers[currentPlayer].darts = ['-', '-', '-']

    updatedPlayers[currentPlayer].turnStartScore =
      updatedPlayers[currentPlayer].score

    setPlayers(updatedPlayers)

    setCurrentPlayer(
      nextPlayer(currentPlayer, updatedPlayers)
    )
  }

  return (

    <div className="min-h-screen bg-[#0b0b0b] text-white overflow-hidden font-sans">

      {/* HEADER */}

      <header className="h-[72px] border-b border-[#1a1a1a] bg-[#101010] flex items-center justify-between px-6">

        <div>

          <h1 className="text-2xl font-black tracking-tight">
            🎯 DartVision
          </h1>

          <p className="text-xs text-zinc-500 mt-1">
            OpenCV Ready
          </p>

        </div>

        <div className="text-sm text-zinc-500">
          Best Of {bestOf}
        </div>

      </header>

      {/* MAIN */}

      <div className="grid grid-cols-[250px_1fr_280px] gap-5 p-5 h-[calc(100vh-72px)]">

        {/* LEFT */}

        <aside className="overflow-y-auto">

          <div className="bg-[#101010] border border-[#1d1d1d] rounded-[24px] p-5">

            <h2 className="text-xl font-black mb-5">
              Spiel
            </h2>

            <div className="space-y-4">

              {/* MODE */}

              <div>

                <label className="block text-sm text-zinc-500 mb-2">
                  Spielmodus
                </label>

                <select
                  value={gameMode}
                  onChange={(e) => setGameMode(parseInt(e.target.value))}
                  className="w-full h-[48px] bg-[#181818] border border-[#242424] rounded-[18px] px-4 outline-none"
                >
                  <option value={301}>301</option>
                  <option value={501}>501</option>
                  <option value={701}>701</option>
                </select>

              </div>

              {/* BEST OF */}

              <div>

                <label className="block text-sm text-zinc-500 mb-2">
                  Best Of
                </label>

                <select
                  value={bestOf}
                  onChange={(e) => setBestOf(parseInt(e.target.value))}
                  className="w-full h-[48px] bg-[#181818] border border-[#242424] rounded-[18px] px-4 outline-none"
                >
                  <option value={3}>3</option>
                  <option value={5}>5</option>
                  <option value={7}>7</option>
                </select>

              </div>

              {/* PLAYER */}

              <div>

                <label className="block text-sm text-zinc-500 mb-2">
                  Spieler
                </label>

                <input
                  type="text"
                  value={playerName}
                  onChange={(e) => setPlayerName(e.target.value)}
                  placeholder="Name eingeben"
                  className="w-full h-[48px] bg-[#181818] border border-[#242424] rounded-[18px] px-4 outline-none"
                />

              </div>

              <button
                onClick={addPlayer}
                className="w-full h-[48px] bg-[#181818] hover:bg-[#222] rounded-[18px] font-semibold transition"
              >
                Spieler hinzufügen
              </button>

              {/* RULES */}

              <div className="grid grid-cols-2 gap-3">

                <button
                  onClick={() => setDoubleIn(!doubleIn)}
                  className={`h-[48px] rounded-[18px] font-semibold transition ${
                    doubleIn
                      ? 'bg-white text-black'
                      : 'bg-[#181818]'
                  }`}
                >
                  Double In
                </button>

                <button
                  onClick={() => setDoubleOut(!doubleOut)}
                  className={`h-[48px] rounded-[18px] font-semibold transition ${
                    doubleOut
                      ? 'bg-white text-black'
                      : 'bg-[#181818]'
                  }`}
                >
                  Double Out
                </button>

              </div>

              <button
                onClick={startGame}
                className="w-full h-[52px] bg-white text-black rounded-[18px] font-black"
              >
                Spiel starten
              </button>

            </div>

          </div>

        </aside>

        {/* CENTER */}

        <main className="overflow-y-auto">

          {/* LIVE STATUS */}

          <div className="bg-[#101010] border border-[#1d1d1d] rounded-[28px] p-5 mb-5">

            <div className="flex items-center justify-between mb-5">

              <div>

                <h2 className="text-xl font-black">
                  Live Erkennung
                </h2>

                <p className="text-sm text-zinc-500 mt-1">
                  OpenCV Verbindung vorbereitet
                </p>

              </div>

              <div className="flex items-center gap-2">

                <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>

                <span className="text-sm text-zinc-500">
                  Bereit
                </span>

              </div>

            </div>

            {/* LAST HIT */}

            <div className="bg-[#181818] rounded-[22px] p-8 text-center mb-4">

              <div className="text-xs uppercase tracking-[4px] text-zinc-500 mb-3">
                Letzter Treffer
              </div>

              <div className="text-[72px] font-black tracking-[-4px]">
                {lastHit}
              </div>

            </div>

            {/* CAMERAS */}

            <div className="grid grid-cols-3 gap-3">

              {[1, 2, 3].map(cam => (

                <div
                  key={cam}
                  className="bg-[#181818] rounded-[18px] p-4"
                >

                  <div className="flex items-center justify-between">

                    <span className="text-sm text-zinc-400">
                      Kamera {cam}
                    </span>

                    <div className="w-2 h-2 rounded-full bg-green-500"></div>

                  </div>

                </div>

              ))}

            </div>

          </div>

          {/* PLAYERS */}

          <div className="space-y-4">

            {players.map((player, index) => (

              <div
                key={index}
                className={`bg-[#101010] border rounded-[24px] p-5 ${
                  currentPlayer === index
                    ? 'border-white/20'
                    : 'border-[#1d1d1d]'
                }`}
              >

                <div className="flex justify-between items-start">

                  <div>

                    <div className="flex items-center gap-3 mb-2">

                      <h2 className="text-2xl font-black">
                        {player.name}
                      </h2>

                      {currentPlayer === index && (

                        <span className="bg-white text-black text-[10px] px-3 py-1 rounded-full font-black uppercase">
                          Am Zug
                        </span>

                      )}

                    </div>

                    <div className="text-[58px] font-black leading-none">
                      {player.score}
                    </div>

                  </div>

                  <div className="text-right">

                    <div className="text-xs text-zinc-500 mb-1">
                      Checkout
                    </div>

                    <div className="text-2xl font-black">
                      {player.checkout}
                    </div>

                  </div>

                </div>

                {/* DARTS */}

                <div className="grid grid-cols-3 gap-3 mt-5">

                  {player.darts.map((dart, i) => (

                    <div
                      key={i}
                      className="h-[64px] rounded-[18px] bg-[#181818] flex items-center justify-center text-2xl font-black"
                    >
                      {dart}
                    </div>

                  ))}

                </div>

                {/* FOOTER */}

                <div className="flex justify-between mt-4 text-sm text-zinc-500">

                  <span>
                    Avg: {player.average}
                  </span>

                  <span>
                    Legs: {legs[player.name] || 0}
                  </span>

                  <span>
                    Dart {player.currentDart}/3
                  </span>

                </div>

              </div>

            ))}

          </div>

        </main>

        {/* RIGHT */}

        <aside className="overflow-y-auto">

          {/* HISTORY */}

          <div className="bg-[#101010] border border-[#1d1d1d] rounded-[24px] p-5 mb-5">

            <h2 className="text-xl font-black mb-5">
              Wurfhistorie
            </h2>

            <div className="space-y-3">

              {history.map((entry, index) => (

                <div
                  key={index}
                  className="bg-[#181818] border border-[#222] rounded-[18px] p-4 text-sm"
                >
                  {entry}
                </div>

              ))}

            </div>

          </div>

          {/* CONTROL */}

          <div className="bg-[#101010] border border-[#1d1d1d] rounded-[24px] p-5">

            <h2 className="text-xl font-black mb-5">
              Steuerung
            </h2>

            <div className="space-y-3">

              {/* TEST BUTTONS */}

              <button
                onClick={() => receiveOpenCVHit('T20')}
                className="w-full h-[52px] bg-[#181818] hover:bg-[#222] rounded-[18px] font-semibold transition"
              >
                Test T20
              </button>

              <button
                onClick={() => receiveOpenCVHit('D20')}
                className="w-full h-[52px] bg-[#181818] hover:bg-[#222] rounded-[18px] font-semibold transition"
              >
                Test D20
              </button>

              <button
                onClick={() => receiveOpenCVHit('BULL')}
                className="w-full h-[52px] bg-[#181818] hover:bg-[#222] rounded-[18px] font-semibold transition"
              >
                Test Bull
              </button>

              {/* NEXT PLAYER */}

              <button
                onClick={() => {

                  const updatedPlayers = [...players]

                  nextTurn(updatedPlayers)

                }}
                className="w-full h-[52px] bg-[#181818] hover:bg-[#222] rounded-[18px] font-semibold transition"
              >
                Nächster Spieler
              </button>

              {/* RESTART */}

              <button
                onClick={startGame}
                className="w-full h-[52px] bg-white text-black rounded-[18px] font-black"
              >
                Spiel neustarten
              </button>

              {/* RESET */}

              <button
                onClick={() => {

                  setPlayers([])
                  setHistory([])
                  setLegs({})
                  setSets({})
                  setCurrentPlayer(0)
                  setLastHit('-')

                }}
                className="w-full h-[52px] bg-red-500 rounded-[18px] font-black"
              >
                Alles zurücksetzen
              </button>

            </div>

          </div>

        </aside>

      </div>

    </div>
  )
}