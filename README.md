# Crypto-Trader-Performance-vs-Market-Sentiment-Analysis
Crypto Trader Performance vs Market Sentiment Analysis
# Overview

This project builds an end-to-end data science pipeline to analyze how Bitcoin market sentiment (Fear & Greed Index) influences trader performance.

Using real trading data, we uncover patterns in profitability, risk behavior, and strategy performance, and derive actionable insights for smarter trading.

# Objectives
Analyze relationship between market sentiment and trading performance
Evaluate profitability, risk, and win rate
Identify top-performing traders
Compare trading strategies
Build a modular, production-ready pipeline

# Datasets
## 1. Bitcoin Market Sentiment 
[Download Dataset](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing) <br>
date
classification → Extreme Fear, Fear, Neutral, Greed, Extreme Greed
value → Sentiment score (0–100)
## 2. Trader Data (Hyperliquid)  
[Download Dataset](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing) <br>
account → Trader wallet
execution_price → Trade price
size_usd → Trade size
side → BUY / SELL
start_position → Existing position
pnl → Profit/Loss
fee → Transaction cost
date → Trade date

# Pipeline Workflow
## 1. Data Loading

Load trading and sentiment datasets

## 2. Preprocessing
Clean column names
Convert timestamps
Merge datasets on date
Handle missing values
## 3. Feature Engineering
Net PnL
ROI (Return on Investment)
Win Rate Indicator
Position Size
Sentiment Score Encoding
Position Change Tracking

# Analysis
## Sentiment-Based Analysis
PnL (mean & total)
ROI comparison
Win rate across sentiment
## Risk Analysis
Position size behavior
Absolute PnL (risk proxy)
Volatility (standard deviation)
## Trader Analysis
Total PnL per trader
Average ROI
Win rate
Top trader identification

# Strategy Evaluation

The following strategies were implemented and compared:

📈 Greed Strategy<br>
📉 Fear Strategy<br>
⚖️ Low Risk Strategy (based on position size)<br>
🏆 Copy Trading Strategy (top traders)<br>
📊 Visualizations<br>
📦 PnL Distribution (Boxplot)<br>
📈 ROI by Sentiment<br>
🎯 Win Rate Analysis<br>
⚖️ Risk vs Return<br>
🔄 Buy vs Sell Behavior<br>
🏆 Top Traders Performance<br>
📊 Strategy Comparison<br>
# Key Insights
Greed markets yield higher profitability and ROI<br>
Fear markets are more volatile and unpredictable<br>
Traders take larger positions during bullish sentiment<br>
High ROI traders differ from high-profit traders<br>
Copy trading significantly outperforms baseline strategies<br>
# Recommendations
Trade more actively during Greed phases<br>
Reduce exposure during Fear markets<br>
Focus on ROI, not just total PnL<br>
Use copy trading strategies for consistency<br>
Apply risk management via position sizing<br>

# Tech Stack
Python<br>
Pandas, NumPy<br>
Matplotlib, Seaborn<br>


# How to Run
```python
## Clone repository
 git clone https://github.com/your-username/crypto-sentiment-analysis.git

cd crypto-sentiment-analysis

## Create virtual environment
python3 -m venv venv
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Run pipeline
python main.py
```

# Notes
Place datasets inside /data/ folder<br>
# Future Improvements
Add Sharpe Ratio & Drawdown<br>
Build predictive ML model<br>
Real-time sentiment integration<br>
Portfolio optimization<br>
# Author

Saloni Sahal<br>
M.Tech CSE | AI/ML & Data Science<br>
📧 salonisahal15@gmail.com<br>

# Why This Project Stands Out
End-to-end modular pipeline<br>
Combines sentiment + trading data<br>
Focus on real-world strategy insights<br>
Clean, scalable architecture<br>
# Final Note

This project demonstrates how market psychology (fear vs greed) directly impacts trading behavior and how data-driven strategies can improve trading outcomes.

# Want to go further?

You can easily extend this project with:<br>

📊 Interactive dashboard (Streamlit)<br>
🤖 ML prediction model<br>
☁️ Deployment (cloud / API)<br>
