import { useEffect, useState } from "react";
import { getCameras } from "../services/api";

export default function Dashboard() {

    const [cameras, setCameras] = useState([]);

    useEffect(() => {

        async function load() {

            const data = await getCameras();

            setCameras(data);

        }

        load();

    }, []);

    return (

        <div>

            <h1>Dashboard</h1>

            <br/>

            <h2>Systemstatus</h2>

            <p>Backend: 🟢 Online</p>

            <p>Kameras erkannt: {cameras.length}</p>

            <br/>

            {

                cameras.map(camera => (

                    <div
                        key={camera.id}
                        style={{
                            marginBottom:20,
                            padding:15,
                            background:"#1f2937",
                            borderRadius:10
                        }}
                    >

                        <h3>Kamera {camera.id}</h3>

                        <p>

                            {camera.width} x {camera.height}

                        </p>

                        <p>

                            {camera.fps.toFixed(1)} FPS

                        </p>

                    </div>

                ))

            }

        </div>

    );

}