from flask import Flask, jsonify, request, abort

app = Flask(__name__)

brands = [
  {"id": 1, "name": "Acura", "average_price": 702109},
  {"id": 2, "name": "Audi", "average_price": 630759},
  {"id": 3, "name": "Bentley", "average_price": 3342575},
  {"id": 4, "name": "BMW", "average_price": 858702},
  {"id": 5, "name": "Buick", "average_price": 290371}
]

models = [
  {"id": 1,"brand_id":1, "name": "ILX", "average_price": 303176},
  {"id": 212,"brand_id":2, "name": "MDX", "average_price": 448193},
  {"id": 31,"brand_id":3, "name": "NSX", "average_price": 3818225},
  {"id": 14,"brand_id":4, "name": "RDX", "average_price": 395753},
  {"id": 56,"brand_id":5, "name": "RL", "average_price": 239050}
]

# Endpoint to get all brands
@app.route("/brands", methods=["GET"])
def get_brands():
    return jsonify(brands)

# Endpoint to get models by brand id
@app.route("/brands/<int:id>/models", methods=["GET"])
def get_models_by_brand(id):
    brand_models = [model for model in models if model["brand_id"] == id]
    if not brand_models:
        abort(404)
    return jsonify(brand_models)
@app.route("/models", methods=["GET"])
def get_models():
    greater = request.args.get('greater', type=int)
    lower = request.args.get('lower', type=int)
    filtered_models = models

    # Filter models with average_price greater than 'greater' parameter
    if greater is not None:
        filtered_models = [model for model in filtered_models if model.get("average_price", 0) > greater]

    # Filter models with average_price lower than 'lower' parameter
    if lower is not None:
        filtered_models = [model for model in filtered_models if model.get("average_price", 0) < lower]

    return jsonify(filtered_models)
# Endpoint to create a new brand
@app.route("/brands", methods=["POST"])
def create_brand():
    if not request.json or "name" not in request.json:
        abort(400, description="Missing 'nombre' in request.")
    new_name = request.json["name"]
    # Check if brand name already exists
    existing_brand = next((brand for brand in brands if brand["name"].lower() == new_name.lower()), None)
    if existing_brand is not None:
        return jsonify({"error": "Brand name already in use"}), 400
    # Assuming 'id' should be auto-incremented based on the last id in the list
    new_id = max(brand["id"] for brand in brands) + 1 if brands else 1
    new_brand = {
        "id": new_id,
        "name": new_name,
        # Add 'average_price' if needed, for simplicity it's omitted here
    }
    brands.append(new_brand)
    return jsonify(new_brand), 201


# Endpoint to create a new model for a brand
@app.route("/brands/<int:brand_id>/models", methods=["POST"])
def create_model_for_brand(brand_id):
    # Check if the brand exists
    brand = next((brand for brand in brands if brand["id"] == brand_id), None)
    if not brand:
        return jsonify({"error": "Brand not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    name = request.json.get("name")
    average_price = request.json.get("average_price", None)

    # Validate model name
    if not name:
        return jsonify({"error": "Model name is required"}), 400
    
    # Validate average_price if provided
    if average_price is not None:
        if not isinstance(average_price, (int, float)) or average_price <= 100000:
            return jsonify({"error": "Average price must be a number greater than 100,000"}), 400

    # Check if model name already exists within the brand
    existing_model = next((model for model in models if model["name"].lower() == name.lower() and model.get("brand_id") == brand_id), None)
    if existing_model:
        return jsonify({"error": "Model name already exists within the brand"}), 400
    
    # Assuming 'id' should be auto-incremented based on the last id in the list
    new_id = max(model["id"] for model in models) + 1 if models else 1
    new_model = {
        "id": new_id,
        "brand_id": brand_id,
        "name": name,
        "average_price": average_price
    }
    models.append(new_model)
    return jsonify(new_model), 201


# Endpoint to update a model by id
@app.route("/models/<int:model_id>", methods=["PUT"])
def update_model(model_id):
    model = next((model for model in models if model["id"] == model_id), None)
    if not model:
        return jsonify({"error": "Model not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    average_price = request.json.get("average_price")
    
    # Validate average_price
    if average_price is None or not isinstance(average_price, (int, float)) or average_price <= 100000:
        return jsonify({"error": "Average price must be a number greater than 100,000"}), 400
    
    # Update model's average price
    model["average_price"] = average_price
    return jsonify(model), 200


# Endpoint to get all models
@app.route("/models", methods=["GET"])
def get_all_models():
    return jsonify(models)

if __name__ == "__main__":
    app.run(debug=True)
