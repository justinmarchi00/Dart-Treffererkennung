import Sidebar from "./Sidebar";
import Header from "./Header";

export default function Layout({ children }) {
    return (
        <div style={{
            display: "flex",
            height: "100vh",
            background: "#111827",
            color: "white"
        }}>

            <Sidebar />

            <div style={{
                flex: 1,
                display: "flex",
                flexDirection: "column"
            }}>

                <Header />

                <div style={{
                    padding: 20,
                    overflow: "auto"
                }}>
                    {children}
                </div>

            </div>

        </div>
    );
}