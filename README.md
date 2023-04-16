# store-sales
kaggle competition: https://www.kaggle.com/competitions/store-sales-time-series-forecasting

Report: report.pdf

Following are the contents:
1) baseline_regression.ipynb, and baseline_regression.pdf - These contain the code for Q5 of homework 4.
2) weka_sample_output.txt, and train_1_BEAUTY.arff, train.py - sample output and data and the train script for the weka SMOreg regressor (this generates it's own features as can be seen from sample output)
3) prophet_model.ipnb, and prophet_model.pdf - this contains the basic model trained on facebook's prophet_model
4) rf-per-family-avg-sales.ipynb, and rf-per-family-avg-sales.pdf - This contains the code for the random forest model trained per family on average sales
5) rf-per-family-store-as-features.ipynb, rf-per-family-store-as-features.pdf - this contains the code for random forest model trained per family using store itself as a feature
6) best-model-final.ipynb, and best-model-final.pdf - this contains the code for the final model, and two penultimate models that we tried with and without pca. We could not improve the model performance on the bare dataset without extrafeatures.

Instructions to Run the Code:
For all the files, just run the ipynb notebook.

Please feel free to contact us in case of any questions:
POC - Shashank Rangarajan - sr87317@usc.edu
