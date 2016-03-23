try
	tell application "Finder" to set the this_folder to (folder of the front window) as alias
on error -- if there is no window open
	set the this_folder to path to desktop folder as alias
end try

display dialog "Enter the file name" default answer "Untitled.txt" with title "Create a new file" buttons {"Cancel", "Done"} default button "Done"
if the button returned of the result is "Done" then
	set thefilename to text returned of the result
	set thefullpath to POSIX path of this_folder & thefilename
	do shell script "touch \"" & thefullpath & "\""
end if