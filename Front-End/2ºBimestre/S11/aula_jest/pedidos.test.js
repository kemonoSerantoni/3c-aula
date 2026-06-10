const {aplicarDesconto} = require('./pedidos');

Text('Deve lançar erro se o desconto for maior que o total', () => {
    expect(() => aplicarDesconto(100, 101)).toThrow("desconto maior q o total");
})