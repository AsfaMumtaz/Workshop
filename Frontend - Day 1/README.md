# Deploying Your First Application on the Cloud

ssh into your EC2 machine

Clone the GitHub Repository 

Now that you have the code downloaded and pre requisites installed. Let jump roght into it!!!

Run `cat index.html` just to take a quick look at our frontend.
Now check the Dockerfile

```bash 
cat Dockerfile
```

Let's try to build the Docker Image now

```bash
sudo docker build -t simple-frontend .
```

Let's check the built Image 

```bash
sudo docker images
```

Now that we have the image on the system, let's try to run it.

```bash 
sudo docker run -d simple-frontend
```

-d: Runs container in a detached mode.

Let's check the running container

```
sudo docker ps
```

See if you can open the Frontend by hitting the insatance's public IP on port 80.

OH NO!! You can't! The docker network is different/separate from the host network. 

Let's confirm this by checking port 80 on the host.

```bash
sudo lsof -i :80
```

You need to map Docker port 80 to the host port 80. Let's do that.

```bash
sudo docker run -d -p 80:80 simple-frontend
```

Check the ports again.

Well Done! You have finished your first exercise!

