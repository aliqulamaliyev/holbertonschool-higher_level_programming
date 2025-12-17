#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_file():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    if source == 'json':
        data = read_json_file()
    else:
        data = read_csv_file()

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
        except ValueError:
            data = []

        if not data:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template(
        'product_display.html',
        products=data
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
