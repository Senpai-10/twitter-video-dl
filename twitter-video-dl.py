#!/bin/python3

import src.twitter_video_dl.twitter_video_dl as tvdl
import argparse
import string
import random
import rich

def generate_file_name() -> str:
    list = string.ascii_letters + string.digits
    length = 10

    return ''.join(random.choice(list) for _ in range(length)) + ".mp4"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a video from a twitter url and save it as a local mp4 file."
    )

    parser.add_argument(
        "urls",
        nargs="+",
        type=str,
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

    download_list_size = len(args.urls)
    
    i = 1
    for url in args.urls:
        file_name = generate_file_name()
        pct = int(i / download_list_size * 100)
        
        rich.print(f"[bold green]Downloading[reset] video [bright_black]([yellow]{i} out of {download_list_size}[white],[yellow] {pct}%[bright_black])[reset]")
        rich.print(f"[bright_black]Url: {url}")
        rich.print(f"[bright_black]Filename: {file_name}")
        
        tvdl.download_video(url, file_name)
        
        i += 1
