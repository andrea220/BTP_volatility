# BTP volatility and HJM
The idea is to derive a volatility function from the BTP yield curve and setup an HJM Gaussian model. <br>
To define the volatility function I applied PCA to the initial data. Then, using the definition of Eigenvalues and Eigenvectors, I derived a compressed version of sample standard deviation and fitted a polynomial on those values. <br>
Using numeric integration on volatility fitted functions it is possible to obtain the risk neutral drift for a general HJM Gaussian model.

