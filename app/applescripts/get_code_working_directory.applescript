-- -- applescript: get the window path reference of the frontmost window of Visual Studio Code
-- tell application "Visual Studio Code"
--     -- Error running get_code_working_directory.applescript: /Users/jasonmelman/dev/time-tracker/app/applescripts/get_code_working_directory.applescript:155:159: script error: Expected end of line but found “text”. (-2741)
--     set window_path to file of active text editor of front window
--     set window_path to POSIX path of window_path
--     return window_path
-- end tell

tell application "Visual Studio Code"
    set window_path to path of active text editor of front window
    set window_path to POSIX path of window_path
    return window_path
end tell