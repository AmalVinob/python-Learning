# import pandas as pd
# import numpy as np
# from zenml import pipeline, step
# from zenml.config import DockerSettings
# from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT

# # from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
# #     MLFlowModelDeveloper,
# # )

# from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
#     MLFlowModelDeployer,
# )

# from zenml.integrations.constants import MLFLOW
# from zenml.integrations.mlflow.services import MLFlowDeploymentService
# from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
# # from zenml.steps import BaseParameters, Output
# from zenml.config.base_settings import BaseSettings





# # from materializer.custom_materializer import cs_materializer

# from step.cleaning import clean_df
# from step.evaluation import evaluation
# from step.ingest_data import ingest_df
# from step.model_train import train_model



# docker_settings = DockerSettings(required_integrations = [MLFLOW])


# # class DeploymentTriggerConfig(BaseSettings):
# #     """deploy trigger config"""
# #     min_accuracy = 0.92

# # from pydantic_settings import BaseSettings

# # class DeploymentTriggerConfig(BaseSettings):
# #     """deploy trigger config"""
# #     min_accuracy: float = 0.92  # Add type annotation here



# # @step
# # def deployement_trigger(
# #     accuracy : float,
# #     config : DeploymentTriggerConfig
# # ):
# #     """ implement a simple model deployment trigger that looks at the inpuut model accuracy and decides if it is good enough to deployment"""
# #     accuracy >= 0.92
# #     return accuracy >= config.min_accuracy



# from typing import Any

# @step
# def deployement_trigger(
#     accuracy: float,
#     min_accuracy: float = 0.92  # Set a default value for min_accuracy
# ):
#     """Implement a simple model deployment trigger that looks at the input model accuracy
#     and decides if it is good enough for deployment."""
#     return accuracy >= min_accuracy




# #contionus deployment pipeline
# @pipeline(enable_cache= False, settings = {"docker" : docker_settings})
# def contious_deployment_pipeline(
#     data_path:str,
#     workers : int = 1,
#     timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
# ):
#     df = ingest_df(data_path=data_path)
#     X_train, X_test, y_train, y_test = clean_df(df)
#     model = train_model(X_train, X_test, y_train, y_test)
#     r2_score , rmse = evaluation(model, X_test, y_test)

#     deployement_decision = deployement_trigger(r2_score)

#     mlflow_model_deployer_step(
#         model = model,
#         deploy_decision = deployement_decision,
#         workers = workers,
#         timeout = timeout
#     )


import pandas as pd
import numpy as np
from zenml import pipeline, step
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT

from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from zenml.integrations.constants import MLFLOW
from zenml.config.base_settings import BaseSettings
from typing import Any

# Docker settings for integration
docker_settings = DockerSettings(required_integrations=[MLFLOW])

# Simple model deployment trigger
@step
def deployment_trigger(accuracy: float, min_accuracy: float = 0.92):
    """Implement a simple model deployment trigger that looks at the input model accuracy
    and decides if it is good enough for deployment."""
    return accuracy >= min_accuracy

# Continuous deployment pipeline
@pipeline(enable_cache=False, settings={"docker": docker_settings})
def continuous_deployment_pipeline(
    data_path: str,
    workers: int = 1,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    df = ingest_df(data_path=data_path)
    X_train, X_test, y_train, y_test = clean_df(df)
    model = train_model(X_train, X_test, y_train, y_test)
    r2_score, rmse = evaluation(model, X_test, y_test)

    deployment_decision = deployment_trigger(r2_score)

    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deployment_decision,
        workers=workers,
        timeout=timeout,
    )
