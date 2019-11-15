# proy_api_testing


token admin => 992e59bb662cf7011a9afd93bdabbb9d8c948ced

## Antes de autentificar -
(env_activado)$ http://127.0.0.1:8000/hello/?format=json

## Instalando  - 'rest_framework.authtoken'
(env_activado)$ http http://127.0.0.1:8000/api/hello/ 'Authorization: Token 992e59bb662cf7011a9afd93bdabbb9d8c948ced'
(env_activado)$ curl http://127.0.0.1:8000/api/hello/ -H 'Authorization: Token 992e59bb662cf7011a9afd93bdabbb9d8c948ced'


(env_activado)$ http http://127.0.0.1:8000/api-token-auth/
(env_activado)$ http post http://127.0.0.1:8000/api-token-auth/ username=admin password=admin1234

