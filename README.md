# Essentials Locator

Essentials Locator is a Flask-based web application designed to assist users in finding essential services efficiently. Whether you're traveling, new to an area, or simply in need of urgent services, Essentials Locator simplifies the process of locating nearby facilities such as public washrooms, petrol pumps, grocery stores, and banks.

## Key Features

- **User-Friendly Interface:** Our application boasts an intuitive user interface that enables seamless navigation and quick access to essential services.
- **Geolocation Integration:** Leveraging geolocation services, Essentials Locator accurately pinpoints your current location and displays nearby essential services on an interactive map.
- **Comprehensive Database:** We maintain a comprehensive database of essential service providers, ensuring that users have access to up-to-date information on nearby facilities.
- **Customizable Search Filters:** Users can tailor their search criteria by specifying preferences such as distance, service type, and operating hours, allowing for personalized results.
- **Detailed Information:** Each listed service provider is accompanied by detailed information, including address, contact details, reviews, and additional amenities, empowering users to make informed decisions.
- **Responsive Design:** Essentials Locator is optimized for various devices, including desktops, tablets, and smartphones, ensuring a seamless user experience across different platforms.
- **User Reviews and Ratings:** To further enhance user experience, our platform incorporates a review and rating system, enabling users to share their feedback and insights with the community.
- **Accessibility Features:** We are committed to inclusivity, and our application includes accessibility features to accommodate users with diverse needs, such as text-to-speech functionality and high-contrast mode.

## Technologies Used

- **Flask:** Our web application is built using the Flask micro-framework, known for its simplicity and flexibility, making it ideal for rapid development.
- **HTML/CSS/JavaScript:** Essentials Locator employs a combination of HTML, CSS, and JavaScript to create an engaging and responsive user interface.
- **Google Maps API:** We integrate Google Maps API to power the mapping functionality, enabling users to visualize nearby essential services effectively.
- **SQLite:** The application utilizes SQLite as the database management system, facilitating efficient storage and retrieval of essential service data.
- **Bootstrap:** We leverage Bootstrap framework to ensure consistent styling and layout across different devices and screen sizes.

## Getting Started

To get started with Essentials Locator, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/essentials-locator.git
cd essentials-locator
pip install -r requirements.txtFLASK_APP=app.py
FLASK_ENV=development
flask run
