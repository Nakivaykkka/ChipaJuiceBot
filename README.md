# ChipaJuiceBot
![Python application](https://github.com/Nakivaykkka/ChipaJuiceBot/actions/workflows/python-app.yml/badge.svg)
Python application(https://github.com/Nakivaykkka/ChipaJuiceBot/actions/workflows/python-app.yml/badge.svg)
Телеграм-бот для поиска и парсинга коллекционных подарков и лотов с сайта [fragment.com](https://fragment.com/).

---

## 📦 Описание

**ChipaJuiceBot** автоматически ищет и парсит новые коллекционные подарки (лоты) с сайта fragment.com и отправляет их пользователям в Телеграм.

---

## 🚦 Статус разработки

🚧 В процессе разработки.

---

## 📝 TODO

- [✅] Инициализация проекта и репозитория
- [✅] MVP: эхо-бот на aiogram
- [✅] Парсер сайта fragment.com (раздел с лотами)
- [✅] Выдача списка новых подарков по команде
- [✅] Dockerfile и docker-compose
- [✅] Тесты на парсер и основные команды
- [✅] Логирование ошибок
- [✅] Документация по API и командам
- [✅] CI/CD (github actions)

---

## 🚀 Быстрый старт
Репа:
git clone https://github.com/Nakivaykkka/ChipaJuiceBot.git

## Быстрый старт
1. Клонируй репу
2. Установи зависимости: `pip install -r requirements.txt`
3. Запусти файл: `python bot/main.py`
4. Пропиши TELEGRAM_TOKEN в .env


---

## 🛠️ Технологии

- Python 3.11+
- aiogram (асинхронный телеграм-бот)
- httpx / aiohttp (асинхронный парсинг)
- pytest (тестирование)
- docker (контейнеризация, позже)
- github actions (CI, позже)

---

## 📚 Как работает бот

1. Пользователь пишет `/start` — бот отвечает приветствием.
2. Пользователь пишет `/gifts` — бот парсит свежие лоты/подарки с fragment.com и присылает список.
3. (В будущем) бот может автоматически уведомлять о новых лотах/подарках.

---

## 🧩 Структура проекта
ChipaJuiceBot/
│
├── bot/ # логика телеграм-бота
├── parsers/ # парсеры сайтов
├── services/ # бизнес-логика, уведомления
├── tests/ # тесты
├── requirements.txt
├── .env.example # пример файла с переменными
├── Dockerfile # контейнеризация
├── docker-compose.yml
└── README.md


## API проекта

### Получить офферы по коллекции
- `get_gift_offers_parser(slug: str, top: int = 5) -> List[Dict]`
    - slug — "berrybox", "astralshard" и т.д.
    - Возвращает: список офферов вида {"price": float, "url": str}

### Пример ответа
```json
[
  {"price": 123.0, "url": "https://fragment.com/gift/astralshard-1868?filter=sale"},
  ...
]
```


Автор: [Nakivaykkka](https://github.com/Nakivaykkka/)

---

**P.S.** Проект делается для портфолио и реального боевого опыта.  
PR/идеи приветствуются!
