# CodeAlpha Stock Portfolio Tracker

A simple, clean, and interactive console-based Stock Portfolio Tracker created in Python for **CodeAlpha Python Programming Internship — Task 2**.

---

## Description

The **Stock Portfolio Tracker** allows users to track their stock investments using predefined, hardcoded stock prices. Users can select available stock symbols, specify quantities, calculate individual and total investment values, view a structured summary in the console, and automatically save the final portfolio summary to a `portfolio.txt` text file.

---

## Features

- **Hardcoded Stock Prices**: Uses a built-in dictionary with standard sample stock prices.
- **User Stock Selection**: Choose from available popular stock symbols with case-insensitive input.
- **Quantity Input**: Enter desired number of shares for each stock.
- **Investment Calculation**: Automatically calculates `Stock Price × Quantity` for each entry.
- **Multiple Stock Entries**: Easily add multiple stocks to build a comprehensive portfolio.
- **Portfolio Summary**: Cleanly formatted breakdown of all holdings in the console.
- **Total Investment Calculation**: Accurately sums all holdings to show total portfolio value.
- **TXT File Saving**: Automatically saves the final portfolio report to `portfolio.txt`.
- **Robust Input Validation**: Handles invalid stock symbols, non-numeric quantities, zero, and negative values gracefully without crashing.

---

## Technologies

- **Python**
- **Python Standard Library** (no external packages or dependencies required)

---

## Python Concepts Used

- **Dictionaries**: For storing and retrieving hardcoded stock prices (`symbol: price`).
- **Lists & Tuples**: For tracking transaction records and portfolio history.
- **Loops (`while` & `for`)**: For repeating user input workflows and iterating over portfolio items.
- **Conditional Statements (`if-else`)**: For checking stock existence and menu branching.
- **User Input & String Methods (`strip()`, `upper()`, `lower()`)**: For sanitized input handling.
- **Arithmetic Operations**: For calculating investment values and total sums.
- **Exception Handling (`try-except ValueError`)**: For validating numeric inputs.
- **File Handling (`open()` with context manager)**: For saving portfolio summaries to `portfolio.txt`.

---

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd CodeAlpha_StockPortfolio
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Example Program Output

```text
================================
     STOCK PORTFOLIO TRACKER    
================================

Available Stocks:
AAPL - $180
TSLA - $250
GOOG - $150
MSFT - $420
AMZN - $180

Enter stock symbol: AAPL
Enter quantity: 5

AAPL: 5 × $180 = $900

Add another stock? (y/n): y

Enter stock symbol: TSLA
Enter quantity: 2

TSLA: 2 × $250 = $500

Add another stock? (y/n): n

================================
        PORTFOLIO SUMMARY       
================================

AAPL: 5 × $180 = $900
TSLA: 2 × $250 = $500
--------------------------------
Total Investment: $1400
================================

Portfolio saved to portfolio.txt
```

---

## Important Note

> The stock prices used in this project are hardcoded sample values for educational purposes and are not live market prices.

---

## Internship

**CodeAlpha Python Programming Internship — Task 2**
