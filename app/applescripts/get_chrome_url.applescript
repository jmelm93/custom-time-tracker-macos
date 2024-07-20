-- def get_chrome_url():
--     script = """
--     tell application "Google Chrome"
--         get URL of active tab of front window
--     end tell
--     """
--     result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
--     if result.returncode == 0:
--         return result.stdout.strip()
--     else:
--         print(f"Error getting Chrome URL: {result.stderr}")
--         return None



-- Path: app/applescripts/google-chrome-url.applescript
tell application "Google Chrome"
    get URL of active tab of front window
end tell