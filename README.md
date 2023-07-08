# dockerizedBE

RUN backend with SSL:
`gunicorn --certfile=certs/server.crt --keyfile=certs/server.key mt_backend.wsgi:application`
