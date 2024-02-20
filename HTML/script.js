//Comportamiento de la web

//menu de categorias principal
let varOne=document.getElementById("opcion1");
let hidenOne=document.getElementById("hiden-box-one");

varOne.addEventListener('mouseover',function(){
    hidenOne.classList.add("active");
});
varOne.addEventListener('mouseleave',function(){
    hidenOne.classList.remove("active");
});