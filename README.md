# YouTube Title Generator

A Python program that uses an external API to generate YouTube video titles based on given content. The program utilizes object-oriented principles, custom error handling, and robust structure with type annotations.

## Features
- **API Integration**: Connects to the SEORoast API to generate YouTube titles.
- **Custom Error Handling**: Custom exception class `YouTubeTitleGenerationError` for handling API-related and unexpected errors.
- **Object-Oriented Design**: Uses an abstract base class for flexibility and scalability.
- **Data Class for Easy Initialization**: Uses Python's `dataclass` to simplify class structure.
- **Type Annotations**: Enhanced readability and maintainability with type hints.

## Installation
#### 1. Clone the repository or download the code.
#### 2. Install required dependencies:

```bash
pip install requests
```

# Usage
## To generate YouTube titles based on your content:

- Update the content in the main() function to your desired input.

- Run the script:

```bash
python youtube_title_generator.py
```

# Example
```python
if __name__ == "__main__":
    generator = YouTubeTitleGenerator()

    try:
        list_of_sentences = generator.generate_titles("A car crash experiment")['sentence_list']
        for index, sentence in enumerate(list_of_sentences, start=1):
            print(f"{index}. {sentence}")
    except YouTubeTitleGenerationError as e:
        print(f"Error: {e}")
```

# Example Output:
```
1. Incredible Car Crash Experiment You Won’t Believe!
2. What Happens When a Car Crashes? See the Shocking Results
3. Unbelievable Car Crash Test – You Have to See This!
```

# Error Handling
- This project includes custom error handling to catch exceptions during the title generation process:

- YouTubeTitleGenerationError: Catches API-related errors and unexpected issues.

## Disclaimer ⚠️

**IMPORTANT: EDUCATIONAL PURPOSE ONLY**

This project does **not** directly interact with the YouTube API. It uses the SEORoast API to generate YouTube video titles, which is a third-party service and not affiliated with YouTube. The purpose of this tool is to help generate video titles for content creators based on the provided input, and it operates independently of YouTube's official API.

By using this tool, users agree to comply with the terms of service of the SEORoast API and any other relevant third-party services. This script does not make requests to YouTube's servers, nor does it interfere with or cause any harm to YouTube's API or its services.

Please ensure you are using this tool responsibly and in accordance with the applicable terms and guidelines of the services you use.


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact
For questions or support, please open an issue or reach out to the maintainer.

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the project repository.
