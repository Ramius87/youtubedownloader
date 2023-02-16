from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Importing long video clip
required_video_file = "Welcome To The Moulin Rouge!.mp4"

# Reading times.txt to identify the cutting times
with open("times.txt") as f:
  times = f.readlines()

# Stripping down the times so python could read it better
times = [x.strip() for x in times] 

# Cutting the video to the necessary lengths
for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  # Saving the cut videos with different names
  ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mp4")