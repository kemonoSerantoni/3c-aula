import React from 'react';

function Saudacao(props) {
    return (
        <div>
            <h2>Olá {props.nome}</h2>
            <p>Idade: {props.idade}</p>            
        </div>
    );
}

export default Saudacao;
