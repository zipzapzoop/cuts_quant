# cuts_quant
Python script to quantify cuts in video media.

This is my first serious python project. This script detects cuts in video files by quantifying white space in individual frames, summing the value for several frames, and comparing that sum to the sum from an adjacent segment. Borderline cuts are detected by comparing the last segment measured to third from last segment measured. That is, if the sum of white space found in frames from seconds three and four were compared and found to be borderline, the sum of white space measured for second two would be compared to the sum of white space measured for second four.
