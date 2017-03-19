//TOGGLE toolbox
var savedFiles = document.querySelector('#savedFiles');
var saveFileEvent = document.querySelector('#saveFileEvent');
saveFileEvent.addEventListener('click', function(){
    if(savedFiles.style.display == 'flex'){
        savedFiles.style.display = 'none';
    }else{
        removeListeners();
        savedFiles.style.display = 'flex';
    };
});

var removeListeners = function(){
    aboutBox.style.display = 'none';
    savedFiles.style.display = 'none';
};
