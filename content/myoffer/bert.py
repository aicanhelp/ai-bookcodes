import torch
from torch import nn


class Classifier(nn.Module):
    def __init__(self, hidden_size):
        self.linear = nn.Linear(hidden_size, 1)
        self.sigmod = nn.Sigmoid()

    def forward(self, x):
        return self.sigmod(self.linear(x).sequeeze(-1))
