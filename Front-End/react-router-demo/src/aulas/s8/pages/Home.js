import React from 'react';
import Aluno from '../components/Alunos';
import Mensagem from '../components/Mensagem';

function Home() {
    return (
        <div>
            <Mensagem nome="Professor" />

            <Aluno nome="Maria" idade="20" />
            <Aluno nome="João" idade="18" />
            <Aluno nome="Ana" idade="22" />
        </div>
    );
}

export default Home;
