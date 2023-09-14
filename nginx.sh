#!/bin/bash

sudo cp -rf inventsoft.conf /etc/nginx/sites-available/inventsoft
chmod 710 /var/lib/jenkins/workspace/django-cicd

sudo ln -s /etc/nginx/sites-available/inventsoft /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx