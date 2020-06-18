# Search and register news API - [Python,Flask,Mongoengine,Docker]
#### by Rodrigo Lucchesi

## 1) Project description:
A project to save & search using MongoDB database using RESTful-API modeling with Python libraries: 

- Flask 
- ORM mongoengine.

Also, a containerized purpose is developed with Docker and docker-compose seeking systems compatibility. In this Flask RESTful-API  three resources were created to perform the required questions to the FLEX project. Consequently, the following resources are described below:

## 1.1) /newsRegistration

News registration resource gets data from a JSON file, using a POST method to the CRUD actions. There are five inputs: username, password, news title, news author and news content. The username is saved in the collection User, used to the credentials verification and also applied to the News collection where the news documents will be stored. The API returning file is also a JSON format with a feedback embedded to the message. 

## 1.2) /queryNews
Query news resource gets data from a JSON file, using a POST method to the CRUD actions. There are four inputs: username, password, search, and options. The whole mechanism is orchestrated by conditional statements where the user credentials are tested as the first step. If the password is right it tests the option inserted. If the search or delete option doesn't find a document with the search engine, it returns a 404 error. The whole search engine is given by weighted values to the news keys, going from the higher value of title to the content as lowest. 

## 1.3) /searchNews
Search resource gets data from a JSON file, using a POST method to the CRUD actions. There is one input: search. This resource query the database, using the same searching engine, to all user documents that match with the input request. Returns an error if not file is found.






