import logging
import pandas as pd
from zenml import step

class IngestData:
    """
    ingesting the data from the datapath
    """
    
    def __init__(self, data_path : str):
        """
        Args :
            data_path :path to the data
        """
        self.data_path = data_path
    
    def get_data(self):
        """
        ingesting the data from the datapath
        """

        logging.info(f"ingest data from {self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingest_df(data_path: str)-> pd.DataFrame:
    """
    Ingesting the data from the datapath

    Args:
        datapath : Path to the data
    returns:
        pd.DataFrame : returns the ingested data
    
    """

    try:
        ingest_Data = IngestData(data_path)
        df = ingest_Data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data : {e}")
        raise e
