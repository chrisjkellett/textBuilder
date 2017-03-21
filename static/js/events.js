
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



//TOGGLE about
aboutEvent.addEventListener('click', function(){
    if(aboutBox.style.display == 'flex'){
        aboutBox.style.display = 'none';
    }else{
        removeListeners();
        aboutBox.style.display = 'flex';
    };
});


getTextArea.addEventListener('click', function(){
    removeListeners();
});

//set listeners for close boxes
getCloseBtns();
