#!/usr/bin/env python

import cv2

from ar_markers.hamming.detect import detect_markers

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)

    if capture.isOpened(): # try to get the first frame
        frame_captured, frame = capture.read()
    else:
        frame_captured = False
    while frame_captured:
        markers = detect_markers(frame)
        for marker in markers:
            marker.highlite_marker(frame)
        cv2.imshow('Test Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame_captured, frame = capture.read()

    # When everything done, release the capture
    capture.release()
    cv2.destroyAllWindows()
