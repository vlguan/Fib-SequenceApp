# Fib-SequenceApp
 Take-home challenge for fullstack software engineering at CZ Biohub SF
 ## Language & Tools
- [Python](https://www.python.org/) - project tested with v3.8
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - server-side framework
- [Pip](https://pypi.org/project/pip/) - as a package manager for the server
- [NPM](https://www.npmjs.com/) - as a package manager for the client
- [React](https://reactjs.org/) - client-side framework
### Server

- System requirements
  - Python3

1. Navigate to the server directory (in Unix that would be `cd server`)

2. Before you get started, you may want to create a virtual environment to help manage multiple versions 
   of Python on your computer. This is an optional step. Here is a 
   [quick tutorial](https://realpython.com/python-virtual-environments-a-primer/) on setting up virtual environments.

3. Copy the contents of the ".env.sample" file to a ".env" file. You can do this by using the following command:
    
    ```
    cp .env.sample .env
    ```

4. Install dependencies by using the command:

    ```
    pip install -r requirements.txt
    ```

5. Create the database by using the command:

    ```
    python seed.py
    ```

    This will re-populate the database with data closer to-date.
    There is an issue on Windows machines where Flask can't find the database, if that is an issue use 
    `sqlite:////{PATH OF DB}/server/instance/database.db`
6. Run the development server by using the command:

    ```
    flask run --port=8080
    ```

This command will launch the Flask server in debug mode (with hot-reloading) on port 8080.
To start backend server

###Client

To run the client, follow these steps:

1. Navigate to the client directory (in Unix that would be `cd client`)

2. Install dependencies

    ```bash
    npm install
    ```

    You can ignore the severity vulnerabilities, this is a [known issue](https://github.com/facebook/create-react-app/issues/11174) related to `create-react-app` and are not real vulnerabilities.

3. Start the client

    ```bash
    npm start
    ```
