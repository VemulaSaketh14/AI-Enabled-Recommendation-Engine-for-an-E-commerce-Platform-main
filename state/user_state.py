import reflex as rx
import pandas as pd
import os


class UserState(rx.State):
    """
    State managing the user's session.
    Stores user_id, logged_in status, and user_type.
    """
    user_id: int = -1
    logged_in: bool = False
    is_new_user: bool = True
    firebase_uid: str = ""
    
    email: str = ""
    password: str = ""
    auth_error: str = ""
    
    def _get_firebase_config(self):
        """Safely fetch Firebase config from environment variables."""
        print("DEBUG ENV:", dict(os.environ))
        return {
            "apiKey": os.getenv("FIREBASE_API_KEY"),
            "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
            "projectId": os.getenv("FIREBASE_PROJECT_ID"),
            "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
            "messagingSenderId": os.getenv("FIREBASE_SENDER_ID"),
            "appId": os.getenv("FIREBASE_APP_ID"),
            "databaseURL": os.getenv("FIREBASE_DATABASE_URL", "")
        }
    
    def signup_with_firebase(self):
        """Register a new user with Firebase using email/password."""
        if not self.email or not self.password:
            self.auth_error = "Please enter both email and password."
            return
            
        try:
            from pyrebase import initialize_app

            firebase_config = self._get_firebase_config()

            # Check if API key exists
            if not firebase_config["apiKey"]:
                self.auth_error = "Firebase configuration missing."
                return

            firebase = initialize_app(firebase_config)
            auth = firebase.auth()
            
            user = auth.create_user_with_email_and_password(self.email, self.password)
            self._handle_successful_login(user['localId'])

        except Exception as e:
            self.auth_error = "Registration failed. " + str(e)
            
    def login_with_firebase(self):
        """Login an existing user with Firebase."""
        if not self.email or not self.password:
            self.auth_error = "Please enter both email and password."
            return
            
        try:
            from pyrebase import initialize_app

            firebase_config = self._get_firebase_config()

            # Check if API key exists
            if not firebase_config["apiKey"]:
                self.auth_error = "Firebase configuration missing."
                return

            firebase = initialize_app(firebase_config)
            auth = firebase.auth()
            
            user = auth.sign_in_with_email_and_password(self.email, self.password)
            self._handle_successful_login(user['localId'])

        except Exception:
            self.auth_error = "Login failed. Please check credentials."

    def _handle_successful_login(self, uid: str):
        """Common logic upon successful authentication."""
        self.firebase_uid = uid
        self.logged_in = True
        self.auth_error = ""
        
        # Mock mapping (can be replaced with real logic)
        self.user_id = 1705  
        
        data_path = 'cleaned_data.csv'
        try:
            if os.path.exists(data_path):
                data = pd.read_csv(data_path, usecols=["User's ID"])
                self.is_new_user = self.user_id not in data["User's ID"].values
            else:
                self.is_new_user = True
        except Exception:
            self.is_new_user = True
            
    def logout(self):
        """Reset state on logout."""
        self.user_id = -1
        self.logged_in = False
        self.is_new_user = True
        self.firebase_uid = ""