import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

class Evaluation(ABC):
    """
    Abstract class defining strategy for evaluating the models
    """
    @abstractmethod
    def calc_score(self, y_true: np.ndarray, y_predi : np.ndarray):
        """
        calculate the score for the model

        Args :
            y_true : true labels (y_test)
            y_predi : predicted value by the model
        """
        pass

class MSE(Evaluation):
    """
    Evaluation stratergy that uses mean squared error
    """

    def calc_score(self, y_true : np.ndarray, y_predi : np.ndarray):
        try:
            logging.info("calculating mse")
            mse = root_mean_squared_error(y_true, y_predi)
            logging.info("MSE : {}".format(mse))
            return mse
        except Exception as e:
            logging.error("error in calculating the mse score : {e}".format(e))
            raise e

class R2_score(Evaluation):
    """
    Evaluation stratergy for rsquared
    """

    def calc_score(self, y_true : np.ndarray, y_predi : np.ndarray):
        try:
            logging.info("calclulating R2score")
            r2 = r2_score(y_true, y_predi)
            logging.info(f"r2score : {r2}")
            return r2
        except Exception as e:
            logging.error(f"error in calculating r2 score {e}")
            raise e
        


class RMSE(Evaluation):
    """
    Evaluation stratergy for Root mean squared error
    """

    def calc_score(self, y_true : np.ndarray, y_predi : np.ndarray):
        try:
            logging.info("calclulating RMSE ")
            rmse = mean_squared_error(y_true, y_predi)
            logging.info(f"r2score : {rmse}")
            return rmse
        except Exception as e:
            logging.error(f"error in calculating RMSE {e}")
            raise e