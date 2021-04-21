const lectureChoice = document.querySelector('#lecture__review__choice')
const practiceChoice = document.querySelector('#practice__review__choice')

const lectureList = document.querySelectorAll("#lecture__column input.lecture__review__option")
const practiceList = document.querySelectorAll("#practice__column input.practice__review__option")

lectureChoice.addEventListener('change', function (e) {
    if (lectureChoice.checked) {
        for (i = 0; i < lectureList.length; i++) {
            void (lectureList.item(i).disabled = true)
        }
    } else {
        for (i = 0; i < lectureList.length; i++) {
            void (lectureList.item(i).disabled = false)
        }
    }

})

practiceChoice.addEventListener('change', function (e) {
    if (lectureChoice.checked){
        lectureChoice.change = true
    }
    if (practiceChoice.checked) {
        for (i = 0; i < practiceList.length; i++) {
            void (practiceList.item(i).disabled = true)
        }
    } else {
        for (i = 0; i < practiceList.length; i++) {
            void (practiceList.item(i).disabled = false)
        }
    }

})

const form = document.getElementById("review__form")