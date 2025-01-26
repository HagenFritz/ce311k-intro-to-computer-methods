import openpyxl
import csv
import json
import re
import argparse
from collections import defaultdict

# Function to execute Python code and check if it matches the expected output
def execute_code(code, expected_output, name, question_number):
    try:
        # Preprocess the code: strip leading/trailing whitespace and normalize newlines
        code = code.strip()

        # Split the code into lines
        lines = code.splitlines()

        # Prepare a local scope for execution
        local_scope = {}

        # Execute all lines of code
        if len(lines) > 1:
            exec("\n".join(lines[:-1]), {}, local_scope)  # Execute all but the last line

        # Handle the last line
        output = None
        if lines:
            last_line = lines[-1].strip()
            if "=" not in last_line:  # If no assignment operator is in the last line
                try:
                    # Dynamically evaluate the last line and assign its result to `output`
                    last_line = f"output = {last_line}"
                    output = eval(last_line, {}, local_scope)
                    local_scope["output"] = output  # Save to `output` for consistency
                except (SyntaxError, NameError):
                    output = local_scope.get("output", None)  # Fallback to existing `output`
            else:
                # Last line contains an assignment, execute it as regular Python code
                exec(last_line, {}, local_scope)
                output = local_scope.get("output", None)  # Check if `output` is in scope

        # Handle regex matching for the expected output
        if isinstance(expected_output, str) and expected_output.startswith("regex:"):
            regex_pattern = expected_output[6:]  # Remove the "regex:" prefix
            if output is None:
                output = ""  # Treat None as an empty string for regex matching
            return bool(re.match(regex_pattern, str(output)))

        # Handle empty expected output
        if expected_output == "":
            return output in (None, "")

        # Standard comparison
        return str(output) == str(expected_output)

    except SyntaxError as e:
        print(f"Syntax error for student '{name}' on question '{question_number}': {e}")
        print(f"Problematic code: {repr(code)}")
        return False
    except Exception as e:
        print(f"Code execution error for student '{name}' on question '{question_number}': {e}")
        print(f"Problematic code: {repr(code)}")
        return False

# Load the expected outputs from a JSON file
def load_expected_outputs(file_path):
    try:
        with open(file_path, 'r') as file:
            expected_outputs = json.load(file)
        return expected_outputs
    except Exception as e:
        print(f"An error occurred while loading expected outputs: {e}")
        return {}

# Process the Excel file, calculate scores, and return results
def process_excel(file_path, expected_outputs):
    scores = defaultdict(int)  # Store scores for each student
    correct_questions = defaultdict(list)  # Track correct question numbers for each student
    processed_questions = defaultdict(set)  # Track processed questions per student

    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # Iterate through rows (assume headers are in the first row)
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip the header row
            submission_time, name, code, question_number, output = row[:5]
            
            # Skip rows with empty name, code, or question number
            if not name or not code or not question_number:
                continue

            if int(question_number) == 0:
                continue

            question_number = str(question_number)  # Ensure question number is a string
            expected_output = expected_outputs.get(question_number, None)

            # Skip if this question has already been successfully processed for this student
            if question_number in processed_questions[name]:
                continue

            # Check if the code executes successfully and matches the expected output
            is_correct = execute_code(code, expected_output, name, question_number)
            if is_correct:
                scores[name] += 1
                correct_questions[name].append(question_number)
                processed_questions[name].add(question_number)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
    return scores, correct_questions

# Write the results to an output CSV file
def write_results(output_path, scores, correct_questions):
    try:
        with open(output_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score", "Correct Questions"])  # Header

            # Sort rows by last name
            sorted_rows = sorted(
                [(name, score, ", ".join(sorted(map(str, correct_questions[name])))) 
                 for name, score in scores.items()],
                key=lambda x: x[0].split()[-1].lower()
            )

            # Write sorted rows
            writer.writerows(sorted_rows)
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

# Main function
def main(filename=""):
    input_file = f"./data/{filename}.xlsx"
    output_file = f"./data/{filename}_results.csv"
    expected_file = f"./data/{filename}.json"

    # Load expected outputs from JSON file
    expected_outputs = load_expected_outputs(expected_file)

    # Process the Excel file to calculate scores
    scores, correct_questions = process_excel(input_file, expected_outputs)

    # Write the results to an output file
    write_results(output_file, scores, correct_questions)

    print(f"Results saved to {output_file}")

# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an Excel file with Python code.")
    parser.add_argument(
        "--file", 
        type=str, 
        required=True, 
        help="Name of the Excel file located in the root/data directory (without extension)"
    )
    args = parser.parse_args()

    main(filename=args.file)
