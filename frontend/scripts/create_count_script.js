const user_name        = document.getElementById("user_name")
const user_email       = document.getElementById("user_email")
const user_password    = document.getElementById("user_password")
const confirm_password = document.getElementById("confirm_password")
const birth_date       = document.getElementById("birth_date")
const error_msg        = document.getElementById("error_msg")
const button           = document.getElementById("botao")

// verify if all inputs are not empty

function verifyEmpty(){
    if(user_name.value == "" || user_email.value == "" || user_password.value == "" || confirm_password.value == "" || birth_date.value == ""){
        error_msg.innerText = "All fields are required"
        console.log("All fields are required")
    }else if(user_password.value != confirm_password.value){
        error_msg.innerText = "Password must be the same"
        console.log("Password must be the same")   
    }else{
        return true
    }
}


// sending users data to api

function sendData(){
    if(verifyEmpty())
        {
        fetch("http://127.0.0.1:5000/create_account",{method: "POST",
                                                      headers: {"Content-Type": "application/json"},
                                                      body: JSON.stringify({"name" : user_name.value,
                                                                            "email": user_email.value,
                                                                            "password": user_password.value,
                                                                            "birth date": birth_date.value})})
        .then((res) => res.json())
        .then((data) => {if(data["resp"]){window.location.replace("login_done.html")}else{registration_answer(data["notification"])}})
        .catch((err) => console.log("Deu erro amigão: " + err))
        }
}



// Make a error registration answer

function registration_answer(answer){
    error_msg.innerText = answer
    }

// Add a button listener

button.addEventListener('click', sendData)

// add event to enter key pressed

document.addEventListener('keydown', (keyPressed) => { if(keyPressed.key == "Enter"){sendData()}})