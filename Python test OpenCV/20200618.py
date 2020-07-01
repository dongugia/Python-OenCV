
import torch

seed= 3
torch.manual_seed(seed)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Decive:' ,device)

N,n_inputs,n_hidden, n_outputs= 5,1,100,1

x = torch.tensor([[0.0],[1.0],[2.0],[3.0],[4.0],[5.0],[6.0],[7.0]],device = device)
y = torch.tensor([[0.0],[10.0],[20.0],[30.0],[40.0],[50.0],[60.0],[70.0]],device = device)

model = torch.nn.Sequential(
    torch.nn.Linear(n_inputs, n_hidden),
    torch.nn.ReLU(),
    torch.nn.Linear(n_hidden, n_outputs)
)
model.to(device)
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4
for t in range(1000):
    y_out= model.forward(x)
    loss = loss_fn(y_out,y)
    if  t % 100 ==99:
        print(t,loss.item())
        print(y_out)
    model.zero_grad()
    loss.backward()

    with torch.no_grad():
        for param in model.parameters():
           param -= learning_rate * param.grad