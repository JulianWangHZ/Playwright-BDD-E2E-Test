from .base_device import BaseDevice

class Pixel9Pro(BaseDevice):
    """
    Device specifications (from Google Store official specs):
    - Screen size: 6.3 inches Super Actua Display (LTPO)
    - Resolution: 1280 x 2856 pixels (portrait, physical)
    - Pixel density: 495 PPI
    - Aspect ratio: 20:9
    - Device pixel ratio: 3.0
    - Viewport size: 427 x 952 pixels (CSS pixels, calculated as 1280/3.0 x 2856/3.0)
    """
    
    def __init__(self):
        super().__init__()
        self.name = "Google Pixel 9 Pro"
        self.width = 427  
        self.height = 952  
        self.pixel_ratio = 3.0  
        self.device_type = "mobile"
        self.is_mobile = True
        self.is_desktop = False
        
        # Pixel 9 Pro user agent (Android 14)
        self.user_agent = (
            "Mozilla/5.0 (Linux; Android 14; Pixel 9 Pro) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Mobile Safari/537.36"
        )
