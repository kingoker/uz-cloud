// Удаление папки
// Получаем все элементы с классом folder__delete
const deleteButtons = document.querySelectorAll('.folder__delete');

// Обрабатываем клик по каждой кнопке удаления
deleteButtons.forEach(button => {
  button.addEventListener('click', (event) => {
    event.preventDefault(); // Отменяем переход по ссылке
    const folderId = event.currentTarget.dataset.id; // Получаем ID папки из атрибута data-id
    deleteFolder(folderId); // Отправляем AJAX-запрос на удаление папки
  });
});

// Функция для отправки AJAX-запроса на удаление папки
function deleteFolder(folderId) {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/delete-folder/', true);
  xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // Устанавливаем заголовок с токеном CSRF
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      console.log('Папка успешно удалена!');
      location.reload();
    }
  };
  const data = new FormData();
  data.append('folder_id', folderId);
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
