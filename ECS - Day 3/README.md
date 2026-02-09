# Deploying you application on ECS

## Push Images to ECR 
To run the application on ECS, Amazon's Elastic Container Service, we will first need to upload the images we built in the previous session to an Image Registry. 
To keep it simple, we will push the image to ECR. 


Connect to your instance again.

You won't be able to connect directlly to ECR as you need to add permission for it. 
So let's do that!

We also need to create an ECR Repository to push the images to.
You can do this through the console or by running the command below.

```bash
aws ecr create-repository --repository-name my-app
```

We also need to make a small change to our Frontend. Instead of calling the IP, we will only call /api.
Rebuild the Image


Now you are ready to push the image to ECR.

Run the below command to login to ECR. Remember to chnage the registry Url.

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```
Now you are logged in to the ECR registry.

Tag the images you have created

```bash
docker tag simple-frontend:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:frontend
docker tag simple-backend:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:backend
```
Push the images to ECR

```bash
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:frontend
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:backend
```

## Create ECS Cluster

Go to ECS service on AWS

Create a cluster with following specifications:

Type: Fargate + Managed EC2
Instance: t2.micro
Max Instances: 1


## Create Task Definitions

Now we need to add task definitions for our container. Task definistions are blueprint for the container. They tell ECS which image to run and specifiy other important details

### Frontend

For your Frontend, add the task definition below. Change the image url.

```json
{
  "family": "frontend-task",
  "networkMode": "bridge",
  "containerDefinitions": [
    {
      "name": "frontend",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:frontend",
      "essential": true,
      "memory": 256,
      "cpu": 256,
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80,
          "protocol": "tcp"
        }
      ]
    }
  ],
  "requiresCompatibilities": ["EC2"],
  "cpu": "256",
  "memory": "256",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
}

```


Now create the Frontend service.

### Backend

```json
{
  "family": "backend-task",
  "networkMode": "bridge",
  "containerDefinitions": [
    {
      "name": "backend",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:backend",
      "essential": true,
      "memory": 256,
      "cpu": 256,
      "portMappings": [
        {
          "containerPort": 3000,
          "hostPort": 3000,
          "protocol": "tcp"
        }
      ]
    }
  ],
  "requiresCompatibilities": ["EC2"],
  "cpu": "256",
  "memory": "256",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
}
```

Create the Backend Service.

## Create Application Load Balancer

Go to EC2 console and select Load Balancer option.

Now create an application load balacer.

You will see an option to create a target group. Create target groups for both your backend and frontend.

Create the ALB. 

Try opening the load balancer url.
You won't see anything as you haven't registered any targets, let's do this through the ECS console.


