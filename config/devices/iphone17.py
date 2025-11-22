from .base_device import BaseDevice

class IPhone17(BaseDevice):
    """
    Device specifications (from Apple official specs):
    - Screen size: 6.3 inches
    - Resolution: 2622 x 1206 pixels (physical, Apple specs format)
    - Pixel density: 460 PPI
    - Device pixel ratio: 3.0
    - Portrait mode resolution: 1206 x 2622 pixels (width x height, physical)
    - Viewport size: 402 x 874 pixels (CSS pixels, calculated as 1206/3.0 x 2622/3.0)
    """
    
    def __init__(self):
        super().__init__()
        self.name = "iPhone 17"
        self.width = 402  
        self.height = 874  
        self.pixel_ratio = 3.0  
        self.device_type = "mobile"
        self.is_mobile = True
        self.is_desktop = False
        
        # iPhone 17 user agent (iOS 18.x)
        self.user_agent = (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/18.1 Mobile/15E148 Safari/604.1"
        )
