import tqdm
import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd

from PIL import Image
from pathlib import Path
from torchvision import datasets, transforms, models


class TestDataset(torch.utils.data.Dataset):
    def __init__(self, df, root_dir, transform=None):
        self.df = df
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        img_path = Path(self.root_dir, self.df.iloc[idx, 0])
        img_name = img_path.name
        image = Image.open(img_path)

        if self.transform:
            image = self.transform(image)

        return image, img_name
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Run inference on a blinded test set.")
    parser.add_argument("-w", "--weights", type=str, required=True, help="Path to the model weights.")
    args = parser.parse_args()
    
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        print("no gpu available! Using cpu instead.")
        device = torch.device("cpu")
        
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    csv_fp = '/data/pathology/users/clement/diag_day/data/test.csv'
    df = pd.read_csv(csv_fp)
    
    image_dir = '/data/pathology/users/clement/diag_day/data/test'
    
    test_dataset = TestDataset(df, root_dir=image_dir, transform=transform)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(model.fc.in_features, 2)
    
    weights_path = args.weights
    
    sd = torch.load(weights_path)
    model.load_state_dict(sd)
    model = model.to(device)
    model.eval()
    
    predictions, image_names = [], []

    with torch.no_grad():

        with tqdm.tqdm(
            test_loader,
            desc=f"Test",
            unit=" img",
            leave=True,
        ) as test_t:

            for inputs, img_names in test_t:

                inputs = inputs.to(device)
                outputs = model(inputs)
                _, preds = torch.max(outputs, 1)
                predictions.extend(preds.cpu().numpy())
                image_names.extend(img_names)
    
    submission_df = pd.DataFrame({
        'image_name': image_names,
        'prediction': predictions
    })
    submission_df.to_csv('submission.csv', index=False)
