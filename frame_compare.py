import wpix_count_video as pxc
import itertools

v_file = input('Show me whatcha got!: ')

sample1 = []
sample2 = []
i=0
switch = True
ratio = 0
temp = 0
ratio_mod = 0.000
for ret, wpx_v in pxc.wpix_count(v_file):
    time = (i/25.00)
    if ret == True and switch == True:
        
        sample1.append(wpx_v)
        i = i+1

        if i%5 == 0: 
            switch = False ; x = sum(sample1[:5])

    elif ret == True and switch == False:
        sample2.append(wpx_v)
        i = i+1

        if i%5 == 0:
            switch = True ; y = sum(sample2[:5])

    if i != 0 and i%10 == 0:

        if x !=0:
            ratio = y/x

            if ratio >= 1.00:
                ratio = 1/ratio
            else:
                pass

        if abs(ratio)<0.400:
            print('Scene Change at: ', time,'sec')

        elif temp > 0 and 0.01 < ratio < 0.8:
            
            ratio_mod = (y/temp)
   
            if ratio_mod >= 1.00:
                ratio_mod = 1/ratio_mod
           
            if ratio_mod < 0.400:
               print('Scene Change at: ', time,'sec')

        temp = sum(sample1[:5])
        sample1 = []
        sample2 = []
