import torch
import torchvision
import torch.nn as nn


net = torchvision.models.resnet152()
net.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
net.fc = nn.Linear(2048, 512)


from torchsummary import summary


summary(net, (1, 14, 300))