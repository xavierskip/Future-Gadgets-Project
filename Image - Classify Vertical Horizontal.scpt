on adding folder items to this_folder after receiving added_items
	tell application "Finder"
		if not (exists folder "vertical" of this_folder) then
			make new folder at this_folder with properties {name:"vertical"}
		end if
		if not (exists folder "horizontal" of this_folder) then
			make new folder at this_folder with properties {name:"horizontal"}
		end if
		set the vertical_folder to folder "vertical" of this_folder as alias
		set the horizontal_folder to folder "horizontal" of this_folder as alias
	end tell
	repeat with i from 1 to the count of added_items
		try
			set this_file to (item i of added_items as alias)
			tell application "Image Events"
				launch
				set my_image to open this_file
				set my_dimensions to dimensions of my_image
				close my_image
				set pic_x to item 1 of my_dimensions as integer
				set pic_y to item 2 of my_dimensions as integer
				
				if pic_x < pic_y then
					tell application "Finder" to move file this_file to vertical_folder
				else
					tell application "Finder" to move file this_file to horizontal_folder
				end if
				quit
			end tell
		end try
	end repeat
end adding folder items to