const words = document.querySelectorAll('.list-group-item')

words.forEach(function (word){
    word.addEventListener('mouseover', function (){
        this.style.backgroundColor = '#E9DAC1';
    })
    word.addEventListener('mouseout', function (){
        this.style.backgroundColor = 'white';
    })

})

document.querySelectorAll('.start').forEach(function (word){
    word.addEventListener('mouseover', function (){
        this.style.backgroundColor = '#E9DAC1';
    })
        word.addEventListener('mouseout', function (){
        this.style.backgroundColor = 'white'
    })

})

// document.querySelector('.wordbtn').addEventListener('click', function(){
//     document.querySelector('.word').innerHTML = ""<h1>${words.1.foreign_laguage}</h1>"";
//     });

fetch('words/views/')
        .then(function(response) { return response.json(); })
        .then(function(elements) {
            console.log(elements);
        })
