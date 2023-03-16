from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy JSON data
products = [
  {
    "description": "Description of Product 1",
    "id": 1,
    "image": "https://via.placeholder.com/150",
    "name": "Product 1",
    "price": 100,
    "rating": 4.5,
    "reviews": [
      {
        "comment": "Great product!",
        "rating": 4,
        "user": "John Doe"
      },
      {
        "comment": "I love it!",
        "rating": 5,
        "user": "Jane Doe"
      }
    ]
  },
  {
    "description": "Description of Product 2",
    "id": 2,
    "image": "https://via.placeholder.com/150",
    "name": "Product 2",
    "price": 200,
    "rating": 3.5,
    "reviews": [
      {
        "comment": "Good product.",
        "rating": 4,
        "user": "John Smith"
      },
      {
        "comment": "Not bad.",
        "rating": 3,
        "user": "Jane Smith"
      }
    ]
  },
  {
    "description": "Description of Product 3",
    "id": 3,
    "image": "https://via.placeholder.com/150",
    "name": "Product 3",
    "price": 150,
    "rating": 4.0,
    "reviews": [
      {
        "comment": "Nice product.",
        "rating": 4,
        "user": "Alice Johnson"
      },
      {
        "comment": "Satisfied.",
        "rating": 4,
        "user": "Bob Johnson"
      }
    ]
  },
    {
    "description": "Description of Product 4",
    "id": 4,
    "image": "https://via.placeholder.com/150",
    "name": "Product 4",
    "price": 250,
    "rating": 3.0,
    "reviews": [
      {
        "comment": "Decent product.",
        "rating": 3,
        "user": "Charlie Brown"
      },
      {
        "comment": "Average quality.",
        "rating": 3,
        "user": "Sally Brown"
      }
    ]
  },
  {
    "description": "Description of Product 5",
    "id": 5,
    "image": "https://via.placeholder.com/150",
    "name": "Product 5",
    "price": 300,
    "rating": 5.0,
    "reviews": [
      {
        "comment": "Excellent product!",
        "rating": 5,
        "user": "David Green"
      },
      {
        "comment": "Top-notch quality.",
        "rating": 5,
        "user": "Ella Green"
      }
    ]
  },
  {
    "description": "Description of Product 6",
    "id": 6,
    "image": "https://via.placeholder.com/150",
    "name": "Product 6",
    "price": 125,
    "rating": 4.2,
    "reviews": [
      {
        "comment": "Good value for money.",
        "rating": 4,
        "user": "Frank White"
      },
      {
        "comment": "Nice design.",
        "rating": 4,
        "user": "Grace White"
      }
    ]
  },
  {
    "description": "Description of Product 7",
    "id": 7,
    "image": "https://via.placeholder.com/150",
    "name": "Product 7",
    "price": 400,
    "rating": 4.7,
    "reviews": [
      {
        "comment": "High-quality product.",
        "rating": 5,
        "user": "Harry Wilson"
      },
      {
        "comment": "Worth the price.",
        "rating": 4,
        "user": "Isla Wilson"
      }
    ]
  },
  {
    "description": "Description of Product 8",
    "id": 8,
    "image": "https://via.placeholder.com/150",
    "name": "Product 8",
    "price": 350,
    "rating": 3.8,
    "reviews": [
      {
        "comment": "Good product, but a bit pricey.",
        "rating": 3,
        "user": "Isla Wilson"
      },
      {
        "comment": "mediocre quality product.",
        "rating": 4,
        "user": "Harry Wilson"
      }
    ]
  }
]

@app.route("/", methods=["GET"])
def home():
    return "<h2>Products</h2>"

# Endpoint to fetch the product list
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)

# Endpoint to fetch product details by ID
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

if __name__ == "__main__":
  app.run(debug=True)

