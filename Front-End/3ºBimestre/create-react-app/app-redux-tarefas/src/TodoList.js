import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { adicionar, remover } from './tarefasSlice';
 
function TodoList() {
  const tarefas = useSelector((state) => state.tarefas);
  const dispatch = useDispatch();
 
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h2>Lista de Tarefas (Redux)</h2>
      
      <button onClick={() => dispatch(adicionar('Dormir'))}>
        Adicionar "Dormir"
      </button>
 
      <ul>
        {tarefas.map((tarefa, index) => (
          <li key={index} style={{ marginBottom: '8px' }}>
            {tarefa}{' '}
            <button onClick={() => dispatch(remover(tarefa))}>
              x
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
 
export default TodoList;