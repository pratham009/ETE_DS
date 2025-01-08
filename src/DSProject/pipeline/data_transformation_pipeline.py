from src.DSProject.config.configuration import ConfigurationManager
from src.DSProject.components.data_transformation import DataTransformation
from src.DSProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                config = ConfigurationManager()
                data_tranformation_config = config.get_data_transformation()
                data_tranformation = DataTransformation(config=data_tranformation_config)
                data_tranformation.train_test_splitting()
            else:
                raise Exception("Your schema is not valid")
        except Exception as e:
            print(e)

