document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", function(){

            const spinner = document.getElementById("loading");

            if(spinner){
                spinner.style.display = "flex";
            }

        });

    }

});