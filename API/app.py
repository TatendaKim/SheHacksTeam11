from fastapi import FastAPI
from fastapi import HTTPException
import httpx
import json

"""
Run FASTAPI server using uvicorn app:app --reload
This module performs API requests using asynchronous code with 
the httpx library. Asynchronous requests allow your application
to make multiple requests concurrently without blocking the 
execution of other tasks. This is beneficial for applications that
need to handle a higher volume of requests or require more responsiveness.
"""


app = FastAPI()

API_URL = "https://api-uct.mukuru.com/taurus/v1"


# Fetch data from an API endpoint
async def fetch_data(endpoint: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint)
        data = response.json()
    return data


# Countries Endpoint
@app.get("/countries/")
async def get_countries():
    countries_endpoint = f"{API_URL}/resources/countries"
    countries_data = await fetch_data(countries_endpoint)
    print(countries_data)
    return countries_data

# Currencies Endpoint
@app.get("/currencies/")
async def get_currencies():
    currencies_endpoint = f"{API_URL}/resources/currencies"
    currencies_data = await fetch_data(currencies_endpoint)
    return currencies_data


# Product Types Endpoint
@app.get("/product-types/")
async def get_product_types():
    product_types_endpoint = f"{API_URL}/resources/product-types"
    product_types_data = await fetch_data(product_types_endpoint)
    return product_types_data


# Remittance Calculator Endpoint
@app.get("/calculate-remittance/")
async def calculate_remittance_async(pay_in_country: str, pay_out_country: str, pay_in_currency: str, pay_out_currency: str, pay_in_amount: float, product_type: str):
    price_check_endpoint = f"{API_URL}/products/price-check"
    params = {
        "pay_in_country": pay_in_country,
        "pay_out_country": pay_out_country,
        "pay_in_currency": pay_in_currency,
        "pay_out_currency": pay_out_currency,
        "pay_in_amount": str(pay_in_amount),
        "type": product_type,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(price_check_endpoint, params=params)
        data = response.json()

    pay_out_amount = data.get("pay_out_amount", 0)
    return {"pay_out_amount": pay_out_amount}