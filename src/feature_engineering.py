def create_features(df):

    df['net_pnl'] = df['pnl'] - df['fee']
    df['position_size'] = df['size_usd']
    df['roi'] = df['net_pnl'] / (df['position_size'] + 1e-6)
    df['is_profit'] = (df['net_pnl'] > 0).astype(int)

    df['direction'] = df['side'].str.upper().map({'BUY': 1, 'SELL': -1})

    df['abs_pnl'] = df['net_pnl'].abs()

    sentiment_map = {
        'Extreme Fear': -2,
        'Fear': -1,
        'Neutral': 0,
        'Greed': 1,
        'Extreme Greed': 2
    }

    df['sentiment_score'] = df['classification'].map(sentiment_map)

    df['position_change'] = df.groupby('account')['start_position'].diff()

    return df