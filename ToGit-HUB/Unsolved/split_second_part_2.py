
def price_this_home(home_price, hurdle_rate, expected_sale_price, holding_months):
    present_value = expected_sale_price / (1 + (hurdle_rate / 12)) ** holding_months
    if present_value > home_price:
        print("Buy this one, junior analyst! It's worth more than it's selling for.")
    elif present_value < home_price:
        print("Don't buy this, as it's offered at a price higher than what it's worth.")
    elif present_value == home_price:
        print(
            "Breakeven case! You can expect to earn exactly your hurdle rate on this deal."
        )


    net_present_value = present_value - home_price
    return net_present_value



# Run the function
npv = price_this_home(
    home_price=100000, expected_sale_price=180000, hurdle_rate=0.10, holding_months=36
)

# Print the npv
print(f"The Expected Profit is: {npv}")
