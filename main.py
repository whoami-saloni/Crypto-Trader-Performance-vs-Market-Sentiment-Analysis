# ---------------- IMPORT MODULES ----------------
from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.feature_engineering import create_features

from src.analysis import (
    sentiment_analysis,
    trader_analysis,
    risk_and_behavior_analysis
)

from src.visualisation import (
    plot_pnl_distribution,
    plot_roi,
    plot_win_rate,
    plot_risk_analysis,
    plot_volatility,
    plot_direction_bias,
    plot_trader_performance,
    plot_top_traders,
    plot_strategy_comparison
)
from src.strategy import strategy_analysis


# ---------------- MAIN PIPELINE ----------------
def run_pipeline():

    print("\n🚀 Starting Crypto Analysis Pipeline...\n")

    # -------- LOAD DATA --------
    trades, sentiment = load_data("Data/historical_data.csv", "Data/fear_greed_index.csv")
    print("✅ Data Loaded")

    # -------- PREPROCESS --------
    df = preprocess_data(trades,sentiment)
    print("✅ Preprocessing Done")


    # -------- FEATURE ENGINEERING --------
    df = create_features(df)
    print("✅ Features Created")

    # -------- ANALYSIS --------
    sentiment_result = sentiment_analysis(df)
    trader_stats = trader_analysis(df)
    strategy_results = strategy_analysis(df)
    risk_analysis, volatility, direction_bias = risk_and_behavior_analysis(df)

    print("\n📊 Sentiment Analysis:\n", sentiment_result)
    print("\n🏆 Strategy Results:\n", strategy_results)

    # -------- VISUALIZATION --------
    print("\n📈 Generating Visualizations...\n")

    plot_pnl_distribution(df)
    plot_roi(df)
    plot_win_rate(df)

    plot_risk_analysis(risk_analysis)
    plot_volatility(volatility)
    plot_direction_bias(direction_bias)

    plot_trader_performance(trader_stats)
    plot_top_traders(trader_stats)

    plot_strategy_comparison(strategy_results)

    print("\n✅ Pipeline Completed Successfully!")


# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    run_pipeline()