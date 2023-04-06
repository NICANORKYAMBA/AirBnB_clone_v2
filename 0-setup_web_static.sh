#!/usr/bin/env bash
# script that sets up my web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create folder /data/ if it doesn't exist
mkdir /data/

# Create folder /data/web_static if it doesn't exist
mkdir /data/web_static/

# Create folder /data/web_static/releases/ if it doesn't exist
mkdir /data/web_static/releases/

# Create folder /data/web_static/shared/ if it doesn't exist
mkdir /data/web_static/shared/

# Create folder /data/web_static/releases/test/
mkdir /data/web_static/releases/test/

# Create fake HTML file
touch /data/web_static/releases/test/index.html

echo " <html>
  	<head>
  	</head>
  	<body>
    	 alx #DoHardThings
  	</body>
       </html>" > /data/web_static/releases/test/index.html

# Remove the symbolic link if it exists
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

# Create the symbolic link
ln -s /data/web_static/releases/test /data/web_static/current

# Giving ownership of /data/ to ubuntu owner and group
chown -R ubuntu:ubuntu /data/

# Updating Nginx configuration to serve content of /data/
# web_static/current/ to hbnb_static

echo "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/;
    }
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
    add_header X-Served-By \$hostname;
}" > /etc/nginx/sites-available/default

# Restarting Nginx
sudo service nginx restart
