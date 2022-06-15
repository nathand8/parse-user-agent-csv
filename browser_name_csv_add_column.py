#! /usr/bin/env python3

import csv, argparse
import httpagentparser
from user_agents import parse

def getBrowserNameV1(user_agent: str):
    """
    Get the browser name using the user_agents library
    https://pypi.org/project/user-agents/
    """
    ua = parse(user_agent)
    return ua.browser.family

def getBrowserNameV2(user_agent: str):
    """
    Get the browser name using the httpagentparser library
    https://pypi.org/project/httpagentparser/
    """
    ua = httpagentparser.detect(user_agent)
    if 'browser' in ua:
        return ua['browser']['name']
    else:
        return 'Browser Name'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filepath", help="File path to input csv file (required)")
    parser.add_argument("output_filepath", help="File path to input csv file (required)")
    parser.add_argument("-c", "--user-agent-column-index", help="Index of column with user agent strings. Default is first column (index = 0)", type=int, default=0, dest="col_index")
    args = parser.parse_args()

    with open(args.input_filepath, newline='') as inputcsvfile, open(args.output_filepath, 'w', newline='') as outputcsvfile:
        csvreader = csv.reader(inputcsvfile)
        csvwriter = csv.writer(outputcsvfile)
        for row in csvreader:
            browser_name_v1 = getBrowserNameV1(row[args.col_index])
            browser_name_v2 = getBrowserNameV2(row[args.col_index])
            row.insert(args.col_index + 1, browser_name_v1)
            row.insert(args.col_index + 1, browser_name_v2)
            csvwriter.writerow(row)



