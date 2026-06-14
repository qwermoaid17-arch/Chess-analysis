# ♟️ Chess Match Analyzer (Version 3.0)

The **Chess Match Analyzer** is a command-line tool built using **Python** and **MySQL**. It is designed specifically for chess players who want to record their matches, analyze their performance, and generate detailed statistics regarding win rates, best openings, and peak performance hours.

---

## 🚀 Key Features

Version 3.0 introduces a robust data management and analysis system including:

* **Smart Match Recording:** A step-by-step input system (State Machine) that validates user data, preventing erroneous inputs while allowing users to go back (`#`) or exit (`*`) at any stage.
* **Advanced Statistics & Analytics:**
  * Calculates total matches played.
  * Measures wins, losses, and draws along with precise percentage distributions.
  * Provides average opponent rating.
  * Determines your **most successful opening** and **most dominant piece color** (White vs. Black).
* **Time-Based Filtering:** View match counts filtered by specific periods (Today, This Week, This Month).
* **Peak Performance Analysis:** Automatically calculates your **best hour of the day** based on historical win rates.
* **Advanced Search functionality:** Search through historical matches using filters (Color, Opening Name, or Rating thresholds using logical operators `>`, `<`, `=`).
* **Full Data Control (CRUD):** Update records or permanently delete past matches using their unique IDs.

---

## 🛠️ Tech Stack

* **Core Language:** [Python 3.x](https://www.python.org/)
* **Database:** [MySQL](https://www.mysql.com/)
* **Database Connector:** `pymysql` (To bridge Python script execution with a local MySQL server).

---

## 📋 Prerequisites

To run this project locally, ensure you have the following installed:

1. **Python** environment setup on your system.
2. A local database server running MySQL, such as **XAMPP** or **WampServer**.
3. The `pymysql` database adapter installed via terminal:
   ```bash
   pip install pymysql
