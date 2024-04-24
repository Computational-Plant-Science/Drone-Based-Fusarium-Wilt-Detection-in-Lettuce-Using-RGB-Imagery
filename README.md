# Introduction:
Lettuce cultivation faces significant challenges from Fusarium wilt, a fungal disease that can cause considerable damage to crops. This problem is exacerbated by factors such as climate change and declining pollinator populations. Traditional methods for identifying Fusarium wilt, such as manual inspection or handheld devices, are time-consuming and often inefficient, leading to delays in disease detection and management.
To address these challenges, this study proposes a novel drone-based technique for Fusarium wilt detection in lettuce using RGB imagery. Drones offer a faster and more cost-effective solution compared to traditional methods, allowing for efficient monitoring of large agricultural areas. High-dimensional images, sized 3000 x 4000 pixels, were collected by a drone at an altitude of 10 meters over a span of two months at the Yuma Agricultural Center.
As shown in Figure 1, we created image patches from the full image to enlarge the images for detailed evaluation of each pixel, enabling precise analysis of Fusarium wilt symptoms. We then assess the light Tan intensity within these patches, as it provides a reliable measure for distinguishing Fusarium wilt-infected areas from non-infected ones. Subsequently, we use contour detection to identify Fusarium-infected regions, followed by a mosaicking technique to reconstruct the stretched image from the patches.

# Data Collection:
![image](https://github.com/Computational-Plant-Science/Drone-Based-Fusarium-Wilt-Detection-in-Lettuce-Using-RGB-Imagery/assets/133724174/6dc7a528-2b7b-4fe0-83f2-51a5aac8284f)
Data Collection Timeline 

Nine weeks of data were collected over a two-month period at the Yuma Agricultural Center. During the first week, data was collected twice. No data was collected in the 7th week due to some reasons. In total, 7,257 RGB images were collected for analysis.


