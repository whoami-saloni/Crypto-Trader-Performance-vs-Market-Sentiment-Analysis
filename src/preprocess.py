import pandas as pd
def preprocess_data(trades, sentiment):
    trades.columns = trades.columns.str.strip().str.lower().str.replace(" ", "_")

# Drop unwanted columns
    trades = trades.drop(columns=[
    'coin', 'size_tokens', 'direction',
    'transaction_hash', 'order_id', 'trade_id',
    'timestamp', 'crossed'
    ])

    # ---------------- CLEAN TRADES ----------------
    trades.columns = trades.columns.str.lower().str.replace(" ", "_")

    trades['timestamp_ist'] = pd.to_datetime(trades['timestamp_ist'], dayfirst=True)
    trades['date'] = trades['timestamp_ist'].dt.date

# Rename columns for consistency
    trades.rename(columns={
    'closed_pnl': 'pnl',
    'size_usd': 'size_usd'
    }, inplace=True)

# ---------------- CLEAN SENTIMENT ----------------
    sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# Keep only required columns
    sentiment = sentiment[['date', 'classification', 'value']]
    trades = trades.drop(columns=['timestamp_ist'])
    df = trades.merge(sentiment, on='date', how='left')
    df = df.dropna(subset=['classification'])
    df.info()
    df.isnull().sum()
    df.describe()
    df.duplicated().sum()

    return df