
# Password Manager Python Application
#### Video Demo:  <https://youtu.be/WRB_kWmLZDU>
This project is a simple Python-based Password Manager that allows users to securely store, edit, and manage their passwords. The application runs in the console and offers basic functionalities like adding, removing, editing, and displaying stored passwords.

## Item structure
**{name, username, password}**

## Features

- **Add Item**: Store a new password for an application, website, or account.
- **Remove Item**: Delete a password entry.
- **Edit Item**: Update the stored information for an existing entry.
- **Show Items**: Display all stored passwords.

## Project Structure

- **project.py**: The main file containing the core functionalities of the Password Manager, such as adding, removing, editing, and displaying stored items.
- **test_project.py**: Contains unit tests using `pytest` to validate the functionality of the main application.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```

2. **Install dependencies:**
   Ensure you have Python installed. Then, install `pytest` for testing:
   ```bash
   pip install pytest
   ```

## Usage

1. **Run the application:**
   ```bash
   python project.py
   ```

2. **Commands:**
   - Follow the on-screen prompts to add, edit, remove, or view password entries.

## Testing

To run the unit tests and ensure everything is working correctly:
```bash
pytest test_project.py
```

## Error Handling

- **Adding Items**: Validates that all required fields (`name`, `username`, `password`) are provided and unique.
- **Removing/Editing Items**: Ensures that the entry exists before performing the action.
- **Displaying Items**: Handles empty lists and ensures the user can only edit or remove valid entries.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any inquiries or issues, please contact the contributors:

- osonhast@gmail.com
- erfanriahi90@gmail.com
- arminshabanian2000@gmail.com
