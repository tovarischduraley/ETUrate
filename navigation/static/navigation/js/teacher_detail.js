const sliders = document.getElementsByClassName('review__slider')
const values = document.getElementsByClassName('value')
for (i = 0; i < sliders.length; i++) {
    sliders[i].setAttribute('oninput', `setValue(${i})`)
}

function setValue(i) {
    values[i].innerHTML = sliders[i].value
}