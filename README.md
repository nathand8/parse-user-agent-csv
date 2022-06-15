# parse-user-agent-csv
Short python script to parse user agent strings in a CSV and add a column to the CSV with the browser name

# Setup

Install the required pip packages
```
pip3 install -r requirements.txt
```

# Run

Run with command
```
./browser_name_csv_add_column.py input.csv output.csv
```

If your user_agent strings are not in the first column of input.csv, put the column index using `-c` argument.

For example, if user_agent strings are in the third column:
```
./browser_name_csv_add_column.py input.csv output.csv -c 2
```