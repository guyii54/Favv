import cv2
import os

def seq2avi():
    seq_dir = r'G:\Dataset\PAMIRain\Dataset824\train\Bs'
    avi_dir = r'G:\Dataset\PAMIRain\Dataset824\train\testwrite.avi'
    img_list = os.listdir(seq_dir)

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    writer = cv2.VideoWriter(avi_dir, fourcc, 20.0, (256, 256))

    for name in img_list:
        img = cv2.imread(os.path.join(seq_dir, name))
        writer.write(img)

def avi2seq():
    import shutil
    from os.path import join
    seq_dir = r'G:\Dataset\PAMIRain\Dataset825\train\Os'
    raw_dir = r'G:\Dataset\PAMIRain\Dataset825\train\Bs'
    avi_dir = r'G:\Dataset\PAMIRain\Dataset825\big.avi'

    raw_img_list = os.listdir(raw_dir)
    reader = cv2.VideoCapture(avi_dir)

    index = 0
    while True:
        # ret, img = reader.read()
        shutil.copy(join(raw_dir, raw_img_list[index]), join(raw_dir, 'middle_'+raw_img_list[index]))
        shutil.copy(join(raw_dir, raw_img_list[index]), join(raw_dir, 'small_'+raw_img_list[index]))
        # save_name = os.path.join(seq_dir, 'big_'+raw_img_list[index])
        # cv2.imwrite(save_name, img)
        index += 1

if __name__ == '__main__':
    # seq2avi()
    avi2seq()