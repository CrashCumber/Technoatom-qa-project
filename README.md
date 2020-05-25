# Тестирование приложения
## Сборка и запуск приложения

1. Для запуска приложения необходимо скачать образ приложения myapp.
2. Сборка сервисов `docker-compose build`. 
3. Первый запуск сервисов `docker-compose up`.

Приложение доступно на http://0.0.0.0:8082/login/.  

Пользователь по умолчанию:
 name: *valentina* pass: *valentina*   
 (для изменения пользователя по умолчанию править данные в файле __mysql-dump/startup_data.sql`__)

Для последующего запуска и остановки приложения:
 
* `docker-compose start`
* `docker-compose stop`

## Тестирование
#### Запуск тестов
* `pytest -m API` 
* `pytest -m UI`

(дополнительные марки тестов смотреть в pytest.ini)

#### Использование selenoid 
Для сборки и запуска необходимо 

1. скачать образ
 `aerokube/selenoid:1.10.0` (`latest`) 
2. cкачать образ `selenoid/vnc_chrome:80.0` (`latest`) (при скачивании версии отличной от 80.0 изменить название образа в конфиге __config/browsers.json__)
3. в скрипте run\_selenoid.sh меняем путь до директории с конфигом браузера (`pwd`) 

 __/Users/mac/Desktop__/project_qa/config/ =>  __{your path to dir}__/project_qa/config/
4. запустить скрипт `bash run_selenoid.sh` 

Для запуска тестов с использованием selenoid 

- `pytest --selenoid=True`

#### Отчет 
Для получения отчета в браузере необходимо. 

1. `brew install allure`
2. `pip install allure-pytest`
3. `pytest --alluredir=/tmp/my_allure_results`
4. `allure serve /tmp/my_allure_results`
Данные записываются в директорию /tmp/my_allure_results (если ее нет, то директория создается)


