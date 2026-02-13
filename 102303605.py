import sys
import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-8.0.1-essentials_build\bin"
import yt_dlp
from moviepy import AudioFileClip
from pydub import AudioSegment


def download_videos(singer, num):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'retries': 10,
    'fragment_retries': 10,
    'socket_timeout': 30
}


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search = f"ytsearch{num}:{singer}"
        ydl.download([search])

def trim_audio(duration):
    trimmed_files = []

    for file in os.listdir("downloads"):
        path = os.path.join("downloads", file)

        audio = AudioFileClip(path)
        trimmed = audio.subclipped(0, duration)

        output = f"trimmed_{file}.mp3"
        trimmed.write_audiofile(output)

        trimmed_files.append(output)

    return trimmed_files

def merge_audio(files, output):
    final = AudioSegment.empty()

    for f in files:
        sound = AudioSegment.from_file(f)
        final += sound

    final.export(output, format="mp3")

def main():
    if len(sys.argv) != 5:
        print("Usage: python program.py <SingerName> <NumberOfVideos> <Duration> <OutputFile>")
        return

    singer = sys.argv[1]
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
    output_file = sys.argv[4]

    try:
        print("Downloading videos...")
        download_videos(singer, num_videos)

        print("Trimming audio...")
        files = trim_audio(duration)

        print("Merging...")
        merge_audio(files, output_file)

        print("Mashup created successfully!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

