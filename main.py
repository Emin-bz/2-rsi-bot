# Install the required library with: pip install ccxt
import ccxt
import time

# Insert API keys here
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

# Configure exchange (e.g., Binance) using CCXT
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})

# Trading parameters
symbol = 'BTC/USDT'  # Trading pair
rsi_period = 14      # RSI period for calculation
overbought = 70      # Overbought level
oversold = 30        # Oversold level
trade_amount = 0.001 # Amount to buy/sell

# RSI calculation function
def calculate_rsi(prices):
    gains = [prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1]]
    losses = [-1 * (prices[i] - prices[i - 1]) for i in range(1, len(prices)) if prices[i] < prices[i - 1]]
    
    average_gain = sum(gains) / rsi_period if gains else 0
    average_loss = sum(losses) / rsi_period if losses else 0
    
    if average_loss == 0:
        return 100  # Max RSI value if no losses (only gains)
    
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Function to fetch historical prices
def fetch_prices():
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=rsi_period + 1)
    return [x[4] for x in ohlcv]  # Close prices

# Main trading loop
def main():
    print("Starting the RSI trading bot...")
    while True:
        try:
            # Fetch historical price data
            prices = fetch_prices()
            if len(prices) < rsi_period:
                print("Not enough data to calculate RSI.")
                time.sleep(60)
                continue
            
            # Calculate RSI
            rsi = calculate_rsi(prices)
            print(f"Current RSI: {rsi}")
            
            # Trading logic based on RSI
            if rsi < oversold:
                print("Signal: BUY")
                # Place a buy order (market order)
                exchange.create_market_buy_order(symbol, trade_amount)
            elif rsi > overbought:
                print("Signal: SELL")
                # Place a sell order (market order)
                exchange.create_market_sell_order(symbol, trade_amount)
            else:
                print("Signal: HOLD")
            
            # Wait before the next iteration
            time.sleep(60)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)

# Run the bot
if __name__ == "__main__":
    main()
