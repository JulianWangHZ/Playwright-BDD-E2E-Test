import os

from typing import Dict, Any, Literal
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# define supported browser types
BrowserType = Literal['chromium', 'firefox', 'webkit', 'chrome', 'safari']  # chrome/safari map to chromium/webkit
# define supported environment types
EnvType = Literal['dev', 'staging', 'prod']

# Domain Configuration -> Both dev, staging, prod use the same domain
DOMAIN = {
    'dev': 'www.transglobalus.com',
    'staging': 'www.transglobalus.com',
    'prod': 'www.transglobalus.com'
}

# Get current env domain
def get_domain(env: str = None):
    if env is None:
        env = os.getenv('ENV', 'staging')
    return DOMAIN.get(env.lower(), DOMAIN['staging'])


class Config:

    def __init__(self):
        # browser configuration (default to chromium for Playwright)
        self.BROWSER: BrowserType = os.getenv('BROWSER', 'chromium')  # type: ignore
        self.HEADLESS: bool = os.getenv('HEADLESS', 'False').lower() == 'true'
        
        # wait time configuration
        self.DEFAULT_TIMEOUT: int = int(os.getenv('DEFAULT_TIMEOUT', '20'))
        self.POLL_FREQUENCY: float = float(os.getenv('POLL_FREQUENCY', '0.5'))
        self.RETRY_TIMES: int = int(os.getenv('RETRY_TIMES', '3'))
        self.RETRY_DELAY: int = int(os.getenv('RETRY_DELAY', '2'))
        
        # environment configuration
        self.ENV: EnvType = os.getenv('ENV', 'staging')  # type: ignore
        
        # device configuration
        self.DEVICE_TYPE: str = 'desktop'  # default device type
        
        # log configuration
        self.LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
        self.SCREENSHOT_PATH: str = os.getenv('SCREENSHOT_PATH', 'screenshots')
    
    @property
    def BASE_URL(self) -> str:
        protocol = 'https://'
        domain = get_domain(self.ENV)
        return f"{protocol}{domain}"
    
    def get_page_url(self, path: str = '') -> str:
        if path:
            clean_path = '/' + path.lstrip('/')
            return f"{self.BASE_URL}{clean_path}"
        return self.BASE_URL
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """
        Get current environment configuration
        
        Returns:
            Dict[str, Any]: Configuration dictionary
        """
        instance = cls()
        return {
            'browser': instance.BROWSER,
            'headless': instance.HEADLESS,
            'timeout': instance.DEFAULT_TIMEOUT,
            'poll_frequency': instance.POLL_FREQUENCY,
            'retry_times': instance.RETRY_TIMES,
            'retry_delay': instance.RETRY_DELAY,
            'env': instance.ENV,
            'base_url': instance.BASE_URL,
            'domain': get_domain(instance.ENV),
            'log_level': instance.LOG_LEVEL,
            'screenshot_path': instance.SCREENSHOT_PATH,
            'device_type': instance.DEVICE_TYPE
        } 