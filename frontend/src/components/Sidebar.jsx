import { Link } from "react-router-dom";

export default function Sidebar() {

    const item = {
        color: "white",
        textDecoration: "none",
        padding: "12px 16px",
        display: "block"
    };

    return (
        <div style={{
            width: 230,
            background: "#1f2937"
        }}>

            <h2 style={{ padding: 20 }}>
                DartVision
            </h2>

            <Link style={item} to="/">🏠 Dashboard</Link>

            <Link style={item} to="/game">🎯 Spiel</Link>

            <Link style={item} to="/calibration">📐 Kalibrierung</Link>

            <Link style={item} to="/cameras">📷 Kameras</Link>

            <Link style={item} to="/settings">⚙ Einstellungen</Link>

        </div>
    );
}