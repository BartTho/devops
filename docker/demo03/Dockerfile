# Start met Rocky Linux 9
# FROM rockylinux:9-minimal
FROM ubuntu:latest

# update het OS
#RUN yum -y update && yum clean all

# Install nginx webserver
#RUN yum install -y nginx

# Maak een website aan

#RUN yum install -y unzip
#RUN yum install -y wget

RUN apt -y update

RUN apt -y install nginx
#COPY html /var/www/

# Start nginx en ook na herstart
#RUN systemctl enable nginx
#RUN systemctl restart nginx
# Open toegang tot poort 80 http

EXPOSE 80

#STOPSIGNAL SIGTERM
#CMD ["nginx", "-g", "daemon off;"]