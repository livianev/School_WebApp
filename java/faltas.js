
let indiceAtual = 0;

function mostrarFalta(indiceAtual) {
    const texto = document.getElementById("faltas-texto");
     if (faltas.length > 0 && texto) {
         const falta = faltas[indiceAtual];
         console.log("Mostrando faltas:", falta);
        texto.textContent = `Data: ${falta.data}  ${falta.total}`;

 }
}


function proximaFalta() {
 if (indiceAtual < faltas.length - 1) {
 indiceAtual++;
 mostrarFalta(indiceAtual);
 }
}

function voltarFalta() {
 if (indiceAtual > 0) {
 indiceAtual--;
 mostrarFalta(indiceAtual);
 }
}

// Mostrar a primeira falta ao carregar a página
window.onload = () => {
 mostrarFalta(indiceAtual);
};


