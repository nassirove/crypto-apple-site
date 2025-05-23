// Переключение языка
function changeLanguage(lang) {
  localStorage.setItem('language', lang);
  document.getElementById('current-flag').textContent = flagMap[lang];
  applyLanguage();
  toggleLangMenu();
  
  // Анимация
  document.body.style.opacity = 0;
  setTimeout(() => document.body.style.opacity = 1, 300);
}

// Применение языка
function applyLanguage() {
  const lang = localStorage.getItem('language') || 'ru';
  document.querySelectorAll('[data-lang]').forEach(el => {
    const key = el.getAttribute('data-lang');
    el.textContent = translations[lang][key];
  });
}

// Меню языков
function toggleLangMenu() {
  const menu = document.getElementById('langMenu');
  menu.classList.toggle('show');
}

// Автоопределение языка
function detectBrowserLanguage() {
  const userLang = navigator.language.substring(0, 2);
  return ['uz', 'ru', 'en'].includes(userLang) ? userLang : 'ru';
}

// Инициализация
document.addEventListener('DOMContentLoaded', () => {
  const lang = localStorage.getItem('language') || detectBrowserLanguage();
  changeLanguage(lang);
  
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.lang-switcher')) {
      document.getElementById('langMenu').classList.remove('show');
    }
  });
});