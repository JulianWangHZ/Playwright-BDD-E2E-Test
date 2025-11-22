from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class BaseDevice:

    # Desktop full screen size
    name: str = "Base Device"
    width: int = 1920
    height: int = 1080
    pixel_ratio: float = 1.0
    
    # User agent string
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    # Device type
    device_type: str = "desktop"
    
    # Device features
    is_mobile: bool = False
    is_tablet: bool = False
    is_desktop: bool = True
    
    def get_viewport_size(self) -> Dict[str, int]:
        return {
            "width": self.width,
            "height": self.height
        }
    
    def get_device_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.device_type,
            "viewport": self.get_viewport_size(),
            "pixel_ratio": self.pixel_ratio,
            "user_agent": self.user_agent,
            "is_mobile": self.is_mobile,
            "is_tablet": self.is_tablet,
            "is_desktop": self.is_desktop
        }
    
    def __str__(self) -> str:
        return f"{self.name} ({self.width}x{self.height})"
