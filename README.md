# AutoShorts

AutoShorts is an automated system for generating and distributing AI-created short-form video content across various social media platforms.

## Project Overview

This project uses AI to generate stories, convert them to speech, create videos with synchronized subtitles, and automatically post them to social media platforms like TikTok, Instagram Reels, and YouTube Shorts.

### Key Features

- AI-powered story generation
- Text-to-speech conversion
- Automatic video creation with subtitles
- Multi-platform social media posting

## Project Structure

```
AutoShorts/
├── src/
│   ├── content_generation/
│   │   ├── story_generator.py
│   │   └── content_filter.py
│   ├── audio/
│   │   └── tts.py
│   ├── video/
│   │   ├── video_creator.py
│   │   └── subtitle_generator.py
│   ├── social_media/
│   │   ├── facebook_poster.py
│   │   ├── tiktok_poster.py
│   │   └── youtube_poster.py
│   └── utils/
│       └── config.py
├── tests/
│   ├── test_story_generator.py
│   ├── test_tts.py
│   └── ...
├── main.py
├── requirements.txt
└── README.md
```

### Component Descriptions

- `content_generation/`: Handles AI story generation and content filtering
- `audio/`: Manages text-to-speech conversion
- `video/`: Handles video creation and subtitle generation
- `social_media/`: Contains modules for posting to various social media platforms
- `utils/`: Includes utility functions and configuration management
- `tests/`: Contains unit tests for various components
- `main.py`: The entry point of the application, orchestrating the entire process

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AutoShorts.git
   cd AutoShorts
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your environment variables:
   ```bash
   touch .env
   ```
   Then edit the file to add your API keys and other configuration. Refer to `.env.example` for the required variables.

6. You're all set! Run the main script with:
   ```bash
   python main.py
   ```

Remember to activate the virtual environment every time you work on this project:
```bash
source venv/bin/activate
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

## Usage

After setting up the project, you can customize the content generation and posting process by modifying the relevant modules:

1. Adjust story prompts in `src/content_generation/story_generator.py`
2. Customize video creation parameters in `src/video/video_creator.py`
3. Configure social media posting options in the respective files under `src/social_media/`

Run `main.py` to execute the entire pipeline, from story generation to social media posting.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- ANTHROPIC for the LLModel (Claude 3 Haiku) used in story generation
