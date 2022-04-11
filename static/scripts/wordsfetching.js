const button = document.querySelector('.wordbtn')
const word = document.querySelector('.word')
let i = 0


fetch('http://127.0.0.1:8000/wordgroups/food/wordsdata/?format=json')
    .then(response => {
        return response.json()
    })
     .then(function(elements) {
         //tu pętlę chyba trzeba zrobić
         word.innerText = `${elements[i].your_language}`
         button.addEventListener('click',function (){
             word.innerText = `${elements[i].foreign_language}`;
             i++

         })})


