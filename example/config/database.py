from artifaq.config.register_config import register_config

register_config('database' ,{
    'driver': 'postgresql',

    'host': 'localhost',
    'port': 27017,
    'username': 'root',
    'password': 'password',

    'database': 'artifaq',

    'collection': 'artifaq',
})