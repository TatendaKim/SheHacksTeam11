from remittance_calculator import calculate_remittance
import asyncio

"""
An endpoint/route
* The point of entry in a communication channel,
when two systems are interacting.
* It refers to touchpoints of the communication between an API and a server.
"""


if __name__ == "__main__":
    pay_in_country = "US"
    pay_out_country = "IN"
    pay_in_currency = "USD"
    pay_out_currency = "INR"
    pay_in_amount = 100
    product_type = "standard"


    # Asynchronous calculation
    loop = asyncio.get_event_loop()
    async_remittance_cost = loop.run_until_complete(
        calculate_remittance(pay_in_country, pay_out_country, pay_in_currency, pay_out_currency, pay_in_amount, product_type)
    )
    print("Asynchronous Remittance Cost:", async_remittance_cost)

