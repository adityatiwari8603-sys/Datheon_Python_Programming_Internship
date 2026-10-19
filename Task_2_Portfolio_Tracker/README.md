
# Investment Portfolio Tracker

## Datheon Python Programming Internship — Task 2

### Project Overview

The Investment Portfolio Tracker is a Python command-line application that helps users monitor stock investments, calculate portfolio performance, and export investment summaries to a CSV file.

### Features

* Add stocks using ticker symbols.
* Enter purchase price, quantity, and current market price.
* Calculate total invested amount and current market value.
* Calculate profit or loss for each stock.
* Display percentage returns.
* Update existing stock positions using weighted-average purchase prices.
* Export portfolio summaries to CSV.
* Validate user input and handle file-saving errors.

### Technologies Used

* Python 3
* CSV module
* datetime module
* pathlib module

### How to Run

Open a terminal in the internship project's main folder and execute:

```powershell
python .\Task_2_Portfolio_Tracker\portfolio.py
```

### Menu Options

1. **Add Stock:** Enter stock details.
2. **View Portfolio:** Display investment performance.
3. **Export Portfolio to CSV:** Save results to `portfolio_summary.csv`.
4. **Exit:** Save the current portfolio, if it contains stocks, and close the application.

### Example

Sample stock:

* Ticker: AAPL
* Buying price: 150
* Quantity: 10
* Current price: 180

Results:

* Invested amount: 1500
* Market value: 1800
* Profit: 300
* Return: 20%

*All prices are entered manually. The application does not retrieve live stock prices.*

### Output Files

* `portfolio.py` — Main application
* `portfolio_summary.csv` — Exported investment summary

### Author

Developed as part of the Datheon Python Programming Internship.
