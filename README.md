## Stripe payment

### Описание проекта

Cервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров.

На сервере реализовано два эндпоинта:

GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe выполняется stripe.checkout.Session.create(...) и полученный session.id выдается в результате запроса.

GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходит редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id).


### Инструменты

- Django 5.0.2
- Stripe 8.4.0
- Postgres 16.1
- Docker 24.0.6
- Gunicorn 21.2.0


### Как запустить проект

- клонировать репозиторий

```
git@github.com:ApriCotBrain/stripe-payment.git
```

- в директории stripe_payment/ создать файл .env по примеру .env_sample

- если вы используете Windows, убедиться что файл run_app.sh в директории stripe_payment/ имеет формат конца строки LF

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d --build 
```

После сборки контейнеров проект доступен по адресу:

```
http://localhost/
```

В базе данных уже есть администратор. 

Логин для входа: admin, пароль: admin

Также есть два тестовых item.

### Без локального запуска посмотреть можно [здесь](http://olgamelikhova.pythonanywhere.com/item/1/)

### UPD

Добавлена страница заказа

Эндпоинты создания сессии изменены на /buy/item/{id}/ и /buy/order/{id}/ для item и order соответсвенно

Посмотреть здесь:

[item](http://olgamelikhova.pythonanywhere.com/item/1/)

[order](http://olgamelikhova.pythonanywhere.com/order/1/)
