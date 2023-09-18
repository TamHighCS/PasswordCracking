import argparse
from hashlib import sha256

# Create a parser for the command line
parser = argparse.ArgumentParser(description="A password cracker")

# Add arguments
parser.add_argument(
    "-p",
    "--passwords_path",
    type=str,
    help="The path to the passwords file",
    default="examples/comcast.txt",
    required=False,
)

parser.add_argument(
    "-d",
    "--dictionary_path",
    type=str,
    help="The path to the dictionary file",
    default="examples/dictionary.txt",
    required=False,
)

parser.add_argument(
    "-o",
    "--output_path",
    type=str,
    help="The path to the output file",
    default="cracked/output.txt",
    required=False,
)

# Parse the arguments
args = parser.parse_args()

# Read the arguments
passwordsPath = args.passwords_path
dictionaryPath = args.dictionary_path
outputPath = args.output_path

# Load the passwords and dictionary

with open(passwordsPath) as passwordsFile:
    passwords = passwordsFile.readlines()

with open(dictionaryPath) as dictionaryFile:
    dictionary = dictionaryFile.readlines()

# Remove the new line character from the end of each password in the dictionary
dictionary = [password.strip() for password in dictionary]

passwordsMap = {}

# Split the passwords into a map of email and password
for line in passwords:
    # Remove the new line character
    line = line.strip()

    # Split the line into email and password
    email, userPassword = line.split(":", 1)
    passwordsMap[email] = userPassword

    # Loop through each password
    for password in dictionary:
        # Hash the password
        hashedPassword = sha256(password.encode()).hexdigest()

        # Check if the hashed password matches the user's password
        if hashedPassword == userPassword:
            print(f"Found password: {email}:{password}")

            # Save the found password to the output file
            with open(outputPath, "a") as outputFile:
                outputFile.write(f"{email}:{password}\n")

            break
