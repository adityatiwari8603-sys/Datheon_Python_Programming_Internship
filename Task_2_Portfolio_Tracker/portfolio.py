"""
DATHEON PYTHON PROGRAMMING INTERNSHIP

Task 2: Investment Portfolio Tracker

Description:
A terminal-based application that tracks
stock investments, calculates portfolio
performance, and exports results to CSV.
"""

import csv
from datetime import datetime
from pathlib import Path


# CSV output location
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "portfolio_summary.csv"


def get_positive_number(message, whole_number=False):
    """Get a valid positive number from the user."""

    while True:
        try:
            user_input = input(message).strip()

            if whole_number:
                value = int(user_input)
            else:
                value = float(user_input)

            if value <= 0:
                print("Please enter a value greater than zero.")
                continue

            if not whole_number:
                import math

                if not math.isfinite(value):
                    print("Please enter a finite number.")
                    continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_stock(portfolio):
    """Add a stock to the portfolio."""

    print("\n========== ADD STOCK ==========")

    ticker = input(
        "Enter stock ticker symbol: "
    ).strip().upper()

    if not ticker:
        print("Ticker symbol cannot be empty.")
        return

    buy_price = get_positive_number(
        "Enter buying price: "
    )

    quantity = get_positive_number(
        "Enter number of shares: ",
        whole_number=True
    )

    current_price = get_positive_number(
        "Enter current market price: "
    )

    if ticker in portfolio:

        previous = portfolio[ticker]

        old_quantity = previous["quantity"]

        total_quantity = old_quantity + quantity

        total_investment = (
            previous["buy_price"] * old_quantity
            + buy_price * quantity
        )

        average_buy_price = (
            total_investment / total_quantity
        )

        portfolio[ticker] = {
            "buy_price": average_buy_price,
            "quantity": total_quantity,
            "current_price": current_price
        }

        print(f"\n{ticker} position updated successfully!")

    else:

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price
        }

        print(f"\n{ticker} added successfully!")


def calculate_portfolio(portfolio):
    """Calculate portfolio performance."""

    if not portfolio:
        print("\nYour portfolio is empty!")
        return []

    print("\n" + "=" * 90)
    print("                         INVESTMENT PORTFOLIO SUMMARY")
    print("=" * 90)

    print(
        f"{'Ticker':<12}"
        f"{'Invested':>15}"
        f"{'Market Value':>18}"
        f"{'Profit/Loss':>18}"
        f"{'Return %':>15}"
    )

    print("-" * 90)

    total_invested = 0
    total_market_value = 0

    results = []

    for ticker, stock in portfolio.items():

        buy_price = stock["buy_price"]
        quantity = stock["quantity"]
        current_price = stock["current_price"]

        invested = buy_price * quantity

        market_value = current_price * quantity

        profit_loss = market_value - invested

        return_percentage = (
            profit_loss / invested
        ) * 100

        total_invested += invested
        total_market_value += market_value

        print(
            f"{ticker:<12}"
            f"{invested:>15.2f}"
            f"{market_value:>18.2f}"
            f"{profit_loss:>18.2f}"
            f"{return_percentage:>14.2f}%"
        )

        results.append({
            "Ticker": ticker,
            "Buy Price": round(buy_price, 2),
            "Quantity": quantity,
            "Current Price": round(current_price, 2),
            "Invested Amount": round(invested, 2),
            "Market Value": round(market_value, 2),
            "Profit/Loss": round(profit_loss, 2),
            "Return Percentage": round(return_percentage, 2)
        })

    total_profit = (
        total_market_value - total_invested
    )

    overall_return = (
        total_profit / total_invested
    ) * 100

    print("-" * 90)

    print(f"Total Investment : {total_invested:.2f}")
    print(f"Market Value     : {total_market_value:.2f}")
    print(f"Total Profit/Loss: {total_profit:.2f}")
    print(f"Overall Return   : {overall_return:.2f}%")

    print("=" * 90)

    return results


def save_to_csv(results):
    """Save portfolio summary to a CSV file."""

    if not results:
        print("\nNo portfolio data available to save.")
        return

    fieldnames = [
        "Date",
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested Amount",
        "Market Value",
        "Profit/Loss",
        "Return Percentage"
    ]

    try:
        with open(
            CSV_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            for stock in results:

                row = {
                    "Date": timestamp,
                    **stock
                }

                writer.writerow(row)

        print("\nPortfolio summary saved successfully!")
        print(f"CSV Location: {CSV_FILE}")

    except (PermissionError, OSError) as error:
        print(f"\nUnable to save CSV: {error}")


def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 45)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Export Portfolio to CSV")
    print("4. Exit")

    print("=" * 45)


def main():
    """Main application function."""

    portfolio = {}

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice (1-4): "
        ).strip()

        if choice == "1":

            add_stock(portfolio)

        elif choice == "2":

            calculate_portfolio(portfolio)

        elif choice == "3":

            results = calculate_portfolio(portfolio)

            save_to_csv(results)

        elif choice == "4":

            if portfolio:

                results = calculate_portfolio(portfolio)

                save_to_csv(results)

            print("\nThank you for using Portfolio Tracker!")
            print("Goodbye!")

            break

        else:

            print("\nInvalid choice! Please select 1-4.")


if __name__ == "__main__":

    try:
        main()

    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted. Goodbye!")