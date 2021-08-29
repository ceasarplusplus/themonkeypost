"use strict"

console.log('hello word')
const postvideo = document.getElementById('postvideo')
const spinnerbox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBox = document.getElementById('end-box')


const vidphotos = [...document.getElementsByClassName('vidphoto')]
            // console.log(vidphoto.reverse())
            const vidphoto = vidphotos.reverse()
            vidphoto.forEach(item=>item.addEventListener('click', e=>{
               
                const videoId = e.target.parentElement.getAttribute('data-vid')
                console.log(videoId)
                iframe.innerHTML = `<iframe id="Geeks3" class="embed-responsive-item" controls=1 width="100%" height="315"
                src="https://www.youtube.com/embed/${videoId}" allowfullscreen></iframe>`
            }))
// const helloworldbox = document.getElementById

// let visible = 3


// $.ajax({
//     type: 'GET',
//     url: `/vid-json/${visible}`,
//     success: function (response) {
//         console.log('response', response)
//         const data = response.data
//         setTimeout(() => {
//             spinnerbox.classList.add('not-visible')
//             data.forEach(el => {
//                 postvideo.innerHTML += `
//             <div class="col-lg-6">
//                 <div class="card" style="width: 100%;">
//                     <div class="card-body my-vid" data-toggle="modal" data-target="#previewmodal" data-vid="${el.link}">
//                         <img class="vidphoto card-img-top" src="${el.image}" alt="${el.title}">
//                         <p class="card-text">${el.title}</p>
//                     </div>
//                 </div>
//             </div>   
            
//             `

//             });
//         }, 1000);

//         console.log(response.size)
//         if (response.size === 0) {
//             endBox.textContent = "Videos are not available at the moment... "
//         } else if (response.size <= visible) {
//             endBox.textContent = "No more videos to load... "
//         }
        
//     },
//     error: function (error) {
//         console.log('error', error)
//     }
// })

// const getData = () => {
//     $.ajax({
//         type: 'GET',
//         url: `/vid-json/${visible}`,
//         success: function (response) {
//             console.log('response', response)
//             const data = response.data
//             setTimeout(() => {
//                 spinnerbox.classList.add('not-visible')
//                 data.forEach(el => {
//                     postvideo.innerHTML += `
//                 <div class="col-lg-6">
//                     <div class="card" style="width: 100%;">
//                         <div class="card-body my-vid" data-toggle="modal" data-target="#previewmodal" data-vid="${el.link}">
//                             <img class="vidphoto card-img-top" src="${el.image}" alt="${el.title}">
//                             <p class="card-text">${el.title}</p>
//                         </div>
//                     </div>
//                 </div>   
                
//                 `

//                 });
//             }, 1000);

//             console.log(response.size)
//             if (response.size === 0) {
//                 endBox.textContent = "Videos are not available at the moment... "
//             } else if (response.size <= visible) {
//                 endBox.textContent = "No more videos to load... "
//             }
//             const vidphotos = [...document.getElementsByClassName('vidphoto')]
//             // console.log(vidphoto.reverse())
//             const vidphoto = vidphotos.reverse()
//             vidphoto.forEach(item => item.addEventListener('click', e => {

//                 const videoId = e.target.parentElement.getAttribute('data-vid')
//                 console.log(videoId)
//                 iframe.innerHTML = `<iframe id="Geeks3" class="embed-responsive-item" controls=1 width="100%" height="315"
//                 src="https://www.youtube.com/embed/${videoId}" allowfullscreen></iframe>`
//             }))
//         },
//         error: function (error) {
//             console.log('error', error)
//         }
//     })

// }


// loadBtn.addEventListener('click', () => {
//     spinnerbox.classList.remove('not-visible')
//     visible += 3
//     getData()
// })

// // getData()