tell application "Slack"
    set active_team to name of team of front window
    set active_channel to name of selected channel of front window
    return active_team & " - " & active_channel
end tell