import cv2
import os

def seq2avi():
    seq_dir = r'G:\Dataset\PAMIRain\Dataset831\train\Bs'
    avi_dir = r'G:\Dataset\PAMIRain\Dataset831\train\Bs.avi'
    img_list = os.listdir(seq_dir)

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    writer = cv2.VideoWriter(avi_dir, fourcc, 20.0, (256, 256))

    for name in img_list:
        img = cv2.imread(os.path.join(seq_dir, name))
        writer.write(img)

def avi2seq():
    import shutil
    from os.path import join
    import fnmatch
    seq_dir = r'G:\Dataset\PAMIRain\Dataset831\train\Os'
    raw_dir = r'G:\Dataset\PAMIRain\Dataset831\train\Bs'
    avi_dir = r'G:\Dataset\PAMIRain\Dataset831\train\middle.avi'

    raw_img_list = os.listdir(raw_dir)
    # name_list = fnmatch.filter(raw_img_list, 'big_*')

    reader = cv2.VideoCapture(avi_dir)

    index = 0
    while True:
        # ret, img = reader.read()
        # save_name = os.path.join(seq_dir, 'middle_'+raw_img_list[index])
        # cv2.imwrite(save_name, img)

        shutil.copy(join(raw_dir, raw_img_list[index]), join(raw_dir, 'middle_' + raw_img_list[index]))
        shutil.copy(join(raw_dir, raw_img_list[index]), join(raw_dir, 'small_' + raw_img_list[index]))
        shutil.copy(join(raw_dir, raw_img_list[index]), join(raw_dir, 'big_' + raw_img_list[index]))
        index += 1

if __name__ == '__main__':
    # seq2avi()
    avi2seq()