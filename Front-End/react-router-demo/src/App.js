import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
//import Navbar from './aulas/s5a2/components/Navbar';

// 🔁 mudou aqui
//import Home from './aulas/s5a2/pages/Home';
//import About from './aulas/s5a2/pages/About';
//import Contact from './aulas/s5a2/pages/Contact';

//import Home from './aulas/s8/pages/Home';
//import About from './aulas/s8/pages/About';
//import Contact from './aulas/s8/pages/Contact';

import Navbar from './aulas/s10-redux/components/Navbar';
import Home from './aulas/s10-redux/pages/Home';
import About from './aulas/s10-redux/pages/About';
import Contact from './aulas/s10-redux/pages/Contact';


function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
            </Routes>
        </Router>
    );
}

export default App;
