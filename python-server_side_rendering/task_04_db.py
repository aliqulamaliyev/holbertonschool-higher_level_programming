#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
    except Exception:
        return None

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template(
                'product_display.html',
                error="Database error"
            )
    else:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

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
