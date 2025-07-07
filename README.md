# Personal Finance Tracker App

## 📖 Description

The **Personal Finance Tracker App** is an interactive, text-based Python application designed to help users manage and analyze their spending habits. This project demonstrates proficiency in Python programming, data manipulation with pandas, data visualization with matplotlib, and collaborative development using Git and GitHub.

## 🎯 Objectives

- Build a Python-based interactive application for personal finance management
- Implement comprehensive file handling for importing, editing, and saving transaction data
- Use pandas for efficient data manipulation and analysis
- Create insightful data visualizations using matplotlib
- Practice collaborative development and version control with GitHub

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **CSV** - Data storage format
- **Git/GitHub** - Version control and collaboration

## 📁 Project Structure

```
Personal-Finance-Tracker/
│
├── main.py                    # Main application entry point
├── data_management.py         # Transaction CRUD operations
├── data_analysis.py          # Spending analysis functions
├── visualization.py          # Chart generation functions
├── budget_management.py      # Budget and income management (Extended)
├── sampledata.csv           # Sample transaction data
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── .gitignore             # Git ignore rules
│
└── docks/                 # Documentation
    ├── Basic_Features.md      # Core features documentation
    ├── Extended_Features.md   # Extended features documentation
    ├── Gitflow_Strategy.md   # Git workflow documentation
    └── Lecture_Material.md   # Educational materials
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Personal-Finance-Tracker
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 📝 Usage

### Getting Started

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Main Menu Options**
   ```
   === Personal Finance Tracker ===
   0. Import a CSV File
   1. View All Transactions
   2. View Transactions by Date Range
   3. Add a Transaction
   4. Edit a Transaction
   5. Delete a Transaction
   6. Analyze Spending by Category
   7. Calculate Average Monthly Spending
   8. Show Top Spending Category
   9. Visualize Monthly Spending Trend
   10. Save Transactions to CSV
   11. Exit
   ```

### Sample CSV Format

Your CSV file should have the following structure:
```csv
Date,Category,Description,Amount
2024-10-01,Food,Grocery,50.75
2024-10-02,Rent,Monthly Rent,1200.00
2024-10-02,Utilities,Electricity Bill,60.00
```