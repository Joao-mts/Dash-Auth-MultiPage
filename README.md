# Dash-Auth-MultiPage

 

This repository serves as a template for anyone looking to create a multipage and/or authenticated Dash app. I personally dislike dash bootstrap components, so i am using [dash-mantime-components](https://github.com/snehilvj/dash-mantine-components) for styling, and a [custom css navbar](https://codepen.io/fadzrinmadu/pen/bGqrJjB). The app includes the following features:

- **Multipage Structure**: Easily set up multiple pages within your Dash app.

- **User Authentication**: Integrate custom user authentication to secure your app.

- **URL Parameters**: Create dynamic layouts using URL parameters.

- **Custom Navbar**: Custom navbar with multiple links and menu.

  

## Getting Started

  

1. **Clone the repository**:

    ```bash

    git clone https://github.com/Joao-mts/Dash-Auth-MultiPage.git

    cd Dash-Auth-MultiPage

    ```

  

2. **Install Dependencies**:

    ```bash

    pip install -r requirements.txt

    ```

  

3. **Run the App**:

    ```bash

    python app.py

    ```

---

## Authentication

This application includes a custom-built authentication system using JWT (JSON Web Token) and password hashing to manage user creation, login, and access control.

### Key Features

1. **Password Security**:
    
    - Passwords are securely hashed using `bcrypt` before being stored, ensuring they are never saved in plain text.
2. **JWT-Based Authentication**:
    
    - Users receive a JWT token upon successful login, which is used to authenticate future requests. This token includes the user's email and name and expires after a set period.
3. **User Data Storage**:
    
    - User information, including hashed passwords, is stored in a `users.json` file.

### How It Works

- **User Registration**:
    
    - Users can register by providing a name, email, and password. The password is hashed, and the user's data is stored. By default, all newly created users are automatically set as valid (`is_valid: True`).
- **User Login**:
    
    - During login, the system verifies the user's email and password. If successful, a JWT token is generated and returned to the user.
- **Token Validation**:
    
    - The system checks the validity of JWT tokens to ensure that only authenticated users can access protected routes.

### Important Note

By default, when a user creates an account, they are automatically marked as valid (`is_valid: True`). If your application requires additional verification steps (e.g., email confirmation), you may want to modify this behavior. Set `is_valid` to `False` upon registration and implement a verification process where users must authenticate themselves (such as clicking a verification link) before their account is fully activated.

## Contributing
  

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

  
