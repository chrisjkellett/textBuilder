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

var removeListeners = function(){
    aboutBox.style.display = 'none';
    loginForm.style.display = 'none';
    registerForm.style.display = 'none';
};


//TOGGLE register/login
loginEvent2.addEventListener('click', function(){
    if(loginForm.style.display == 'flex'){
        loginForm.style.display = 'none';
        registerForm.style.display = 'flex';
    }else{
        removeListeners();
        loginForm.style.display = 'flex';
    };
});

