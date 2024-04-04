from flask import Flask, render_template, request, jsonify
import json
import math

app = Flask(__name__)

# Load book data from JSON file
with open('books.json', 'r') as f:
    books = json.load(f)

# Pagination function
def paginate(items, page, per_page):
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    return items[start_index:end_index]

@app.route('/')
def index():
    # Get page number from query parameter, default to 1
    page = int(request.args.get('page', 1))
    # Number of items per page
    per_page = 10
    # Calculate total number of pages
    total_pages = math.ceil(len(books) / per_page)
    # Paginate the books
    paginated_books = paginate(books, page, per_page)
    return render_template('index.html', books=paginated_books, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
