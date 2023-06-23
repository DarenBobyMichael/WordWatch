var x=document.querySelector("#sidebar-close");
var y=document.querySelector(".sidebar");
x.addEventListener("click",()=>
{
    y.classList.toggle("close");
    
});
var z = document.querySelector(".user");
var rightsidebar=document.querySelector(".rightsidebar");
z.addEventListener("click", () => {
  rightsidebar.classList.toggle("show");
});

document.addEventListener("click", (event) => {
    if (!rightsidebar.contains(event.target) && !event.target.matches(".user")) {
      rightsidebar.classList.remove("show");
    }
});

var logoutButton = document.querySelector("#logout"); // Get the first element with the class "loginb"
logoutButton.addEventListener("click", function() {
  console.log("aaa");
   window.location.href = "../templates/index.html";
});