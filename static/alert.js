const email = document.getElementById("mce-EMAIL")
const button = document.getElementById("mc-embedded-subscribe")
const change = document.getElementById("change")

button.onclick =  function (){
    if (email.value === ''){
        Swal.fire({
            text:'Email required'
        })
        return false;
    }else{
        validateEmail(email);
    }
}

function validateEmail(inputText){
    var mailformat =  /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;;
    if(inputText.value.match(mailformat)){
        change.innerHTML = 'Thanks for subscribing';
        true;
    }else{
        Swal.fire({
            text: "Email is not valid"
        })
        return false;
    }
}