window.addEventListener("load", () => {
    document.getElementById("input-nome").addEventListener(
        "input", (evento) => {
        document.getElementById("span-nome").innerHTML = trabalha_string.nome(document.getElementById("input-nome").value);
    });
});

