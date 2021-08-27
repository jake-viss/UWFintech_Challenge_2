# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

import questionary

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @COMPLETED: Usability dialog for saving the CSV Files. 

    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    # Header row includes: Lender,Max Loan Amount,Max LTV,Max DTI,Min Credit Score,Interest Rate
    
    # Asks the user if they would like to save their file.
    save_file = questionary.text("Would you like to save the list of your qualifying loans?").ask()
    
    # If the user chooses Yes, writes the list to a new csv file of the users chosen path.
    if save_file == str("Yes"):

        csvpath = questionary.text("Please enter a file path to save your qualifying loans sheet (.csv):").ask()
        csvpath = Path(csvpath)

        with open(csvpath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write the header row
            csvwriter.writerow(header)
            # Write the data rows
            for row in qualifying_loans:
                csvwriter.writerow(row)
    # Otherwise, gives an exit message.       
    else:
        print("Thank you for using the loan qualifier app. You've chosen not to save a file of your qualifying loans.")

