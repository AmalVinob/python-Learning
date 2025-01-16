# from zenml.steps import BaseParameters


# class ModelNameConfig(BaseParameters):
#     """model Config"""

#     model_name : str = "LinearRegression" 


from pydantic import BaseModel

class ModelNameConfig(BaseModel):
    model_name: str = "LinearRegression"
