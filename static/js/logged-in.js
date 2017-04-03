//globals available only when logged in
var savedFiles = document.querySelector('#savedFiles');
var saveFileEvent = document.querySelector('#saveFileEvent');
var saveBtn = document.querySelector('#submitBtn4');
var add_Title = document.querySelector('#addTitle');

//title for save
saveBtn.addEventListener('click', function(){
    if(add_Title.style.display == 'flex'){
        add_Title.style.display = 'none';
    }else{
        removeListeners();
        add_Title.style.display = 'flex';
    };
});

//listeners
saveFileEvent.addEventListener('click', function(){
    if(savedFiles.style.display == 'flex'){
        savedFiles.style.display = 'none';
    }else{
        removeListeners();
        savedFiles.style.display = 'flex';
    };
});



//remove listeners
var removeListeners = function(){
    aboutBox.style.display = 'none';
    savedFiles.style.display = 'none';
};
