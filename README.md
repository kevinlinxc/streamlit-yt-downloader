# Streamlit YouTube Downloader

Hosted website for free, fast YouTube downloading at https://share.streamlit.io/kevinlinxc/streamlit-yt-downloader


# About
My dad occasionally asks me to download a YouTube video, either for the video itself or for the audio.
This is usually easy to do, but I figured I could make it easier and provide him autonomy by making this app.

Some problems with other ways of downloading YouTube videos:
- [4k Video Downloader](https://www.4kdownload.com/welcome-8), the app I use to download videos, which I downlaoded for him
is not readily available on devices - my dad could switch to a new computer or to a new context, and would have to figure out how to set it up on his own. 
- I haven't looked specifically for an extension that would allow for easy downloading, I assume there is one, but it suffers
the same problem of having to reinstall the extension in new contexts.
- Other YouTube downloading websites are usually monetized by limiting the number of downloads per day, or download speed.
They also frequently have clunky user interfaces with lots of text, ads, lots of buttons etc. 

So, I made a simple web app with Streamlit to allow for audio and video downloading.
Under the hood, I've used **youtube_dl**'s ancestor, **yt_dlp**. Downloading audio is [seemingly unsolved](https://github.com/yt-dlp/yt-dlp/issues/4237#issuecomment-1172190572), so I've just converted the 
video to audio using **moviepy**. The file size for both audio and video is within 1% from what I get from 4k Video Downloader, which is a good sign.

The video defaults to 1080p and gets the highest resolution if 1080p is not available.
