PyQt Application README
This is a PyQt application that serves as a user interface for managing various tasks related to patient registration, visits, and more. The main script of the application is menu.py, which acts as the main frame to call all the different frames and functionalities.

Features
Login: The application starts with a login screen where users can log in using their credentials.
Patient Registration: Allows users to register new patients by providing necessary details.
Visit Summary: Displays a summary of visits, allowing users to view, edit, and delete visit records.
Scan Summary: Provides a summary of scans with options to view templates and generate QR code PDFs.
Report Generation: Allows users to create and manage report templates for generating PDF reports.
Installation
Clone this repository to your local machine.

Install the required dependencies using the following command:

sh
Copy code
pip install PyQt5 sqlite3 qrcode fpdf
Usage
Run the application by executing menu.py.
The application will open, and you'll be prompted to log in.
Navigate through different frames using the menu and interact with the various functionalities.
File Structure
menu.py: The main script that launches the PyQt application and handles the main menu.
patientregister.py: UI file and code for patient registration frame.
patientdetails.py: UI file and code for patient details frame.
refdrmaster.py: UI file and code for referring doctor master frame.
testmaster.py: UI file and code for test master frame.
registrationsummary.py: UI file and code for registration summary frame.
reportformat.py: UI file and code for report format frame.
scansummary.py: UI file and code for scan summary frame.
images/: Directory containing image resources used in the application.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

<!-- Contact
For any questions or feedback, please contact . -->
