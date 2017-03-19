//TOGGLE login
var loginEvent = document.querySelector('#loginEvent');
var loginForm = document.querySelector('#loginForm');
loginEvent.addEventListener('click', function(){
    if(loginForm.style.display == 'flex'){
        loginForm.style.display = 'none';
    }else{
        removeListeners();
        loginForm.style.display = 'flex';
    };
});