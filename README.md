# RSI Trading Bot

This is a simple cryptocurrency trading bot built in Python that uses the **Relative Strength Index (RSI)** as its primary indicator. The bot connects to a cryptocurrency exchange (e.g., Binance) via the **CCXT** library and makes trades based on RSI levels, aiming to buy in oversold conditions and sell in overbought conditions.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [Get More](#get-more)

---

## Introduction

This bot is designed as an educational tool for those interested in automated trading. It uses the **RSI (Relative Strength Index)**, a momentum-based indicator, to generate buy and sell signals. When the RSI falls below a certain level, it suggests the asset may be oversold, triggering a buy signal. Conversely, if the RSI rises above a threshold, it may be overbought, leading to a sell signal.

## Features

- Calculates the RSI based on a configurable period (default: 14)
- Generates buy and sell signals based on customizable RSI thresholds
- Connects to multiple crypto exchanges via the CCXT library
- Simple and easy-to-understand code, suitable for beginners

## Requirements

- Python 3.x
- `ccxt` library (Install with `pip install ccxt`)

## Installation

1. Clone or download this repository.
2. Install the required Python package:

    ```bash
    pip install ccxt
    ```

## Configuration

1. Open the bot script (`rsi_bot.py`).
2. Enter your exchange API keys:

    ```python
    API_KEY = "YOUR_API_KEY"
    API_SECRET = "YOUR_API_SECRET"
    ```

3. Customize trading parameters as needed:
    - **symbol**: The trading pair to use, e.g., `'BTC/USDT'`
    - **rsi_period**: Period for the RSI calculation (default is 14)
    - **overbought** and **oversold**: RSI levels to trigger sell and buy signals, respectively
    - **trade_amount**: Amount to buy or sell per trade

## How It Works

1. The bot fetches recent historical prices for the chosen trading pair.
2. It calculates the RSI based on the specified period.
3. It generates a **buy** signal if the RSI falls below the oversold threshold and a **sell** signal if it rises above the overbought threshold.
4. The bot places market orders based on the signal, holding if neither threshold is reached.

## Usage

1. Run the bot:

    ```bash
    python rsi_bot.py
    ```

2. Monitor the console output for **buy**, **sell**, and **hold** signals.

3. The bot checks for trading signals every 60 seconds.

## Disclaimer

This bot is intended for educational purposes only. Cryptocurrency trading is highly risky and may not be suitable for all investors. Use this bot with caution and at your own risk, and only trade with funds you can afford to lose.

---

## Get More

Interested in learning how to deploy this bot properly and maximize its potential? For a step-by-step deployment guide, advanced strategies, and exclusive trading insights, join me on [Patreon](https://www.patreon.com/YourPatreonName)!

As a Patreon member, you’ll gain access to:
- Detailed deployment tutorials
- Advanced bot strategies for real market conditions
- Live Q&A sessions and a private community for hands-on support

Happy trading!
