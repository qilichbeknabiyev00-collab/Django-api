# Dockerfile
FROM debian:bookworm-slim

RUN apt-get update 
    # apt-get install -y nginx

# Agar index.html mavjud bo'lsa
COPY ./index.html /var/www/html/index.html

CMD ["nginx", "-g", "daemon off;"]
