var closeeye=document.querySelector(".close-eye");
var openeye=document.querySelector(".open-eye");
var passwordinput=document.querySelector("#passwordInput");
openeye.addEventListener("click",()=>
{
    closeeye.classList.toggle("show");
    console.log(passwordinput.type)
    if(passwordinput.type==="password"){
        passwordinput.type="text";
        
    }
    else if(passwordinput.type==="text"){
        passwordinput.type="password";
    }
});
var emailinput=document.querySelector("#emailInput");
var loginButton = document.querySelector(".loginb"); // Get the first element with the class "loginb"
loginButton.addEventListener("click", function() {
  if(emailinput.value===""|| passwordinput.value===""){
        var popup = document.getElementById("popup");
        popup.classList.remove("hidden");
  }
  else{
    window.location.href = "../templates/main_page.html";
  }
  
});

