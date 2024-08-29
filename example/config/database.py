from artifaq.config.register_config import register_config

register_config('database' ,{
    'driver': 'mongodb',

    'host': 'localhost',
    'port': 27017,
    'username': 'root',
    'password': 'password',

    'database': 'artifaq',

    'collection': 'artifaq',
})