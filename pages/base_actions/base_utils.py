import random
import string
from datetime import datetime, timedelta

class BaseUtils:
    @staticmethod
    def generate_random_phone_number():
        """
        Generate a random Taiwan phone number
        
        Returns:
            str: Randomly generated Taiwan phone number, format is 09XXXXXXXX
        """
        # Generate the remaining 8 digits
        remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        
        # Combine the full phone number
        phone_number = f"09{remaining_digits}"
        
        return phone_number

    @staticmethod
    def generate_random_string(length=8):
        """
        Generate a random string
        
        Args:
            length (int): String length, default is 8
            
        Returns:
            str: Randomly generated string
        """
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_email():
        """
        Generate a random email
        
        Returns:
            str: Randomly generated email
        """
        username = BaseUtils.generate_random_string(8).lower()
        domain = BaseUtils.generate_random_string(6).lower()
        return f"{username}@{domain}.com"

    @staticmethod
    def generate_random_date(start_date=None, end_date=None):
        """
        Generate a random date
        
        Args:
            start_date (datetime): Start date, default is 30 days ago
            end_date (datetime): End date, default is today
            
        Returns:
            datetime: Randomly generated date
        """
        if not start_date:
            start_date = datetime.now() - timedelta(days=30)
        if not end_date:
            end_date = datetime.now()
            
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        return start_date + timedelta(days=random_number_of_days)

    @staticmethod
    def generate_random_number(min_value=0, max_value=100):
        """
        Generate a random number
        
        Args:
            min_value (int): Minimum value
            max_value (int): Maximum value
            
        Returns:
            int: Randomly generated number
        """
        return random.randint(min_value, max_value)
