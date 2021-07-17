"use strict"
console.log('hello world')
const blogBox = document.getElementById('blog-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 2


const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/blogjs/${visible}/`,
        success: function (response) {
            // console.log(response.data)

            max_size = response.max
            const data = response.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(() => {
                spinnerBox.classList.add('not-visible')
                data.map(post => {
                    // console.log(post.image.url)
                    blogBox.innerHTML += `<div class="posts__item posts__item--card posts__item--category-1 card">
                    <figure class="posts__thumb">
                        <div class="posts__cat"><span class="label posts__cat-label">${post.category}</span>
                        </div><a href="#"><img src="${post.image.url}" alt=""></a>
                    </figure>
                    <div class="posts__inner card__content"><a href="#" class="posts__cta"></a> <time
                            datetime="2016-08-23" class="posts__date">${post.date}</time>
                        <h6 class="posts__title"><a href="#">${post.title}</a></h6>
                        <div class="posts__excerpt">${post.detail}</div>
                    </div>

                </div>`

                })
                if (max_size) {
                    console.log('Done')
                    loadBox.innerHTML = "<p>no more posts</p>"
                }

            }, 1000)



        },
        error: function (error) {
            console.log(error)
        }

    })
}

handleGetData()

loadBtn.addEventListener('click', () => {
    visible += 2
    handleGetData()
})

// ==============================================================

// $.ajax({
//     type: 'GET',
//     url: '/blog_js/',
//     success: function (response) {
//         console.log(response.data)
//         const data = JSON.parse(response.data)
//         console.log(data)
//         data.forEach(rs => {
//             blogBox.innerHTML += `${rs.fields.detail}`
//         });
//     },
//     error: function (error) {
//         console.log(error)
//     }
// })