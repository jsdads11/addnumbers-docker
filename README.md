# addnumbers-docker
This project is based on a boilerplate for future Flask applications. This app is call my-flask-app and is store on GitHub here https://github.com/jsdads11/flask-helloworld-docker.git 
The steps below can be executed on any unix-like system.
## Setup SSH key
**This step is an option and can be omitted.**
Create ssh key and add it to GitHub's [SSH keys](https://github.com/settings/keys) settings.
```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
```
## Installation
```bash
# Cloning the source code
git clone https://github.com/jsdads11/addnumbers-docker.git
cd addnumbers-docker
# Building and running as a Docker container
docker build --tag addnumbers-docker --build-arg FLASK_DEBUG=True .
docker run --detach --name my-addnumbers-app --publish 80:8080 --rm addnumbers-docker
docker ps
```
## API
```bash
curl "http://localhost"; echo
```
## Testing
Unit test
```bash
docker exec my-addnumbers-app pytest
```
Code coverage
```bash
docker exec my-addnumbers-app coverage run -m pytest
docker exec my-addnumbers-app coverage report
```
Stop container
```bash
docker stop my-addnumbers-app
```
