## Here are we going to train different different models
import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRFRegressor

from src.components.exception import CustomException
from src.components.logger import logging
from src.components.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig() #INside model_trainer_config we will get the path name
        
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Random Forest":RandomForestRegressor(),
                "Decision Trees":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K -neighbors Classifier": KNeighborsRegressor(),
                "XGBClassifier":XGBRFRegressor(),
                "Catboosting Classifier":CatBoostRegressor(verbose=False),
                #What is the purpose of verbose
                "Adaboost Classifier":AdaBoostRegressor()
            }
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            
            # To get the best model score from dict
            best_model_score=max(sorted(model_report.values()))
            
            #To get best models name from dict
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            predicted=best_model.predict(X_test)
            r2_score1=r2_score(y_test,predicted)
            return r2_score1
        except Exception as e:
            raise CustomException(e,sys)