# Personal Finance Decision Tool 💰

## V1 — Basic Personal Finance Management

This is my first personal Python project.

I decided to build it around personal finance because I have a strong interest in finance, investing, and financial decision-making. I believe that understanding how to manage money and make better financial decisions can have a significant impact on reaching personal goals.

The idea is to start with something simple and gradually turn it into a more complete tool for analysing personal finances and comparing different saving and investment scenarios.

## 🎯 What is the project about?

The long-term goal is to create a tool that helps a user understand their financial situation and provides useful calculations and comparisons to support better decision-making.

I don't want to build everything at once. The project will grow as I learn more Python.

For now, V1 focuses on three basic calculations:

### 1. Saving capacity

How much money is left after monthly expenses.

`Saving capacity = Income - Expenses`

### 2. Saving rate

What percentage of monthly income can be saved.

`Saving rate = (Saving capacity / Income) × 100`

### 3. Uninvested savings

How much of the available saving capacity remains after a monthly investment contribution.

`Uninvested savings = Saving capacity - Investment contribution`

## 🛡️ Input validation

The program also checks that:

- Income is greater than 0.
- Expenses are greater than 0.
- Expenses are lower than income.
- Investment contributions are greater than 0.
- Investment contributions do not exceed saving capacity.

## 🧠 What I learned from V1

This is the first time I've built a Python program from an idea of my own rather than simply following an exercise or tutorial.

While building it, I mainly worked on:

- Variables and user input.
- `if` statements and conditions.
- `while` loops.
- Input validation.
- Functions.
- Function arguments.
- `return`.
- Returning multiple values from a function.
- Debugging and finding bugs.
- Refactoring code.
- Organising code into different functional blocks.

One of the most useful parts of the process was learning that getting a program to work is only the first step. Once it worked, I had to go back, find problems, improve the structure and make the code easier to understand.

## 📊 Example

Example:

- Monthly income: €2,200
- Monthly expenses: €750
- Monthly investment contribution: €300

Results:

- Saving capacity: €1,450
- Saving rate: 65.91%
- Uninvested savings: €1,150

## 🔜 V2

The next step will be to introduce **time into the calculations**.

I want to start working with:

- Compound interest.
- Future value.
- Regular contributions.
- Investment time horizons.
- Comparing saving without investing vs investing regularly.

This will be the next step towards the bigger goal of eventually comparing different investment scenarios.

## 📌 How I'm developing it

I'm treating this project as part of my Python learning process.

The idea is simple:

**Learn → Build → Test → Debug → Refactor → Improve**

I'll try to update the project roughly once a week, although this may vary depending on my workload. I work full-time as a teacher, so some weeks I may have less time available for the project.

The goal isn't to build a perfect application quickly. It's to keep learning and make the project better with every version.

## ⚠️ Disclaimer

This is a personal learning project and is not intended to provide personalised financial advice or replace professional financial advice.
