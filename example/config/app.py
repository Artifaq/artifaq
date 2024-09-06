from artifaq.configs.app_config import AppConfig

config = AppConfig(
    apps=[
        'test',
        'home',
    ],
    mode='development',
    debug=True,
    logs_dir='logs',
    logs_enabled=True,
    logs_level='DEBUG',
    logs_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    log_file='app.log',
)