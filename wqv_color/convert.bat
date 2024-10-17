set /a Index=1
SETLOCAL ENABLEDELAYEDEXPANSION


::First use Jpeg the Ripper to convert pdb files into jpegs
::Jpeg the ripper is supposed to handle multiple jpegs in one bin,
::not a bunch of individual files. So rename the output jpgs manually.

for %%I in (pdb\*.pdb) do (
	"jpegrip.exe" %%n %%I
	rename "jpg00000000.jpg" "!Index!.jpg"
	set /a Index+=1
)


::Move all extracted files to work directory
for /r  %%x in (*.jpg) do move "%%x" "work"

::Execute python script on work files to clean up corruption
py -3 wqv3.py
