const {aplicarDesconto} = require('./pedidos');

test('Deve lançar erro se o desconto for maior que o total', () => {
    expect(() => aplicarDesconto(100,200)).toThrow('Desconto maior que o total');
});