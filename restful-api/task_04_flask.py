@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # NEW CHECK → username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201
