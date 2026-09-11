from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/predict")
def predict():
    image = request.files["image"]

    # Run model
    # mask = model.predict(image)

    # Save images
    # ...

    return render_template(
        "result.html",
        original="/static/uploads/original.png",
        mask="/static/results/mask.png"
    )


if __name__ == "__main__":
    app.run(debug=True)