 **# Personalized Letter Generator**

This Python script automates the creation of personalized letters by combining a template letter with recipient names from a list.

## Functionality

1. **Loads Recipient Names:**
   - Reads a list of names from `./Input/Names/invited_names.txt`, removing any leading/trailing whitespace.
2. **Loads Letter Template:**
   - Reads a template letter from `./Input/Letters/starting_letter.txt`.
3. **Personalizes Letters:**
   - Iterates through the names:
     - Replaces `[name]` placeholder in the template with the recipient's name.
     - Writes the personalized letter to a separate file in `./Output/ReadyToSend`, named `letter_for_<name>.txt`.

## Usage

1. **Place files:**
   - Ensure the template letter is in `./Input/Letters/starting_letter.txt`.
   - Place the recipient names list in `./Input/Names/invited_names.txt`, one name per line.
2. **Run the script:**
   - Execute the Python script.

**This will create personalized letters in the `./Output/ReadyToSend` directory.**

## Additional Notes

- **Placeholder:** The script specifically replaces `[name]` in the template. Adjust accordingly if using a different placeholder.
- **File Paths:** The script assumes specific file locations. Modify the assigned variables if needed.

## Example Output

Assuming a template letter with "Dear [name]," and a names list containing "Alice" and "Bob":

- The script will generate:
   - `./Output/ReadyToSend/letter_for_Alice.txt` containing "Dear Alice,"
   - `./Output/ReadyToSend/letter_for_Bob.txt` containing "Dear Bob,"

