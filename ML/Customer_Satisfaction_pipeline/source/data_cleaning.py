import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataStrategy(ABC):
    """
    Abstract class defining handiling statergy
    """

    @abstractmethod
    def handle_data(self, data:pd.DataFrame)->Union[pd.DataFrame, pd.Series]:
        pass

class DataPreProcessingStrategy(DataStrategy):
    """
    Strategy for preprocessing data
    """
    def handle_data(self, data: pd.DataFrame)-> pd.DataFrame:
        """
        preprocess data
        """
        try:
            """
            Drop unwanted columns
            """
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp"
                ],
                axis= 1)
            
            """
            Filling null values, stratergy :median
            """
            data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            data["review_comment_message"].fillna("No Review", inplace=True)


            data = data.select_dtypes(include=[np.number])

            cols_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(cols_to_drop, axis=1)

            data = data.dropna()
            print(data.isna().sum())
            logging.info(f"sum null : {data.isna().sum()}")

            return data
        except Exception as e:
            logging.error(f"error in processing data {e}")
            raise e



class DataSplitStrategy(DataStrategy):
    """
    strategy for divinding the data innto train and test
    """
    def handle_data(self, data: pd.DataFrame)-> Union[pd.DataFrame, pd.Series]:
        """
        Divide the data
        """
        try:
            X = data.drop(["review_score"], axis=1)
            y = data["review_score"]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            X_train = X_train.dropna()
            y_train = y_train[X_train.index]

            
            
            return X_train, X_test, y_train, y_test
        
        except Exception as e:
            logging.error(f"Error dividing the data : {e}")
            raise e
    

class DataCleaning:
    """
    class for cleaning the data : which preprocess the data and then divide the data into train and test
    """
    def __init__(self, data: pd.DataFrame, strategy : DataStrategy):
        self.data = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """
        Handle data
        """

        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error in handling data {}".format(e))
            raise e


# we use it like this
# if __name__ == "__main__":
#     data = pd.read_csv("C:\\Users\\amalv\\OneDrive\\Desktop\\todo project\\datasets\\Customer satisfaction\\data\\archive\\Customer_data.csv")
#     data_cleaning = DataCleaning(data, DataPreProcessingStrategy())
#     data_cleaning.handle_data()
