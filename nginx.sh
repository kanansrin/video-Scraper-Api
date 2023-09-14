#!/bin/bash

sudo cp -rf scrapapp.conf /etc/nginx/sites-available/scrapapp
chmod 710 /var/lib/jenkins/workspace/sih2023

sudo ln -s /etc/nginx/sites-available/scrapapp /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx