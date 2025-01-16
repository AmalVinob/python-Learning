import logging
import pandas as pd
from zenml import step

from source.evaluation_model import MSE, R2_score, RMSE
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated

import mlflow
from zenml.client import Client


experiment_tracker = Client().active_stack.experiment_tracker


@step(experiment_tracker = experiment_tracker.name)
def evaluation(model: RegressorMixin, 
               X_test: pd.DataFrame,
               y_test: pd.DataFrame) -> Tuple[
                   Annotated[float , "r2_score"],
                   Annotated[float , "rmse"]
                   ]:
    """
    Evaluates the model on the ingested data
    Args :
        df : the ingested data
    """
    try: 
        prediction = model.predict(X_test)

        mse_class = MSE()
        mse = mse_class.calc_score(y_test, prediction)
        mlflow.log_metric("mse", mse)

        r2_score_class = R2_score()
        r2_score = r2_score_class.calc_score(y_test, prediction)
        mlflow.log_metric("r2score", r2_score)

        
        rmse_class = RMSE()
        rmse = rmse_class.calc_score(y_test, prediction)
        mlflow.log_metric("rmse", rmse)

        return r2_score, rmse
    except Exception as e:
        logging.error(f"error in evaluating the model : {e}")
        raise e

