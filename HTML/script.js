//Comportamiento de la web

//menu de categorias principal opcion 1
let varOne = document.getElementById("opcion1");
let hidenOne = document.getElementById("hiden-box-one");

varOne.addEventListener('mouseover', function () {
    hidenOne.classList.add("active");
});
varOne.addEventListener('mouseleave', function () {
    hidenOne.classList.remove("active");
});
//submenu numero 2
let varTwo = document.getElementById("opcion2");
let hidenTwo = document.getElementById("hiden-box-two");
varTwo.addEventListener('mouseover', function () {
    hidenTwo.classList.add("active")
});
varTwo.addEventListener('mouseleave', function () {
    hidenTwo.classList.remove("active");
});
//submenu numero 3
let varThree = document.getElementById("opcion3");
varThree.addEventListener('mouseover', function () {
    document.getElementById("hiden-box-three").classList.add("active")
});
varThree.addEventListener('mouseleave', function () {
    document.getElementById("hiden-box-three").classList.remove("active")
});

//submenu numero 4
let varFour = document.getElementById("opcion4");
varFour.addEventListener('mouseover', function () {
    document.getElementById("hiden-box-four").classList.add("active")
});
varFour.addEventListener('mouseleave', function () {
    document.getElementById("hiden-box-four").classList.remove("active")
});
//reel de imagen
let indice = 0;
function mover(direccion) {
    const fotos = document.querySelectorAll('.foto');
    const totalFotos = fotos.length;
    indice = (indice + direccion + totalFotos) % totalFotos;
    const carrusel = document.querySelector('.carrusel');
    carrusel.scrollLeft = fotos[indice].offsetLeft;
}

function openPopup() {
    document.getElementById("popup").style.display = "block";
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}

