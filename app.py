from flask import Flask,jsonify,request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

connection_string = "mongodb+srv://parvezislam45:ihigYMqR70Odk8j4@cluster0.n9caqqb.mongodb.net/your_database_name?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.get_database('dbCollection') 
collection = db['collection']

@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

@app.route('/add_data', methods=['POST'])
def add_data_to_different_collection():
    try:
        data = request.get_json()
        new_collection = db['newCollection']
        inserted_data = new_collection.insert_one(data)
        return jsonify({'message': 'Data inserted successfully', 'inserted_id': str(inserted_data.inserted_id)})
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
@app.route('/add_data', methods=['GET'])
def get_added_data():
    try: 
        new_collection = db['newCollection']
        data_from_new_collection = list(new_collection.find({},{'_id': 0}))

        return jsonify({'data': data_from_new_collection})
    
    except Exception as e:
        
        return jsonify({'error': str(e)})   

if __name__ == '__main__':
    app.run(debug=True)
