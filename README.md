♟️ Chess Match Analyzer & Tracker (v4.0 - Final Release)

The Chess Match Analyzer is an advanced command-line interface (CLI) application built with Python and MySQL. Designed for passionate chess players, this tool automates match tracking, parses complex chess game data, and generates granular performance analytics—such as win-rate distributions, opening success rates, and optimal peak-performance hours.

Version 4.0 marks the definitive final release, transitioning the project from a manual logger into a fully automated, API-driven chess telemetry dashboard.

🚀 Key Features

1. Fully Automated API Integration (New in v4.0)

Lichess Live Sync: Dynamically connects to the Lichess.org open API to fetch real-time game history for any public username.

Streamlined Filtering Modes:

Fetch and record only the single most recent match.

Batch-import a custom number of recent matches.

Pull all rated games played Today dynamically using millisecond timestamp calculations.

On-the-Fly PGN Parsing: Integrates chess.pgn to read raw text data streams, automatically extracting critical metadata including opening names, Elo ratings, and exact game results.

2. Bulletproof UX Navigation & State Machine

Multi-Stage Error Mitigation: Hand-crafted input validation routines that completely isolate the application from ValueError crashes or improper data types.

Smart Backtracking: Implements flexible navigational hooks (0, *, or # depending on context) allowing users to safely escape inner loops, reset parameters, or step back to the main menu without dropping the execution state.

3. Deep Analytical & Time-Based Telemetry

Core Analytics: Yields overall counts, precise percentage distributions for Wins/Losses/Draws, and running Elo averages.

Strategic Strengths: Pinpoints your absolute highest-performing piece color (White vs. Black) and isolates your most successful openings.

Chronological Filters: Dedicated reporting subroutines filtering performance metrics across exact intervals: Daily, Weekly, and Monthly scopes.

Peak Performance Clock: Scans historical timestamps to compute the precise hour of the day where your win-rate peaks.

4. Granular Search & Full CRUD Capabilities

Flexible Queries: Search past matches using color filters, specific openings, or rating thresholds backed by relational operators (>, <, =).

Database Management: Direct control handles to safely UPDATE specific attributes or permanently DELETE specific rows via unique relational IDs.

🛠️ Tech Stack & Libraries

Core Language: Python 3.x


Database Engine: MySQL (Leverages native ENUM mapping optimized for direct numerical index lookups).

Database Driver: pymysql


Chess Logic Core: python-chess (for deep PGN stream processing)

Networking: requests (Handling RESTful API calls to Lichess)

📋 Prerequisites & Installation

1. Database Configuration

Ensure you have a local MySQL server instance running via environments like XAMPP or WampServer. The application automatically builds the required schema and table structure upon its first runtime initialization:

Database Name: Chess


Table Name: Chess_analysis


2. Dependency Setup

Install all required Python packages directly via pip:

Bash



pip install pymysql python-chess requests

3. Launching the App

Run the main entry script:

Bash



python chess_project_4.py

🎮 How to Use

Upon startup, you will be greeted with the main command hub:

Plaintext



What do you want to do?

1=> Record a new match

2=> Automatic registration

3=> Statistics presentation and analysis

4=> search for matches

5=> UPDATE a match

6=> Delete a match

0=> Exit

To sync your online matches instantly, choose 2, enter your Lichess handle, select your sync range, and watch the system parse and insert rows seamlessly.

To review your habits, choose 3 to reveal your ultimate peak chess hours and strongest openings.