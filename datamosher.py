# identify i-frames
# remove all but first i-frame

"""

Each video frame in the AVI file will start with the code 00dc,
you can search for these in the file (there will be a lot!).
About 1 in 25 of these will be an I-Frame (though this depends on things like what quality you saved it at, etc).
An I-Frame can be identified by the HEX string 00 01 B0 01 that will appear about 5 bytes after the 00dc frame start marker.
