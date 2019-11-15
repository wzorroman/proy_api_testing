# proy_api_testing

## Tutorial 01
- URL => https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html

https://github.com/hendisantika/django-rest-api-jwt

   > token admin => 992e59bb662cf7011a9afd93bdabbb9d8c948ced

## Antes de autentificar -
- **(env_activado)$** http://127.0.0.1:8000/hello/?format=json

## Instalando  - `rest_framework.authtoken`
- **(env_activado)$** http http://127.0.0.1:8000/api/hello/ 'Authorization: Token 992e59bb662cf7011a9afd93bdabbb9d8c948ced'
- Resultado:
    ```
    HTTP/1.1 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Length: 27
    Content-Type: application/json
    Date: Fri, 15 Nov 2019 22:43:13 GMT
    Server: WSGIServer/0.2 CPython/3.6.8
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    {
        "message": "Hello, World!"
    }
    ```


- **(env_activado)$** curl http://127.0.0.1:8000/api/hello/ -H 'Authorization: Token 992e59bb662cf7011a9afd93bdabbb9d8c948ced'
- Resultado:
    ```
    {"message":"Hello, World!"}
    ```

- **(env_activado)$** http http://127.0.0.1:8000/api-token-auth/
- **(env_activado)$** http post http://127.0.0.1:8000/api-token-auth/ username=admin password=admin1234
- Resultado:
    ```
    HTTP/1.1 200 OK
    Allow: POST, OPTIONS
    Content-Length: 52
    Content-Type: application/json
    Date: Fri, 15 Nov 2019 22:55:40 GMT
    Server: WSGIServer/0.2 CPython/3.6.8
    X-Frame-Options: SAMEORIGIN

    {
        "token": "992e59bb662cf7011a9afd93bdabbb9d8c948ced"
    }
    ```

## Tutorial 02
- URL => https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb 
- GIT => https://github.com/ShubhamBansal1997/token-authentication-django
- **(env_activado)$** http post http://127.0.0.1:8000/api/login username=admin password=admin1234
- Resultado :
    ```
    HTTP/1.1 200 OK
    Allow: OPTIONS, POST
    Content-Length: 52
    Content-Type: application/json
    Date: Fri, 15 Nov 2019 22:41:11 GMT
    Server: WSGIServer/0.2 CPython/3.6.8
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    {
        "token": "992e59bb662cf7011a9afd93bdabbb9d8c948ced"
    }
    ```
- Para crear un nuevo token al usuario creado recientemente desde del comando *createsuperuser* :
- **(env_activado)$** http post http://127.0.0.1:8000/api/login username=admin2 password=admin1234
- Resultado:
    ```
    HTTP/1.1 200 OK
    Allow: POST, OPTIONS
    Content-Length: 52
    Content-Type: application/json
    Date: Fri, 15 Nov 2019 23:16:10 GMT
    Server: WSGIServer/0.2 CPython/3.6.8
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    {
        "token": "64a2fb6dacee25d27567b274d051c7ca1130752b"
    }
    ```
