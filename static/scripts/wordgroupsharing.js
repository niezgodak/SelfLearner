// const apihost = 'http://127.0.0.1:8000/wordgroups/'
// const wordGroup = document.getElementById('wordGroupName').value
// console.log(wordGroup);
// const user = document.getElementById('user').value
// console.log(user);
// const addButton = document.querySelector('.add')
//
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
//
// function apiUpdateName(group, user){
//     return fetch(
//     apihost + group + '/wordgroupdata/',
//     {
//         credentials: 'same-origin',
//       headers:{'Content-Type': 'application/json', "X-CSRFToken": getCookie("csrftoken")},
//       body: JSON.stringify({ user: user }),
//       method: 'PUT'
//     }
//   ).then(
//     function (resp) {
//       if(!resp.ok) {
//         alert('Wystąpił błąd! Otwórz devtools i zakładkę Sieć/Network, i poszukaj przyczyny');
//       }
//       return resp.json();
//     }
//   );
// }
//
// addButton.addEventListener('click', function (){
//     apiUpdateName(wordGroup, user)
// })