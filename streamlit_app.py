import streamlit as st
import re
import youtube_downloader
from dataclasses import dataclass
from enum import IntEnum


class AudioOrVideo(IntEnum):
    VIDEO = 1
    AUDIO = 2
    BOTH = 3


@dataclass
class Download:
    title: str
    id: str
    video_or_audio: AudioOrVideo


def page_setup():
    st.set_page_config(page_title="YT Downloader", page_icon="🎥", layout="wide", )
    hide_streamlit_style = """
                           <style>
                           #MainMenu {visibility: hidden;}
                           footer {visibility: hidden;}
                           .css-hxt7ib {padding-top: 0rem;}
                           </style>
                           """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    if "dl_list" not in st.session_state:
        st.session_state.dl_list = []


def display_download_info(title, video, audio):
    dl_options = []
    if video:
        dl_options.append("video")
    if audio:
        dl_options.append("audio")
    st.sidebar.write(f"Downloading {', '.join(dl_options)} from \"{title}\"")


def render_download(dl_item):
    st.write(f"### {dl_item.title}")
    col1, col2 = st.columns(2)

    # if audio only, render it in col 1, otherwise col1 will be video and col2 will be audio
    if dl_item.video_or_audio == AudioOrVideo.AUDIO:
        audio_name = f"{dl_item.id}.mp3"
        with open(audio_name, 'rb') as file:
            st.download_button(label="Download Audio", data=file, file_name=audio_name, mime="audio/mpeg")
        return
    # from here and down we know it's video or both, so render video in col1
    video_name = f"{dl_item.id}.mp4"
    with open(video_name, 'rb') as file:
        col1.download_button(label="Download Video", data=file, file_name=video_name, mime="video/mp4")
    # lastly, if there's audio, put it in col2
    if dl_item.video_or_audio == AudioOrVideo.BOTH:
        audio_name = f"{dl_item.id}.mp3"
        with open(audio_name, 'rb') as file2:
            col2.download_button(label="Download Audio", data=file2, file_name=audio_name, mime="audio/mpeg")


class StreamlitYoutubeDownloader:
    def __init__(self):
        self.link_error = None
        page_setup()

    def start(self):
        st.sidebar.write("# YouTube Downloader")
        st.sidebar.write("Enter a link below, select if you want video and/or audio downloaded, and click Download!")
        form = st.sidebar.form("Link")
        link = form.text_input("Enter link below")
        self.link_error = form.empty()
        video = form.checkbox("Video")
        audio = form.checkbox("Audio")
        if form.form_submit_button("Download"):
            self.download(link, video, audio)
        print(st.session_state.dl_list)
        for dl_item in st.session_state.dl_list:
            render_download(dl_item)

    def download(self, link, video, audio):
        matcher = re.match(r"https?://(?:www\.)?youtu(?:be\.com/watch\?v=|\.be/)([\w\-_]*)(&(amp;)?‌​[\w?‌​=]*)?", link)

        if matcher.group(1):
            video_id = matcher.group(1)
            title = youtube_downloader.get_title(link)
            video_file_name = f"{video_id}.mp4"
            display_download_info(title, video, audio)

            download_obj = Download(title, video_id, AudioOrVideo(video + 2 * audio))
            # 0 is a successful download
            video_ret = 0
            audio_ret = 0
            if video:
                video_ret = youtube_downloader.download_video(link, video_id)
            if audio:
                audio_file_name = f"{video_id}.mp3"
                youtube_downloader.mp4_to_mp3(video_file_name, audio_file_name)
            if video_ret != 0 or audio_ret != 0:
                st.error("Error while downloading video or audio")
                return
            st.session_state.dl_list.append(download_obj)

        else:
            self.link_error.error("Invalid YouTube link")
            return
        if not (video or audio):
            st.sidebar.error("Please select video or audio.")
            return


if __name__ == '__main__':
    syd = StreamlitYoutubeDownloader()
    syd.start()