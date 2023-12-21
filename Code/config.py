from azureml.core.model import InferenceConfig

inference_config = InferenceConfig(entry_script="score.py", environment=myenv)