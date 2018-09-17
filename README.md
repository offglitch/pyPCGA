# pyPCGA

Python library for Principal Component Geostatistical Approach

version 0.1

updates
- Exact preconditioner construction (inverse of cokriging/saddle-point matrix) using generalized eigendecomposition [Lee et al., WRR 2016, Saibaba et al, NLAA 2016]
- Fast predictive model validation using cR/Q2 criteria [Kitanidis, Math Geol 1991] ([Lee et al., 2018 in preparation]) 
- Fast posterior variance/std computation using exact preconditioner

version 0.2 will include
- automatic covariance model parameter calibration
- link with FMM (pyFMM3D) and HMatrix (pyHmatrix) to support unstructured grids 

# Example Notebooks

* [1D linear inversion example](https://github.com/jonghyunharrylee/pyPCGA/blob/master/examples/pumping_history_identification/linear_inverse_problem_pumping_history_identification.ipynb)

* [1D nonlinear inversion example](https://github.com/jonghyunharrylee/pyPCGA/blob/master/examples/pumping_history_identification/nonlinear_inverse_problem_pumping_history_identification.ipynb)

* [Hydraulic conductivity estimation example using USGS-FloPy (MODFLOW)](https://github.com/jonghyunharrylee/pyPCGA/blob/master/examples/modflow_flopy/inversion_modflow.ipynb) [Lee and Kitanidis, 2014]

* [Bathymetry estimation example using STWAVE](https://github.com/jonghyunharrylee/pyPCGA/blob/master/examples/stwave_duck/inversion_stwave.ipynb)

* TOUGH2/Crunch/E4D/adh examples coming soon! 

# Credits

pyPCGA is based on Lee et al. [2016] and currently used for Stanford-USACE ERDC project led by EF Darve and PK Kitanidis and NSF EPSCoR `Ike Wai project. 

Code contributors include:

* Jonghyun Harry Lee 
* Matthew Farthing

* Hojat Ghorbanidehno (TOUGH2 interface comming soon!)
* Amalia Kokkinaki (TOUGH2 interface comming soon!)
* Ty Hesser (STWAVE example)

FFT-based matvec code is adapted from Arvind Saibaba's work (https://github.com/arvindks/kle). 

# References

- J Lee, H Yoon, PK Kitanidis, CJ Werth, AJ Valocchi, "Scalable subsurface inverse modeling of huge data sets with an application to tracer concentration breakthrough data from magnetic resonance imaging", Water Resources Research 52 (7), 5213-5231

- AK Saibaba, J Lee, PK Kitanidis, Randomized algorithms for generalized Hermitian eigenvalue problems with application to computing Karhunen–Loève expansion, Numerical Linear Algebra with Applications 23 (2), 314-339

- J Lee, PK Kitanidis, "Large‐scale hydraulic tomography and joint inversion of head and tracer data using the Principal Component Geostatistical Approach (PCGA)", WRR 50 (7), 5410-5427

- PK Kitanidis, J Lee, Principal Component Geostatistical Approach for large‐dimensional inverse problems, WRR 50 (7), 5428-5443

# Applications

- J Lee, H Ghorbanidehno, M Farthing, T. Hesser, EF Darve, and PK Kitanidis, Riverine bathymetry imaging with indirect observations, Water Resources Research, 54(5): 3704-3727, 2018

- J Lee, A Kokkinaki, PK Kitanidis, Fast large-scale joint inversion for deep aquifer characterization using pressure and heat tracer measurements, Transport in Porous Media, 123(3): 533-543, 2018

- PK Kang, J Lee, X Fu, S Lee, PK Kitanidis, J Ruben, Improved Characterization of Heterogeneous Permeability in Saline Aquifers from Transient Pressure Data during Freshwater Injection, Water Resources Research, 53(5): 4444-458, 2017

- S. Fakhreddine, J Lee, PK Kitanidis, S Fendorf, M Rolle, Imaging Geochemical Heterogeneities Using Inverse Reactive Transport Modeling: an Example Relevant for Characterizing Arsenic Mobilization and Distribution, Advances in Water Resources, 88: 186-197, 2016
