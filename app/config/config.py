from app.config.development import DevelopmentConfig
from app.config.staging import StagingConfig
from app.config.production import ProductionConfig


class Config:
    def __init__(self):
        self.development_config = DevelopmentConfig()
        self.staging_config = StagingConfig()
        self.production_config = ProductionConfig()
