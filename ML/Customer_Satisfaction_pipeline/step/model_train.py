# import logging
# import pandas as pd
# from zenml import step

# from source.model_dev import LinearRegresssionModel
# from sklearn.base import RegressorMixin
# from .config import ModelNameConfig

# @step
# def train_model(
#     X_train : pd.DataFrame,
#     X_test : pd.DataFrame,
#     y_train : pd.DataFrame,
#     y_test : pd.DataFrame,
#     config :ModelNameConfig,
# )-> RegressorMixin:
#     """
#     Trains the model on the ingested data

#     Args : 
#         df: the ingested data
#     """
#     try : 
#         model = None
#         if config.model_name == "LinearRegression":
#             model =LinearRegresssionModel()
#             trained_model = model.train(X_train=X_train, y_train=y_train)
#             return trained_model
#         # if config.model_name == "randommforest":
#         # ....

#         else:
#             raise ValueError("Model {} not supported ".format(config.model_name__))
#     except Exception as e:
#         logging.error("Error in training model {}".format(e))
#         raise e
    
import logging
import pandas as pd
from zenml import step
from source.model_dev import LinearRegresssionModel  # Import the Linear Regression Model
from sklearn.base import RegressorMixin

import mlflow
from zenml.client import Client


experiment_tracker = Client().active_stack.experiment_tracker




@step(experiment_tracker = experiment_tracker.name)
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
) -> RegressorMixin:
    """
    Trains the model on the ingested data

    Args:
        X_train: The training features.
        X_test: The test features.
        y_train: The training labels.
        y_test: The test labels.
    """
    try:
        # Here, directly initializing the Linear Regression model without config
        mlflow.sklearn.autolog()
        model = LinearRegresssionModel()
        trained_model = model.train(X_train=X_train, y_train=y_train)  # Train the model
        logging.info("Model training complete.")
        return trained_model
    except Exception as e:
        logging.error("Error in training model: {}".format(e))
        raise e
