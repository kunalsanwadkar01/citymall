let submit = document.getElementById("submit")
let name1,email,contact,date,slots;

submit.addEventListener("click",function(event){
    event.preventDefault();

    name1 = document.getElementById("name1").value
    email = document.getElementById("email").value
    contact = document.getElementById("number").value
    date = new Date();
    date.setDate(date.getDate() + 1); 
    // date = document.getElementById("date").value
    // slots = document.getElementById("slots").value


    if(document.getElementById('slot1').checked) {   
        slots = document.getElementById('slot1').value;
        let ticket= name1+date+slots;
        let firstSlot = localStorage.getItem("firstSlot");
        if(firstSlot==null){
            ticketarr = [];
        }
        else{
           ticketarr = JSON.parse(firstSlot);
        }
    
        

        // function sendEmail() {
        //     Email.send({
        //     Host: "smtp.gmail.com",
        //     Username : "trialminiproject@gmail.com",
        //     Password : "Vit@778800",
        //     To : 'kunalsanwadkar@gmail.com',
        //     From : "trialminiproject@gmail.com",
        //     Subject : "You can show the token below along with vaccinated certificate to get entry at the mall",
        //     Body : ticket,
        //     }).then(
        //         message => alert("mail sent successfully")
        //     );
        // }

        // sendEmail();
        if(ticketarr.length < 10){   //made 10 for testing purpose 
            ticketarr.push(ticket);
            localStorage.setItem("firstSlot",JSON.stringify(ticketarr));
            alert("successfully booked your slot !!"+" You have booked "+slots + " for date : " + date +  " Your token number is "+ ticket);

        }else {
            alert("slot 1 is full !")
        }
        
        ticket="";
        console.log(ticketarr.length)  //length parameter
          
        } else if(document.getElementById('slot2').checked) {   
                slots = document.getElementById('slot2').value;
                let ticket= name1+date+slots;
                let secondSlot = localStorage.getItem("secondSlot");
                if(secondSlot==null){
                  ticketarr1 = [];
                }
                else{
                    ticketarr1 = JSON.parse(secondSlot);
                }
              
                

                if(ticketarr1.length < 50){
                    ticketarr1.push(ticket);
                    localStorage.setItem("secondSlot",JSON.stringify(ticketarr1));
                    alert("successfully booked your slot !!"+" You have booked "+slots + " for date : " + date +  " Your token number is "+ ticket);
        
                }else {
                    alert("slot 2 is full !")
                }
                
                ticket="";
              
            }else {   
                slots = document.getElementById('slot3').value;
                let ticket= name1+date+slots;
                let thirdSlot = localStorage.getItem("thirdSlot");
                if(thirdSlot==null){
                   ticketarr2 = [];
                }
                else{
                   ticketarr2 = JSON.parse(thirdSlot);
                }
            
                

                if(ticketarr2.length < 50){
                    ticketarr2.push(ticket);
                    localStorage.setItem("thirdSlot",JSON.stringify(ticketarr2));
                    alert("successfully booked your slot !!"+" You have booked "+slots + " for date : " + date +  " Your token number is "+ ticket);
        
                }else {
                    alert("slot 3 is full !")
                }
                
                ticket="";  
            }
    
    
    


    




})


// window.setInterval(function(){ // Set interval for checking
//     var date = new Date(); // Create a Date object to find out what time it is
//     if(date.getHours() === 23 && date.getMinutes() === 59){ // Check the time
//         localStorage.clear()
//     }
// }, 60000);


function ticketcheck(){
let ticketcode = document.getElementById("verifyticket")
let token;
ticketcode.addEventListener('click',function(event){
    event.preventDefault();

    token= document.getElementById('ticketcode').value
    console.log(token)
    let token1 = JSON.parse(localStorage.getItem('firstSlot'))
    let token2 = JSON.parse(localStorage.getItem('secondSlot'))
    let token3 = JSON.parse(localStorage.getItem('thirdSlot'))

    console.log(token1)
    if(token1.includes(token) || token2.includes(token) || token3.includes(token)){
        alert("welcome to City Mall")

    } else {
        alert("wrong token, please check your token code")
    }
})
}
    

