# 🎨 Jeuan M. Mitchell's Portfolio Website

Welcome to my Django portfolio project! This website is like a digital trophy case where I can show off all the cool projects I've built. Think of it as Instagram, but for coding projects instead of food pics.

## 🚀 What Does This Thing Do?

This is a full-stack web application that lets me (and anyone I give permission to):
- Display my coding projects with pictures and descriptions
- Show off my technical skills
- Share my experience and background
- Let visitors contact me through a form
- Switch between light mode and dark mode (because who doesn't love dark mode?)

## 🛠️ Technologies Used (The Cool Tools)

- **Django 6.0.1** - The main framework (like the foundation of a house)
- **Python** - The programming language that makes everything work
- **SQLite** - A mini database that lives in one file (super portable!)
- **Pillow** - For handling images (not the fluffy kind, sadly)
- **HTML/CSS/JavaScript** - Makes it look pretty and interactive
- **Font Awesome** - Free icons because buying icons is not fun

## 📋 Setup Instructions (How to Get This Running)

### Step 1: Make Sure You Have Python Installed
You need Python 3.10 or newer. Check if you have it by opening your terminal and typing:
```bash
python --version
```
If you see something like "Python 3.14.0" you're good to go! If not, download Python from [python.org](https://www.python.org/).

### Step 2: Download This Project
If you're reading this, you probably already downloaded it from GitHub. Good job! 🎉

### Step 3: Create a Virtual Environment (Your Own Coding Bubble)
Think of a virtual environment like a separate room where all your project's stuff lives. This keeps everything organized and prevents fights with other projects.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

You'll know it worked when you see `(venv)` at the start of your terminal line. Congrats, you're in the bubble! 🫧

### Step 4: Install All the Required Packages
This is like downloading all the ingredients before you start cooking.
```bash
pip install -r requirements.txt
```

This will install:
- Django (the main web framework)
- Pillow (for image uploads)
- django-environ (for managing secret settings)
- A few other helpful tools

Grab a snack while this installs. It might take a minute.

### Step 5: Set Up the Database
Right now, the database doesn't exist. We need to create it! Run this command:
```bash
python manage.py migrate
```

This creates a file called `db.sqlite3` which is basically a mini database. All your data will live here!

### Step 6: Create Your Admin Account (Become the Boss)
You need an admin account to add, edit, or delete projects. Run:
```bash
python manage.py createsuperuser
```

It will ask you for:
- **Username** - Pick something cool (or just use "admin" if you're feeling lazy)
- **Email** - Your email address (you can fake this for testing)
- **Password** - Make it secure! (But also write it down so you don't forget it)

### Step 7: Start the Server (The Moment of Truth!)
```bash
python manage.py runserver
```

You should see something like:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 8: Check It Out in Your Browser
Open your favorite web browser and go to:
```
http://127.0.0.1:8000/
```

BOOM! 💥 The portfolio website should appear!

## 🎮 How to Use the Website

### Viewing as a Regular Visitor
Just browse around! Check out:
- **About Me** - My introduction (the home page)
- **Experience** - Where I've worked and what I've done
- **Skills** - All the programming languages and tools I know
- **Projects** - The cool stuff I've built (this will be empty at first)
- **Contact** - A form to send me messages

You can also click the moon/sun icon in the top right to switch between light and dark mode. Try it, it's satisfying!

### Adding Projects (Admin Only!)
To add projects, you need to be logged in as an admin:

1. Click the "Login" button in the navigation bar
2. Use the username and password you created in Step 6
3. Once logged in, you'll see an "+ Add New Project" button
4. Click it and fill out the form:
   - **Project Name** - What you called it
   - **Year** - When you made it
   - **Description** - What it does (be descriptive!)
   - **Image** - Upload a screenshot or logo
   - **Repository** - Link to your GitHub repo (optional)
   - **Skills** - Select the technologies you used
5. Hit "Submit" and watch your project appear!

### Managing Projects
When logged in, you'll see **Edit** and **Delete** buttons on each project. Use these carefully - there's no "undo" button! (Well, there's a confirmation dialog for deleting, but still.)

## 🔧 Project Structure (Where Everything Lives)

```
portfolio CH 61/
├── config/              # Main settings and URLs
├── pages/               # About, Experience, Skills pages
├── projects/            # Projects app (the main feature)
├── static/              # CSS, images, JavaScript
├── templates/           # HTML files
├── media/               # Uploaded project images (created when you upload)
├── venv/                # Virtual environment (don't touch!)
├── db.sqlite3           # Database (created after migrations)
├── manage.py            # Django's magic wand
├── requirements.txt     # List of required packages
└── README.md            # You are here! 📍
```

## 🎨 Features Included

✅ Full CRUD for projects (Create, Read, Update, Delete)  
✅ User authentication (login/logout)  
✅ Protected routes (can't delete stuff unless logged in)  
✅ Contact form with email functionality  
✅ Light/Dark mode toggle (with localStorage so it remembers your preference)  
✅ Responsive design (works on phones too!)  
✅ Mitchell Library styling (fancy beveled buttons and gradients)  
✅ Skills management system  
✅ Custom 404 error handling  

## 📧 Contact Form Setup (Optional)

The contact form can send real emails, but it needs some setup. If you just want to test the website, you can skip this part - the form will still work, it just won't actually send emails.

To make emails work:
1. Create a `.env` file in the project root
2. Add your Gmail account and app password:
```
EMAIL_HOST_USER="your-email@gmail.com"
EMAIL_HOST_PASSWORD="your-app-password-here"
```

**Note:** You need a Gmail App Password (not your regular password). Google it for instructions!

## 🐛 Troubleshooting (When Things Go Wrong)

### "Command not found: python"
Try using `python3` instead of `python` in all commands.

### "Port 8000 is already in use"
Something is already running on that port. Either:
- Close the other program
- Use a different port: `python manage.py runserver 8001`

### "No module named Django"
Your virtual environment isn't activated. Look for Step 3 again!

### The CSS Looks Weird
Try force-refreshing your browser:
- **Windows/Linux:** Ctrl + Shift + R
- **Mac:** Cmd + Shift + R

### I Forgot My Admin Password
No worries! Run this and create a new superuser:
```bash
python manage.py createsuperuser
```

## 🎓 Assignment Notes (For My Instructor)

This project demonstrates:
- Django MVC architecture (Models, Views, Templates)
- Database design with relationships (Projects have many Skills)
- User authentication and authorization
- Form handling and validation
- File upload functionality
- RESTful routing
- Responsive CSS design
- JavaScript DOM manipulation
- Security best practices (CSRF protection, login decorators)

**Note:** The database (`db.sqlite3`) is not included in the repository because it contains user passwords. You'll need to run migrations and create your own superuser account to test the admin features.

## 🤝 Credits

Built with ❤️ by Jeuan M. Mitchell  
Special thanks to caffeine and Stack Overflow

---

**Need help?** Feel free to reach out through the contact form on the website (once you get it running)!

Happy grading! 🎓✨
