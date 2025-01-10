from src.DSProject.config.configuration import ConfigurationManager
from src.DSProject.components.data_validation import DataValidation
from src.DSProject import logger
from src.DSProject.components.model_trainer import ModelTrainer


STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()