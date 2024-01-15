from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
        config_manager = ConfigurationManager()
        evaluation_config = config_manager.get_evaluation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f"******************")
        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e