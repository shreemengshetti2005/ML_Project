# How the Files Work Together
# train_pipeline.py:

# Uses data_ingestion.py to load and prepare the data.
# Calls data_transformation.py to preprocess the data.
# Invokes model_trainer.py to train and evaluate the model.
# predict_pipeline.py:

# Takes in new input data.
# Preprocesses it using functions from data_transformation.py.
# Uses the trained model from model_trainer.py to generate predictions.
# Shared Utilities:

# logger.py logs key events across all components.
# exception.py ensures consistent error handling in all modules.
# utils.py provides helper functions used by all other modules.