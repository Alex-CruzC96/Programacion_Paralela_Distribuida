//Comportamiento de la web

//menu de categorias principal opcion 1
let varOne = document.getElementById("opcion1");
let hidenOne = document.getElementById("hiden-box-one");
let cuerpo=document.getElementById("cuerpo");

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

//Programacion de cuadrito
let cuadrito = document.getElementById("cuadrito");
let options = document.getElementById("columna2-header");
var control=false;

cuadrito.addEventListener("click",function(){
    if (!control){
        options.classList.add("active");
        cuerpo.classList.add("blur");
        control=!control;
    }
    else{
        options.classList.remove("active");
        cuerpo.classList.remove("blur");
        control=!control;
    }
});
//control del aside al clickear fuera de el
cuerpo.addEventListener('click',function(){
    if(control){
        options.classList.remove("active");
        cuerpo.classList.remove("blur");
        control=!control;
    }
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

function openPopup() {
    document.getElementById("popup").style.display = "block";
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}



