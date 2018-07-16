FOR /F "delims=|" %%A IN ("%cd%") DO (
    SET _FOLDERNAME=%%~nxA
)

::open cmd and execute the workon + foldername
start cmd /k workon %_FOLDERNAME%