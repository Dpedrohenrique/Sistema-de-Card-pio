function mudarCorDeFundo(cor) {
    // Muda o fundo do <body>
    document.body.style.backgroundColor = cor;

    // Muda o fundo da div principal (estrutura geral da página)
    const divPrincipal = document.querySelector('.div_0');
    if (divPrincipal) {
        divPrincipal.style.backgroundColor = cor;
    }

    // Muda o fundo de elementos internos como divs e cards
    const sections = document.querySelectorAll('.card, #div_1, #div_2');
    sections.forEach(sec => {
        sec.style.backgroundColor = cor;
    });
}