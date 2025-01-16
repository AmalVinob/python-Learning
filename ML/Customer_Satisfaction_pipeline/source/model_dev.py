import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression

class Model(ABC):
    """
    abstract class for all models
    """
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Train the model

        args :
            X_train : training data
            y_train : training label

        return : None
        """

        pass

class LinearRegresssionModel(Model):
    """
    linear regression model
    """
    def train(self, X_train , y_train, **kwargs):
        """
        Train the model

        args :
            X_train : training data
            y_train : training label

        return : None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)

            logging.info("Model training complete")
            return reg
        except Exception as e:
            logging.error(f"error while training the model {e}")
            raise e
        

# class Random forest(model)
#.....
    
