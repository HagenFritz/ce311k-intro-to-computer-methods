# Interactive Coding Session 01

# **Option 1: Bank Account (Finance / Transactions)**
### **Class: `BankAccount`**
A simple banking system that tracks deposits, withdrawals, and interest.

### **Attributes**
- `account_holder` (str) → Name of the account holder
- `account_number` (str) → Unique account identifier
- `account_type` (str) → Checking, savings, etc.
- `__balance` (float) → Private variable for account balance (encapsulation)
- `transactions` (list) → Stores a history of transactions
- `interest_rate` (float) → Interest rate for savings accounts
- `overdraft_limit` (float) → Negative balance allowance (for checking accounts)

### **Methods**
1. `get_balance()` → Getter for private `__balance`
2. `set_balance(new_balance)` → Setter for private `__balance` (ensuring valid value)
3. `deposit(amount)` → Adds money to the account
4. `withdraw(amount)` → Removes money, checking overdraft limits
5. `apply_interest()` → Adds interest to balance if account is savings
6. `get_transaction_history()` → Returns a list of past transactions
7. `transfer(amount, target_account)` → Sends money to another account
8. `set_overdraft_limit(limit)` → Adjusts overdraft settings
9. `check_funds(amount)` → Checks if withdrawal is possible
10. `account_summary()` → Prints a summary of the account details

---

# **Option 2: Construction Project Tracker (Civil Engineering)**
### **Class: `Project`**
Tracks project budget, expenses, and status.

### **Attributes**
- `project_name` (str) → Name of the project
- `location` (str) → Construction site location
- `contractor` (str) → Company handling the project
- `__budget` (float) → Private total budget
- `expenses` (list) → Tracks spending transactions
- `status` (str) → Current project status (`Planned`, `In Progress`, `Completed`)
- `start_date` (str) → Project start date
- `end_date` (str) → Project estimated completion date

### **Methods**
1. `get_budget()` → Getter for private `__budget`
2. `set_budget(new_budget)` → Setter for `__budget` (ensures non-negative value)
3. `allocate_budget(amount, description)` → Allocates funds for specific needs
4. `remaining_budget()` → Returns how much budget is left
5. `update_status(new_status)` → Changes project status
6. `get_expense_report()` → Returns expense history
7. `extend_deadline(new_end_date)` → Modifies the project timeline
8. `assign_contractor(new_contractor)` → Updates contractor information
9. `is_within_budget(amount)` → Checks if a new expense fits within the budget
10. `project_summary()` → Prints project details

---

# **Option 3: Environmental Sensor (Data Collection)**
### **Class: `AirQualitySensor`**
Monitors air quality levels and determines health risks.

### **Attributes**
- `location` (str) → Monitoring station name
- `sensor_type` (str) → Type of sensor (e.g., PM2.5, CO2, Ozone)
- `__current_reading` (float) → Private attribute storing the latest measurement
- `reading_history` (list) → Stores past sensor values
- `unit` (str) → Measurement unit (e.g., µg/m³, ppm)
- `warning_threshold` (float) → Value above which air quality is dangerous
- `last_calibrated` (str) → Date of last sensor calibration

### **Methods**
1. `get_current_reading()` → Getter for private `__current_reading`
2. `set_current_reading(value)` → Setter for `__current_reading` (valid range check)
3. `record_measurement(value)` → Stores a new reading
4. `get_average_reading()` → Returns the average of recent readings
5. `check_air_quality()` → Determines if air quality is within a safe range
6. `display_warning()` → Issues an alert if the reading exceeds the threshold
7. `reset_sensor()` → Clears history and resets sensor
8. `update_threshold(new_threshold)` → Changes the alert threshold
9. `needs_calibration()` → Determines if calibration is needed based on time elapsed
10. `sensor_summary()` → Prints sensor details
