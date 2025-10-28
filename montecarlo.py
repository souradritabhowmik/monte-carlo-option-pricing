from monte_carlo_option_pricing import MonteCarloOptionPricer

# Parameters
S0 = 100      # Initial stock price
K = 105       # Strike price
T = 1         # Time to maturity (1 year)
r = 0.05      # Risk-free interest rate
sigma = 0.2   # Volatility
simulations = 100000

# Initialize pricer
pricer = MonteCarloOptionPricer(S0, K, T, r, sigma, simulations)

# Get option prices
call_price = pricer.price_option("call")
put_price = pricer.price_option("put")

print(f"🎉 Call Price: {call_price:.2f}")
print(f"🎉 Put Price: {put_price:.2f}")
