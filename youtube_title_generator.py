import requests
import re
from typing import Optional, List, Dict, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass


# Custom exception class for handling API-related errors
class YouTubeTitleGenerationError(Exception):
    def __init__(self, message: str):
        """
        Initializes a YouTubeTitleGenerationError instance with a custom error message.

        Args:
            message (str): The error message to be associated with the exception.
        """
        super().__init__(message)


# Abstract base class defining the structure for YouTube title generation
class TitleGenerator(ABC):
    @abstractmethod
    def generate_titles(self, content: str, tone: Optional[str] = "auto") -> Dict[str, Any]:
        """
        Generates a list of YouTube title options based on the provided content and tone.

        Args:
            content (str): The content to generate titles for.
            tone (Optional[str], optional): The tone of the titles to generate. Defaults to "auto".

        Returns:
            Dict[str, Any]: A dictionary containing a list of generated title options.
        """
        pass


# Concrete implementation of the TitleGenerator class
@dataclass
class YouTubeTitleGenerator(TitleGenerator):
    """
    A concrete implementation of the TitleGenerator class for generating YouTube titles.

    This class utilizes the YouTubeTitleGenerationError custom exception to handle errors related to title generation.
    It provides a method to generate a list of YouTube title options based on the provided content and tone.
    """
    api_url: str = "https://seoroast.co/api/generate-youtube-titles"
    model: str = "google/gemini-flash-1.5"
    headers: Dict[str, str] = None

    def __post_init__(self):
        """
        Initializes the YouTubeTitleGenerator instance with default headers if not provided.
        """
        if self.headers is None:
            self.headers = {
                "accept": "*/*",
                "Content-Type": "application/json",
                "origin": "https://seoroast.co"
            }

    def generate_titles(self, content: str, tone: Optional[str] = "auto") -> Dict[str, Any]:
        """
        Generates a list of YouTube title options based on the provided content and tone.

        Args:
            content (str): The content to generate titles for.
            tone (Optional[str], optional): The tone of the titles to generate. Defaults to "auto".

        Returns:
            Dict[str, Any]: A dictionary containing a list of generated title options.
        """
        payload = {
            "content": content,
            "model": self.model,
            "tone": tone
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            sentences = str(response.json().get("result", "")[9:-6]).strip()
            sentence_list = re.findall(r'"(.*?)"', sentences)
            return {"sentence_list": sentence_list}
        except requests.exceptions.RequestException as e:
            raise YouTubeTitleGenerationError(f"An error occurred while generating YouTube titles: {str(e)}")
        except Exception as e:
            raise YouTubeTitleGenerationError(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    generator = YouTubeTitleGenerator()

    try:
        list_of_sentences = generator.generate_titles("A car crash experiment")['sentence_list']
        for index, sentence in enumerate(list_of_sentences, start=1):
            print(f"{index}. {sentence}")
    except YouTubeTitleGenerationError as e:
        print(f"Error: {e}")