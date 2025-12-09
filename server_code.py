from flask import Flask,request,jsonify
app=Flask(__name__)

import json,os
FILE_PATH = "users.json"

def load_users():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILE_PATH, "w") as f:
        json.dump(users, f, indent=4)
        
#Assigning File to variable Users
users = load_users() 

#Adding/Creating a User
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = {
        "id": data["id"],
        "name": data["name"],
        "email": data["email"],
        "mobileNumber": data["mobileNumber"],
        "password": data["password"]
    }
    users.append(user)
    return jsonify({"message": "User created", "user": user}), 201

#To Get all users details
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users)

#Getting User Details
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404

#Updating User
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["mobileNumber"] = data.get("mobileNumber", user["mobileNumber"])
            user["password"] = data.get("password", user["password"])

            return jsonify({"message": "User updated", "user": user})

    return jsonify({"error": "User not found"}), 404

#Deleting a user
@app.route("/users/<int:user_id>",methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": f"User {user_id} deleted"}

    return {"error": "User not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
