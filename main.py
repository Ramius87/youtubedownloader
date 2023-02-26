import tkinter
import tkinter.messagebox
import customtkinter
import download

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Youtube Downloader")
        self.geometry(f"{800}x{480}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1,2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create link entry and download button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Youtube Link")
        self.entry.grid(row=0, column=0, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="ew")

        self.download_button = customtkinter.CTkButton(master=self, text="Download", command=self.download_button_event)
        self.download_button.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="ew")

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=2, column=0, columnspan=4, padx=20, pady=(20, 20), sticky="nsew")

    def download_button_event(self):
        #download.download_video(self.entry.get)
        #self.textbox.insert("insert", self.entry.get() + "\n")
        self.textbox.insert("insert", download.get_video_information(self.entry.get()) + "\n")
        print(download.get_video_information(self.entry.get()))
        download.download_playlist(self.entry.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()