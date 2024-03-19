# api.py #

######## Importing Libraries ########
from flask import Flask
from flask_restful import Api, Resource

# List containing numbers from 0 to 5
list_of_numbers=list(range(5))   # ( 0,1,2,4 )

# Creating a Flask instance and passing that instance to the API
# Here __name__ is a special variable whose value is set by Interpreter
# (Here __name__ = __main__)
app = Flask(__name__)
api = Api(app)

# Adding the list numbers_to_add using the sum method
total=sum(list_of_numbers)

# add class inherits the Resource class to specify Route associated with it

class add(Resource):
            #   HTTP GET method.    (REST)
	  def get(self):
	      return f""total, {escape(total)}!"
	
# Associating class 'add' with the route '/total'
api.add_resource(add, "/total")

# Debug parameter set as True to make changes without restarting the program.

if __name__ == "__main__":
    app.run(port=8000, debug=True)

# app.run(debug=True)
