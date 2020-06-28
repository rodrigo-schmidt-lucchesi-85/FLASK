# 1) Defining modules
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from mongoengine import * # por nos documentos


# 2) Connect to mongodb localhost
connect('FLEX_DATABASE', host='localhost', port=27017)  # Create a Database

# 3) Create collections to the MongoDB data modelling
class User(Document):
    username = StringField(required=True, max_length=100)
    password = StringField(required=True,max_length=20)
    
class News(Document):
    username = StringField(required=True, max_length=100)
    news_title = StringField(required=True,max_length=200)
    news_author = StringField(required=True,max_length=200)
    news_content = StringField(required=True,max_length=None)
    
    meta = {'indexes': [
        {'fields': ['$news_title', "$news_author", "$news_content"],
         'default_language': 'english',
         'weights': {'news_title': 10, 'news_author': 7, 'news_content': 3}
        }
    ]}

# 4) Create Flask app and an api from it
app = Flask(__name__)
api = Api(app)

# 5) Create the News registration resource
class NewsRegistration(Resource): # Working
    def post(self):
        # Step 1 is to get posted data by the user
        postedData = request.get_json()

        # Get the data -> username, password
        post_username = postedData["username"]
        post_password = postedData["password"]
        post_news_title = postedData["news_title"]
        post_news_author = postedData["news_author"]
        post_news_content = postedData["news_content"]

        # Store username and password into the database
        User(username = post_username, password = post_password).save()
        News(username = post_username, news_title = post_news_title, news_author = post_news_author, news_content = post_news_content).save()
        
        
        # Returning JSON file
        returningJsonFile = {
            "status": 201,
            "msg": "Welcome"+" "+ post_username +" "+". You successfully registered the news!"
        }
        return jsonify(returningJsonFile)

# 6) Create the Query dataset resource with user credentials verifications
class QueryNews(Resource):
    def post(self):

        # Get Data
        postedData = request.get_json()

        post_username = postedData["username"]
        post_password = postedData["password"]
        post_search = postedData["search"]
        option = postedData["option"]
        
        if post_password == User.objects(username=post_username)[0].password:
            
            document = News.objects(username=post_username).search_text(post_search).first()
            
            if option == 'show':

                if document is None:
            
                    returningJsonFile = {
                        "status": 404,
                        "msg": "File not found"                
                    }
                    return jsonify(returningJsonFile)
                    
                else:

                    returningJsonFile = {
                        "status": 200,
                        "msg": "The file found to the performed search:",
                        "news_title": document.to_json()
                    }
                    return jsonify(returningJsonFile)
            
            elif option == 'delete':

                if document is None:
            
                    returningJsonFile = {
                        "status": 404,
                        "msg": "File not found"                
                    }
                    return jsonify(returningJsonFile)

                else:

                    documentDeleted = document
                    document.delete()
                    
                    returningJsonFile = {
                        "status": 200,
                        "msg": "The file found to be deleted:",
                        "news_title": documentDeleted.to_json()
                    }
                    return jsonify(returningJsonFile)
            
            else: 
                
                returningJsonFile = {
                    "status": 301,
                    "msg": "Wrong option!"
                }
                return jsonify(returningJsonFile)
                
        
        else:
            
            returningJsonFile = {
                "status": 301,
                "msg": "Wrong password!"
            }
            return jsonify(returningJsonFile)

# 7) Create a Global search resource with control search results with weights
class SearchNews(Resource):
    def post(self):

        # Get Data
        postedData = request.get_json()
        post_search = postedData["search"]

        document = News.objects.search_text(post_search).first()

        if document is None:
            
            returningJsonFile = {
                "status": 404,
                "msg": "File not found"                
            }
            return jsonify(returningJsonFile)

        else:

            returningJsonFile = {
            "status": 200,
            "msg": "The file found to the performed search:",
            "news_title": document.to_json()
            }
            return jsonify(returningJsonFile)


api.add_resource(NewsRegistration, '/newsRegistration')
api.add_resource(QueryNews, '/queryNews')
api.add_resource(SearchNews, '/searchNews')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
