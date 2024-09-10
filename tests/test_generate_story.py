import unittest
from unittest.mock import patch, MagicMock
from src.content_generation.generate_story import generate_story, read_subjects

class TestGenerateStory(unittest.TestCase):

    def test_read_subjects(self):
        # Test the read_subjects function
        with patch('builtins.open', unittest.mock.mock_open(read_data="Subject 1\nSubject 2\nSubject 3")):
            subjects = read_subjects('dummy_path')
        self.assertEqual(subjects, ['Subject 1', 'Subject 2', 'Subject 3'])

    @patch('src.content_generation.generate_story.anthropic')
    def test_generate_story(self, mock_anthropic):
        # Mock the Anthropic API response
        mock_completion = MagicMock()
        mock_completion.completion = "This is a test story."
        mock_anthropic.completions.create.return_value = mock_completion

        story = generate_story("Test Subject")
        self.assertIsNotNone(story)
        self.assertTrue(len(story) > 0)
        self.assertEqual(story, "This is a test story.")

    @patch('src.content_generation.generate_story.anthropic')
    def test_generate_story_content(self, mock_anthropic):
        # Test that the generated story doesn't contain meta-commentary
        mock_story = "Once upon a time... The end."
        mock_completion = MagicMock()
        mock_completion.completion = f"Here's a story: {mock_story}"
        mock_anthropic.completions.create.return_value = mock_completion

        story = generate_story("Test Subject")
        self.assertEqual(story, mock_story)  # Should only contain the story, not the meta-commentary

if __name__ == '__main__':
    unittest.main()