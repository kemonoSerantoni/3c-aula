import React from 'react';
import Saudacao from '../components/Saudacao';
import { useSelector, useDispatch } from 'react-redux';
import { changeName } from '../redux/userActions';
import './Home.css';

function Home() {
    // Lê o estado da Store
    const nome = useSelector((state) => state.nome);

    // Permite disparar actions
    const dispatch = useDispatch();

    const pessoas = [
        { nome: "João", idade: 20 },
        { nome: "Maria", idade: 25 },
        { nome: "Ana", idade: 30 }
    ];

    return (
        <div>
            <h1 className='titulo'>Página Home Redux</h1>
            {/* Nome vindo da Store */}
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

            {/* BOTÕES Redux */}
            <button onClick={() => dispatch(changeName("Maria"))}>
                Maria
            </button>

            <button onClick={() => dispatch(changeName("Ana"))}>
                Ana
            </button>

            <button onClick={() => dispatch(changeName("Carlos"))}>
                Carlos
            </button>

        </div>

    );
}

export default Home;