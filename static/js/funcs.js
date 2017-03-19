//sort array numerically
function compareNumbers(a, b){  
    return a - b;
};


//check words against RegEx
var validateWords = function(){
    for (var i in lTextB){
        if (lTextB[i].search(RegPunc) != -1){
            notValids.push(parseInt(i));
        };
    };
};

var getLevel = function(){
    if (selectedLevel == 'hard'){
        level = hard;
    }else if (selectedLevel == 'intermediate'){
        level = intermediate;
    }else{
        level = easy;
    }
};

var trimWords = function(listToTrim){
    for (var i in listToTrim){
        var trimmed = listToTrim[i];
        if (trimmed == ""){
            listToTrim.splice(i, 1); 
        };
    };
}

var resetVariables = function(){
    lTextB = lTextA;
    holdsGaps.innerHTML = '';
    holdsAns.innerHTML = '';
    notValids = [];
    holdRandomGaps = [];
    repeatEx = true;
};

var removeListeners = function(){
    aboutBox.style.display = 'none';
    loginForm.style.display = 'none';
    savedFiles.style.display = 'none';
    registerForm.style.display = 'none';
};


var getCloseBtns = function(){
    for (i of closeBox){
        i.addEventListener('click', function(){
    removeListeners();
        });
    };
};
