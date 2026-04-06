# NuOps Demo App - Simple User Management API
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store (demo purposes)
users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "user"},
}


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "users_count": len(users)})


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": list(users.values())})


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    new_id = max(users.keys()) + 1
    user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"],
        "role": data.get("role", "user"),
    }
    users[new_id] = user
    return jsonify(user), 201


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"deleted": deleted})


def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
