import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    TIKTOK_API_KEY = os.getenv('TIKTOK_API_KEY')
    FACEBOOK_API_KEY = os.getenv('FACEBOOK_API_KEY')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

    # File Paths
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'output')
    BACKGROUND_VIDEO_PATH = os.getenv('BACKGROUND_VIDEO_PATH', 'assets/background.mp4')

    # Story Generation Settings
    MAX_STORY_LENGTH = int(os.getenv('MAX_STORY_LENGTH', 280))  # e.g., for Twitter-length stories
    STORY_LANGUAGE = os.getenv('STORY_LANGUAGE', 'en')

    # Text-to-Speech Settings
    TTS_VOICE = os.getenv('TTS_VOICE', 'en-US-Standard-C')

    # Video Creation Settings
    VIDEO_LENGTH = int(os.getenv('VIDEO_LENGTH', 60))  # in seconds
    VIDEO_RESOLUTION = os.getenv('VIDEO_RESOLUTION', '1080p')

    # Social Media Settings
    PLATFORMS = os.getenv('PLATFORMS', 'tiktok,youtube').split(',')

    # Debugging
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

config = Config()