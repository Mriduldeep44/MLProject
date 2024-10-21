import os
import pandas as pd
import sys
import numpy as np
from src.components.exception import CustomException
import dill
#Dill is basically used for saving the object into the file by converting it into
# first the pkl file
#dill is also used in serialisation of complex python objects

def save_object(file_path,obj):# take the two parameters 1st being the location where it has to be saved and then the object that has to be saved
    try:
        dir_path=os.path.dirname(file_path)#extrcating the path of the directory or the folder
        os.makedirs(dir_path,exist_ok=True)#if it does not exist make one
        
        with open(file_path,"wb") as file_obj: #opening the folder and dumping the object into the directory/folder
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)