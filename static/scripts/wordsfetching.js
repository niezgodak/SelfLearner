const buttonShow = document.querySelector('.wordbtn')
const buttonOK = document.querySelector('.known')
buttonOK.classList.add('d-none')
const buttonNotOK = document.querySelector('.unknown')
buttonNotOK.classList.add('d-none')
const buttonNextRound= document.querySelector('.next-round')
buttonNextRound.classList.add('d-none')
const buttonStart= document.querySelector('.start')
const word = document.querySelector('.word')
const wordForeign = document.querySelector('.word-foreign')
const wordExample = document.querySelector('.word-example')
document.querySelector('.successful').classList.add('d-none')
document.querySelectorAll('.another').forEach(function(button){
    button.classList.add('d-none')
})

const wordGroup = document.getElementById('wordGroup').value
const user = document.getElementById('user').value
const apihost = 'https://selflearnerapp.herokuapp.com/wordgroups/wordsdata/'
let i = 1

function toggleButtons(){
    buttonOK.classList.toggle('d-none');
    buttonNotOK.classList.toggle('d-none');
    buttonShow.classList.toggle('d-none');}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function apiUpdate(wordId, counter, is_learned){
    return fetch(
    apihost + wordId + '/',
    {
        credentials: 'same-origin',
      headers:{'Content-Type': 'application/json', "X-CSRFToken": getCookie("csrftoken")},
      body: JSON.stringify({ counter: counter, is_learned: is_learned }),
      method: 'PUT'
    }
  ).then(
    function (resp) {
      if(!resp.ok) {
        alert('Wystąpił błąd! Otwórz devtools i zakładkę Sieć/Network, i poszukaj przyczyny');
      }
      return resp.json();
    }
  );
}

function apiUpdateIsLearned(wordId, is_learned){
    return fetch(
    apihost + wordId + '/',
    {
        credentials: 'same-origin',
      headers:{'Content-Type': 'application/json', "X-CSRFToken": getCookie("csrftoken")},
      body: JSON.stringify({ is_learned: is_learned }),
      method: 'PUT'
    }
  ).then(
    function (resp) {
      if(!resp.ok) {
        alert('Wystąpił błąd! Otwórz devtools i zakładkę Sieć/Network, i poszukaj przyczyny');
      }
      return resp.json();
    }
  );
}
function learnOn(elements){
    let t = []
         elements.forEach(function (element){
             if(element.is_learned === false){
             t.push(element)
             }})
    console.log(t);
    if(t.length === 0){
        word.classList.add('d-none')
        wordForeign.classList.add('d-none')
        wordExample.classList.add('d-none')
        buttonShow.classList.add('d-none')
        document.querySelector('.successful').classList.remove('d-none')
        document.querySelectorAll('.another').forEach(function(button){
            button.classList.remove('d-none')
            button.addEventListener('click', function(){
            fetch('https://selflearnerapp.herokuapp.com/wordgroups/' + wordGroup + '/' + user + '/wordsdata/?format=json')
    .then(response => {
        return response.json()
    })
     .then(function (elements){
         elements.forEach(function (element){
             let wordId = element.id;
             apiUpdateIsLearned(wordId, false)
         })
         })
        })
        })
    }
        let i = 0
         word.innerText = `${t[i].your_language}`;
         wordForeign.classList.add('d-none');
         wordExample.classList.add('d-none');
         wordForeign.innerText = `${t[i].foreign_language}`;
         wordExample.innerText = `${t[i].example_of_use}`;
         buttonShow.classList.remove('d-none');
         buttonShow.addEventListener('click',function (){
             console.log('klikniete w show');
             buttonShow.classList.add("d-none")
             buttonOK.classList.remove("d-none")
             buttonNotOK.classList.remove("d-none")

             wordForeign.classList.remove('d-none');
             wordExample.classList.remove('d-none');
             i++;
         })
         buttonOK.addEventListener('click', function (){
             if(t.length === i){
                 let wordId = t[i-1].id;
                 let wordCounter = t[i-1].counter;
                 apiUpdate(wordId, wordCounter, true);
                 buttonOK.classList.add('d-none');
                 buttonNotOK.classList.add('d-none');
                  t.splice(i-1, 1)
                 i --
                 buttonNextRound.classList.toggle('d-none');

             }
             else{
             word.innerText = `${t[i].your_language}`;
             let wordId = t[i-1].id;
             let wordCounter = t[i-1].counter;
             apiUpdate(wordId, wordCounter, true)
             wordForeign.innerText = `${t[i].foreign_language}`;
             wordExample.innerText = `${t[i].example_of_use}`;
             wordForeign.classList.toggle('d-none');
             wordExample.classList.toggle('d-none');
             toggleButtons()
                 t.splice(i-1, 1)
                 i --

                 }
         })
         buttonNotOK.addEventListener('click', function () {
             if (t.length == i) {
                 let wordId = t[i - 1].id;
                 let isWordLearned = t[i - 1].is_learned;
                 let wordCounter = t[i - 1].counter + 1;
                 apiUpdate(wordId, wordCounter, isWordLearned);
                 buttonOK.classList.add('d-none');
                 buttonNotOK.classList.add('d-none');
                 buttonNextRound.classList.toggle('d-none');


             } else {
                 word.innerText = `${t[i].your_language}`;
                 let wordId = t[i - 1].id;
                 let isWordLearned = t[i - 1].is_learned;
                 let wordCounter = t[i - 1].counter + 1;
                 apiUpdate(wordId, wordCounter, isWordLearned)
                 wordForeign.innerText = `${t[i].foreign_language}`;
                 wordExample.innerText = `${t[i].example_of_use}`;
                 wordForeign.classList.toggle('d-none');
                 wordExample.classList.toggle('d-none');

                 toggleButtons()
             }
         })
}


function first(){fetch('https://selflearnerapp.herokuapp.com/wordgroups/' + wordGroup + '/' + user + '/' + 'wordsdata/?format=json')
    .then(response => {
        return response.json()
    })
     .then(function (elements){
         elements.forEach(function (element){
             let wordId = element.id;
             apiUpdateIsLearned(wordId, false)
         })
         console.log("Zaczynamy runde wywolana przez funkcje first");
         learnOn(elements)
         buttonNextRound.addEventListener('click', function (){
             second()
             buttonNextRound.classList.toggle('d-none')
         })
         })}

function second(){fetch('https://selflearnerapp.herokuapp.com/wordgroups/' + wordGroup + '/' + user + '/wordsdata/?format=json')
    .then(response => {
        return response.json()
    })
     .then(function (elements){
         console.log("Zaczyna się druga runda");
         learnOn(elements)
         })}

first()

