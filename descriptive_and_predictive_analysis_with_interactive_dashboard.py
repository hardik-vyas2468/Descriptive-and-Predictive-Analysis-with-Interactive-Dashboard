# -*- coding: utf-8 -*-
"""Descriptive and Predictive Analysis with Dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://drive.google.com/drive/u/0/my-drive
"""

pip install dash plotly pandas

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the data
data_path = 'sample_sales_dataset'
df = pd.read_csv(data_path, encoding='ISO-8859-1')

# Initialize the Dash app
app = Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Sales Dashboard"),

    dcc.Dropdown(
        id='status-filter',
        options=[{'label': status, 'value': status} for status in df['STATUS'].unique()],
        value=df['STATUS'].unique().tolist(),
        multi=True,
        placeholder="Select Order Status"
    ),

    dcc.Graph(id='sales-by-product'),

    dcc.Graph(id='order-status-distribution'),

    dcc.Graph(id='quantity-vs-sales')
])

# Callback for updating the bar chart based on the selected status
@app.callback(
    Output('sales-by-product', 'figure'),
    Input('status-filter', 'value')
)
def update_sales_by_product(selected_status):
    filtered_df = df[df['STATUS'].isin(selected_status)]
    fig = px.bar(filtered_df, x='PRODUCTLINE', y='SALES', color='PRODUCTLINE',
                 title='Total Sales by Product Line')
    return fig

# Callback for updating the pie chart based on the selected status
@app.callback(
    Output('order-status-distribution', 'figure'),
    Input('status-filter', 'value')
)
def update_order_status_distribution(selected_status):
    filtered_df = df[df['STATUS'].isin(selected_status)]
    fig = px.pie(filtered_df, names='STATUS', title='Order Status Distribution')
    return fig

# Callback for updating the scatter plot based on the selected status
@app.callback(
    Output('quantity-vs-sales', 'figure'),
    Input('status-filter', 'value')
)
def update_quantity_vs_sales(selected_status):
    filtered_df = df[df['STATUS'].isin(selected_status)]
    fig = px.scatter(filtered_df, x='QUANTITYORDERED', y='SALES', color='PRODUCTLINE',
                     title='Quantity Ordered vs Total Sales')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

