## Installation

### Prerequisites
1. **Java JDK 11 or higher** - Required for the Java backend.
2. **Python 3.8 or higher** - Required for data processing and script-based functionalities.
3. **Visual Studio Code** - Preferred IDE for project setup.
4. **VS Code Extensions**:
   - **Spring Boot Extension Pack** - For Spring Boot development, including dependencies management and support for running the server.
   - **Java Extension Pack** - For Java development and code editing.
   - **Python Extension** - For Python script support.

### Clone the Repository

First, clone the project to your local machine:

```bash
git clone https://github.com/YourUsername/MeteorTracker.git
cd MeteorTracker

Backend Setup
1. Install Java Dependencies

The backend uses Spring Boot with Java, so make sure Java is properly installed and configured.

    Open the Project in VS Code:
        Open the root directory of MeteorTracker in Visual Studio Code.
        Ensure that the Spring Boot Extension Pack and Java Extension Pack are installed.

    Configure pom.xml for Maven Dependencies:

        The pom.xml file should automatically load dependencies. If not, use the Maven sidebar in VS Code or run the following command in the terminal:

        bash

        mvn clean install

2. Run the Backend

Run the Spring Boot application on your local server.

bash

mvn spring-boot:run

    This should start the backend server, which will be available by default at http://localhost:8080.

Frontend Setup

The frontend is a simple HTML file located in the static folder. You can open this directly in your web browser or use VS Code’s Live Server extension for a local server.

    Open index.html:
        Navigate to the static folder in your project.
        Open index.html in a web browser.

    Alternatively, Use Live Server (optional):
        If you have the Live Server extension in VS Code, right-click index.html and select Open with Live Server to serve the file locally.
        This will serve the frontend at http://localhost:5500.

Running the Project
Full Setup Process

    Start the Backend:
        Run mvn spring-boot:run in the terminal from the project’s root directory. The backend should now be running at http://localhost:8080.

    Run the Frontend:
        Open the index.html file in your preferred browser or use Live Server in VS Code to run it locally.

    Test the Connection:
        The frontend should automatically connect to the backend to fetch meteor data.
        Use the filters provided in the UI to explore meteor information based on parameters like distance, size, and speed.

Project Structure

    src/main/java: Contains Java files for the Spring Boot backend.
        controller: Handles HTTP requests and endpoints.
        service: Contains the business logic for data processing.
    static: Contains the frontend HTML, CSS, and JavaScript files.
        index.html: The main frontend file.
        styles.css: Styling for the application.
        script.js: JavaScript functionality and API calls.

Technologies Used

    Java (Spring Boot) for backend server
    Python for data processing scripts
    HTML, CSS, JavaScript for frontend
    Maven for Java dependency management
    VS Code Extensions for enhanced development



Troubleshooting

    CORS Issues: Ensure that CORS is properly configured in corsConfigurer in MeteorTrackerApp.java.
    Python/Pip Issues: If pip install -r requirements.txt fails, check Python and pip versions. Try python3 -m pip install --upgrade pip to update pip.
