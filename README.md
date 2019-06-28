# Machine Learning Project
Having the ability to diagnose breast cancer in its early stages has been the focus of many researches in the last decade. Although many strides have been achieved in this area, there is still a long way to go before prevention and early detection is achieved in most cases. Over forty thousand women are expected to die from breast cancer in 2019 based on predictive analytics. But as technology moves in the right direction, our team is confident that machine learning models will be able to contribute to this effort. 

The statistics state that “Uninsured women who were diagnosed with breast cancer were 60% more likely to die from the disease… Uninsured women were also nearly almost 3 times more likely to be diagnosed with a later stage of the disease, compared to women who had health insurance.”

We have created an app to be utilized as a suplemental diagnostic tool for users to detect the type of cancer (malignant or benign) a patient is likely to have based on results from a digitized image of a Fine Needle Aspiration Biopsy (FNA). The images from this test describe characteristics of the cell nuclei present in the image. The main idea around this tool is to construct a diagnosis system that could achieve diagnostic accuracy comparable to that of a surgical biospy.

This app will be shared with Health Centers, Research Institutes, and Cancer Centers that serve uninsured or underinsured demographics and do not have the resources to acquire this type of tool.

Data Summary:
We gathered data that includes test results of a Fine Needle Aspiration Biopsy (FNA) perfomed on over 500 subjects. The results included the final diagnosis - malignant or benign - from the tumors studied. 
The following features were analyzed: 
    - radius                
    - texture                 
    - perimeter               
    - area                    
    - smoothness              
    - compactness             
    - concavity               
    - concave_points          
    - symmetry                
    - fractal_dimension       

While wrangling the data, we extracted the features from the list above that were not good indicators of either diagnosis and therefore would not assist in the predictive process of our machine learning model. 

Below is our structure model that shows our overall process.

[image of model goes here]