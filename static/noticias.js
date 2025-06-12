

// Exibe a primeira notícia ao carregar a página
const noticias = [
    "Nova biblioteca será inaugurada em breve!",
    "Curso de informática para pais e alunos começa na próxima semana.",
    "Projeto de reciclagem ganha prêmio nacional."
];

let indiceAtual = 0;


function mostrarNoticia(indice) {
    const texto = document.getElementById("noticia-texto");
    if (texto) {
        texto.textContent = noticias[indice];
        console.log("Mostrando notícia:", noticias[indice]);
    } else {
        console.error("Elemento com ID 'noticia-texto' não encontrado.");
    }
}


function proximaNoticia() {
    indiceAtual = (indiceAtual + 1) % noticias.length;
    mostrarNoticia(indiceAtual);
}

function anteriorNoticia() {
    indiceAtual = (indiceAtual - 1 + noticias.length) % noticias.length;
    mostrarNoticia(indiceAtual);
}



window.onload = () => {
    mostrarNoticia(indiceAtual);
    setInterval(proximaNoticia, 5000); // troca automática
};

