import os

class MenuScreen:
    def __init__(self, top_message, exit_message, menu_options):
        self.is_running = True
        self.top_message = top_message
        self.valid_message = ""
        self.exit_message = exit_message
        self._menu_options = menu_options
        self._menu_options.append({"msg": "Exit", "fn": self._exit_program})
    
    @property
    def menu_options(self):
        return self._menu_options

    @menu_options.setter
    def menu_options(self, value):
        self._menu_options = value
        self._menu_options.append({"msg": "Exit", "fn": self._exit_program})

    def run(self):
        """Main application loop."""
        while self.is_running:
            self._show_main_menu()

            choice = self._get_user_choice()
            if choice is None:
                continue
            
            os.system('cls' if os.name == 'nt' else 'clear')
            self._execute_menu_option(choice)
            
            if self.is_running:  # Only wait if not exiting
                input("\nPress Enter to continue...")
    
    def _show_main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display validation messages to the user
        if self.valid_message:
            print(f"{self.valid_message}\n")
            self.valid_message = ""
        
        print(self.top_message)
        print()
        for index, option in enumerate(self.menu_options, start=1):
            print(f"{index}. {option['msg']}")

    def _get_user_choice(self):
        """Get and validate user menu choice."""
        menu_count = len(self.menu_options)
        
        try:
            choice = int(input(f"Choose an option (1-{menu_count}): "))
            if not (1 <= choice <= menu_count):
                self.valid_message = f"Invalid selection. Please choose a number between 1 and {menu_count}."
                return None
            return choice
        except ValueError:
            self.valid_message = f"Invalid input. Please enter a number between 1 and {menu_count}."
            return None
        except KeyboardInterrupt:
            self.valid_message = "\nOperation cancelled by user."
            return None
        except Exception as e:
            self.valid_message = f"An unexpected error occurred: {e}"
            return None
    
    def _execute_menu_option(self, choice):
        """Execute the selected menu option."""
        try:
            selected_option = self.menu_options[choice - 1]
            print(f"You selected: {choice}. {selected_option['msg']}\n")
            
            # Execute the selected function
            fns = selected_option["fn"]

            if isinstance(fns, list):
                for fn in fns:
                    fn()
            else:
                fns()
                
        except Exception as e:
            self.valid_message = f"Error executing menu option: {e}"
        
    def _exit_program(self):
        """Exit the application gracefully."""
        self.is_running = False
        print(self.exit_message)