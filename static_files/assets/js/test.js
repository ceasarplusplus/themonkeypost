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


$.ajax({
    type: 'GET',
    url: `/highlight-json/`,
    success: function (response) {
        console.log('response', response)
        const data = response.data
        console.log(data)
        data.forEach(el => {
            // console.log('images', el.image)
            postvideo.innerHTML += `
            <aside class="widget widget--sidebar card widget-preview">
							<div class="widget__title card__header">
								<h4>${el.title}</h4>
							</div>
							
							<div class="widget__content card__content">
								<!-- Match Preview -->
								<div class="match-preview">
									<section class="match-preview__body">
										<header class="match-preview__header">
											<div class="mb-1" data-toggle="modal" data-target="#previewmodal" data-vid="${data.indexOf(el)}">
												<img class="vidphoto" src="${el.thumbnail}" alt="">
											</div>
											<h3 class="match-preview__title">${el.competition}</h3><time
												class="match-preview__date" datetime="2017-05-17">${el.date}</time>
										</header>
										</header>
										
										<!-- <div class="match-preview__action"><a href="#"
												class="btn btn-default btn-block">Buy Tickets Now</a></div> -->
									</section>
									<!-- <section class="match-preview__countdown countdown">
										<h4 class="countdown__title">Game Countdown</h4>
										<div class="countdown__content">
											<div class="countdown-counter" data-date="June 18, 2021 21:00:00"></div>
										</div>
									</section> -->
								</div><!-- Match Preview / End -->
							</div>
						</aside>          
            `
        });
        const vidphotos = [...document.getElementsByClassName('vidphoto')]
            // console.log(vidphoto.reverse())
            const vidphoto = vidphotos.reverse()
            vidphoto.forEach(item=>item.addEventListener('click', e=>{
               
                const videoId = e.target.parentElement.getAttribute('data-vid')
                console.log(videoId)
                const modal = data[videoId]
                console.log(modal)
                iframe.innerHTML = modal.embed
            }))
       
        
    },
    error: function (error) {
        console.log('error', error)
    }
})

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


