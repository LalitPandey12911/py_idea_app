from flask import Flask,redirect,url_for,render_template,request# importing flask class from the flask library

app = Flask(__name__)  # creating the instance of flask class

@app.route('/') #this is a decorator that tells Flask what URL should trigger the funtion 
def hello_world():
    return 'Hello mere bete'

@app.route('/home')
def hello_home():
    return "hello form homepage"

@app.route('/<name>')
def user(name):
    return f"hello {name}!"

@app.route('/home/test')
def test_home():
    return redirect(url_for("hello_home"))  #redirect to the hello_home url

@app.route('/html_tag')
def html():
    return "<h1>HTML USE:</h>"

#to render the function from html page to this app.py
@app.route('/render_html')
def rendering():
    return render_template('test.html')




#IdeaApp
#create the idea repository
ideas ={
    1:{
        "id":1,
        "idea_name": "ONDC",
        "idea_description":"Details about ONDC",
        "idea_author":"Adeeb"
    },
    2:{
        "id":2,
        "idea_name":"Save Soil",
        "idea_description":"Details about Saving Soil ",
        "idea_author":"Ankit Sharma"
    }

}

"""
Create an RESTFUL endpoint for fetching all the ideas
"""

@app.get("/ideaapp/api/v1/ideas")
def get_all_idea():
    #I need to read the query param 
    idea_author = request.args.get('idea_author')

    if idea_author:
        #filter the idea created by this author
        idea_res = {}
        for key,value in ideas.items():
            if value["idea_author"] == idea_author:
                idea_res[key] =value
        return idea_res
    #logic to fetch all the ideas and support query params
    return ideas


"""
Create a RESTful endpoint for creating a new idea
"""
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    #logic to create a new idea
 try:
        #first read the request body
        request_body = request.get_json() #>>this rep. the req. body passed by the user

        #check if the idea id pass is not present already
        if request_body['id'] and request_body["id"] in ideas:
            return "idea with the same id already present",400 #400>> bad req.

        #insert the passed idea in the idea dic
        ideas[request_body["id"]] = request_body

        #return the response saying idea got saved
        return "idea created and saved successfully",201 #201 >> code for successfully created
 except KeyError:
     return "id is missing",400
 except:
     return "some internal server error",500
 


 """
 End point to fetch idea based on the idea id
 """
@app.get("/ideaapp/api/v1/ideas/<idea_id>") #Idea_id>>is a path param >> should be in angular braket
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "Idea id passed is not present",400

    except:
        return "some internal error happended",500


"""
Endpoint for updating the idea
"""
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)]=request.get_json()
            return ideas[int(idea_id)],200
        else:
            return "Idea id passed is not present",400

    except:
        return "some internal error happended",500



'''
End point to delete an idea
'''
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))
            return "idea got successfully removed"
        else:
            return "idea id passed is not present",400
        
    except:
        return "some inernal error happended",500



if __name__ == '__maine__':
    app.run(port=8080)#this line runs the application on the local development server,and allow possible error to apperar on the web page.
