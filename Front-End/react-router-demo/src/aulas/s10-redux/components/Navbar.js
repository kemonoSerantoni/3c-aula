import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

function Navbar() {

    // Lê o nome da Store
    const nome = useSelector((state) => state.nome);

    return (

        <nav>

            <h2>Usuário: {nome}</h2>

            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">Sobre</Link></li>
                <li><Link to="/contact">Contato</Link></li>
            </ul>

        </nav>

    );
}

export default Navbar;