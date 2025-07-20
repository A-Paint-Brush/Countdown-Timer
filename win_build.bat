@echo off
rem Activate Python virtual environment first before running this script.
md "dist\Countdown Timer\Data"
xcopy "Images" "dist\Countdown Timer\Images\" /e
xcopy "Ringtones" "dist\Countdown Timer\Ringtones\" /e
pyinstaller --distpath "dist\Countdown Timer" "win_compile.spec"
