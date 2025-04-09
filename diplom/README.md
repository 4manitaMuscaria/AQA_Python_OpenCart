## О проекте
Данный проект представляет собой набор автоматизированных тестов для платформы OpenCart. 
Тесты разделены на две категории:

- **UI-тесты** : 3 теста, проверяющие функциональность пользовательского интерфейса.
- **API-тесты** : 3 теста, включая CRUD-операции, проверяющие работу API.

Тесты написаны на Python с использованием современных инструментов и библиотек для обеспечения надежности и удобства поддержки.

## Структура проекта
Проект организован следующим образом:
```markdown
diplom/  
├── config/  
│   └── credentials.py          # Файл с конфигурацией (учетные данные, URL и т.д.)  
├── elements/                   # Веб-элементы для UI-тестов  
├── pages/                      # Классы страниц для Page Object Model  
├── locators/                   # Локаторы элементов UI  
├── models/                     # Модели Pydantic для валидации данных API  
├── src/                        # Вспомогательные модули  
│   └── test_data.py            # Генерация тестовых данных  
├── tests/  
│   ├── ui_tests/               # UI-тесты  
│   │   ├── conftest_ui.py      # Конфигурация фикстур для WebDriver  
│   │   ├── fixtures_ui.py      # Конфигурация фикстур setup и teardown для UI-тестов  
│   │   └── test_*.py           # Файлы с UI-тестами  
│   └── api_tests/              # API-тесты  
│       ├── conftest_api.py     # Конфигурация фикстур для API-тестов  
│       ├── fixtures_api.py     # Конфигурация фикстур setup и teardown для API-тестов  
│       └── test_*.py           # Файлы с API-тестами  
├── utils/  
│   └── logger.py               # Настройка логирования  
├── docker-compose.yml          # Docker Compose для развертывания OpenCart  
├── Dockerfile                  # Dockerfile для сборки образа с тестами  
├── pytest.ini                  # Конфигурация pytest  
├── poetry.lock                 # Замороженные зависимости  
└── pyproject.toml              # Конфигурация Poetry  
```
## Используемые библиотеки
Проект использует следующие библиотеки:

- pytest : Фреймворк для написания и запуска тестов.
- selenium : Для автоматизации браузера в UI-тестах.
- requests : Для выполнения HTTP-запросов в API-тестах.
- pydantic : Для валидации данных в API-тестах.
- faker : Для генерации тестовых данных.
- pyautogui : Для эмуляции действий пользователя (например, загрузка файлов).
- sqlalchemy : Для работы с базой данных (если требуется).
- pymysql : Для взаимодействия с MySQL.
- pylint : Для статического анализа кода.

## Инструкция по сборке и запуску
1. Развертывание OpenCart и сборка образа Docker с тестами  
Используйте скрипт для развертывания OpenCart:
```bash
python utils/docker_setup.py
```
Примечание 1: Убедитесь, что порты 8080 и 3306 свободны или измените их в docker-compose.yml.

2. Запуск Selenoid  
Для запуска Selenoid выполните следующие команды:
```bash
cm selenoid start --vnc
```
Так же, при необходимости запустите Selenoid-ui:
```bash
cm selenoid-ui start
```
Примечание: Убедитесь, что Docker и утилита **cm** установлены и работают на вашей системе, и команда выполняется из директории расположения **cm**. 

3. Установка зависимостей
Если вы хотите запустить тесты локально, установите зависимости с помощью Poetry:
```bash
poetry install
```

4. Запуск тестов  
#### Локальный запуск  
Локально запускайте тесты командой:
```bash
poetry run pytest tests/ --execution=local
```
Чтобы запустить только UI-тесты:
```bash
poetry run pytest tests/ui_tests/ --execution=local
```
Чтобы запускать только API-тесты:
```bash
poetry run pytest tests/api_tests/ 
```
#### Запуск из Docker

Запустите контейнер с тестами командой:
```bash
docker run --name test-run --network selenoid -v "$(pwd)/allure-result:/diplom/allure-result" -v "$(pwd)/logs:/diplom/logs" opencart-tests tests/api_tests/ --executor=selenoid --headless
```
Альтернативный вариант (с передачей текущего IP)
```bash
$$HOST_IP=$(python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0])")
```
```bash
docker run -e "HOST_IP=$HOST_IP" --name test-run --network selenoid -v "$(pwd)/allure-report:/diplom/allure-result" -v "$(pwd)/logs:/diplom/logs" opencart-tests tests/ --executor=selenoid --headless
```
Примечание: Использование --network selenoid необходимо для доступа к Selenoid. 

Для генерации отчета Allure выполните:
```bash
C:\Allure\bin\allure.bat generate ./allure-result -o ./allure-report --clean
```
где C:\Allure\bin\allure.bat путь до Allure, если он не установлен в системе  
или 
```bash
allure generate ./allure-result -o ./allure-report --clean
```
если Allure установлен в окружении

5. Логирование  
Все логи тестов сохраняются в директорию logs/. Вы можете настроить формат и уровень логирования в utils/logger.py.

## Дополнительная информация
- Генерация тестовых данных : Все тестовые данные генерируются динамически с помощью модуля src/test_data.py.
- Конфигурация : Учетные данные и URL для тестов находятся в config/credentials.py.
- Локальные настройки : Если вы хотите изменить конфигурацию pytest, отредактируйте файл pytest.ini.