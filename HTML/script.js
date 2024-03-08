//Comportamiento de la web

//menu de categorias principal opcion 1
let varOne = document.getElementById("opcion1");
let hidenOne = document.getElementById("hiden-box-one");
let cuerpo = document.getElementById("cuerpo");

varOne.addEventListener('mouseover', function () {
    hidenOne.classList.add("active");
    cuerpo.classList.add("blur");
});
varOne.addEventListener('mouseleave', function () {
    hidenOne.classList.remove("active");
    cuerpo.classList.remove("blur");
});
//submenu numero 2
let varTwo = document.getElementById("opcion2");
let hidenTwo = document.getElementById("hiden-box-two");
varTwo.addEventListener('mouseover', function () {
    hidenTwo.classList.add("active")
    cuerpo.classList.add("blur");
});
varTwo.addEventListener('mouseleave', function () {
    hidenTwo.classList.remove("active");
    cuerpo.classList.remove("blur");
});
//submenu numero 3
let varThree = document.getElementById("opcion3");
varThree.addEventListener('mouseover', function () {
    document.getElementById("hiden-box-three").classList.add("active")
    cuerpo.classList.add("blur");
});
varThree.addEventListener('mouseleave', function () {
    document.getElementById("hiden-box-three").classList.remove("active")
    cuerpo.classList.remove("blur");
});

//submenu numero 4
let varFour = document.getElementById("opcion4");
varFour.addEventListener('mouseover', function () {
    document.getElementById("hiden-box-four").classList.add("active")
    cuerpo.classList.add("blur");
});
varFour.addEventListener('mouseleave', function () {
    document.getElementById("hiden-box-four").classList.remove("active")
    cuerpo.classList.remove("blur");
});


// document.addEventListener("DOMContentLoaded", function () {
//     if (!localStorage.getItem("popupShown")) {
//         openPopup();
//     }
// });

// function openPopup() {
//     document.getElementById("popup").style.display = "block";
// }

// function closePopup() {
//     document.getElementById("popup").style.display = "none";
//     localStorage.setItem("popupShown", "true");
// }


// let popup; {

//     cuerpo = document.getElementById("cuerpo");
// }

function openPopup() {
    document.getElementById("popup").style.display = "block";
    // cuerpo.classList.add("popup");
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}



