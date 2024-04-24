![image](https://github.com/Computational-Plant-Science/Drone-Based-Fusarium-Wilt-Detection-in-Lettuce-Using-RGB-Imagery/assets/133724174/80016099-0c55-454c-a377-3927c19bd8d1)

Fig 1. Example of lettuce image, (a) Image capture by a drone at Yuma agricultural (Size: 3000 x 4000) (b) Fusarium affected lettuce (Source internet) 

# Introduction:
Lettuce cultivation faces significant challenges from Fusarium wilt, a fungal disease that can cause considerable damage to crops. This problem is exacerbated by factors such as climate change and declining pollinator populations. Traditional methods for identifying Fusarium wilt, such as manual inspection or handheld devices, are time-consuming and often inefficient, leading to delays in disease detection and management.
To address these challenges, this study proposes a novel drone-based technique for Fusarium wilt detection in lettuce using RGB imagery. Drones offer a faster and more cost-effective solution compared to traditional methods, allowing for efficient monitoring of large agricultural areas. High-dimensional images, sized 3000 x 4000 pixels, were collected by a drone at an altitude of 10 meters over a span of two months at the Yuma Agricultural Center.
As shown in Figure 2, we created image patches from the full image to enlarge the images for detailed evaluation of each pixel, enabling precise analysis of Fusarium wilt symptoms. We then assess the light Tan intensity within these patches, as it provides a reliable measure for distinguishing Fusarium wilt-infected areas from non-infected ones. Subsequently, we use contour detection to identify Fusarium-infected regions, followed by a mosaicking technique to reconstruct the stretched image from the patches.

![image](https://github.com/Computational-Plant-Science/Drone-Based-Fusarium-Wilt-Detection-in-Lettuce-Using-RGB-Imagery/assets/133724174/b47f4582-0b42-4872-b808-99557e7526e2)
Fig 2. The framework for detecting Fusarium wilt consists of two distinct sub-processes implemented to detect fusarium. The first process is designed to detect potential Fusarium, while the second one aims to discard false positives using a neural network. The process inside the dotted box was implemented so far to detect all potential fusarium.

# Data Collection:
![image](https://github.com/Computational-Plant-Science/Drone-Based-Fusarium-Wilt-Detection-in-Lettuce-Using-RGB-Imagery/assets/133724174/6dc7a528-2b7b-4fe0-83f2-51a5aac8284f)
Fig 3. Data Collection Timeline 

Nine weeks of data were collected over a two-month period at the Yuma Agricultural Center. During the first week, data was collected twice. No data was collected in the 7th week due to some reasons. In total, 7,257 RGB images were collected for analysis. 

# How to Run the script:
Run the fusarium_detection_Tan_intensity.py, and it will automatically load a test image, and detect potential fusarium with boundary box. The input image is a patches with a 
size of 300 x 300. 

![image](https://github.com/Computational-Plant-Science/Drone-Based-Fusarium-Wilt-Detection-in-Lettuce-Using-RGB-Imagery/assets/133724174/23d00252-a596-4d82-b448-197211d4108f)
Fig 4. Experimental results 
# Performance:
We evaluated our technique with 10 image patches, containing a total of 68 Fusarium instances. The model detected 63 Fusarium instances, while 5 were missed. Overall, our approach achieves a high precision rate of 92.65% for almost all types of Fusarium, except for a few serious Fusarium cases due to their resemblance to soil color. Excluding serious Fusarium, the precision rate was over 99%.
However, the model also detected 40 instances of non-Fusarium due to their high-intensity lettuce. The model's false positive rate for non-Fusarium instances is quite high, indicating a need for improvement. Our next goal is to integrate a deep learning model, such as ResNet or YOLO, to reduce false positives and improve the overall accuracy of the detection method. Additionally, we will evaluate the severity of Fusarium infections, ensuring comprehensive disease management strategies.




