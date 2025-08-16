let InputUsername = null;
let InputPassword = null;

let SignUpButton = document.getElementById("sign_in_button_button");
SignUpButton.addEventListener("click",async ()=>{
  InputUsername = document.getElementById("user_name_id").value;
  InputPassword = document.getElementById("password_id").value;

  if(InputUsername.length<5 || InputUsername.length>20){
    alert("invalid username, your username length should be bigger than 5 "+
      "and smaller than 20");
    return;
  }
  if(InputUsername.includes(" ")){
    alert("invalid username, your username should not include space in it");
  }
  if((/[0-9]/.test(InputPassword)) != true){
    alert("invalid password, your password should have at least one number");
    return;
  }
  if(InputPassword.includes(" ")){
    alert("invalid password, your password should not include space in it");
    return;
  }

  console.log(InputUsername);
  let functionEnd = false;
  await fetch(`http://127.0.0.1:8000/username_check_if_exist/${InputUsername}`)
  .then((temp)=>temp.json())
  .then((whether_exist)=>{
    console.log(whether_exist);
    if(whether_exist === "exist"){
      alert("the username already exist, try something else");
      functionEnd = true;
    }
    else if(whether_exist === "not_exist"){
      console.log("this username does not exist before, the username is ok");
      functionEnd = false;
    }
    else{
      alert("there is an error");
      functionEnd = true;
    }
  })

  if(functionEnd === true){
    return;
  }
  
  await fetch("http://127.0.0.1:8000/get_username_and_password", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ 
      username:InputUsername,
      password:InputPassword
    })
  });

  alert("you are signed up");
  return;
  
})