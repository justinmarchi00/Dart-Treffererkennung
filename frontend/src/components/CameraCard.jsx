import { API_URL } from "../services/api";

export default function CameraCard({ camera }) {

    return (

        <div
            style={{
                background: "#1f2937",
                borderRadius: 12,
                overflow: "hidden",
                padding: 15,
                boxShadow: "0 0 15px rgba(0,0,0,.3)"
            }}
        >

            <h3>Kamera {camera.id}</h3>

            <img
                src={`${API_URL}/api/camera/${camera.id}/stream`}
                alt=""
                style={{
                    width: "100%",
                    borderRadius: 10
                }}
            />

            <div
                style={{
                    marginTop: 10,
                    display: "flex",
                    justifyContent: "space-between"
                }}
            >
                <span>

                    {camera.width} × {camera.height}

                </span>

                <span>

                    {camera.fps.toFixed(1)} FPS

                </span>

            </div>

        </div>

    );

}