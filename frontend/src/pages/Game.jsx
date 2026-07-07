import { useEffect, useState } from "react";
import {
    createGame,
    throwPoints,
    nextPlayer,
    getGameState
} from "../services/api";

export default function Game() {

    const [game, setGame] = useState(null);

    useEffect(() => {

        async function start() {

            const state = await createGame([
                "Justin",
                "Spieler 2"
            ]);

            setGame(state);

        }

        start();

    }, []);

    async function add(points) {

        const state = await throwPoints(points);

        setGame(state);

    }

    async function next() {

        const state = await nextPlayer();

        setGame(state);

    }

    if (!game)
        return <h1>Lade Spiel...</h1>;

    return (

        <div style={{padding:40}}>

            <h1>DartVision</h1>

            <h2>Aktiver Spieler</h2>

            <h1>

                {game.players[game.currentPlayer].name}

            </h1>

            <hr/>

            {

                game.players.map(player => (

                    <div key={player.name}>

                        <h2>{player.name}</h2>

                        <h1>{player.score}</h1>

                        Average: {player.average}

                        <br/><br/>

                    </div>

                ))

            }

            <button onClick={() => add(60)}>+60</button>

            <button onClick={() => add(45)}>+45</button>

            <button onClick={() => add(26)}>+26</button>

            <button onClick={() => add(100)}>+100</button>

            <button onClick={next}>

                Nächster Spieler

            </button>

        </div>

    );

}