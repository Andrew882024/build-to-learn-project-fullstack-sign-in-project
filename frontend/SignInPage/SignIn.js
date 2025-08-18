let InputUsername = null;
let InputPassword = null;

let signInButton = document.getElementById("sign_in_button_button")
signInButton.addEventListener("click",async()=>{
  InputUsername = document.getElementById("InputUsername").value;
  InputPassword = document.getElementById("InputPassword").value;

  if(InputUsername === ""){
    alert("username can not be empty, please enter your username");
    return;
  }
  if(InputPassword === ""){
    alert("password can not be empty, please enter your password");
    return;
  }

  let functionEnd = false;
  await fetch(`http://127.0.0.1:8000/username_check_if_exist/${InputUsername}`)
  .then((temp)=>temp.json())
  .then((whether_exist)=>{
    console.log(whether_exist);
    if(whether_exist === "exist"){
      functionEnd = false;
    }
    else if(whether_exist === "not_exist"){
      alert("this username does not exist, try other username");
      functionEnd = true;
    }
    else{
      alert("there is an error");
      functionEnd = true;
    }
  })
  if(functionEnd === true){
    return;
  }

  await fetch(`http://127.0.0.1:8000/check_whether_username_and_password_match/${InputUsername}/${InputPassword}`)
  .then((output)=>output.json())
  .then((whether_match)=>{
    if(whether_match === "username_and_password_match"){
      alert("username and password match, you are signed in");
      window.location.href="./YouAreSignedIn.html";
    }
    else if(whether_match === "username_and_password_does_not_match"){
      alert("username and password does not match, try again");
    }
    else{
      alert("there is an error");
    }
  })
})