
submitBtn.addEventListener('click', function(){
    sText = getTextArea.value;
    selectedLevel = document.querySelector('#setLevel').value;
    getLevel();
    lTextA = sText.split(" ");
    trimWords(lTextA);
    lTextB = sText.split(" ");
    trimWords(lTextB);
    if (lTextA.length > minInput && lTextA.length < maxInput){
        lTextLength = lTextA.length;
        maxFor = Math.ceil(lTextLength*level);
        validateWords();
        setRandomGaps();
        writetoPage();
    }else{
        errorMessage.style.display = "inline";
    };
});


submitBtn2.addEventListener('click', function(){
    correctEx();
});


submitBtn3.addEventListener('click', function(){
    location.reload();
});


submitBtn5.addEventListener('click', function(){
    resetVariables();
    clozeAns.style.display = 'none';
    holdsForm.style.display = 'block';
});

//TOGGLE login
loginEvent.addEventListener('click', function(){
    if(loginForm.style.display == 'flex'){
        loginForm.style.display = 'none';
    }else{
        removeListeners();
        loginForm.style.display = 'flex';
    };
});


//TOGGLE about
aboutEvent.addEventListener('click', function(){
    if(aboutBox.style.display == 'flex'){
        aboutBox.style.display = 'none';
    }else{
        removeListeners();
        aboutBox.style.display = 'flex';
    };
});


//TOGGLE toolbox
toolBoxEvent.addEventListener('click', function(){
    if(toolBox.style.display == 'flex'){
        toolBox.style.display = 'none';
    }else{
        removeListeners();
        toolBox.style.display = 'flex';
    };
});


getTextArea.addEventListener('click', function(){
    removeListeners();
});

//set listeners for close boxes
getCloseBtns();