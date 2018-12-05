**This project is unmaintained and just here fore historical reasons!***

python-ar-markers
=================

Detection of hamming markers for OpenCV written in python.

This package is able to read and create hamming markers, described in [this](https://web.archive.org/web/20180104190717/http://iplimage.com/blog/approach-encodedecode-black-white-marker/) blogpost.

Helperscripts
-------------

There are two helperscripts located in `ar_markers/scripts`. `generate_marker` to generate the markers and `livetest`. To do the `livetest`, first generate some markers and print them out. After that, start the livetest and hold the marker into your camera. You will see a blue border around the marker, (if detected) and a green number, showing the ID the marker represents.
