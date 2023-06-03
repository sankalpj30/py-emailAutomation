# Automated Email Sender

This script is a simple example of how to use the `yagmail` library to send automated emails using Gmail in Python.

## Prerequisites

- Python 3.x
- `yagmail` library (can be installed via `pip install yagmail`)

## Setup

1. Install the required `yagmail` library by running the following command: `pip install yagmail`

2. Replace the placeholders in the code with your own email details:
- Update the `user` variable with your Gmail address.
- Update the `app_password` variable with your Gmail application password. You can generate an application password in your Gmail account settings.
- Update the `to` variable with the recipient's email address.
- Modify the `subject` variable to the desired email subject.
- Customize the `content` list to include the email body and any file attachments you want to include.

## Usage

1. Save the modified code into a Python file (e.g., `script.py`).

2. Run the script by executing the following command: `python script.py`

3. The script will establish a connection to Gmail using the provided credentials and send an email to the specified recipient.

4. After the email is sent successfully, a message will be displayed in the console.

Note: Make sure that you have a stable internet connection while running the script. Ensure that you have enabled the Gmail API and generated the appropriate application password for your Gmail account.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code according to your needs.

## Acknowledgments

- This script utilizes the `yagmail` library, which simplifies email sending using Gmail in Python.



