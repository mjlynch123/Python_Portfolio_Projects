from pytube import YouTube

url = input("Please enter the link: ")
yt = YouTube(url)

print("Title: {}".format(yt.title))
print("Views: {}".format(yt.views))
print("Ratings: {}".format(yt.rating))

res = yt.streams.get_highest_resolution()

res.download('''Path to download folder''')