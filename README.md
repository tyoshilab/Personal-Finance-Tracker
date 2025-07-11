# Personal Finance Tracker App

## 📖 Description

The **Personal Finance Tracker App** is an interactive, text-based Python application designed to help users manage and analyze their personal finances. This comprehensive application includes transaction management, spending analysis, budget management, and data visualization capabilities. The project demonstrates proficiency in Python programming, data manipulation with pandas, data visualization with matplotlib, and collaborative development using Git and GitHub.

## 🎯 Objectives

- Build a Python-based interactive application for comprehensive personal finance management
- Implement transaction CRUD operations with robust file handling
- Provide spending analysis and budget management with alerts and suggestions
- Create insightful data visualizations for financial trends and patterns
- Use pandas for efficient data manipulation and analysis
- Practice collaborative development and version control with GitHub

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization and charting
- **datetime** - Date and time handling
- **CSV** - Data storage format
- **Git/GitHub** - Version control and collaboration

## 📁 Project Structure

```
Personal-Finance-Tracker/
│
├── main.py                    # Main application entry point
├── data_management.py         # Transaction CRUD operations and file handling
├── data_analysis.py          # Spending analysis and statistical functions
├── visualization.py          # Chart generation and data visualization
├── budget_management.py      # Budget setting, income tracking, and alerts
├── menu_screen.py            # Reusable menu system for UI navigation
├── transactions.csv          # Main transaction data file
├── sampledata.csv           # Sample transaction data for testing
├── development_tasks.csv    # Project development task tracking
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── data_flow_diagram.md    # Data flow visualization documentation
│
└── docks/                   # Documentation directory
    ├── Basic_Features.md        # Core features documentation
    ├── Extended_Features.md     # Extended features documentation
    ├── Gitflow_Strategy.md     # Git workflow documentation
    └── Lecture_Material.md     # Educational materials
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/tyoshilab/Personal-Finance-Tracker.git
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