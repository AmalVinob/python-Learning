import logging
import pandas as pd
from zenml import step

from source.data_cleaning import DataCleaning, DataPreProcessingStrategy, DataSplitStrategy
from typing import Annotated
from typing import Tuple


@step
def clean_df(df: pd.DataFrame) ->Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    """
    Cleans the data and then divide it 

    Args:
        df : a raw data
    
    return : 
        X_train : training data, 
        X_test : testing data , 
        y_train : training labels, 
        y_test : testing labels
    """
    try:
        process_strategy = DataPreProcessingStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        process_Data = data_cleaning.handle_data()


        data_divide_strategy = DataSplitStrategy()
        data_divide = DataCleaning(process_Data, data_divide_strategy)
        X_train, X_test, y_train, y_test = data_divide.handle_data()
        logging.info("Data cleaning completed")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        logging.error(f"error while cleaning the data {e}")
        raise e
