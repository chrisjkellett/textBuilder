
//body - stage 1: select gaps
var setRandomGaps = function(){
    for (var i = 0; i < maxFor; i++){
    var selectRandGap = Math.round(Math.random() * (lTextLength - 1));
    if (holdRandomGaps.includes(selectRandGap) || notValids.includes(selectRandGap)){
        if (holdRandomGaps.length != 0){
        maxFor += 1;
        };
    }else{
        holdRandomGaps.push(selectRandGap);
        };
    };
    holdRandomGaps.sort(compareNumbers);
    for (gap of holdRandomGaps){
        lTextB[gap] = 'Qx';
    };
    return lTextB;
};


//body - stage 2: write to page
var writetoPage = function(){
    holdsForm.style.display = 'none';
    clozeEx.style.display = 'block';
    setHiddenTextArea = document.querySelector('#textAreaHidden');
    if (setHiddenTextArea != null){
    setHiddenTextArea.value = sText;
    }
    for(var i = 0; i < lTextLength; i++) {
        if(lTextB[i] != 'Qx'){
            holdsGaps.innerHTML += `<span id="w${i}" class="myWord">${lTextB[i]}</span> `;
        }else{
            holdsGaps.innerHTML += `<input type="text" id="Q${i}" class="myInput"></input> `;
        };
    };
};


//body - stage 3: correct exercise
var correctEx = function(){
    clozeEx.style.display = 'none';
    clozeAns.style.display = 'block';
    for(var i=0; i < lTextLength; i++){
        if(lTextB[i] == 'Qx'){
            var getInput = document.querySelector('#Q' + i).value;
            if(getInput == ''){
                getInput = '-';
            };

            if(lTextA[i] == getInput){
                holdsAns.innerHTML += `<span class="feedback successy raleway font-small" id="Q${i}"><strong>${lTextA[i]}</strong> \u2713</span> `;
            }else if(lTextA[i] != getInput && getInput == '-'){
                holdsAns.innerHTML += `<span class="feedback alerty raleway font-small" id="Q${i}"><strong>${lTextA[i]}</strong></span> `;
            }else{
                holdsAns.innerHTML += `<strike>${getInput}</strike>&nbsp;<span class="feedback dangery raleway font-small" id="Q${i}"><strong>${lTextA[i]}</strong></span>
                 `;
        };  
    }else{
        holdsAns.innerHTML += `${lTextA[i]} `;
    };
};
    var correctAns = document.querySelectorAll('.success').length;
    correctAnsAll += correctAns;
    var totalGaps = holdRandomGaps.length;
    totalGapsAll += totalGaps;
    var percentage = Math.round((correctAns/totalGaps) * 100);
    percentageAll += percentage;
    analysisDiv.innerHTML = `Score: <strong>${correctAns}/${totalGaps}</strong> (${percentage}%).<br>`
    if(repeatEx){
        analysisDiv.innerHTML += `Total: <strong>${correctAnsAll}/${totalGapsAll}</strong> (${percentageAll}%).<br>`
    };
};










