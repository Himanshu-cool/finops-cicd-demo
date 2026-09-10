@app.route("/budget")
def budget():
    return jsonify({
        "monthly_budget": 500,
        "current_spend": 350,
        "remaining": 150
    })

