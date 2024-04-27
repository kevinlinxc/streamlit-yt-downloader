# Streamlit YouTube Downloader

Hosted website for free, fast YouTube downloading at https://kevinlinxc-yt-downloader.streamlit.app/


# About
My dad occasionally asks me to download a YouTube video, either for the video itself or the audio.
This is usually easy to do, but I figured I could make it easier and provide him autonomy by making this app.

Some problems with other ways of downloading YouTube videos:
- Apps or extensions need to be installed on every new computer, whereas a website can be visited easily on any computer/phone
- Other YouTube downloading websites are usually monetized by limiting the number of downloads per day, or download speed.
They also frequently have clunky user interfaces with lots of text, ads, buttons etc. 

So, I made a simple web app with Streamlit to allow for audio and video downloading.
Under the hood, I've used **youtube_dl**'s ancestor, **yt_dlp**. Downloading audio is [seemingly unsolved](https://github.com/yt-dlp/yt-dlp/issues/4237#issuecomment-1172190572), so I've just converted the 
video to audio using **moviepy**. The file size for both audio and video is within 1% of what I get from 4K Video Downloader, which is a good sign.

The video defaults to 1080p and gets the highest resolution if 1080p is not available.
