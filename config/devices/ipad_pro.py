from .base_device import BaseDevice

class IPadPro(BaseDevice):
    """
    Device specifications:
    - Screen size: 12.9 inches
    - Resolution: 2048 x 2732 pixels
    - Pixel density: 264 PPI
    - Viewport size: 1024 x 1366 pixels (CSS pixels)
    """
    
    def __init__(self):
        super().__init__()
        self.name = "iPad Pro 12.9-inch"
        self.width = 1024  
        self.height = 1366  
        self.pixel_ratio = 2.0  
        self.device_type = "tablet"
        self.is_tablet = True
        self.is_desktop = False
        
        # iPad Pro user agent
        self.user_agent = (
            "Mozilla/5.0 (iPad; CPU OS 17_2_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.2 Mobile/15E148 Safari/604.1"
        )
