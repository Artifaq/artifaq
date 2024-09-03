from pydantic import BaseModel

class APPConfig(BaseModel):
    externals_apps: list = []
    mode: str = 'development'
    debug: bool = True
    logs_dir: str = 'logs'
    logs_enabled: bool = True
    logs_level: str = 'DEBUG'
    logs_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logs_file: str = 'app.log'