```python
from src.mouse_test import MouseTest
from src.user_interface import UserInterface

def main():
    # Create instances of MouseTest and UserInterface
    mouse_test = MouseTest()
    user_interface = UserInterface()

    # Display the user interface
    user_interface.display_ui()

    # Handle user interaction
    user_interface.handle_user_interaction()

    # Start the mouse accuracy test
    mouse_test.start_test()

    # End the mouse accuracy test
    mouse_test.end_test()

if __name__ == "__main__":
    main()
```