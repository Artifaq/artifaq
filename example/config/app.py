from artifaq.config.register_config import register_config

register_config('app' ,{
    'mode': 'development',
    'debug': True,
    'port': 5000,
    'logs.dir': 'logs',
    'logs.enabled': True,
    'logs.level': 'DEBUG',
    'logs.format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'logs.file': 'app.log',
})