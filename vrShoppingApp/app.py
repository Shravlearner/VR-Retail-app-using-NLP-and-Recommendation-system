from flask import Flask, render_template

# Create the Flask app instance
app = Flask(__name__)

# Route to render the index page
@app.route('/')
def home():
    return render_template('index.html')  # Assuming index.html is inside the templates folder

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
