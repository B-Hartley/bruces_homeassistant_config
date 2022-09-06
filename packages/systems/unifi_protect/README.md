# Unifi Protect

I use the Custom Component from Briis - available through HACS or [GitHub](https://github.com/briis/unifiprotect)

The Last Motion Attribute is pulled out into a template sensor for each camera.

Each camera that handles object detection has its own detection script.
These could be combined into a single script, but having them seperate means that I can prevent any camera sending an alert more often than every 5 minutes.
I have a script mode of single, and a 5 minute delay at the end of the script.

The script when triggered will capture a short video, then send it to me by Telegram.
