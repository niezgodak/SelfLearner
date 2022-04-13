const buttonShow = document.querySelector('.wordbtn')
const buttonOK = document.querySelector('.known')
buttonOK.classList.add('d-none')
const buttonNotOK = document.querySelector('.unknown')
buttonNotOK.classList.add('d-none')
const buttonGoBack= document.querySelector('.go-back')
buttonGoBack.classList.add('d-none')
const word = document.querySelector('.word')
const wordForeign = document.querySelector('.word-foreign')
const wordExample = document.querySelector('.word-example')
const wordGroup = document.getElementById('wordGroup').value
console.log(wordExample);
const apihost = 'http://127.0.0.1:8000/wordgroups/wordsdata/'
let i = 1

function toggleButtons(){
    buttonShow.classList.toggle('d-none');
    buttonOK.classList.toggle('d-none');
    buttonNotOK.classList.toggle('d-none');}

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

fetch('http://127.0.0.1:8000/wordgroups/' + wordGroup + '/wordsdata/?format=json')
    .then(response => {
        return response.json()
    })
     .then(function(elements) {
         const elementsList = Array.from(elements)
         word.innerText = `${elements[i-1].your_language}`;
         wordForeign.classList.add('d-none');
         wordExample.classList.add('d-none');
         wordForeign.innerText = `${elements[i-1].foreign_language}`;
         wordExample.innerText = `${elements[i-1].example_of_use}`;
         buttonShow.addEventListener('click',function (){
             wordForeign.classList.toggle('d-none');
             wordExample.classList.toggle('d-none');
             i++;
             toggleButtons()
             if (elementsList.length == i -1){
                 buttonGoBack.classList.toggle('d-none')
                 buttonOK.classList.toggle('d-none');
                 buttonNotOK.classList.toggle('d-none');
             }
         })
         buttonOK.addEventListener('click', function (){
             word.innerText = `${elements[i-1].your_language}`;
             let wordId = elements[i-2].id;
             let wordCounter = elements[i-2].counter;
             apiUpdate(wordId, wordCounter, true)
             wordForeign.innerText = `${elements[i-1].foreign_language}`;
             wordExample.innerText = `${elements[i-1].example_of_use}`;
             wordForeign.classList.toggle('d-none');
             wordExample.classList.toggle('d-none');
             toggleButtons()
         })
         buttonNotOK.addEventListener('click', function (){
             word.innerText = `${elements[i-1].your_language}`;
             let wordId = elements[i-2].id;
             let isWordLearned = elements[i-2].is_learned;
             let wordCounter = elements[i-2].counter + 1;
             apiUpdate(wordId, wordCounter, isWordLearned)
             wordForeign.innerText = `${elements[i-1].foreign_language}`;
             wordExample.innerText = `${elements[i-1].example_of_use}`;
             wordForeign.classList.toggle('d-none');
             wordExample.classList.toggle('d-none');
             toggleButtons()

     })})


