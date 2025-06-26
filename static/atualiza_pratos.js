function novo_prato_na_lista(nome, ingredientes, preco) {
    const lista = document.getElementById("lista-cardapio");

    const card = document.createElement("div");
    card.className = "card-prato";
    card.innerHTML = `
        <h3>${nome}</h3>
        <p><strong>Ingredientes:</strong> ${ingredientes}</p>
        <p><strong>Preço:</strong> R$ ${parseFloat(preco).toFixed(2)}</p>
    `;
    lista.appendChild(card);
}