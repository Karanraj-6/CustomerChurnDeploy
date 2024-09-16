# Customer_churn_prediction


## Overview

The Customer Churn Prediction project aims to identify customers who are likely to leave a service or subscription. This project involves data preprocessing, model development, and deployment using a machine learning model trained on IBM's Telco Customer Churn dataset.

### Key Features

- **Data Preprocessing**: Cleaned and processed data to handle missing values and feature engineering.
- **Model Development**: Built and trained various machine learning models to predict customer churn.
- **Performance Metrics**: Achieved significant improvements in accuracy, precision, and recall.
- **Database Integration**: Stores user-entered data in a SQLite database for persistent storage and easy retrieval.

### Database Integration

One of the standout features of this project is its ability to store and manage data using a database. Here’s how it works:

1. **Database Setup**: The application uses SQLite to store customer data and prediction results. SQLite is a lightweight, disk-based database that doesn’t require a separate server process, making it ideal for small to medium-sized applications.

2. **Data Insertion**: User-entered data is captured through the web application interface and inserted into the SQLite database. This allows for persistent storage of data and ensures that predictions and user interactions are recorded.

3. **Data Retrieval**: The application can retrieve stored data to display historical predictions, analyze trends, or generate reports.

4. **Benefits**:
   - **Persistence**: Data is saved even after the application is closed, ensuring that information is not lost.
   - **Accessibility**: Easily access and manipulate stored data for further analysis or reporting.
   - **Efficiency**: Improves the application's efficiency by avoiding repeated data entry and processing.

### Demo Video

Here’s a video demonstration of the Customer Churn Prediction project:

<div align="center">
  <a href="https://www.linkedin.com/posts/karanraj-kumbala-1566ba283_innovation-machinelearning-datascience-activity-7230575979524411392-HMRv?utm_source=share&utm_medium=member_desktop" target="_blank">
    <img src="https://www.linkedin.com/posts/karanraj-kumbala-1566ba283_innovation-machinelearning-datascience-activity-7230575979524411392-HMRv?utm_source=share&utm_medium=member_desktop" alt="Watch the video" style="max-width: 100%; height: auto; border-radius: 8px;">
  </a>
</div>

Replace `YOUR_VIDEO_ID` with the actual ID of your YouTube video.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
 
