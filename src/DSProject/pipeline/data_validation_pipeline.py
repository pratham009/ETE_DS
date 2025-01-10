from src.DSProject.config.configuration import ConfigurationManager
from src.DSProject.components.data_validation import DataValidation
from src.DSProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

