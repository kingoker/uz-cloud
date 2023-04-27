// Удаление файла или папки
// Получаем все элементы с классом delete__btn
const deleteButtons = document.querySelectorAll('.folder__delete');

// Обрабатываем клик по каждой кнопке удаления
deleteButtons.forEach(button => {
button.addEventListener('click', (event) => {
event.preventDefault(); // Отменяем переход по ссылке
const elementId = event.currentTarget.dataset.id; // Получаем ID элемента из атрибута data-id
const elementType = event.currentTarget.dataset.type; // Получаем тип элемента из атрибута data-type
deleteElement(elementId, elementType); // Отправляем AJAX-запрос на удаление элемента
});
});

// Функция для отправки AJAX-запроса на удаление файла или папки
function deleteElement(elementId, elementType) {
const xhr = new XMLHttpRequest();
xhr.open('POST', '/delete-element/', true);
xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // Устанавливаем заголовок с токеном CSRF
xhr.onreadystatechange = function() {
if (xhr.readyState === 4 && xhr.status === 200) {
console.log('Элемент успешно удален!');
location.reload();
}
};
const data = new FormData();
data.append('element_id', elementId);
data.append('element_type', elementType); // Добавляем тип элемента в FormData
xhr.send(data);
}

// Функция для получения значения токена CSRF из cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}