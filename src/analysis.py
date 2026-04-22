def sentiment_analysis(df):
    return df.groupby('classification').agg({
        'net_pnl': ['mean', 'sum'],
        'is_profit': 'mean',
        'roi': 'mean'
    })


def trader_analysis(df):
    stats = df.groupby('account').agg({
        'net_pnl': 'sum',
        'is_profit': 'mean',
        'roi': 'mean',
        'position_size': 'mean'
    }).reset_index()

    stats.columns = ['account','total_pnl','win_rate','avg_roi','avg_size']
    return stats

# ---------------- RISK & BEHAVIOR ----------------
def risk_and_behavior_analysis(df):

    risk_analysis = df.groupby('classification').agg({
        'position_size': 'mean',
        'net_pnl': 'mean'
    })

    volatility = df.groupby('classification')['net_pnl'].std()

    direction_bias = df.groupby(['classification', 'side']).size().unstack()

    return risk_analysis, volatility, direction_bias