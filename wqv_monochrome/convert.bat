::Start by dividing the pdb into individual files
par x pdb/wqvlinkdb.pdb

::move all extracted files to source directory
for /r  %%x in (*.pdr) do move "%%x" "work"
::for /r  %%x in (*.pdr) do move "%%x" work

::execute python script to extract bitmaps
py -3 wqv.py