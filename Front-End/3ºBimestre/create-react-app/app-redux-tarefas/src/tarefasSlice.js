import { createSlice } from '@reduxjs/toolkit';
 
const tarefasSlice = createSlice({
  name: 'tarefas',
  initialState: ['Estudar'],
  reducers: {
    adicionar: (state, action) => {
      state.push(action.payload);
    },
    remover: (state, action) => {
      return state.filter((t) => t !== action.payload);
    },
  },
});
 
export const { adicionar, remover } = tarefasSlice.actions;
export default tarefasSlice.reducer;