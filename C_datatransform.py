import numpy as np
from torchvision import transforms

def get_data_transforms(op):
    op = 0
    mean = np.array([0.5, 0.5, 0.5])
    std = np.array([0.25, 0.25, 0.25])
    data_transforms = {
        'train': transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
        ]),
        'val': transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
        ]),
        'test': transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
        ]),
    }
    if op == 0:
        return data_transforms
    elif op == 1:
        temp = [
            transforms.Resize(224),
            transforms.Normalize(mean, std),
            transforms.ToTensor(),
        ]
        data_transforms = {
            'train': transforms.Compose(temp),
            'val': transforms.Compose(temp),
            'test': transforms.Compose(temp),
        }
    elif op == 2:
        temp = [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.Normalize(mean, std),
            transforms.ToTensor(),
        ]
        data_transforms = {
            'train': transforms.Compose(temp),
            'val': transforms.Compose(temp),
            'test': transforms.Compose(temp),
        }
    for ii in range(1,4):
        data_transforms[f'aug{ii-1}'] = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.RandomHorizontalFlip(ii//2),
            transforms.RandomVerticalFlip(ii%2),
            transforms.Normalize(mean, std),
            transforms.ToTensor(),
        ])
    return data_transforms