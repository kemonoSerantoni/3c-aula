import React, { useState } from 'react';
import Saudacao from '../components/Saudacao';
import './Home.css';

function Home() {
    // ✅ STATE aqui
    const [nome, setNome] = useState("Ornella");
    
    const pessoas = [
        { nome: "João", idade: 20 },
        { nome: "Maria", idade: 25 },
        { nome: "Ana", idade: 30 }
    ];

    return (
        <div>
            {/* em React é className (não class)*/}
            <h1 className='titulo'>Página Home</h1> 

            {/* mostrando o state */}
            <h2>{nome}</h2>

            {/* LISTA COM MAP */}
            <div className='container'>
                {
                    pessoas.map((pessoa, index) => (
                        <div key={index} className="card">
                            <Saudacao 
                                nome={pessoa.nome} 
                                idade={pessoa.idade} 
                            />
                        </div>
                    ))
                }
            </div>


            {/* BOTÕES (STATE + EVENTO) */}
            <button onClick={() => setNome("Maria")}>Trocar nome</button>
            <button onClick={() => setNome("Ana")}>Ana</button>
            <button onClick={() => setNome("Carlos")}>Carlos</button>

        </div>
    );
}

export default Home;
