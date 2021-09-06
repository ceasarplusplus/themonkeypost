"use strict"

// console.log('hello word')
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
                src="https://www.youtube.com/embed/${videoId}" allowfullscreen ></iframe>`
            }))


// "use strict"
// console.log('hello world')
// const postvideo = document.getElementById('postvideo')
// const iframe = document.getElementById('iframe')
// const url = window.location.host
// const spinnerbox = document.getElementById('spinner-box')
// const loadBtn = document.getElementById('load-btn')
// const endBox = document.getElementById('end-box')

// let visible = 3

// console.log(url)
// $.ajax({
//     type: 'GET',
//     url: `/vid-json/${visible}`,
//     success: function (response) {
//         console.log(response.data)
//         const data = response.data
//         const datas = data.reverse()
//         datas.forEach(el => {
//             // console.log(el.fields)
//             postvideo.innerHTML += `
//             <div class="col-lg-6">
//                 <div class="card" style="width: 100%;">
//                     <div class="card-body my-vid" data-toggle="modal" data-target="#previewmodal" data-vid="${el.link}">
//                         <img class="vidphoto" src="${el.image}" alt="${el.title}">
//                         <p class="card-text">${el.title}</p>
//                     </div>
//                 </div>
//             </div>           
//             `
//         });
//         const vidphotos = [...document.getElementsByClassName('vidphoto')]
//         // console.log(vidphoto.reverse())
//         const vidphoto = vidphotos.reverse()
//         vidphoto.forEach(item=>item.addEventListener('click', e=>{
           
//             const videoId = e.target.parentElement.getAttribute('data-vid')
//             console.log(videoId)
//             iframe.innerHTML = `<iframe id="Geeks3" class="embed-responsive-item" controls=1 width="100%" height="315"
//             src="https://www.youtube.com/embed/${videoId}" allowfullscreen></iframe>`
//         }))
//         console.log(response.size)
//             if (response.size === 0) {
//                 endBox.textContent = "Videos are not available at the moment... "
//             } else if (response.size <= visible) {
//                 endBox.textContent = "No more videos to load... "
//             }
//     },
//     error: function (error) {
//         console.log(error)
//     }
// })


// const getData = () => {
//     $.ajax({
//         type: 'GET',
//         url: `/vid-json/${visible}`,
//         success: function (response) {
//             console.log(response.data)
//             const data = response.data
//             // console.log(data)
//             data.forEach(el => {
//                 console.log('images', el.image)
//                 postvideo.innerHTML += `
//                 <div class="col-lg-6">
//                     <div class="card" style="width: 100%;">
//                         <div class="card-body my-vid" data-toggle="modal" data-target="#previewmodal" data-vid="${el.link}">
//                             <img class="vidphoto" src="${el.image}" alt="${el.title}">
//                             <p class="card-text">${el.title}</p>
//                         </div>
//                     </div>
//                 </div>           
//                 `
//             });
//             const vidphotos = [...document.getElementsByClassName('vidphoto')]
//             // console.log(vidphoto.reverse())
//             const vidphoto = vidphotos.reverse()
//             vidphoto.forEach(item=>item.addEventListener('click', e=>{
               
//                 const videoId = e.target.parentElement.getAttribute('data-vid')
//                 console.log(videoId)
//                 iframe.innerHTML = `<iframe id="Geeks3" class="embed-responsive-item" controls=1 width="100%" height="315"
//                 src="https://www.youtube.com/embed/${videoId}" allowfullscreen></iframe>`
//             }))
//             console.log(response.size)
//                 if (response.size === 0) {
//                     endBox.textContent = "Videos are not available at the moment... "
//                 } else if (response.size <= visible) {
//                     endBox.textContent = "No more videos to load... "
//                 }
//         },
//         error: function (error) {
//             console.log(error)
//         }
//     })
// }




// loadBtn.addEventListener('click', () => {
//     spinnerbox.classList.remove('not-visible')
//     visible += 3
//     getData()
// })






// {/* <a class="vid" id="${el.fields.link}"  data-toggle="modal" data-target="#previewmodal" data-vid=${el.fields.link}   href="" class="posts__link-wrapper mp_iframe">
//                         <figure class="posts__thumb "><img src="/media/${el.fields.image}"
//                                 alt="${el.fields.title}"></figure>
//                         <div class="posts__inner">
//                             <div class="posts__cat"><span class="label posts__cat-label">${el.fields.category}</span>
//                             </div>
//                             <h3 class="posts__title">${el.fields.title}</h3>
//                         </div>
//                 </a>
            
            

//   <figure class="posts__thumb posts__link-wrapper"><img src="/media/${el.fields.image}"
//                                 alt="${el.fields.title}"></figure>
//                         <div class="posts__inner">
//                             <div class="posts__cat"><span class="label posts__cat-label">${el.fields.category}</span>
//                             </div>
//                             <h3 class="posts__title">${el.fields.title}</h3>
//                         </div>
                


            
//             */}







// // const handleGetData = () => {
// //     $.ajax({
// //         type: 'GET',
// //         url: `/blogjs/${visible}/`,
// //         success: function (response) {
// //             // console.log(response.data)

// //             max_size = response.max
// //             const data = response.data
// //             spinnerBox.classList.remove('not-visible')
// //             setTimeout(() => {
// //                 spinnerBox.classList.add('not-visible')
// //                 data.map(post => {
// //                     // console.log(post.image.url)
// //                     blogBox.innerHTML += `<div class="posts__item posts__item--card posts__item--category-1 card">
// //                     <figure class="posts__thumb">
// //                         <div class="posts__cat"><span class="label posts__cat-label">${post.category}</span>
// //                         </div><a href="#"><img src="${post.image.url}" alt=""></a>
// //                     </figure>
// //                     <div class="posts__inner card__content"><a href="#" class="posts__cta"></a> <time
// //                             datetime="2016-08-23" class="posts__date">${post.date}</time>
// //                         <h6 class="posts__title"><a href="#">${post.title}</a></h6>
// //                         <div class="posts__excerpt">${post.detail}</div>
// //                     </div>

// //                 </div>`

// //                 })
// //                 if (max_size) {
// //                     console.log('Done')
// //                     loadBox.innerHTML = "<p>no more posts</p>"
// //                 }

// //             }, 1000)



// //         },
// //         error: function (error) {
// //             console.log(error)
// //         }

// //     })
// // }

// // handleGetData()

// // loadBtn.addEventListener('click', () => {
// //     visible += 2
// //     handleGetData()
// // })

// // ==============================================================