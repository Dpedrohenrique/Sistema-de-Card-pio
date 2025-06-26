alert('olá')
function mudaCor(evento) {
    let div_direito = document.getElementById("div_2");
    let cor = document.getElementById("input-cor").value;
    div_direito.style['background-color'] = cor;

}
function associa_clique_a_funcao() {
    let botao = document.getElementById("botao-cor");
    botao.addEventListener("click", mudaCor);
}
window.addEventListener("load", associa_clique_a_funcao);