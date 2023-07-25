# Lab 01. 이미지 분류 문제 해결 학습 : 20가지 다른 클래스의 다양한 음식 이미지 데이터 세트

import torch.nn as nn
import torch
import torchvision
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torchvision.models.mobilenetv2 import mobilenet_v2
from torch.optim import AdamW
from torch.nn import CrossEntropyLoss
from tqdm import tqdm
from torch.utils.data import DataLoader
from ex_01_0717_customdataset import MyFoodDataset

def train(model, train_loader, val_loader, epochs, optimizer, criterion, device) :
    best_val_acc = 0.0
    train_losses = []
    val_losses = []
    train_accs = []
    val_accs = []
    print("Train....")

    for epoch in range(epochs) :
        train_loss = 0.0
        val_loss = 0.0
        train_acc = 0.0
        val_acc = 0.0

        model.train()
        
        # tqdm Info
        train_loader_iter = tqdm(train_loader, desc=(f"Epoch : {epoch + 1} / {epochs}"), leave=False)

        for i , (data, target) in enumerate(train_loader_iter) :
            data, target = data.float().to(device), target.to(device)

            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, target)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

            # train acc
            _, pred = torch.max(outputs, 1)
            train_acc += (pred == target).sum().item()

            train_loader_iter.set_postfix({"Loss": loss.item()})

        train_loss /= len(train_loader)
        train_acc = train_acc / len(train_loader.dataset)


        # eval
        model.eval()
        with torch.no_grad() :
            for data, target in val_loader :
                # data,target = data.to(device).float(), target.to(device)
                data, target = data.float().to(device), target.to(device)
                output = model(data)
                pred = output.argmax(dim=1, keepdim=True)
                val_acc += pred.eq(target.view_as(pred)).sum().item()
                val_loss += criterion(output, target).item()
                
        val_loss /= len(val_loader)
        val_acc = val_acc / len(val_loader.dataset)

        train_losses.append(train_loss)
        train_accs.append(train_acc)
        val_losses.append(val_loss)
        val_accs.append(val_acc)

        # save model
        if val_acc > best_val_acc :
            torch.save(model.state_dict(), "./ex01_0717_mobilenet_v2_best.pt")
            best_val_acc = val_acc

        print(f"Epoch [{epoch + 1} / {epochs}] , Train loss [{train_loss:.4f}],"
              f"Val loss [{val_loss :.4f}], Train ACC [{train_acc:.4f}],"
              f"Val ACC [{val_acc:.4f}]")

    torch.save(model.state_dict(), "./ex01_0717_mobilenet_v2_last.pt")

    # save train and val result to csv
    # Plot and save train and val loss, acc

def main() :
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = mobilenet_v2(pretrained=True)
    model.classifier[1] = nn.Linear(1280, 20)
    model.to(device)

    # aug albumentations
    train_transforms = A.Compose([
        A.SmallestMaxSize(max_size=250),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=15, p=0.6),
        A.RandomShadow(),
        A.RGBShift(r_shift_limit=15, g_shift_limit=15, b_shift_limit=15, p=0.4),
        A.RandomBrightnessContrast(p=0.5),
        A.Resize(height=224, width=224),
        ToTensorV2()
    ])

    val_transforms = A.Compose([
        A.SmallestMaxSize(max_size=250),
        A.Resize(height=224, width=224),
        ToTensorV2()
    ])

    # dataset , dataloader
    train_dataset = MyFoodDataset("./food_dataset/train/", transform=train_transforms)
    val_dataset = MyFoodDataset("./food_dataset/validation/", transform=val_transforms)

    train_loader = DataLoader(train_dataset, batch_size=124, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=124, shuffle=False)

    # loss function , epoch, optimizer
    epochs = 20
    criterion = CrossEntropyLoss().to(device)
    optimizer = AdamW(model.parameters(), lr=0.001, weight_decay=1e-2)

    train(model,train_loader, val_loader, epochs, optimizer,criterion, device)

if __name__ == "__main__" :
    main()