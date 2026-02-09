# Deploying the Backend

Start by updating the username to your name.

Build the backend image


Now run the container and expose it on port 3000 of the host..

Nwow that your backend is running, let's update the instance security group to allow traffic on port 3000

Once updated, let's stop the old running frontend container.

```bash 
sudo docker stop <container-id>
sudo docker rm <container-d>
sudo docker rmi simple-frontend
```

Now update the code in Frontend where you see a call to simple-backend:3000/api

Instead of localhost, add the instance IP.


Build and run the container again.

Open the browser and see the magic!

