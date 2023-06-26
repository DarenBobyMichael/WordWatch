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
   window.location.href = "login";
});

const textarea = document.getElementById('typing-textarea');
const text = textarea.value;
const typingSpeed = 10; // Speed of typing in milliseconds

textarea.value = ''; // Clear the textarea content

let index = 0;

function typeText() {
  if (index < text.length) {
    textarea.value += text.charAt(index);
    index++;
    setTimeout(typeText, typingSpeed);
  }
}

typeText();