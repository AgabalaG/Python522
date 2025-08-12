// Создаем div
document.write("<div id='demonstration'></div>");

// Получаем элемент по id
var div = document.getElementById('demonstration');

// Задаем текстовое содержимое
div.innerHTML = "Ваше текстовое содержимое";

// Применяем стили (пример для ul, но нужно применить к div)
// ul.style.listStyleType = 'square';
// ul.style.width = '50%';

// Применяем класс
div.className = 'Ваше имя класса';

