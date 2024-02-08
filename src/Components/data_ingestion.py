import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



'''
Sure, let's break it down in simple terms:

Imagine you're a chef preparing to cook a meal. You need specific ingredients, right? And those ingredients might come from different places - maybe the grocery store, maybe the farmer's market. So, you organize a list of where to find each ingredient.

Now, in programming, we do something similar. We often need to work with different sets of data when building software, like training data (used to teach a model), testing data (used to check if the model learned well), and raw data (the original, untouched info). 

The `DataIngestionConfig` class is like that list of ingredients for your program. It helps keep track of where to find each type of data your program needs. For instance, `train_data_path` tells the program where to find the training data, `test_data_path` for testing data, and `raw_data_path` for the untouched original data.

By having this class, it makes it easier for developers to manage and update the locations of these data files without having to search through the entire codebase. It's a way to organize and centralize this information, making the code cleaner and more maintainable.
'''
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

        def initiate_data_ingestion(self):
            logging.info("Entered the data ingestion method or component")
            try:
                df=pd.read_csv('Notebook\data\stud.csv')
                logging.info('Read the dataset as dataframe')
                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
                df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
                logging.info("Train test split initiated")

                train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
                train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
                test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

                logging.info("ingestion of the data is complete")

                return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )
            except Exception as e:
                raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

'''
This code defines a data ingestion process for a machine learning project. Let's break it down:

1. **DataIngestionConfig**: This class is a configuration holder. It defines default paths for training data, testing data, and raw data. It's like a set of instructions on where to find different types of data needed for the project.

2. **DataIngestion**: This class is responsible for actually ingesting the data. It initializes with an instance of `DataIngestionConfig` to access the paths. Inside the `initiate_data_ingestion` method:
   - It logs the start of the data ingestion process.
   - It reads a CSV file named 'stud.csv' located in a specific directory.
   - It creates directories if they don't exist for the train, test, and raw data paths specified in the `DataIngestionConfig`.
   - It saves the entire dataset as raw data in the specified raw data path.
   - It splits the dataset into training and testing sets using `train_test_split` from `sklearn`.
   - It saves the training and testing sets into separate CSV files in the paths specified in the `DataIngestionConfig`.
   - It logs the completion of the data ingestion process.

3. **Outcome**: The outcome of running this code would be:
   - Reading a dataset from 'Notebook\data\stud.csv'.
   - Saving the entire dataset as raw data in 'artifacts/data.csv'.
   - Splitting the dataset into training and testing sets and saving them in 'artifacts/train.csv' and 'artifacts/test.csv', respectively.
   - Logging messages indicating the progress and completion of the data ingestion process.

In simple words, this code sets up a structured way to manage data files for a machine learning project, reads a dataset, splits it into training and testing sets, and saves them in designated locations while logging the process for monitoring.

'''