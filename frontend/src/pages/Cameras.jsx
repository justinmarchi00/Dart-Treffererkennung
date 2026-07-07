import { useEffect, useState } from "react";

import CameraCard from "../components/CameraCard";

import { getCameras } from "../services/api";

export default function Cameras() {

    const [cameras, setCameras] = useState([]);

    useEffect(() => {

        async function load() {

            const result = await getCameras();

            setCameras(result);

        }

        load();

    }, []);

    return (

        <div>

            <h1>Kameras</h1>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(auto-fit,minmax(450px,1fr))",
                    gap: 20
                }}
            >

                {

                    cameras.map(camera => (

                        <CameraCard

                            key={camera.id}

                            camera={camera}

                        />

                    ))

                }

            </div>

        </div>

    );

}