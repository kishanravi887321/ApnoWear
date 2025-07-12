
# ApnoWear

**Team:** Team 2531  
**Product Name:** ApnoWear  
**Problem Statement:** PS-3 ReWear – Community Clothing Exchange  
**Team Members:**  
- Neha Kasera (Team Lead)  
- Ravi Kishan  
- Roma  
- Subhash Rajpurohit  
**Team Lead Email:** nehakasera1823@gmail.com  

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Presentation Assets](#presentation-assets)
- [License](#license)
- [Contact](#contact)

---

## Overview

**ApnoWear** is a web-based platform designed to foster sustainable fashion by enabling users to exchange unused clothing through direct swaps or a point-based redemption system. The initiative aims to reduce textile waste and promote reuse by offering a community-driven, eco-friendly solution.

---

## Features

- **User Authentication:** Secure email/password signup and login system.
- **Landing Page:** Introduction to the platform with CTAs like “Start Swapping”, “Browse Items”, and “List an Item”.
- **User Dashboard:** Shows profile info, points balance, listed items, and swap history.
- **Item Detail Page:** Item image gallery, uploader details, swap/redeem options, and availability.
- **Add New Item:** Upload clothing details including condition, size, tags, and category.
- **Admin Panel:** Manage listings, approve/reject items, and moderate platform activity.
- **Sustainability Focus:** Built to encourage circular economy and responsible fashion habits.

---

## Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default, can be upgraded)  
- **APIs:** Django REST Framework  
- **Authentication:** Django built-in authentication

---

## Setup & Installation

1. **Clone the Repository**
   ```
   git clone 
   cd ApnoWear/App
   ```

2. **Create Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```
   python manage.py runserver
   ```

6. **Frontend**
   - Open `frontend/index.html` in a browser to preview the static landing page.

---

## Usage

- **Register / Login:** Create an account or sign in.
- **Browse Items:** Discover clothing shared by other users.
- **List an Item:** Upload unused items for swaps or point-based redemption.
- **Swap / Redeem:** Choose to swap items or redeem them using your point balance.
- **Dashboard:** Track your contributions and ongoing/completed exchanges.
- **Admin Privileges:** Moderators can approve/reject listings and oversee user activity.

---

## Contributing

We welcome open-source contributions. Here's how you can contribute:

1. Fork the repository
2. Create a new branch
   ```
   git checkout -b feature-branch
   ```
3. Commit your changes
   ```
   git commit -am 'Add new feature'
   ```
4. Push to your branch
   ```
   git push origin feature-branch
   ```
5. Open a Pull Request

---

## Presentation Assets

- **Logo:** `frontend/logos/apnowear_logo.png`
- **Circular Economy Model:** `Presentation/images/CIRCULAR economy model.png`
- **Fashion Market Stats:** `Presentation/images/fashion market stats.png`
- **Target Audience:** `Presentation/images/target audience.png`
- **Pitch Deck & Product Overview:** `ApnoWear.pdf`
- **System DFD:** `Final Dfd_ApnoWear.pdf`
- **Video Matter:** `Presentation/video_matter_files/`

---

## Youtube Link

The link to the video is https://youtu.be/usAoFGzeSZo

---

## License

This project is developed solely for educational and hackathon purposes.

---

## Contact

For queries and collaborations, reach out to:  
**Neha Kasera (Team Lead)**  
nehakasera1823@gmail.com

---

Thank you for exploring ApnoWear — together, let’s make fashion sustainable!

