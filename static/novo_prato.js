document.getElementById("botao_sub_prato").addEventListener("click", async function () {
    const nome = document.getElementById("nome-prato").value;
    const ingredientes = document.getElementById("ingredientes-prato").value;
    const preco = document.getElementById("preco-prato").value;

    const resposta = await fetch("/adiciona_prato", {
        method: "POST",
        body: JSON.stringify({ nome, ingredientes, preco }),
        headers: { "Content-Type": "application/json" }
    });

    const resultado = await resposta.json();
    if (resultado.sucesso) {
        novo_prato_na_lista(nome, ingredientes, preco);
    } else {
        alert("Erro ao adicionar prato.");
    }
});