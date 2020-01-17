### Deploying Machine Learning to Production (Microservices)


### Main Technologies
- Docker
- Flask
- PySpark
- AWS
- Scikit-Learn
- Spark MLlib
- TensorFlow
- Keras
- Go

=> Train Models in Python, save/serialize models, load it into Go, containerize, and build the API (application). Voila!


-----------
1. Train the Model (in Python) using Keras, TensorFlow, PyTorch, Scikit-Learn or Spark MLlib
2. Build the API - Flask, Flask-RESTful, or Go
3. Test the API
4. Test webserver - Gunicorn web server
5. Load Balancer - Configure NGINX or AWS ELB, [Example: Serve Apps w/ Flask, Gunicorn, & NGINX](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
6. Load/Performance Testing (Recommended: [Locust](https://github.com/locustio/locust))


**Gunicorn**

```bash
gunicorn --workers 1 --timeout 300 --bind 0.0.0.0:8000 api:app
- workers (INT): The number of worker processes for handling requests.
- timeout (INT): Workers silent for more than this many seconds are killed and restarted.
- bind (ADDRESS): The socket to bind. [['127.0.0.1:8000']]
- api: The main Python file containing the Flask application.
- app: An instance of the Flask class in the main Python file 'api.py'.
```

**Load Balancer**
You can configure `nginx` to handle all the test requests across all the `gunicorn` workers, where each worker has its own API with the DL model. Refer this resource to understand the setup between `nginx` and `gunicorn`.











### Popular Methods of Deploying Machine Learning Models to Production

1. Deploy your machine learning model as a REST API using Docker and AWS services like ECR, Sagemaker and Lambda.

- We’ll then deploy the containerized model to ECR and create a machine learning endpoint in Sagemaker. Then we’ll finish off by creating the REST API endpoint. The model used in this post was made using Scikit Learn, but the approach detailed here will work with any ML framework in which an estimator’s or transformer’s state can be serialized, frozen or saved.
  
You will need to save (serialize, e.g. Joblib and Pickle) any estimators or transformers in addition to your model for the API. e.g. anything done to preprocess the data for the model.


1. Build the Model. Pick your technology, it doesn't really matter. Python, Go, JavaScript, Java, Scala, etc. The main thing is being able to save the model in a serialized format that can be used anywhere.
2. Create Tests for your model
3. Save the Model in a serialized format

4. Creating the Dockerfile
5. Build and Test the Docker container
6. Figure out the smoke tests/capacity needed (which EC2, ECS, etc size or fleet you need to handle load)
7. Deploy to Production




1. Save the Model

The first step in the deployment process will be to prepare and store your model such that it can be easily re-opened elsewhere. This can be achieved through serialization, which freezes the state of your trained classifier and saves it. To do this, we will be using Scikit Learn’s Joblib, a serialization library specifically optimized for storing large numpy array’s, and thus especially suited for Scikit Learn models. If you have more than one Scikit Learn estimator or transformer in your model (for example, a TFIDF preprocessor, like we have), you can save those using Joblib as well. The sentiment analysis model includes two components that we will have to save/freeze: the TFIDF text-preprocessor and the classifier. The following code dumps the classifier and tfidf vectorizer to the folder Model_Artifacts.

```python
from sklearn.externals import joblib
joblib.dump(classifier, 'Model_Artifacts/classifier.pkl')
joblib.dump(tfidf_vectorizer, 'Model_Artifacts/tfidf_vectorizer.pkl')
```

2. Creating the Dockerfile

Once the estimators and transformer are serialized, we can create a Docker image that holds our inference and server environment. Docker makes it possible to package your local environment and use it on any other server/environment/computer without having to worry about technical details. The Docker image will contain all the necessary components that will enable your model to perform predictions and communicate with the outside world. We can define a Docker image with a Dockerfile that specifies the contents of the environment: we’ll want to install Python 3, Nginx for the webserver and various Python packages like Scikit-Learn, Flask and Pandas.






### WebServers
- [Overall Rundown of Python WSGI Servers](https://www.appdynamics.com/blog/engineering/an-introduction-to-python-wsgi-servers-part-1/)
- [Performance Analytics and Benchmarks of Python WSGI Servers](https://www.appdynamics.com/blog/engineering/a-performance-analysis-of-python-wsgi-servers-part-2/)
- [Bjoern](https://github.com/jonashaag/bjoern) - describes itself as a “screamingly fast Python WSGI server” and boasts that is “the fastest, smallest and most lightweight WSGI server.”
- [Gunicorn](https://gunicorn.org/) - It modestly claims that it is “simply implemented, light on server resources, and fairly speedy.” Unlike Bjoern and CerryPy, Gunicorn is a standalone server. 
- [CherryPy](https://github.com/cherrypy/cherrypy)


### Deploying ML Models with Go


### Machine Learning Deployment with Kubernetes
- [seldon-core](https://github.com/SeldonIO/seldon-core) - Machine Learning Deployment for Kubernetes https://www.seldon.io/

### Pre-trained TensorFlow Models
- [Github Repo: TensorFlow Models](https://github.com/tensorflow/models)
### Docker
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

### Async Worker Queue for ML submit requests (Decouples backend)
- [mlq](https://github.com/tomgrek/mlq) - Asynchronous queue for machine learning jobs
- Dask
- Celery

### Tips
- Use a queue
- Don’t tie up your backend webserver; separate any ML processes (on it's own server) from the act of serving up assets and endpoints
- Ensure everything is stateless and able to operate in parallel

###

### End-to-End Examples of Deploying Python ML Models to Production
- [A guide to deploying Machine/Deep Learning model(s) in Production](https://blog.usejournal.com/a-guide-to-deploying-machine-deep-learning-model-s-in-production-e497fd4b734a)
- [Exposing Python machine learning models using Flask, Docker and Azure](https://www.martinnorin.se/exposing-python-machine-learning-models-using-flask-docker-and-azure/)
- [Deploy your Machine Learning model as an API in 5 minutes (with Docker and Flask)](https://medium.com/dataswati-garage/deploy-your-machine-learning-model-as-api-in-5-minutes-with-docker-and-flask-8aa747b1263b)
- [There are two very different ways to deploy ML models, here’s both](https://towardsdatascience.com/there-are-two-very-different-ways-to-deploy-ml-models-heres-both-ce2e97c7b9b1)
- [Save Machine Learning Model to A File (Part 1)](https://www.mikulskibartosz.name/how-to-save-a-machine-learning-model-into-a-file/)
- [A comprehensive guide to putting a machine learning model in production using Flask, Docker, and Kubernetes](https://www.mikulskibartosz.name/a-comprehensive-guide-to-putting-a-machine-learning-model-in-production/)
- [Deploying Python ML Models with Flask, Docker and Kubernetes](https://alexioannides.com/2019/01/10/deploying-python-ml-models-with-flask-docker-and-kubernetes/)
- [Building a spam classifier: PySpark+MLLib vs SageMaker+XGBoost](https://medium.com/@julsimon/building-a-spam-classifier-pyspark-mllib-vs-sagemaker-xgboost-1980158a900f)
- [Learn to how to create a simple API from a machine learning model in Python using Flask](https://www.datacamp.com/community/tutorials/machine-learning-models-api-python)
- [DEPLOYING FLASK APP TO ECS](https://www.bogotobogo.com/DevOps/Docker/Docker-Flask-ALB-ECS.php)
- [Develop a NLP Model in Python & Deploy It with Flask, Step by Step](https://towardsdatascience.com/develop-a-nlp-model-in-python-deploy-it-with-flask-step-by-step-744f3bdd7776)
- [Deploying a Keras Deep Learning Model as a Web Application in Python](https://towardsdatascience.com/deploying-a-keras-deep-learning-model-as-a-web-application-in-p-fc0f2354a7ff)
- [Deploying a Python Web App on AWS](https://towardsdatascience.com/deploying-a-python-web-app-on-aws-57ed772b2319)





### Serving ML Models with PySpark
- [Lightning Fast ML Predictions with PySpark](https://medium.com/homeaway-tech-blog/lightning-fast-ml-predictions-with-pyspark-354c8c5abe83)


### Architectures of Microservices

Redis - Docker - Flask - DynamoDB/MongoDb


- [Redis](https://github.com/andymccurdy/redis-py), [Redis Tutorial](https://realpython.com/python-redis/?__s=zwqjxatutwooqsxdbtg1)


### Linear Algebra
https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab

### Deep Learning
- [Fastai v3](https://github.com/fastai/course-v3/tree/master/nbs)
- [Fastai Blog](https://www.fast.ai/)

### Deep Learning Hubs
- [PyTorch Hub](https://pytorch.org/hub)
- [TensorFlow Hub](https://www.tensorflow.org/hub)

### PyTorch Tutorials
https://pytorch.org/tutorials/
https://forums.fast.ai/t/wiki-thread-intro-workshop/6537

### Others to Sort out
https://github.com/kubeflow/pipelines
https://github.com/kubeflow/examples#end-to-end
https://www.kubeflow.org/
https://github.com/SeldonIO/seldon-core
https://www.seldon.io/
https://www.notion.so/The-Best-Artificial-Intelligence-Machine-Learning-and-Data-Science-Resources-b3b97fa097b747698e87fd3badc657cf
