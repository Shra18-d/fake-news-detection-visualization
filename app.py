from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from viz import generate_plots

app = Flask(__name__)

# Load dataset
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["class"] = 0
true["class"] = 1

data = pd.concat([fake, true])
data = data.sample(frac=1)

x = data["title"]
y = data["class"]

vectorizer = TfidfVectorizer(stop_words="english")
x_vector = vectorizer.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x_vector, y, test_size=0.25, random_state=42
)

model = PassiveAggressiveClassifier(max_iter=1000)
model.fit(x_train, y_train)
# Predict test data
y_pred = model.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Convert into percentage
accuracy = round(accuracy * 100, 2)

# Generate visualization plots
generate_plots(fake, true, accuracy)


def is_nonsense(text):
    text = text.strip()

    # condition 1: too short
    if len(text) < 5:
        return True

    # condition 2: no alphabets
    if not any(char.isalpha() for char in text):
        return True

    # condition 3: too many random characters
    if len([w for w in text.split() if len(w) > 2]) < 2:
        return True

    return False


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/stats')
def stats():
    """Display data visualization and statistics"""
    return render_template("stats.html", accuracy=accuracy)


@app.route('/news', methods=['POST'])
def news():

    headline = request.form['news']
    text = headline.lower()

    input_data = vectorizer.transform([headline])
    prediction = model.predict(input_data)

    # ---------------- LOGIC WITH ELIF ---------------- #

    if is_nonsense(text):

        result = "⚠ Unable to verify news credibility"
        color = "orange"

    elif prediction[0] == 0:

        result = "⚠ Fake News Detected"
        color = "red"

    else:

        result = "✅ Real News Detected"
        color = "lime"

    return render_template(
        "index.html",
        prediction=result,
        textcolor=color,
        headline=headline,
        accuracy=accuracy
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
