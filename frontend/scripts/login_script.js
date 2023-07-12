email = document.getElementById("user_email")
password = document.getElementById("user_password")
error_msg = document.getElementById("error_msg")
botao = document.getElementById("botao")



// verifying if email and password are not empty
function verifyEmpty(){
    if(email.value == "" || password.value == ""){
        console.log("email or password is missing")
        error_msg.innerText = "you must enter email and password!"
        return false
    }else{
        return true
    }
}


// doing somethin with login response

function loginVerification(resp){
    if(resp["resp"]== "user_not_found"){
        error_msg.innerText = "user not found"
        return console.log("user not found")
    }
    if(resp["resp"]){
        console.log("login sucess, welcome " + resp["name"])
    }else{
        error_msg.innerText = "wrong password"
    }

    
}


// making a request using fecth

function loginRequest(){
    if(verifyEmpty()){
        fetch("http://127.0.0.1:5000/login", {method: "POST",
                                              headers: {"Content-Type": "application/json"},
                                              body: JSON.stringify({ "email": email.value,
                                                                     "password": password.value})})
        .then((res) => res.json())
        .then((data) => loginVerification(data))
        .catch((err) => console.log("Deu erro filão: " + err))
    }
}



//add a button event

botao.addEventListener("click", loginRequest)

// add event to enter key pressed

document.addEventListener('keydown', (keyPressed) => { if(keyPressed.key == "Enter"){loginRequest()}})

