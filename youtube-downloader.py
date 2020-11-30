# Import modules
import youtube_dl

# Declare variables & arrays
links = []
opt = 1

# Interaction with user
while opt > 0:
    link = input('Video URL: ')
    links.append(link)
    opt = int(input('Type (1) to add another link and (0) to quit: '))

# Download procedure
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(links)