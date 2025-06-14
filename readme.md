# 🌐 Encyclopedia

A simple Markdown-powered encyclopedia web application built with **DJANGO**. Users can view, create, edit, and search entries just like a wiki.

### 🚀 Deployed ->  [[HERE]](https://wiki-mzuv.onrender.com)🌐

This project is Project 1 from the [CS50 Web Programming](https://cs50.harvard.edu/web/2020/) course.

## ✨ Features

- 🔍 **Search** encyclopedia entries (partial matches allowed)
- 📄 **View** Markdown-formatted pages
- ➕ **Add** new entries
- ✏️ **Edit** existing entries
- 🎲 **Random** entry feature


## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

```bash
git clone https://github.com/sawankshrma/wiki.git
cd wiki
pip install -r requirements.txt  
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 📁 File Structure

```
wiki/
├── encyclopedia/       # App directory
│   ├── templates/
│   ├── static/
│   ├── urls.py
│   ├── views.py
│   └── util.py
├── entries/            # Markdown files stored here
├── wiki/               # Main project folder
├── manage.py
└── README.md
```

## 🧪 Example Entry

Create a Markdown file like `entries/Python.md`:

````markdown
# Python

Python is a high-level programming language that supports multiple programming paradigms.
