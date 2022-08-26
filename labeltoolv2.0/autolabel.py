import cv2 as cv
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
# from window import Ui_MainWindow
confThreshold = 0.5




def detect(imgName, class_name):

    # if imgName == "":
    #     return "The image path is none."
    # elif class_name == "":
    #     return "Please select the label object you want to detect."


    print(imgName, class_name)
    classFile = "models/maskrcnn/mscoco_labels.names"
    classes = None
    with open(classFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')

    # 权重文件和模型textGraph的路径
    modelWeights = "models/maskrcnn/frozen_inference_graph.pb";
    textGraph = "models/maskrcnn/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt";

    yoloModel = "models/yolo/yolov7.onnx"

    # 加载网络
    net = cv.dnn.readNetFromONNX(yoloModel);
    net1 = cv.dnn.readNetFromONNX(modelWeights, textGraph);
    # net.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)
    print("using GPU device")

    # Load the classes
    colorsFile = "colors.txt";
    with open(colorsFile, 'rt') as f:
        colorsStr = f.read().rstrip('\n').split('\n')
    colors = []  # [0,0,0]
    for i in range(len(colorsStr)):
        rgb = colorsStr[i].split(' ')
        color = np.array([float(rgb[0]), float(rgb[1]), float(rgb[2])])
        colors.append(color)
    # 读入图片文件
    cap = cv.VideoCapture(imgName)
    hasFrame, frame = cap.read()
    # img = cv.imread(inputPath)
    outputFile = imgName[:-4] + '_detect.jpg'
    print(classes)
    # Stop 当没有frame的时候
    if not hasFrame:
        print("处理完成!!!")
        print("输出的图片为：", outputFile)
        cv.waitKey(5000)
        return

    print("hasFrame, frame:", hasFrame, frame)
    inputBlob = cv.dnn.blobFromImage(frame, swapRB=True, crop=False)

    # 输入网络中
    net.setInput(inputBlob)
    print("输入blob")

    # 向前计算
    boxes, masks = net.forward(['detection_out_final', 'detection_masks'])
    print("向前计算")

    '''
    开始对于每一帧， 为每个检测到的对象提取bbox和mask
    '''
    numClasses = masks.shape[1]
    numDetections = boxes.shape[2]

    frameH = frame.shape[0]
    frameW = frame.shape[1]
    print("frameH, frameW:", frameH, frameW)
    for i in range(numDetections):
        box = boxes[0, 0, i]
        mask = masks[i]
        score = box[2]
        classId = int(box[1])
        if score > confThreshold and classes[classId] == class_name:

            # 提取bbox信息
            left = int(frameW * box[3])
            top = int(frameH * box[4])
            right = int(frameW * box[5])
            bottom = int(frameH * box[6])
            print("box3, box4, box5, box6", box[3], box[4], box[5], box[6])

            left = max(0, min(left, frameW - 1))
            top = max(0, min(top, frameH - 1))
            right = max(0, min(right, frameW - 1))
            bottom = max(0, min(bottom, frameH - 1))
            print("left, top, right, bottom", left, top, right, bottom)

            x_ = (left + right) / (2 * frameW)
            y_ = (top + bottom) / (2 * frameH)
            w_ = (right - left) / frameW
            h_ = (bottom - top) / frameH
            print("x_, y_, w_, h_", format(x_, '.6f'), format(y_, '.6f'), format(w_, '.6f'), format(h_, '.6f'))
            save_as_yolo(outputFile, format(x_, '.6f'), format(y_, '.6f'), format(w_, '.6f'), format(h_, '.6f'))
            # 画bbox的边框
            cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

            # 打印类别标签
            label = '%.2f' % score
            if classes:
                assert (classId < len(classes))
                label = '%s:%s' % (classes[classId], label)

            # 在bbox顶部显示标签
            labelSize, baseline = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            top = max(top, labelSize[1])
            cv.rectangle(frame, (left, top - round(1.5 * labelSize[1])),
                         (left + round(1.5 * labelSize[0]), top + baseline), (255, 255, 255), cv.FILLED)
            cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)

    cv.imwrite(outputFile, frame.astype(np.uint8))
    return outputFile


def save_as_yolo(outputpath, x, y, w, h):
    outputFile = outputpath[:-11] + '.txt'
    with open(outputFile, 'a+') as file_handle:
        classnum = 4
        file_handle.write(str(classnum) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')
    file_handle.close()