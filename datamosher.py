# identify i-frames
# remove all but first i-frame OR delete certain iFrames

"""

Each video frame in the AVI file will start with the code 00dc,
you can search for these in the file (there will be a lot!).
About 1 in 25 of these will be an I-Frame (though this depends on things like what quality you saved it at, etc).
An I-Frame can be identified by the HEX string 00 01 B0 01 that will appear about 5 bytes after the 00dc frame start marker.

"""

#open file

source_vid = raw_input("Choose a file to mosh:")

readfile=open(source_vid, "r")

with open(source_vid+"_moshed", "w") as outfile:
  new_vid = "" #define new video
  
  iframes = [] #list of iframes
  
  #notes about slicing
  """
  list[0:4] returns a slice (another list) of the beginning of the list to the 5th item.
  
  Below is a test to check for wubs.
  
  for i in range(len(blam)):
    if blam[i] == 'd':
		  if blam[i:i+12] == 'drop the beat':
			  print 'sweet wubs' 
  """
  
  #sudo code
  """
  loop through data
  	if data starts with the right thing:
  		look for slice. if slice is correct:
  			continue loop through data for next frame. if next frame:
  				create slice
  				add to list of iFrames
  				
  option 1: write out new file, skip over any known iFrames
  option 2: write out everything, delete selected iFrames
  """
  outfile.write(new_vid)
  
readfile.close() #this is necessary, right?
