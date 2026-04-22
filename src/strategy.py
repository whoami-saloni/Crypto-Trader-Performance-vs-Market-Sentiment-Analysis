from src.analysis import trader_analysis
def strategy_analysis(df):

    # ---------------- SENTIMENT STRATEGIES ----------------
    greed = df[df['classification'].str.contains('Greed')]
    fear = df[df['classification'].str.contains('Fear')]

    greed_pnl = greed['net_pnl'].sum()
    fear_pnl = fear['net_pnl'].sum()

    # ---------------- LOW RISK STRATEGY ----------------
    low_risk = df[df['position_size'] < df['position_size'].quantile(0.75)]
    low_risk_pnl = low_risk['net_pnl'].sum()

    # ---------------- COPY TRADING STRATEGY ----------------
    trader_stats = trader_analysis(df)

    top_accounts = (
        trader_stats
        .sort_values(by='total_pnl', ascending=False)
        .head(10)['account']
    )

    copy_trading = df[df['account'].isin(top_accounts)]
    copy_trading_pnl = copy_trading['net_pnl'].sum()

    # ---------------- RETURN EVERYTHING ----------------
    return {
        "greed_pnl": greed_pnl,
        "fear_pnl": fear_pnl,
        "low_risk_pnl": low_risk_pnl,
        "copy_trading_pnl": copy_trading_pnl,

        # Optional (for visualization/dashboard)
        "greed_df": greed,
        "fear_df": fear,
        "low_risk_df": low_risk,
        "copy_trading_df": copy_trading
    }