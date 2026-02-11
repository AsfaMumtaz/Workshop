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


## Nginx

```bash
sudo dnf install nginx -y
```
```sudo nano /etc/nginx/nginx.conf
```


```bash
server {
    listen 80;

    server_name _;

    location /api {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

