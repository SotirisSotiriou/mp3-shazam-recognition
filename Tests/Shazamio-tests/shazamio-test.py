import asyncio
from shazamio import Shazam
import sys

# sys.argv contains the script name and arguments
if len(sys.argv) != 2:
    print("Usage: python shazamio-test.py <mp3_file_path>")
    exit(1)
else:
    mp3_file = sys.argv[1]

# Create a function to fetch the text by title
def get_text_by_title(data, title):
    for item in data:
        if item['title'] == title:
            return item['text']
    return None  # Return None if the title is not found

async def recognize_song(file_path):
    shazam = Shazam()

    # Open the MP3 file as binary
    with open(file_path, 'rb') as file:
        audio_data = file.read()

    # Recognize the song from the audio data
    out = await shazam.recognize(audio_data)
    
    # Print out the song's information
    if out:
        print(f"Song: {out['track']['sections'][0]['metapages'][1]['caption']}")
        return out
    else:
        print("Song could not be recognized.")
        return None

# Run the async function
print("Song recognizer result: ")
shazam_output = asyncio.run(recognize_song(mp3_file))
metadata = shazam_output['track']['sections'][0]['metadata']

singer = shazam_output['track']['sections'][0]['metapages'][0]['caption']
title = shazam_output['track']['sections'][0]['metapages'][1]['caption']
album = get_text_by_title(metadata, "Album")
released_year = get_text_by_title(metadata, "Released")

# print(shazam_output)
print("\n\nInfo retrieved: ")
print("Singer: ", singer)
print("Title: ", title)
print("Album: ", album)
print("Release Year: ", released_year)