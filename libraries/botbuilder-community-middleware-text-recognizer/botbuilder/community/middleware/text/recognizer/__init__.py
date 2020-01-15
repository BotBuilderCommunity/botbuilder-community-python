from .about import __version__
from .email_middleware import EmailRecognizerMiddleware
from .phone_middleware import PhoneRecognizerMiddleware
from .social_media_middleware import SocialMediaRecognizerMiddleware
from .url_middleware import UrlRecognizerMiddleware

__all__ = [
    "EmailRecognizerMiddleware",
    "PhoneRecognizerMiddleware",
    "SocialMediaRecognizerMiddleware",
    "UrlRecognizerMiddleware",
	"__version__"
    ]