@echo off
rem 

echo Creating executable for termini...

rem --- Configuration ---
set "EXECUTABLE_NAME=termini.bat"

rem --- Script ---

rem Get the absolute path of the directory containing this install script.
rem This is assumed to be the project's root directory.
set "PROJECT_PATH=%~dp0"
rem Remove the trailing backslash
if "%PROJECT_PATH:~-1%"=="\" set "PROJECT_PATH=%PROJECT_PATH:~0,-1%"

echo Project path detected: %PROJECT_PATH%

rem Create the content of the executable script.
rem This will be written into the new .bat file.
rem It changes to the project directory, activates the virtual environment,
rem runs the python script with all arguments, and then returns to the original directory.
(
    echo @echo off
    echo rem Save the current directory before changing it
    echo set "ORIGINAL_DIR=%%CD%%"
    echo.
    echo rem Change to the project directory. The /d switch handles changing drives if necessary.
    echo cd /d "%PROJECT_PATH%"
    echo.
    echo rem Activate the virtual environment
    echo call .venv\Scripts\activate.bat
    echo.
    echo rem Run the python script, passing all command-line arguments (%%*)
    echo python termini\main.py %%*
    echo.
    echo rem Return to the original directory
    echo cd /d "%%ORIGINAL_DIR%%"
) > %EXECUTABLE_NAME%

echo.
echo ======================================================================
echo.
echo ^<DONE^> Created the executable script: %EXECUTABLE_NAME%
echo.
echo To run the '%EXECUTABLE_NAME%' command from anywhere, you must add it to your PATH:
echo.
echo 1. Move the "%EXECUTABLE_NAME%" file to a permanent folder (e.g., C:\Users\YourUser\Scripts).
echo 2. Search for "Edit the system environment variables" in the Start Menu and open it.
echo 3. Click the "Environment Variables..." button.
echo 4. In the "User variables" section, select the "Path" variable and click "Edit...".
echo 5. Click "New" and paste the path to the folder where you moved the script (e.g., C:\Users\YourUser\Scripts).
echo 6. Click OK on all windows. You may need to restart your terminal (cmd/PowerShell) for the changes to take effect.
echo.
echo ======================================================================
