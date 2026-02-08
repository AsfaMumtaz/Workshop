# Workshop
The Resposiry contains all the content for all the workshops conducted

To get started, you will need to install a few things on your EC2 insstance

## Git Installation Guide (EC2 Amazon Linux 2023)

```bash

sudo dnf update -y

sudo dnf install git -y

git --version
```

## Docker Installation Guide

```bash
sudo dnf install docker -y
```
Start docker daemon

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Additional steps if you want to run docker without sudo

`sudo usermod -aG docker $USER`

The above command adds your user to the "docker" group.






