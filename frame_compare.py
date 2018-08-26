import wpix_count_video as pxc
import itertools



def count_jcuts():
    sample1 = []
    sample2 = []
    i=0
    switch = True
    skip = False
    ratio = 0
    temp = 0
    ratio_mod = 0.000
    v_file = input('Provide name of video file to be analyzed (abc.zxy): ')
    reset = 0
    fps = pxc.fps(v_file)
    print(fps)

## grabs white value output from wpix_count_video for 10 frames
    
    for ret, wpx_v in pxc.wpix_count(v_file):
        if ret == True and switch == True:
            
            sample1.append(wpx_v)
            i += 1
            if i%5 == 0: 
                switch = False ; x = sum(sample1[:5])

        elif ret == True and switch == False:
            sample2.append(wpx_v)
            i += 1

            if i%5 == 0:
                switch = True ; y = sum(sample2[:5])      

##Checks if a scene change was detected in the last 10 frames
##if so the next 10 frames are not checked
        if skip == True and i%10 == 0:
            reset += 1
            if reset == 2:
                reset = 0
                skip = False
                
                
        if skip == False and i%10 == 0:
            time = (i/fps)
            if x !=0:
                ratio = y/x

                if ratio >= 1.00:
                    ratio = 1/ratio
                else:
                    pass
## Compares white pixel count for two five frame segments
## If the ratio is less than .400, it registers as a cut
            if abs(ratio)<0.400:
                print('Scene Change at: ', time,'sec') ; skip = True
## Secondary check for borderline cases
## Uses x value from previous 10pix seg. for comparison with y from current 10pix seg.
## Helps detect fade cuts

            elif temp > 0 and 0.01 < ratio < 0.8:
            
                ratio_mod = (y/temp)
   
                if ratio_mod >= 1.00:
                    ratio_mod = 1/ratio_mod
           
                if ratio_mod < 0.400:
                    print('Scene Change at: ', time,'sec') ; skip = True
## Stores x value for borderline comparisons
## Wipes sample1 and sample2 list
        temp = sum(sample1[:5])
        sample1 = []
        sample2 = []
            
