// window.onload = function(e){

//   async function postData(url, data) {
//     // Default options are marked with *
//     const response = await fetch(url, {
//       method: 'POST', // *GET, POST, PUT, DELETE, etc.
//       // mode: 'cors', // no-cors, *cors, same-origin
//       cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//       credentials: 'same-origin', // include, *same-origin, omit
//       headers: {
//         'Content-Type': 'application/json',
//         // 'Content-Type': 'application/x-www-form-urlencoded',
//       },
//       redirect: 'follow', // manual, *follow, error
//       referrerPolicy: 'no-referrer', // no-referrer, *client
//       body: JSON.stringify(data) // body data type must match "Content-Type" header
//     });
//     return await response.json(); // parses JSON response into native JavaScript objects
//   }

//   console.log('start')
  
//   postData('http://127.0.0.1:8000/api/test', {'ererer': 232332, '3333': 454545})
//   .then((data) => {
//     console.log(data); // JSON data parsed by `response.json()` call
//   });
  
//   console.log('end')






//     const cities=[]
//     fetch('http://127.0.0.1:8000/api/get-cities')
//       .then((response) => {
//         return response.json();
//       }).then(function(data){
//         data.map(i => {
//           cities.push(i.name)
//         })
//       })

//     const inputStyles = 'border:1px solid blue; box-shadow:0 0 5px blue;'

//     autocomplete(document.getElementById("cityto"), cities);
//     autocomplete(document.getElementById("cityfrom"), cities);
//     const cityfrom = document.getElementById('cityfrom')
//     const cityto = document.getElementById('cityto');
//     const volume = document.getElementById('volume');
//     const weight = document.getElementById('weight');
//     const quantity = document.getElementById('quantity')

//     const inputData = [cityfrom, cityto,volume, weight, quantity  ]

//     for(let i=0; i<inputData.length; i++){
//         inputData[i].addEventListener('input', () => {
//             if((inputData[i]).value) {
//                 inputData[i].style.borderColor = '#e9ecef'
//                 inputData[i].style.boxShadow = 'none'
//             }
//         })
//         inputData[i].addEventListener('mouseenter', (e) => {
//           e.target.style.cssText = inputStyles
//       })
//         inputData[i].addEventListener('mouseleave', (e) => {
//           e.target.style = 'none'
//       })
//     }
  
// }
  
//   function autocomplete(inp, arr) {
//       inp.addEventListener("input", function(e) {
//         let a, b, i, val = this.value;
//         closeAllLists();
//         if (!val) {
//           return false;
//         } 
//         currentFocus = -1;
//         a = document.createElement("DIV");
//         a.style.cursor = 'pointer'
//         a.style.padding = '12px 16px'
//         a.style.boxShadow = '0px 8px 16px 0px rgba(0,0,0,0.2)'
//         a.style.overflowY = 'auto'

//         a.setAttribute("id", this.id + "autocomplete-list");
//         a.setAttribute("class", "autocomplete-items");

//         this.parentNode.appendChild(a);
//         /*for each item in the array...*/
//         for (i = 0; i < arr.length; i++) {
//           /*check if the item starts with the same letters as the text field value:*/
//           if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
//             /*create a DIV element for each matching element:*/
//             b = document.createElement("DIV");
//             /*make the matching letters bold:*/
//             b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
//             b.innerHTML += arr[i].substr(val.length);
//             /*insert a input field that will hold the current array item's value:*/
//             b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
//             /*execute a function when someone clicks on the item value (DIV element):*/
//                 b.addEventListener("click", function(e) {
//                 /*insert the value for the autocomplete text field:*/
//                 inp.value = this.getElementsByTagName("input")[0].value;
//                 /*close the list of autocompleted values,
//                 (or any other open lists of autocompleted values:*/
//                 closeAllLists();
//             });
//             a.appendChild(b);
//           }
//         }
//     });
//         inp.addEventListener("keydown", function(e) {
//           let x = document.getElementById(this.id + "autocomplete-list");
//           if (x) x = x.getElementsByTagName("div");
//           if (e.keyCode == 40) {
//             currentFocus++;
//             addActive(x);
//           } else if (e.keyCode == 38) { 
//             currentFocus--;
//             addActive(x);
//           } else if (e.keyCode == 13) {
//             /*If the ENTER key is pressed, prevent the form from being submitted,*/
//             e.preventDefault();
//             if (currentFocus > -1) {
//               /*and simulate a click on the "active" item:*/
//               if (x) x[currentFocus].click();
//             }
//           }
//     });
//       function addActive(x) {
//         /*a function to classify an item as "active":*/
//         if (!x) {
//           return false
//         };
//         /*start by removing the "active" class on all items:*/
//         removeActive(x);
//         if (currentFocus >= x.length) currentFocus = 0;
//         if (currentFocus < 0) currentFocus = (x.length - 1);
//         /*add class "autocomplete-active":*/
//         x[currentFocus].classList.add("autocomplete-active");
//       }
//       function removeActive(x) {
//         /*a function to remove the "active" class from all autocomplete items:*/
//         for (let i = 0; i < x.length; i++) {
//           x[i].classList.remove("autocomplete-active");
//         }
//       }
//       function closeAllLists(elmnt) {
//         /*close all autocomplete lists in the document,
//         except the one passed as an argument:*/
//         const x = document.getElementsByClassName("autocomplete-items");
//         for (let i = 0; i < x.length; i++) {
//           if (elmnt != x[i] && elmnt != inp) {
//           x[i].parentNode.removeChild(x[i]);
//         }
//       }
//     }
//   /*execute a function when someone clicks in the document:*/
//       document.addEventListener("click", function (e) {
//           closeAllLists(e.target);
//       });
// }

