import torch
import os
import torchvision.datasets as datasets
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms
import torch.nn as nn
import math
import numpy as np
import matplotlib.pyplot as plt

'''
Human Detection Dataloader
Available at: https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset
Acquired on Wednesday 29th November
'''


class Classifier(nn.Module):

    # Create the train and val dataloaders and the model
    def __init__(self, dataset_src: str = "../Datasets/human detection dataset", batch_size: int = 32, loss_func=None):
        super(Classifier, self).__init__()

        self.loss_func = nn.CrossEntropyLoss() if loss_func is None else loss_func

        # Create dataloaders
        self.batch_size = batch_size
        self.classes = ["No People", "Yes People"]
        tensor_transform = transforms.Compose([
            transforms.PILToTensor(),
            transforms.Resize((128, 128), antialias=True),
            transforms.Lambda(lambda y: y.float() / 255),
            transforms.Normalize(0.5, 0.5),
        ])
        people_dataset = datasets.ImageFolder(root=dataset_src, transform=tensor_transform)

        train_size = int(0.8 * len(people_dataset))
        test_size = len(people_dataset) - train_size
        self.train_dataset, self.validation_dataset = torch.utils.data.random_split(people_dataset,
                                                                                    [train_size, test_size])

        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=self.batch_size, shuffle=True)
        self.validation_loader = DataLoader(dataset=self.validation_dataset, batch_size=self.batch_size, shuffle=True)

        # Define Model
        self.conv_layers = nn.Sequential(

            nn.Conv2d(in_channels=3, out_channels=4, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(4),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # B x 4 x 64 x 64

            nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(8),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # B x 8 x 32 x 32

            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # B x 16 x 16 x 16

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # B x 32 x 8 x 8

        )
        self.MLP = nn.Sequential(
            nn.Linear(in_features=32 * 8 * 8, out_features=64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Linear(in_features=64, out_features=2)
        )

        total_parameters = (sum(p.numel() for p in self.conv_layers.parameters() if p.requires_grad) +
                            sum(p.numel() for p in self.MLP.parameters() if p.requires_grad))
        print(f"Created classifier with {total_parameters} trainable parameters")

    # Display a sample of the images from the dataset along with their class
    def display_sample(self):
        images, labels = next(iter(self.train_loader))
        figure = plt.figure(figsize=(10, 8))
        cols, rows = 5, 5
        for i in range(cols * rows):
            figure.add_subplot(rows, cols, i + 1)
            plt.title(self.classes[labels[i]])
            plt.axis("off")
            plt.imshow((images[i].squeeze().permute(1, 2, 0) + 1) / 2)
        plt.show()

    # Saves the model weights to location
    def save(self, location: str):
        pass

    # Loads model weights from location
    def load(self, location: str):
        pass

    # Train the classifier against the dataset specified initially
    def train_epochs(self, epochs: int = 0):
        pass



    def forward(self, x):
        # Input x has dimensions B x 3 x 128 x 128, B is batch size
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        x = self.MLP(x)
        # Output has dimensions B x 5
        return x


model = Classifier()
