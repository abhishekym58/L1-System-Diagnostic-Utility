# Automated L1 System Diagnostic Utility

## Overview
A Python-based lightweight diagnostic tool designed to automate the first 5 minutes of a Level 1 IT Support call. This script instantly profiles the host system, verifies external network connectivity, and exports the results into a timestamped log file that can be attached to IT Service Management (ITSM) ticketing systems (like Jira or ServiceNow) for faster issue resolution.

## Core Features
* **System Profiling:** Automatically retrieves the Operating System version, system architecture, and available C: Drive disk space to check for common storage bottlenecks.
* **Network Diagnostics:** Executes an automated 4-packet ping test to Google Public DNS (8.8.8.8) to verify outbound internet connectivity and measure latency.
* **Automated Logging:** Generates a clean, timestamped `.txt` log file in the local directory without requiring administrative privileges.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `platform`, `subprocess`, `shutil`, `datetime` (Built-in, no external dependencies required)
* **Environment:** Windows OS, Command Line / PowerShell

## How to Use
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/abhishekym58/L1-System-Diagnostic-Utility.git](https://github.com/abhishekym58/L1-System-Diagnostic-Utility.git)