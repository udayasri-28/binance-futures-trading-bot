\# Binance Futures Testnet Trading Bot



\## Overview

This project is a simplified trading bot built in Python that interacts with Binance Futures Testnet (USDT-M).



It supports:

\- MARKET orders

\- LIMIT orders

\- BUY and SELL

\- CLI input using argparse

\- Input validation

\- Logging of API requests, responses, and errors



\## Project Structure



trading\_bot/

│

├── bot/

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   ├── logging\_config.py

│

├── cli.py

├── requirements.txt



\## Setup



1\. Create virtual environment:

&nbsp;  python -m venv venv



2\. Activate environment:

&nbsp;  venv\\Scripts\\activate



3\. Install dependencies:

&nbsp;  pip install -r requirements.txt



4\. Create .env file:

&nbsp;  API\_KEY=your\_api\_key

&nbsp;  API\_SECRET=your\_secret\_key

&nbsp;  BASE\_URL=https://testnet.binancefuture.com



\## Run MARKET Order



python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002



\## Run LIMIT Order



python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000



\## Logging



Logs are saved in:

trading\_bot.log



\## Assumptions



\- Using Binance Futures Testnet (USDT-M)

\- GTC timeInForce for LIMIT orders

