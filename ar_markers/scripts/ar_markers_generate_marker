#!/usr/bin/env python

import sys
from cv2 import imwrite

from ar_markers.hamming.marker import HammingMarker


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--generate':
            for i in range(int(sys.argv[2])):
                marker = HammingMarker.generate()
                imwrite('marker_images/marker_{}.png'.format(marker.id), marker.generate_image())
                print("Generated Marker with ID {}".format(marker.id))
        else:
            marker = HammingMarker(id=int(sys.argv[1]))
            imwrite('marker_images/marker_{}.png'.format(marker.id), marker.generate_image())
            print("Generated Marker with ID {}".format(marker.id))
    else:
        marker = HammingMarker.generate()
        imwrite('marker_images/marker_{}.png'.format(marker.id), marker.generate_image())
        print("Generated Marker with ID {}".format(marker.id))
    print('Done!')
