// Страница в разработке
let text = document.querySelector('.loader__text p');
if (text){
    text.innerHTML = text.innerText.split("").map((char, i) => `<b style="transform:rotate(${i * 15}deg)">${char}</b>`).join("");   
}







// Модальные окна
const popupLinks = document.querySelectorAll('.popup-link');
const body = document.querySelector('body');
const lockPadding = document.querySelectorAll(".lock-padding");
let unlock = true;
const timeout = 800;

if (popupLinks.length > 0){
    for (let index = 0; index < popupLinks.length; index++){
        const popupLink = popupLinks[index];
        popupLink.addEventListener("click", function (e){
            const popupName = popupLink.getAttribute('href').replace('#', '');
            const curentPopup = document.getElementById(popupName);
            popupOpen(curentPopup);
            e.preventDefault();
        });
    }
}

const popupCloseIcon = document.querySelectorAll('.close__popup');
if (popupCloseIcon.length > 0) {
    for (let index = 0; index < popupCloseIcon.length; index++){
        const el = popupCloseIcon[index];
        el.addEventListener('click', function (e){
            popupClose(el.closest('.popup'));
            e.preventDefault();
        })
    }
}

function popupOpen(curentPopup){
    if (curentPopup && unlock){
        const popupActive = document.querySelector('.popup.open');
        if (popupActive){
            popupClose(popupActive, false);
        }else{
            bodyLock();
        }
        curentPopup.classList.add('open');
        curentPopup.addEventListener("click", function (e){
            if (!e.target.closest('.popup__content')){
                popupClose(e.target.closest('.popup'));
            }
        });
    }
}

function popupClose(popupActive, doUnlock = true){
    if (unlock){
        popupActive.classList.remove('open');
        if (doUnlock){
            bodyUnlock();
        }
    }
}

function bodyLock(){
    const lockPaddingValue = window.innerWidth - document.querySelector('.wrapper').offsetWidth + 'px';

    if (lockPadding.length > 0){
        for (let index = 0; index < lockPadding.length; index++){
            const el = lockPadding[index];
            el.style.paddingRight = lockPaddingValue;
        }
    }
    body.style.paddingRight = lockPaddingValue;
    body.classList.add('lock');

    unlock = false;
    setTimeout(function (){
        unlock = true;
    }, timeout);
}

function bodyUnlock(){
    setTimeout(function (){
        for (let index = 0; index <lockPadding.length; index++){
            const el = lockPadding[index];
            el.style.paddingRight = '0px';
        }
        body.style.paddingRight = '0px';
        body.classList.remove('lock');
    }, timeout);

    unlock = false;
    setTimeout(function (){
        unlock = true;
    }, timeout);
}

document.addEventListener('keydown', function(e){
    if (e.which === 27){
        const popupActive = document.querySelector('.popup.open');
        popupClose(popupActive);
    }
});



// часы
if(document.querySelector('#time')){
    setInterval(()=>{
        const time = document.querySelector('#time');
        let date = new Date();
        let hours = date.getHours()
        let minutes = date.getMinutes()
        let seconds = date.getSeconds()
        if (minutes<10){
            minutes = "0" + minutes;
        }
        if (seconds<10){
            seconds = "0" + seconds;
        }
        if (hours<10){
            hours = "0" + hours;
        }
        time.textContent = hours + ":" + minutes  + ":" + seconds;
    })
}



// Плавная прокрутка якорных ссылок
// выбираем все якорные ссылки на странице
const anchors = document.querySelectorAll('a[href*="#"]');

// добавляем обработчик событий на каждую якорную ссылку
for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault(); // отменяем стандартное поведение браузера при клике на ссылку
    const blockID = anchor.getAttribute('href').substr(1); // получаем id элемента, на который ссылается якорная ссылка
    const block = document.getElementById(blockID); // получаем целевой элемент
    const offset = 95; // задаем отступ для остановки прокрутки
    const top = block.getBoundingClientRect().top + window.pageYOffset - offset; // вычисляем позицию целевого элемента с учетом отступа
    window.scrollTo({
      top: top,
      behavior: 'smooth'
    }); // прокручиваем страницу к целевому элементу с учетом отступа
  });
}



// Распечатка телефонных номеров
function printContent() {
    window.print();
}
  