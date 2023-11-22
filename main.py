from tkinter import Tk, Label, Entry, Button, StringVar
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def download_video():
    url = url_entry.get()
    output_path = output_path_entry.get().strip() or "."

    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Update labels with video information
        title_label.config(text="Title: " + yt.title)
        views_label.config(text="Views: " + str(yt.views))

        # Get the highest resolution stream
        yd = yt.streams.get_highest_resolution()

        # Specify the output path and download the video
        yd.download(output_path)

        status_var.set("Download complete.")
    except VideoUnavailable:
        status_var.set("The video is unavailable or private.")
    except Exception as e:
        status_var.set("An error occurred: " + str(e))

# Create the main window
root = Tk()
root.title("YouTube Video Downloader")

# URL entry
Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=5)
url_var = StringVar()
url_entry = Entry(root, textvariable=url_var, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Output path entry
Label(root, text="Output Path (default is current directory):").grid(row=1, column=0, padx=10, pady=5)
output_path_var = StringVar()
output_path_entry = Entry(root, textvariable=output_path_var, width=40)
output_path_entry.grid(row=1, column=1, padx=10, pady=5)

# Labels for video information
title_label = Label(root, text="Title: ")
title_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

views_label = Label(root, text="Views: ")
views_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Download button
download_button = Button(root, text="Download", command=download_video)
download_button.grid(row=4, column=0, columnspan=2, pady=10)

# Status label
status_var = StringVar()
status_label = Label(root, textvariable=status_var, fg="red")
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
