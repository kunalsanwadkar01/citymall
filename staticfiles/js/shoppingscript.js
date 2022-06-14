let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{

  menu.classList.toggle('fa-times');
  navbar.classList.toggle('active');

}

window.onscroll = () =>{

  menu.classList.remove('fa-times');
  navbar.classList.remove('active');

  if(window.scrollY > 60){
    document.querySelector('#scroll-top').classList.add('active');
  }else{
    document.querySelector('#scroll-top').classList.remove('active');
  }

}

function loader(){
  document.querySelector('.loader-container').classList.add('fade-out');
}

function fadeOut(){
  setInterval(loader, 3000);
}

window.onload = fadeOut();




var slideIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("slidefood");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  x[slideIndex-1].style.display = "block";
  setTimeout(carousel, 2000); // Change image every 2 seconds
}




var contactform = document.getElementById("contactform");

contactform.addEventListener('submit',function(event){
  event.preventDefault();
  let firstName = document.getElementById("firstname").value
  let lastName = document.getElementById("firstname").value
  let contactNumber = document.getElementById("contnumber").value
  let emailAdd = document.getElementById("emailadd").value
  let message = document.getElementById("message").value

  console.log(firstName + lastName + contactNumber + emailAdd + message);



console.log(firstName + lastName + contactNumber + emailAdd + message);

// email
function sendEmail() {
	Email.send({
	Host: "smtp.gmail.com",
	Username : "trialminiproject@gmail.com",
	Password : "Vit@778800",
	To : emailAdd,
	From : "trialminiproject@gmail.com",
  Subject : "Thanks for contacting us !",
	Body : "demo",
	}).then(
		message => alert("Check Your Mail !")
	);
}

})


var slideIndex1 = 0;
carousel1();

function carousel1() {
  var i;
  var x = document.getElementsByClassName("mySlidesx");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex1++;
  if (slideIndex1 > x.length) {slideIndex1 = 1}
  x[slideIndex1-1].style.display = "block";
  setTimeout(carousel1, 2000); // Change image every 2 seconds
}
