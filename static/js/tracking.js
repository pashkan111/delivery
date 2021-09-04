// window.onload = function(e){

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

function test(){
  console.log('start')
}

  function toSend(){
    //   e.preventDefault()
    const btn = document.getElementById('btn');

    const struct = {
      trak: btn.value
    };


    function newF(data){
        insertPrice(data['price']) 
    }

    if (cityto  && cityfrom  && weight && volume){

        // $.ajax({
        //       type: 'POST',
        //       url: 'http://127.0.0.1:8000/api/post-calc',
        //       contentType:"application/json",
        //       data: JSON.stringify(struct),
        //       success: (data) => {
        //           res = JSON.parse(data)
        //           newF(res)
        //       }
        // });   
        
        
        async function postData(url, data) {
          // Default options are marked with *
          const response = await fetch(url, {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            // mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
              'Content-Type': 'application/json'
              // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            redirect: 'follow', // manual, *follow, error
            referrerPolicy: 'no-referrer', // no-referrer, *client
            body: JSON.stringify(data) // body data type must match "Content-Type" header
          });
          return await response.json(); // parses JSON response into native JavaScript objects
        }
        
        postData('http://127.0.0.1:8000/api/post-calc', struct)
          .then((data) => {
            console.log(data); // JSON data parsed by `response.json()` call
          });



       };
    }