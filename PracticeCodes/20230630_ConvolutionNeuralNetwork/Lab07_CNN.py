# Lab 07. 파이토치를 활용한 간단한 CNN 모델 구현 : MNIST 데이터셋을 사용하여 모델 학습

import torch
from torch import nn
import torchvision
from torchvision import transforms
import torchvision.utils as vutils
from torch.utils.data import DataLoader

class RBM(nn.Module):
    def __init__(self, visible_size, hidden_size):
        super(RBM, self).__init__()
        self.W = nn.Parameter(torch.randn(visible_size, hidden_size))
        self.v_bias = nn.Parameter(torch.randn(visible_size))
        self.h_bias = nn.Parameter(torch.randn(hidden_size))

    def forward(self, x):
        hidden_prob = torch.sigmoid(torch.matmul(x, self.W) + self.h_bias)
        hidden_state = torch.bernoulli(hidden_prob)
        visible_prob = torch.sigmoid(torch.matmul(hidden_state, torch.transpose(self.W, 0, 1) + self.v_bias))
        return visible_prob, hidden_state
    

if __name__ == "__main__":
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, ), (0.5, ))
        ])
    train_dataset = torchvision.datasets.MNIST(root="./data", train=True, transform=transform, download=True)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

    visible_size = 784
    hidden_size = 256
    rbm = RBM(visible_size, hidden_size)

    criterion = nn.BCELoss()
    optimizer = torch.optim.SGD(rbm.parameters(), lr=0.01)

    num_epochs = 10

    for epoch in range(num_epochs):
        for images, _ in train_loader:
            inputs = images.view(-1, visible_size)

            visible_prob, _ = rbm(inputs)

            loss = criterion(visible_prob, inputs)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch [{epoch + 1} / {num_epochs}], Loss : {loss.item():.4f}")

        vutils.save_image(rbm.W.view(hidden_size, 1, 28, 28), f"weights_epoch_{epoch + 1}.png", normalize=True)

        inputs_display = inputs.view(-1, 1, 28, 28)
        outputs_display = visible_prob.view(-1, 1, 28, 28)
        comparison = torch.cat([inputs_display, outputs_display], dim=3)
        vutils.save_image(comparison, f"reconstruction_epoch_{epoch+1}.png", normalize=True)