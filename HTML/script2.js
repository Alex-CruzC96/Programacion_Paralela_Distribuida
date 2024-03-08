let cuadrito2 = document.getElementById("cuadrito");
let options2 = document.getElementById("columna2-header");
var control2=false;

cuadrito2.addEventListener("click",function(){
    if (!control2){
        options2.classList.add("active");
        cuerpo.classList.add("blur");
        control2=!control2;
    }
    else{
        options2.classList.remove("active");
        cuerpo.classList.remove("blur");
        control2=!control2;
    }
});
//control del aside al clickear fuera de el
cuerpo.addEventListener('click',function(){
    if(control2){
        options2.classList.remove("active");
        cuerpo.classList.remove("blur");
        control2=!control2;
    }
});