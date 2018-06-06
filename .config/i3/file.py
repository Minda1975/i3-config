from i3pystatus import Status

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X KW%V",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Displays whether a DHCP client is running
status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{used}/{total}G [{avail}G]",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)
    
# Shows cmus status
# Format:
# Cloud connected▶Reroute to Remain
status.register("cmus",
    format="{artist}{status}{album}",
    status={
        "paused": "▷",
        "playing": "▶",
        "stopped": "◾",
    },)
    
status.register("cpu_usage",
format="CPU {usage}%")

status.register("uptime",
    format="Up {hours}:{mins}:{secs}")
  

status.run()
