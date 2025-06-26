let total = 0;

function adicionarConta() {
    const seletor = document.getElementById("seletor-prato");
    const preco = parseFloat(seletor.value);
    total += preco;
    document.getElementById("total-conta").textContent = total.toFixed(2);
    document.getElementById("mensagem-final").textContent = ""; // limpa mensagem anterior
}

function finalizarPedido() {
    if (total === 0) {
        document.getElementById("mensagem-final").textContent = "Nenhum prato foi adicionado.";
        return;
    }

    document.getElementById("mensagem-final").textContent = "Pedido finalizado! Obrigado pela preferência.";
    total = 0;
    document.getElementById("total-conta").textContent = "0.00";
}