//globals available only when logged in
var savedFiles = document.querySelector('#savedFiles');
var saveFileEvent = document.querySelector('#saveFileEvent');
var saveBtn = document.querySelector('#submitBtn4');
var add_Title = document.querySelector('#addTitle');
var setHiddenTextArea = document.querySelector('#textAreaHidden');

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

var confirmDelete = function(id){
    spanId = '#delete-' + id.toString();
    glyphs = document.querySelectorAll('.glyphicon');
    var x = document.querySelector(spanId);
    x.style.display = 'block';
    for (var i=0; i<glyphs.length; i++){
        glyphs[i].style.display = 'none';
    };
};

var cancelDelete = function(id){
    spanId = '#delete-' + id.toString();
    glyphs = document.querySelectorAll('.glyphicon');
    var x = document.querySelector(spanId);
    x.style.display = 'none';
    for (var i=0; i<glyphs.length; i++){
        glyphs[i].style.display = 'block';
    };
};
