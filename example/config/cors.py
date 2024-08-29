from artifaq.config.register_config import register_config

register_config('cors' ,{
    'origins': ['*'],
    'methods': ['GET', 'POST', 'PUT', 'DELETE'],
    'headers': ['Content-Type'],
    'expose_headers': ['Content-Type'],
    'credentials': True,
})