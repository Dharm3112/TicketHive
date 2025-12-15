# TicketHive 🎬

A modern, full-stack Django movie ticketing application. This project features a robust backend for managing movies, theaters, and showtimes, paired with a sleek, dark-themed frontend for users to browse and view movie details.

## ✨ Features

### 🖥️ Frontend (User Interface)
* **Modern Dark Theme**: Aesthetic UI built with CSS variables and the "Inter" font family.
* **Movie Listing**: Grid layout displaying currently showing movies.
* **Movie Details**: Dedicated pages for each movie showing cast, description, and genres.
* **Showtime Schedule**: Real-time list of available shows, categorized by format (2D, 3D, 4DX) and language.
* **Responsive Design**: Optimized for desktop and mobile viewing.

### ⚙️ Backend (Django Admin)
* **Movie Management**: Add/Edit movies, categories, and descriptions.
* **Cast Database**: Manage Actors and Actresses separately.
* **Theater Management**: Manage Multiplexes, locations (City/State), and screens.
* **Show Scheduling**: Link movies to specific multiplexes at specific times with pricing.

## 🛠️ Tech Stack
* **Framework**: Django 5.2.3
* **Language**: Python 3.13
* **Database**: SQLite3 (Default)
* **Frontend**: HTML5, CSS3 (Custom Dark Theme)

## 🚀 Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/Dharm3112/TicketHive.git](https://github.com/Dharm3112/TicketHive.git)
cd TicketHive
````

### 2\. Set Up Virtual Environment

It is recommended to use a virtual environment to keep dependencies organized.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3\. Install Dependencies

```bash
pip install django
```

### 4\. Apply Database Migrations

Initialize the database tables.

```bash
python manage.py migrate
```

### 5\. Create Admin User

You need an admin account to add movies (since the database starts empty).

```bash
python manage.py createsuperuser
```

*Follow the prompts to set a username and password.*

### 6\. Run the Server

```bash
python manage.py runserver
```

## 📖 Usage Guide

### 1\. Populate Data (Admin Panel)

The site will look empty initially. You need to add data first:

1.  Go to `http://127.0.0.1:8000/admin/`
2.  Login with your superuser credentials.
3.  Add **Categories** (e.g., Action, Sci-Fi).
4.  Add **Actors/Actresses**.
5.  Add **Multiplexes** (Theaters).
6.  Create **Movies** and link them to actors/categories.
7.  Create **Shows** linking a Movie to a Multiplex at a specific time.

### 2\. View the Website

Once data is added, go to the homepage to see the new UI:
👉 `http://127.0.0.1:8000/`

## 📂 Project Structure

```text
TicketHive/
├── db.sqlite3          # Database file
├── manage.py           # Django command utility
├── moviesite/          # Main project configuration
│   ├── settings.py
│   └── urls.py         # Main URL routing
└── moviedata/          # Main application
    ├── admin.py        # Admin panel configuration
    ├── models.py       # Database models
    ├── views.py        # Logic for fetching data
    └── templates/      # HTML Files
        └── moviedata/
            ├── base.html       # Main layout & Dark Theme CSS
            ├── movie_list.html # Homepage
            └── movie_detail.html # Detail view
```

## 🔮 Future Enhancements

To make this project a fully production-ready application, the following features are planned:

### 💳 Payments & Bookings
* **Payment Gateway Integration:** Integrate Stripe or Razorpay to process real online payments.
* **Dynamic Seat Selection:** Upgrade the `seats` logic to a visual seat map, allowing users to select specific row/seat numbers (e.g., A1, A2) instead of just a quantity.
* **Booking History:** Create a user dashboard where customers can view their past and upcoming tickets.

### 🔔 Notifications & User Engagement
* **Email & SMS Confirmations:** Use SMTP (Gmail) or Twilio to send booking confirmation tickets and QR codes to users after purchase.
* **Reviews & Ratings:** Allow users to rate movies and write reviews, displaying the average rating on the movie detail page.
* **Watchlist:** Enable users to "favorite" upcoming movies and get notified when bookings open.

### 📊 Admin & Analytics
* **Sales Dashboard:** Add charts (using Chart.js) to the Admin panel to visualize daily revenue, ticket sales per movie, and occupancy rates.
* **Export Data:** Add functionality to export booking data to CSV/Excel for accounting purposes.

### 🛠️ Technical Improvements
* **Dockerization:** Containerize the application using Docker and Docker Compose for easy deployment.
* **Caching:** Implement Redis caching for the "Movie List" and "Showtimes" pages to improve load speeds under high traffic.
* **Rest API:** Build a robust API using Django REST Framework (DRF) to support a separate React or Mobile App frontend.
``

### Why these matter:

1.  **Payment/Seat Selection** shows you understand complex logic and third-party integrations.
2.  **Docker/Caching** shows you understand DevOps and performance optimization.
3.  **Analytics** shows you can build tools for business owners, not just customers.


---
## 📄 License

<p align="center">
  Open-source project <b>Serenipy</b> • Created by <a href="https://github.com/Dharm3112"><b>Dharm Patel</b></a>
</p>

