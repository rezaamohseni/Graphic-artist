const singInBtn = document.querySelector("#sign_in-btn");
const singUpBtn = document.querySelector("#sign_up-btn");
const container = document.querySelector(".container");

// add event
singUpBtn.addEventListener('click', ()=>{
  container.classList.add("sign_up-mode")
});

singInBtn.addEventListener('click', ()=>{
  container.classList.remove("sign_up-mode")
});