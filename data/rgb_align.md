# Images of the Russian Empire: Colorizing the Prokudin-Gorskii photo collection

## Description
Sergei Mikhailovich Prokudin-Gorskii had an idea to create colored images
using the tools available to him. His idea was simple: record three exposures
of every scene onto a glass plate using a red, a green, and a blue filter.
Never mind that there was no way to print color photographs until much later
-- he envisioned special projectors to be installed in "multimedia" classrooms
all across Russia where the children would be able to learn about their vast
country. The result was a series of photos that are for the red, green, and
blue channels. The goal of this project is to align the channels and create a
colored image.

This project experiments with 3 different alignment strategies: Euclidean
Distance (Mean Square Difference), Normalized Cross Correlation, and Sobel Edge
Detection.

<!-- ## Method
Let the two channels be $c_1, c_2$. Let the shift functions be $\text{shift}_x(k, c)$, $\text{shift}_y (k, c)$, which shifts an image $c$ in the $x$ and $y$ directions by $k$ pixels.

### Euclidean Distance (Mean Squared Difference)
For this method we compute the Euclidean Distance bewtween the channels. We seek to minimize this distance due to our assumption that bright areas should be bright across all channels. Thus let the shifted channel 1 be $c_1'$, then
$$c_1' = \text{shift}_y(y, \text{shift}_x(x, c_1)) $$
We then find
$$(x, y) = \text{argmin}_{x, y} \sqrt{(c_1 - c_2)^2}$$
where $x, y \in [-15, 15]$

### Normalized Cross Correlation (NCC)
For this method we compute the Cross Correlation. We seek to maximize this since we believe that areas in which the image is bright __relative__ to the rest of the image should be __relatively__ bright in all channels. This improves upon MSD since it there may be images that are brighter for an entire channel, which throws off the metric. Let the normalized channels be $c_1', c_2'$ 
$$c_i = \frac{c_i}{||c_i||} - 0.5 \times \vec{1}$$
This normalizes the mean and variance of the vectors.
let the shifted channel 1 be $c_1''$, then
$$c_1' = \text{shift}_y(y, \text{shift}_x(x, c_1')) $$

We then find
$$(x, y) = \text{argmax}_{x, y} c_1'' \cdot c_2'$$
where $x, y \in [-15, 15]$

### Sobel Edge Detection (NCC)
For this method we still compute the Cross Correlation and seek to maximize this. However, the features are no longer the pixel values, but the edge features created by the Sobel Edge Extractor. Let the extracted features channels be $c_1', c_2'$ 
$$c_i = \text{Sobel}(c_1)$$
Since Sobel already normalizes, we do not need to normalize again.
Let the shifted channel 1 be $c_1''$, then
$$c_1' = \text{shift}_y(y, \text{shift}_x(x, c_1')) $$

We then find
$$(x, y) = \text{argmax}_{x, y} c_1'' \cdot c_2'$$
where $x, y \in [-15, 15]$ -->

## Image Processing Results
MSD: Mean Squared Difference

NCC: Normalized Cross Correlation

SED: Sobel Edge Detection

