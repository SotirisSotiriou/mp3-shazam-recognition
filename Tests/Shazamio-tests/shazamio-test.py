import asyncio
from shazamio import Shazam

async def recognize_song(file_path):
    shazam = Shazam()

    # Open the MP3 file as binary
    with open(file_path, 'rb') as file:
        audio_data = file.read()

    # Recognize the song from the audio data
    out = await shazam.recognize(audio_data)
    
    # Print out the song's information
    if out:
        # print(f"Song recognized: {out['track']['title']} by {out['track']['subtitle']}")
        # print(f"Album: {out['track']['sections'][0]['metadata'][0]['text']}")
        # print(f"Shazam link: {out['track']['url']}")
        print(out)
    else:
        print("Song could not be recognized.")

# File path to the MP3 you want to recognize
mp3_file = "a.mp3"

# Run the async function
asyncio.run(recognize_song(mp3_file))
