from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "FinOps CI/CD Demo",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/cost")
def cost():
    return jsonify({
        "service": "Amazon EC2",
        "monthly_cost": 125.50,
        "currency": "USD"
    })


@app.route("/budget")
def budget():
    return jsonify({
        "monthly_budget": 500,
        "current_spend": 350,
        "remaining": 150
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