| MSD| NCC  | SED |
| - | ------------- | ------------- |
| ![](../data/rgb_align/mse/emir.jpg) <br> Red-Blue Shift: [50, 22] <br> Green-Blue Shift: [-270, 254] | ![](../data/rgb_align/cc/emir.jpg) <br> Red-Blue Shift: [-3, 7] <br> Green-Blue Shift: [107, 17] | ![](../data/rgb_align/sobel/emir.jpg) <br> Red-Blue Shift: [49, 24] <br> Green-Blue Shift: [105, 41] |
| ![](../data/rgb_align/mse/church.jpg) <br> Red-Blue Shift: [25, 3] <br> Green-Blue Shift: [60, -5] | ![](../data/rgb_align/cc/church.jpg) <br> Red-Blue Shift: [0, -5] <br> Green-Blue Shift: [52, -6] | ![](../data/rgb_align/sobel/church.jpg) <br> Red-Blue Shift: [25, 3] <br> Green-Blue Shift: [58, -4] |
| ![](../data/rgb_align/mse/three_generations.jpg) <br> Red-Blue Shift: [56, 12] <br> Green-Blue Shift: [112, 12] | ![](../data/rgb_align/cc/three_generations.jpg) <br> Red-Blue Shift: [52, 5] <br> Green-Blue Shift: [108, 7] | ![](../data/rgb_align/sobel/three_generations.jpg) <br> Red-Blue Shift: [59, 16] <br> Green-Blue Shift: [115, 12] |
| ![](../data/rgb_align/mse/melons.jpg) <br> Red-Blue Shift: [260, 270] <br> Green-Blue Shift: [-138, -198] | ![](../data/rgb_align/cc/melons.jpg) <br> Red-Blue Shift: [83, 4] <br> Green-Blue Shift: [177, 8] | ![](../data/rgb_align/sobel/melons.jpg) <br> Red-Blue Shift: [79, 9] <br> Green-Blue Shift: [176, 14] |
| ![](../data/rgb_align/mse/onion_church.jpg) <br> Red-Blue Shift: [51, 27] <br> Green-Blue Shift: [109, 37] | ![](../data/rgb_align/cc/onion_church.jpg) <br> Red-Blue Shift: [52, 22] <br> Green-Blue Shift: [108, 35] | ![](../data/rgb_align/sobel/onion_church.jpg) <br> Red-Blue Shift: [50, 28] <br> Green-Blue Shift: [108, 35] |
| ![](../data/rgb_align/mse/train.jpg) <br> Red-Blue Shift: [-6, -8] <br> Green-Blue Shift: [84, 32] | ![](../data/rgb_align/cc/train.jpg) <br> Red-Blue Shift: [111, -7] <br> Green-Blue Shift: [107, 1] | ![](../data/rgb_align/sobel/train.jpg) <br> Red-Blue Shift: [53, 5] <br> Green-Blue Shift: [84, 28] |
| ![](../data/rgb_align/mse/icon.jpg) <br> Red-Blue Shift: [270, 165] <br> Green-Blue Shift: [268, 141] | ![](../data/rgb_align/cc/icon.jpg) <br> Red-Blue Shift: [42, 16] <br> Green-Blue Shift: [89, 22] | ![](../data/rgb_align/sobel/icon.jpg) <br> Red-Blue Shift: [39, 16] <br> Green-Blue Shift: [88, 23] |
| ![](../data/rgb_align/mse/self_portrait.jpg) <br> Red-Blue Shift: [-30, 250] <br> Green-Blue Shift: [-9, 172] | ![](../data/rgb_align/cc/self_portrait.jpg) <br> Red-Blue Shift: [50, -2] <br> Green-Blue Shift: [130, -5] | ![](../data/rgb_align/sobel/self_portrait.jpg) <br> Red-Blue Shift: [74, 25] <br> Green-Blue Shift: [175, 37] |
| ![](../data/rgb_align/mse/harvesters.jpg) <br> Red-Blue Shift: [-270, -231] <br> Green-Blue Shift: [-270, -226] | ![](../data/rgb_align/cc/harvesters.jpg) <br> Red-Blue Shift: [118, -3] <br> Green-Blue Shift: [120, 7] | ![](../data/rgb_align/sobel/harvesters.jpg) <br> Red-Blue Shift: [56, 11] <br> Green-Blue Shift: [118, 10] |
| ![](../data/rgb_align/mse/sculpture.jpg) <br> Red-Blue Shift: [-270, -222] <br> Green-Blue Shift: [-270, -222] | ![](../data/rgb_align/cc/sculpture.jpg) <br> Red-Blue Shift: [33, -11] <br> Green-Blue Shift: [140, -26] | ![](../data/rgb_align/sobel/sculpture.jpg) <br> Red-Blue Shift: [33, -11] <br> Green-Blue Shift: [140, -27] |
| ![](../data/rgb_align/mse/lady.jpg) <br> Red-Blue Shift: [54, 8] <br> Green-Blue Shift: [-138, -14] | ![](../data/rgb_align/cc/lady.jpg) <br> Red-Blue Shift: [57, -6] <br> Green-Blue Shift: [123, -17] | ![](../data/rgb_align/sobel/lady.jpg) <br> Red-Blue Shift: [57, 9] <br> Green-Blue Shift: [121, 13] |
| ![](../data/rgb_align/mse/monastery.jpg) <br> Red-Blue Shift: [-3, 2] <br> Green-Blue Shift: [3, 2] | ![](../data/rgb_align/cc/monastery.jpg) <br> Red-Blue Shift: [-6, 0] <br> Green-Blue Shift: [9, 1] | ![](../data/rgb_align/sobel/monastery.jpg) <br> Red-Blue Shift: [-3, 2] <br> Green-Blue Shift: [3, 2] |
| ![](../data/rgb_align/mse/tobolsk.jpg) <br> Red-Blue Shift: [3, 2] <br> Green-Blue Shift: [7, 3] | ![](../data/rgb_align/cc/tobolsk.jpg) <br> Red-Blue Shift: [3, 2] <br> Green-Blue Shift: [6, 3] | ![](../data/rgb_align/sobel/tobolsk.jpg) <br> Red-Blue Shift: [3, 2] <br> Green-Blue Shift: [6, 3] |
| ![](../data/rgb_align/mse/cathedral.jpg) <br> Red-Blue Shift: [-50, -138] <br> Green-Blue Shift: [-176, 172] | ![](../data/rgb_align/cc/cathedral.jpg) <br> Red-Blue Shift: [1, -1] <br> Green-Blue Shift: [7, -1] | ![](../data/rgb_align/sobel/cathedral.jpg) <br> Red-Blue Shift: [5, 2] <br> Green-Blue Shift: [12, 3] |

