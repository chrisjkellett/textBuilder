//get global variables
var submitBtn = document.querySelector('#submitBtn');
var submitBtn2 = document.querySelector('#submitBtn2');
var submitBtn3 = document.querySelector('#submitBtn3');
var submitBtn4 = document.querySelector('#submitBtn4');
var submitBtn5 = document.querySelector('#submitBtn5');
var getTextArea = document.querySelector('#textArea');
var holdsForm = document.querySelector('#holdsForm');
var holdsGaps = document.querySelector('#holdsGaps');
var holdsAns = document.querySelector('#holdsAns');
var clozeAns = document.querySelector('#clozeAns');
var clozeEx = document.querySelector('#clozeEx');
var errorMessage = document.querySelector('#errorMessage');
var analysisDiv = document.querySelector('#analysis');
var registerForm = document.querySelector('#registerForm');
var aboutBox = document.querySelector('#aboutBox');
var closeBox = document.querySelectorAll('.closeBox');
var myInputs; 

//set variables
const minInput = 9;
const maxInput = 200;
var sText;
var lTextA = []; 
var lTextB = [];
var easy = 0.07; var intermediate = 0.14; var hard = 0.21;
var level;
var holdRandomGaps = [];
var lTextLength;
var maxFor;
var selectedLevel; 
var RegPunc = /[,."'?!\-–¡¿():;\dA-Z]/;
var notValids = [];
var totalGapsAll = 0;
var percentageAll = 0;
var correctAnsAll = 0; 
var repeatEx = false;