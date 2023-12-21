import torch
from torchvision.transforms import functional as F
from torchvision import datasets
from torch.utils.data import DataLoader
from facenetmodelensemble import EnsembleModel, ModifiedInceptionResnetV1

resnet_model_count = 3
resnet_models = [ModifiedInceptionResnetV1(pretrained='vggface2').eval() for _ in range(resnet_model_count)]
ensemble_model = EnsembleModel(models=resnet_models)

def init():
    global ensemble_model
    ensemble_model = ensemble_model.to("cuda" if torch.cuda.is_available() else "cpu")

def run(input_data):
    # Perform inference
    input_data = torch.tensor(input_data['data'], dtype=torch.float32)
    input_data = F.to_tensor(input_data).unsqueeze(0)
    input_data = input_data.to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        output = ensemble_model(input_data)

    return output.cpu().numpy().tolist()