//   function checkInputData(){
//     const cityfrom = document.getElementById('cityfrom');
//     const cityto = document.getElementById('cityto');
//     const volume = document.getElementById('volume');
//     const weight = document.getElementById('weight');
//     const inputData = [cityfrom, cityto, volume, weight]
//     for(let i=0; i<inputData.length; i++){
//         if (!(inputData[i]).value){
//           const error = document.createElement('span')
//           error.className='error'
//           error.style.color = 'red'
//           inputData[i].style.borderColor = '#f71616'
//           inputData[i].style.boxShadow = '0 0 7px #d45252'
//           inputData[i].parentNode.insertBefore(error, inputData[i])
//         }
//     }
// }

// // function check(){
// // }

//   async function fetchData(url, method, data){
//       let responce = await fetch({
//         url:url,
//         method: method,
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//       });
//       return await responce
//     }

//     function insertPrice(price){
//         field = document.getElementById('standartCost')
//         field.innerHTML = price
//     }

//   function calc(){
//     const cityfrom = document.getElementById('cityfrom').value;
//     const cityto = document.getElementById('cityto').value;
//     const quantity = document.getElementById('quantity').value;
//     const weight = document.getElementById('weight').value;
//     const volume = document.getElementById('volume').value;
//     const delivery_from = document.getElementById('delivery_from').checked;
//     const delivery_to = document.getElementById('delivery_to').checked;

//     const standartCost = document.getElementById('standartCost');
//     const standartTerm = document.getElementById('standartTerm');
//     const expressCost = document.getElementById('expressCost');
//     const expressTerm = document.getElementById('expressTerm');

//     const struct = {
//       cityfrom: cityfrom,
//       cityto: cityto,
//       weight: weight,
//       volume: volume,
//       quantity: quantity,
//       delivery_from: delivery_from,
//       delivery_to: delivery_to
//     };

//     checkInputData()

//     function newF(data){
//         insertPrice(data['price']) 
//     }

//     if (cityto  && cityfrom  && weight && volume){

//         // $.ajax({
//         //       type: 'POST',
//         //       url: 'http://127.0.0.1:8000/api/post-calc',
//         //       contentType:"application/json",
//         //       data: JSON.stringify(struct),
//         //       success: (data) => {
//         //           res = JSON.parse(data)
//         //           newF(res)
//         //       }
//         // });   
        
//         var csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value'); 

//         async function postData(url, data) {
//           // Default options are marked with *
//           const response = await fetch(url, {
//             method: 'POST', // *GET, POST, PUT, DELETE, etc.
//             // mode: 'cors', // no-cors, *cors, same-origin
//             cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//             credentials: 'same-origin', // include, *same-origin, omit
//             headers: {
//               'Content-Type': 'application/json',
//               // 'Content-Type': 'application/x-www-form-urlencoded',
//             },
//             redirect: 'follow', // manual, *follow, error
//             referrerPolicy: 'no-referrer', // no-referrer, *client
//             body: JSON.stringify(data) // body data type must match "Content-Type" header
//           });
//           return await response.json(); // parses JSON response into native JavaScript objects
//         }
        
//         postData('http://127.0.0.1:8000/api/test', struct)
//           .then((data) => {
//             console.log(data); // JSON data parsed by `response.json()` call
//           });
//         // postData('http://127.0.0.1:8000/api/post-calc', struct)
//         //   .then((data) => {
//         //     console.log(data); // JSON data parsed by `response.json()` call
//         //   });



//        };
//     }