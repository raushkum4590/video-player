import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import pygame

class VideoPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Video Player")
        self.window.geometry("800x600")

        self.video_path = None
        self.clip = None
        self.paused = False

        self.label = tk.Label(window, text="Video Player", font=("Arial", 20))
        self.label.pack(pady=20)

        self.btn_select = tk.Button(window, text="Select Video", command=self.select_video, font=("Arial", 12))
        self.btn_select.pack()

        self.btn_play = tk.Button(window, text="Play", command=self.play_pause_video, font=("Arial", 12))
        self.btn_play.pack()

        self.btn_stop = tk.Button(window, text="Stop", command=self.stop_video, font=("Arial", 12))
        self.btn_stop.pack()

        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Initialize pygame mixer
        pygame.init()
        pygame.mixer.init()

    def select_video(self):
        self.video_path = filedialog.askopenfilename(initialdir="./", title="Select Video",
                                                     filetypes=(("Video files", "*.mp4;*.avi"), ("All files", "*.*")))

    def play_pause_video(self):
        if self.video_path:
            if self.clip is None or self.paused:
                self.clip = VideoFileClip(self.video_path)
                self.paused = False
                self.clip.preview()
                pygame.mixer.music.load(self.video_path)
                pygame.mixer.music.play(-1)  # Play audio in a loop
            else:
                self.paused = True

            self.update_frame()

    def stop_video(self):
        if self.clip:
            self.clip.close()
            self.canvas.delete("all")
            pygame.mixer.music.stop()

    def update_frame(self):
        if not self.paused:
            self.window.after(30, self.update_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()
