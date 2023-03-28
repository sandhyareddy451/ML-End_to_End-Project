# Housing Predictor Machine Learning Project

## Software and Tools Requirement


 [Github Account](https://github.com/sandhyareddy451)

 [Heroku Account](https://signup.heroku.com/)

 [VsCode IDE](https://code.visualstudio.com/)

 [GitCLI](https://git-scm.com/downloads)


## Creating conda environment
---
conda create -p venv python==3.7 -y

---
conda activate venv/

---

## To Add files to git
---
git add .

---
## To check the git status

---
git status

---

## To create version/commit all changes by git
---
git commit -m "message"

---

## To send version/changes to github

---
git push origin main

---

## To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = vemula.sandhya51@gmail.com

HEROKU_API_KEY = <>

HEROKU_APP_NAME = ml-regression-app



## BUILD DOCKER IMAGE

---
docker build -t <image_name>:<tag_name>.

---
## To list docker image

---
docker images

---

## Run docker image

---
docker run -p 5000:5000 -e PORT=5000 <key>

---