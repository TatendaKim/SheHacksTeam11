from fastapi import FastAPI
import httpx

"""
This module performs API requests using asynchronous code with 
the aiohttp library. Asynchronous requests allow your application
to make multiple requests concurrently without blocking the 
execution of other tasks. This is beneficial for applications that
need to handle a higher volume of requests or require more responsiveness.
"""


app = FastAPI()

API_URL = "https://api-uct.mukuru.com/taurus/v1/products/price-check"

@app.get("/calculate-remittance/")
async def calculate_remittance_async(pay_in_country: str, pay_out_country: str, pay_in_currency: str, pay_out_currency: str, pay_in_amount: float, product_type: str):
    params = {
        "pay_in_country": pay_in_country,
        "pay_out_country": pay_out_country,
        "pay_in_currency": pay_in_currency,
        "pay_out_currency": pay_out_currency,
        "pay_in_amount": str(pay_in_amount),
        "type": product_type,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        data = response.json()

    pay_out_amount = data.get("pay_out_amount", 0)
    return {"pay_out_amount": pay_out_amount}
