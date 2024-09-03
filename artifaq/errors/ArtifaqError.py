class ArtifaqError(Exception):
    """Base exception for Artifaq"""

class ApplicationLoadError(ArtifaqError):
    """Raised when there's an error loading an application"""

class ConfigurationError(ArtifaqError):
    """Raised when there's an error in the configuration"""

class InterfaceError(ArtifaqError):
    """Raised when there's an error with the application interface"""