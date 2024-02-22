from pytube import Youtube
try :
   # Ask the user to input the Youtube URL
   url = input("Enter the Youtube URL:")

   yt = Youtube(url)

   print("Title:", yt.title)
   print("Views:", yt.Views)

   # Get the highest resolution stream

   yd = yt.streams.get_highest_resoluiton()

   # Download the video to the current directory

   yd.download()

   print("Download Complete.")

   except Exception as e:

      print("An error occured:", str(e))


   