We observe that the MSD alignment strategy fails in Emir, Melons, and Lady. This is due to the luminencne in the RGB channels not aligning, and the strategy going off course because of it. We also try multiscale alignment even for smaller JPG's. This leads to compounding errors for smaller images for the MSD strategy. Cross correlation improves this, and no image is greatly color shifted like MSD. However, in Emir's photo for example, the channels are still visibily misaligned. This is most likely due to the differently thick edges lining up, messing up the alignment of the image subject. We improved results by suing an edge detector. Since all 3 channels describe the same subject, we can ssume that the object's edges will align. By using the Sobel Edge extractor, we can extract edges and then compute Cross Correlation on this edge feature. This leads to much better results as shown in the above table.

## Edge Detector
Below are the Sobel features of the Red, Green, and Blue channels for Emir
![Sobel Features of the Red Channel for Emir](../data/../data/rgb_align/sobel1.jpg)
![Sobel Features of the Green Channel for Emir](../data/../data/rgb_align/sobel2.jpg)
![Sobel Features of the Blue Channel for Emir](../data/../data/rgb_align/sobel2.jpg)

## Automatic Contrast
For automatic contrast, we normalize the histogram to both linear and sigmoid distributions. 
To achieve this, we first compute the percentile of a pixel in its channel relative to the rest of the image. Then we replace its value by the the value of our function at the point of that percentile.
If a pixel is at the 50 percentile, then if we use the linear case, then its value should be $0.5 \times 255 = 128$ (rounded to the nearest integer). The linear function uses a linear function to create the histogram function, and the sigmoid one uses a sigmod function.

Below we test our method on 3 images downloaded from the Prokudin-Gorskii collection.

| Original |  Uncorrected  | Linear Contrast | Sigmoid Contrast |
| ------------- | ------------- | ------------- | -------------|
| ![](../data/rgb_align/custom_0.jpg) | ![](../data/rgb_align/custom0_stack.jpg) | ![](../data/rgb_align/custom0_lin.jpg) | ![](../data/rgb_align/custom0_sigmoid.jpg)|
| ![](../data/rgb_align/custom_1.jpg) | ![](../data/rgb_align/custom1_stack.jpg) | ![](../data/rgb_align/custom1_lin.jpg) | ![](../data/rgb_align/custom1_sigmoid.jpg)|
| ![](../data/rgb_align/custom_2.jpg) | ![](../data/rgb_align/custom2_stack.jpg) | ![](../data/rgb_align/custom2_lin.jpg) | ![](../data/rgb_align/custom2_sigmoid.jpg)|


## Run Time
| Method     | Runtime (all 14 images)|
| ------------- | ------------- |
| MSD Minimization | 04:37 | 
| Normalized CC | 09:45 | 
| Sobel Edge detection| 06:47 | 

MSD comptues the fastest, followed by Sobel, and NCC computes the slowest.