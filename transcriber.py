import os
from libraries.dotenv import load_dotenv
from google import genai

def transcribe_audio(audio_file_path, output_file_path, model_name='gemini-2.0-flash', prompt="Hello, how are you doing today?"):
    """
    Transcribes audio using Google's Gemini API and writes the result to a file.

    Args:
        audio_file_path (str): Path to the audio file.
        output_file_path (str): Path to save the transcript.
        model_name (str): Name of the Gemini model to use.
        prompt (str): Optional prompt to include with the audio.
    """
    try:
        # Load environment variables
        load_dotenv()
        client = genai.Client()

        # Upload the audio file
        src = client.files.upload(file=audio_file_path)

        # Generate content using the specified model
        response = client.models.generate_content(
            model=model_name,
            contents=[prompt, src]
        )

        # Write the response to the output file
        with open(output_file_path, 'w') as transcript_file:
            transcript_file.write(str(response.text)) #access the text attribute of the response

        print(f"Transcription saved to {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None #return None when there is an error.

if __name__ == "__main__":
    audio_file = 'media/filename.mp3'
    output_file = 'output/transcript.txt'

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    transcribe_audio(audio_file, output_file)