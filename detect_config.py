import cv2 as cv
import argparse
import numpy as np
import os.path
import sys
import random


confThreshold = 0.5 # confidence threshold

# 绘制预测的边界框
def drawBox(frame, classId, conf, left, top, right, bottom, classMask):
    # 画边界框
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

    # 打印类别标签
    label = '%.2f' % conf
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    # 再边界框顶部显示标签
    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv.rectangle(frame, (left, top - round(1.5 * labelSize[1])), (left + round(1.5 * labelSize[0]), top + baseLine),
                 (255, 255, 255), cv.FILLED)
    cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)

    # 调整mask、阈值、颜色并将其应用于图像
    # classMask = cv.resize(classMask, (right - left + 1, bottom - top + 1))
    # mask = (classMask > maskThreshold)
    # roi = frame[top:bottom + 1, left:right + 1][mask]

    # color = colors[classId%len(colors)]
    # Comment the above line and uncomment the two lines below to generate different instance colors
    # colorIndex = random.randint(0, len(colors) - 1)
    # color = colors[colorIndex]

    # frame[top:bottom + 1, left:right + 1][mask] = ([0.3 * color[0], 0.3 * color[1], 0.3 * color[2]] + 0.7 * roi).astype(
    #     np.uint8)

    # Draw the contours on the image
    # 在图像上绘制轮廓
    # mask = mask.astype(np.uint8)
    # contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(frame[top:bottom + 1, left:right + 1], contours, -1, color, 3, cv.LINE_8, hierarchy, 100)


# 对于每一帧，为每个检测到的对象提取倒边界框
def postprocess(boxes):
    numDetections = boxes.shape[2]

    #frameH = frame.shape[0]


    for i in range(numDetections):
        box = boxes[0, 0, i]
        score = box[2]
        if score > confThreshold:
            classId = int(box[1])

            # 提取bounding box
            # left =


def detect(inputPath):
    classFile = "models/mscoco_labels.names"
    classes = None
    with open(classFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')

    # 权重文件和模型textGraph的路径
    modelWeights = "models/frozen_inference_graph.pb";
    textGraph = "models/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt";

    # 加载网络
    net = cv.dnn.readNetFromTensorflow(modelWeights, textGraph);
    net.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

    # Load the classes
    colorsFile = "colors.txt";
    with open(colorsFile, 'rt') as f:
        colorsStr = f.read().rstrip('\n').split('\n')
    colors = [] #[0,0,0]
    for i in range(len(colorsStr)):
        rgb = colorsStr[i].split(' ')
        color = np.array([float(rgb[0]), float(rgb[1]), float(rgb[2])])
        colors.append(color)


    img = cv.imread(inputPath)
    outputFile = inputPath[:-4]+'_detect.jpg'
    print(classes)


    inputBlob = cv.dnn.blobFromImage(img, swapRB = True, crop=False)

    net.setInput(inputBlob)
    print("输入blob")
    detections = net.forward()
    print("向前计算")

    h = img.shape[0]
    w = img.shape[1]
    print(h, w)
    numDetections = detections.shape[2]
    for i in range(numDetections):
        score = detections[0, 0, i, 2]
        if score > confThreshold:
            # 从detections中提取类标签的索引
            idx = int(detections[0, 0, i, 1])
            print("idx:", idx)
            # 计算物体边界框的（X,Y) 坐标
            startX = int(w * detections[0, 0, i, 3])
            startY  = int(h * detections[0, 0, i, 4])
            endX = int(w * detections[0, 0, i, 5])
            endY = int(h * detections[0, 0, i, 6])

            # startX = max(0, min(startX, w - 1))
            # startY = max(0, min(startY, h - 1))
            # endX = max(0, min(endX, w - 1))
            # endY = max(0, min(endY, h - 1))

            #显示预测
            label = "{}: {:.2f}%".format(classes[idx], score * 100)
            print("[INFO] {}".format(label))
            cv.rectangle(img, (startX, startY), (endX, endY), colors[idx], 2)
            #y = startY - 15 if startY - 15 > 15 else startY + 15
            cv.putText(img, label, (startX, startY),
                           cv.FONT_HERSHEY_SIMPLEX, 0.75, colors[idx])

    # 展示输出图像
    # cv.imshow("output", img)
    cv.imwrite(outputFile, img)

    return outputFile


