<<<<<<< HEAD
# Event_Management
=======
Event Management Application
A web-based Event Management system designed to help users create and manage events, book tickets, and make payments seamlessly. This application includes a Stripe payment gateway integration for secure online transactions.

Features
User Authentication: Users can register and log in to manage events and bookings.
Event Creation: Admins can create and manage events with details such as date, time, location, and ticket price.
Event Booking: Users can browse events and book tickets.
Stripe Payment Integration: Users can securely make payments for event bookings via Stripe.
Admin Dashboard: Admins can view and manage events and bookings.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite (can be replaced with any other DB like PostgreSQL)
Payment Gateway: Stripe API (for secure payments)
Authentication: Django's built-in authentication system
Version Control: Git, GitHub
Installation
To set up the project locally, follow the steps below:

1. Clone the Repository
Clone this repository to your local machine using:

bash
Copy code
git clone https://github.com/fathimaris/Event_Management.git
2. Install Dependencies
Navigate to the project directory and create a virtual environment:

bash
Copy code
cd Event_Management
python -m venv venv
Activate the virtual environment:

For Windows:
bash
Copy code
.\venv\Scripts\activate
For Mac/Linux:
bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
3. Configure Stripe API Keys
In the project settings, add your Stripe API keys. You can get them from the Stripe Dashboard.

python
Copy code
# In settings.py
STRIPE_SECRET_KEY = 'your_secret_key'
STRIPE_PUBLIC_KEY = 'your_public_key'
4. Migrate Database
Run the following command to apply migrations to the database:

bash
Copy code
python manage.py migrate
5. Create a Superuser
Create an admin user to access the admin panel:

bash
Copy code
python manage.py createsuperuser
Follow the instructions to set up the admin credentials.

6. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to access the application.

Usage
Admin Login: Visit /admin and log in using the superuser credentials you created.
User Login/Registration: Users can register and log in to view and book events.
Booking: After logging in, users can browse available events and make bookings. Payments will be processed via Stripe.
Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request with your changes.

Steps for contributing:
Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes and commit them (git commit -am 'Add your feature').
Push your branch (git push origin feature/your-feature-name).
Open a pull request on GitHub.
License
This project is licensed under the MIT License - see the LICENSE file for details.
>>>>>>> 846c091 (Create README.md)
