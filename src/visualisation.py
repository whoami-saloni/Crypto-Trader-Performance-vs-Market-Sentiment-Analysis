import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

def save_plot(fig_name):
    output_dir = "outputs/plots"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"{fig_name}.png")
    plt.savefig(file_path, bbox_inches='tight')
    print(f"✅ Saved: {file_path}")
# ---------------- PnL DISTRIBUTION ----------------
def plot_pnl_distribution(df):
    plt.figure()
    sns.boxplot(x='classification', y='net_pnl', data=df)
    plt.title("PnL Distribution by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Net PnL")
    plt.xticks(rotation=30)
    plt.tight_layout()
    save_plot("pnl_distribution")
    plt.close()
    plt.show()


# ---------------- ROI ----------------
def plot_roi(df):
    plt.figure()
    df.groupby('classification')['roi'].mean().plot(kind='bar')
    plt.title("Average ROI by Sentiment")
    plt.ylabel("ROI")
    plt.xticks(rotation=30)
    plt.tight_layout()
    save_plot("Average ROI by Sentiment")
    plt.close()
    plt.show()


# ---------------- WIN RATE ----------------
def plot_win_rate(df):
    plt.figure()
    df.groupby('classification')['is_profit'].mean().plot(kind='bar')
    plt.title("Win Rate by Sentiment")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=30)
    plt.tight_layout()
    save_plot("Win Rate by Sentiment")
    plt.close()
    plt.show()


# ---------------- RISK ANALYSIS ----------------
def plot_risk_analysis(risk_analysis):
    plt.figure()
    risk_analysis.plot(kind='bar')
    plt.title("Risk Metrics by Sentiment")
    plt.ylabel("Value")
    plt.xticks(rotation=30)
    plt.tight_layout()
    save_plot("Risk Metrics by Sentiment")
    plt.close()
    plt.show()


# ---------------- VOLATILITY ----------------
def plot_volatility(volatility):
    plt.figure()
    volatility.plot(kind='bar')
    plt.title("PnL Volatility by Sentiment")
    plt.ylabel("Std Dev of PnL")
    plt.xticks(rotation=30)
    plt.tight_layout()
    save_plot("PnL Volatility by Sentiment")
    plt.close()
    plt.show()


# ---------------- BUY/SELL BEHAVIOR ----------------
def plot_direction_bias(direction_bias):
    plt.figure()
    direction_bias.plot(kind='bar', stacked=True)
    plt.title("Buy vs Sell Behavior by Sentiment")
    plt.ylabel("Number of Trades")
    plt.xticks(rotation=30)
    plt.tight_layout()
    save_plot("Buy vs Sell Behavior by Sentiment")
    plt.close()
    plt.show()


# ---------------- TRADER PERFORMANCE ----------------
def plot_trader_performance(trader_stats):
    plt.figure()
    sns.scatterplot(data=trader_stats, x='avg_roi', y='total_pnl')
    plt.title("Trader Performance: ROI vs Total PnL")
    plt.xlabel("Average ROI")
    plt.ylabel("Total PnL")
    plt.tight_layout()
    save_plot("Trader Performance: ROI vs Total PnL")
    plt.close()
    plt.show()


# ---------------- TOP TRADERS ----------------
def plot_top_traders(trader_stats, top_n=10):
    plt.figure()
    top = trader_stats.sort_values(by='total_pnl', ascending=False).head(top_n)
    sns.barplot(x='account', y='total_pnl', data=top)
    plt.title(f"Top {top_n} Traders by PnL")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_plot("Top Traders by PnL")
    plt.close()
    plt.show()


# ---------------- STRATEGY COMPARISON ----------------
def plot_strategy_comparison(strategy_results):
    plt.figure()

    strategies = [
        "Greed",
        "Fear",
        "Low Risk",
        "Copy Trading"
    ]

    values = [
        strategy_results['greed_pnl'],
        strategy_results['fear_pnl'],
        strategy_results['low_risk_pnl'],
        strategy_results['copy_trading_pnl']
    ]

    plt.bar(strategies, values)
    plt.title("Strategy Performance Comparison")
    plt.ylabel("Total Net PnL")
    plt.tight_layout()
    save_plot("Strategy Performance Comparison")
    plt.close()
    plt.show()