# Shows Backend (TicketHive)

A Django-based backend application designed to manage data for movies, theaters (multiplexes), actors, and showtimes. This system serves as the foundational database and administrative interface for a movie ticketing platform.

## 📂 Project Structure

  * **Project Name:** `TicketHive`
  * **Database:** SQLite (Default)

## ✨ Features

  * **Movie Management:** Create and manage movie details, including descriptions and categories.
  * **Cast Management:** Distinct models for managing Male and Female actors with biographical data.
  * **Theater Management:** Manage Multiplex details including location (City/State), address, and website links.
  * **Showtime Scheduling:** Comprehensive system to schedule shows, linking specific movies to multiplexes with details like:
      * Show date and time.
      * Seat capacity and pricing.
      * Format (2D, 3D, 4DX3D).
      * Language (Hindi, English, Gujarati, Hinglish).
  * **Admin Panel:** Fully configured Django Admin interface to view, search, and edit all records.

## 🛠️ Tech Stack

  * **Language:** Python 3.13
  * **Framework:** Django 5.2.3
  * **Database:** SQLite3

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine.

### 1\. Clone the Repository

```bash
git clone https://github.com/Dharm3112/TicketHive.git
cd <repository-folder>
```

### 2\. Set Up a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3\. Install Dependencies

Ensure you have Django installed.

```bash
pip install django
```

### 4\. Apply Database Migrations

Initialize the database schema.

```bash
python manage.py migrate
```

### 5\. Create a Superuser

Create an admin account to access the backend dashboard.

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### 6\. Run the Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

## 📖 Usage

### Accessing the Admin Panel

1.  Open your browser and navigate to `http://127.0.0.1:8000/admin/`.
2.  Log in using the superuser credentials you created.
3.  You will see the **Moviedata** app where you can manage:
      * Categories
      * Male/Female Actors
      * Movies
      * Multiplexes
      * Shows

### Data Models Overview

  * **Category:** Genres or categories for movies (e.g., Thriller, Entertainment).
  * **MaleActor / FemaleActor:** Stores actor names, dates of birth, and descriptions.
  * **Movie:** Links to actors and categories.
  * **Multiplex:** Stores theater info. **Note:** Cities and States are currently selected from a predefined list within the model (e.g., Ahmedabad, Surat, Gujarat, Maharashtra).
  * **Shows:** The core scheduling model that connects a **Movie** to a **Multiplex** at a specific **Time**, defining the Price, Language, and Format.

## 🔮 Future Enhancements

  * **API Implementation:** Create REST APIs (using Django REST Framework) to serve data to a frontend application.
  * **User Authentication:** Add user login/signup for booking tickets.
  * **Booking System:** Implement a model to handle ticket reservations and seat selection.

## 🤝 Contributing

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature-branch`).
3.  Commit your changes (`git commit -m 'Add new feature'`).
4.  Push to the branch (`git push origin feature-branch`).
5.  Open a Pull Request.

## 📄 License

This project is open-source and available for use.

*Created by [Dharm Patel](https://github.com/Dharm3112)*
