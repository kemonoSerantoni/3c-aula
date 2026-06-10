function aplicarDesconto(total, desconto) {
    if(desconto > total){
        throw new Error("Desconto maior que o total");
    }
    return total - desconto;
}

module.exports = {aplicarDesconto};