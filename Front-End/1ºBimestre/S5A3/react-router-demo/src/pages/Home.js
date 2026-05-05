import React, {useState} from 'react';
import Saudacao from '../components/Saudacao';
import './Home.css';


function Home() {
    const [nome,setNome] = useState("Ornella")
    return (
        <div>
            <h1 className='titulo'>Pagina Home!</h1>
    
            <div className='caixa'>
                <div className='nome1'>
                    <Saudacao idade="18" nome="João" />
                    </div>
                    <div className='nome1'>
                    <Saudacao idade="15" nome="Mariah" />
                    </div>
                    <div className='nome1'>
                    <Saudacao idade="13" nome="Mariana" />
                </div>
            </div>
        </div>
    );
}

export default Home;