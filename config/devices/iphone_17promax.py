from .base_device import BaseDevice

class IPhone17ProMax(BaseDevice):
    """
    Device specifications:
    - Screen size: 6.9 inches
    - Resolution: 1320 x 2868 pixels (portrait, physical)
    - Pixel density: 460 PPI
    - Device pixel ratio: 3.0
    - Viewport size: 440 x 956 pixels (CSS pixels)
    """
    
    def __init__(self):
        super().__init__()
        self.name = "iPhone 17 Pro Max"
        self.width = 440  
        self.height = 956  
        self.pixel_ratio = 3.0  
        self.device_type = "mobile"
        self.is_mobile = True
        self.is_desktop = False
        
        # iPhone 17 Pro Max user agent (iOS 18.x)
        self.user_agent = (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/18.1 Mobile/15E148 Safari/604.1"
        )
