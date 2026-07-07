import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout";

import Dashboard from "./pages/Dashboard";
import Game from "./pages/Game";
import Calibration from "./pages/Calibration";
import Cameras from "./pages/Cameras";
import Settings from "./pages/Settings";

function App() {
    return (
        <BrowserRouter>

            <Layout>

                <Routes>

                    <Route path="/" element={<Dashboard />} />

                    <Route path="/game" element={<Game />} />

                    <Route path="/calibration" element={<Calibration />} />

                    <Route path="/cameras" element={<Cameras />} />

                    <Route path="/settings" element={<Settings />} />

                </Routes>

            </Layout>

        </BrowserRouter>
    );
}

export default App;