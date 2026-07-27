import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('Deve renderizar a pagina principal com o titulo', () => {
  render(<App />);
  expect(screen.getByText("Ornella")).toBeInTheDocument();
});
