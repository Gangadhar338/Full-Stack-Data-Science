# Install PyTorch for your platform using https://pytorch.org/get-started/locally/
import torch
from torch import nn

torch.manual_seed(42)
X = torch.arange(0, 10, dtype=torch.float32).reshape(-1, 1)
y = 2 * X + 1
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for epoch in range(500):
    prediction = model(X)
    loss = loss_fn(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Learned weight and bias:", model.weight.item(), model.bias.item())
print("Final loss:", round(loss.item(), 4))
