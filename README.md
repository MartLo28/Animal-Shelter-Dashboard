# Grazioso Salvare Dashboard Project

## Project Overview

This project is a dashboard for Grazioso Salvare to manage and filter animal data from shelters. The dashboard is built using Python Dash and MongoDB. It provides interactive filtering options and dynamic charts to visualize the data.

### Functionality

- **Interactive Filtering Options:** Users can filter the data based on the type of rescue operation such as Water Rescue, Mountain Rescue, Disaster Rescue, and Tracking.
- **Dynamic Data Table:** The data table updates based on the selected filter, displaying relevant information about the animals.
- **Geolocation Chart:** A scatter map that shows the locations of the animals based on the selected filter.
- **Additional Chart:** A pie chart displaying the breed distribution of the animals based on the selected filter.

### Tools Used

- **Python:** The main programming language used for developing the dashboard.
- **Dash:** A Python framework for building analytical web applications.
- **MongoDB:** A NoSQL database used for storing animal data.
- **Plotly:** A graphing library used to create interactive charts.

### Setup Instructions

#### Prerequisites

- Python 3.9 or later
- MongoDB

#### Steps

1. **Import Data into MongoDB:**
   Ensure your MongoDB service is running and then import the data:
   ```bash
   mongoimport --username=${MONGO_USER} --password=${MONGO_PASS} --port=${MONGO_PORT} --host=${MONGO_HOST} --db AAC --collection animals --authenticationDatabase admin --drop --type csv --headerline ./aac_shelter_outcomes.csv

2. **Run the Dashboard:
   Open the ProjectTwoDashboard.ipynb file in Jupyter Notebook and run all cells.

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?
To make sure my programs are easy to maintain, read, and adapt, I use clear and simple code with good names for variables. I also add comments to explain what the code does. For example, in the CRUD Python module from Project One, I made sure each function does one thing well and wrote clear descriptions. This makes the code easier to work with and reuse later.

### What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
Working with well-structured code made it easier to debug and add new features. In the future, I can use this CRUD module for other projects that need database interactions, like other web apps or data dashboards.

### How do you approach a problem as a computer scientist?
I break down the problem into smaller tasks. For the database and dashboard needs of Grazioso Salvare, I first figured out what key features were needed, then planned how data would move and be used. This approach is more detailed compared to simpler past assignments. In future projects, I will use similar steps, focusing on clear requirements and building in stages to meet client needs.

### What do computer scientists do, and why does it matter?
Computer scientists create and improve software to solve real problems. This work is important because it helps make things run better and more efficiently in many fields. For Grazioso Salvare, making a good dashboard helps them manage rescue operations better by making data easy to access and use.
