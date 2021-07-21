# REST API for deploying a CNN for MNIST prediction
  
## Features:
- CNN trained in Keras (tensorflow)
- API developed using the Flask framework
- WSGI using Gurnicorn
- Nginx Web Server
- Docker compose implementation

## How to run:
1. In the repository directory:
    `sudo docker-compose build`
    then,
    `sudo docker-compose up`

2. Use Postman to query the API on `http://0.0.0.0/predict` uploading your image file in the `form-data` field of the request with key as `image-file`

3. Get the prediction in the response as:

`{ ` 
  `filename:'sample0.png',  `
  `prediction: 3`
`}`