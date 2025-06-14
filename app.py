import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Stroke Prediction Project Proposal",
    page_icon="🧠",
    layout="wide"
)

# Main title
st.title("Stroke Prediction Project Proposal")
st.markdown("---")

# Introduction and Background
st.header("Introduction and Background")
st.write("""
This project focuses on predicting the likelihood of stroke occurrence using machine learning techniques. 
""")

st.info("""
Our project is to use machine learning to predict strokes before they happen, by aiming to identify high risk individuals using medical and demographic data. We will be using the Stroke Prediction Dataset from Kaggle which contains features such as age, gender, BMI, and work type.  

Currently, Support Vector Machine (SVM) is the most widely used ML method for using AI to predict diagnoses, with many studies finding it achieves the best performance [1]. One study found it to have a 97.56% accuracy rate in detecting Alzheimer's [2]. Random Forest is another method that's widely used and has achieved good results, in one study having a 98.4% accuracy in detecting TD antibodies [1]. Hybrid systems, such as between SVM and artificial neural network, have also found good results [3], and Naive Bayes was able to achieve 82.35% test accuracy in evaluating heart disease data [3].  

Stroke is a leading cause of death and long-term disability worldwide, and timely intervention is critical to treatment. A data-driven model that can estimate an individual's probability of experiencing a stroke would allow earlier diagnosis and access to care, allow doctors to spend less time going through data and more time with patients, reduce human error, and allow disease likelihoods to be evaluated based on much larger pools of data [2], potentially saving lives. Given the growing availability of electronic health records and wearable medical devices that track health data in real time, there is a clear opportunity to apply machine learning for stroke risk prediction at scale. 

To preprocess the dataset, we'll start by replacing missing values with the feature's median. Next, we'll encode categorical data into quantitative data and normalize across features using StandardScalar. Features will be evaluated for correlation to see if dimensionality can be reduced. Finally, the dataset will be split into 70% training data and 30% testing data. 

The first algorithm used will be Naive Bayes, a simple and common method that will be useful as a baseline. As the data will be entirely numerical and includes continuous values such as age and BMI, we will use GaussianNB for classification [4]. 

The second algorithm we'll use is SVM since it works well in cases with a high number of dimensions and takes advantage of support vectors to be less affected by outliers [5]. We believe this algorithm will be useful for dealing with any of our data that strays away from a linear decision boundary since SVM is able to model complex decision boundaries [5]. Since the data may be better-suited with a non-linear kernel, we will use SVC (Support Vector Classifier) for classification. 

Our final algorithm will be Random Forest, as it works well to avoid overfitting, as well as working well with imbalanced data [6]. To classify our prediction of a stroke, we will use RandomForestClassifier. 

The first metric we plan to use is the f1_score, which will use a combination of precision and recall to evaluate how well our model uses data to make predictions.  Our second metric is the precision_recall_curv, ideal for our unbalanced dataset, which will give an evaluation of the precision and recall ratios based on thresholds. Finally, we will use class_likelihood_ratios, which will allow us to evaluate our positive and negative likelihood ratios based on the actual probability of having a stroke. Based on the studies we reviewed, we expect that Naive Bayes will have the lowest accuracy rating. We hope to get at least 80% across our metrics. Our goal is that SVM and Random Forest will be much more accurate, with at least 90% across our metrics. 
""")

st.subheader("References")
st.info("""
[1] N. Ghaffar Nia, E. Kaplanoglu, and A. Nasab, "Evaluation of artificial intelligence techniques in disease diagnosis and prediction," Discov Artif Intell 3, 5 (2023). [Online] Available: https://doi.org/10.1007/s44163-023-00049-5 [Accessed June 12, 2025] 

[2] Y. Kumar, A. Koul, R. Singla et al. "Artificial intelligence in disease diagnosis: a systematic literature review, synthesizing framework and future research agenda,"  J Ambient Intell Human Comput 14, 8459–8486 (2023).  [Online] Available: https://doi.org/10.1007/s12652-021-03612-z [Accessed June 12, 2025] 

[3] V. Jackins, S. Vimal, M. Kaliappan et al. "AI-based smart prediction of clinical disease using random forest classifier and Naive Bayes.," J Supercomput 77, 5198–5219 (2021).  [Online] Available: https://doi.org/10.1007/s11227-020-03481-x [Accessed June 12, 2025] 

[4] "Naive Bayes," Scikit Learn. [Online] Available: https://scikit-learn.org/stable/modules/naive_bayes.html [Accessed June 13, 2025] 

[5] "Support Vector Machines," Scikit Learn. [Online] Available: https://scikit-learn.org/stable/modules/svm.html [Accessed June 13, 2025] 

[6] "Random Forest and Other Randomized Tree Ensembles," Scikit Learn. [Online] Available: https://scikit-learn.org/stable/modules/ensemble.html#forest [Accessed June 13, 2025] 
""")

st.subheader("Team Responsibilities")
st.markdown("""
| Team Member | Sections | Responsibilities |
|------------|----------|-----------------|
| Tyler | 1, 2, 7.5, 9 | • Intro/background, Problem Definition, Responsibility table, PowerPoint |
| Taylor | 5 | • Research/references |
| Nima | 3, 4 | • Methods, Results and Discussion |
| Benjamin | 6 | • Making website |
| Yoomin | 6, 7 | • Making website, Gantt chart |
| Everyone | 8 | • Recording Video |
""")

st.subheader("Gantt Chart")
st.image("gantt_converted.png")

# Add download button for Excel file
with open("Summer 2025 ML GanttChart.xlsx", "rb") as file:
    st.download_button(
        label="Download Gantt Chart Excel File",
        data=file,
        file_name="Summer 2025 ML GanttChart.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.subheader("Github Repository")
st.markdown("[https://github.gatech.edu/bproell3/StrokePrediction](https://github.gatech.edu/bproell3/StrokePrediction)")


st.markdown("---")
st.markdown("Ben Proell, Nima Mollaei, Yoomin Choi, Taylor West, Tyler Chevalier")
