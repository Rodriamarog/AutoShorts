import time
from anthropic import Anthropic
from src.utils.config import config

anthropic = Anthropic(api_key=config.ANTHROPIC_API_KEY)

def read_subjects(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def generate_story(subject):
    prompt = f"""
Create a captivating and unsettling short story centered around the subject: "{subject}". 
Follow these guidelines:

1. Length: Aim for approximately 200-250 words.
2. Tone: Eerie, suspenseful, with a subtle sense of dread.
3. Structure: 
   - Begin with a hook that immediately grabs attention.
   - Build tension gradually.
   - Include a surprising twist or revelation.
   - End with a haunting final line that lingers in the reader's mind.
4. Setting: Establish a vivid, atmospheric setting that contributes to the story's mood.
5. Character: Focus on one or two main characters. Provide just enough detail to make them relatable.
6. Pacing: Given the short format, maintain a brisk pace but allow for moments of suspense.
7. Theme: Incorporate elements of mystery, the unknown, or the supernatural, tied to the given subject.
8. Language: Use vivid, evocative language. Employ sensory details to immerse the reader.
9. Dialogue: If used, keep it minimal and impactful.

Remember, the story should be suitable for adaptation into a short video format (think: tiktok, youtube shorts, instagram reels). Avoid graphic violence or explicit content. Instead, focus on creating a pervasive sense of unease and anticipation.

IMPORTANT: Provide ONLY the story text. Do not include any introductory comments, meta-commentary, or messages outside of the story itself. Begin directly with the first sentence of the story and end with the last sentence of the story.

Now, write the story:
"""
    
    response = anthropic.completions.create(
        model=config.MODEL,
        max_tokens_to_sample=config.MAX_TOKENS,
        prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
    )
    
    # Strip any leading or trailing whitespace and remove any potential meta-commentary
    story = response.completion.strip()
    if ":" in story:
        story = story.split(":", 1)[1].strip()
    
    return story

def main():
    subjects = read_subjects(config.STORY_SUBJECTS_PATH)
    total_subjects = len(subjects)

    for index, subject in enumerate(subjects, 1):
        print(f"Generating story {index}/{total_subjects} for subject: {subject}")
        story = generate_story(subject)
        print(f"\nGenerated story about {subject}:\n\n{story}")
        print("\n" + "="*50 + "\n")  # Separator between stories

        # Add a delay between API calls to avoid rate limiting
        time.sleep(1)  # Wait for 1 second between stories

if __name__ == "__main__":
    main()

