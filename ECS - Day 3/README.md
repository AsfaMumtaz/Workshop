# Deploying you application on ECS


To run the application on ECS, Amazon's Elastic Container Service, we will first need to upload the images we built in the previous session to an Image Registry. 
To keep it simple, we will push the image to ECR. 


Connect to your instance again.

You won't be able to connect directlly to ECR as you need to add permission for it. 
So let's do that!


Once you have added the correct role to your instance, you are ready to push the image to ECR.