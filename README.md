# RemoteHunter - Automated Remote Job Alert Platform

![RemoteHunter Dashboard](https://raw.githubusercontent.com/LetaEmiru1/RemoteHunter-MVP/main/Dashboard.png) 

**Live Application:** [remote-hunter-mvp.vercel.app](https://remote-hunter-mvp.vercel.app)
<!-- Make sure this is your correct Vercel URL -->

---

## 🚀 About This Project

RemoteHunter is a full-stack web application designed to automate the search for remote job opportunities. As my first end-to-end project, it was built to solve a personal challenge: breaking out of "tutorial hell" and creating a complete, functional, and deployed product from scratch.

The application automatically fetches new remote job listings, stores them, and allows users to register for personalized daily email alerts based on a specific keyword, all while operating at zero financial cost.

---

## ✨ Features

*   **Public Job Board:** A clean, responsive interface displaying the latest remote job listings.
*   **User Authentication:** Secure user registration, email verification, login, and session management.
*   **Personalized Keyword Alerts:** A protected user dashboard where users can save and update a specific keyword for their job search.
*   **Fully Automated Pipeline:** A GitHub Actions workflow runs daily to:
    1.  Fetch new jobs from a third-party API.
    2.  Match jobs against user keywords.
    3.  Send personalized HTML email alerts to subscribed users.

---

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **Frontend:** Vanilla JavaScript (ES6+), HTML5, CSS3, Bootstrap 5
*   **Database:** PostgreSQL (hosted on Supabase)
*   **Authentication:** Supabase Auth
*   **Automation:** GitHub Actions (CI/CD)
*   **Deployment:**
    *   **Backend (API):** Render
    *   **Frontend (Static Site):** Vercel
*   **APIs:** Jooble (Job Data), Resend (Email Delivery)
*   **Key Python Libraries:** `requests`, `supabase-py`, `python-dotenv`, `gunicorn`

---

## ⚙️ Running Locally

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/LetaEmiru1/RemoteHunter-MVP.git
    cd RemoteHunter-MVP
    ```

2.  **Set up a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add your secret keys. Use the `.env.example` file as a template. You will need keys for:
    *   `SUPABASE_URL`
    *   `SUPABASE_KEY` (the secret `service_role` key)
    *   `JOOBLE_KEY`
    *   `RESEND_API_KEY`

5.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

## 📈 What I Learned

Building RemoteHunter was an incredible learning experience. I went from understanding language syntax to architecting a full-stack system. Key takeaways include:
*   Designing a relational database schema and implementing server-side SQL triggers.
*   Building a secure, decoupled frontend/backend architecture.
*   Managing secret keys and credentials securely using environment variables.
*   Automating a complete data pipeline using GitHub Actions for a true "set it and forget it" application.