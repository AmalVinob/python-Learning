from zenml import pipeline
from step.ingest_data import ingest_df
from step.cleaning import clean_df
from step.model_train import train_model
from step.evaluation import evaluation


@pipeline(enable_cache = True)
def train_pipeline(data_path : str):
    df = ingest_df(data_path)
    X_train, X_test, y_train, y_test = clean_df(df)
    model = train_model(X_train, X_test, y_train, y_test)
    r2_score , rmse = evaluation(model, X_test, y_test)


