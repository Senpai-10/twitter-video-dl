import src.twitter_video_dl.twitter_video_dl as tvdl
import argparse
import string
import random

def random_file_name_genrator() -> str: 
    list = string.ascii_letters + string.digits
    length = 10
    
    return ''.join(random.choice(list) for i in range(length)) + ".mp4"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a video from a twitter url and save it as a local mp4 file."
    )

    parser.add_argument(
        "urls",
        nargs="+",
        help="Twitter URL to download.  e.g. https://twitter.com/GOTGTheGame/status/1451361961782906889"
    )

    # parser.add_argument(
    #     "--file_name",
    #     type=str,
    #     help="Save twitter video to this filename. e.g. twittervid.mp4",
    #     required=False
    # )

    args = parser.parse_args()

    # file_name = args.file_name if args.file_name.endswith(".mp4") else args.file_name + ".mp4"

    for url in args.urls:
        file_name = random_file_name_genrator()
        
        print(f"Downloading '{url}'")
        tvdl.download_video(url, file_name)
        print("Done!")
    