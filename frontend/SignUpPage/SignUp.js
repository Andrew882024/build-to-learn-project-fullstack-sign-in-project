let InputUsername = null;
let InputPassword = null;

let SignUpButton = document.getElementById("sign_in_button_button");
SignUpButton.addEventListener("click",()=>{
  InputUsername = document.getElementById("user_name_id").value;
  InputPassword = document.getElementById("password_id").value;

  console.log(InputUsername);

  fetch(`http://127.0.0.1:8000/username_check_if_exist/${InputUsername}`)
  .then((temp)=>temp.json())
  .then((whether_exist)=>{
    console.log(whether_exist);
    if(whether_exist === "exist"){
      alert("the username already exist, try something else");
    }
    else if(whether_exist === "not_exist"){
      alert("not exist");
    }
    else{
      alert("there is an error");
    }
  })
  
  fetch("http://127.0.0.1:8000/get_username_and_password", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ 
      username:InputUsername,
      password:InputPassword
    })
  });
  
})