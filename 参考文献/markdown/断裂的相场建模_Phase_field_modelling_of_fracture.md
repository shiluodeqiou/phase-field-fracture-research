# Phase-field modelling of fracture

Jian-Ying Wu<sup>1</sup>, Vinh Phu Nguyen<sup>2</sup>, Chi Thanh Nguyen<sup>3,4</sup>, Danas Sutula<sup>5</sup>, Sina Sinaie<sup>6</sup>, and Stephane Bordas<sup>5</sup> 

<sup>1</sup>State Key Laboratory of Subtropical Building Science, South China University of Technology, Guangzhou 510641, China 

<sup>2</sup>Department of Civil Engineering, Monash University, Clayton, Victoria 3800, Australia <sup>3</sup>Division of Computational Mathematics and Engineering, Institute for Computational Science, Ton Duc Thang University, Ho Chi Minh City, Vietnam 

<sup>4</sup>Faculty of Civil Engineering, Ton Duc Thang University, Ho Chi Minh City, Vietnam <sup>5</sup>Institute of Computational Engineering, University of Luxembourg, Faculty of Sciences Communication and Technology, Luxembourg 

<sup>6</sup>Department of Infrastructure Engineering, The University of Melbourne, VIC 3010, Australia 

March 1, 2019 

## Contents

1 Introduction 7   
2 Overview of phase-field fracture/damage models 11   
2.1 PF models for brittle fracture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
2.2 PF models for ductile fracture .. 16   
2.3 PF models for cohesive fracture .. 16   
2.4 PF models for dynamic fracture .. 17   
2.5 PF models for finite deformation fracture .. 18   
2.6 PF models for three-dimensional fracture .. 18   
2.7 PF models for plate and shell fractures .. 19   
2.8 PF models for multi-field fracture .. 19   
2.9 Structure anisotropy .. 19   
2.10 Fracture of layered materials .. 21   
2.11 Fatigue .. 21   
2.12 Validation of PF models .. 21   
3 Theoretical aspects 23   
3.1 Griffith's theory and the variational approach to brittle fracture .. 23   
3.2 Governing equations of PF models in strong form .. 25   
3.3 Phase-field approximation of a sharp crack topology .. 28   
3.3.1 Classical geometric crack function .. 28   
3.3.2 Generic geometric crack function .. 30   
3.4 Stored energy functional .. 32   
3.4.1 Isotropic model with no split .. 33 

3.4.2 Anisotropic model of Lancioni and Royer-Carfagni [2009] 34
3.4.3 Anisotropic model of Amor et al. [2009] 34
3.4.4 Anisotropic model of Miehe et al. [2010b] 34
3.4.5 Anisotropic model of Wu and Nguyen [2018] 35
3.5 Energetic degradation function 35
3.6 Hybrid formulations 37
3.7 Governing equations of PF models in weak form 38
3.8 Relation with nonlocal damage models 40
3.8.1 Relation with gradient-enhanced damage (GED) models 40
3.8.2 Relation with gradient damage (GD) models 42
4 1-D analytical solution 43
4.1 General results 43
4.1.1 Homogeneous solution 43
4.1.2 Localised solution 44
4.2 Particular examples 45
4.2.1 Quadratic geometric crack function 45
4.2.2 Mixed linear and quadratic geometric crack function 48
4.2.3 Optimal functions for cohesive fracture 50
4.3 Numerical verification 53
4.3.1 Brittle fracture 53
4.3.2 Quasi-brittle failure 53
4.4 A brief summary 55
5 Finite element discretisation and solvers 56
5.1 Finite element discretisation 57
5.2 Irreversibility and boundedness of the crack phase-field 59
5.3 Quasi-static fracture 59
5.3.1 Monolithic solvers 60
5.3.2 Alternating minimisation (Staggered) solvers 61
5.4 Dynamic fracture 63
5.4.1 Implicit dynamics 64
5.4.2 Explicit dynamics 65
6 Computational aspects 65
6.1 Computer codes 66
6.2 Element technologies 66
6.3 Solvers 67
6.4 Adaptive mesh refinement and coarsening 69
6.4.1 Borden's scheme 70
6.4.2 Heister's mesh adaptation 70
6.5 Modelling pre-existing cracks 71
6.6 Determination of crack tip position 74
6.7 Calculation of strain and surface energies 75
7 Numerical examples 75
7.1 Quasi-static brittle fracture 75
7.1.1 Shear test 75
7.1.2 Pre-cracked sample with two holes 78
7.1.3 A square plate with two edge cracks 79
7.1.4 A square plate with 10 cracks 80
7.1.5 Crack growth in rock-like materials 82
7.1.6 Asymmetrically notched beam under three-point bending 86 

7.2 Quasi-static cohesive fracture . 88
7.2.1 Wedge splitting test . 88
7.2.2 L-shaped panel . 90
7.2.3 Mixed-mode failure of notched beams . 91
7.3 Dynamic brittle fracture . 93
7.3.1 Dynamic crack branching . 93
7.3.2 Edge-cracked plate under impulsive loading . 96

8 Conclusions 100
8.1 Summary . 101
8.2 Issues . 102
8.3 Future work and perspectives . 103

A A brief recount on variational calculus 104

B Positive/negative projection and its application to phase-field fracture models 105
B.1 General definition of the positive/negative projection . 105
B.2 Miehe's strain energy decomposition . 106
B.3 Wu and Cervera's strain energy decomposition . 106

C Thermodynamics 106

D Comparison with other gradient-damage models 108

E Arc-length (path following) methods 109

Nomenclature $\mathcal{B}$ the localisation band $\mathcal{B} \subseteq \Omega$ over which the crack is smeared $\mathcal{G}$ the classical energy release rate $\mathcal{H}$ the local history field variable $\mathcal{S}$ the pre-defined cracks $\mathcal{Y}$ the reference value to the energetic crack driving force $\partial \mathcal{B}$ the external boundary of $\mathcal{B}$ $\alpha(\phi)$ the crack geometric function $\bar{\sigma}$ the effective stress tensor $\bar{\sigma}_1$ the largest principal value of the effective stress tensor $\bar{\sigma}_{eq}$ the so-called equivalent effective stress tensor $\epsilon(x)$ the strain field $\epsilon^c$ the cracking strain $\epsilon^e$ the elastic strain $\epsilon^p$ the plastic strain $\sigma$ the Cauchy stress tensor $n _ { d i m }$ the number of spatial dimension $p$ and $a _ { n } , \ ( n = 1 , 2 , 3 )$ the exponent and coefficients for the degradation function $T$ the time interval of calculation $w ( \phi )$ the apparent displacement jump across the localisation band $w _ { c }$ the ultimate apparent jump or the ultimate crack opening $\mathcal { A }$ the Hamilton’s action functional $\mathcal { D }$ the energy dissipation $\mathcal { E } ^ { \mathcal { O } }$ the total energy functional $\mathcal { F }$ the function to define the rate of the crack phase-field $\phi ( x )$ $\mathcal { H }$ the extra kinetic energy $\mathcal { P }$ the external potential energy functional $\mathcal { U } _ { u } , \mathcal { U } _ { \phi }$ test spaces for the displacement and phase field parameters $\mathcal { Y } _ { u } , \mathcal { Y } _ { \phi }$ trial spaces for the virtual displacement and virtual phase field parameters $\mathcal { W } , \mathcal { S }$ the external power and the internal power of a given domain 

<table><tr><td>Δ</td><td>the Laplacian operator i.e., Δφ = ∇ · ∇φ</td></tr><tr><td>εD</td><td>the deviatoric strain</td></tr><tr><td>εn</td><td>the principal strains</td></tr><tr><td>εV</td><td>the volumetric strain</td></tr><tr><td>εeq</td><td>the local equivalent strain, a scalar measure of the strain tensor</td></tr><tr><td>η1, η2</td><td>parameters for the softening curve for normal concrete</td></tr><tr><td>Γ</td><td>a crack/jump set, or the sharp crack surface (page 19)</td></tr><tr><td>γ(φ, ∇φ)</td><td>the crack surface density function</td></tr><tr><td>Γ(t)</td><td>the crack area or length</td></tr><tr><td>Γ0</td><td>the initial state of a crack/jump set or the predefined crack</td></tr><tr><td>Γl</td><td>the regularised crack surface</td></tr><tr><td>λ0, μ0</td><td>the Lamé constants</td></tr><tr><td>∇</td><td>the gradient operator i.e., ∇φ = (φ,x, φ,y, φ,z)T</td></tr><tr><td>ν0</td><td>Poisson's ratio</td></tr><tr><td>ω(φ)</td><td>the monotonically increasing function, ω(φ) = 1/g(φ) - 1</td></tr><tr><td>∂Ω</td><td>the external boundary</td></tr><tr><td>∂Ωt, ∂Ωu</td><td>the Neumann/Dirichlet boundary</td></tr><tr><td>φ</td><td>damage-like crack phase-field</td></tr><tr><td>ψ0(ε)</td><td>the initial energy density function</td></tr><tr><td>ψ±0(ε)</td><td>positive/negative parts of the initial energy density function</td></tr><tr><td>ρ</td><td>the mass density</td></tr><tr><td>σc</td><td>the maximum stress</td></tr><tr><td>ξ</td><td>the non-negative parameter in the equation of the crack geometric function</td></tr><tr><td>J2</td><td>the second invariant of the deviatoric effective stress tensor</td></tr><tr><td>b*, t*</td><td>the macroscopic body force and boundary tractions, respectively</td></tr><tr><td>n</td><td>the outward unit normal</td></tr><tr><td>u(x)</td><td>the displacement field</td></tr><tr><td>ü(x)</td><td>the acceleration field</td></tr><tr><td>Δt</td><td>a typical time increment</td></tr><tr><td>ä, ä</td><td>the nodal velocity and acceleration</td></tr><tr><td>[u]</td><td>the displacement jump</td></tr><tr><td><eq>\mathbf{n}_{\mathcal{B}}</eq></td><td>the outward unit normal vector of the boundary <eq>\partial \mathcal{B}</eq> of the localisation band <eq>\mathcal{B}</eq></td></tr><tr><td><eq>\mathbf{p}_{n}</eq></td><td>the eigenvectors</td></tr><tr><td><eq>\mathrm{C}_{0}</eq></td><td>the fourth-order compliance tensor</td></tr><tr><td><eq>\mathbb{E}_{0}</eq></td><td>the linear elastic tensor</td></tr><tr><td><eq>\mathbb{I}</eq></td><td>the fourth-order identity tensor</td></tr><tr><td><eq>\mathbf{a}, \bar{\mathbf{a}}</eq></td><td>the vectors of the nodal displacement and the crack phase field variables</td></tr><tr><td><eq>\mathbf{B}, \bar{\mathbf{B}}</eq></td><td>the standard strain-displacement matrix and gradient operator</td></tr><tr><td><eq>\mathbf{D}</eq></td><td>the material tangent matrix</td></tr><tr><td><eq>\mathbf{f}^{\text{int/ext}}</eq></td><td>the internal/external force vector</td></tr><tr><td><eq>\mathbf{K}^{\phi u}, \mathbf{K}^{\phi \phi}</eq></td><td>the tangent matrices</td></tr><tr><td><eq>\mathbf{K}^{uu}, \mathbf{K}^{u\phi}</eq></td><td>the tangent matrices</td></tr><tr><td><eq>\mathbf{M}</eq></td><td>the consistent mass matrix</td></tr><tr><td><eq>\mathbf{N}, \bar{\mathbf{N}}</eq></td><td>the interpolation matrices</td></tr><tr><td><eq>\mathbf{r}^{u}, \mathbf{r}^{\phi}</eq></td><td>the residual forms of the nodal displacement and the crack phase field variable</td></tr><tr><td><eq>\tilde{M}</eq></td><td>the kinetic coefficient or mobility parameter</td></tr><tr><td><eq>c_{0}</eq></td><td>the scaling parameter to recover the sharp crack surface</td></tr><tr><td><eq>c_{R}, c_{s}</eq></td><td>the Rayleigh wave speed and the shear wave speed</td></tr><tr><td><eq>D</eq></td><td>the half bandwidth of the localisation band</td></tr><tr><td><eq>D_{0}</eq></td><td>the initial half bandwidth of the localisation band</td></tr><tr><td><eq>D_{u}</eq></td><td>the ultimate half bandwidth of the localisation band</td></tr><tr><td><eq>E_{0}</eq></td><td>Young’s modulus</td></tr><tr><td><eq>f_{c}</eq></td><td>the uniaxial compressive strength</td></tr><tr><td><eq>f_{t}</eq></td><td>the uniaxial tensile strength or the failure strength</td></tr><tr><td><eq>G([u], \kappa)</eq></td><td>the fracture energy function</td></tr><tr><td><eq>g(\phi)</eq></td><td>the stress/energetic degradation function</td></tr><tr><td><eq>G_{c}</eq></td><td>the critical energy release rate or the fracture toughness of the material</td></tr><tr><td><eq>G_{Ic}</eq> and <eq>G_{IIc}</eq></td><td>the critical energy release rates for mode I and mode II</td></tr><tr><td><eq>h</eq></td><td>the fixed mesh size of the FEM discretisation mesh</td></tr><tr><td><eq>K_{0}</eq></td><td>the <eq>n</eq>-dimensional bulk modulus</td></tr><tr><td><eq>k_{0}</eq></td><td>the initial slope of the softening curve</td></tr><tr><td><eq>l_{0}</eq></td><td>length scale</td></tr></table>

## Abbreviations

CDM Continuum Damage Mechanics. 7 

CZM Cohesive Zone Model. 8 

FEM Finite Element Method. 7 

GD Gradient Damage Model. 41 

GED Gradient-Enhanced Damage Model. 39 

LEFM Linear Elastic Fracture Mechanics. 7 

PD Peridynamics. 8 

PF-CZM Phase-field regularised cohesive zone model. 17 

PFM Phase-field Fracture/Damage Model. 8 

## Abstract

Fracture is one of the most commonly encountered failure modes of engineering materials and structures. Prevention of cracking-induced failure is, therefore, a major constraint in structural designs. Computational modelling of fracture constitutes an indispensable tool not only to predict the failure of cracking structures but also to shed insights into understanding the fracture processes of many materials such as concrete, rock, ceramic, metals and biological soft tissues. This manuscript provides an extensive overview of the literature on the so-called phase-field fracture/damage models (PFMs), particularly, for quasi-static and dynamic fracture of brittle and quasi-brittle materials, from the points of view of a computational mechanician. PFMs are the regularised versions of the variational approach to fracture which generalises Griffith’s theory for brittle fracture. They can handle topologically complex fractures such as initiation, intersecting and branching cracks in both two and three dimensions with a quite straightforward implementation. One of our aims is to justify the gaining popularity of PFMs. To this end, both theoretical and computational aspects are discussed and extensive benchmark problems (for quasi-static and dynamic brittle/cohesive fracture) that are successfully and unsuccessfully solved with PFMs are presented. Unresolved issues for further investigations are also documented. 

## 1 Introduction

Fracture is one of the most commonly encountered failure modes of engineering materials and structures. Prevention of cracking-induced failure is, therefore, a major constraint in engineering designs. As with many other physical phenomena computational modelling of fracture constitutes an indispensable tool not only to predict the failure of cracked structures, for which full-scale experiments are either too costly or even impracticable, but also to shed insights into understanding the fracture processes of many materials such as concrete, rock, ceramic, metals and biological soft tissues. The subject has been extensively studied since the milestone work of Griffith [1920], Irwin [1957] who es tablished the theory of Linear Elastic Fracture Mechanics (LEFM). Still, predictive modelling of crack initiation and propagation in materials and structures remains one of the most significant challenges in solid mechanics. This manuscript is confined to fracture theories based on continuum mechanics [Malvern, 1969]. Molecular dynamics are therefore left out in the first place and readers can refer to e.g., Holian and Ravelo [1995], Rountree et al. [2002] and references therein. Discrete element methods are also skipped [Cundall and Strack, 1979, Scholtès and Donzé, 2012, Sinaie et al., 2018a] as well as and lattice models [Hrennikoff, 1941, Schlangen and Van Mier, 1992, Pan et al., 2018] . Multiscale fracture analysis is not discussed neither, we refer to Belytschko et al. [2008], Geers et al. [2010], Nguyen et al. [2011b], Talebi et al. [2013, 2014], Beex et al. [2014], Karamnejad and Sluys [2014] and references therein. 

The term ‘fracture mechanics’ refers to a vital sub-branch of solid mechanics in which the a priori presence of a crack is assumed<sup>1</sup>, and it provides tools to find quantitative relations between the crack length, the inherent resistance to the crack growth of materials, and the criterion at which the crack propagates. Griffith’s theory [Griffith, 1920] – a global energy approach – regards fracture as a competition between the surface energy for crack propagation and the elastic energy stored in the bulk material. It states that ‘crack growth will occur, when there is enough energy available to generate new crack surfaces’. While the energy approach provides a great deal of insight to the fracture process, an alternative method that directly examines the stress state around the crack tip has proven more useful in engineering practice – the well-known stress intensity factor (SIF) approach [Irwin, 1957]. 

In parallel with fracture mechanics, there exists the so-called Continuum Damage Mechanics (CDM) – a discipline pioneered by Kachanov [1958]. In contrast to fracture mechanics which focuses on macroscopic cracks of finite length, CDM mainly deals with microdefects (i.e., microcracks and microcavities) and effects of their evolution [Krajcinovic, 1989] phenomenologically by some damage variables. Utilisation of CDM in the context of the finite element method to model strain softening suffers from excessive mesh (size and bias) dependence [Jirásek, 2007] due to the lack of an internal length scale in the formulation. This has led to the development of various regularisation theories such as the viscous regularisation [Simo and Ju, 1987], Cosserat theory [Borst and Sluys, 1991], the non-local continuum theory [Pijaudier-Cabot and Bažant, 1987, Bažant et al., 1984, Bažant and Jirásek, 2002] and its variants [Giry et al., 2011, Pereira et al., 2016], the gradient-enhanced damage model [Peerlings et al., 1996a] and its variants [Poh and Sun, 2017, Vandoren and Simone, 2018], and the gradient damage model [Frémond and Nedjar, 1996, Lorentz and Andrieux, 1999, Pham et al., 2011]. 

This article is concerned with computational failure (fracture/damage) mechanics – a sub-branch of computational mechanics that refers to the creation of numerical methods to approximate the crack evolution predicted by various analytical fracture/damage models such as LEFM and CDM. To keep the article at a reasonable length, we will focus on the Finite Element Method (FEM) [Hughes, 1987, Zienkiewicz and Taylor, 2006] which is arguably the most widely used numerical method in practice. Meshless/meshfree methods are therefore intentionally not touched upon, and we refer to e.g., Belytschko et al. [1996], Nguyen et al. [2008] and references therein. 

Fracture of solids can be numerically modelled using either a discontinuous approach (also referred to as a discrete approach) or a continuous one. In the former, the displacement field is allowed to be discontinuous across the fracture surfaces whereas in the latter the displacements are continuous everywhere but the stresses are gradually reduced to model the degradation process. The most well-known theories behind the discontinuous approach are the LEFM [Griffith, 1920, Irwin, 1957] and the Cohesive Zone Model (CZM) which was pioneered in Dugdale [1960], Barenblatt [1962]. CDM is probably the most widely used theory catergorised in the continuous approach to fracture even though smeared crack models, pioneered by Rashid [1968], have also been widely used to model failure of concrete, see e.g., Rots [1991], Wu et al. [2015], Oliver [1996]. The smeared crack models can be considered as a kinematically regularised approach, as the displacement jump across the sharp crack is smeared over a localisation band of small but finite width. 

From the fundamental point of view, LEFM and CZM are not self-contained in the sense that they require additional criteria to address the question when/where a crack initiates, grows, how much it propagates and in which direction. Moreover, for dynamic fracture an extra criterion is required to detect crack branching see e.g., Belytschko et al. [2003]. Some well established fracture criteria are the maximum hoop stress criterion [Erdogan and Sih, 1963], the minimum strain energy density criterion [Sih, 1973], the Rankine criterion, etc. A comparison of different crack propagation criteria can be found in e.g., Bouchard et al. [2003], Dumstorff and Meschke [2007]. Most importantly, LEFM cannot predict crack nucleation (or initiation). From numerics perspectives, introducing displacement discontinuities poses great challenges in mesh-based numerical methods such as the standard finite element method with a continuous displacement field. Discontinuities can be resolved either at the element boundaries, using duplicated nodes and remeshing techniques [Ngo and Scordelis, 1967, Bouchard et al., 2003] for LEFM and the well-known zero-thickness interface element (or cohesive surfaces) technique [Hillerborg et al. 1976, Xu and Needleman, 1994, Nguyen and Nguyen-Xuan, 2012, Nguyen, 2014b] for CZM, or at the intra-element level using the embedded strong discontinuity approach [Ortiz et al., 1987, Belytschko et al., 1988, Dvorkin et al., 1990, Simo et al., 1993, Armero and Linder, 2009, Wu et al., 2015] and the eXtended Finite Element Method (XFEM) [Moës et al., 1999, Wells and Sluys, 2001, Wu and Li, 2015]. The utilisa tion of interface elements remains attractive essentially due to the simplicity and effectiveness in some applications. The main advantage is that the complexity of crack initiation and growth including branching and coalescence can be modeled as an outcome of the model, without the need of any additional fracture criterion. In the so-called enriched finite element methods with elemental and nodal enrichments [Wu, 2011], the kinematics of finite elements is enhanced or enriched such that the displacement discontinuities can be incorporated into the approximation space. To this end, the discontinuity surface has to be explicitly tracked, which is, sometimes, an intractable task for those problems with arbitrary and complex crack paths. Despite recent advances numerical modelling of complex fracture problems that involve many intersecting cracks is still a challenging issue especially in three dimensions [Bordas et al., 2008, Sukumar et al., 2015, Sutula et al., 2018a]. 

Difficulties associated with the discontinuous (discrete) crack modelling motivate other computational techniques in which crack paths are automatically determined as part of the solution. Two popular models falling within this category are the phase-field fracture/damage model [Francfort and Marigo 1998, Aranson et al., 2000], and the Peridynamics (PD) of Silling [2000]. As phase-field (PF) theories for modelling fracture and damage are related to both fracture mechanics and damage mechanics, they are herein referred to as Phase-field Fracture/Damage Model (PFM). PFMs are closely related to the variational approach to brittlefracture [Francfort and Marigo, 1998] which aims to seek for, at the same time, the displacement field and the set of cracks by minimising the total potential energy of cracking solids, generalising Griffith’s theory. Numerical implementation of the variational approach to fracture was set forth in Bourdin et al. [2000] where the sharp crack topology is regularised by a diffuse damage band thanks to the introduction of a scalar phase-field that discriminate the intact and broken material; 

see also Bourdin et al. [2008b]. The formulation introduced a small positive length scale parameter $l _ { 0 }$ characterising the width of the localisation band and when $l _ { 0 }  0 .$ , the solution converges to the one of the original problem according to the Γ-convergence theorem<sup>2</sup> [Braides, 1998]. One can regard PFMs as solving fracture mechanics problems using partial differential equations (PDEs): basically one solves two PDEs; one for the vectorial displacement field and the other for the scalar phase-field. In peridynamics (PD), the classical partial differential governing equations are replaced by integral ones such that derivatives are simply not needed. Accordingly, there is no difficulty in dealing with displacement discontinuities. Similar to PFMs, PD is also a non-local theory – a novel non-local continuum mechanics without spatial derivatives. Both PF and PD models can handle topologically complex fractures such as intersecting and branching cracks in both two and three dimensions. More recently, Roy et al. [2017a,b] implemented a PFM for brittle fracture in the framework of PD. In such a combined approach the particles in solids can be physically broken into parts which a PFM cannot by itself accomplish. Furthermore, the smoothness restriction on the displacement and phase-field variables is loosened for the governing equations in integral form. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/668379b8eb7f5a1064200bace584c2f46404e523c4ecd5ff625cc3d15179b4ab.jpg)



Figure 1: Continuum mechanics is equipped with fracture/damage models (LEFM or CDM/PFM) and numerical tools such as FEM, XFEM, and remeshing FEM for the modeling of discontinuous deformations. Note that even though PFMs are in the same category with CDM (as both do not actually model cracks as strong discontinuities, but rather, model them using damage variables in the range [0, 1]), they are closely related to CZM and LEFM.


This manuscript focuses on PFMs for brittle, quasi-brittle and ductile fracture in both quasi-static and dynamic regimes, implemented within the framework of the finite element method. Our aims in writing this article are (i) to provide an extensive overview of the literature on this trending topic, particularly from the points of view of a computational mechanician, (ii) to present practically useful numerical implementation aspects, (iii) to justify the gaining popularity of PFMs, (iv) to provide an extensive set of benchmark problems that are successfully and unsuccessfully solved with the PFMs and (v) to point out unresolved issues for further investigations. Also presented are some new contributions: (i) a unified framework of phase-field models for both brittle fracture and quasi-brittle failure; (ii) a method motivated by XFEM to represent any number of initial cracks independently of the discretisation meshes, (iii) a comparison of some PF simulations with XFEM. We note that earlier reviews on PFMs can be found in 

Ambati et al. [2015a] from the computational mechanics community, in Bourdin et al. [2008b] from the applied mathematics community, in Spatschek et al. [2011] from the physics community and particularl the lecture of Del Piero [2013]. We also refer to Rabczuk [2013] for an extensive overview of popular computational methods for modelling brittle fracture and Rabczuk et al. [2010] for a review of numerical techniques for 3-D crack modelling. This document contains 85 figures of which nearly 99% are our own figures, 8 tables and 385 references (possibly with multiple citations) upto early 2019. We are sure that this list of references is not exhaustive and absence of relevant items are due only to our focused idiosyncrasy and negligence. The discussion is mostly based on a set of eleven numerical simulations covering brittle, cohesive fracture under both static and dynamic loading conditions conducted by the authors themselves. 

The remainder of this manuscript is organised as follows. In Section 2 we give an extensive overview of PFMs, focusing on those for brittle, ductile and cohesive fracture in two-dimensional infinitesimal deformations under quasi-static and dynamic loadings. Extensions to three dimensions, finite deformations, structural elements e.g., plates and shells, multi-physics problems, anisotropic surface energies, fracture of layered materials and fatigue are briefly commented. Verification and validation of PFMs are also presented. Section 3 addresses the theoretical aspects of PFMs. The general formulation and governing equations are first presented in a unified manner. Various ingredients of PFMs, including the diffuse approximation of the sharp crack topology, the stored energy functional with or without tension/compression split, the energetic/stress degradation functions commonly adopted in the literature, are systematically investigated. Several strategies dealing with the crack evolution law and the irreversibility condition are then presented. Relations between PFMs and gradient damage models and gradient-enhanced ones are also discussed. Section 4 is devoted to the application of various PFMs to a softening bar of which the analytical solution is presented in details, shedding light on optimal choices of the involved characteristic functions. Finite element discretisation and various solvers are discussed in Section 5, with the corresponding computational aspects–code platforms, solvers for the coupled PDEs, element technologies, adaptivity etc.–explored in Section 6. Section 7 presents extensive numerical examples covering both brittle/cohesive fracture under quasi-static and dynamic loadings. Section 8 ends this paper with some conclusions and discussion. 

Remark 1. A summary of different fracture/damage mechanics and numerical tools is given in Fig. 1. We share the viewpoint of Sukumar et al. [2015] that numerical methods such as remeshing FEM or XFEM are enabling technologies. They provide approximate solutions to complex fracture problems of which the physics is modelled by the corresponding fracture theories. 

Remark 2. We also note the thick level set (TLS) model – a new non-local damage model [Moës et al., 2011]; see Cazes and Moës [2015] for a comparison with the PFMs. In the TLS model, the level set with a specific propagation law is used to separate the sound zone from the damaged one. The damage variable is an explicit function<sup>3</sup> of the level set. Being nonlocal, the damage driving force averages information over the domain ahead of the damage front. Both brittle and cohesive fracture can be considered by tuning the explicit damage evolution law, though sometimes it is necessary to introduce XFEM to properly account for the transition to traction-free cracks in fully damaged zones [Bernard et al., 2012]. Qualitatively, similar results are exhibited, although the TLS model is observed to be less sensitive to boundary conditions, and more mesh sensitive; all with a more involved implementation and more parameters. 

Remark 3. The major drawback of continuous approaches for fracture is that a true discontinuity cannot be properly represented. This led to the development of continuous-discontinuous approaches, where a continuous description of cracking (by nonlocal damage models in integral or gradient form, for instance) is used until the final stage of failure which is modelled by a discontinuous approach (by XFEM, for example), see e.g., Simone et al. [2003], Mediavilla et al. [2006], Comi et al. [2007], Moonen et al. [2008], Cuvilliez et al. [2012], Giovanardi et al. [2017], Geelen et al. [2018] within the context of single-scale analyses and Nguyen et al. [2011a, 2012], Karamnejad et al. [2013] within the framework of multi-scale analyses. However, there is no consensus in defining the transition procedure between continuous and discontinuous approaches, especially when cracking induced anisotropy is important. Furthermore, all these continuous-discontinuous techniques have been applied only to problems where there exists a dominant propagating crack. 

Remark 4. Peridynamics and phase-field fracture models are the two fracture theories that probably receive most attention at the time of this writing. The governing equations of PD are integro-differential equations which result in a natural meshless discretisation [Silling and Askari, 2005, Bessa et al., 2014, Ganzenmuller et al., 2015]. Therefore, modelling extreme loading (impact and explosive loadings) of large structures is feasible in PD; see e.g., Demmie and Silling [2007], Silling and Askari [2005]. Moreover, as PD may be thought of as a continuum version of molecular dynamics (MD), coupling PD with MD seamlessly leads to efficient multiscale models [Seleson et al., 2009]. However, both PD and PFMs are very computationally expensive, limiting their usage within the academic community, at least at the time of this writing. It seems that PD is more costly than PFMs due to its meshless implementation. 

Remark 5. Due to our background in engineering we may have skipped celebrated works done by mathematicians even though they are strictly necessary for issues such as convergence, uniqueness and proof. We refer to e.g., Dal Maso and Toader [2002], Artina et al. [2015], Del Piero [2013] and references therein. In the parlance of mathematicians, the original problem raised by Francfort and Marigo [1998] is coined a free discontinuity problem [Braides, 1998] in which the solution can have discontinuities and, in addition, the jump sets of the solution are a priori unknown. The PFM of Bourdin et al. [2000] is motivated by the Ambrosio-Tortorelli regularisation [Ambrosio and Tortorelli, 1990] of the Mumford-Shahfunctional [Mumford and Shah, 1989] in image segmentation. 

Notation. Compact tensor notation is used in the theoretical part of this paper. As general rules, scalars are denoted by italic light-face Greek or Latin letters (e.g. a or λ); vectors, second- and fourth-order tensors are signified by italic boldface minuscule, majuscule and blackboard-bold majuscule characters like a, A and A, respectively. The inner products with single and double contractions are denoted by ‘ ’ and ‘:’, respectively. Symbols with a bar on top (✷¯ ) denote effective quantities whereas ones with an asterisk (✷∗) represent prescribed quantities. In the numeric part of finite elements, Voigt notation is adopted where vectors and second-order tensors are denoted by boldface minuscule and majuscule letters like a and A, respectively. 

## 2 Overview of phase-field fracture/damage models

In order to introduce the PF model, we refer to Fig. 2 where a solid $\mathcal { Q } \subset \mathbb { R } ^ { n _ { \mathrm { d i m } } } ( n _ { \mathrm { d i m } } = 1 , 2 , 3$ is the number of spatial dimensions) with a crack set ${ \cal T } \subset \mathbb { R } ^ { n _ { \mathrm { d i m } } - 1 }$ is considered. The solid is kinematically characterised by the displacement field ${ \pmb u } ( { \pmb x } )$ and the (infinitesimal) strain field $\pmb { \epsilon } ( \pmb { x } ) : = \nabla ^ { s } \pmb { u } ( \pmb { x } )$ , for the symmetric gradient operator $\nabla ^ { s } ( \cdot )$ with respect to the spatial coordinates x. The external boundary $\partial \Omega \subset \mathbb { R } ^ { n _ { \mathrm { d i m } } - 1 }$ , with the outward unit normal denoted by vector n, is split into two disjoint parts $\partial \varOmega _ { u }$ and $\partial \Omega _ { t } , \mathrm { i . e . , } \partial \Omega _ { u } \cap \partial \Omega _ { t } = \emptyset$ and $\overline { { { \partial \varOmega _ { u } \cup \partial \varOmega _ { t } } } } = \partial \varOmega$ , on which given displacements ${ \pmb u } ^ { * } ( { \pmb x } )$ for $\pmb { x } \in \partial \Omega _ { u }$ and tractions ${ \pmb t } ^ { * } ( { \pmb x } )$ for $\pmb { x } \in \partial \varOmega _ { t }$ are applied, respectively. Upon the above setting, the external potential energy functional $\mathcal { P }$ is given by 

$$
\mathcal {P} (\boldsymbol {u}) = \int_ {\Omega} \boldsymbol {b} ^ {*} \cdot \boldsymbol {u} \mathrm{d} V + \int_ {\partial \Omega_ {t}} \boldsymbol {t} ^ {*} \cdot \boldsymbol {u} \mathrm{d} A\tag{1}
$$

for the distributed body force $b ^ { * }$ . We adopt the notation that symbols $\sqsubset { \ast }$ represent prescribed (known) quantities whereas symbols ¯ denote effective quantities (such as effective stresses). 

## 2.1 PF models for brittle fracture

In this work, the formulation in the mechanics community is adopted, and the one in the physics community is briefly introduced in Remark 6. Within the context of quasi-static brittle fracture of isotropic elastic solids, the cracks of PFMs are approximated as bands of finite thickness characterised by a crack phase-field parameter<sup>4</sup> $\phi \colon \phi = 1$ represents the cracked material and $\phi = 0$ denotes the intact one. Accordingly, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/47212bea9d8806640ddee4f5333e32d4d8fdc077e89fa39388a32ebb5b8acc17.jpg)



Figure 2: A solid body Ω with the crack set $T \colon$ (a) sharp cracks and (b) approximated diffuse crack bands.


surface energy ${ \varPsi } _ { c } ( T )$ is approximated by 

$$
\Psi_ {c} (\Gamma) = \int_ {\Gamma} G _ {c} \mathrm{d} A \approx \int_ {\Omega} G _ {c} \gamma (\phi ; \nabla \phi) \mathrm{d} A, \qquad \gamma (\phi ; \nabla \phi) = \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\nabla \phi \cdot \nabla \phi) \right]\tag{2a}
$$

where $G _ { c } [ \mathrm { J } / \mathrm { m } ^ { 2 } ]$ is the critical energy release rate or the fracture toughness of the material; $\gamma ( \phi ; \nabla \phi )$ is the crack surface density function [Miehe et al., 2010b]; $l _ { 0 } \in \mathbb { R } ^ { + }$ is the length scale that governs the width of the diffuse crack. Even though it was initially a numerical parameter used to regularise sharp cracks, it is now widely accepted that $l _ { 0 }$ should be considered as a material parameter [Amor et al., 2009]. Thi length scale was experimentally determined in Nguyen et al. [2016b] using the critical stress in uniformly stretched samples. The term $\phi ^ { 2 } / l _ { 0 }$ represents the local part and $l _ { 0 } \left( \nabla \phi \cdot \nabla \phi \right)$ denotes the non-local part that incorporates the length scale $l _ { 0 }$ . Due to the phase-field regularisation of the sharp crack $T ,$ , the stored (bulk) strain energy $\varPsi _ { s }$ depends not only on the displacement field u but also on the crack phase-field $\phi .$ It is now expressed as 

$$
\varPsi_ {s} (\boldsymbol {u}, \phi) = \int_ {\Omega} g (\phi) \psi_ {0} (\boldsymbol {\epsilon} (\boldsymbol {u})) \mathrm{d} V\tag{2b}
$$

where the so-called stress or energetic degradation function $g ( \phi )$ characterises the deterioration of the initial elastic energy function $\psi _ { 0 } ( \epsilon )$ 

The total energy functional of the solid is then given by 

$$
\mathcal {E} (\pmb {u}, \phi) = \int_ {\Omega} g (\phi) \psi_ {0} (\pmb {\epsilon} (\pmb {u})) \mathrm{d} V + \int_ {\Omega} G _ {c} \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\nabla \phi \cdot \nabla \phi) \right] \mathrm{d} V - \mathcal {P} (\pmb {u})\tag{3}
$$

of which minimisers, with appropriate boundary conditions, provide the displacement and phase-fields $( { \pmb u } , \phi )$ [Francfort and Marigo, 1998, Bourdin et al., 2008b]. In this model, crack propagation results from the competition between the bulk and surface energy terms. On the one hand, deformations of an elastic body under load increase the elastic energy. When this value approaches a critical value in a region, it is energetically favourable for the system to decrease the elastic energy by increasing the crack phase-field $\phi$ towards unity. On the other hand, increasing the value of $\phi$ leads to an increase in the surface energy. Note that the total energy functional in Equation (3) is quadratic and convex in u and $\phi$ separately. Therefore, for a fixed $\phi ,$ the energy functional $\boldsymbol { \mathcal { E } } ^ { \circ } ( \boldsymbol { u } , \cdot )$ , can be efficiently minimised by solving a linear system of equations. The same holds for $\mathcal { E } ( \cdot , \phi )$ . As a consequence, the numerical implementation of this PFM is straightforward by means of a very robust algorithm that alternately minimises each field in a staggered manner. 

The major advantages of using phase-field modelling for fracture are summarised as follows: 

the model is purely based on energy minimisation and no assumption of pre-defined cracks is needed such that crack nucleation, growth and coalescence can be automatically determined; 

the model can intrinsically deal with merging and branching of multiple cracks with no additional effort or heuristics; 

the model allows naturally incorporating the multi-field physics owing to its variational structure; 

the model can be generalised effortlessly to three dimensions (cf. Fig. 3), and its computational implementation is straightforward in any dimension<sup>5</sup>. 

The PFMs suffers from the following drawbacks 

high computational cost (sufficiently refined mesh in the damaged zone is necessary to accurately resolve the gradient term, and the robust alternating minimisation solver convergence rate is slow); 

inaccurate location of the crack tips. 

The high computational cost can be tackled using parallel implementations and adaptive remeshing. Compared to discontinuous approaches like XFEM<sup>6</sup>, parallelisation of a PF code can be straightforwardly achieved using the standard domain decomposition method, cf. Fig. 4. Note that ambiguities in determining the crack tips are also found in PD [Agwai et al., 2011, Ha and Bobaru, 2010] and in any other continuous approaches that do not explicitly represent the cracks. This leads to inaccurate predictions of the crack velocity for dynamic fracture. In conclusion, the ease with which PFMs can handle complex threedimensional (3-D) crack patterns, the connection to both fracture mechanics and continuum damage mechanics [Wu et al., 2018], the ease with which they allow handling multi-physics problems and the rigorous variational structure, all render them worthy for further investigations. 

In what follows an overview of the existing PFMs from the mechanics community is given. It all started with the variational approach to brittle fracture [Francfort and Marigo, 1998] which finds its proper mathematical setting in the modern theory of the calculus of variations. The phase-field based regularisation version of Bourdin et al. [2000] was inspired by the Ambrosio and Tortorelli [1990] elliptic regularisation of the free-discontinuity problem characterised by the Mumford-Shah functional [Mumford and Shah, 1989] in image segmentation problems<sup>7</sup>. In Freddi and Royer-Carfagni [2010], the authors claim that the Bourdin et al. [2000] regularised version of the variational approach to fracture is itself a model per se and the original model of Francfort and Marigo [1998] is an approximation. Such a regularised phase-field model is, herein, referred to as an isotropic second-order phase-fieldfracture model. The attribute ‘isotropic’ indicates that the model does not distinguish between tensile and compressive fracture behaviour and the modifier ‘second-order’ refers to the second derivative of the phase-field in the governing equations. An anisotropic version<sup>8</sup> of the model of Bourdin et al. [2000] was presented in Amor et al. [2009] where the elastic energy density is additively decomposed into volumetric and deviatoric components to prevent cracking in compression domains. Yet another anisotropic model was proposed in Lancioni and Royer-Carfagni [2009] for shear fractures and was applied to cracking in the masonry work of the French Panthéon, one of the most famous historical monuments in Paris. Based on the theory of Structured Deformation Freddi and Royer-Carfagni [2010] presented a unified formulation of the different formulations of Bourdin et al. [2000], Amor et al. [2009], Lancioni and Royer-Carfagni [2009] for mode I, mode II, mixed-mode and masonry-like fractures. A fourth-order phase-field model was proposed in Borden et al. [2014] to improve convergence rates for numerical solutions. This fourth-order PFM model was later shown to be a special case of the fracture surface anisotropic PFM of Li et al. [2015b] However, to exploit the attribute of this higher-order model, one needs to consider at least C<sup>1</sup>-continuous basis functions, which can be seamlessly achieved using isogeometric finite elements [Hughes et al., 2005, Cottrell et al., 2009, Nguyen et al., 2015b]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/225c48bb6edfe2673c55f33042e4a83e3caf146e0518fe9a7596ea9e9cddf8df.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/efbb7b089f4d79485e52aa654f2c332fdb0be09833b5238b1ee1ea0c317c67e7.jpg)



Figure 3: A 3-D fracture simulation with a PFM: stress contour on a deformed configuration where elements having φ larger than 0.9 were omitted (left) and the iso-volume $\phi = 0 . 9$ of the phase-field.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/1f57c4444e59d98b01fa8acdfeaa668d9e179e92447d783c2020e374f9932f98.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/291b438bdfe2d04c97549158656a74d9fb1045bb2cb3292c1357d7e44c3d077e.jpg)



(b)



Figure 4: A simulation running on four processors with a phase-field fracture model: (a) colours of different domains and (b) plot of the displacement field on the top left domain and the phase-field on the remaining domains.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f9cbb7003ef3dea890e23f5f0409ec1d3d07463b8e0c180f82a99abc734bb00d.jpg)



Figure 5: Sensitivity of the model result with respect to the length scale parameter: load-displacement curves for 3 cases: $l _ { 0 } = \{ 0 . 0 0 7 5 , 0 . 0 1 5 , 0 . 0 3 0 \}$ mm. The behaviour is totally different to non-local damage or gradient damage models where the larger the length scale the more ductile the behaviour.


Kuhn and Müller [2008, 2010a] presented a model similar to Bourdin’s. The evolution law of the phase-field is determined using the Ginzburg-Landau equation which is well-known in the phase-field modelling of phase transformation in the materials science community. The phase-field theory used to model phase transformations was also adopted in Yalcinkaya et al. [2011] to model plastic slips, resulting in a strain gradient crystal plasticity model. Miehe et al. [2010b] introduced an intuitive formulation of a phase-field fracture model based on pure geometry, continuum mechanics and thermodynamic arguments. Compared to the more formal formulation of Francfort and Marigo [1998] and Bourdin et al. [2000], it may be more accessible to the engineering community. 

All of the above PFMs adopt a quadratic function $\phi ^ { 2 }$ in the crack surface density functional (Equa tion $\left( 2 \right) _ { 2 } )$ . In these standard PFMs, the admissible range $\phi \in [ 0 , 1 ]$ can be intrinsically guaranteed for the resulting exponential distribution of the phase-field [Miehe et al., 2010b]. However, this choice virtually regularises the sharp crack topology into a diffuse crack with infinite support. As a consequence, the phasefield evolution equation has to be solved in the whole computational domain to determine the phase-field value at each point [Moës et al., 2011]. Moreover, damage is initiated at the beginning and the linear elastic behavior prior to the onset of damage cannot be easily dealt with. To address the above issues, Pham et al. [2011] proposed a non-standard PFM using a linear function $\phi ,$ resulting in a diffuse localisation band with a parabolic damage distribution and global responses with an initial linear elastic stage. One side effect is that the crack phase-field cannot be intrinsically guaranteed to remain in the interval [0, 1] in this case. Consequently, the phase-field boundedness has to be explicitly enforced, bringing about extra difficulties to the numerical implementation [Farrell and Maurini, 2017]. It is claimed in Tanné et al. [2018] that a phase-field model with a strictly positive elastic limit is the necessary condition for correctly predicting crack nucleation. 

Wu [2017] proposed a unified phase-field model for both brittle fracture and quasi-brittle failure in which a generic function $\xi \phi + { \bigl ( } 1 - \xi { \bigr ) } \phi ^ { 2 }$ , with $\xi \in [ 0 , 2 ]$ being a constant, was employed in the crack surface density functional (Equation (2) ). Later on, an alternative but much simpler derivation of the PFM was presented in Wu [2018b]. In particular, only standard thermodynamics with internal variables is needed. The evolution law for the crack phase-field is established based on the energetic equivalence between the sharp crack and the geometrically regularised one, bridging the gap between fracture mechanics and continuum damage mechanics. 

Remark 6. The PFMs developed by the physics community are based on the Ginzburg-Landau equation [Aranson et al., 2000, Karma et al., 2001, Henry and Levine, 2004, Henry, 2008, Henry and Adda-Bedia, 2013] but with a double well function $1 6 \phi ^ { 2 } ( 1 - \phi ) ^ { 2 }$ instead of $\phi ^ { 2 }$ in the crack surface density functional given in Equation $( 2 ) _ { 2 }$ . Models belonging to this family are, however, rather distant from Griffith’s fracture theory [Bourdin et al., 2011]. We refer to the review in Spatschek et al. [2011], Ambati et al. [2015a] for more details. 

Remark 7. The variational approach to fracture of Francfort and Marigo [1998] can be referred to as a generalisation of Griffith’s theory for brittle fracture [Schmidt et al., 2009]. And its phase-field regu larised formulation of Bourdin et al. [2000] is not the only approximation candidate. Schmidt et al. [2009] presented an eigenfracture method to the variational approach to fracture. The numerical implementation in the context of both finite element [Pandolfi and Ortiz, 2012, Mitchell et al., 2016] and meshfree [Pandolfi et al., 2014, Li et al., 2015a, 2012] methods were also proposed. Practically, it can be considered as a regularised non-local element-erosion method which does not involve extra equations with auxiliary fields (like the phase-field). An elaborate presentation of this eigen-erosion was reported in Wang and Sun [2017] for poromechanics problems. Even though the method has not yet been studied as extensively as the Bourdin et al. [2000] model, impressive results for problems involving fragmentation, contacts and phase transition were obtained [Pandolfi et al., 2014, Li et al., 2015a, 2012]. Note that PFMs have not yet been applied to those complex problems except the very recent work of Moutsanidis et al. [2018]. Imple mentation of a PFM in the material point method (MPM – which is suitable for large deformation solid problems, see e.g., Sulsky et al. [1994], Nguyen et al. [2016c]) is presented in Kakouris and Triantafyllou [2017]. However, only problems with small strain were considered. Based on our experiences from Sinaie et al. [2017, 2018b], MPM is quite computationally intensive and thus its combination with PFMs would result in a not very practically useful tool. Recently, Xavier et al. [2017] employed the topological derivative [Novotny and Sokolowski, 2013] to approximate the variational approach to fracture of Francfort and Marigo [1998]. The resulting method is rather similar to the eigen-errosion method for brittle fracture. 

## 2.2 PF models for ductile fracture

The phase-field theory for brittle fracture has also been extended to ductile fracture, e.g., Duda et al. [2015], Miehe et al. [2015a], Alessi et al. [2015] and Ambati et al. [2015b, 2016], Borden et al. [2016], Kuhn et al. [2016] where some of them [Miehe et al., 2015a, Borden et al., 2016, Ambati et al., 2016] considered finite deformations. The common point between these models is the decomposition of the stored energy functional into an elastic part and a plastic one, with the fracture part essentially unchanged. The stored energy functional, for example, according to the models of Ambati et al. [2015b], Duda et al. [2015], is given by<sup>9</sup> 

$$
\varPsi_ {s} (\pmb {\epsilon} ^ {e}, \pmb {\epsilon} ^ {p}, \kappa , \phi) = \int_ {\Omega} \Big [ g (\phi) \psi_ {0} (\pmb {\epsilon} ^ {e}) + \psi^ {p} (\kappa) \Big ] \mathrm{d} V\tag{4}
$$

where $\epsilon ^ { e }$ and $\epsilon ^ { p }$ denote the elastic and plastic strains; $\psi ^ { p } ( \kappa )$ is the plastic energy density in terms of the plastic internal variable κ. As can be seen, the plastic deformation is not affected by the phase-field or crack growth, and vice versa. Furthermore, from a numerical point of view, in a staggered scheme, the phase-field sub-problem is no longer linear, which increases the inherent high computational cost of PFMs. In Miehe et al. [2015a], Borden et al. [2016], Kuhn et al. [2016], a remedy for this was proposed through a plastic degradation function $g ^ { p } ( \phi )$ . That is, the plastic energy density is expressed as $g ^ { p } ( \phi ) \psi ^ { p } ( \kappa )$ , leading to the following strain energy functional 

$$
\varPsi_ {s} \left(\boldsymbol {\epsilon} ^ {e}, \boldsymbol {\epsilon} ^ {p}, \kappa , \phi\right) = \int_ {\Omega} \left[ g (\phi) \psi_ {0} \left(\boldsymbol {\epsilon} ^ {e}\right) + g ^ {p} (\phi) \psi^ {p} (\kappa) \right] \mathrm{d} V\tag{5}
$$

Generally, identical degradation functions $g ^ { p } ( \phi ) = g ( \phi )$ are selected [Miehe et al., 2015a]. This is due probably to the fact that classical stress return algorithms for plasticity can be directly reused. In the resulting PF model for ductile fracture, the evolution of the crack phase-field is now affected by the plastic energy density $\psi ^ { p } ( \kappa )$ . We refer to a recent review of Alessi et al. [2018a] on these models for ductile fracture. 

## 2.3 PF models for cohesive fracture

The essential difference between brittle and cohesive fracture is that for the latter the fracture energy is not released abruptly but rather, progressively, with respect to the displacement jump across the fracture surfaces. The first PF model for cohesive fracture was set in Bourdin et al. [2008a] and further developed in Verhoosel and de Borst [2013], May et al. [2015], Nguyen et al. [2016a], Vignollet et al. [2014]. In this model, the surface energy is written as [Verhoosel and de Borst, 2013, May et al., 2015] 

$$
\Psi_ {c} = \int_ {\Omega} G ([   [ \boldsymbol {u} ]   ], \kappa) \gamma (\phi ; \nabla \phi) \mathrm{d} V\tag{6}
$$

where $G ( \mathbb { I } { \boldsymbol { \mathbf { \mathit { u } } } } \mathbb { I } , \kappa )$ is the fracture energy function of which derivative with respect to the displacement jump (or crack opening) [[u]] yields the cohesive traction-separation law, and κ denotes a set of history variables. As the crack opening is not trivial to determine in the smeared format, an auxiliary field v was introduced and constrained to be coincident with the crack opening $[ [ \pmb { u } ] ]$ [Verhoosel and de Borst, 2013]. Furthermore, an additive decomposition of the strain tensor into an elastic part and a cracking part is adopted such that the stored strain energy is now defined as 

$$
\Psi_ {s} = \int_ {\Omega} \psi_ {0} (\pmb {\epsilon} ^ {e}) \mathrm{d} V, \quad \pmb {\epsilon} = \pmb {\epsilon} ^ {e} + \pmb {\epsilon} ^ {c}, \quad \pmb {\epsilon} ^ {c} = (\pmb {n} \otimes^ {s} \pmb {v}) \gamma (\phi ; \nabla \phi)\tag{7}
$$

However, as reported in Verhoosel and de Borst [2013], May et al. [2015], Vignollet et al. [2014], only crack propagation along pre-defined paths i.e., interfacial cracks can be modelled with the above PFM. Moreover, the traction continuity condition has to be introduced to determine the auxiliary variable v, leading inevitably to stress oscillations around the localisation band due to distinct approximations to the stress field and cohesive tractions [Verhoosel and de Borst, 2013]. Nguyen et al. [2016a] avoided using the auxiliary field v by resorting to the level set method. Their model is, however, also applied only to material interfaces (or non-propagating adhesive fractures). 

An alternative approach to model cohesive fracture consists in using an energetic degradation function $g ( \phi )$ which depends on the length scale parameter $l _ { 0 }$ such that the surface energy is not released abruptly as in brittle fracture, but rather, approaches asymptotically Griffith’s critical energy $G _ { c } \operatorname { a s } \phi \to 1 .$ . Such a PFM for cohesive fracture can be found in Freddi and Iurlano [2017] where the energetic degradation function $g ( \phi )$ is proportional to the length scale $l _ { 0 } .$ . Though they have certain attractive attributes, the results are also sensitive to the value of the length scale parameter $l _ { 0 }$ [Freddi and Iurlano, 2017] similarly to the PF model for brittle fracture (cf. Fig. 5). 

Almost at the same time, Wu [2017, 2018b] proposed a novel PF model, dubbed Phase-field regularised cohesive zone model (PF-CZM), for quasi-brittle failure, though it also applies to brittle fracture. With a rational energetic degradation function $g ( \phi )$ in terms of the length scale $l _ { 0 } ,$ , the long tail of the softening curve, typically for failure of quasi-brittle materials such as concrete, can be modelled using the phase field theory. Accordingly, it is not necessary to introduce the auxiliary field $\pmb { v }$ to explicitly approximate the displacement jump u which is, instead, implicitly expressed in terms of the crack phase-field $\phi .$ Furthermore, the numerical results are insensitive to the length scale parameter $l _ { 0 }$ so long as the crack surface is approximated with sufficient precision by the phase-field $\phi$ [Wu and Nguyen, 2018, Nguyen and Wu, 2018]; see Section 3.3. This is true for not only quasi-static and dynamic fracture of homogeneous quasi-brittle materials but also fracture of heterogeneous materials with complex crack patterns [Yang et al., 2019]. All the model parameters can be related to those material properties (e.g., the failure strength, fracture energy, initial slope and ultimate crack opening of the softening curve, etc.) defining the behaviour of cohesive cracks. Interestingly, the model can capture the boundary and size effect of concrete fracture that defied classical non-local damage models [Feng and Wu, 2018]. The analytical proof of the equivalence between this PF-CZM and the discontinuous CZM for a one-dimensional softening bar, see Section 4, was corroborated by numerical results given in Wu et al. [2018] where PF-CZM was numerically compared with cohesive XFEM for some mixed-mode fracture tests. 

## 2.4 PF models for dynamic fracture

PFMs have been applied to dynamic fracture as reported in Larsen et al. [2010], Bourdin et al. [2011], Hofacker and Miehe [2012, 2013], Borden et al. [2012], Schlüter et al. [2014], Li et al. [2016], Bleyer et al. [2017]. The extension of PFMs to dynamic fracture is straightforward based on the assumption that the kinetic energy is not affected by the phase-field and the fracture energy is constant (i.e., independent of the crack velocity). Experimentally observed crack branching can be captured; see for example Fig. 6. More interesting, the dynamic crack instability phenomenon where many small crack branches are present has been successfully captured [Bleyer and Molinari, 2017]. Noteworthy is the work of Nguyen and Wu [2018] which reported results of dynamic fracture simulations independent of mesh discretisation and length scale $l _ { 0 }$ . Note that other methods such as the cracking particle method [Rabczuk and Belytschko 2004, 2007] and the discontinuous Galerkin cohesive interface elements [Nguyen, 2014b] can also model crack branching without any ad hoc criteria, but lead to a somewhat more involved implementation. Non local integral damage models and microplane models can also capture dynamic branching [Ožbolt et al., 2013, Wolff et al., 2015, Pereira et al., 2017]. Most of these studies focused on capturing the branching phenomenon rather than the quantitative crack speeds except for the recent work of Bleyer et al. [2017], Agrawal and Dayal [2017]. We emphasise that established advanced numerical methods such as XFEM and PD fail in predicting experimentally consistent crack velocities [Song et al., 2008, Agwai et al., 2011]. However, the reason of this is not fully understood. It would be interesting to see how PFMs compare with PD or XFEM in predicting the crack velocity. To this end, one issue is how to accurately determine the location of crack tips such that crack velocities can be calculated. One pending issue is how to deal with velocity-dependent fracture energy in a PFM. We anticipate that adding micro-inertia might be one promising solution [Parrinello, 2017, Kamensky et al., 2018] to consider rate effects in PFMs. 

Alternatively, the fracture energy can be made non-constant and rate-dependent. In Section 7.3 some dynamic fracture benchmarks are presented to demonstrate the performance of PFMs. Most of the above works considered dynamic fracture of homogeneous materials except Bleyer et al. [2017], Yılmaz et al. [2018], Carlsson and Isaksson [2018] studied heterogeneous materials. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/5b2867e7540a54962c0bbb0ee49b7181699f9e7abe508dfb97a460e1d61c1632.jpg)



(a) phase-field model


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6385a6af5cbf6454b84f4294e1fb5904ee9122e82d5dbce5f0ce0ea54c6141d9.jpg)



(b) discrete cohesive crack models



Figure 6: Dynamic fracture: Crack branching predicted by (a) the phase-field model and (b) the discrete cohesive crack model [Nguyen, 2014b].


Remark 8. Phase-field degraded kinetic energy (by the same energetic degradation function $g ( \phi ) )$ was adopted in Chen et al. [2017] to predict arbitrary paths of ultra-high-speed cracks. This is supported by the recent material/mass sink theory of Faye et al. [2019]. Therefore, the assumption of phase-field independent kinetic energy and fracture might not apply to fast-growing cracks; see also Agrawal and Dayal [2017]. 

## 2.5 PF models for finite deformation fracture

Extension of the PFMs to finite deformation is also quite straightforward [Miehe and Schänzel, 2014 Hesch and Weinberg, 2014, Miehe et al., 2015b,a, Raina and Miehe, 2016, Gültekin et al., 2016, Ambati et al., 2016, Hesch et al., 2016, 2017]. In Piero et al. [2007], a finite elasticity (precisely compressible neo-Hookean elasticity) version of the original PFM of Bourdin et al. [2000] was presented. Numerical simulations were conducted using spatially adaptive 2-D finite elements. Clayton and Knap [2014] pro posed a similar model but with an anisotropic surface energy and 3-D FE implementations. However, to the best of our knowledge just few works have been reported on the application of PFMs to problems involving extreme deformations under e.g., impacts and fragmentation [Moutsanidis et al., 2018]. 

## 2.6 PF models for three-dimensional fracture

The modeling of three-dimensional fracture is rather challenging. Discrete crack methods such as XFEM or configurational force based remeshing methods can handle 3-D non-planar crack growth, see e.g., Bordas et al. [2008], Fries and Baydoun [2012], Rabczuk et al. [2010], Gurses and Miehe [2009], Gupta and Duarte [2014], Kaczmarczyk et al. [2017], Agathos et al. [2018]. However, at the time of this writing, these methods still suffers from the following issues: (i) complex representation of the 3-D crack surfaces (thus a very intricate implementation), (ii) no merging of non-planar 3-D discrete cracks has been reported, and (iii) numerical robustness (e.g., in XFEM when the crack is very close to a node which requires extra treatment). 

Even though attention has been devoted dominantly to 2-D problems probably owing to the inherentl high computational cost, PFMs can deal straightforwardly with 3-D fractures; see for example Miehe et al. [2010b], Hofacker and Miehe [2012], Borden et al. [2012, 2014], Mesgarnejad et al. [2015], Borden et al. [2016], Liu et al. [2016], Lee et al. [2016b], Gültekin et al. [2016], Pham and Ravi-Chandar [2017]. We note that application of a PFM to 3-D problems does not involve extra computer implementation efforts. This is in strong contrast to discrete crack methods such as XFEM and cohesive interface elements. However, the resulting discrete problems are large – problems that involve 3 million elements are not uncommon [Borden et al., 2012, 2016, Pham and Ravi-Chandar, 2017]. Such simulations are often run using high performance computing facilities [Hofacker and Miehe, 2012, Borden et al., 2014, Mesgarnejad et al., 2015, Lee et al., 2016b, Pham and Ravi-Chandar, 2017]. 

## 2.7 PF models for plate and shell fractures

Crack initiation and propagation in metallic thin-walled structures is a common failure phenomenon encountered in engineering applications (e.g., ship grounding, aircraft fuselage rupture, and automobile vehicle crash). Shell fracture has been modelled using CZMs within a meshfree framework [Rabczuk et al., 2007], a FEM framework using cohesive interface elements [Li and Siegmund, 2002, Cirak et al., 2005, Zavattieri, 2006] or XFEM [Larsson et al., 2011, Ahmed et al., 2012]. Gurson-type constitutive models are also used for shell fracture see for instance [Ren and Li, 2012]. 

Few attempts at extending PFMs to plates and shells are known. The key idea is to project a PFM in a solid mechanics setting to dimensionally-reduced continua (except solid-like shells). Ulmer et al. [2012], Mesgarnejad et al. [2013], Amiri et al. [2014], Ambati and Lorenzis [2016] present shell fracture PFMs using geometrically linear plate/shell formulations. Only Ambati and Lorenzis [2016] consider both brittle and ductile fracture. Recent developments deal with large deformation shell fracture Areias et al. [2016b], Reinoso et al. [2017]. Kirchoff-Love shell (transverse shear strain was thus neglected) theory was used in Kiendl et al. [2016], Amiri et al. [2014] in conjunction with high order smooth basis functions such as NURBS [Hughes et al., 2005] and local max-entropy functions Arroyo and Ortiz [2006] whereas a solid-shell formulation was adopted in Ambati and Lorenzis [2016], Reinoso et al. [2017]. Most of these models adopted the PFM of Bourdin i.e., with the crack surface density function given in Equation (2) PFMs not based on solid-like shell theories employed a single phase-field (thus assuming this field is constant across the thickness) except Areias et al. [2016b] who utilised two phase-fields–one for the lower surface and the other for the upper one. Tearing of brittle thin sheets with a shell PFM was recently given in Li et al. [2018] where the high order PFM of Borden et al. [2014] was combined with a nonlinear Koiter thin shell model. 

## 2.8 PF models for multi-field fracture

The variational nature of PFMs provides a framework to couple fracture with other physical phenomena. This is evidenced in the wide range of problems that have been successfully tackled using this approach. Fracture with thermal effects taken into account has been reported in Bourdin et al. [2014], Miehe et al. [2015b], Schlüter et al. [2016]. Complex periodic crack initiation in a ceramic plate in a quenching test was successfully captured. Extension to fracture of thermo-elastic-plastic solids was given in Miehe et al. [2015a]. In Radszuweit and Kraus [2017] a PFM for fracture is combined with a PFM to represent material phases. Modelling complex 3-D fluid-driven fractures (or hydraulic fractures) have been presented in Mikelic et al.´ [2015], Lee et al. [2016b], Miehe and Mauthe [2016], Lee et al. [2016a, 2017a], Zhou et al. [2018b]. Among many other things, the crack aperture or crack opening is calculated for a diffuse crack formulation and used in the well known cubic law to determine the fluid pressure inside the fractures. Coupling of crystal plasticity and phase-field fracture was presented in Shanthraj et al. [2017], Diehl et al. [2017]. Hydrogen-assisted crack initiation and propagation in high-strength steel specimens using a PFM was reported in Duda et al. [2017], Nguyen et al. [2017b], Martínez-Pañeda et al. [2018] where the fracture energy was degraded by the presence of hydrogen concentration. For completeness, we refer to Wu and Lorenzis [2016], Klinsmann et al. [2016] for similar models but with different applications. 

## 2.9 Structure anisotropy

Modelling fracture of brittle solids with anisotropic surface energy (i.e., orientation-dependent fracture energy) have been reported in e.g., Hakim and Karma [2005], Clayton and Knap [2014], Li et al. [2015b], Nguyen et al. [2017c], Teichtmeister et al. [2017]. These are extensions of the aforementioned PFMs for isotropic solids to anisotropic ones such as single crystals, geological materials including sedimentary and granitic rocks, biological tissues, fiber-reinforced composites etc. We recall that in a PFM the surface energy is approximated as $\begin{array} { r } { \int _ { \Gamma } G _ { c } \mathrm { d } A \approx G _ { c } \int _ { \Omega } \gamma ( \phi ; \nabla \phi ; \nabla ^ { 2 } \phi ) \mathrm { d } V } \end{array}$ where $\gamma ( \phi ; \nabla \phi ; \nabla ^ { 2 } \phi )$ is the crack density 

function which can be of the following form 

$$
\gamma (\phi ; \nabla \phi ; \nabla^ {2} \phi) = \left\{ \begin{array}{l l} \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\nabla \phi \cdot \nabla \phi) \right] & \text { Bourdin   et   al.   [2000]} \\ \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\nabla \phi \cdot \boldsymbol {A} \cdot \nabla \phi) \right] & \text { Teichtmeister   et   al.   [2017]} \\ \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + \frac {l _ {0}}{2} \nabla \phi \cdot \nabla \phi + \frac {l _ {0} ^ {3}}{1 6} (\nabla^ {2} \phi : \mathbb {A}: \nabla^ {2} \phi) \right] & \text { Teichtmeister   et   al.   [2017]} \end{array} \right.\tag{8}
$$

where A and $\mathbb { A }$ are the second-order and fourth-order structure (or fabric) tensors and $\nabla ^ { 2 } \phi$ denotes the second gradient of $\phi .$ . With $\pmb { A } = \pmb { 1 } + \beta \pmb { a } \otimes \pmb { a }$ where a is a given structural director, the resulting PFM can capture anisotropic fracture of transversely isotropic materials with a single damage variable $\phi .$ 

Another approach was introduced by Bleyer and Alessi [2018] where multiple phase-field variables are used to capture different damage mechanisms. Limiting to the case of two damage mechanisms, the free energy functional reads 

$$
\begin{array}{r} \mathcal {E} (\pmb {u}, \phi_ {1}, \phi_ {2}) = \int_ {\Omega} g (\phi_ {1}, \phi_ {2}) \psi_ {0} (\pmb {\epsilon} (\pmb {u})) \mathrm{d} V + \int_ {\Omega} \frac {G _ {c I}}{2} \left[ \frac {1}{l _ {0}} \phi_ {1} ^ {2} + l _ {0} (\nabla \phi_ {1} \cdot \nabla \phi_ {1}) \right] \mathrm{d} V \\ + \int_ {\Omega} \frac {G _ {c I I}}{2} \left[ \frac {1}{l _ {0}} \phi_ {2} ^ {2} + l _ {0} (\nabla \phi_ {2} \cdot \nabla \phi_ {2}) \right] \mathrm{d} V - \mathcal {P} (\pmb {u}) \end{array}\tag{9}
$$

(10) 

where $G _ { c I }$ and $G _ { c I I }$ are the fracture energies of the two mechanisms. 

Interestingly, at the same time with Bleyer and Alessi [2018], Nguyen et al. [2017c] presented a method that used both multiple damage variables and anisotropic fracture surface: 

$$
\begin{array}{r} \mathcal {E} (\pmb {u}, \phi_ {1}, \phi_ {2}) = \int_ {\Omega} g (\phi_ {1}, \phi_ {2}) \psi_ {0} (\pmb {\epsilon} (\pmb {u})) \mathrm{d} V + \int_ {\Omega} \frac {G _ {c I}}{2} \left[ \frac {1}{l _ {0}} \phi_ {1} ^ {2} + l _ {0} (\nabla \phi_ {1} \cdot \pmb {A} _ {1} \cdot \nabla \phi_ {1}) \right] \mathrm{d} V \\ + \int_ {\Omega} \frac {G _ {c I I}}{2} \left[ \frac {1}{l _ {0}} \phi_ {2} ^ {2} + l _ {0} (\nabla \phi_ {2} \cdot \pmb {A} _ {2} \cdot \nabla \phi_ {2}) \right] \mathrm{d} V - \mathcal {P} (\pmb {u}) \end{array}\tag{11}
$$

(12) 

We think that these anisotrpic PFMs can have an impact on modelling fracture of geological materials such as rocks. At this moment, fracture of rock-like materials or cracking under compression has not received as much attention. One notable exception is the work of Zhang et al. [2017a] where the F-criterion proposed by Shen and Stephansson [1994] was utilised to capture the wing cracks and secondary cracks (or shear cracks) usually observed in rock samples, cf. Fig. 7. Few other works are Freddi and Royer-Carfagni [2011], Zhou et al. [2018c], Bryant and Sun [2018]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/b302687c5266cd5e7a70050e32ab12e441cd1b7962063c4a4cc7ed64a1a48c22.jpg)



Figure 7: Fracture of a rock sample under uniaxial compression: crack pattern with the model of Zhang et al. [2017a] $( l _ { 0 } = 0 . 4$ mm). Stable curvilinear wing cracks grow from the notch tips followed by initiation and unstable propagation of secondary cracks which lead to sample failure.


## 2.10 Fracture of layered materials

Fracture of layered materials is a very complex phenomenon that involves bulk fracture, interfacial fracture (of the interfaces between different material layers) and their interaction [Hutchinson and Suo, 1991, van der Meer, 2012]. To our knowledge the literature on this class of problem is scarce. Mesgarnejad et al. [2013], Baldelli et al. [2014] presented a PFM for modelling fracture and debonding of thin films under in-plane and out-of-plane loadings. Nguyen et al. [2016a, 2018] presented a PFM where a zero-thickness interface is also approximated by a diffuse band of finite thickness with the introduction of yet another length scale and an interface scalar field. Paggi and his co-workers have proposed a combined PFM (for the bulk fracture) and discrete CZM (for the zero-thickness interfacial fracture) Paggi and Reinoso [2017], Paggi et al. [2018], Carollo et al. [2018]. Interfacial fracture within a pure PFM (only a single damage field is needed) was been recently presented in Hansen-Dörr et al. [2019] where the interfaces are distributed over a finite length with their own fracture toughness. The problem of crack impinging on an interface was successfully solved [Paggi and Reinoso, 2017, Hansen-Dörr et al., 2019]. However, existing PFMs have not yet been applied to problems with complex delamination and matrix cracking (hundreds of matrix cracks treated with an XFEM formulation) as reported in van der Meer [2012], Vigueras et al. [2015]. 

## 2.11 Fatigue

The formation and propagation of cracks in structures due to fatigue, when the structures are submitted to cyclic loadings, is one of the critical causes of failure in many engineering structures. Fatigue fracture occurs at stress amplitudes which are well below the static fracture strength. There are not many phase-field models for fatigue. Exceptions are Caputo and Fabrizio [2015], Amendola et al. [2016], Boldrini et al. [2016], Alessi et al. [2018b]. The last model seems to be able to capture many aspects of fatigue, thus we briefly present it here. The key point is the reduction of the fracture energy $G _ { c }$ 

The energy density is now given by [Alessi et al., 2018b] 

$$
W (\pmb {\epsilon} (\pmb {u}), \phi ; \nabla \phi) = \psi_ {0} (\pmb {\epsilon} (\pmb {u}), \phi) + \varphi_ {\mathrm{F}} (\phi ; \nabla \phi)\tag{13}
$$

where the second term is the fatigue fracture energy, that is written as 

$$
\varphi_ {\mathrm{F}} = \int_ {0} ^ {t} f (\bar {\alpha}) \dot {\varphi} (\phi ; \nabla \phi) \mathbf {d} \tau , \qquad \varphi (\phi ; \nabla \phi) = \frac {G _ {c}}{2} \bigg (\frac {\phi^ {2}}{l _ {0}} + l _ {0} | \nabla \phi | ^ {2} \bigg)\tag{14}
$$

with $f ( \bar { \alpha } )$ being the fatigue degradation function written in terms of the accumulated (history) fatigue variable $\bar { \alpha } ( { \pmb x } , t )$ which in turn is a function of the fatigue variable α. For high cycle fatigue problems, the computational cost will be extremely high and thus Seiler et al. [2018] presented an efficient 1-D fatigue phase-field model using a local lifetime variable where each load cycle is resolved with one load increment only. 

## 2.12 Validation of PF models

Most of the existing PFMs are validated against brittle fracture [Klinsmann et al., 2015, Mesgarnejad et al., 2015, Dally and Weinberg, 2015, Nguyen et al., 2016b, Ambati et al., 2016, Pham et al., 2017, Zhang et al., 2017b, Nguyen et al., 2017a, Santillán et al., 2017, Tanné et al., 2018], though very few of them are applied to quasi-brittle or cohesive fracture [Wu, 2017, 2018b, Lorentz, 2017] and ductile fracture [Borden et al., 2016]. Klinsmann et al. [2015], Tanné et al. [2018] validated the PFM by checking its agreement with well established results from classical fracture mechanics. Other work compares the phase-field predictions with experimental results. Some benchmark experiments are given in Fig. 8. 

A phase-field model for brittle fracture requires four parameters – Young’s modulus $E _ { 0 }$ , Poisson’s ratio $\nu _ { 0 }$ , the fracture energy $G _ { c }$ and the length scale parameter $l _ { 0 }$ . The former three parameters are material properties and can be determined from standard procedures. The length scale parameter $l _ { 0 }$ is determined using the relation between the maximum stress $\sigma _ { c }$ and the length scale $l _ { \mathrm { 0 } } ~ { \mathrm { e . g } } .$ ., Pham et al. [2011], Borden et al. [2012] based on the homogeneous solution of a 1-D bar under uniaxial traction, $l _ { 0 } ~ = ~ 2 7 / 2 5 6 l _ { \mathrm { c h } }$ with $l _ { \mathrm { c h } }$ being the material characteristic length; see Section 4 for the details. Using this procedure, Mesgarnejad et al. [2015], Nguyen et al. [2016b], Pham et al. [2017], Zhang et al. [2017b] reported very good agreement of the predicted peak loads with the experiment values. Ambati et al. [2016] reported a validation of the PFM for ductile fracture but the value of $l _ { 0 }$ was chosen without explanation. Nguyen et al. [2017a], Martínez-Pañeda et al. [2018] reported excellent agreement between numerical simulations and experiment results for stress corrosion cracking of a nickel based alloy, with the fracture energy dependent on the corrosion degradation level. Santillán et al. [2017] validated the standard PFM in the context of dam engineering but only focused on the fracture pattern. Recently Wu et al. [2017] validated the standard PFM against mixed-mode fracture test results. Although the crack paths are very well captured, the post peak response is not. Usually the length scale is determined from the tensile strength using the exact homogeneous solution as mentioned before. However, this value is often very large compared to the specimen size, see [Zhang et al., 2017b] for concrete and very small e.g., for polymethylmethacrylate (PMMA) materials [Pham et al., 2017]. This has led these authors to scale down and up the length scale quite arbitrarily. For brittle materials with these material properties $E _ { 0 } = 3 2 \mathrm { G P a }$ and the fracture energy $G _ { c } = 3 . 0 \ : \mathrm { J / m ^ { 2 } }$ , one has $l _ { \mathrm { c h } } \approx 1 . 0$ mm (and thus $l _ { 0 } \approx 0 . 1 0 5 \ : \mathrm { m m } )$ , and for quasi-brittle materials such as concrete with $E _ { 0 } = 4 1$ GPa and $G _ { c } = 7 0 . 0 \ : \mathrm { J / m ^ { 2 } }$ one has $l _ { \mathrm { c h } } \approx 2 0 0 . 0$ mm, and thus $l _ { 0 } \approx 2 1$ mm which is too large for specimens of laboratory scales. Consequently, the sharp crack surface is not sufficiently approximated and the Γ-convergence of the resulting PFM cannot be guaranteed. Rather, these models are considered as gradient-damage models [Pham et al., 2011]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/a9373cfded5773adf79aaa4e8a1f405290e63fc26af72a62772fdaaa0986b4f7.jpg)



(a) compact test


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/1fe3e020f82a5b54e70c8f1c81d9670cb4ab545e2668b983fb08d307bb5e26cf.jpg)



(b) L shape test


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/77de11e156649a62297bc5490c29ca3832709d76642f32303eaf4252dd55ce41.jpg)



(c) Sandia fracture test



Figure 8: Some validation benchmarks. Note that by validation we meant both the fracture pattern (qualitative) and the load-displacement responses (quantitative) have been validated.


The Wu [2017, 2018b] PF-CZM applies to both brittle fracture [Wu, 2018a, Wu and Nguyen, 2018] and quasi-brittle failure. In addition to the above parameters i.e., Young’s modulus $E _ { 0 }$ , Poisson’s ratio $\nu _ { 0 }$ the fracture energy $G _ { c }$ and the length scale parameter $l _ { 0 } ,$ , extra parameters related to the target softening curve, e.g., the failure strength $f _ { t } ,$ , the initial slope $k _ { 0 }$ and ultimate crack opening $w _ { c } .$ , are needed. However, all these parameters can be calibrated from standard fracture properties of quasi-brittle solids. More importantly, provided that the crack surface is sufficiently resolved, the value of the length scale $l _ { 0 }$ has negligible effects on the global response. This is in strong contrast to the standard PFM for brittle fracture. Validation against representative benchmark tests show that not only the peak load and fracture pattern, but also the softening regimes, can be well captured [Wu, 2017, 2018a,b, Wu et al., 2018]. Furthermore, size and boundary effects, which defy the classical nonlocal and gradient-enhanced damage models, can also be predicted [Feng and Wu, 2018]. Section 4 provides a concise description of this model. 

## 3 Theoretical aspects

In this section the theoretical aspects of PFMs are addressed in detail. The interested readers are referred to the monograph Bourdin et al. [2008b] for more details from the mathematical points of view. 

## 3.1 Griffith’s theory and the variational approach to brittle fracture

It is in Griffith [1920] that the field of brittle fracture was born. In this energetic approach, crack propagation results from the competition between the bulk energy away from the crack and the surface energy on the crack. From this point of view, the total energy functional $\mathcal { E } ^ { \mathcal { O } }$ in a quasi-static loading regime reads 

$$
\mathcal {E} := \Psi_ {s} + \Psi_ {c} - \mathcal {P}\tag{15}
$$

where the external potential energy $\mathcal { P }$ is given in Equation (1); the stored strain energy $\psi _ { s } ( { \boldsymbol { \mathbf { \em u } } } , I )$ , a volume integral and the surface energy ${ \varPsi } _ { c } ( T )$ , a surface integral are defined as 

$$
\varPsi_ {s} (\boldsymbol {u}) = \int_ {\Omega \backslash \Gamma} \psi_ {0} (\boldsymbol {\epsilon} (\boldsymbol {u}), \Gamma) \mathrm{d} V, \quad \varPsi_ {c} (\Gamma) = \int_ {\Gamma} G _ {c} \mathrm{d} A\tag{16}
$$

The initial (elastic) strain energy density function $\psi _ { 0 } ( \epsilon , T )$ is expressed as usual in terms of the standard linearised strain tensor $\epsilon ( u )$ and also dependent on the crack set $T ;$ the critical energy release rate or the fracture toughness, $G _ { c } [ \mathrm { J } / \mathrm { m } ^ { 2 } ]$ , is usually regarded as a material property. 

Assuming suitable smoothness of all relevant quantities, let us consider the following variational problem [Bourdin et al., 2008b] 

Irreversibility condition: The crack Γ always grows with time from its initial state $\varGamma _ { 0 } .$ , i.e., 

$$
\dot {\Gamma} (t) \geq 0\tag{17}
$$

Unilateral stationarity condition: The pair $( { \pmb u } ( t ) , \varGamma ( t ) )$ is a stationary point of the energy functional $\mathcal { E } ( \pmb { u } , T )$ , or, equivalently, 

$$
\delta \mathcal {E} (\boldsymbol {u}, \Gamma) \geq 0\tag{18}
$$

for any admissible variations ${ \delta } { \mathbf { } } { \mathbf { } }$ satisfying $\delta \mathbf { { u } } = \mathbf { 0 }$ on the boundary $\partial \varOmega _ { u }$ and $\delta { \cal { T } } \geq 0$ 

Energy conservation condition: The energy functional $\mathcal { E } ^ { \mathcal { O } }$ has to satisfy the following energy balance throughout the time evolution: 

$$
\dot {\mathcal {E}} = \int_ {\partial \Omega_ {u}} (\boldsymbol {\sigma} \cdot \boldsymbol {n}) \cdot \dot {\boldsymbol {u}} \mathrm{d} A - \int_ {\Omega} \dot {\boldsymbol {b}} ^ {*} \cdot \boldsymbol {u} \mathrm{d} V - \int_ {\partial \Omega_ {t}} \dot {\boldsymbol {t}} ^ {*} \cdot \boldsymbol {u} \mathrm{d} A\tag{19}
$$

for the time derivative ${ \dot { ( ) } } = \mathrm { d } ( ) / \mathrm { d } t$ 

After calling for integration by parts, the first-order optimisation condition $\delta \mathcal { E } \geq 0$ for the pair $( \pmb { u } , \pmb { I } )$ to be a stationary point is expressed as 

$$
\begin{array}{l} \delta \mathcal {E} = \int_ {\Gamma} (\boldsymbol {\sigma} \cdot \boldsymbol {n}) \cdot \delta \boldsymbol {u} \mathrm{d} A + \int_ {\partial \Omega_ {t}} (\boldsymbol {\sigma} \cdot \boldsymbol {n} - \boldsymbol {t} ^ {*}) \cdot \delta \boldsymbol {u} \mathrm{d} A - \int_ {\Omega \setminus \Gamma} (\nabla \cdot \boldsymbol {\sigma} + \boldsymbol {b} ^ {*}) \cdot \delta \boldsymbol {u} \mathrm{d} V \\ + \left(\frac {\partial \Psi_ {s}}{\partial \Gamma} + G _ {c}\right) \delta \Gamma \geq 0 \end{array}\tag{20}
$$

or, equivalently, 

$$
\nabla \cdot \boldsymbol {\sigma} + \boldsymbol {b} ^ {*} = 0 \quad \text {   in   } \Omega \backslash \Gamma\tag{21a}
$$

$$
\pmb {\sigma} \cdot \pmb {n} = \pmb {t} ^ {*} \qquad \mathrm{on} \partial \Omega_ {t}\tag{21b}
$$

$$
\pmb {\sigma} \cdot \pmb {n} = 0 \qquad \mathrm{on} \Gamma\tag{21c}
$$

and 

$$
\delta \mathcal {E} = (- \mathcal {G} + G _ {c}) \delta \Gamma \geq 0 \quad \Longrightarrow \quad \mathcal {G} - G _ {c} \leq 0\tag{22}
$$

for Cauchy stress tensor $\pmb { \sigma } : = \partial \psi _ { 0 } / \partial \pmb { \epsilon }$ and the energy release rate $\mathcal { G } : = - \partial \varPsi _ { s } / \partial T$ . Similarly, the energy conservation condition, Equation (19), gives 

$$
\left(\mathcal {G} - G _ {c}\right) \dot {\Gamma} = 0\tag{23}
$$

which supplements the following Karush-Kuhn-Tucker loading/unloading conditions 

$$
\dot {\Gamma} \geq 0, \quad \mathcal {G} - G _ {c} \leq 0, \quad \left(\mathcal {G} - G _ {c}\right) \dot {\Gamma} = 0\tag{24}
$$

As can be seen, upon the assumption of smooth crack propagation (referred to Bourdin et al. [2008b] for details), Griffith’s criterion and the above variational formulation are strictly equivalent. 

Griffith’s theory cannot deal with crack initiation; a pre-defined crack $\varGamma _ { 0 }$ has therefore to be introduced. For the existence of a unique smooth crack evolution, Griffith’s criterion implicitly pre-supposes that the potential energy $\mathcal { E } ^ { \mathcal { O } }$ is a convex function of the crack area Γ or length in two dimensions (2-D) [Bourdin et al., 2008b]. In this context, the unilateral stationarity condition given in Equation (18) is actually the first-order optimality condition for $( { \pmb u } ( t ) , \varGamma ( t ) )$ to be a local unilateral minimiser of the potential energy ${ \mathcal { E } } .$ . That is, the crack area (or length) $\boldsymbol { \Gamma } ( t )$ is actually a minimiser of the energy functional $\mathcal { E } ^ { \mathcal { O } }$ among all $T \supseteq T ( t )$ along the pre-defined crack path. Motivated by the above facts, Francfort and Marigo [1998] regarded brittle fracture as an energy minimisation problem; see also Bourdin et al. [2008b]. That is, the pair $( { \pmb u } ( t ) , \varGamma ( t ) )$ is a global minimiser of the potential energy functional ${ \mathcal { E } } .$ , i.e., 

$$
(\boldsymbol {u} (t), \Gamma (t)) = \operatorname{Arg} \left\{\min \mathscr {E} (\boldsymbol {u}, \Gamma) \right\}\tag{25}
$$

among all $r \supseteq r ( t ) \left( \supseteq r _ { 0 } \right)$ if a pre-defined crack $\varGamma _ { 0 }$ exists) and all $\pmb { u } = \pmb { u } ^ { * } ( t )$ on $\partial \varOmega _ { u }$ . Note that for the case in which the crack path $\varGamma$ may be not smooth “enough”, an infimum energy rather than a minimal one should be sought. In such a variational approach to brittle fracture, cracks should propagate along the path of least energy such that crack initiation can be intrinsically dealt with in an initially perfectly sound solid. Furthermore, the solution path $( \boldsymbol { \Gamma } ( t ) , \boldsymbol { \mathbf { \boldsymbol { u } } } ( t ) )$ at any time t can be selected by the unilateral global minimisation condition. In particular, for the crack topology constrained along a pre-defined surface, Griffith’s criterion is exactly retrieved. 

Remark 9. In the mathematical nature, though the above global minimisation based variational approach provides a convenient postulate to predict crack nucleation and propagation path in a unified framework, local minimisers proved a more accurate description of crack evolution. However, compared to the global minimisation postulate in which prediction of crack path is completely topology-free, an appropriate distance has be to introduced in local minimisation between two arbitrary crack states to define a certain topology to the crack admissible space. Such a variational approach to fracture employing localisation minimisation is still an active on-going research topic; see Chambolle et al. [2009], Crismale and Lazzaron [2017] and the references therein. 

## 3.2 Governing equations of PF models in strong form

Equation (25) is usually referred to as a free discontinuity problem [Braides, 1998, Friedman and Spruck, 2012] in which the displacement u and the jump sets $\varGamma$ are both a priori unknown. In order to numerically implement the resulting free discontinuity problem, Bourdin et al. [2000] proposed using the so-called regularised variational fracture model<sup>10</sup> based on the Ambrosio and Tortorelli [1990] regularisation in image segmentation. That is, a crack of zero width is replaced by a diffuse crack of a finite width scaled by the length parameter $l _ { 0 }$ 

Without loss of generality, in the PF model the sharp crack surface $\varGamma$ is regularised by the following functional $T _ { l } ( \phi )$ 

$$
\Gamma \approx \Gamma_ {l} (\phi) = \int_ {\mathcal {B}} \gamma (\phi ; \nabla \phi) \mathrm{d} V\tag{26}
$$

such that the surface energy $\varPsi _ { c }$ is approximated as 

$$
\varPsi_ {c} := \int_ {\Gamma} G _ {c} \mathrm{d} \Gamma \approx \int_ {\mathcal {B}} G _ {c} \gamma (\phi ; \nabla \phi) \mathrm{d} V\tag{27}
$$

where the crack surface density functiona $\gamma ( \phi ; \nabla \phi )$ is expressed in terms of the crack phase-field $\phi \in [ 0 , 1 ]$ and its gradient $\nabla \phi$ within the localisation band $B \subseteq { \mathcal { Q } }$ over which the crack is smeared. In the literature sometimes notation $d ( x )$ is adopted for the crack phase-field to connect with the theory of continuum damage mechanics. Note that in practice the localisation band $B ,$ with the external boundary denoted by ∂ , can be a small region of the considered domain $\varOmega ,$ , ensuing reduced computational cost in the modelling of localised failure in solids and structures. 

Due to the smeared nature of the crack phase-field, the stored energy functional $\varPsi _ { s }$ is given by 

$$
\varPsi_ {s} (\pmb {u}, \phi) = \int_ {\Omega} \psi (\pmb {\epsilon} (\pmb {u}), \phi) \mathrm{d} V\tag{28}
$$

where the free energy density function $\psi ( \epsilon , \phi )$ depends on the strain tensor $\mathbf { \epsilon } \mathbf { \tilde { \epsilon } } ( \mathbf { u } )$ and the crack phase-field $\phi ,$ with its explicit expression to be specified later. By virtue of thermodynamic reasoning, the following material law is obtained (see Appendix C for details) 

$$
\pmb {\sigma} = \frac {\partial \psi}{\partial \pmb {\epsilon}}\tag{29}
$$

associated with the free energy density function $\psi ( \epsilon , \phi )$ 

With the external potential functional $\mathcal { P }$ introduced in Equation (1), the total energy functional is expressed as 

$$
\mathcal {E} (\boldsymbol {u}, \phi) = \int_ {\Omega} \psi (\boldsymbol {\epsilon} (\boldsymbol {u}), \phi) \mathrm{d} V + \int_ {\mathcal {B}} G _ {c} \gamma (\phi ; \nabla \phi) \mathrm{d} V - \int_ {\Omega} \boldsymbol {b} ^ {*} \cdot \boldsymbol {u} \mathrm{d} V - \int_ {\partial \Omega_ {t}} \boldsymbol {t} ^ {*} \cdot \boldsymbol {u} \mathrm{d} A\tag{30}
$$

The displacement and phase-fields $( { \pmb u } , \phi )$ are determined by solving the following minimisation problem 

$$
\left(\boldsymbol {u} (\boldsymbol {x}), \phi (\boldsymbol {x})\right) = \operatorname{Arg} \left\{\min \mathscr {E} (\boldsymbol {u}, \phi) \right\} \quad \text { subjected   to } \quad \dot {d} \geq 0, d \in [ 0, 1 ]\tag{31}
$$

which is the phase-field counterpart of Equation (25). To derive the governing equations, we consider the first variation of the energy functional $\mathcal { E } ( \boldsymbol { u } , \phi )$ (see Appendix A for derivation) 

$$
\delta \mathcal {E} = \int_ {\Omega} \pmb {\sigma} \delta \pmb {\epsilon} \mathrm{d} V + \int_ {\mathcal {B}} \frac {\partial \psi}{\partial \phi} \delta \phi \mathrm{d} V + \int_ {\mathcal {B}} G _ {c} \left(\frac {\partial \gamma}{\partial \phi} \delta \phi + \frac {\partial \gamma}{\partial \nabla \phi} \cdot \delta \nabla \phi\right) \mathrm{d} V - \int_ {\Omega} \pmb {b} ^ {*} \cdot \delta \pmb {u} \mathrm{d} V - \int_ {\partial \Omega_ {t}} \pmb {t} ^ {*} \cdot \delta \pmb {u} \mathrm{d} A\tag{32}
$$

Application of the divergence theorem yields 

$$
\begin{array}{r l} & {\delta \mathcal {E} = - \int_ {\Omega} (\nabla \cdot \pmb {\sigma} + \pmb {b} ^ {*}) \cdot \delta \pmb {u} \mathrm{d} V + \int_ {\partial \Omega_ {t}} (\pmb {\sigma} \cdot \pmb {n} - \pmb {t} ^ {*}) \cdot \delta \pmb {u} \mathrm{d} A} \\ & {\qquad + \int_ {\mathcal {B}} \left[ \frac {\partial \psi}{\partial \phi} + G _ {c} \delta_ {\phi} \gamma \right] \delta \phi \mathrm{d} V + \int_ {\partial \mathcal {B}} G _ {c} \Bigl (\frac {\partial \gamma}{\partial \nabla \phi} \cdot \pmb {n} _ {\mathcal {B}} \Bigr) \mathrm{d} A} \end{array}\tag{33}
$$

with $\delta _ { \phi } \gamma$ being the variational (or functional) derivative 

$$
\delta_ {\phi} \gamma := \frac {\partial \gamma}{\partial \phi} - \nabla \cdot \left(\frac {\partial \gamma}{\partial \nabla \phi}\right)\tag{34}
$$

where $\mathbf { \delta } _ { n _ { B } }$ is the outward unit normal vector of the boundary $\partial B$ of the localisation band . 

The unilateral stationary condition of the total energy functional i.e., $\delta \mathcal { E } = 0$ for $\delta \phi > 0$ and $\delta \mathcal { E } > 0$ for $\delta \phi = 0$ , gives the following governing equations in strong form 

$$
\nabla \cdot \pmb {\sigma} + \pmb {b} ^ {*} = 0 \qquad \mathrm{in} \Omega\tag{35a}
$$

$$
\pmb {\sigma} \cdot \pmb {n} = \pmb {t} ^ {*} \qquad \mathrm{on} \partial \Omega_ {t}\tag{35b}
$$

as well as 

$$
\left\{ \begin{array}{l l} Y - G _ {c} \delta_ {\phi} \gamma = 0 & \dot {\phi} > 0 \\ Y - G _ {c} \delta_ {\phi} \gamma <   0 & \dot {\phi} = 0 \end{array} \right. \quad \text { in } \mathcal {B}\tag{36a}
$$

$$
\frac {\partial \gamma}{\partial \nabla \phi} \cdot \boldsymbol {n} _ {\mathcal {B}} = 0 \quad \text { on } \partial \mathcal {B}\tag{36b}
$$

where the conjugate energetic crack drivingforce Y is associated with the free energy function $\psi ( \epsilon , \phi )$ 

$$
Y := - \frac {\partial \psi}{\partial \phi} = - \frac {\partial \psi}{\partial g} \frac {\partial g}{\partial \phi} = - g ^ {\prime} (\phi) \bar {Y}, \quad \bar {Y} := \frac {\partial \psi}{\partial g}\tag{37}
$$

for the effective crack driving force $\bar { Y }$ associated to an energetic degradation function $g ( \phi ) : [ 0 , 1 ]  [ 1 , 0 ]$ to be specified later. Equation (35a) is the classical force balance equation, whereas Equation (36a) refers to the phase-field evolution equation. Equations (35b) and (36b) are both natural boundary conditions. 

Remark 10. Being an important ingredient of the PFM, the crack irreversibility requires that $T _ { n } \subseteq T _ { n + 1 }$ for the crack sets $\varGamma _ { n }$ and $\varGamma _ { n + 1 }$ at times $n$ and $n + 1$ , respectively. In terms of the regularised crack surface functional $T _ { l } ( \phi )$ , this condition becomes 

$$
\dot {\Gamma_ {l}} := \frac {\mathrm{d}}{\mathrm{d} t} \Gamma_ {l} (\phi) \geq 0\tag{38}
$$

where the rate $\dot { T _ { l } }$ is elaborated as 

$$
\dot {\Gamma} _ {l} = \int_ {\mathcal {B}} \dot {\gamma} \mathrm{d} V = \int_ {\mathcal {B}} \dot {\phi} \delta_ {\phi} \gamma \mathrm{d} V\tag{39}
$$

It can be seen that the global crack irreversibility condition (39) is satisfied if the following local conditions are met 

$$
\delta_ {\phi} \gamma \geq 0, \quad \dot {\phi} \geq 0\tag{40}
$$

where the first condition can be enforced easily — by adopting a decreasing degradation function $g ( \phi )$ which only applies to the non-negative quantity $\bar { Y } = \psi _ { 0 } ^ { + 1 1 }$ . Thus, the crack irreversibility condition boil down to the enforcement of $\dot { \phi } \geq 0$ 

Remark 11. The phase-field evolution Equation (36a) can be rewritten as the following Karush-Kuhn-Tucker conditions [Wu, 2017, 2018b] 

$$
\dot {\phi} \geq 0, \qquad f (Y, \phi) \leq 0, \qquad \dot {\phi} f (Y, \phi) \equiv 0\tag{41}
$$

where the damage criterion $f ( Y , \phi ) \leq 0$ is defined as 

$$
f (Y, \phi) := Y - G _ {c} \delta_ {\phi} \gamma \leq 0\tag{42}
$$

Upon loading of the crack phase-field i.e., $\dot { \phi } > 0$ it follows from $f ( Y , \phi ) = 0$ that 

$$
\underbrace {G _ {c}   \delta_ {\phi} \gamma} _ {\text { crack   resistance }} = Y := \underbrace {- g ^ {\prime} (\phi) \bar {Y}} _ {\text { crack   driving   force }}\tag{43}
$$

As can be seen, the crack phase-field is zero for $- g ^ { \prime } ( \phi ) \bar { Y } / G _ { c } = 0$ . Therefore, in order to prevent cracking in some regions, it is simple to assign a very high value to $G _ { c }$ . This technique can be used to avoid unphysical damage near supports or point loads. Another strategy achieving the same goal is to impose straightforwardly the Dirichlet boundary conditions/constraints $\phi ( { \pmb x } ) = 0$ on selected nodes. 

Remark 12. In the case of dynamic fracture, we simply consider an extra kinetic energy which is independent of the phase-field, thus ensuring mass conversation (otherwise, the density would be decreasing and therefore mass is changed as the volume is the same). Furthermore, micro inertias can be accounted for as well. Upon this setting, an extra kinetic energy $\mathcal { H }$ is defined in terms of the velocity field $\dot { \pmb { u } } : = \mathrm { d } \pmb { u } / \mathrm { d } t$ and damage rate field $\dot { d } : = \mathrm { d } d / \mathrm { d } t$ , i.e., 

$$
\mathcal {K} = \int_ {\Omega} \frac {1}{2} \rho \dot {\boldsymbol {u}} \cdot \dot {\boldsymbol {u}} \mathrm{d} V + \int_ {\mathcal {B}} \frac {1}{2} \varrho \dot {d} \cdot \dot {d} \mathrm{d} V\tag{44}
$$

for the coefficient $\varrho$ of dimension [kg/m]. Note that the above kinetic energy is independent of the phase-field, thus ensuring mass conversation. The Hamilton’s action functional is now given by 

$$
\mathcal {A} := \int_ {t _ {1}} ^ {t _ {2}} \left(\mathcal {E} - \mathcal {K}\right) \mathrm{d} t\tag{45}
$$

at two specified times $t _ { 1 }$ and $t _ { 2 }$ . Hamilton’s principle $\delta { \mathcal { A } } = 0$ then yields the following dynamic equilibrium equation 

$$
\begin{array}{c c} \nabla \cdot \boldsymbol {\sigma} + \boldsymbol {b} = \rho \ddot {\boldsymbol {u}} & \text {in} \varOmega \\ Y - G _ {c}   \delta_ {\phi} \gamma \leq \varrho \ddot {\phi} & \text {in} \mathcal {B} \end{array}\tag{46a}
$$

(46b) 

for the acceleration fields $\ddot { \pmb u } : = \mathrm { d } ^ { 2 } { \pmb u } / \mathrm { d } t ^ { 2 }$ and $\ddot { \phi } : = \mathrm { d } ^ { 2 } \phi / \mathrm { d } t ^ { 2 }$ . Similarly, extra terms can be added to account for the viscosity-related damping effects, i.e., 

$$
\nabla \cdot \boldsymbol {\sigma} + \boldsymbol {b} = \rho \ddot {\boldsymbol {u}} + \mu \dot {\boldsymbol {u}} \quad \text { in } \Omega\tag{47a}
$$

$$
Y - G _ {c} \delta_ {\phi} \gamma \leq \varrho \ddot {\phi} + \eta \dot {d} \quad \text {in} \mathcal {B}\tag{47b}
$$

for the viscosity coefficients $\mu > 0$ and $\eta > 0$ The natural boundary conditions (35b) and (36b) remains unchanged. In the literature, Equation (47b) usually refers to as the hyperbolically regularised damage evolution law, which recovers the parabolic one with $\varrho = 0$ and the classical elliptical one for $\varrho = 0 \mathrm { ~ a n d ~ } \eta = 0 ;$ see Kamensky et al. [2018], Parrinello [2017] for some discussion. Note that the parabolic phase-field equation can be formally derived using the microforces concept of Gurtin [1996] and Staroselsky et al. [2018] presented a new derivation using a micromechanics-based Lagrangian density. We refer to Appendix C for details. In this work, only the standard elliptic regularisation (36a) is considered. 

Remark 13. The above PF formulation can be easily extended to ductile fracture, with the free energy density function $\psi$ additively decomposed into an elastic part and a plastic part i.e., 

$$
\psi (\epsilon^ {e}, \kappa , \phi) = \psi^ {e} (\epsilon^ {e}, \phi) + \psi^ {p} (\kappa , \phi)\tag{48}
$$

Accordingly, the stress field is given by 

$$
\pmb {\sigma} = \frac {\partial \psi^ {e}}{\partial \pmb {\epsilon} ^ {e}}\tag{49}
$$

and all the governing equations given in Equations (35) and (36) still apply. Note that in the resulting model, the evolution of the crack phase-field is also affected by the plastic free energy potential $\psi ^ { p }$ . In this work we do not intend to elaborate further on PFMs for ductile fracture and interested reader is referred to e.g., Ambati et al. [2015b], Miehe et al. [2015b], Borden et al. [2016], Alessi et al. [2018a] for more details. 

## 3.3 Phase-field approximation of a sharp crack topology

The key aspect of PF models is the approximation of sharp crack topologies/geometries by a diffuse crack smeared within a localisation band $\boldsymbol { B }$ of a finite width controlled by the length scale $l _ { 0 }$ . 

## 3.3.1 Classical geometric crack function

In order to better explain the phase-field regularisation of the sharp crack topology, let us consider a diffuse representation of a 1-D crack at $x = 0$ by the following exponential equation [Lancioni and Royer-Carfagni, 2009, Miehe et al., 2010b]: 

$$
\phi (x) = \exp \left(- \frac {| x |}{l _ {0}}\right)\tag{50}
$$

which satisfies the properties 

$$
\phi (x = 0) = 1, \quad \phi (x) \rightarrow 0: x \rightarrow \pm \infty\tag{51}
$$

for the length scale parameter $l _ { 0 } \in \mathbb { R } ^ { + }$ . Fig. 9 plots the phase-field profile $\phi ( d )$ corresponding to different values of $l _ { 0 }$ . Clearly, the crack phase-field $\phi ( x )$ has an infinite support [Miehe et al., 2010b]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/8909d56ae7768626ef78e4c43795492658b1858e6aa1e4de89436cc85834b8a7.jpg)



Figure 9: Diffuse representation of a crack at $x = 0$ for various length parameters $l _ { 0 }$ . Note the cusp profile of $\phi ( x )$ which is typical for the second-order phase-field model.


It can be easily verified that the crack phase-field given in Equation (50) is a solution to the following ordinary differential equation (ODE) 

$$
\frac {1}{l _ {0}} \phi (x) - l _ {0} \phi^ {\prime \prime} (x) = 0\tag{52}
$$

supplemented by the boundary conditions in Equation (51). Consistent with the variational approach to fracture, we seek for a crack surface functional of which the minimisation condition yields the ODE specified in Equation (52) i.e., 

$$
\Gamma_ {l} (\phi) = \int_ {- \infty} ^ {+ \infty} \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\phi^ {\prime}) ^ {2} \right] \mathrm{d} x = \int_ {- \infty} ^ {+ \infty} \gamma (\phi ; \nabla \phi) \mathrm{d} x\tag{53}
$$

where the crack surface densityfunction – a term proposed in Miehe et al. [2010b], $\gamma ( \phi ; \nabla \phi )$ , is defined by 

$$
\gamma (\phi ; \nabla \phi) = \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\phi^ {\prime}) ^ {2} \right]\tag{54}
$$

As the length scale $l _ { 0 }$ approaches to zero, the regularised crack surface $\varGamma _ { l }$ converges to a sharp crack in the context of the Γ-convergence theorem [Braides, 1998]. 

Extension to multi-dimensions is straightforward i.e., 

$$
\gamma (\phi ; \nabla \phi) = \frac {1}{2} \left[ \frac {1}{l _ {0}} \phi^ {2} + l _ {0} (\nabla \phi \cdot \nabla \phi) \right], \qquad \delta_ {\phi} \gamma = \frac {1}{l _ {0}} \phi - l _ {0} \Delta \phi\tag{55}
$$

for the Lapacian operator $\Delta \phi : = \nabla \cdot ( \nabla \phi )$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4cfe97effb4014c177ae49916b9ac2e434725ad35928f47f0ad74138aae9f79e.jpg)



Figure 10: Diffuse representation of a crack at $y = 0 . 5 , 0 \leq x \leq 0 . 5$ on a square domain of unit length. From left to right, $\varGamma _ { l } = 0 . 5 8 4 5$ for $l _ { 0 } = 0 . 5 , T _ { l } = 0 . 5 5 0 7$ for $l _ { 0 } = 0 . 1$ and ${ \varGamma _ { l } } = 0 . 5 1 1 3$ for $l _ { 0 } = 0 . 0 2$ . A mesh of $1 0 0 \times 1 0 0$ bilinear quadrilateral elements is used.


A test example is given to illustrate the diffuse representation of 2-D cracks following Miehe et al. [2010b]. A square domain of unit length with a horizontal crack at $y = 0 . 5 , 0 \leq x \leq 0 . 5$ (the origin is at the lower left corner of the square). A mesh of $1 0 0 \times 1 0 0$ bilinear quadrilateral elements is used. Note that the mesh has to be constructed in such a way that there are nodes on the horizontal line $y = 0 . 5$ . The linear scalar FE problem is given by (see Section 5 for details) 

$$
\mathbf {K} ^ {\phi \phi} \bar {\mathbf {a}} = \mathbf {0}, \qquad \bar {K} _ {I J} ^ {\phi \phi} = \int_ {\Omega} \left[ G _ {c} l _ {0} \frac {\partial N _ {I}}{\partial x _ {i}} \frac {\partial N _ {J}}{\partial x _ {i}} + \frac {G _ {c}}{l _ {0}} N _ {I} N _ {J} \right] \mathrm{d} V\tag{56}
$$

subject to the Dirichlet boundary condition $\phi = 1$ for the nodes locating on the crack. Fig. 10 shows the distribution of the crack phase-field for three different values of $l _ { 0 } = \{ 0 . 5 , 0 . 0 2 , 0 . 0 5 \}$ . As can be seen, only for sufficiently small values of the length scale $l _ { 0 } ,$ can the approximation of the sharp crack surface be of sufficient precision. Note that the regularised crack surface $\varGamma _ { l }$ was calculated in a post-processing step using Equation (53). We refer to Linse et al. [2017], Freddi [2019] for extensive studies on the convergence of the phase-field surface energy to the discrete counterpart. Their analyses however limited to the standard PFM with the crack density function given by Equation (55). 

Remark 14. In the literature e.g., Borden et al. [2012], a different form of the crack surface density function is usually used: 

$$
\gamma (s; \nabla s) = \frac {1}{4 \epsilon} (1 - s) ^ {2} + \epsilon (\nabla s \cdot \nabla s)\tag{57}
$$

Due to the relation $\epsilon = l _ { 0 } / 2$ and $s = 1 - \phi .$ , the above formulation is equivalent to Miehe’s model [Miehe et al., 2010b]. We prefer to Equation (55) where the crack phase-field $\phi$ finds roots in the damage variable in continuum damage mechanics. 

## 3.3.2 Generic geometric crack function

The crack surface density function $\gamma ( \phi ; \nabla \phi )$ in Equation (55) is not the unique one that can be used to regularise the sharp crack topology. Without loss of generality, let us consider the following generic form of the crack surface density function [Wu, 2017] 

$$
\gamma (\phi ; \nabla \phi) = \frac {1}{c _ {0}} \Big [ \frac {1}{l _ {0}} \alpha (\phi) + l _ {0} \big | \nabla \phi \big | ^ {2} \Big ], \qquad \delta_ {\phi} \gamma = \frac {1}{c _ {0}} \Big [ \frac {1}{l _ {0}} \alpha^ {\prime} (\phi) - 2 l _ {0} \Delta \phi \Big ]\tag{58}
$$

where the crack surface density function $\gamma ( \phi ; \nabla \phi )$ is characterised by the so-called geometric crack function $\alpha ( \phi )$ ; the scaling parameter $\begin{array} { r } { c _ { 0 } : = 4 \int _ { 0 } ^ { 1 } \alpha ^ { \frac { 1 } { 2 } } ( \hat { \phi } ) \mathrm { d } \hat { \phi } } \end{array}$ is introduced such that the sharp crack surface $\varGamma$ is recovered for a fully softened crack. The resulting profile of the crack phase-field $\phi ( x )$ for the 1-D crack initiated at $x = 0$ is given by 

$$
x (\phi) = l _ {0} \int_ {\phi} ^ {1} \alpha^ {- \frac {1}{2}} (\hat {\phi}) \mathrm{d} \hat {\phi}\tag{59}
$$


As can be seen, the geometric crack function $\alpha ( \phi )$ determines the distribution of the crack phase-field.


<table><tr><td><eq>\alpha(\phi)</eq></td><td><eq>\xi</eq></td><td><eq>c_0</eq></td><td><eq>\phi(x)</eq></td></tr><tr><td><eq>\phi^2</eq></td><td>0</td><td>2</td><td><eq>\exp\left(-\frac{|x|}{l_0}\right)</eq></td></tr><tr><td><eq>\phi</eq></td><td>1</td><td>8/3</td><td><eq>\left(1-\frac{|x|}{2l_0}\right)^2</eq></td></tr><tr><td><eq>2\phi - \phi^2</eq></td><td>2</td><td><eq>\pi</eq></td><td><eq>1-\sin\left(\frac{|x|}{l_0}\right)</eq></td></tr></table>


Table 1: Generic geometric crack function α(φ) and the resulting crack phase-field $\phi ( x )$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/d62a051fecf2d300bbb537c9041138c043baa510618969c9af1dd573eae4a042.jpg)



Figure 11: Crack phase-field φ(x) for different geometric crack functions $\alpha ( \phi )$


The geometric crack function $\alpha ( \phi ) \in [ 0 , 1 ]$ is assumed to satisfy the following properties 

$$
\alpha (0) = 0, \qquad \alpha (1) = 1\tag{60}
$$

Though higher-oder polynomials can be considered as well, Wu [2017] proposed the following quadratic one 

$$
\alpha (\phi) = \xi \phi + (1 - \xi) \phi^ {2} \in [ 0, 1 ] \quad \forall \phi \in [ 0, 1 ]\tag{61}
$$

for the non-negative parameter $\xi \in [ 0 , 2 ] ;$ ; otherwise, $\alpha ( \phi ) \in [ 0 , 1 ]$ cannot be guaranteed. For various values of $\xi \in [ 0 , 2 ]$ , the resulting crack phase-fields $\phi ( x )$ are summarised in Table 1 and shown in Fig. 11. In Fig. 12, the localisation (or damage) band obtained with different α are given for a traction bar. As can be seen, the localisation bandwidth decreases with larger value $\xi \in [ 0 , 2 ]$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/587e39c7064a91adbf52bd9d5683a2628a48fafbc3a0005dcda02a980c49fee8.jpg)



Figure 12: Distribution of the phase-field $\phi$ for a traction bar with different geometric crack functions.


In PF models for brittle fracture, the quadratic geometric crack function $\alpha ( \phi ) = \phi ^ { 2 }$ with $\xi = 0$ [Bourdin et al., 2000, Miehe et al., 2010b] and its linear counterpart $\alpha ( \phi ) = \phi$ with $\xi = 1$ [Pham et al., 2011] have been dominantly adopted in the literature, resulting in a localisation bandwidth of an infinite support and of a finite one $4 l _ { 0 }$ , respectively (see Fig. 12). In $\mathrm { { W u } } ^ { \prime } \mathrm { { s } }$ PFM [Wu, 2017, 2018b] for both brittle fracture and quasi-brittle failure the geometric crack function $\alpha ( \phi ) = 2 \phi - \phi ^ { 2 }$ with $\xi = 2$ is used, resulting in a sinusoidal distribution of the crack phase-field with a finite bandwidth $\pi l _ { 0 }$ . The other geometric crack functions commonly adopted in the literature are discussed in Remark 15. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/3023696cd2694ae73e5acc874f531fdd737fd65a277edaed5c5f13e46ec7c1a0.jpg)



(a) $\varGamma _ { l } = 0 . 5 0 9 0$ for $l _ { 0 } = 0 . 0 2$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/a63dff49ba4b18c24891d8d222185f7a3978ca9bd72f66432d29f1b5bb43e27b.jpg)



(b) $T _ { l } = 0 . 5 0 4 7$ for $l _ { 0 } = 0 . 0 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/c9e3a3a4d8bb648c6dcaac193750963199775dcae01766c9af0e8b1927a5a5ed.jpg)



(c) $\varGamma _ { l } = 0 . 5 0 3 1$ for l<sub>0</sub> = 0.005



Figure 13: Γ-convergence of a unit square plate with an edge crack: regularised crack surface $T _ { l } ( \phi )$ governed by $\alpha ( \phi ) = 2 \phi - \phi ^ { 2 }$ for different length scales $l _ { 0 }$ and a fixed mesh size $h = 0 . 0 0 1$ . The sequence of pictures depicts the Γ-convergence $\Gamma _ { l }  \Gamma _ { d } = 0 . 5$ of the crack surface functional in Equation (26) as the length scale $l _ { 0 }  0$ . Note the finite support of the resulting localisation band in all cases.


In order to demonstrate Γ-convergence of the regularised crack surface functional (Equation (58)), let us consider the same unit square plate with a horizontal edge crack as before. The crack phase-field in the entire plate is solved by the finite element approximation of the minimisation problem set in Equation (26), with the Dirichlet boundary condition $\phi = 1$ imposed for the nodes located on the crack line. Several length scale parameters $l _ { 0 } = 0 . 0 2 , 0 . 0 1 , 0 . 0 0 5$ are investigated for the geometric crack function $\alpha ( \phi ) = 2 \phi - \phi ^ { 2 }$ In order to resolve these length scales, a mesh with fixed size $h = 0 . 0 0 1$ is used to discretise the plate resulting in about 1 325 000 unstructured constant strain triangular elements. The computed distributions of the crack phase-field are shown in Figure 13. The length scale $l _ { 0 } = 0 . 0 2$ yields an approximated regularised crack surface $\varGamma _ { l } = 0 . 5 0 9 0$ , while the smallest one $l _ { 0 } = 0 . 0 0 5$ gives ${ T _ { l } } = 0 . 5 0 3 1 \approx { T _ { d } } = 0 . 5$ . As expected, the Γ-convergence of the regularised crack surface functional to its sharp crack counterpart is guaranteed, 


so long as the incorporated length scale $l _ { 0 }$ can be resolved with a sufficiently fine mesh. Furthermore, all the calculated crack phase-fields are of finite support, localised within a narrow band whose width is scaled by the length scale $l _ { 0 } .$ . This fact is in strong contrast to those shown in Fig. 10 corresponding to the geometric crack function $\alpha ( \phi ) = \phi ^ { 2 }$


<table><tr><td>α(φ)</td><td>c0</td><td>authors</td></tr><tr><td>φ</td><td>8/3</td><td>Pham et al. [2011]</td></tr><tr><td>φ2</td><td>2.0</td><td>Bourdin et al. [2000]</td></tr><tr><td>1-(1-φ)p/2</td><td>-</td><td>Pham et al. [2011]</td></tr><tr><td>1-(1-φ)2</td><td>π</td><td>Alessi et al. [2015]</td></tr><tr><td>ξφ+(1-ξ)φ2</td><td>-</td><td>Wu [2017]</td></tr><tr><td>16φ2(1-φ)2</td><td>8/3</td><td>Karma et al. [2001]</td></tr></table>


Table 2: Commonly adopted geometric crack functions $\alpha ( \phi )$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4eb5ef72d12128bcf0b3cf881a396209aafb68fd78cb9548ba5285f8d82ce0ea.jpg)



(a) monotonic functions


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/0b432f068f72acfd1feb70c41bcd3def769656dbc71f555745ead554053a1ab3.jpg)



(b) double well function



Figure 14: Plots of different geometric functions. Note that $\alpha = \phi ^ { 2 }$ is the only function that has a local minimum at $\phi = 0$


Remark 15. Some of geometric crack functions commonly adopted in the literature are summarised in Table 2. The table is not meant to be exhautive and several other alternatives exist [Lancioni and Corinaldesi, 2017]. Clearly, for $p = 4$ and $\xi = 2$ , the third, fourth and fifth equations are identical. From a numerical point of view, the case of $\alpha = \phi ^ { 2 }$ renders the phase-field problem (within a staggered scheme) linear and thus computationally attractive. Moreover, the admissible range $0 \leq \phi \leq 1$ is intrinsically satisfied. For other functional forms, special strategies have to be introduced to guarantee the boundedness $0 \leq \phi \leq 1$ This can be seen from Fig. 14 where the quadratic function $\alpha = \phi ^ { 2 }$ is the only function that has a local minimum at $\phi = 0$ , i.e. the unbroken state. Therefore, in the absence of mechanical strains $\phi = 0$ is a minimiser of the total energy. Note that the last double-well function $\alpha ( \phi ) = 1 6 \phi ^ { 2 } ( 1 - \phi ) ^ { 2 }$ has been frequently adopted in PFMs developed by the physics community [Karma et al., 2001]. However, it is not related to the well-accepted Griffith’s theory [Bourdin et al., 2011]. 

## 3.4 Stored energy functional

The stored energy functional describes a smooth transition from the intact bulk material to the fully crack state, characterised by the initial free energy density function $\psi _ { 0 } ( \epsilon )$ and an energetic/stress degradation function $g : \phi  g ( \phi ) : [ 0 , 1 ]  [ 1 , 0 ]$ . In this section, the former is discussed and the later is deferred to Section 3.5. 

For an isotropic elastic body, the initial Helmholtz free energy (HFE) potential $\psi _ { 0 } ( \epsilon )$ is given by 

$$
\psi_ {0} (\boldsymbol {\epsilon}) = \frac {1}{2} \boldsymbol {\epsilon}: \mathbb {E} _ {0}: \boldsymbol {\epsilon} = \frac {1}{2} \lambda_ {0} \mathrm{tr} ^ {2} (\boldsymbol {\epsilon}) + \mu_ {0} \boldsymbol {\epsilon}: \boldsymbol {\epsilon} = \frac {1}{2} \bar {\boldsymbol {\sigma}}: \mathbb {C} _ {0}: \bar {\boldsymbol {\sigma}} = \psi_ {0} (\bar {\boldsymbol {\sigma}})\tag{62}
$$

where the linear elasticity tensor $\mathbb { E } _ { 0 } = 2 \mu _ { 0 } \mathbb { I } + \lambda _ { 0 } \pmb { \mathscr { 1 } } \otimes \pmb { \mathscr { 1 } }$ is defined in terms of the Lamé constants $\lambda _ { 0 }$ and $\mu _ { 0 }$ , with I and 1 being the fourth- and second-order identity tensors, respectively; $\mathbb { C } _ { 0 } : = \mathbb { E } _ { 0 } ^ { - 1 }$ denotes the fourth-order compliance tensor; $\bar { \pmb { \sigma } } = \mathbb { E } _ { 0 } : \pmb { \epsilon }$ represents the effective stress tensor. 

In order to prevent cracking in regions under compression, a tension/compression split of the initial HFE potential $\psi _ { 0 } ( \epsilon )$ is usually considered i.e., 

$$
\psi_ {0} (\pmb {\epsilon}) = \psi_ {0} ^ {+} (\pmb {\epsilon}) + \psi_ {0} ^ {-} (\pmb {\epsilon})\tag{63}
$$

such that 

$$
\psi (\pmb {\epsilon}, \phi) = g (\phi) \psi_ {0} ^ {+} (\pmb {\epsilon}) + \psi_ {0} ^ {-} (\pmb {\epsilon})\tag{64}
$$

where the energetic degradation function $g ( \phi )$ is only applied to the tension part $\psi _ { 0 } ^ { + }$ of the initial strain elastic energy. 

The resulting stress field and evolution law, given in Equation (29) and Equation (43), respectively, of the crack phase-field read 

$$
\pmb {\sigma} = \frac {\partial \psi}{\partial \pmb {\epsilon}} = g (\phi) \frac {\partial \psi_ {0} ^ {+}}{\partial \pmb {\epsilon}} + \frac {\partial \psi_ {0} ^ {-}}{\partial \pmb {\epsilon}}\tag{65a}
$$

$$
G _ {c} \delta_ {\phi} \gamma = - g ^ {\prime} (\phi) \bar {Y}, \qquad \bar {Y} = \frac {\partial \psi}{\partial g} = \psi_ {0} ^ {+}\tag{65b}
$$

From a numerical point of view the above anisotropic formulation with a tension/compression split usually renders the equilibrium equation nonlinear. Consequently, in the staggered solution scheme one has to solve for a system of nonlinear equations for the displacement sub-problem. Note that with this strain energy split, the Γ-convergence towards Griffith’s theory remains to be proven. 

In the literature there are different options for $\psi _ { 0 } ^ { + } ( \epsilon )$ and $\psi _ { 0 } ^ { - } ( \epsilon )$ . Here, we only present some commonly used alternatives. We refer to Li et al. [2016] for a discussion on the performance of some common strain energy split models and Steinke and Kaliske [2018] for a directional split where the crack oritentation is considered for the first time in a PFM. 

## 3.4.1 Isotropic model with no split

In the standard PFM [Bourdin et al., 2000] no split is considered and the free energy density function $\psi ( \epsilon , \phi )$ is simply expressed as 

$$
\psi^ {+} (\boldsymbol {\epsilon}) = \psi (\boldsymbol {\epsilon}), \quad \psi^ {-} (\boldsymbol {\epsilon}) = 0 \quad \Longrightarrow \quad \psi (\boldsymbol {\epsilon}, \phi) = g (\phi) \psi_ {0} (\boldsymbol {\epsilon})\tag{66}
$$

This choice results in the following stress field, where $\bar { \pmb { \sigma } }$ denotes the effective stress 

$$
\pmb {\sigma} = \frac {\partial \psi}{\partial \pmb {\epsilon}} = g (\phi) \bar {\pmb {\sigma}}, \qquad \bar {\pmb {\sigma}} = \frac {\partial \psi_ {0}}{\partial \pmb {\epsilon}} = \mathbb {E} _ {0}: \pmb {\epsilon}\tag{67a}
$$

and an isotropic evolution law of the crack phase-field 

$$
G _ {c} \delta_ {\phi} \gamma = - g ^ {\prime} (\phi) \bar {Y}, \qquad \bar {Y} = \frac {\partial \psi}{\partial g} = \psi_ {0} (\pmb {\epsilon})\tag{67b}
$$

The above standard PFM cannot discriminate between the asymmetric tensile and compressive behaviour. In particular, it predicts identical cracking in regions under compression, which is not realistic for brittle and quasi-brittle fracture (cf. Fig. 43 in Section 7.1.1 for an illustration). Furthermore, it cannot be used in the case of cyclic loading since it does not account for the unilateral effect [Mazars et al., 1990, Reinhardt and Cornelissen, 1984] caused by microcracks closure-reopening (MCR). Beside, existing cracks would exhibit interpenetration of the crack surfaces under compressive loading. 

## 3.4.2 Anisotropic model of Lancioni and Royer-Carfagni [2009]

In Lancioni and Royer-Carfagni [2009] shear fracture is considered. That is, only the deviatoric part of the initial HFE potential is affected by the degradation function while the volumetric part is unaffected i.e., 

$$
\psi_ {0} ^ {+} (\pmb {\epsilon}) = \mu_ {0} \pmb {\epsilon} _ {D}: \pmb {\epsilon} _ {D}, \qquad \psi_ {0} ^ {-} (\pmb {\epsilon}) = \frac {1}{2} K _ {0} \mathbf {t r} ^ {2} (\pmb {\epsilon})\tag{68}
$$

where $K _ { 0 } = \lambda _ { 0 } + 2 \mu _ { 0 } / 3$ denotes the bulk modulus; the strain tensor  is decomposed in a volumetric part and a deviatoric one 

$$
\boldsymbol {\epsilon} = \boldsymbol {\epsilon} _ {V} + \boldsymbol {\epsilon} _ {D}; \quad \boldsymbol {\epsilon} _ {V} = \frac {1}{3} \operatorname{tr} (\boldsymbol {\epsilon}) \boldsymbol {1}, \quad \boldsymbol {\epsilon} _ {D} = \boldsymbol {\epsilon} - \frac {1}{3} \operatorname{tr} (\boldsymbol {\epsilon}) \boldsymbol {1}\tag{69}
$$

The resulting stress field in Equation (65a) becomes 

$$
\pmb {\sigma} = g (\phi) 2 \mu_ {0} \pmb {\epsilon} _ {D} + K _ {0} \mathbf {t r} (\pmb {\epsilon}) \pmb {1}\tag{70}
$$

The PFM with the above split was used to analyse the failure of some structural members of the French Panthéon, one of the most famous historical monuments in Paris. 

## 3.4.3 Anisotropic model of Amor et al. [2009]

Amor et al. [2009] proposed the following positive/negative parts of the initial HFE potential 

$$
\psi_ {0} ^ {+} (\pmb {\epsilon}) = \frac {1}{2} K _ {0} \langle \mathbf {t r} (\pmb {\epsilon}) \rangle^ {2} + \mu_ {0} \pmb {\epsilon} _ {D}: \pmb {\epsilon} _ {D}, \qquad \psi_ {0} ^ {-} (\pmb {\epsilon}) = \frac {1}{2} K _ {0} \langle - \mathbf {t r} (\pmb {\epsilon}) \rangle^ {2}\tag{71}
$$

such that 

$$
\boldsymbol {\sigma} = g (\phi) \left[ K _ {0} \langle \operatorname{tr} (\epsilon) \rangle \mathbf {1} + 2 \mu_ {0} \epsilon_ {D} \right] - K _ {0} \langle - \operatorname{tr} (\epsilon) \rangle \mathbf {1}\tag{72}
$$

where the McAuley brackets are defined as $\langle a \rangle : = \operatorname* { m a x } \{ a , 0 \}$ . The resulting PFM partially limits but not completely prevents the creation of cracks under compression. It is the deviatoric part of the bulk energy that contributes to the crack driving force when $\mathbf { t r } ( \epsilon ) < 0$ 

## 3.4.4 Anisotropic model of Miehe et al. [2010b]

Miehe et al. [2010b] considered an anisotropic PFM with a spectral decomposition of the strain tensor <sup>12</sup> 

$$
\boldsymbol {\epsilon} = \sum_ {n = 1} ^ {3} \epsilon_ {n} \boldsymbol {p} _ {n} \otimes \boldsymbol {p} _ {n} = \boldsymbol {\epsilon} ^ {+} + \boldsymbol {\epsilon} ^ {-}\tag{73}
$$

for the positive/negative components [Ortiz, 1985, Wu and Xu, 2013] 

$$
\boldsymbol {\epsilon} ^ {+} := \sum_ {n = 1} ^ {3} \left\langle \epsilon_ {n} \right\rangle \boldsymbol {p} _ {n} \otimes \boldsymbol {p} _ {n}, \quad \boldsymbol {\epsilon} ^ {-} = \sum_ {n = 1} ^ {3} - \left\langle - \epsilon_ {n} \right\rangle \boldsymbol {p} _ {n} \otimes \boldsymbol {p} _ {n}\tag{74}
$$

where $\epsilon _ { n }$ and ${ \pmb p } _ { n } \ ( n = 1 , 2 , 3 )$ denote the principal strains and eigenvectors of the eigenvalues of $\epsilon ,$ respectively; $\otimes$ is the dyadic product of two vectors. Note that the above tensile/compressive strain tensors are orthogonal in the Frebrius norm [Wu and Cervera, 2018] $\mathrm { i . e . , } \epsilon ^ { + } : \epsilon ^ { - } = 0$ 

Accordingly, the positive/negative parts of the initial HFE potential are expressed as 

$$
\psi_ {0} ^ {\pm} (\boldsymbol {\epsilon}) := \frac {1}{2} \lambda_ {0} \langle \pm \mathrm{tr} (\boldsymbol {\epsilon}) \rangle^ {2} + \mu_ {0} \boldsymbol {\epsilon} ^ {\pm}: \boldsymbol {\epsilon} ^ {\pm}\tag{75}
$$

It then follows that 

$$
\boldsymbol {\sigma} = g (\phi) \left[ \lambda_ {0} \langle \operatorname{tr} (\epsilon) \rangle \mathbf {1} + 2 \mu_ {0} \epsilon^ {+} \right] - \lambda_ {0} \langle - \operatorname{tr} (\epsilon) \rangle \mathbf {1} + 2 \mu_ {0} \epsilon^ {-}\tag{76}
$$

The resulting PFM can completely suppress the creation of cracks under compression. 

## 3.4.5 Anisotropic model of Wu and Nguyen [2018]

Similarly to the strain tensor , a positive/negative decomposition of the effective stress $\bar { \pmb { \sigma } }$ can also be considered i.e., 

$$
\bar {\boldsymbol {\sigma}} = \bar {\boldsymbol {\sigma}} ^ {+} + \bar {\boldsymbol {\sigma}} ^ {-}, \quad \bar {\boldsymbol {\sigma}} ^ {\pm} = \sum_ {n = 1} ^ {3} \bar {\sigma} _ {n} ^ {\pm} \boldsymbol {p} _ {n} \otimes \boldsymbol {p} _ {n}\tag{77}
$$

where bar $\sigma _ { n } ^ { \pm }$ are the principal values of the positive/negative effective stresses. Note that the eigenvectors ${ \pmb p } _ { n }$ of the effective stress coincide with those of the strain. Though other alternatives exist [Carol and Willam, 1996, Wu and Xu, 2013], Wu and Cervera [2018] proposed the following eigenvalues $\bar { \sigma } _ { n } ^ { \pm }$ 

$$
\bar {\sigma} _ {1} ^ {+} = \left\langle \bar {\sigma} _ {1} \right\rangle , \quad \bar {\sigma} _ {2} ^ {+} = \left\langle \max \left(\bar {\sigma} _ {2}, \tilde {\nu} _ {0} \bar {\sigma} _ {1}\right) \right\rangle\tag{78a}
$$

$$
\bar {\sigma} _ {3} ^ {+} = \Big \langle \max \big [ \max \big (\bar {\sigma} _ {3}, \nu_ {0} \big (\bar {\sigma} _ {1} + \bar {\sigma} _ {2} \big) \big), \tilde {\nu} _ {0} \bar {\sigma} _ {1} \big ] \Big \rangle\tag{78b}
$$

such that the following orthogonal condition in energy norm holds 

$$
\bar {\boldsymbol {\sigma}} ^ {+}: \mathbb {C} _ {0}: \bar {\boldsymbol {\sigma}} ^ {-} = 0\tag{79}
$$

for $\tilde { \nu } _ { 0 } = \nu _ { 0 } / ( 1 - \nu _ { 0 } )$ in 3-D and plane strain cases, and $\tilde { \nu } _ { 0 } = \nu _ { 0 }$ in the plane stress condition $( \bar { \sigma } _ { 2 } = 0 )$ 

With the above split, the positive/negative parts of the initial HFE potentials $\psi _ { 0 } ^ { \pm }$ are expressed as 

$$
\psi_ {0} ^ {\pm} (\bar {\pmb {\sigma}}) = \frac {1}{2} \bar {\pmb {\sigma}} ^ {\pm}: \mathbb {C} _ {0}: \bar {\pmb {\sigma}} ^ {\pm}\tag{80}
$$

Note that the above decomposition minimises the positive part $\psi _ { 0 } ^ { + } ( \bar { \pmb { \sigma } } )$ , which is consistent with the variational interpretation of the PFM. Accordingly, the stress field is given by (see Appendix B.3 for the details) 

$$
\frac {\partial \psi_ {0} ^ {\pm}}{\partial \pmb {\epsilon}} = \mathbb {E} _ {0}: \frac {\partial \psi_ {0} ^ {\pm}}{\partial \bar {\pmb {\sigma}}} = \bar {\pmb {\sigma}} ^ {\pm} \qquad \Longrightarrow \qquad \pmb {\sigma} = g (\phi) \bar {\pmb {\sigma}} ^ {+} + \bar {\pmb {\sigma}} ^ {-}\tag{81}
$$

This anisotropic PFM was proposed in Wu and Nguyen [2018] for both brittle and quasi-brittle fracture. 

## 3.5 Energetic degradation function

In PF models, the energetic degradation function, $g ( \phi )$ , plays an important role since it links the crack phase-field and the mechanical fields. Precisely it determines how the stored energy functional responds to changes in the crack phase-field. 

The energetic degradation function has to satisfy the following conditions: 

$g ( 0 ) = 1$ (intact state) and $g ( 1 ) = 0$ (completely broken state); 

$g ^ { \prime } ( \phi ) = \mathrm { d } g / \mathrm { d } \phi < 0 \mathrm { i . e . , } g ( \phi )$ is a monotonically decreasing function; 

$g ^ { \prime } ( 1 ) = 0$ 

The third property comes from the crack driving force term $- g ^ { \prime } ( \phi ) \psi _ { 0 } ^ { + } ( \epsilon )$ in the evolution law, cf. Equation (65b), guaranteeing that the localisation band does not grow orthogonally as usually observed in the classical nonlocal/gradient-enhanced damage models [Geers et al., 1998]. 

Common choices for the degradation function $g ( \phi )$ are given in Table 3. The first one – the quadratic polynomial – was introduced in Bourdin et al. [2000] in the context of elliptic Ambrosio and Tortorelli [1990] regularisation and utilised by many others; the second cubic polynomial was introduced in Karma et al. [2001]; the third cubic polynomial with an extra parameter s was proposed by Borden et al. 

[2016] to have an elastic domain before crack initiation<sup>13</sup>; the fourth quartic polynomial was presented in Kuhn et al. [2015]. Plots of these functions are given in Fig. 15. Though the last three degradation functions of rational-type can also be applied to brittle fracture, they were proposed in the literature mainly for cohesive fracture and quasi-brittle failure. 

<table><tr><td>g(φ)</td><td>authors</td></tr><tr><td>(1-φ)2</td><td>Bourdin et al. [2000]</td></tr><tr><td>3(1-φ)2-2(1-φ)3</td><td>Karma et al. [2001]</td></tr><tr><td>(3-s)(1-φ)2-(2-s)(1-φ)3</td><td>Borden et al. [2016]</td></tr><tr><td>4(1-φ)3-3(1-φ)4</td><td>Kuhn et al. [2015]</td></tr><tr><td>(1-φ)2/(1-φ)2+Q(φ), Q(φ)=φ+pφ2</td><td>Lorentz et al. [2012, 2011]</td></tr><tr><td>(1-φ)2/1+(k-1)Q(φ), Q(φ)=1-(1-φ)2</td><td>Alessi et al. [2015]</td></tr><tr><td>(1-φ)p/(1-φ)p+Q(φ), Q(φ)=a1φ+a1a2φ2+a1a2a3φ3</td><td>Wu [2017]</td></tr></table>


Table 3: Commonly selected energetic degradation functions $g ( \phi )$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/742cea3182ac8221be64a39fdde829ce0c0d7f1f316a7c2d24b692d793074a27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7e5a1a2727ebaa3815b04eb61b47c662ead1830b5486f7289c3aca9314c56d3a.jpg)



Figure 15: Plots of some common energetic/stress degradation functions and their first derivatives.


Analysis of these functions was reported in Pham et al. [2011], Borden et al. [2012], Kuhn et al. [2015], Wu [2017]. In Section 4 we will investigate the influence of various energetic degradation functions for the particular case of a softening bar under uniaxial traction. Note that Table 3 is by no means exhaustive, but presents the most commonly used degradation functions; we refer to Sargado et al. [2018], Wilson et al. [2013] for other functions. 

Remark 16. In most implementations, a small positive numerical parameter k is introduced in the degradation function e.g., $g ( \phi ) = ( 1 - \phi ) ^ { 2 } + k$ in order to guarantee the well-conditioning of the system of equations. However, this is not necessarily mandatory and we have used $k = 0$ for all static and dynamic simulations presented later. Borden et al. [2012] also confirmed this. 

## 3.6 Hybrid formulations

All the PFMs we have discussed are variationally consistent. More specifically, the stress field $\sigma$ and the evolution law of the crack phase-field $\phi$ are derived from a single stored energy functional i.e., $\psi ( \epsilon , \phi ) = g ( \phi ) \psi _ { 0 } ( \epsilon )$ for the isotropic formulation with no split and $\psi ( \epsilon , \phi ) = g ( \phi ) \psi _ { 0 } ^ { + } + \psi _ { 0 } ^ { - }$ for the anisotropic formulation with tension/compression split, respectively. However, for the former the asymmetric tensile/compressive behaviour cannot be discriminated, while for the later the equilibrium equation becomes nonlinear and rendering the displacement sub-problem more computationally inefficient. 

To overcome the above issue, we can use the so-called hybrid PFMs [Ambati et al., 2015a, Wu, 2017, 2018a,b, Wu and Nguyen, 2018] 

$$
\pmb {\sigma} = \frac {\partial \psi}{\partial \pmb {\epsilon}} = g (\phi) \bar {\pmb {\sigma}}, \qquad \bar {\pmb {\sigma}} = \frac {\partial \psi_ {0}}{\partial \pmb {\epsilon}} = \mathbb {E} _ {0}: \pmb {\epsilon}\tag{82a}
$$

$$
G _ {c} \delta_ {\phi} \gamma = - g ^ {\prime} (\phi) \bar {Y}, \quad \bar {Y} = \frac {\partial \bar {\psi}}{\partial g} = \bar {\psi} _ {0} (\epsilon)\tag{82b}
$$

where distinct energy functions, $\psi ( \epsilon , \phi )$ and $\bar { \psi } ( \epsilon , \phi )$ , respectively, are postulated for the stress field (67a) and the crack phase evolution law (67b) 

$$
\psi (\epsilon , \phi) = g (\phi) \psi_ {0} (\epsilon), \qquad \bar {\psi} (\epsilon , \phi) = g (\phi) \bar {\psi} _ {0} (\epsilon)\tag{83}
$$

For the case $\bar { \psi } _ { 0 } = \psi _ { 0 } ( \epsilon )$ , the classical isotropic PFM given in Section 3.4.1 is recovered; otherwise, the resulting hybrid model is no longer variationally consistent since the stress field and the crack phase-field evolution law correspond to distinct energy functionals. However, such a variational crime does not violate the second law of thermodynamics; see Wu [2018a]. Moreover, the asymmetric tensile/compressive behaviour can be captured with no loss of computational efficiency: in a staggered solution scheme, with a fixed phase-field $\bar { \phi } ,$ the stress is simply $\pmb { \sigma } = g ( \bar { \phi } ) \mathbb { E } _ { 0 } : \pmb { \epsilon }$ , and thus the sub-displacement problem is a linear problem. 

In the literature, the following energetically inconsistent effective driving forces have been considered i.e., [Ambati et al., 2015a, Wu, 2017, 2018a,b, Wu and Nguyen, 2018] 

$$
\bar {Y} = \bar {\psi} _ {0} (\epsilon) = \left\{ \begin{array}{l l} \psi_ {0} ^ {+} (\epsilon) & \text {Ambati et al. [2015a]} \\ \frac {1}{2 E _ {0}} \bar {\sigma} _ {\mathrm{eq}} ^ {2} & \text {Wu [2017]} \\ \psi_ {0} ^ {+} (\bar {\sigma} ^ {+}) & \text {Wu and Nguyen [2018]} \end{array} \right.\tag{84}
$$

In Ambati et al. [2015a], the Miehe et al. [2010b] tension/compression split was adopted to define the positive initial free energy density $\psi _ { 0 }$ . For brittle fracture, Ambati et al. [2015a] compared the hybrid PFM with the standard anisotropic one for some 2-D fracture tests. It is found that the crack patterns almost coincide but the global load-displacement curves were slightly different. In Wu [2017], the so-called equivalent effective stress $\bar { \sigma } _ { \mathrm { e q } }$ is defined as 

$$
\bar {\sigma} _ {\mathrm{eq}} = \frac {1}{1 + \beta_ {c}} \left(\beta_ {c} \langle \bar {\sigma} _ {1} \rangle + \sqrt {3 \bar {J} _ {2}}\right)\tag{85}
$$

with $\beta _ { c } : = f _ { c } / f _ { t } - 1$ , related to the ratio of the uniaxial compressive strength $f _ { c }$ and the uniaxial tensile strength $f _ { t } ; \bar { \sigma } _ { 1 }$ denotes the largest principal value of the effective stresses and ${ \bar { J } } _ { 2 }$ is the second invariant of the deviatoric effective stress tensor. Usually the Rankine based equivalent effective stress $\bar { \sigma } _ { \mathrm { e q } } = \langle \bar { \sigma } _ { 1 } \rangle$ resulting from $\beta _ { c } \to \infty$ is employed. In Wu and Nguyen [2018], the tension/compression split proposed by Wu and Cervera [2018] was adopted to define the effective driving force, and both brittle and cohesive fractures were considered. The conclusion drawn by Ambati et al. [2015a] for brittle fracture was confirmed, but some discrepancies in both the crack pattern and global response were observed for quasi-brittle mixed-mode failure; see Wu and Nguyen [2018] for more details and the recent work of 

Jeong et al. [2018] where the anisotropic model is shown to suffer from stress-locking (i.e., completely damaged material with non-zero stresses) and the hybrid ones performs well for fracture analyses of composite materials. 

For the standard PFM with $\alpha = \phi ^ { 2 }$ , the evolution law in Equation (65b) can be further modified as 

$$
\phi - l _ {0} ^ {2} \Delta \phi = - g ^ {\prime} (\phi) \tilde {Y}\tag{86}
$$

where $\tilde { Y }$ is the normalised effective driving force. This form allows introducing many more complex crack driving forces though they are most often rather ad hoc e.g., 

$$
\tilde {Y} = \left\{ \begin{array}{l} \frac {\psi_ {0 I} ^ {+} (\boldsymbol {\epsilon})}{G _ {I c} / l _ {0}} + \frac {\psi_ {0 I I} ^ {+} (\boldsymbol {\epsilon})}{G _ {I I c} / l _ {0}} \\ \zeta \Big \langle \frac {1}{\sigma_ {c} ^ {2}} \langle \bar {\sigma} _ {1} \rangle^ {2} - 1 \Big \rangle \\ \zeta \Big \langle \frac {1}{\sigma_ {c} ^ {2}} \sum_ {n = 1} ^ {3} \langle \bar {\sigma} _ {n} \rangle^ {2} - 1 \Big \rangle \end{array} \right.
$$

Zhang et al. [2017a] 

Miehe et al. [2015b] 

(87) 

Miehe et al. [2015b] 

The first expression incorporates the critical energy release rates $G _ { I c }$ and $G _ { I I c }$ for mode I and mode II, respectively; the corresponding positive energy functions $\psi _ { 0 I } ^ { + } ( \epsilon )$ and $\psi _ { 0 I I } ^ { + } ( \epsilon )$ are defined as [Zhang et al., 2017a] 

$$
\psi_ {0 I} ^ {+} (\pmb {\epsilon}) := \frac {1}{2} \lambda_ {0} \langle \mathbf {t r} (\pmb {\epsilon}) \rangle^ {2}, \quad \psi_ {0 I I} ^ {+} (\pmb {\epsilon}) := \mu_ {0} \pmb {\epsilon} ^ {+}: \pmb {\epsilon} ^ {+}\tag{88}
$$

even though it is apparent that $\scriptstyle \frac { 1 } { 2 } \lambda _ { 0 } \langle \mathrm { t r } ( \epsilon ) \rangle ^ { 2 }$ is the volumetric strain energy rather than the strain energy due to pure tensile deformations. Zhang et al. [2017a] used this crack driving force to model compressive cracking of rock-like materials (cf. Section 7.1.5 for some simulations of cracking in rocks). The second equation is the well-known Rankine criterion and the third one is a rounded counterpart in terms of the principal effective stresses $\bar { \sigma } _ { n }$ ; the parameter $\zeta > 0$ was introduced to control the growth of the crack phase-field in the post-critical regimes. 

Remark 17. Note that the evolution law given in Equation (86) resembles the screened Poisson equation in physics. It is this reason that the phase-field model presented in Areias et al. [2016a] was called so. It is also very similar to the inhomogeneous Helmholtz equation. 

## 3.7 Governing equations of PF models in weak form

In accordance with the weighted residual method, the governing equations and boundary conditions summarised in Equations (35) and (36) can be rewritten as the following weak form: Find $\pmb { u } \in \mathcal { U } _ { u }$ and $\phi \in \mathcal { U } _ { \phi }$ such that 

$$
\left\{ \begin{array}{l l} \int_ {\Omega} \boldsymbol {\sigma}: \nabla^ {s} \delta \boldsymbol {u}   \mathrm{d} V + \int_ {\Omega} \rho \ddot {\boldsymbol {u}} \cdot \delta \boldsymbol {u}   \mathrm{d} V = \delta \mathcal {P} & \forall \delta \boldsymbol {u} \in \mathcal {V} _ {u} \\ \int_ {\mathcal {B}} \left[ g ^ {\prime} (\phi) \bar {Y}   \delta \phi + G _ {c}   \delta \gamma \right]   \mathrm{d} V \geq 0 & \forall \delta \phi \in \mathcal {V} _ {\phi} \end{array} \right.\tag{89}
$$

for the standard virtual power $\delta \mathcal { P }$ of external (body and surface) forces. For the generic crack surface density function in Equation (58), the variation of $\delta \gamma$ is expressed as 

$$
\delta \gamma = \frac {1}{c _ {0}} \Big [ \frac {1}{l _ {0}} \alpha^ {\prime} (\phi) \delta \phi + 2 l _ {0} \nabla \phi \cdot \nabla \delta \phi \Big ]\tag{90}
$$

We have also introduced in Equation (89) the following test and trial spaces 

$$
\mathcal {U} _ {u} := \left\{\boldsymbol {u} | \boldsymbol {u} (\boldsymbol {x}) = \boldsymbol {u} ^ {*} \forall \boldsymbol {x} \in \partial \Omega_ {u} \right\}, \quad \mathcal {V} _ {u} := \left\{\delta \boldsymbol {u} | \delta \boldsymbol {u} (\boldsymbol {x}) = \boldsymbol {0} \forall \boldsymbol {x} \in \partial \Omega_ {u} \right\}\tag{91a}
$$

$$
\mathcal {U} _ {\phi} := \Big \{\phi \big | \phi (\boldsymbol {x}) \in [ 0, 1 ], \dot {\phi} (\boldsymbol {x}) \geq 0 \forall \boldsymbol {x} \in \mathcal {B} \Big \}, \quad \mathcal {V} _ {\phi} := \Big \{\delta \phi \big | \delta \phi (\boldsymbol {x}) \geq 0 \forall \boldsymbol {x} \in \mathcal {B} \Big \}\tag{91b}
$$

Note that pre-defined cracks $s$ can be accounted for either indirectly by the Dirichlet condition $\phi ( { \pmb x } ) = 1$ for $\pmb { x } \in \mathcal { S }$ or directly by mesh discretisation. In order to prevent cracking in some regions, the Dirichlet boundary conditions/constraints $\phi ( { \pmb x } ) = 0$ can also be enforced on selected nodes. Alternatively, a high value for $G _ { c }$ can be used for such regions. 

Equation $( 8 9 ) _ { 2 }$ is a variational inequality on the damage field with unilateral constraint, in which the boundedness $\phi ( \pmb { x } ) \in [ 0 , 1 ]$ and irreversibility condition $\dot { \phi } ( { \pmb x } ) \ge 0$ have to be dealt with carefully. In the literature, there exists different techniques to deal with $\dot { \phi } \geq 0$ 

In Bourdin et al. [2000] the authors only enforced the irreversibility condition when the crack phase-field is close to one: 

$$
\phi (\pmb {x}, t > t _ {0}) = 1 \quad \mathrm{if} \phi (\pmb {x}, t _ {0}) \approx 1\tag{92}
$$

which is not a satisfactory solution for cohesive fracture or quasi-brittle failure. 

In order to prevent cracks from healing when the source term $\bar { Y } ~ = ~ \psi _ { 0 } ^ { + }$ decreases, Miehe et al. [2010b] proposed replacing the effective driving force $\bar { Y }$ by a local history field $\mathcal { H } ( { \boldsymbol { \mathbf { \mathit { x } } } } , t )$ 

$$
\bar {Y} = \mathcal {H} (\boldsymbol {x}, t) := \max _ {0 \leq t ^ {\prime} \leq t} \psi_ {0} ^ {+} (\boldsymbol {\epsilon} (\boldsymbol {x}, t ^ {\prime}))\tag{93}
$$

Note that in continuum damage models a similar strategy has already been a standard scheme in defining the damage threshold since the work of Simó and Ju [1987]. This strategy automatically deals with the irreversibility conditions $\dot { \phi } ( { \pmb x } ) \geq 0$ . For a PFM with the geometric crack function $\alpha ( \phi ) = \phi ^ { 2 }$ in which the boundedness $\phi ( \pmb { x } ) \in [ 0 , 1 ]$ is intrinsically guaranteed, Equation $( 8 9 ) _ { 2 }$ becomes a variational equality. It also allows to implicitly describe initial cracks independently of the finite element mesh [Borden et al., 2012, Klinsmann et al., 2015] (and also see Section 6.5). 

However, though this strategy has been widely adopted in the literature, it does not apply to general PFMs since the boundedness $\phi ( \pmb { x } ) \in [ 0 , 1 ]$ cannot be guaranteed for non-quadratic geometric crack functions $\alpha ( \phi ) \neq \phi ^ { 2 }$ 

In Amor et al. [2009], an exact enforcement of the irreversibility condition was achieved by considering the phase-field evolution equation as a bound-constrained optimisation problem i.e., 

$$
(\boldsymbol {u}; \phi) = \operatorname{Arg} \left\{\min _ {\hat {\boldsymbol {u}} \in \mathcal {U} _ {u}, \hat {\phi} \in \mathcal {U} _ {\phi}} \mathscr {E} (\hat {\boldsymbol {u}}; \hat {\phi}) \right\}\tag{94}
$$

Practically, Equation (94) can be solved using either the primal-dual active set strategy [Heister et al., 2015] or the bound-constrained quadratic optimisation solver (included in Matlab Optimisation Toolbox and PETSc toolkit). This strategy was later adopted in Li et al. [2016] and further enhanced by Farrell and Maurini [2017]. 

For the hybrid PFM which is variationally inconsistent, the minimisation problem (94) does not hold for both unknown fields $( { \pmb u } ; \phi )$ . To address this issue, Wu [2017, 2018a,b] considered the following bound-constrained problem 

$$
\left\{ \begin{array}{l l} \boldsymbol {u} = \operatorname{Arg} \Big \{\min _ {\hat {\boldsymbol {u}} \in \mathcal {U} _ {u}} \mathcal {E} (\hat {\boldsymbol {u}}; \hat {\phi}) \Big \} & \quad \forall \hat {\phi} \in \mathcal {U} _ {\phi} \\ \phi = \operatorname{Arg} \Big \{\min _ {\hat {\phi} \in \mathcal {U} _ {\phi}} \bar {\mathcal {E}} (\hat {\boldsymbol {u}}; \hat {\phi}) \Big \} & \quad \forall \hat {\boldsymbol {u}} \in \mathcal {U} _ {u} \end{array} \right.\tag{95a}
$$

where the modified energy functional $\bar { \mathcal { E } } ( \boldsymbol { u } ; \boldsymbol { \phi } )$ is defined as 

$$
\bar {\mathcal {E}} (\boldsymbol {u}; \phi) := \int_ {\Omega} \bar {\psi} (\boldsymbol {\epsilon} (\boldsymbol {u}), \phi) \mathrm{d} V + \int_ {\mathcal {B}} G _ {c} \gamma (\phi) \mathrm{d} V - \int_ {\Omega} \boldsymbol {b} ^ {*} \cdot \boldsymbol {u} \mathrm{d} V - \int_ {\partial \Omega_ {t}} \boldsymbol {t} ^ {*} \cdot \boldsymbol {u} \mathrm{d} A\tag{95b}
$$

For a variationally consistent PFM with $\bar { \mathcal { E } } ( \mathbf { u } ; \boldsymbol { \phi } ) = \mathcal { E } ( \mathbf { u } ; \boldsymbol { \phi } )$ , the bound-constrained minimisation problem (94) is recovered. 

Remark 18. Variational consistency usually implies an energy minimization principle which gives us a prototype model. However, for brittle and quasi-brittle solids with asymmetric tension/compression cracking behavior, the variational formulation is not rich enough to be able to capture experimental results. Therefore, the variationally consistent prototype model is modified resulting in a variationally inconsistent model which is able to reproduce many crack phenomena experimentally observed. 

## 3.8 Relation with nonlocal damage models

Even though PFMs were developed based on the variational approach to fracture, it is rather similar to some nonlocal damage theories. This section presents a discussion on the similarity and differences between PFMs and the gradient-enhanced damage model proposed by Peerlings et al. [1996a] and the gradient-damage models (GDM) developed by Frémond and Nedjar [1996]. The conclusions are (i) PFM is entirely different from GED [Mandal et al., 2019] and (ii) PFM is very similar to GDM (final equations are the same) if the length scale $l _ { 0 }$ in PFM is considered as a material property without ad hoc introduction of the so-called nonlocal energy residual. 

## 3.8.1 Relation with gradient-enhanced damage (GED) models

Let us first discuss the similarity and differences between the standard PFM (i.e., the one with quadratic geometric function $\alpha ( \phi ) = \phi ^ { 2 } )$ and Gradient-Enhanced Damage Model (GED) model developed by Peerlings et al. [1996a]. A more comprehensive elaboration on this topic was given in de Borst and Verhoosel [2016], Steinke et al. [2016b], Mandal et al. [2019]. Regarding the isotropic formulation, the main equations for these two models are summarised in Table 4. 

<table><tr><td></td><td>Gradient-enhanced damage model</td><td>Phase-field fracture model</td></tr><tr><td>stress-strain relation</td><td><eq>\boldsymbol{\sigma} = (1 - \phi)\mathbb{E}_{0} : \boldsymbol{\epsilon}; \quad \phi = h(\bar{\epsilon}_{\text{eq}})</eq></td><td><eq>\boldsymbol{\sigma} = g(\phi)\mathbb{E}_{0} : \boldsymbol{\epsilon}</eq></td></tr><tr><td>extra PDE</td><td><eq>\bar{\epsilon}_{\text{eq}} - c_{0}\Delta\bar{\epsilon}_{\text{eq}} = \epsilon_{\text{eq}}(\boldsymbol{\epsilon})</eq></td><td><eq>\phi - l_{0}^{2}\Delta\phi = -g&#x27;(\phi)\bar{Y}l_{0}/G_{c}</eq></td></tr><tr><td>boundary conditions</td><td><eq>\nabla\bar{\epsilon}_{\text{eq}} \cdot \boldsymbol{n} = 0</eq></td><td><eq>\nabla\phi \cdot \boldsymbol{n} = 0</eq></td></tr></table>

Table 4: Main equations of the isotropic gradient-enhanced damage (GED) and the standard PFMs. The local equivalent strain, a scalar measure of the strain tensor, is denoted by $\epsilon _ { \mathrm { { e q } } }$ , its nonlocal counterpart is designated by $\bar { \epsilon } _ { \mathrm { e q } }$ on which the damage variable $\phi$ depends. 

Based on this table, the following comments can be made: 

In the GED model, the Laplacian operator $\Delta ( \cdot )$ is applied to the damage driving force $\mathrm { i . e . , }$ the non-local equivalent strain $\bar { \epsilon } _ { \mathrm { e q } }$ that drives damage evolution, rather than to the damage $\phi$ itself as in the PFM. The involved diffusion terms contribute differently to the regularisation of the local damage model. 

The evolution laws for the non-local equivalent strain $\bar { \epsilon } _ { \mathrm { e q } }$ and the phase-field $\phi$ are very similar except the right hand side driving force. The major difference is that in the PFM, the crack driving force vanishes for a fully softened crack i $. . . , \phi = 1$ . Comparatively, this is not the case for the GED model, which results in damage widening [Geers et al., 1998]; 

In the GED model, the softening curve experimentally obtained can be straightforwardly incorporated into the model via $\phi = h ( \bar { \epsilon } _ { \mathrm { e q } } )$ where h can be a linear/exponential/hyperbolic function. Comparatively, the softening curve is implicitly determined by the adopted geometric crack function $\alpha ( \phi )$ and the energetic degradation function $g ( \phi )$ ; 

In the GED model, the damage field is always admissible i.e., $0 \leq \phi \leq 1$ and $\dot { \phi } \geq 0$ by properly selecting $h ( \bar { \epsilon } _ { \mathrm { e q } } )$ . Comparatively, in the PFM, it is more complicated to numerically ensure that $0 \leq \phi \leq 1$ and $\dot { \phi } \geq 0$ 

The natural boundary condition for $\phi$ are obtained variationally in the PFM, whereas it is somehow introduced ad hoc in the GED model; 

A crucial difference is about the role of $c _ { 0 }$ in GED and $l _ { 0 }$ in $P F M ; c _ { 0 }$ defines the size of the spatial interaction and thus the smaller $c _ { 0 }$ is the more brittle the response is. In PFM, when $l _ { 0 }$ is sufficiently small, the crack surface is accurately captured, and the dissipation is independent of $l _ { 0 } .$ , as it is defined as the product of the crack surface with $\mathit { G _ { c } } ,$ resulting in a response insensitive to $l _ { 0 }$ . The dependence of the responses on $c _ { 0 }$ makes the calibration of $c _ { 0 }$ a non-trivial task [Pereira et al., 2016], cf. Fig. 18; 

Yet another crucial difference lies in the damage profile. In PFMs, the damage profile is governed by the crack geometric function $\alpha ( d ) = \xi d + ( 1 - \xi ) d ^ { 2 }$ . For various values of ξ the resulting damage profiles are shown in Fig. 16a whereas the damage profile of GED is given in Fig. 16b which is taken from Peerlings et al. [1996b]. As can be seen, the damage distribution in space approaching a crack is of an exponential form in PFMs instead of the bell like Gaussian form observed in the GED model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/a86142206e9b211a905d0203046fe160d2c183d1828cdf5734629c8c3158c7c7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/feb97376536382bbb054b2099d7470a4b93c59bd6202283d4ca3524e8c660f6f.jpg)



(b) GED damage profiles



Figure 16: Damage profiles of phase-field and GED model [Peerlings et al., 1996b].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/701a9af64db69eafee0140004ad15e0e796575da4cce394b710323607ce28e98.jpg)



(a) Problem configuration


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/accf30bd47e0dad18820d851e451adccf21fe68659696fceb37541cdb1672524.jpg)



(b) GED


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/d860c0090fbce93c4d6053372998198c784d650881a890095fe0a9d141d5345a.jpg)



(c) PFM



Figure 17: The composite compact tension specimen: $W = 5 0$ mm and $d = 1 0$ mm. Material constants are $E _ { 0 } = 2 5 0 0$ $\mathrm { N } / \mathrm { m m ^ { 2 } }$ $\nu _ { 0 } = 0 . 2 7 7$ $G _ { c } = 0 . 5$ N/mm and $l _ { 0 } = 2$ mm. For the material constants used in the GED model, we refer to Geers et al. [1998]. GED (damage widening occurs) versus PFM (no damage widening).


In order to illustrate the second point of the above comments, we consider the experiment carried out by Geers et al. [1998]. The problem configuration and material properties are given in Fig. 17a. The numerical fracture patterns are shown in Fig. 17. It can be seen that damage widening i.e., damage grows orthogonally to the crack, happens with the GED model<sup>14</sup>. The damage band of the PFM has a constant width thanks to the crack driving force $- g ^ { \prime } ( \phi ) \bar { Y } / l _ { 0 }$ that vanishes when $\phi = 1$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/9bd9cb3bcdb1007044132dfd44a7ada051d158ebc70ebc9af79621562e52b0d4.jpg)



(a) Problem configuration


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/c55e8fa19000cd0c87a65eead6b78c72c1071c61c6bfa52aa8d2d8b6763234b6.jpg)



(b) GED


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/218afa373e4fc04a6c380cfe014f36db233b0a04fb9637b50b1a9c93781dbaa5.jpg)



(c) PF-CZM



Figure 18: The four-point bending test: GED (length scale sensitive) versus PF-CZM (length scale insensitive).


## 3.8.2 Relation with gradient damage (GD) models

Provided the incorporated length scale is treated as a material property rather than a numerical parameter [Sicsic and Marigo, 2013], the PFM resembles the Gradient Damage Model (GD) [Frémond and Nedjar, 1996, Pham et al., 2011, Marigo et al., 2016], though they were motivated from rather distinct points of view. 

The gradient-damage model dates back to Frémond and Nedjar [1996]. In this celebrated work, the classical principle of virtual power is extended to incorporate the damage gradient accounting for microscopic nonlocal interactions, resulting in both the macroscopic balance equations and the damage evolution law of gradient-type in the same format as Equation (36). Almost at the same time, Pijaudier-Cabot and Burlion [1996] proposed a similar model to analyse damage and localisation in elastic solids with voids. In this model, besides the displacement field, an extra damage field with an evolution law of gradient-type was introduced to characterise the irreversible variation of the volume fraction of material in porous con tinua. In parallel, Lorentz and Andrieux [1999], Lorentz and Godard [2011], Lorentz [2017] developed a similar gradient-damage model based on an energetic interpretation of the balance equation and of the constitutive relations for generalised standard continua. Compared to the classical local and non-local (gradient-enhanced) damage models, the free energy potential of all the aforementioned gradient-damage models depends not only on the damage field but also on its spatial gradient, invalidating the standard thermodynamics [Coleman and Gurtin, 1967]. In order to circumvent this issue, Polizzotto and Borino [1998] postulated an insulation condition on the so-called nonlocal energy residual, assuming that no long distance energy is allowed to transfer from the localisation band to exterior domains; see Liebe et al. [2001], Polizzotto [2003] for details. As an alternative regularisation to the variational approach for fracture, Pham et al. [2011] proposed a gradient-damage model resembling to the standard PFM, with the only difference of using a linear geometric crack function $\alpha ( \phi ) = \phi$ rather than a quadratic one. 

However, it seems that all the gradient damage models were developed mainly for regularising their local counterparts rather than for the modelling of fracture. This argument is seen from the fact that the fracture energy $G _ { c }$ does not enter the formulation from the beginning, but rather, it is later identified heuristically from the 1-D analytical solution. Moreover, the notion of approximating the sharp crack topology by the crack phase (or damage) field $\phi$ does not appear at all, even in the latest GD models [Pham et al., 2011, Lorentz, 2017]. For a more comprehensive discussion on this topic, readers are referred to Appendix D. 

Recently in Wu [2018b] the gap between the PF model and the GD model was eventually bridged. In this work, only the standard thermodynamics for continuum damage mechanics is adopted. The established GD model for fracture is entirely equivalent to the PFM proposed in Wu [2017]. In particular, for the isotropic model the constitutive relation is also given by Equation (67a), with the damage evolution law derived based on the following postulate of energetic equivalence between the sharp crack and the geometrically regularised one i.e., 

$$
\dot {\mathcal {D}} = \int_ {\mathcal {B}} Y \dot {\phi} \mathrm{d} V = \int_ {\mathcal {B}} \left[ - g ^ {\prime} (\phi) \bar {Y} \right] \dot {\phi} \mathrm{d} V = \int_ {\mathcal {B}} G _ {c} \dot {\gamma} \mathrm{d} V = G _ {c} \dot {\Gamma_ {l}}\tag{96a}
$$

or, equivalently, 

$$
\int_ {\mathcal {B}} \left[ g ^ {\prime} (\phi) \bar {Y} + G _ {c} \delta_ {\phi} \gamma \right] \dot {\phi} \mathrm{d} V = 0\tag{96b}
$$

As can be seen, the above damage evolution law coincides with Equation (65b) for the crack phase-field. 

## 4 1-D analytical solution

In this section the PFM is applied to a softening bar in uniaxial traction and the analytical results are addressed in details. Assume a bar $x \in [ - L , L ]$ sufficiently long such that crack evolution is not affected by boundary effects. The bar is loaded at both ends by an increasing displacement u along opposite directions. The distributed body forces are neglected for simplicity. Under these assumptions, the following equations hold 

$$
\sigma_ {, x} = 0\tag{97a}
$$

$$
\frac {G _ {c}}{c _ {0}} \Big [ \frac {1}{l _ {0}} \alpha^ {\prime} (\phi) - 2 l _ {0} \phi_ {, x x} \Big ] = - \frac {1}{2} g ^ {\prime} (\phi) E _ {0} \epsilon^ {2}\tag{97b}
$$

$$
\sigma = g (\phi) E _ {0} \epsilon\tag{97c}
$$

where the first equation represents the static equilibrium of the bar, the second is the damage evolution equation which is the 1-D version of Equation (43) with the crack driving force given by Equation (67b) and the third equation is the stress-strain relationship. As can be seen the stress field $\sigma ( x )$ is homogeneous along the bar. 

To ease the mathematical derivation, let us introduce a monotonically increasing function $\omega ( \phi )$ such that 

$$
\omega (\phi) = \frac {1}{g (\phi)} - 1 \qquad \Longrightarrow \qquad g (\phi) := \frac {1}{1 + \omega (\phi)}, \qquad g ^ {\prime} (\phi) = - g ^ {2} (\phi) \omega^ {\prime} (\phi) <   0\tag{98}
$$

with the first-order derivative $\omega ^ { \prime } ( \phi ) > 0$ . Accordingly, the evolution law (97b) and the constitutive relation (97c) yield 

$$
\sigma^ {2} \omega^ {\prime} (\phi) - A _ {0} \big [ \alpha^ {\prime} (\phi) - 2 l _ {0} ^ {2} \phi_ {, x x} \big ] = 0, \qquad A _ {0} = \frac {2 E _ {0} G _ {c}}{c _ {0} l _ {0}}\tag{99}
$$

The applied displacement u is determined by the compatibility relation $\epsilon = u _ { , x } \mathrm { i } . e .$ 

$$
u = \int_ {0} ^ {L} \epsilon \mathrm{d} x, \quad \epsilon = \frac {\sigma}{g (\phi) E _ {0}} = \frac {\sigma}{E _ {0}} [ 1 + \omega (\phi) ]\tag{100}
$$

The analytical results are first derived for generic characteristic functions $\alpha ( \phi )$ and $g ( \phi )$ (or, equivalently, $\omega ( \phi ) ,$ ), and then applied to several particular examples frequently considered in the literature. 

## 4.1 General results

Regarding the spatial distribution of the crack phase-field, the following two cases are identified: (i) homogeneous solution for which the crack phase-field and strain field are both uniform along the bar and (ii) localised solution. 

## 4.1.1 Homogeneous solution

Let us first consider the homogeneous solution for which the crack phase-field and strain field are both uniform along the bar. In this case, the identity $\phi _ { , x x } = 0$ holds and the governing equation (99) becomes 

$$
\sigma^ {2} \omega^ {\prime} (\phi) - A _ {0} \alpha^ {\prime} (\phi) = 0\tag{101}
$$

which yields 

$$
\sigma = \sqrt {A _ {0} \frac {\alpha^ {\prime} (\phi)}{\omega^ {\prime} (\phi)}}, \qquad \epsilon = \frac {1}{E _ {0}} \sqrt {- A _ {0} \frac {\alpha^ {\prime} (\phi)}{g ^ {\prime} (\phi)}}, \qquad u = \epsilon L = \frac {L}{E _ {0}} \sqrt {- A _ {0} \frac {\alpha^ {\prime} (\phi)}{g ^ {\prime} (\phi)}}\tag{102}
$$

The above results constitute the stress versus displacement (or strain) relation parametrised by the crack phase-field $\phi .$ 

For the generic geometric crack function $\alpha ( \phi ) = \xi \phi + { \bigl ( } 1 - \xi { \bigr ) } \phi ^ { 2 }$ , it follows from the damage evolution equation evaluated at $\phi = 0$ that 

PFMs with $\xi = 0 \colon \alpha ^ { \prime } ( 0 ) = \xi = 0$ . On the one hand, $g ^ { \prime } ( 0 ) < 0$ (or, equivalently, $\omega ^ { \prime } ( 0 ) > 0 )$ implies that the failure criterion is activated at the onset of the loading and the crack phase-field $\phi$ grows with no initial elastic stage. On the other hand, $g ^ { \prime } ( 0 ) = \omega ^ { \prime } ( 0 ) = 0$ means that an initial elastic stage exists. In both cases, the stress achieves its peak value $\sigma ( \phi _ { c } )$ at the strain $\epsilon ( \phi _ { c } )$ 

$$
\sigma_ {c} = \sqrt {A _ {0} \frac {\alpha^ {\prime} (\phi_ {c})}{\omega^ {\prime} (\phi_ {c})}}, \qquad \epsilon_ {c} = \frac {1}{E _ {0}} \sqrt {- A _ {0} \frac {\alpha^ {\prime} (\phi_ {c})}{g ^ {\prime} (\phi_ {c})}}\tag{103}
$$

where the critical crack phase-field $\phi _ { c }$ is solved from 

$$
\left. \frac {\partial \sigma}{\partial \phi} \right| _ {\phi_ {c}} = 0 \quad \Longrightarrow \quad \Big [ g (\phi_ {c}) \cdot g ^ {\prime \prime} (\phi_ {c}) - 2 \big (g ^ {\prime} (\phi_ {c}) \big) ^ {2} \Big ] \phi_ {c} = g ^ {\prime} (\phi_ {c}) \cdot g (\phi_ {c})\tag{104}
$$

Note that the condition $\phi _ { c } \in [ 0 , 1 ]$ has to be verified. 

PFMs with $\xi > 0 \colon \alpha ^ { \prime } ( 0 ) = \xi > 0$ . The response has an initial elastic stage in which the material remains sound with $\phi = 0$ . The peak stress $\sigma _ { c }$ and the corresponding strain $\epsilon _ { c }$ are given by 

$$
\sigma_ {c} = \sqrt {A _ {0} \frac {\alpha^ {\prime} (0)}{\omega^ {\prime} (0)}}, \quad \epsilon_ {c} = \frac {1}{E _ {0}} \sqrt {- A _ {0} \frac {\alpha^ {\prime} (0)}{g ^ {\prime} (0)}}\tag{105}
$$

for $g ^ { \prime } ( 0 ) < 0$ and 

$$
\sigma_ {c} = \sqrt {A _ {0} \frac {\alpha^ {\prime \prime} (0)}{\omega^ {\prime \prime} (0)}}, \quad \epsilon_ {c} = \frac {1}{E _ {0}} \sqrt {A _ {0} \frac {\alpha^ {\prime \prime} (0)}{\omega^ {\prime \prime} (0)}}\tag{106}
$$

if $g ^ { \prime } ( 0 ) = \omega ^ { \prime } ( 0 ) = 0$ . In both cases, the critical crack phase-field is $\phi _ { c } = 0$ 

## 4.1.2 Localised solution

In practice $: ^ { 1 5 }$ the above homogeneous solution is stable only in the ascending stage $\mathrm { i } . \mathrm { e } . , \epsilon \le \epsilon _ { c }$ . When the strain $\epsilon > \epsilon _ { c } .$ , the crack phase-field localises into a localisation band with its size controlled by the length scale $l _ { 0 }$ . Assume that the crack is initiated at the location $x _ { 0 } = 0$ and the localisation band is localised within the domain $\lceil - D , D \rceil$ , with $D \ll L$ being the half bandwidth not necessarily constant. 

Upon the above setting, multiplying the governing equation (99) by $\phi ^ { \prime }$ and integration with respect to x gives [Wu, 2017] 

$$
\sigma^ {2} \omega (\phi) - A _ {0} \big [ \alpha (\phi) - 2 l _ {0} ^ {2} \phi_ {, x} \big ] = 0\tag{107}
$$

where the relation $\omega ( x = \pm D ) = \omega ( \phi = 0 ) = 0$ resulting from the boundary conditions $\phi ( x = \pm D ) = 0$ and $\nabla \phi ( x = \pm D ) = 0$ has been considered. 

The crack phase-field $\phi ( x )$ attains the maximum value $\phi ,$ at the point $x = 0$ where the identity $\phi _ { , x } = 0$ holds. The stress $\sigma$ is then evaluated at this position 

$$
\sigma (\phi_ {*}) = \sqrt {A _ {0} \frac {\alpha (\phi_ {*})}{\omega (\phi_ {*})}} = \sqrt {\frac {2 E _ {0} G _ {c}}{c _ {0} l _ {0}} \cdot \frac {\alpha (\phi_ {*})}{\omega (\phi_ {*})}}\tag{108}
$$

$\mathbf { A } \mathbf { s }$ the crack phase-field $\phi ( x )$ is a monotonically decreasing function for $x > x _ { 0 } .$ , it follows from the relation (107) that 

$$
\frac {\mathrm{d} \phi}{\mathrm{d} x} = - \frac {1}{l _ {0}} \mathcal {F} (\phi ; \phi_ {*}) \qquad \text {with} \qquad \mathcal {F} (\phi ; \phi_ {*}) = \sqrt {\alpha (\phi) - \frac {\alpha (\phi_ {*})}{\omega (\phi_ {*})} \omega (\phi)}\tag{109}
$$

Accordingly, the inverse crack phase-field $x ( \phi ; \phi _ { * } )$ and the half width $D ( \phi _ { * } )$ of the localisation band are determined as 

$$
x (\phi ; \phi_ {*}) = l _ {0} \int_ {\phi} ^ {\phi_ {*}} \mathcal {F} ^ {- 1} (\hat {\phi}; \phi_ {*}) \mathrm{d} \hat {\phi}, \qquad D (\phi_ {*}) = l _ {0} \int_ {0} ^ {\phi_ {*}} \mathcal {F} ^ {- 1} (\hat {\phi}; \phi_ {*}) \mathrm{d} \hat {\phi}\tag{110}
$$

Furthermore, the displacement u imposed at the free end $x = L$ is given by 

$$
u (\phi_ {*}) = \frac {\sigma}{E _ {0}} \int_ {0} ^ {L} [ 1 + \omega (\phi) ] \mathrm{d} x = \frac {\sigma}{E _ {0}} \bigg [ L + \int_ {0} ^ {D} \omega (\phi) \mathrm{d} x \bigg ] = \frac {\sigma}{E _ {0}} L + \frac {1}{2} w (\phi_ {*})\tag{111}
$$

which allows defining an apparent displacement jump w across the localisation band 

$$
w (\phi_ {*}) := \frac {\sigma}{E _ {0}} \int_ {- D} ^ {D} \omega (\phi) \mathrm{d} x = 2 \sqrt {\frac {2 G _ {c} l _ {0}}{c _ {0} E _ {0}}} \int_ {0} ^ {\phi_ {*}} \sqrt {\frac {\alpha (\phi_ {*})}{\omega (\phi_ {*}) \alpha (\hat {\phi}) - \alpha (\phi_ {*}) \omega (\hat {\phi})}} \omega (\hat {\phi}) \mathrm{d} \hat {\phi}\tag{112}
$$

Note that Equation (108) and (112) constitute the stress versus apparent jump parametrised by the maximum crack phase-field $\phi ,$ attained at the point $x = 0$ 

## 4.2 Particular examples

Now let us apply the above general results to several particular cases commonly adopted in the literature. The geometric crack function $\alpha ( \phi ) = \xi \phi + ( 1 - \xi ) \phi ^ { 2 }$ is considered together with the energetic degradation functions $g ( \phi )$ summarised in Table 3. 

## 4.2.1 Quadratic geometric crack function

The quadratic geometric crack function adopted in the classical PFMs [Bourdin et al., 2000, Amor et al., 2009, Miehe et al., 2010b,a] is first considered i.e., 

$$
\alpha (\phi) = \phi^ {2} \quad \Longrightarrow \quad \xi = 0, \quad c _ {0} = 2\tag{113}
$$

Several energetic degradation functions $g ( \phi )$ are discussed as follows. 

Quadratic function $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$ . It follows from the condition (104) that 

$$
\phi_ {c} = \frac {1}{4} \quad \Longrightarrow \quad \sigma_ {c} = \frac {3}{1 6} \sqrt {\frac {3 E _ {0} G _ {c}}{l _ {0}}}, \quad \epsilon_ {c} = \sqrt {\frac {G _ {c}}{3 E l _ {0}}}\tag{114}
$$

The corresponding global response is given from Equation (102) i.e., 

$$
\sigma = \left(\frac {G _ {c}}{G _ {c} + l _ {0} E _ {0} \epsilon^ {2}}\right) ^ {2} E _ {0} \epsilon , \quad \phi = \frac {E _ {0} \epsilon^ {2}}{G _ {c} / l _ {0} + E _ {0} \epsilon^ {2}}\tag{115}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/b7479189f07ae9691ae3ebfdb1892392a1567f703dccac0df6d41067cf0d515b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/9cdef740770737e9894332460864e9a28b57d3abeecdd817a1e1a3041203fcd8.jpg)



Figure 19: 1-D homogeneous stress-strain (left) and phase-field-strain (right) curves for different length scale $l _ { 0 } \colon \boldsymbol { \alpha } ( \phi ) = \phi ^ { 2 }$ and $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$


Fig. 19 gives the plots of the homogeneous stress versus strain and the phase-field versus strain. We used $G _ { c } = E _ { 0 } = 1$ for simplicity in these plots. Two observations can be made: (i) decreasing $l _ { 0 }$ results in an increase of the maximum stress, and in the limit $l _ { 0 }  0$ the maximum stress approaches infinity which is compatible with Griffith’s theory; $( i i )$ no initial elastic stage exist upon loading. In order to have better predictions for brittle fracture, other energetic degradation functions $g ( \phi )$ and/or geometric functions $\alpha ( \phi )$ have been proposed. 

Cubic function $g ( \phi ) = 3 ( 1 - \phi ) ^ { 2 } - 2 ( 1 - \phi ) ^ { 3 }$ . Equation (104) gives the following critical phase-field $\phi _ { c }$ and the corresponding stress/strain 

$$
\phi_ {c} = \frac {1}{1 0} \qquad \Longrightarrow \qquad \sigma_ {c} = \frac {2 7}{2 5 0} \sqrt {\frac {3 0 E _ {0} G _ {c}}{l _ {0}}}, \qquad \epsilon_ {c} = \sqrt {\frac {1 0 G _ {c}}{2 7 l _ {0} E _ {0}}}\tag{116}
$$

Equation (102) gives the following global responses 

(1) Elastic stage: $\epsilon \leq \bar { \epsilon }$ 

$$
\sigma = E _ {0} \epsilon , \qquad \phi = 0\tag{117a}
$$

(2) Inelastic stage: $\epsilon \geq \bar { \epsilon }$ 

$$
\sigma = \left(\frac {G _ {c}}{l _ {0}}\right) ^ {2} \left(\frac {9 E _ {0} \epsilon^ {2} - 2 G _ {c} / l _ {0}}{2 7 E _ {0} ^ {2} \epsilon^ {5}}\right), \quad \phi = 1 - \frac {G _ {c}}{3 E _ {0} l _ {0} \epsilon^ {2}}\tag{117b}
$$

for the elastic limit strain $\bar { \epsilon } = \sqrt { G _ { c } / \left( 3 E _ { 0 } l _ { 0 } \right) }$ 

Quartic function $g ( \phi ) = 4 \big ( 1 - \phi \big ) ^ { 3 } - 3 \big ( 1 - \phi \big ) ^ { 4 }$ . Similarly, the critical phase-field $\phi _ { c }$ and the corresponding stress/strain are determined as 

$$
\phi_ {c} = \frac {1}{9} \qquad \Longrightarrow \qquad \sigma_ {c} = \frac {1 2 8}{1 4 3} \sqrt {\frac {2 E _ {0} G _ {c}}{3 l _ {0}}}, \qquad \epsilon_ {c} = \frac {9}{1 6} \sqrt {\frac {2 G _ {c}}{3 E _ {0} l _ {0}}}\tag{118}
$$

It follows from Equation (102) that 

(1) Elastic stage: $\epsilon \leq \bar { \epsilon }$ 

$$
\sigma = E _ {0} \epsilon , \quad \phi = 0\tag{119a}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/229ab59612acfb150ac46f1ef4224c0239c7ca39851381282dcf31816b483b31.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/75a7dd306b72db87febdb51d2b61784b54fbc4ec2ebf4f658051e9e9856863c3.jpg)



Figure 20: 1-D homogeneous phase-field – strain curves (left) and stress – strain curves (right): $\alpha = \phi ^ { 2 }$ together with quadratic, cubic and quartic degradation functions $( l _ { 0 } = 0 . 2 5 )$ . The vertical lines correspond to ¯ and $\epsilon _ { c } ,$ respectively.



(2) Inelastic stage: $\epsilon \geq \bar { \epsilon }$


$$
\sigma = \frac {E _ {0}}{\epsilon^ {3}} \Big (\frac {G _ {c}}{6 E _ {0} l _ {0}} \Big) ^ {3 / 2} \Bigg (4 \epsilon - 3 \sqrt {\frac {G _ {c}}{6 E _ {0} l _ {0}}} \Bigg), \qquad \phi = 1 - \frac {G _ {c}}{6 E _ {0} l _ {0} \epsilon^ {2}}\tag{119b}
$$

for the elastic limit strain $\bar { \epsilon } = \sqrt { G _ { c } / \left( 6 E _ { 0 } l _ { 0 } \right) }$ 

Fig. 20 compares the quadratic, cubic and quartic degradation functions. It can be seen that, the homogeneous stress – strain curve of the cubic function is nearly linear elastic before damage onset. In fact, the ratio of $\bar { \epsilon } / \epsilon _ { c } = \sqrt { 2 7 / 3 0 } = 0 . 9 4 8 7$ is very close to 1. Furthermore, the maximum homogeneous stress is higher than the quadratic corresponding value, which results in a larger $l _ { 0 }$ for a given critical stress $\sigma _ { c }$ and thus a reduced computational cost [Borden et al., 2012]. The response of the quartic degradation functions is also characterised by an initial elastic stage as shown in Fig. 20. The elastic limit is close to the critical stress, with the corresponding ratio $\bar { \epsilon } / \epsilon _ { c } = 8 / 9 = 0 . 8 8 9$ 

<table><tr><td><eq>\alpha(\phi)</eq></td><td><eq>g(\phi)</eq></td><td><eq>\sigma_c</eq></td><td><eq>\epsilon_c</eq></td></tr><tr><td><eq>\phi^2</eq></td><td><eq>(1-\phi)^2</eq></td><td><eq>\frac{9}{16}\sqrt{\frac{E_0G_c}{3l_0}}</eq></td><td><eq>\sqrt{\frac{G_c}{3E_0l_0}}</eq></td></tr><tr><td><eq>\phi^2</eq></td><td><eq>3(1-\phi)^2-2(1-\phi)^3</eq></td><td><eq>\frac{27}{250}\sqrt{\frac{30E_0G_c}{l_0}}</eq></td><td><eq>\sqrt{\frac{10G_c}{27l_0E_0}}</eq></td></tr><tr><td><eq>\phi^2</eq></td><td><eq>4(1-\phi)^3-3(1-\phi)^4</eq></td><td><eq>\frac{128}{243}\sqrt{\frac{2E_0G_c}{3l_0}}</eq></td><td><eq>\frac{9}{16}\sqrt{\frac{2G_c}{3l_0E_0}}</eq></td></tr><tr><td><eq>\phi</eq></td><td><eq>(1-\phi)^2</eq></td><td><eq>\sqrt{\frac{3E_0G_c}{8l_0}}</eq></td><td><eq>\sqrt{\frac{3G_c}{8E_0l_0}}</eq></td></tr><tr><td><eq>2\phi-\phi^2</eq></td><td><eq>(1-\phi)^2</eq></td><td><eq>\sqrt{\frac{2E_0G_c}{\pi l_0}}</eq></td><td><eq>\sqrt{\frac{2G_c}{\pi E_0l_0}}</eq></td></tr></table>


Table 5: Peak stress $\sigma _ { c }$ and the corresponding critical strain $\epsilon _ { c }$ for various geometric crack functions $\alpha ( \phi )$ and energetic degradation functions $g ( \phi )$


## 4.2.2 Mixed linear and quadratic geometric crack function

Following the work of Wu [2017], let us consider the generic characteristic functions 

$$
\alpha (\phi) = \xi \phi + (1 - \xi) \phi^ {2} \qquad \xi \in (0, 1 ]\tag{120a}
$$

$$
g (\phi) = \frac {(1 - \phi) ^ {p}}{(1 - \phi) ^ {p} + Q (\phi)}, \quad \omega (\phi) = \frac {Q (\phi)}{(1 - \phi) ^ {p}}\tag{120b}
$$

for the polynomial $Q ( \phi )$ 

$$
Q (\phi) = a _ {1} \phi + a _ {1} a _ {2} \phi^ {2} + a _ {1} a _ {2} a _ {3} \phi^ {3} + \dots = a _ {1} \phi \cdot P (\phi)\tag{121a}
$$

$$
P (\phi) = 1 + a _ {2} \phi + a _ {2} a _ {3} \phi^ {2} + \dots\tag{121b}
$$

where the exponent $p > 0$ , and the coefficients $a _ { 1 } > 0 , a _ { 2 } , a _ { 3 } , \cdots$ , are all parameters to be determined. 

Upon the above setting, it follows that $g ^ { \prime } ( 0 ) < 0 ( \mathrm { o r } ,$ , equivalently, $\omega ^ { \prime } ( 0 ) > 0 )$ and the material behaves elastic until the stress $\sigma$ arrives at the critical value $\sigma _ { c }$ 

$$
\sigma_ {c} = \sqrt {A _ {0} \frac {\alpha^ {\prime} (0)}{\omega^ {\prime} (0)}} = \sqrt {\frac {2 \xi E _ {0} G _ {c}}{c _ {0} a _ {1} l _ {0}}}\tag{122}
$$

If the applied displacement continues increasing, the crack phase-field localises into a localisation band, resulting in the following stress versus (apparent) jump relation $\sigma ( w )$ parametrised by the maximum damage $\phi _ { * }$ 

$$
\sigma (\phi_ {*}) = \sigma_ {c} \sqrt {\frac {\left[ \xi + (1 - \xi) \phi_ {*} \right] (1 - \phi_ {*}) ^ {p}}{\xi P (\phi_ {*})}}\tag{123a}
$$

$$
w (\phi_ {*}) = \frac {4 G _ {c} \sqrt {\xi}}{c _ {0} \sigma_ {c}} \int_ {0} ^ {\phi_ {*}} \left[ \frac {P (\phi_ {*})}{(1 - \phi_ {*}) ^ {p}} \cdot \frac {\xi + (1 - \xi) \hat {\phi}}{\xi + (1 - \xi) \phi_ {*}} - \frac {P (\hat {\phi})}{(1 - \hat {\phi}) ^ {p}} \right] ^ {- \frac {1}{2}} \frac {\sqrt {\hat {\phi}} \cdot P (\hat {\phi})}{(1 - \hat {\phi}) ^ {p}} \mathrm{d} \hat {\phi}\tag{123b}
$$

The initial slope $k _ { 0 }$ of the curve $\sigma ( w )$ and the ultimate apparent jump $w _ { c }$ are then given by 

$$
k _ {0} := \lim _ {\phi * \to 0} \frac {\partial \sigma}{\partial w} = - \frac {c _ {0}}{4 \pi} \frac {\sigma_ {c} ^ {2}}{G _ {c}} \frac {\left[ \xi (a _ {2} + p + 1) - 1 \right] ^ {3 / 2}}{\xi^ {2}}\tag{124a}
$$

$$
w _ {c} := \lim _ {\phi_ {*} \to 1} w = \frac {2 \pi G _ {c}}{c _ {0} \sigma_ {c}} \sqrt {\xi P (1)} \lim _ {\phi_ {*} \to 1} \left(1 - \phi_ {*}\right) ^ {1 - p / 2}\tag{124b}
$$

for $P ( 1 ) : = P ( \phi _ { * } = 1 ) = 1 + a _ { 2 } + a _ { 2 } a _ { 3 } + \cdot \cdot \cdot \cdot$ . Furthermore, the initial half bandwidth $D _ { 0 }$ and the ultimate one $D _ { u }$ are determined as 

$$
D _ {0} = \pi l _ {0} \Big [ \xi (a _ {2} + p + 1) - 1 \Big ] ^ {- 1 / 2} = l _ {0} \sqrt [ 3 ]{- \frac {c _ {0} \pi^ {2} \sigma_ {c} ^ {2}}{4 k _ {0} \xi^ {2} G _ {c}}}\tag{125}
$$

$$
D _ {u} (\xi) = l _ {0} \int_ {0} ^ {1} \alpha^ {- \frac {1}{2}} (\hat {\phi}) \mathrm{d} \hat {\phi} = \left\{ \begin{array}{l l} \frac {l _ {0}}{\sqrt {1 - \xi}} \ln \left(\frac {2 \sqrt {1 - \xi} + 2 - \xi}{\xi}\right) & \qquad \xi \in (0, 1 ] \\ \frac {l _ {0}}{\sqrt {\xi - 1}} \left(\frac {\pi}{2} - \arcsin \frac {2 - \xi}{\xi}\right) & \qquad \xi \in [ 1, 2 ] \end{array} \right.\tag{126}
$$

which are both proportional to the length scale $l _ { 0 }$ . 

Regarding the parameter $a _ { 1 } > 0$ , the following two cases are discussed: 

The parameter $a _ { 1 }$ is fixed i.e., independent of the length scale $l _ { 0 } .$ , it follows from Equation (122) that 

$$
\sigma_ {c} \propto l _ {0} ^ {- 1 / 2} \to \infty , \qquad k _ {0} \propto l _ {0} ^ {- 1} \to - \infty , \qquad w _ {c} \propto l _ {0} ^ {1 / 2} \to 0\tag{127}
$$

for a vanishing length scale $l _ { 0 }  0$ . In this case a brittle fracture consistent with Griffith’s theory is recovered. 

For instance, for the energetic degradation function $g ( \phi ) = { \bigl ( } 1 - \phi { \bigr ) } ^ { 2 }$ it follows that 

$$
g (\phi) = \left(1 - \phi\right) ^ {2} \qquad \Longrightarrow \qquad Q (\phi) = 2 \phi - \phi^ {2}, \qquad P (\phi) = 1 - \frac {1}{2} \phi\tag{128}
$$

or, equivalently, $\begin{array} { r } { p = 2 , a _ { 1 } = 2 , a _ { 2 } = - \frac { 1 } { 2 } } \end{array}$ and $a _ { 3 } = 0$ . In this case, the critical stress $\sigma _ { c }$ is given by 

$$
\sigma_ {c} = \left\{ \begin{array}{l l} \sqrt {\frac {3 E _ {0} G _ {c}}{8 l _ {0}}} & \alpha (\phi) = \phi \\ \sqrt {\frac {2 E _ {0} G _ {c}}{\pi l _ {0}}} & \alpha (\phi) = 2 \phi - \phi^ {2} \end{array} \right.\tag{129}
$$

which depends on the length scale $l _ { 0 }$ . The above results correspond to the phase-field/gradientdamage models for brittle fracture [Pham et al., 2011, Wu and Nguyen, 2018]. 

For a constant critical stress $\sigma _ { c }$ regarded as an intrinsic material property (i.e., failure strength $f _ { t } )$ the product $a _ { 1 } l _ { 0 }$ has to be fixed as 

$$
\sigma_ {c} = \sqrt {\frac {2 \xi E _ {0} G _ {c}}{c _ {0} a _ {1} l _ {0}}} = f _ {t} \quad \Longrightarrow \quad a _ {1} l _ {0} = \frac {2 \xi E _ {0} G _ {c}}{c _ {0} f _ {t} ^ {2}}\tag{130}
$$

That is, the parameter $a _ { 1 }$ is not a material property but is inversely proportional to the length scale $l _ { 0 }$ As shown in Fig. 21, for a smaller length scale $l _ { 0 }$ which guarantees higher precision in the phase-field approximation of the sharp crack topology, the energetic degradation function $g ( \phi )$ decreases more rapidly and less energy exchange is allowed between the bulk and the crack surface. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6bdc7bdfef06f209a76580424c3e4946e7e4bf49718a18e95010ac1dbeb3b494.jpg)



Figure 21: The energetic degradation function $\begin{array} { r } { g ( \phi ) = \frac { ( 1 - \phi ) ^ { 2 } } { ( 1 - \phi ) ^ { 2 } + a _ { 1 } \phi \cdot ( 1 - \frac { 1 } { 2 } \phi ) } } \end{array}$ for various values of the parameter $a _ { 1 }$ . The value $a _ { 1 } = 2 . 0$ corresponds to the quadtric function $g ( \phi ) = \overline { { ( 1 - \phi ) ^ { 2 } } }$


In this case the stress versus (apparent) jump relation $\sigma ( w )$ given in Equation (123) is independent from the length scale parameter $l _ { 0 }$ for the constant critical stress $\sigma _ { c } = f _ { t }$ . Dependent on the involved parameters, various softening curves can be predicted as shown in Fig. 22a. This fact allows defining an equivalent cohesive zone model pioneered by Barenblatt [1959, 1962], Dugdale [1960], Hillerborg et al. [1976]. Accordingly, for a given traction – separation law (TSL) $\sigma ( w ) \ \mathbf { e . g . }$ ., the linear, exponential, hyperbolic and Cornelissen et al. [1986] softening curves as shown in Fig. 22b, the model parameters $a _ { 1 } > 0 , a _ { 2 }$ and $a _ { 3 }$ can be calibrated as [Wu, 2017] 

$$
a _ {1} = \frac {2 E _ {0} G _ {c}}{f _ {t} ^ {2}} \cdot \frac {\xi}{c _ {0} \cdot l _ {0}} = \frac {2 \xi}{c _ {0}} \cdot \frac {l _ {\mathrm{ch}}}{l _ {0}}\tag{131a}
$$

$$
a _ {2} = \frac {1}{\xi} \left[ \left(- \frac {4 \pi \xi^ {2}}{c _ {0}} \frac {G _ {c}}{f _ {t} ^ {2}} k _ {0}\right) ^ {\frac {2}{3}} + 1 \right] - (p + 1)\tag{131b}
$$

$$
a _ {3} = \left\{ \begin{array}{l l} 0 & p > 2 \\ \frac {1}{a _ {2}} \left[ \frac {1}{\xi} \left(\frac {c _ {0} w _ {c} f _ {t}}{2 \pi G _ {c}}\right) ^ {2} - (1 + a _ {2}) \right] & p = 2 \end{array} \right.\tag{131c}
$$

for Griffith’s or Irwin’s characteristic length $l _ { \mathrm { c h } } : = E _ { 0 } G _ { c } / f _ { t } ^ { 2 }$ . Note that, in contrast to the parameter $a _ { 1 }$ which is inversely proportional to the length scale $l _ { 0 }$ , the coefficients $a _ { 2 }$ and $a _ { 3 }$ are independent from it, and so is the function $P ( \phi )$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6eae9b067be9b13a2a5f66e8fd83e4ee18bbd478edc2e46f113a856f200d555f.jpg)



(a) Softening law (123) for various parameter p


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/69096e5f3e462025f2f2d84e81d110571f7064ee186f55f84e23a4f51a2981d1.jpg)



(b) Softening curves frequently adopted for quasi-brittle solids



Figure 22: Softening laws predicted by the PFM and those frequently adopted for quasi-brittle solids.


## 4.2.3 Optimal functions for cohesive fracture

For cohesive fracture, it is possible to determine the optimal geometric crack function and energetic degradation function given in Equation (120). By ‘optimal’ we mean these functions are consistent with the well known cohesive zone model. 

On the one hand, it follows from the result (Equation (124b)) that, the parameter $p < 2$ would give a zero ultimate opening displacement, generally implying a softening curve with snap-back. Contrariwise, an exponent $p \geq 2$ would lead to a positive failure crack opening $w _ { c } > 0 ;$ ; in particular, $p = 2$ results in a finite one; see Fig. 22a. Accordingly, it is justified to assume that $p \geq 2$ in the generic degradation function, cf. Equation (120b). On the other hand, a necessary condition of the irreversibility condition $\dot { \phi } \geq 0$ is that the half bandwidth $D ( \phi _ { * } )$ is non-decreasing. In particular, the initial half bandwidth, Equation (125), is not larger than the ultimate one given in Equation (126) i.e., 

$$
D _ {0} (\xi , k _ {0}) \leq D _ {u} (\xi)\tag{132}
$$

As shown in Fig. 23, the initial and ultimate half bandwidths are both monotonically decreasing functions of the parameter $\xi \in [ 0 , 2 ]$ , but the former decreases much more rapidly than the latter. Furthermore, as the initial slope $k _ { 0 } < 0$ increases, the initial half bandwidth $D _ { 0 } ( \xi ; k _ { 0 } )$ increases monotonically and eventually exceeds the ultimate one $D _ { u } ( \boldsymbol { \xi } )$ which remains constant for a given parameter $\xi .$ . Therefore, though the irreversibility condition (Equation (132)) cannot always be fulfilled, a larger parameter $\xi \in [ 0 , 2 ]$ is more favourable. More specifically, for the geometric crack function described in Equation (120a), the parameter $\xi = 2$ is optimal since it automatically guarantees the condition set in Equation (132) so long as the initial slope $k _ { 0 } \leq - f _ { t } ^ { 2 } / ( 2 G _ { c } )$ which is the case for those general softening laws frequently adopted in the modelling of quasi-brittle failure. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/800f289eab2b6856614c7b13257ff66ef2276a1e19e3400073b5de60d18e5183.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/11cb1f5fdb0f4373e726fdb7e07872fa159bc629d5938178c4fbf455c84ecea5.jpg)



(a) Various parameter $0 \le \xi \le 2$



(b) Various initial slope $k _ { 0 } < 0$



Figure 23: Initial and ultimate half bandwidths for various parameter ξ and initial slope $k _ { 0 }$


With the above arguments, Wu [2017] suggested using the geometric crack function given in Equation (120a) with $\xi = 2$ and the energetic degradation function given in Equation (120b) with $p \geq 2 ,$ i.e., 

$$
\alpha (\phi) = 2 \phi - 2 \phi^ {2} \quad \Longrightarrow \quad c _ {0} = \pi
$$

$$
g (\phi) = \frac {(1 - \phi) ^ {p}}{(1 - \phi) ^ {p} + Q (\phi)}, \qquad p \geq 2\tag{133a}
$$

(133b) 

for the polynomial $Q ( \phi )$ of cubic (or higher) order 

$$
Q (\phi) = a _ {1} \phi \cdot P (\phi), \quad P (d) = 1 + a _ {2} \phi (1 + a _ {3} \phi)\tag{133c}
$$

The parameters $a _ { 1 } > 0 , a _ { 2 }$ and $a _ { 3 }$ are determined from the relations set in Equation (131) as 

$$
a _ {1} = \frac {4}{\pi} \cdot \frac {E _ {0} G _ {c}}{f _ {t} ^ {2} l _ {0}} = \frac {4}{\pi} \cdot \frac {l _ {\mathrm{ch}}}{l _ {0}}\tag{134a}
$$

$$
a _ {2} = 2 \left(- 2 k _ {0} \frac {G _ {c}}{f _ {t} ^ {2}}\right) ^ {2 / 3} - \left(p + \frac {1}{2}\right)\tag{134b}
$$

$$
a _ {3} = \left\{ \begin{array}{l l} 0 & p > 2 \\ \frac {1}{a _ {2}} \left[ \frac {1}{8} \left(\frac {w _ {c} f _ {t}}{G _ {c}}\right) ^ {2} - (1 + a _ {2}) \right] & p = 2 \end{array} \right.\tag{134c}
$$

for the failure strength $f _ { t } > 0$ , initial modulus (slope) $k _ { 0 } \leq - 0 . 5 f _ { t } ^ { 2 } / G _ { c }$ and ultimate crack opening $w _ { c } > 0$ of a target softening curve $\sigma ( w )$ to be approximated. Once the length scale $l _ { 0 }$ is given or calibrated (which should be small enough such that sufficient precision of the phase-field approximation of the sharp crack topology is guaranteed), the parameters $a _ { 1 } , a _ { 2 }$ and $a _ { 3 }$ are then determined from standard material properties (i.e., Young’s modulus $E _ { 0 } ,$ , failure strength $f _ { t }$ , fracture energy $G _ { c } )$ and the target softening curve. 

In particular, the following optimal parameters are calibrated for those softening laws frequently adopted for quasi-brittle failure in solids [Wu, 2017]: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7f5108b4d28e35c93431303c221cbbadad76e55c49db73f324e528da8fd4dc35.jpg)



(a) Linear softening law


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/0be24d5a42b8d1761b8b028106085e670f8354b904ff95ecd79ba5dbc9a6903e.jpg)



(b) Exponential softening law


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/d36a1a45850a6ba604bff1e478dfe56f14e307d381ec4cd1d3bf1e6638d1c8f8.jpg)



(c) Hyperbolic softening law


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/636f0c70b2130426a20ba2928671a4037c742609dc7e3d83691f018a3028b863.jpg)



(d) Cornelissen’s softening law



Figure 24: Softening curves predicted by the PFM with the optimal characteristic functions given in Equation (133). The material properties are assumed as $f _ { t } = 3 . 0 \mathrm { M P a } , G _ { c } = 1 2 0 \mathrm { J / m ^ { 2 } }$


Linear softening curve: $\begin{array} { r } { p = 2 , a _ { 2 } = - \frac { 1 } { 2 } } \end{array}$ and $a _ { 3 } = 0$ 

$$
\sigma (w) = f _ {t} \max \Big (1 - \frac {f _ {t}}{2 G _ {c}} w, 0 \Big), \qquad k _ {0} = - \frac {f _ {t} ^ {2}}{2 G _ {c}}, \qquad w _ {c} = \frac {2 G _ {c}}{f _ {t}}\tag{135}
$$

Exponential softening curve: $\begin{array} { r } { p = { \frac { 5 } { 2 } } , a _ { 2 } = 2 ^ { 5 / 3 } - 3 } \end{array}$ and $a _ { 3 } = 0$ 

$$
\sigma (w) = f _ {t} \exp \Big (- \frac {f _ {t}}{G _ {c}} w \Big), \qquad k _ {0} = - \frac {f _ {t} ^ {2}}{G _ {c}}, \qquad w _ {c} = + \infty\tag{136}
$$

Hyperbolic softening curve: $p = 4 , a _ { 2 } = 2 ^ { 7 / 3 } - 4 . 5$ and $a _ { 3 } = 0$ 

$$
\sigma (w) = f _ {t} \Big (1 + \frac {f _ {t}}{G _ {c}} w \Big) ^ {- 2}, \qquad k _ {0} = - \frac {2 f _ {t} ^ {2}}{G _ {c}}, \qquad w _ {c} = + \infty\tag{137}
$$

Cornelissen et al. [1986] softening curve for normal concrete: $p = 2 , a _ { 2 } = 1 . 3 8 6 8$ and $a _ { 3 } = 0 . 6 5 6 7$ 

$$
\sigma (w) = f _ {t} \Big [ \big (1. 0 + \eta_ {1} ^ {3} r ^ {3} \big) \exp \big (- \eta_ {2} r \big) - r \big (1. 0 + \eta_ {1} ^ {3} \big) \exp \big (- \eta_ {2} \big) \Big ]\tag{138a}
$$

$$
k _ {0} = - 1. 3 5 4 6 \frac {f _ {t} ^ {2}}{G _ {c}}, \qquad w _ {c} = 5. 1 3 6 1 \frac {G _ {c}}{f _ {t}}\tag{138b}
$$

for the normalised crack opening $r : = w / w _ { c }$ as well as the typical parameters $\eta _ { 1 } ~ = ~ 3 . 0$ and $\eta _ { 2 } = 6 . 9 3$ 

The resulting softening curves described by Equation (123) are compared in Fig. 24 against the target ones. Among them, the linear softening curve is exactly reproduced, while the discrepancies for the exponential and hyperbolic ones are invisible. For the Cornelissen et al. [1986] softening curve, the observed discrepancy is also very satisfactory, though only the cubic polynomial $Q ( \phi )$ is considered in the energetic degradation function. Increasing the order of $Q ( \phi )$ or using other functions may reduce the discrepancy. Other softening laws can be similarly considered as well such as a bilinear TSL can also be reproduced using this PF-CZM model [Wu et al., 2018]. 

Remark 19. For the sake of local stability, the energetic degradation function $g ( \phi )$ has to be convex [Lorentz, 2017]. This condition transforms to [Wu and Nguyen, 2018] 

$$
a _ {1} \geq \frac {3}{2} \quad \Longrightarrow \quad l _ {0} \leq \frac {8}{3 \pi} l _ {\mathrm{ch}} \approx 0. 8 5 l _ {\mathrm{ch}}\tag{139}
$$

As it is necessary to consider $l _ { 0 } \ll l _ { \mathrm { c h } }$ in order to sufficiently resolve the phase-field regularisation (26) and (58), this sets an (almost useless) upper bound of the length scale $l _ { 0 }$ for the optimal characteristic functions (133). Comparatively, for other non-optimal options some strict conditions have to be enforced on the model parameters [Lorentz and Godard, 2011, Lorentz et al., 2012, Lorentz, 2017] 

## 4.3 Numerical verification

The aforementioned analytical solutions are verified via numerical simulations of a bar under uniaxial traction. Both brittle fracture and quasi-brittle failure are considered. 

## 4.3.1 Brittle fracture

Let us first consider the bar shown in Fig. 25. The loading is imposed using a displacement control method with a constant incremental displacement of 0.01. Units are deliberately left out here, given that they can be consistently chosen in any system. The FE mesh consists of a single layer of 1250 Q4 elements along the bar length. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f10766c1a5892c52bb7ce39a24ae7a2c063ca3faad88d104991f9cdf63c02af8.jpg)



Figure 25: Traction bar problem: geometry and material properties.


The numerical stress-strain curves are to be compared with the analytical solutions described in Section 4.2.1. Fig. 26 shows this comparison regarding the PFMs with the quadratic energetic degradation function $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$ and the cubic one $g ( \phi ) = ( 3 - s ) ( 1 - \phi ) ^ { 2 } - ( 2 - s ) ( 1 - \phi ) ^ { 3 }$ while the geometric crack functions are both adopted as $\alpha ( \phi ) = \phi ^ { 2 }$ . Excellent agreement was obtained for the cubic degradation function with $s = 1 0 ^ { - 4 }$ . Comparatively, the cubic degradation function $g ( \phi ) = 3 ( 1 - \phi ) ^ { 2 } - 2 ( 1 - \phi ) ^ { 3 }$ was considered in Kuhn et al. [2015] in which a perturbation was introduced in the first iteration of the Newton-Raphson scheme to trigger the transition from the trivial solution $\phi = 0$ to the non-trivial solution. Without this trick, one never gets damage as the phase-field stays at 0. 

## 4.3.2 Quasi-brittle failure

Let us consider a bar of length $L = 2 0 0$ mm and unit cross section (plane stress condition) under uniaxial traction. As shown in Fig. 27, the left edge of the bar is fixed, while the right edge is stretched by applying the monotonically increasing displacement $u ^ { * }$ . The Wu [2017, 2018b] PFM is considered for quasi-brittle failure. Typical material properties of concrete are assumed, i.e., Young’s modulus $E _ { 0 } = 3 . 0 \times 1 0 ^ { 4 }$ MPa, Poisson’s ratio $\nu _ { 0 } = 0 . 2$ , failure strength $f _ { t } = 3 . 0$ MPa and fracture energy $G _ { c } = 1 2 0 \ : \mathrm { J / m ^ { 2 } }$ , resulting in Griffith’s characteristic length $l _ { \mathrm { c h } } = 4 0 0$ mm. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/bfdd9472c9f5f36849a03cebf8d6ecc6ca1d06377ef6925f2861188d4223ccf4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/d16fbfe5a77d70879cd6d2e469628250542666d066ffa5b2c3a1a1a33cb8b254.jpg)



Figure 26: Numerical results of a traction bar: $\alpha = \phi ^ { 2 }$ and quadratic and cubic degradation functions. On the right is a close-up view of the left figure. Note that only the ascending parts are meaning since the softening regimes are not stable for brittle fracture.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/1d50a165f512936c24e1817a9879006c1951a87376d246f51bc9a9eec3972991.jpg)



Figure 27: Uniaxial traction of a softening bar: Geometry, loading and boundary conditions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/e5bf4babd54dd09f0fcd49f5c53ace6476aa02937e560f626f2116a7e72b7b55.jpg)



Figure 28: Uniaxial traction of a softening bar: crack phase-field for $l _ { 0 } = 1 0$ mm.


In the numerical simulations, four different internal length scale, $l _ { 0 } = 5$ mm, 10mm, 20 mm and 50 mm, are considered, with the corresponding model parameter $a _ { 1 } = { 3 2 0 } / { \pi } , { 1 6 0 } / { \pi } , { 8 0 } / { \pi }$ and $3 2 / \pi$ respectively. For each length scale $l _ { 0 } .$ , uniformly distributed finite elements with different mesh sizes h, i.e., $l _ { 0 } / h = 5 , 1 0 , 2 0$ and 50, respectively, are used in each case. 

The model parameters $a _ { 2 } = 1 . 3 8 6 8$ and $a _ { 3 } = 0 . 6 5 6 7$ are considered, resulting in analytically a softening curve approximating the Cornelissen et al. [1986] one discussed in Section 4.2.3. If no Dirichlet condition is imposed on the crack phase-field, the localisation band forms at the boundary edge as shown in Figure 28a. It may be located either at the left or right edge of the bar, dependent on imperfections and numerical errors. In this case, only one half of the fracture energy is sufficient to break the bar. Comparatively, if Dirichlet condition $\phi = 0$ is imposed on both left and right edges of the bar, the localisation band can forms at any interior position of the bar as shown in Fig. 28b. The later strategy is adopted in the simulations. 

In Fig. 29, the numerical results of load $F ^ { * }$ versus imposed displacement $u ^ { * }$ are compared against the analytical ones [Wu, 2011]. It can be seen that, for sufficiently fine mesh $( \mathrm { i . e . , } h \leq l _ { 0 } / 5 )$ the crack phase-field of large gradient within the localisation band can be sufficiently resolved. As the mesh is refined, the numerical results converge to the analytical one asymptotically. Remarkably, the numerical results are independent from the internal length $l _ { 0 } ,$ , confirming the analytical results presented in Section 4.2.2. This fact is in strong contrast to other PFMs [Bourdin et al., 2000, Amor et al., 2009, Miehe et al., 2010b, Pham et al., 2011, Freddi and Iurlano, 2017]. The above properties are rather important for a PFM be applicable for the numerical modelling of localised failure in solids. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/84c6cfcc0b10bacae6da787b45b74d6492218d2f2790d341d704c8d007cf2f0f.jpg)



(a) $l _ { 0 } / h = 5$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/fb119ba14383739c66a8ec3f0a95d4ab3b2ca0b77d912f39cd376fc0fcf549fa.jpg)



(b) $l _ { 0 } / h = 1 0$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/852be6faa2c421eb9ee11c90357f93bb1f5cf3a4c2a443b8243cf3f63f8c3e2a.jpg)



(c) $l _ { 0 } / h = 2 0$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7bbbd883c5781460a1d5d6768b0869e41a58a025bc5a3c57d8500491ccd844b3.jpg)



(d) $l _ { 0 } / h = 5 0$



Figure 29: Uniaxial traction of a softening bar with Cornelissen et al. [1986] softening curve: influences of the length scale $l _ { 0 }$ and mesh size h for the Wu [2017, 2018b] PFM for cohesive fracture.


## 4.4 A brief summary

In order to help beginners to this field find their way through this complex field fraught with jargon, we present in Table 6 a brief summary of common phase-field models for brittle and cohesive fracture. Note that we have skipped Miehe’s model which is identical to Bourdin’s model (often referred to as AT2 in the literature) except that the phase-field equation is a parabolic PDE in the former and an elliptic PDE in the latter. As can be seen, most models except the length-scale insensitive PFM of Wu [2017], Wu and Nguyen [2018] use the material strength (precisely the tensile strength $f _ { t } )$ to determine the length scale $l _ { 0 }$ . In the latter model, $l _ { 0 } \approx L / 5 0$ or $l _ { 0 } \approx L / 1 0 0$ , where L is the smallest length of the structure, gives good results. 

Remark 20. The $\tt R T 2$ model is referred to as the standard Ambrosio-Tortorelli model in the applied mathematics literature [Burke et al., 2013]. Other formulations, obtained by different combinations of $\alpha ( \phi )$ and $g ( \phi )$ , are designated by generalised Ambrosio-Tortorelli models. Burke et al. [2013] showed that for certain combinations the resulting phase-field minimisation problem has certain convenient properties e.g., positive definiteness of the Jacobian. This paper, however, confined to models with polynomial functions only. 

<table><tr><td>model</td><td><eq>\alpha(\phi)</eq></td><td><eq>g(\phi)</eq></td><td>fracture type</td><td>length scale</td><td>support</td><td><eq>\phi \in [0,1]</eq></td></tr><tr><td>AT2</td><td><eq>\phi^2</eq></td><td><eq>(1-\phi)^2</eq></td><td>brittle</td><td><eq>l_0 = \frac{27}{256} \frac{E_0 G_c}{f_t^2}</eq></td><td><eq>\infty</eq></td><td>yes</td></tr><tr><td>AT1</td><td><eq>\phi</eq></td><td><eq>(1-\phi)^2</eq></td><td>brittle</td><td><eq>l_0 = \frac{3}{8} \frac{E_0 G_c}{f_t^2}</eq></td><td><eq>4l_0</eq></td><td>no</td></tr><tr><td>Wu</td><td><eq>2\phi - \phi^2</eq></td><td><eq>\frac{(1-\phi)^p}{(1-\phi)^p + Q(\phi)}</eq></td><td>brittle/cohesive</td><td>numerical parameter</td><td><eq>\pi l_0</eq></td><td>no</td></tr></table>


Table 6: A summary of common phase-field models for brittle and cohesive fracture.


Remark 21. For AT1 $/ 2$ models, it is widely accepted that the length scale $l _ { 0 }$ should be considered as a material parameter [Pham et al., 2011, Nguyen et al., 2016b]. Even though the expressions for $l _ { 0 }$ as given in Table 6 are determined for an 1-D bar with a homogeneous phase-field, they have been successfully used for 2-D/3-D samples with notches if $l _ { 0 }$ is small compared with the problem characteristic dimensions [Mesgarnejad et al., 2015, Zhang et al., 2017b]. When this condition is not met, one obtains very thick damage zones as $l _ { 0 }$ is large with respect to the problem size [Mesgarnejad et al., 2015, Zhang et al., 2017b]. Note that reducing $l _ { 0 } ,$ , even though resulting in thinner damage zones like cracks, would yield a peak load much larger than the experimental value. The Wu model is free of this dilemma as $l _ { 0 }$ can always be selected as a small positive number. To illustrate this we refer to Fig. 30 where four geometrically similar concrete beams are analysed using the same set of parameters except the length scale for each beam is one-hundredths of its depth. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/41aa479fed9ee8c9932af24c4ff702bb997f418f640d139bcc3213f9238c7fdd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4c20b0ca44dfb66cda0d216124f30757b821a99e514760ca9b6b89af239a86fb.jpg)



Figure 30: Phase-field analysis of four geometrically similar beams [Feng and Wu, 2018].


## 5 Finite element discretisation and solvers

This section address the spatial discretisation using finite elements<sup>16</sup> be they standard Lagrange elements or isogeometric elements of the previously described PFMs. Without loss of generality, the governing equations in weak form (Equation (89)) are considered. The standard Bubnov-Galerkin finite element method is used, with the nodal displacements and phase-field variables being the unknowns. These finite elements are usually referred to as multifieldfinite elements which have been used extensively in multiphysics FE simulations for e.g., poroelasticity (see e.g., Simoni and Schrefler [2014], Nguyen et al. [2017d] for a coupled poroelasticity with cohesive cracks to model hydraulic fractures) and thermoelasticity problems etc.. Fig. 31 gives some multifield finite elements in 2-D and 3-D. Both monolithic and staggered solvers are presented. We refer to Heister et al. [2015], Gerasimov and Lorenzis [2016], Farrell and Maurini [2017] for a comprehensive treatment on these solvers. 

It is necessary for the element size h within the localisation band to be much smaller than the length scale $l _ { 0 }$ such that an accurate estimation of the fracture energy can be guaranteed in the discrete context. For brittle fracture, numerical simulations have demonstrated that the elements inside the crack band should have a size of $h \leq l _ { 0 } / 2$ [Borden et al., 2012, Miehe et al., 2010b]. Comparatively, for cohesive fracture it is suggested [Wu, 2017, 2018b] that a smaller mesh size $h \leq l _ { 0 } / 5$ be used since the energetic function is more steep than that for brittle fracture, cf. Fig. 21. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4637a6347f52b68a53db5e44a5bbd782f24aa2ee438634ca6f51f4e22f4af1df.jpg)



Figure 31: Mutifield finite elements: four-node quadrilateral element (left), three-node triangular element (middle) and linear tetrahedra element (right). Identical basis functions are usually used for the displacement and the phase-field.


Remark 22. In the multi-field FEM it is usually preferred to using unequal interpolation orders for the coupled field variables in order to suppress the stress oscillations and numerical locking. Accordingly, in the context of phase-field/gradient-damage models, it would be better that the interpolation order of the displacement is one-order higher than that of the damage. However, as already clarified in Simone et al. [2004] regarding the gradient-enhanced damage model [Peerlings et al., 1996a], even if stress oscillations otherwise exist, this strategy is not mandatory for the multi-field FEM since the use of equal-order interpolation does not decrease the convergence rate. For the linear-linear elements–linear shape functions are used for both the displacements and damage–considered in this work, the stress oscillations and potential numerical locking, both localizing within a very narrow band, have negligible effects on the numerical results. Moreover, if necessary, they can be simply solved by means of post-processing techniques like the element-wise averaging. Other approaches include the smoothed finite element method [Liu et al., 2007, Bordas et al., 2010] which are akin to hybrid methods. The above facts are in strong contrast to the mixed FEM. 

Remark 23. For problems with many cracks distributed throughout the domain, the localisation band $B \subseteq { \mathcal { Q } }$ must be coincident with the whole computational domain $\varOmega .$ . For localised failures in solids, however, a much smaller domain can be used for , so long as it encompasses potential crack propagation paths [Wu et al., 2018]. This can be achieved by only employing a PFM (with both displacement and phase-field dofs) for the sub-domain that is going to undergo damage/cracking–the so-called damage domain in Fig. 32. For the remaining part a cheaper elastic model (with only displacement dofs) is used. 

## 5.1 Finite element discretisation

Upon the above setting, the displacement field $\mathbf { u } ^ { h }$ and the resulting strain field $\epsilon ^ { h }$ are interpolated in terms $\mathbf { a } : = \left\{ \mathbf { a } _ { 1 } , \cdot \cdot \cdot , \mathbf { a } _ { I } , \cdot \cdot \cdot \right\}$ T of the nodal displacements 

$$
\mathbf {u} (\boldsymbol {x}) = \sum_ {I} \mathrm{N} _ {I} (\boldsymbol {x}) \mathbf {a} _ {I} = \mathrm{Na}, \quad \epsilon (\boldsymbol {x}) = \sum_ {I} \mathrm{B} _ {I} (\boldsymbol {x}) \mathbf {a} _ {I} = \mathrm{Ba}\tag{140}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/9bdd90175f023438c74e71e9d84470b3bdc38200831beb814de3df4a131c4561.jpg)



Figure 32: Selective usage of the phase-field model: only nodes in the damage sub-domain have crack phase-field degrees of freedom. This damage domain can be determined via a premilinary cheap full phase-field simulation.


where in 2-D cases, the interpolation matrix $\mathbf { N } : = \left[ N _ { 1 } , \cdots , N _ { I } , \cdot \cdot \cdot \right]$ and the displacement-strain matrix $\mathbf { B } : = \left[ B _ { 1 } , \cdots , B _ { I } , \cdot \cdot \cdot \right]$ have the following components 

$$
\mathbf {N} _ {I} (\boldsymbol {x}) = \left[ \begin{array}{c c} N _ {I} (\boldsymbol {x}) & 0 \\ 0 & N _ {I} (\boldsymbol {x}) \end{array} \right], \qquad \mathbf {B} _ {I} (\boldsymbol {x}) = \left[ \begin{array}{c c} N _ {I, x} & 0 \\ 0 & N _ {I, y} \\ N _ {I, y} & N _ {I, x} \end{array} \right]\tag{141}
$$

for the interpolation function $N _ { I } ( { \pmb x } )$ associated with node I of the element in the computational domain Ω. Similarly, the damage field $\phi$ and its gradient $\nabla \phi$ are interpolated in terms of the nodal damage dofs $\bar { \mathbf { a } } : = \left\{ \bar { a } _ { 1 } , \cdot \cdot \cdot , \bar { a } _ { I } , \cdot \cdot \cdot \right\} ^ { \bar { \mathrm { T } } }$ 

$$
\phi (\boldsymbol {x}) = \sum_ {I} \bar {N} _ {I} (\boldsymbol {x}) \bar {a} _ {I} = \bar {\mathbf {N}} \bar {\mathbf {a}}, \quad \nabla \phi (\boldsymbol {x}) = \sum_ {I} \bar {\mathbf {B}} _ {I} (\boldsymbol {x}) \bar {a} _ {I} = \bar {\mathbf {B}} \bar {\mathbf {a}}\tag{142}
$$

where in 2-D cases, the interpolation matrix $\bar { \mathbf { N } } : = \left\lceil N _ { 1 } , \cdots , N _ { I } , \cdot \cdot \cdot \right\rceil$ and $\bar { \mathbf { B } } : = \left\lceil \bar { \mathbf { B } } _ { 1 } , \cdot \cdot \cdot , \bar { \mathbf { B } } _ { I } , \cdot \cdot \cdot \right\rceil$ have the following components 

$$
\bar {N} _ {I} (\boldsymbol {x}) = N _ {I} (\boldsymbol {x}), \qquad \bar {\mathbf {B}} _ {I} (\boldsymbol {x}) = \left\{ \begin{array}{l} \bar {N} _ {I, x} \\ \bar {N} _ {I, y} \end{array} \right\}\tag{143}
$$

associated with the node I of elements within the localisation band . Note that identical interpolation functions $N _ { I } ( { \pmb x } )$ are generally used in the approximation of the displacement and damage fields. 

Similar FE approximations for δu and $\delta \phi$ can be defined within the framework of the Bubnov-Galerkin method. It then follows from the governing equation in weak form (89) that 

$$
\delta \mathbf {a} ^ {\mathrm{T}} \left(\int_ {\Omega} \mathbf {B} ^ {\mathrm{T}} \boldsymbol {\sigma} \mathrm{d} V + \mathbf {M} \ddot {\mathbf {a}}\right) = \delta \mathbf {a} ^ {\mathrm{T}} \mathbf {f} ^ {\text { ext }}\tag{144a}
$$

$$
\delta \bar {\mathbf {a}} ^ {\mathrm{T}} \int_ {\mathcal {B}} \left[ \bar {\mathbf {N}} ^ {\mathrm{T}} g ^ {\prime} \bar {Y} + G _ {c} \frac {1}{c _ {0}} \left(\bar {\mathbf {N}} ^ {\mathrm{T}} \frac {1}{l _ {0}} \alpha^ {\prime} + 2 l _ {0} \bar {\mathbf {B}} ^ {\mathrm{T}} \nabla \phi\right) \right] \mathrm{d} V \geq \mathbf {0}\tag{144b}
$$

for the nodal accelerations $\ddot { \mathbf { a } } = \mathrm { d } ^ { 2 } \mathbf { a } / \mathrm { d } t ^ { 2 }$ , the consistent mass matrix $\begin{array} { r } { \mathbf { M } = \int _ { \Omega } \mathbf { N } ^ { \mathrm { T } } \boldsymbol { \rho } \mathbf { N } \mathrm { d } V } \end{array}$ and the standard external force vector $\mathbf { f } ^ { \mathrm { e x t } }$ [Hughes, 1987, Zienkiewicz and Taylor, 2006], respectively. Note that sometimes a lumped mass matrix is preferred in particular for explicit dynamics. 

The arbitrariness of δa and δa¯ results in the following semi-discrete equations in residual form 

$$
\mathbf {r} ^ {u} := \mathbf {f} ^ {\text { ext }} - \int_ {\Omega} \mathbf {B} ^ {\mathrm{T}} \boldsymbol {\sigma} \mathrm{d} V - \mathbf {M} \ddot {\mathbf {a}} = \mathbf {0}\tag{145a}
$$

$$
\mathbf {r} ^ {\phi} := - \int_ {\mathcal {B}} \left[ \bar {\mathbf {N}} ^ {\mathrm{T}} \Big (g ^ {\prime} \bar {Y} + \frac {1}{c _ {0} l _ {0}} \alpha^ {\prime} G _ {c} \Big) + \frac {2 l _ {0}}{c _ {0}} G _ {c} \bar {\mathbf {B}} ^ {\mathrm{T}} \nabla \phi \right] \mathrm{d} V \leq \mathbf {0}\tag{145b}
$$

Note that above governing equations hold upon the damage boundedness $\phi \in [ 0 , 1 ]$ and the irreversibility conditions $\dot { \phi } \geq 0$ 

The system of nonlinear equations (145) in general are solved in an incremental procedure. That is, during the time interval [0, T] of interest all the state variables are considered at the discrete interval $[ t _ { n } , t _ { n + 1 } ]$ for $n = 0 , 1 , 2 , \cdots , N - 1$ . For a typical time increment $[ t _ { n } , t _ { n + 1 } ]$ of length $\varDelta t : = t _ { n + 1 } - t _ { n } .$ with all state variables known at the instance $t _ { n }$ the system of nonlinear equations (145) is solved. The unknowns are solved for each incremental step until the end instant T is reached. 

## 5.2 Irreversibility and boundedness of the crack phase-field

For the numerical implementation of non-standard phase-field/gradient-damage models, it is very important to enforce the damage boundedness $\phi ( \pmb { x } ) \in [ 0 , 1 ]$ and the irreversibility condition $\dot { \phi } \geq 0$ . Though other alternatives exist for some particular PFMs, a general strategy is to regard the governing equation (145b) as an optimisation problem bounded by the following condition [Amor, 2008] 

$$
0 \leq \bar {a} _ {I, n} \leq \bar {a} _ {I, n + 1} \leq 1 \quad \forall I = 1, 2, \dots , n _ {p}\tag{146}
$$

Upon the above condition, the governing equation (145b) constitutes a mixed complementarity problem [Facchinei and Pang, 2003, Farrell and Maurini, 2017], i.e., 

$$
\left\{ \begin{array}{l l} \bar {a} _ {I, n} <   \bar {a} _ {I, n + 1} <   1 & r _ {I} ^ {\phi} = 0 \\ \bar {a} _ {I, n + 1} = \bar {a} _ {I, n} & r _ {I} ^ {\phi} \leq 0 \\ \bar {a} _ {I, n + 1} = 1 & r _ {I} ^ {\phi} \geq 0 \end{array} \right.\tag{147}
$$

The resulting mixed complementarity problem can be solved by an appropriate solver, e.g., the quadratic optimisation solver included in the Matlab Optimization Toolbox as in Amor et al. [2009] and Pham et al. [2011] where up to 200,000 dofs were considered. In this work, we use the reduced-space active set Newton method [Benson and Munson, 2006]. That is, in each iteration 

A set of active nodes is first determined from the conditions $( \bar { a } _ { { } _ { I , n + 1 } } = \bar { a } _ { { } _ { I , n } } , r _ { I } ^ { \phi } < 0 ) \mathrm { o r } ( \bar { a } _ { { } _ { I , n + 1 } } =$ $1 , r _ { I } ^ { \phi } > 0 )$ ; 

The sub-system of Equation (145b) associated with the inactive nodes (the remaining ones), which now consists of equalities, is then solved by the Newton scheme, and the solution associated with the active nodes is set to zero. 

The solution is updated and projected onto the bounds (i.e., if $\bar { a } _ { I } > 1$ we set $\bar { a } _ { I } = 1 )$ 

The truncated residuals (excluding those corresponding to the inactive nodes) is computed to check for convergence, and the above process is repeated. 

Note that hereafter in solving Equation (145b) the linearisation is considered only for those equalities associated with the inactive nodes. The above reduced-space active set Newton method is included in the SNES solver of the open source toolkit PETSc [Balay et al., 2016]. In this work, problems up to 1.8 million dofs are considered on a high performance workstation. 

Remark 24. As we mentioned in Section 3.7, Miehe et al. [2010a] proposed replacing the damage driving force $\bar { Y }$ in Equation (145b) by a history field variable that represents its maximum value ever reached cf. Equation (93). Though this strategy has been widely adopted in the literature for those standard PFMs with $\alpha ( \phi ) = \phi ^ { 2 }$ , it does not apply to general PFMs since the boundedness $\phi ( \pmb { x } ) \in [ 0 , 1 ]$ is not guaranteed. 

## 5.3 Quasi-static fracture

In the case of quasi-static fracture, the kinetic energy is neglected such that the inertial forces Ma¨ associated with the nodal accelerations a¨ vanish in Equation (145a). In what follows, both monolithic and staggered solvers are presented. 

## 5.3.1 Monolithic solvers

For the Newton-Raphson method, the system of linear algebra equations for the correction of the nodal unknowns is written as 

$$
\left[ \begin{array}{c c} \mathbf {K} ^ {u u} & \mathbf {K} ^ {u \phi} \\ \mathbf {K} ^ {\phi u} & \mathbf {K} ^ {\phi \phi} \end{array} \right] \left\{ \begin{array}{c} \mathrm{d} \mathbf {a} \\ \mathrm{d} \bar {\mathbf {a}} \end{array} \right\} = \left\{ \begin{array}{c} \mathbf {r} ^ {u} \\ \mathbf {r} ^ {\phi} \end{array} \right\}\tag{148}
$$

where the tangent matrices are given by 

$$
\mathbf {K} ^ {u u} = \int_ {\Omega} \mathbf {B} ^ {\mathrm{T}} \left(\frac {\partial \boldsymbol {\sigma}}{\partial \boldsymbol {\epsilon}}\right) \mathbf {B} \mathrm{d} V\tag{149a}
$$

$$
\mathbf {K} ^ {u \phi} = \int_ {\mathcal {B}} \mathbf {B} ^ {\mathrm{T}} \left(\frac {\partial \pmb {\sigma}}{\partial \phi}\right) \bar {\mathbf {N}} \mathrm{d} V\tag{149b}
$$

$$
\mathbf {K} ^ {\phi u} = \int_ {\mathcal {B}} \bar {\mathbf {N}} ^ {\mathrm{T}} \left(g ^ {\prime} \frac {\partial \bar {Y}}{\partial \boldsymbol {\epsilon}}\right) \mathbf {B} \mathrm{d} V\tag{149c}
$$

$$
\mathbf {K} ^ {\phi \phi} = \int_ {\mathcal {B}} \left[ \bar {\mathbf {N}} ^ {\mathrm{T}} \Big (g ^ {\prime \prime} \bar {Y} + \frac {1}{c _ {0} l _ {0}} \alpha^ {\prime \prime} G _ {c} \Big) \bar {\mathbf {N}} + \frac {2 l _ {0}}{c _ {0}} G _ {c} \bar {\mathbf {B}} ^ {\mathrm{T}} \bar {\mathbf {B}} \right] \mathrm{d} V\tag{149d}
$$

Standard Gauss quadrature rules are used to evaluate the above integrals. In $\mathbf { K } ^ { \phi \phi }$ , the first term is a peusdo mass matrix because it is quite similar to the consistent mass matrix M. The material tangent matrix is given by 

$$
\frac {\partial \pmb {\sigma}}{\partial \pmb {\epsilon}} = g (\phi) \frac {\partial^ {2} \psi_ {0} ^ {+}}{\partial \pmb {\epsilon} ^ {2}} + \frac {\partial^ {2} \psi_ {0} ^ {-}}{\partial \pmb {\epsilon} ^ {2}}\tag{150a}
$$

and 

$$
\frac {\partial \pmb {\sigma}}{\partial \phi} = g ^ {\prime} (\phi) \frac {\partial \psi_ {0} ^ {+}}{\partial \pmb {\epsilon}}\tag{151a}
$$

for a general anisotropic PFM. As can be seen, for a variationally inconsistent PFMs i.e., $\bar { Y } \neq \psi _ { 0 } ^ { + }$ and models employing $\mathcal { H }$ to enforce damage irreversibility, the tangent matrix is no longer symmetric. It should be emphasised that to the best of our knowledge, monolithic solvers are used only for the standard PFMs in which the boundedness condition i.e., $\phi \in [ 0 , 1 ]$ is automatically satisfied and the strategy of using the local history field applies. 

As crack growth results in a strain softening response i.e., decreasing stresses with increasing strains, the external loading is usually modelled using a displacement control or an arc-length control. Unlike the gradient-enhanced damage model Peerlings et al. [1996a], the Newton-Raphson solver performs badly for Equation (145) in the quasi-static case due to the fact that the underlying energy functional is not convex. A few attempts have been presented to deal with this issue. Gerasimov and Lorenzis [2016] developed a line search technique to improve the convergence of the Newton-Raphson solver. Heister et al. [2015] proposed a strategy, among other things, to convexify the energy functional. Arc-length or continuation methods for PFMs have also been presented in May et al. [2016], Singh et al. [2016]. Our own experience with the standard monolithic solver, presented in this section, was unconvincing as it does not converge for simple fracture problems. We refer to Section 6.3 for more details on this issue of robustness of monolithic solvers. 

Remark 25. When the node-by-node sub-matrices approach is preferred, the system of linear algebra equation for the correction of the nodal unknowns is expressed as 

$$
\left[ \begin{array}{c c} \mathbf {K} _ {I J} ^ {u u} & \mathbf {K} _ {I J} ^ {u \phi} \\ \mathbf {K} _ {I J} ^ {\phi u} & K _ {I J} ^ {\phi \phi} \end{array} \right] \left\{ \begin{array}{c} \mathrm{d} \mathbf {a} _ {J} \\ \mathrm{d} \bar {a} _ {J} \end{array} \right\} = \left\{ \begin{array}{c} \mathbf {r} _ {I} ^ {u} \\ r _ {I} ^ {\phi} \end{array} \right\}\tag{152}
$$

where the node-to-node sub-matrices are given by 

$$
\mathbf {K} _ {I J} ^ {u u} = \int_ {\Omega} \mathbf {B} _ {I} ^ {\mathrm{T}} \left(\frac {\partial \boldsymbol {\sigma}}{\partial \boldsymbol {\epsilon}}\right) \mathbf {B} _ {J} \mathrm{d} V\tag{153a}
$$

$$
\mathbf {K} _ {I J} ^ {u \phi} = \int_ {\mathcal {B}} \mathbf {B} _ {I} ^ {\mathrm{T}} \frac {\partial \pmb {\sigma}}{\partial \phi} N _ {J} \mathrm{d} V\tag{153b}
$$

$$
\mathbf {K} ^ {\phi u} = \int_ {\mathcal {B}} N _ {I} \left(g ^ {\prime} \frac {\partial \bar {Y}}{\partial \epsilon}\right) \bar {\mathbf {B}} _ {J} \mathrm{d} V\tag{153c}
$$

$$
K ^ {\phi \phi} = \int_ {\mathcal {B}} \left[ N _ {I} \Big (g ^ {\prime \prime} \bar {Y} + \frac {1}{c _ {0} l _ {0}} \alpha^ {\prime \prime} G _ {c} \Big) N _ {J} + \frac {2 l _ {0}}{c _ {0}} G _ {c} \bar {\mathbf {B}} _ {I} ^ {\mathrm{T}} \bar {\mathbf {B}} _ {J} \right] \mathrm{d} V\tag{153d}
$$

with the standard displacement-strain matrice $\mathbf { B } _ { I }$ and the gradient operator $\bar { \mathbf { B } } _ { I }$ 

## 5.3.2 Alternating minimisation (Staggered) solvers

In the applied mechanics community an alternating minimisation (AM) algorithm is often adopted to solve the coupled problem. This algorithm is referred to as staggered solver in the computational mechanics community. Compared to the monolithic solver, it is much more robust and flexible, with, however, slower convergence rate. 

Algorithm 1: Quasi-static phase-field fracture model: alternating minimisation solver
Data: $\mathbf{a}_n, \bar{\mathbf{a}}_n, \mathcal{H}_n$ Result: $\mathbf{a}_{n+1}, \bar{\mathbf{a}}_{n+1}, \mathcal{H}_{n+1}$ for every successive time step $n+1$ do
    Initialisation: $(\mathbf{a}_{n+1}^{(0)}, \bar{\mathbf{a}}_{n+1}^{(0)}, \mathcal{H}_{n+1}^0) = (\mathbf{a}_n, \bar{\mathbf{a}}_n, \mathcal{H}_n), k=1$ ;
    while not converged do
    1. Compute nodal displacements $\mathbf{a}_{n+1}^{(k)}$ with fixed nodal crack phase-field variables $\bar{\mathbf{a}}_{n+1}^{(k-1)}$ $\mathbf{r}^u(\mathbf{a}_{n+1}^{(k)}) := \mathbf{f}^{\text{ext}} - \int_\Omega \mathbf{B}^\mathrm{T} \boldsymbol{\sigma} \mathrm{d}V = \mathbf{0}; \quad \boldsymbol{\sigma} = \boldsymbol{\sigma}(\mathbf{a}_{n+1}^{(k)}, \bar{\mathbf{a}}_{n+1}^{(k-1)})$ 2. For a H-based solver: update $\mathcal{H}_{n+1}^{(k)} = \max(\psi_0^+(\boldsymbol{\epsilon}(\mathbf{a}_{n+1}^{(k)})), \mathcal{H}_n)$ ;
    3. Compute crack phase-field variables $\bar{\mathbf{a}}_{n+1}^{(k)}$ with the following $g' := g'(\bar{\mathbf{a}}_{n+1}^{(k)}), \quad \alpha' := \alpha'(\bar{\mathbf{a}}_{n+1}^{(k)}), \quad \bar{Y} := \bar{Y}(\mathbf{a}_{n+1}^{(k)})$ for fixed nodal displacements $\mathbf{a}_{n+1}^{(k)}$ , using one of the following solver if applicable:
    • Bound-constrained optimisation solver $\mathbf{r}^\phi(\bar{\mathbf{a}}_{n+1}^{(k)}) := -\int_\mathcal{B}\left[\bar{\mathbf{N}}^\mathrm{T}\left(g' \bar{Y} + \frac{1}{c_0 l_0} \alpha' G_c\right) + \frac{2l_0}{c_0} G_c \bar{\mathbf{B}}^\mathrm{T} \nabla \phi\right] \mathrm{d}V \leq 0$ subjected to: $0 \leq \bar{a}_{I,n} \leq \bar{a}_{I,n+1}^{(k)} \leq 1 \quad \forall I = 1, 2, \cdots$ • H-based solver $\mathbf{r}^\phi(\bar{\mathbf{a}}_{n+1}^{(k)}) := -\int_\mathcal{B}\left[\bar{\mathbf{N}}^\mathrm{T}\left(g' \mathcal{H} + \frac{1}{c_0 l_0} \alpha' G_c\right) + \frac{2l_0}{c_0} G_c \bar{\mathbf{B}}^\mathrm{T} \nabla \phi\right] \mathrm{d}V = 0$ 4. Set $k = k + 1$ end
Update nodal unknowns: $(\mathbf{a}_{n+1}, \bar{\mathbf{a}}_{n+1}) = (\mathbf{a}_{n+1}^{(k)}, \bar{\mathbf{a}}_{n+1}^{(k)})$ ;
For a H-based solver: update $\mathcal{H}_{n+1} = \mathcal{H}_{n+1}^{(k)}$ end 

In the so-called AM solver, one first solves the nodal displacements $\mathbf { a } _ { n + 1 }$ using the crack phase-field dofs $\bar { \mathbf { a } } _ { n }$ at $t _ { n }$ . This is a linear solid mechanics problem for isotropic/hybrid PF formulations and a nonlinear one for anisotropic formulations (due to the decomposition of the strain energy). The standard Newton-Raphson method can be used. Next, the updated nodal displacements $\mathbf { a } _ { n + 1 }$ are used to solve the crack phase-field dofs $\bar { \mathbf { a } } _ { n + 1 }$ , which is a bound-constrained optimisation problem. The involved irreversibility condition and the admissible range, $0 \leq \phi _ { n } \leq \phi _ { n + 1 } \leq 1$ , can be dealt with straightforwardly as in Section 5.2 i.e., by the bound-constrained quadratic optimisation solver included in e.g., the Matlab optimisation Toolbox or the PETSc library [Balay et al., 2016]. Note that one can also solve the sub-displacement problem first followed by solving the sub-phase-field problem. The above alternative minimisation is repeated until a stop criterion is reached. Bourdin et al. [2000] used a criterion based on the phase-field i.e., $| \bar { \phi _ { n + 1 } ^ { ( k ) } } - \phi _ { n + 1 } ^ { ( k - 1 ) } | < \bar { \epsilon }$ , where  is a small positive number. Energy based stopping criterion can be considered as well [Ambati et al., 2015a]. The solution procedure is given in Algorithm 1 which corresponds to the step from $t _ { n }$ to $t _ { n + 1 }$ The above AM algorithm for general PFMs was first proposed in Amor et al. [2009] and later was adopted by Pham et al. [2011]. The slow convergence rate – Pham et al. [2017] reported 500 iteration were needed for convergence for their static fracture analyses – can be accelerated by using the overrelaxed strategy and the composite staggered-monolithic algorithm [Farrell and Maurini, 2017] though the numerical implementation is rather cumbersome. This composite solver was also adopted in Wu [2017, 2018b]. More recently, the local arc-length method with indirect displacement control was incorporated into the AM algorithm, leading to a rather robust solver to deal with localised failure induced snap-backs; see Wu [2018a] for details. 

Remark 26. For the particular case of $\alpha ( \phi ) = \phi ^ { 2 }$ , it is able to use the local history field concept of Miehe et al. [2010b] to ensure crack irreversibility and boundedness conditions. Moreover, for the energetic degradation function $g ( \phi ) = \left( 1 - \phi \right) ^ { 2 }$ a simple linear sub-problem is obtained to solve the crack phase-field. The resulting solution procedure corresponding to the step from $t _ { n } \tan t _ { n + 1 }$ is also given in Algorithm 1. Note that many researchers only use one iteration $\mathrm { e . g . }$ , Miehe et al. [2010a] disregarding whether the solution converges or not. Consequently, sufficiently small load/time size $( \sim 1 0 ^ { - 4 }$ or smaller) have to be used. 

Remark 27. In the framework of AM solver, it is possible to use two different FE meshes; one for the displacement sub-problem and one for the damage sub-problem. The mesh for the latter problem is finer than the mesh for the former. However, such an implementation is not yet realised. 

## 5.4 Dynamic fracture

In accordance with the Newmark scheme [Newmark, 1956], the nodal displacements $\mathbf { a } _ { n + 1 }$ and velocities $\dot { \mathbf { a } } _ { n + 1 }$ at the instant $t _ { n + 1 }$ are approximated as 

$$
\begin{array}{l} \mathbf {a} _ {n + 1} = \mathbf {a} _ {n} + \Delta t \dot {\mathbf {a}} _ {n} + \frac {(\Delta t) ^ {2}}{2} \Big [ (1 - 2 \beta) \ddot {\mathbf {a}} _ {n} + 2 \beta \ddot {\mathbf {a}} _ {n + 1} \Big ] \\ \dot {\mathbf {a}} _ {n + 1} = \dot {\mathbf {a}} _ {n} + \Delta t \Big [ (1 - \gamma) \ddot {\mathbf {a}} _ {n} + \gamma \ddot {\mathbf {a}} _ {n + 1} \Big ] \end{array}\tag{154a}
$$

(154b) 

for the parameters $\beta \in [ 0 , 0 . 5 ]$ and $\gamma \in [ 0 , 1 ]$ define different time integration schemes within the Newmark family. The case $\beta = 1 / 4$ and $\gamma = 1 / 2$ corresponds to the trapezoidal rule, whereas for $\beta = 0$ and $\gamma = 1 / 2$ an explicit central difference method is obtained. Note that improved schemes controlling the high frequency numerical dissipations like the HHT-α method [Hilber et al., 1977] can be considered as well in e.g., Borden et al. [2012]. 

Algorithm 2: Initialisation for the implicit and explicit dynamics phase-field fracture model
Data: $a_{0}$ , $\dot{a}_{0}$ Result: $\bar{a}_{0}$ , $\ddot{a}_{0}$ Initialisation
Compute the crack phase-field $\bar{a}_{0} \in [0,1]$ for the initial nodal displacements $a_{0}$ $\mathbf{r}^{\phi}(\bar{\mathbf{a}}_{0}) := -\int_{\mathcal{B}} \left[ \bar{\mathbf{N}}^{\mathrm{T}} \left( g' \bar{Y} + \frac{1}{c_{0} l_{0}} \alpha' G_{c} \right) + \frac{2 l_{0}}{c_{0}} G_{c} \bar{\mathbf{B}}^{\mathrm{T}} \nabla \phi \right] \mathrm{d}V = 0$ subjected to: $0 \leq \bar{a}_{I,0} \leq 1 \quad \forall I = 1, 2, \cdots$ Compute the nodal acceleration $\ddot{a}_{0}$ $\ddot{\mathbf{a}}_{0} = \mathbf{M}^{-1} \left[ f_{0}^{\mathrm{ext}} - \int_{\Omega} \mathbf{B}^{\mathrm{T}} \boldsymbol{\sigma}_{0} \mathrm{d}V \right]$ with $\boldsymbol{\sigma}_{0} = \boldsymbol{\sigma}(\mathbf{a}_{0}, \bar{\mathbf{a}}_{0})$ 

The above time evolution procedure requires an initialisation step. The initial damage state is recomputed based on a priori knowledge of the crack phase-field resulting from a previous calculation or a pre-defined crack $\varGamma _ { 0 }$ . Furthermore, the initial accelerations are determined in accordance with the initial displacement and velocity conditions. The initialisation step is given in Algorithm 2. 

## 5.4.1 Implicit dynamics

For the implicit Newmark method $( \mathrm { i } . \mathrm { e } . , \beta \ne 0 )$ , the nodal accelerations $\ddot { \mathbf { a } } _ { n + 1 }$ and velocities $\dot { \mathbf { a } } _ { n + 1 }$ can be rewritten in terms of the nodal displacements $\mathbf { a } _ { n + 1 }$ 

$$
\ddot {\mathbf {a}} _ {n + 1} = \vartheta \big (\mathbf {a} _ {n + 1} - \mathbf {a} _ {n + 1} ^ {\mathrm{trial}} \big), \qquad \dot {\mathbf {a}} _ {n + 1} = \dot {\mathbf {a}} _ {n + 1} ^ {\mathrm{trial}} + \varDelta t \gamma \ddot {\mathbf {a}} _ {n + 1}\tag{155}
$$

for the coefficient $\vartheta : = \left[ \beta ( \Delta t ) ^ { 2 } \right] ^ { - 1 }$ . The predictions for the nodal displacements and velocities $\left( \mathbf { a } _ { n + 1 } ^ { \mathrm { t r i a l } } , \dot { \mathbf { a } } _ { n + 1 } ^ { \mathrm { t r i a l } } \right)$ are expressed as 

$$
\mathbf {a} _ {n + 1} ^ {\mathrm{trial}} = \mathbf {a} _ {n} + \varDelta t \dot {\mathbf {a}} _ {n} + \frac {(\varDelta t) ^ {2}}{2} \big (1 - 2 \beta \big) \ddot {\mathbf {a}} _ {n}, \qquad \dot {\mathbf {a}} _ {n + 1} ^ {\mathrm{trial}} = \dot {\mathbf {a}} _ {n} + \varDelta t \big (1 - \gamma \big) \ddot {\mathbf {a}} _ {n}\tag{156}
$$

Substitution of the above result in to Eq. (145a) then yields a nonlinear algebraic equation in terms of the nodal displacements $\mathbf { a } _ { n + 1 }$ as 

$$
\mathbf {r} ^ {u} := \mathbf {f} ^ {\mathrm{ext}} - \int_ {\Omega} \mathbf {B} ^ {\mathrm{T}} \boldsymbol {\sigma} \mathrm{d} V - \vartheta \mathbf {M} \big (\mathbf {a} _ {n + 1} - \mathbf {a} _ {n + 1} ^ {\mathrm{trial}} \big) = \mathbf {0}\tag{157}
$$

together with the crack phase-field evolution equation (145b). The resulting system of nonlinear equations requires elegant iterative algorithm and evaluation of the current tangent stiffness. 

Algorithm 3: Implicit dynamics phase-field fracture model
Initialisation
See Algorithm 2
for every successive time step n + 1 do
    Compute the trial nodal displacements $a_{n+1}^{trial}$ and velocities $\dot{a}_{n+1}^{trial}$ $\mathbf{a}_{n+1}^{trial} = \mathbf{a}_n + \Delta t \dot{\mathbf{a}}_n + \frac{(\Delta t)^2}{2}(1 - 2\beta) \ddot{\mathbf{a}}_n, \quad \dot{\mathbf{a}}_{n+1}^{trial} = \dot{\mathbf{a}}_n + \Delta t(1 - \gamma) \ddot{\mathbf{a}}_n$ while not converged do
    Compute nodal displacements $\mathbf{a}_{n+1}^{(k)}$ with fixed nodal crack phase-field dofs $\bar{\mathbf{a}}_{n+1}^{(k-1)}$ $\mathbf{r}^u(\mathbf{a}_{n+1}^{(k)}) := \mathbf{f}^{\text{ext}} - \int_{\Omega} \mathbf{B}^{\mathrm{T}} \boldsymbol{\sigma} \mathrm{d}V - \vartheta \mathbf{M}\big(\mathbf{a}_{n+1}^{(k)} - \mathbf{a}_{n+1}^{trial}\big) = \mathbf{0}; \quad \boldsymbol{\sigma} = \boldsymbol{\sigma}(\mathbf{a}_{n+1}^{(k)}, \bar{\mathbf{a}}_{n+1}^{(k-1)})$ Compute crack phase-field dofs $\bar{\mathbf{a}}_{n+1}^{(k)}$ with fixed nodal displacements $\mathbf{a}_{n+1}^{(k)}$ $\mathbf{r}^\phi(\bar{\mathbf{a}}_{n+1}^{(k)}) := -\int_{\mathcal{B}} \left[ \bar{\mathbf{N}}^{\mathrm{T}}\left(g' \bar{Y} + \frac{1}{c_0 l_0} \alpha' G_c\right) + \frac{2l_0}{c_0} G_c \bar{\mathbf{B}}^{\mathrm{T}} \nabla \phi \right] \mathrm{d}V = \mathbf{0}$ subjected to: $0 \leq \bar{a}_{I,n} \leq \bar{a}_{I,n+1}^{(k)} \leq 1 \quad \forall I = 1, 2, \cdots$ $g' := g'(\bar{\mathbf{a}}_{n+1}^{(k)}), \quad \alpha' := \alpha'(\bar{\mathbf{a}}_{n+1}^{(k)}), \quad \bar{Y} := \bar{Y}(\mathbf{a}_{n+1}^{(k)})$ Set $k = k + 1$ Update nodal unknowns: $(\mathbf{a}_{n+1}, \bar{\mathbf{a}}_{n+1}) = (\mathbf{a}_{n+1}^{(k)}, \bar{\mathbf{a}}_{n+1}^{(k)})$ Compute the nodal accelerations $\ddot{\mathbf{a}}_{n+1}$ and velocities $\dot{\mathbf{a}}_{n+1}$ $\ddot{\mathbf{a}}_{n+1} = \vartheta(\mathbf{a}_{n+1} - \mathbf{a}_{n+1}^{trial}), \quad \dot{\mathbf{a}}_{n+1} = \dot{\mathbf{a}}_{n+1}^{trial} + \Delta t \gamma \ddot{\mathbf{a}}_{n+1}$ Fix Dirichlet boundary conditions for the nodal velocities $\dot{\mathbf{a}}_{n+1}$ . 

Note that for dynamic brittle fracture, it seems that the monolithic scheme works well without any modification of the Newton solver [Borden et al., 2012]. In principle, one can implement a monolithic implicit dynamics solver using for example the Newmark time integrator [Schlüter et al., 2014] or the HHT-α integrator [Borden et al., 2012, Ziaei-Rad et al., 2016], but more investigations are needed. Alternatively, one can also adopt an AM (staggered) solver where the displacement subproblem is advanced in time using any time integrator such as the Newmark or HTT scheme; see Algorithm 3. 

## 5.4.2 Explicit dynamics

For the explicit Newmark method with $\beta \ : = \ : 0 .$ , the resulting time evolution system is automatically decoupled such that the sub-problems separately in $\mathbf { a } _ { n + 1 }$ and $\bar { \mathbf { a } } _ { n + 1 }$ can be solved in a sequence at every time step. In particular, the current nodal displacements $\mathbf { a } _ { n + 1 }$ can be directly updated from Equation (154a), i.e., 

$$
\mathbf {a} _ {n + 1} = \mathbf {a} _ {n} + \varDelta t \dot {\mathbf {a}} _ {n} + \frac {(\varDelta t) ^ {2}}{2} \ddot {\mathbf {a}} _ {n}\tag{158}
$$

Then the crack phase-field variables $\bar { \mathbf { a } } _ { n + 1 }$ is solved via Equation (145b). The nodal accelerations $\ddot { \mathbf { a } } _ { n + 1 }$ are readily solved from the governing equation Equation (145a) with the lumped mass matrix M<sup>¯</sup> (in order to suppress the noises associated with high frequencies), and the nodal velocities $\dot { \mathbf { a } } _ { n + 1 }$ are then updated from Equation (154b) with a specific value $\gamma ( \mathbf { e . g . } , \gamma = 1 / 2$ for a middle-step velocity). The resulting procedure is summarised in Algorithm 4. Note that explicit dynamics requires very small time steps and thus it seems unnecessary to employ multiple-pass AM solver. 

```txt
Algorithm 4: Explicit dynamics phase-field fracture model
Initialisation
└ See Algorithm 2 using the lumped mass matrix M̄
for every successive time step n + 1 do
Update the nodal displacements a_{n+1} and fix the associated Dirichlet boundary conditions
a_{n+1} = a_n + Δt\dot{a}_n + \frac{(\Delta t)^2}{2}\ddot{a}_n
Compute crack phase-field dofs a_{n+1} with fixed nodal displacements a_{n+1}
r^φ(\bar{a}_{n+1}) := -\int_B \left[ \bar{N}^T \left( g' \bar{Y} + \frac{1}{c_0 l_0} \alpha' G_c \right) + \frac{2l_0}{c_0} G_c \bar{B}^T \nabla \phi \right] dV = 0
subjected to: 0 ≤ a_{I,n} ≤ a_{I,n+1} ≤ 1    ∀I = 1,2,\cdots
g' := g'(a_{n+1}),    α' := α'(a_{n+1}),    Y := Y(a_{n+1})
Compute the nodal accelerations a_{n+1} and velocities a_{n+1}
ä_{n+1} = M^{-1} \left[ f_{n+1}^{ext} - \int_\Omega B^T \sigma dV \right]    with    σ = σ(a_{n+1}, a_{n+1})
ä_{n+1} = a_n + Δt[(1 - γ)a_n + γa_{n+1}]
Fix the Dirichlet boundary conditions for the nodal velocities a_{n+1}. 
```

## 6 Computational aspects

Beside the utilisation of parallel computations, see Liu et al. [2016], Ziaei-Rad and Shen [2016], Li et al. [2016], in order to reduce the intensive computational cost inherent to PFMs, it is natural to tackle this drawback by (1) developing efficient element technologies, (2) devising novel solvers, and (3) using adaptive mesh refinement (and coarsening). Another important aspect is the code platform to implement PFMs. All these issues are discussed in this section. 

## 6.1 Computer codes

While it is quite straightforward to have a working implementation of PFMs – for example Matlab was used in Nguyen et al. [2015a] – it is vital to implement them in a future-proof environment. Therefore, a brief survey of the platforms on which existing PFM codes are implemented is first conducted. 

To the best of our knowledge, open source PFM codes, are reported in Farrell and Maurini [2017] for static brittle fracture and in Li et al. [2016] for dynamic fracture, both using the library FENICS<sup>17</sup> [Alnaes et al., 2015, Hale et al., 2017]. Heister et al. [2015] and Klinsmann et al. [2015] implemented the PF model using $\mathrm { D E A L . I I ^ { 1 8 } }$ , with the later supporting adaptive refinement and coarsening. Bourdin’s code MEF90 written in Fortran is also freely available<sup>19</sup>. Chakraborty et al. [2016a,b] implemented the Miehe et al. [2010b] model, with a monolithic solution scheme based on a Jacobian free Newton-Krylow solver using MOOSE – Multiphysics Object Oriented Simulation Environment<sup>20</sup> [Gaston et al., 2009]. The code of Kuhn et al. [2015], Steinke et al. [2016a] was implemented using FEAP, of May et al. [2015] using $\mathrm { J I V E } ^ { 2 1 }$ and of Singh et al. [2016] using NUTIL<sup>22</sup>. We also note the GPU implementation reported in Ziaei-Rad and Shen [2016]. Incorporation of the standard PFM for brittle fracture in Abaqus – a widely used commercial FE package – was presented in Msekh et al. [2015], Liu et al. [2016], Molnár and Gravouil [2017], Pillai et al. [2018], Bhowmick and Liu [2018], Jeong et al. [2018]. However only monolithic and one-pass AM solvers have been reported. In Zhou et al. [2018a], a COMSOL implementation of a multi-pass AM PF solver was presented. Gerasimov et al. [2018] presented a non-intrusive global/local implementation of a PFM, with the main objective to pave the way for a wide adoption of PFMs in industries within legacy codes. 

However, except for Farrell and Maurini [2017], Li et al. [2016], all the aforementioned numerical implementations apply only to the quadratic geometric function $\alpha ( \phi ) = \phi ^ { 2 }$ in which the admissible range [0, 1] is automatically guaranteed for any solver. Recently, the PF-CZM was implemented in Abaqus by Zhang et al. [2018] who also proposed an enhanced AM solver that requires less iterations than the standard AM solver. 

## 6.2 Element technologies

Standard Lagrange linear elements have been extensively used to implement phase-field fracture models. High order Lagrange elements might not be suitable due to the fact that their negative shape functions can result in negative damage at integration points. Some work has been proposed in the literature to speed up the computational efficiency of PF simulations. For example, Kuhn and Müller [2010b] developed shape functions which take into account the exponential character of the crack phase-field and its dependence on the parameter $l _ { 0 } .$ . In simulations with small values of $l _ { 0 }$ and coarse meshes, the elements with exponential shape functions perform significantly better than standard linear elements. However, the method is only limited to straight crack topologies. In another direction, smooth B-splines/NURBS/T splines basis functions have been used within the framework of isogeometric analysis [Borden et al., 2012, 2014, Schillinger et al., 2015, Kästner et al., 2016, Hesch et al., 2016]. An isogeometric collocation formulation was introduced in Schillinger et al. [2015] in an attempt to speed up PF computations. A VEM (virtual element method) implementation of Miehe’s isotropic brittle PFM was presented in Aldakheel et al. [2018] where it was shown that $\mathrm { V E M } ^ { 2 3 }$ with a Voronoi mesh is comparable to using finite elements of higher order with a higher computational cost and one extra parameter–the stabilisation parameter. VEM, however, comes with flexibility in mesh generation (elements of convex and non-convex n-polygons are allowed) and less prone to mesh distortion [Natarajan et al., 2015]. 

High order (precisely 4th order) PFMs have been implemented using smooth basic functions such as NURBS [Borden et al., 2012], local max-entropy [Li et al., 2015b], subdivision surface finite elements [Li et al., 2018] and H2-nonconforming Morley triangular elements [Teichtmeister et al., 2017]. 

As done in Patzák and Jirásek [2003] for nonlocal integral-type damage models, extended finite elements can be used to reduce the cost by embedding the known distribution of the displacement field across a localisation band. However, only simple 2-D problems with one localisation band was considered. In our opinion, it would be rather difficult to extend this approach to complex crack patterns. A discontinuouscontinuous approach was presented in Giovanardi et al. [2017], see Geelen et al. [2018] for a more recent similar work, where the fracture process zone around a crack tip is resolved by a PFM and the tail of the crack is handled as a true discontinuity (using XFEM). Even though the resulting formulation is much faster compared to the standard PFM, applications are however only limited to simple crack patterns in 2-D. Needless to say, the implementation is complex. In our opinion, the main motivation of using a PFM is to solve problems with complex crack patterns that methods like XFEM cannot. Therefore, the combination of a PFM with a discontinuous approach like XFEM may not be the most natural and elegant. 

In an attempt to decrease the computational cost of PFMs, Khisamitov and Meschke [2018] presented a method that can be considered as a sharp phase-field fracture method where the crack sets are forced to locate on the element boundaries. Accordingly, the energy functional reads 

$$
\mathcal {E} = \int_ {\Omega} \psi (\boldsymbol {\epsilon} (\boldsymbol {u})) \mathrm{d} V + \int_ {\Gamma_ {d}} \left[ \omega_ {1} (d) \psi^ {+} ([ [ \boldsymbol {u} ] ]) + \psi^ {-} ([ [ \boldsymbol {u} ] ]) \right] \mathrm{d} A + \int_ {\Gamma_ {d}} G _ {c} \omega_ {2} (d) \mathrm{d} A\tag{159}
$$

where $\Gamma _ { d }$ represents the element inter-boundaries and [[u]] denotes the displacement jumps. The damage field is only discretised along the element boundaries and thus the size of the discretised problem is much smaller compared with standard PFMs. The resulting phase-field zero-thickness interface elements have the same topology (triple-noded interface elements) as the interface elements presented in Nguyen et al. [2017d] for hydraulic fracture modelling. For brittle fracture, $\omega _ { 1 / 2 } ( d )$ are given by 

$$
\omega_ {1} = (1 - d) ^ {2}, \quad \omega_ {2} = d ^ {2}\tag{160}
$$

The results are however sensitive to the mesh in the same manner as zero-thickness interface element techniques and one needs to insert these elements in a FE mesh prior to the simulation. A tool for the latter is described in [Nguyen, 2014a]. 

## 6.3 Solvers

Compared to the implementation of elemental and nodal enrichment methods [Wu, 2011, Bordas et al., 2007], the computer implementation of a PFM is simple at the element level but usually a more specific solver should be used. Basically, the following solvers can be employed to solve the governing equations of a PF model: 

the alternating minimisation algorithm of Bourdin et al. [2000] with bound-constrained optimisation solvers to handle the crack irreversibility and boundedness conditions [Amor et al., 2009, Farrell and Maurini, 2017, Li et al., 2016, Wu, 2017, 2018b], 

the alternating minimisation algorithm with path-following strategies like the local arc-length (or indirect displacement) control [Wu, 2018a], 

the staggered scheme with a single iteration using the local history variable of Miehe et al. [2010a] – this has been widely used in the computational mechanics community, 

the monolithic solver [Miehe et al., 2010b, Heister et al., 2015, Gerasimov and Lorenzis, 2016], 

the monolithic solver with path-following strategies like the energy dissipation or fracture surface control [May et al., 2016, Singh et al., 2016]. 

It is known that the monolithic algorithm using the standard Newton-Raphson scheme performs poorly since the underlying energy functional is not convex with respect to (w.r.t.) the total unknowns (i.e., the displacement and phase-field). Several attempts, such as modified Newton scheme [Heister et al., 2015, Wick, 2017], line search method [Gerasimov and Lorenzis, 2016], path-following strategies [May et al., 2016, Singh et al., 2016], etc., have been proposed to enhance the robustness of the monolithic solver. However, these techniques are usually problem dependent and not always effective. Comparatively, as the energy functional to be minimised is quadratic and convex w.r.t. the displacement and phase-field separately, the discrete governing equations can be solved by fixing the phase-field and the displacement field alternately [Bourdin et al., 2000, 2008b]. The resulting alternating minimisation (AM) or staggered algorithm is very robust, at the cost of computational inefficiency. The slow convergence rate can be accelerated by using the over-relaxed strategy and the composite staggered-monolithic algorithm [Farrell and Maurini, 2017] though the numerical implementation is rather cumbersome. 

In solving the governing equations of a PFM, one has to address correctly the boundedness $\phi \in [ 0 , 1 ]$ and the irreversibility condition $\dot { \phi } \geq 0$ on the phase-field variable. They were considered in Bourdin et al. [2000, 2008b] only for fully developed cracks. Miehe et al. [2010a] proposed a one-pass staggered algorithm using the local history variable, which requires very small time increment and applies only to the standard PFM with quadratic geometric function $\alpha ( \phi ) = \phi ^ { 2 }$ . Amor et al. [2009] suggested using the AM algorithm in which the phase-field sub-problem is solved by a bound-constrained optimisation solver. In the resulting algorithm, the boundedness $\phi \in [ 0 , 1 ]$ and the irreversibility condition $\dot { \phi } \geq 0$ on the phase-field variable can be exactly enforced. Consequently, the AM algorithm with bound-constrained optimisation solvers is universal since it applies to general PFMs with generic geometric crack function $\alpha ( \phi )$ , cf. Equation (58). As far as linear solvers are concerned, Bilgen et al. [2018] proposed to use a multigrid method as a preconditioner within a Krylov-space method in order to speed up the convergence. This efficient linear solver was used in a PFM to study conchoidal fracture. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6f60faa3f77bd6ce8f71c49016514a2faf3682777feb86104aea0f3b42c9c212.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/ca45cb56150e3240b583e79ae880746ee5a9e42928f71c548f713f9712bafbba.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/99446d4ef3365c1a983c83a1b74089a29b9a4484789132854a27864c05c6f307.jpg)



(c)



Figure 33: Edged crack under shear: (a) crack pattern, (b) load-displacement curve and (c) performance of the arc-length solver in solving Equation (213).


None of the aforementioned solvers can deal with global responses with snap-backs i.e., a decreasing global force with a decreasing displacement. As the standard PFM for brittle fracture is considered, May et al. [2016] presented a monolithic arc-length solver in which the path-following function is the internal energy in the elastic regime and the dissipation in the softening regime. Singh et al. [2016] reported a similar solver which uses the crack surface (or length in 2-D) to control the loading process for both monolithic and one-pass staggered schemes; see Appendix E for the details. Our experiences show that an arc-length solver is not only useful for tracing snap-backs but also helps to improve the robustness of the monolithic solver with adaptive time stepping. We demonstrate the robustness of this solver for the edge crack under shear problem, which is now a benchmark problem. The results are given in Fig. 33. As can be observed, the entire load-displacement curve can be tracked with only 200 increments and there are three iterations per increment to achieve convergence with a tolerance of $1 0 ^ { - 4 } .$ . The standard monolithic solver using the displacement control did not converge with increments of $1 0 ^ { - 5 }$ mm. Automatic loading step sizes were used in Liu et al. [2016] and even very small increments of $1 0 ^ { - 6 }$ mm were used in Ambati et al. [2015a]. 

In order to improve precision of the one-pass staggered solver and to further enhance the robustness of the monolithic solver, Wu [2018a] proposed an AM algorithm with path-following strategies. The phasefield sub-problem is solved by a bound-constrained optimisation solver to enforce exactly the boundedness and irreversibility conditions of the phase-field. Material softening induced snap-backs are dealt with by introducing equilibrium paths in terms of the fracture surface and the indirect displacement (selected degrees of freedom). It is found that, the AM solver with the fracture surface control not only cannot be used in the whole stage (extra control is needed in the elastic stage), but also does not apply to the case of prescribed external forces. On the contrary, an indirect displacement control can be incorporated naturally into the displacement subproblem for both cases of prescribed external forces and displacements. The numerical performance of this solver will be illustrated later in Section 7.2. 

In order to illustrate the slow convergence of the robust AM solver, we consider the three point bending test given in Wu [2018a]. We solve this problem using the PF-CZM with the standard AM solver, the enhanced AM solver of Zhang et al. [2018] with the Bourdin’s stopping criterion based on the damage of two consecutive iterations and the enhanced AM solver that uses the residual of the damage sub-problem to check the convergence of the AM iterations. Recall that in the standard AM solver, for every AM iteration the two sub-problems are solved until convergence. The enhanced AM solver is slightly different where the damage sub-problem is solved in only one iteration even though this solution is not converged. Note that as an isotropic PFM was used the displacement sub-problem is linear and thus always converges in one iteration. The results are given in Fig. 34. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/723e222ebf014998b2936374015e36657f36b225107b075bbbe43bb0038d2833.jpg)



Figure 34: Performance of various alternating minimisation solvers for a quasi-brittle fracture simulation.


## 6.4 Adaptive mesh refinement and coarsening

Phase-field simulations with adaptive mesh refinement have been reported in e.g., Piero et al. [2007], Burke et al. [2010], Borden et al. [2014], Klinsmann et al. [2015], Heister et al. [2015], Wick [2016], Kästner et al. [2016], Artina et al. [2015], Paggi et al. [2018]. In Piero et al. [2007], Borden et al. [2014], Heister et al. [2015], the phase-field parameter was used as an indicator for mesh refinement, i.e., elements with $\phi > \phi _ { c }$ for a critical value $\phi _ { c } ,$ , at at least one quadrature point are refined. A different, more involved, refinement/coarsening indicator was proposed in Klinsmann et al. [2015]. In the parlance of adaptive finite element methods, the aforementioned work adopted the h-refinement technique. In Borden et al. [2014], Klinsmann et al. [2015], Heister et al. [2015], elements flagged for refinement are divided into four new 2-D quadrilateral elements i.e., isotropic mesh refinement only. Hanging nodes are treated by appropriate constraints. In what follows we present some simple isotropic mesh adaptation schemes which are able to significantly reduce the high cost of PF simulations; see Remark 28. 

Remark 28. Artina et al. [2015] proposed using anisotropic mesh adaptation in which mesh refinements is done in the direction normal to the crack not along the crack. Even though anisotropic mesh adaptation is more efficient than isotropic mesh refinement [Artina et al., 2015], its implementation is more involved and thus no further discussion on them is presented. 

## 6.4.1 Borden’s scheme

The overall adaptive scheme of Borden et al. [2014] is given in Algorithm 5. As can be seen, by re-running the simulations from the beginning, one avoids the problem of transferring data from the old mesh to the new one. Piero et al. [2007] adopted a different way – the simulation continues after mesh refinement. The old data was transferred to the new refined mesh via interpolation. 

```txt
Algorithm 5: Adaptive remeshing procedure of Borden et al. [2014].
Start with a rather coarse mesh
while not converged do
    Run the simulation
    Flag elements that satisfy the refinement/coarsening indicator
    Refine/coarsen those elements 
```

## 6.4.2 Heister’s mesh adaptation

The idea of the mesh adaptation in Heister et al. [2015] is to accurately resolve the diffuse damage bands. If, at the end of a time step, there exists some cells within the damage bands not sufficiently refined (its refinement level k is smaller than the preset maximum refinement level r), the step is resolved with a refined mesh; see Fig. 35. The procedure is summarised in Algorithm 6. 

Algorithm 6: Adaptive remeshing procedure of Heister et al. [2015].
Data: $l_0$ , maximum mesh refinement level $r$ , damage threshold $0.8 < C < 1$ Start with a rather coarse mesh
for every successive time step $n + 1$ do
    while not sufficiently refined do
    Run the simulation
    Flag cells to be refined (cells with $k < r$ and $\phi > C$ )
    Refine those elements
    Transfer solution from $t_{n+1}$ to the new mesh 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/9d207af6c236fa21065961a9fedb3935c2b7b02623f6bbd4198bbb213052ffb5.jpg)



Figure 35: Example of remeshing used in Heister et al. [2015]. The colour represents the phase-field where red indicates $\phi = 0$ and blue is for $\phi = 1$


Significant work remains to be done to provide full error-based mesh adaptation strategies for phase field fracture problems. Particularly promising directions include the use of goal-oriented error estimates as those developed within an XFEM context [Ródenas et al., 2008, Jin et al., 2017]. Three dimensional implementation of such refinement strategies may well enable a step change in the field. 

## 6.5 Modelling pre-existing cracks

Within the framework of PFMs, initial (or existing) cracks can be modelled by either of the following three methods: 

mesh induced initial cracks: Initial cracks are modelled as discrete cracks in the geometry/mesh; 

phase-field induced initial cracks: Initial cracks are modelled via Dirichlet conditions $\phi ( \pmb { x } ) = 1 \mathrm { e . g . }$ Li et al. [2016], Lee et al. [2017b], Schlüter et al. [2014]; 

-induced initial crack: Initial cracks are modelled by using the local history variable, cf. Equation (93) [Borden et al., 2012, Klinsmann et al., 2015, Strobl and Seelig, 2016]. 

For complex initial cracks, the first method would entail a laborious pre-processing step, especially for 3-D problems. Therefore, the other two options are favored particularly for a fixed regular mesh usually employed in PF simulations. Klinsmann et al. [2015] concluded that predictions given by mesh induced cracks deviate significantly from analytical relations found in the literature. This is contrary to that reported in Li et al. [2016] i.e., for the Kalthoff-Winkler experiment, the approach of phase-field induced initial cracks does not work while the method of mesh induced initial cracks does. No conclusion can be made on this issue since it seems to be very problem dependent 

In what follows, the method of Borden et al. [2012], Klinsmann et al. [2015] is presented, with an extension to handle an arbitrary number of cracks. Note that this method only applies to the standard PFM for brittle fracture i.e., $\alpha ( \phi ) = \phi ^ { 2 }$ and $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$ . In this case, the phase-field equation (101) for a 1-D homogeneous state gives 

$$
\mathcal {H} (x) = \frac {G _ {c}}{2 l _ {0}} \frac {\phi (x)}{1 - \phi (x)}\tag{161}
$$

This led Borden et al. [2012] to define the initial value for the crack as 

$$
\mathcal {H} _ {0} (\boldsymbol {x}) = \left\{ \begin{array}{l l} \frac {G _ {c}}{2 l _ {0}} \frac {\phi_ {c}}{1 - \phi_ {c}} \left(1 - \frac {2 x _ {n} (\boldsymbol {x})}{l _ {0}}\right) & x _ {n} (\boldsymbol {x}) \leq l _ {0} / 2 \\ 0 & \text { otherwise } \end{array} \right.\tag{162}
$$

where $x _ { n } ( { \pmb x } )$ denotes the distance from point x to the pre-defined crack. A critical value $\phi _ { c } = 0 . 9 9 9$ was adopted in Borden et al. [2012]. This method does not consider the region right ahead of the crack tip. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7fa4aa3193c1da5a813466702320f4f1973fb276263696b07b5364a31aa287dc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/1e4e5f454c125ed94b39ea60922b3df4a45f07aa77a0e7b7f40522331df90e4b.jpg)



Figure 36: Initial local history variable $\mathcal { H } _ { 0 }$ for an horizontal initial crack in 2-D problems with the crack tip residing inside an element.


Klinsmann et al. [2015] proposed a different formula for $\mathcal { H } _ { 0 }$ , where the region ahead of the crack tip is considered as in Fig. 36 

$$
\mathcal {H} _ {0} (\pmb {x}) = \beta_ {0} \exp \left[ - (y / \beta) ^ {2} \right] \times \left\{ \begin{array}{l l} 1 & x <   x _ {0} \\ \exp \left[ - (x - x _ {0} / \beta) ^ {2} \right] & x \geq x _ {0} \end{array} \right.\tag{163}
$$

for the crack length $x _ { 0 }$ and the parameters $( \beta _ { 0 } , \beta )$ 

Fig. 36 compares the initial local history variable $\mathcal { H } _ { 0 }$ given by Equations (162) and (163), respectively, regarding the pre-defined crack located at $x = 0$ with parameters $\beta _ { 0 } = 1$ and $l _ { 0 } = 2$ . It can be seen that if $\beta$ is chosen to be $l _ { 0 } / 4$ , the two functions yield very similar $\mathcal { H } _ { 0 }$ . Fig. 37 presents a simple analysis to find a suitable value for $\beta$ by comparing the results given by the phase-field and  induced pre-defined cracks. As it can be seen, $\beta = l _ { 0 } / 1 0$ as suggested by Klinsmann et al. [2015] is a good approximation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/246119a2de75c6341363ee0920bf4d6f93d8944c83ffc1810bf12910cfe195f4.jpg)



(a) phase field induced


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/3121f72bb65c512d1765f91a47c8d6d79833c91659ea8698fc3290f2f42ad5d5.jpg)



(b) H induced, $\beta = l _ { 0 } / 4$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4ee90022514a3291ed44e163d7af22b2638b25a1ba621fd5f0b14f568e40cf79.jpg)



(b) H induced, $\beta = l _ { 0 } / 1 0$



Figure 37: Influence of parameter $\beta$ on the pre-defined crack


Equations (162) and (163) only deal with horizontal or vertical cracks. In what follows we propose a technique that can deal efficiently with an arbitrary number of 2-D cracks, though it can be extended to 3-D without major difficulties. Our method is using the concept of bounding boxes to quickly find which elements are surrounded by a given crack. To this end, we define two sets of bounding boxes as shown in Fig. 38 – one for the finite elements and one for the cracks. A crack box is a rectangle that contains a crack with dimensions determined by the positions of the crack points and $\Delta .$ . In our implementation, we use $\Delta = l _ { 0 }$ . For a given crack it is fast to retrieve the elements surrounded by this crack. One then loops over the Gauss points of these elements, for every Gauss point three level sets are calculated Fig. $3 8 c -$ $\delta$ denotes the signed distance to the crack, $\varPsi _ { 1 }$ defines the (signed) distance to the first tip and $\varPsi _ { 2 }$ is the distance to the second crack tip. Details on the calculation of these level sets, which is classic, can be found in Stolarska et al. [2001], Moës et al. [2002], Gravouil et al. [2002]. Having these level sets the history variable is calculated as 

$$
\mathcal {H} _ {0} (\pmb {x}) = \beta_ {0} \exp \left[ - (\delta / \beta) ^ {2} \right] \times \left\{ \begin{array}{l l} 1 & \qquad \Psi_ {1} > 0, \Psi_ {2} > 0 \\ \exp \left[ - (\Psi_ {1} / \beta) ^ {2} \right] & \qquad \Psi_ {1} <   0, \Psi_ {2} > 0 \\ \exp \left[ - (\Psi_ {2} / \beta) ^ {2} \right] & \qquad \Psi_ {2} <   0, \Psi_ {1} > 0 \end{array} \right.\tag{164}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7e44a81c8a707d12d4f0b2f2edd4ccfe10f0ad901ca8ac6a5944157ff726a280.jpg)



(a) boxes associated with the cracks


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/36a90f7c7db6a036c4ad1f9c91f9e1274a17b50ffd6863a0bdd336247a12cf7f.jpg)



(b) a crack box


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/b5a744cafd3aecf55ef0520b79689b46852e557d25ea2dea38a2d491897e0caf.jpg)



(c) level sets for a crack



Figure 38: Modelling existing cracks using level sets.


An example is given to demonstrate the proposed method. A square plate with an inclined crack as shown in Fig. 39 is considered. The crack will grow symmetrically towards the preferential direction of mode I which is captured by the PFM as given in Fig. 40. 

Singh et al. [2016] presented a scheme to regularise the phase-field at the crack tips. In this scheme the initial distribution of the phase-field associated with the existing cracks is first determined by solving the following problem (obtained by minimising the crack density functional; see Equation (56)) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/8853b900edcd61be74824f391b9cd67c09e38ad109003772244f47cafede20df.jpg)



Figure 39: Plate with an inclined crack of $4 5 ^ { o }$ . The material properties are $E _ { 0 } = 2 1 0 ~ \mathrm { G P a } .$ $\nu _ { 0 } = 0 . 2 .$ $G _ { c } = 0 . 5$ and $l _ { 0 } = 0 . 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f6859e27214a4c6e0d281e51500bc0a3a3e5e084a61ef68324f2d41fd3e8c254.jpg)



Figure 40: Plate with an inclined crack of $4 5 ^ { o }$ . From left to right: initial phase-field, final phase-field and the ’crack’ defined as $0 . 9 \leq \phi \leq 1 . 0$ . A finite element mesh of $2 0 0 \times 2 0 0$ four-node quadrilateral elements is adopted.


$$
\int_ {\Omega} \left[ \frac {1}{l _ {0}} \phi_ {0} \delta \phi_ {0} + l _ {0} \nabla \phi_ {0} \cdot \delta \phi_ {0} \right] \mathrm{d} V = 0\tag{165}
$$

with Dirichlet boundary conditions $\phi _ { 0 } = 1$ for nodes locating on the cracks. The corresponding local variable $\mathcal { H } _ { 0 }$ is then given by Equation (43) 

$$
- 2 \big (1 - \phi_ {0} \big) \mathcal {H} _ {0} = G _ {c} \left(l _ {0} \Delta \phi_ {0} - \frac {1}{l _ {0}} \phi_ {0}\right)\tag{166}
$$

If finite elements with smooth basis functions such as NURBS are used, one can use Equation (166) directly to get $\mathcal { H } _ { 0 } ( \pmb { x } )$ from $\phi _ { 0 }$ determined previously using Equation (165). Alternatively, one can solve the following weak form to determine $\mathcal { H } _ { 0 }$ 

$$
\int_ {\Omega} 2 l _ {0} (1 - \phi_ {0}) \mathcal {H} _ {0} \delta \mathcal {H} _ {0} \mathrm{d} V = \int_ {\Omega} G _ {c} \left[ l _ {0} ^ {2} \nabla \phi_ {0} \cdot \nabla \delta \mathcal {H} _ {0} + \phi_ {0} \delta \mathcal {H} _ {0} \right] \mathrm{d} V\tag{167}
$$

Assuming that $\mathcal { H } _ { 0 }$ is approximated by $\mathcal { H } _ { 0 } = { N _ { I } } \mathcal { H } _ { 0 I }$ , from the above equation one obtains the following discrete equation to be solved for $\mathcal { H } _ { 0 I } -$ the nodal values of $\mathcal { H } _ { 0 }$ 

$$
\left(\int_ {\Omega} 2 l _ {0} (1 - \phi_ {0}) N _ {I} N _ {J} \mathrm{d} V\right) \mathcal {H} _ {0 J} = \int_ {\Omega} G _ {c} \big [ l _ {0} ^ {2} \nabla \phi_ {0} \cdot \nabla N _ {I} + \phi_ {0} N _ {I} \big ] \mathrm{d} V\tag{168}
$$

which is a simple linear problem. Finally, the value of $\mathcal { H } _ { 0 }$ is interpolated to the integration points to initialise the history variable. 

Remark 29. It is worth noting that the above methods to model initial cracks via the local variable $\mathcal { H } _ { 0 }$ applies only to the standard PF model with $\alpha ( \phi ) = \phi ^ { 2 }$ and $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$ . Attempts to use it with the cubic degradation resulted in a vanishing φ everywhere in the domain. The parametrised version of this degradation function [Borden et al., 2016] performs better in the sense that the distribution of $\phi$ is correct but not the magnitude – very small compared to the maximum value of 1 close to the crack. One possibility is to adopt the 1-D analytical localised solution given in Section 4.1.2 to define the initial values for the phase-field $\phi$ and uses a bound-constrained optimisation solver to solve the phase-field sub-problem. This option has, however, not yet been reported in literature. 

## 6.6 Determination of crack tip position

For the case of dynamics fracture it is necessary to compute the crack velocity in time. To this end, location of the crack tip has to be determined. The discussion here is restricted to 2-D problems and cracks grow in the positive x-direction. The crack tip is defined using the iso-curves of the PF following Borden et al. [2012], Ziaei-Rad et al. [2016], cf. Fig. 41. The input are coordinates $( x _ { 0 } , y _ { 0 } )$ of the initial crack tip and the phase-field threshold $\phi _ { \mathrm { m a x } } , \mathrm { e . g . , } \phi _ { \mathrm { m a x } } = 0 . 9$ . The procedure, implemented in a post-processing step, is as follows 

find the nodes I that have its phase-field $\bar { a } _ { I } > \phi _ { \mathrm { m a x } }$ ; 

find the coordinates of the nodes $I ;$ 

the crack tip is defined as the node having the maximum x-coordinate among the nodes $I ;$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f8ec5613a7880512d264c63bcb8a5e6630d215a531ac1cc0f157db519501cbb8.jpg)



Figure 41: Iso-curves of different values of $\phi .$


<table><tr><td><eq>t_{n+1}</eq> [μs]</td><td><eq>x_{n+1}</eq> [mm]</td><td><eq>y_{n+1}</eq> [mm]</td><td><eq>\Delta a_{n+1}^{\text{cr}}</eq>[mm]</td><td><eq>a_{n+1}^{\text{cr}}</eq> [mm]</td></tr><tr><td>0.000</td><td>50</td><td>25</td><td>0.0</td><td>0.0</td></tr><tr><td>23.425</td><td>50</td><td>25.5</td><td>0.5</td><td>0.5</td></tr><tr><td>23.925</td><td>50</td><td>25.5</td><td>0.0</td><td>0.5</td></tr><tr><td>24.425</td><td>50</td><td>25.5</td><td>0.0</td><td>0.5</td></tr><tr><td>24.925</td><td>50</td><td>26.5</td><td>1.0</td><td>1.5</td></tr></table>


Table 7: Exemplary data for the crack tip. The crack increment for time step n is denoted by $\Delta a _ { n + 1 } ^ { \mathrm { c r } }$ and the (total) crack length at time step $a _ { n + 1 } ^ { \mathrm { c r } }$ is computed as $\begin{array} { r } { a _ { n + 1 } ^ { \mathrm { c r } } = \sum _ { m \leq n } \Delta a _ { m } ^ { \mathrm { c r } } } \end{array}$


The coordinates of the crack tip are written to a file, of which one example is given in Table 7. The first three columns correspond to the raw data from which one can calculate the crack length at a given time step. Having this data, the crack velocity is calculated from a linear fitting to three points of the $( t _ { n + 1 } , a _ { n + 1 } ^ { \mathrm { c r } } )$ curve Nguyen [2014b]; that is, the crack speed at time step $t _ { n + 1 }$ is the slope of the line that best fits, in a least square sense, $( t _ { n - 1 } , a _ { n - 1 } ^ { \mathrm { c r } } ) , ( t _ { n + 1 } , a _ { n + 1 } ^ { \mathrm { c r } } )$ and $( t _ { n + 1 } , a _ { n + 1 } ^ { \mathrm { c r } } )$ 

## 6.7 Calculation of strain and surface energies

It is sometimes necessary to plot the time evolution of the strain energy $\varPsi _ { s }$ and the surface energy (or the dissipation) $\varPsi _ { s }$ . In another situation, these quantities are needed to compute the total energy which can be used as a convergence criterion in an AM solver. They are computed according to the following expressions for the anisotropic PF model 

$$
\varPsi_ {s} = \int_ {\Omega} \left[ g (\phi) \psi_ {0} ^ {+} (\pmb {\epsilon}) + \psi_ {0} ^ {-} (\pmb {\epsilon}) \right] \mathrm{d} V = \sum_ {e = 1} ^ {n _ {\mathrm{elem}}} \sum_ {i = 1} ^ {n _ {\mathrm{gp}}} w _ {i} \left[ g (\phi_ {i}) \psi_ {0} ^ {+} (\pmb {\epsilon} _ {i}) + \psi_ {0} ^ {-} (\pmb {\epsilon} _ {i}) \right]\tag{169}
$$

$$
\varPsi_ {c} = \frac {G _ {c}}{c _ {0}} \int_ {\Omega} \left[ \frac {1}{l _ {0}} \alpha (\phi) + l _ {0} \nabla \phi \cdot \nabla \phi \right] \mathrm{d} V = \frac {G _ {c}}{c _ {0}} \sum_ {e = 1} ^ {n _ {\mathrm{elem}}} \sum_ {i = 1} ^ {n _ {\mathrm{gp}}} w _ {i} \left[ \frac {1}{l _ {0}} \alpha (\phi_ {i}) + l _ {0} (\mathbf {g r a d} \phi) ^ {\mathrm{T}} \mathbf {g r a d} \phi \right]\tag{170}
$$

where $n _ { \mathrm { e l e m } }$ and $n _ { \mathrm { g p } }$ are the numbers of elements and of integration points per element, respectively; $( \pmb { x } _ { i } , \pmb { w } _ { i } )$ denote the coordinates and weights of the integration point i; grad ${ \boldsymbol { \phi } } = \left\{ { { N _ { I , x } } { { \bar { a } } _ { I } } , { N _ { I , y } } { { \bar { a } } _ { I } } , { N _ { I , z } } { { \bar { a } } _ { I } } } \right\} ^ { \mathrm { { T } } }$ and $\phi _ { i } = N _ { I } ( { \pmb x } _ { i } ) { \bar { a } } _ { I }$ in 3-D. 

## 7 Numerical examples

This section presents numerous examples to demonstrate the performance of PFMs and also to verify the capabilities in modelling fractures. The section is divided into three parts – part I in Section 7.1 concerns quasi-static brittle fracture simulations, part II addresses quasi-static cohesive fracture examples and part III in Section 7.3 is devoted to dynamic fractures. Unless otherwise stated, all the simulations are carried out using our JIVE-based C++ code FEFRAC. Visualisation is performed in PARAVIEW. Though the localisation band $B _ { h }$ is usually a much smaller sub-domain of $\varOmega _ { h }$ due to the localised nature of cracking, in this section (and probably in all works in the literature), $B _ { h }$ is taken to be coincident with the whole computational domain for simplicity $\mathrm { i . e . }$ , all the nodes have displacement and damage dofs. 

Remark 30. Bourdin et al. [2008a] showed that the fracture energy is amplified in the simulation based on finite element discretization and that this has to be taken into account in formulating the simulation. That is, 

$$
G _ {c} ^ {\mathrm{sym}} = \left(1 + \frac {h}{2 l _ {0}}\right) G _ {c}\tag{171}
$$

However as very fine meshes $( l _ { 0 } \ge 5 h )$ are needed for PF-CZM, the factor $\begin{array} { r } { 1 + \frac { h } { 2 l _ { 0 } } } \end{array}$ is very close to 1 and thus we have not applied this factor in all simulations reported in this manuscript. 

## 7.1 Quasi-static brittle fracture

In this section, several quasi-static brittle fracture problems are presented. The aims are to (1) verify performances of PF models for a wide range of problems, (2) identify difficulties that can be encountered when using PFMs to solve crack growth problems. Unless otherwise stated, the one-pass AM (staggered) solution scheme is used in all examples. 

## 7.1.1 Shear test

As a test to verify the implementation we consider the shear test as shown in Fig. 42, which becomes a popular benchmark test in the PF community. Both the isotropic formulation and the anisotropic one with the Amor et al. [2009] split of the strain energy function are considered. An FE mesh of $2 5 6 \times 2 5 6$ square elements (thus $h \approx 0 . 0 0 3 9 \mathrm { m m } )$ is utilised and a displacement control with a constant increment of $1 0 ^ { - 5 }$ mm is used. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/93f2db5672371e5b58393c2a732bde0347bcb316bfe9143f36582284a876f010.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7e140b57b1fbf749fb39d65bdb28a0a97869f0589ca97e15ae17fb15f678fae2.jpg)



Figure 42: Shear test: problem setting and material parameters. Nodes on the bottom edge are fixed, nodes on the other three edges are fixed in the vertical direction and a shear displacement is imposed on nodes located along the top edge.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6e8bd2c82db103e12529655b66363e94d6a94aaa63d7375b3b93ac3ff1c616f1.jpg)



(a) phase-field φ


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/e88abfe8c8518d63e04b30eaa6d9fed6ab65af9b986398bbf1c5b41cea046a3c.jpg)



(b) stress



Figure 43: Shear test: Numerical results with the standard isotropic PFM [Bourdin et al., 2000]. (a) crack pattern and (b) shear stress on the deformed configuration.



(a) phase-field φ


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/02a95063dcdcf98e70fb2951155d9ac8f6f4385aaaeffe27dde4c1586bc372ef.jpg)



(b) stress



Figure 44: Shear test: Numerical results with Amor et al. [2009] model: (a) crack pattern and (b) magnitude of the stresses on the deformed configuration where elements having $\phi > 0 . 9$ were removed from the plot.


The scheme of mesh induced initial cracks is first considered<sup>24</sup>. In Figs. 43 and 44 the crack pattern indicated by the phase-field $\phi$ and a plot of the shear stress are shown. The crack patterns, for both isotropic and anisotropic models are identical to the results reported in Ambati et al. [2015a]. This coincidence verifies the computer implementation. In Fig. 44(b), elements with $\phi > 0 . 9$ were removed from the $\mathrm { p l o t } ^ { 2 5 }$ to visualise the crack. Next, the influence of the length scale $l _ { 0 }$ on the response of the sample is studied by considering three values $l _ { 0 } = \{ 0 . 0 0 7 5 , 0 . 0 1 5 , 0 . 0 3 0 \}$ mm. Fig. 45 confirms the theoretical finding that the result is sensitive to the length scale $l _ { 0 }$ . That is, the smaller $l _ { 0 }$ the larger the maximum stress that the specimen can sustain. We refer to Wu and Nguyen [2018] where this test was re-visited with results being insensitive to $l _ { 0 }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/06ef54f3c8889ac9895583845bc3cf7c41d1c64e3f24201e107bc749032d634a.jpg)



Figure 45: Shear test: load-displacement curves for various $l _ { 0 } = \{ 0 . 0 0 7 5 , 0 . 0 1 5 , 0 . 0 3 0 \}$ mm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/c028760f003a6e27c35117729ee5be280ce7e80bce216a54eee5b344ec84da39.jpg)



(a) mesh1, crack inside elements


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/0ff5f99fe05d16e41a9b3b44fa2bcf1c50f5ea48a142d99e495d645a3a32c6bc.jpg)



(b) mesh2, crack on element edges


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6c3594e0c98405c3fdf0f75b16d2add4ea4c075c1882fcca6f0399a5174013cb.jpg)



(c) load-displacement curves


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/17bafa2fdf27c13d9bbc08d1d85669d96b16cd8203ca70537ef96b5c825fc448.jpg)



(d) load-displacement curves, zoom in



Figure 46: Shear test: mesh-induced initial cracks versus -induced ones for $l _ { 0 } = 0 . 0 1 5$ mm. The thick white lines in (a) and (b) represent the crack.


Next, we study different ways of representing initial cracks. To this end, besides the above method of mesh (duplicated nodes along the crack) induced initial cracks, two extra methods are considered: (1) -induced representation where the crack is located on the element edges and (2) -induced cracks where the crack is inside the elements, cf. Fig. 46(a) and Fig. 46(b), respectively. It can be observed from the results shown in Fig. 46(c) that, -induced representation with the crack located on element edges results in a stiffer elastic response compared to the other two schemes since there is no element with all Gauss points having $\phi \approx 1$ . On the other hand, -induced representation with the crack located interior elements yields a softer elastic response. This is also expected because there is one row of elements with all Gauss points having $\phi \approx 1$ (equivalent to a crack but with a finite width h). Moreover, the peak load predicted from the mesh-induced technique is smaller than both ones obtained with the -induced cracks. 

## 7.1.2 Pre-cracked sample with two holes

This example concerns a pre-cracked sample with two holes [Bouchard et al., 2003, Zheng et al., 2015]. The material properties are: Young’s modulus $E _ { 0 } = 2 1 0 \mathrm { { G P a } }$ , Poisson’s ratio $\nu _ { 0 } = 0 . 3$ , the fracture energy $G _ { c } = 1 . 0$ N/mm and the length scale parameter $l _ { 0 } = 0 . 1$ mm. A displacement control is used with an imposed displacement at the top edge whereas the bottom edge is fixed. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/58fc624178a904bc36e93a0da82fe913e7851fbc4b2ad103b8bcd667573ae73b.jpg)



Figure 47: Pre-cracked sample with two holes: the crack length is 1 mm and the hole radius is 2 mm. The bottom edge is fixed and the top edge is stretched along the vertical direction.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/154633b5aed25516693a4f1532ce3781963ad3507c56092bb5f821ada8f9cf21.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/5134dfc3a6bc32cea8622236768f00184b9f1d2e367fa9cd3cd390dec15bb839.jpg)



(a) PF result with no damage prevention around the holes (b) PF result with no damage around the hole perimeter


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/83adbda48656fb61b4bb8590944398d2496aa033e83b6f0199d3c74f0dacbd37.jpg)



(c) XFEM result [Sutula et al., 2018a,b,c]



Figure 48: Pre-cracked sample with two holes


The Amor et al. [2009] PFM and the -induced initial cracks are considered. The obtained crack patterns are given in Fig. 48. As can be seen in Fig. 48(a), if damage was not prevented from initiating around the holes, the existing cracks do not propagate but instead new cracks are initiated at the hole perimeters and grow further. Then, damage was not allowed around the holes, and the resulting damage pattern is shown in Fig. 48(b) which is different from that shown in Fig. 48(c) reported in Bouchard et al. [2003], Sutula et al. [2018c] using discrete LEFM. Note, however that the latter crack path is similar to the prediction of Zheng et al. [2015] in which symmetry was broken. As we are not aware of any experimental result of this example, it is difficult to judge which one is the correct crack path. We also obtained a different crack path using a PFM with $\alpha ( \phi ) = 2 \phi - \phi ^ { 2 }$ and $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$ . In Artina et al. [2015], the authors obtained mesh-dependent crack paths for problems with holes. Therefore, we advocate this problem as a benchmark to test the performance of PFMs. 

## 7.1.3 A square plate with two edge cracks

This example studies the growth of two edge cracks in a square subjected to uni-axial tension as shown in Fig. 49, using the Amor et al. [2009] PFM. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7bba863230930b59f824d8d314d4c687f3908a0e97966f2cff6fcb9f2102b0f9.jpg)



Figure 49: A unit square plate with 2 edge cracks under uni-axial tension.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f1237814aecbb1130d076fd4911fda6d6473812614d47f62caafe300110acf73.jpg)



(a) Deformed displacements


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/d70d590d85973e56e400e2e89c39140cf71dd71da301e4f40fa9080c6c2094ce.jpg)



(b) Crack paths



Figure 50: A unit square plate with 2 edge cracks under uni-axial tension: mesh-induced cracks.


Both mesh- and -induced initial cracks are considered as in cf. Fig. 50a and Fig. 51a. For the former, a mesh of $4 0 0 \times 4 0 0 \ : \mathrm { Q 4 }$ elements $( h = 0 . 0 0 2 5 \ : \mathrm { m m } )$ are used which ensures that the cracks are located along some element edges. For the latter, a mesh of $3 0 0 \times 3 0 0 ( h = 0 . 0 0 3 3 \mathrm { m m } )$ Q4 elements are adopted. A value of $l _ { 0 } = 0 . 0 0 6 6$ mm, twice the element size of the second mesh, is used. Note that we focus herein on the crack pattern only, so a ‘precise’ value of $l _ { 0 }$ is not chased. The crack patterns are shown in Fig. 50b and Fig. 51b which resemble the results reported for example in Judt and Ricoeur [2015]. 

We then present a comparison between the PFM and a discrete crack model implemented using the LEFM based XFEM [Sutula et al., $2 0 1 8 \mathrm { a } , \mathrm { b } , \mathrm { c } ]$ . A structured mesh independent from the cracks is considered. The fracture solution also follows from the minimisation of the total energy functional with respect to evolving total fracture area. The crack patterns given from the PFM and the XFEM are compared in Fig. 52. Note that in the XFEM one has to specify a fracture criterion e.g., the maximum hoop stress or global minimum of energy, thus rendering slightly different crack trajectories for various criteria. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/3869f4d80d4a647f5c1c4eadd6f84cc66ea468c4428ef7d56ae8f54bf6dd300f.jpg)



(a) Deformed displacements


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/ffce777c1434780d0b3142c44dc2e7d3c759bf8f80f7f7d96ed9a63841fcfe42.jpg)



(b) Crack paths



Figure 51: A unit square plate with 2 edge cracks under uni-axial tension: -induced cracks.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/11af6a1535c1460a28a173bcb4d94e6e3752145d9a03012344b73bbe4cf1d234.jpg)



(a) PF model


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/093795ff903bb642a30e4d86fa7aadfc5d92e0fd971f02f38d59530009eb85e6.jpg)



(b) XFEM [Sutula et al., 2018a,b,c]



Figure 52: A unit square plate with 2 edge cracks under uni-axial tension: PFM versus XFEM.


## 7.1.4 A square plate with 10 cracks

This example concerns the growth of 10 cracks in a square plate subjected to a bi-axial tension as shown in Fig. 53, mimicking randomly distributed joints in rocks. The crack geometry was taken from Budyn et al. [2004] and tabulated in Table 8 for completeness. The material properties are also given in Fig. 53 (the fracture toughness $K _ { c } = \sqrt { E G _ { c } }$ for the assumed plane stress condition). As introducing these 10 cracks into the mesh would be cumbersome (even in 2-D), we only utilise the method of -induced cracks such that the pre-processing can be significantly simplified as in the XFEM. An FE mesh of $3 0 0 \times 3 0 0$ Q4 elements is adopted and the length scale $l _ { 0 } = 0 . 0 1$ mm is used. The crack patterns obtained from the PFM [Amor et al., 2009] and the XFEM [Sutula et al., 2018a,b,c] are given in Fig. 54. 

For this complex problem, discrepancies are evidenced between these two solutions. We are not certain which one is correct but it should be noted that even if l 0 the PFM would not converge to the XFEM (which is based on LEFM) as the Γ convergence proof is not available for an anisotropic PFM with split of the strain energy potential. Furthermore, in our XFEM simulation, we assumed that all cracks will grow. Despite the discrepancy, it is remarkable that with a very simple FE implementation, complex crack interactions can be captured robustly by the PFM. The PFM is, therefore, a promising numerical method for modelling complex crack problems e.g., hydraulic fractures [Miehe and Mauthe, 2016, Lee et al., 2016a, 2017a]. And the same analysis can be done in 3-D case (certainly with a significantly higher cost). This is in sharp contrast to the XFEM in which an intricate implementation is required and it is very difficult to deal with complex 3-D crack patterns. Note that the ‘robustness’ of our XFEM code is achieved by simplifying the crack geometries i.e., a crack tip is frozen if it is detected that growing fractures completely cut off a rigid body; in this case, one of the cracks is pulled back so that the material is held in place by a small ligament. Furthermore, the results might be sensitive to the crack extension length [Bordas et al., 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/536dbd65e4047151ec8808dc93e79577fc2ed7c9c1144e9e47be29f37eb3533c.jpg)



Figure 53: A square plate, of $2 \times 2 ~ \mathrm { m m ^ { 2 } } .$ , with 10 random cracks under bi-axial tension.


<table><tr><td>crack ID</td><td><eq>x_1</eq></td><td><eq>y_1</eq></td><td><eq>x_2</eq></td><td><eq>y_2</eq></td></tr><tr><td>1</td><td>0.308514</td><td>1.531184</td><td>0.488788</td><td>1.711458</td></tr><tr><td>2</td><td>0.605291</td><td>1.511563</td><td>0.713210</td><td>1.332516</td></tr><tr><td>3</td><td>1.128942</td><td>1.518921</td><td>1.359495</td><td>1.694289</td></tr><tr><td>4</td><td>1.517694</td><td>1.412228</td><td>1.673441</td><td>1.229502</td></tr><tr><td>5</td><td>0.268045</td><td>0.819902</td><td>0.411528</td><td>0.991591</td></tr><tr><td>6</td><td>0.829713</td><td>0.903294</td><td>1.087246</td><td>0.957253</td></tr><tr><td>7</td><td>1.456377</td><td>0.994043</td><td>1.592502</td><td>0.819902</td></tr><tr><td>8</td><td>0.326910</td><td>0.368605</td><td>0.482656</td><td>0.520673</td></tr><tr><td>9</td><td>0.908199</td><td>0.465487</td><td>1.090925</td><td>0.346531</td></tr><tr><td>10</td><td>1.436755</td><td>0.364926</td><td>1.624387</td><td>0.493693</td></tr></table>


Table 8: A plate with 10 random cracks: crack geometry data.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/c2aa2915091fd25641276d2de747f64ab542ce4422cb4f71a2bcb77dae57431a.jpg)



(a) PFM


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/66d592e83edca7ba1b3b9953d032bf761ac2151876c6d9004133f8956e3d98b0.jpg)



(b) XFEM [Sutula et al., 2018a,b,c]



Figure 54: A square plate with 10 random cracks under bi-axial tension: PFM versus XFEM.


2007] and local mesh refinement [Ródenas et al., 2008, Jin et al., 2017]. As far as the computational cost is concerned, our XFEM code (written in Matlab) is significantly faster than our PF code (written in C++). This is not surprising because (1) the displacement sub-problem in the PFM is nonlinear, (2) our XFEM code is highly optimised and specific to the problem of 2-D static crack growth and (3) our PF code is generic in the sense that it can handle 3-D fracture problems (with the same code) and dynamic ones with branching. 

## 7.1.5 Crack growth in rock-like materials

This example presents some simulations of fracture of rock-like materials under compression. To the best knowledge of the authors, Zhang et al. [2017a] first applied PF theories to rocks. We replicate some simulations given in this reference and provide some extensions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/17ce10d935c981e7ea0dc2623096faccea1acc168b6cde3ad0b62a5168769818.jpg)



Figure 55: Rock sample with one inclined notch under uniaxial compression: geometry, loadings and material constants.


Uniaxial compression of a rock plate with one inclined notch The first example concerns a rock sample under uniaxial compression of which the geometry, loading and material properties are given in Fig. 55. Based on the given material properties, one can calculate the length scale as $l _ { 0 } = 2 7 E _ { 0 } G _ { c } / ( 2 5 6 \sigma _ { c } ^ { 2 } ) =$ 0.4 mm. An FE mesh of $5 1 0 \times 5 1 0$ Q4 elements is used $( h = 0 . 2 \ : \mathrm { m m } )$ . A displacement control of constant increment of $1 0 ^ { - 4 }$ mm is adopted. Note that a smaller value of the displacement increments did not improve the results. The fracturing process is shown in Fig. 56. Two wing cracks start growing from the notch tip in a stable manner. After these wing cracks have propagated for a while, two secondary cracks appear and start growing. The growth of these two secondary cracks is unstable and leads to failure. It seems from stage $\cdot _ { \mathrm { e } } ,$ in Fig. 56 that the PFM cannot capture correctly the final stage of failure, cf. Fig. 57. 

Uniaxial/biaxial compression of a rock plate with two inclined parallel notches The second example on rock-like materials is a sample with two inclined parallel notches as shown in Fig. 58. The geometry of the notches is designated by the terminology $" \beta - s - c " \quad$ where $\beta$ is the inclination angle of the notch with respect to the horizontal axis, $s ( a )$ denotes the spacing between the two notches and $c ( a )$ is the continuity. Note that both s and c are functions of $^ { a , }$ half crack length. In the experiments, different cases were considered. For example, $4 5 - a - 2 a$ represents a two-notch specimen with an angle of $4 5 ^ { o }$ , a spacing of a and a continuity of 2a. From the material parameters, it follows that $l _ { 0 } = 0 . 5 9 4 2$ mm. 

As Zhang et al. [2017a] have analysed different geometry configurations. Herein we consider only the case of $^ { \cdot } 4 5 { - } 2 { \mathrm { a - } } 2 { \mathrm { a } } ^ { \cdot }$ geometry and provide results not discussed in the aforementioned reference. A structured mesh of Q4 elements with a uniform element size of $0 . 5 l _ { 0 }$ is used. The load-displacement curve together with the crack pattern at a chosen time instant are given in Fig. 59. The numerical simulation gives a crack pattern similar to the experimental observation. That is, the growth of four wing cracks and the coalescence of a secondary and one wing crack. The fracturing process is explained in more detail in Fig. 60. Initially a stable growth of four wing cracks (two for each initial notch) is seen (Fig. 60b). The outer wing cracks continue to grow for a while and a shear crack is subsequently initiated close to the inner tip of the upper notch, and it coalesces with the inner wing crack of the lower notch (Fig. 60c). Up to this point, the simulated crack pattern is quite similar to the experiment, and it is remarkable that even though the numerical problem is completely symmetric, only one coalescent crack, instead of two, is captured. The crack pattern shown in Fig. 60d has not been experimentally observed. However, it is unclear to us whether the experiment has been terminated early. 

Finally, an attempt that adapts Amor et al. [2009] strain energy decomposition is presented. The crack 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/925372be6c92f4bff6e73d57becccf86c4ad8c6b745e913a677ca5e6211e9eba.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/1e30babdc7ffb9c6b5d8c57c571e37610631d4d6f85449e463cac80144d71b2d.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f94c86441cd41cc68c0b1af9b16b774a8fea01941ec7bbddd2d47ed95212bdf9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/44706324af4cabecd0ed1df63110bd6b1f86b50cf03e81b6c36377ab46fcc63f.jpg)



(b)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/9f209b762d912e4bba5eb297ef28c2555b5f28e5577cad9b8a6617379f953dc5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/1a9ac8d316b5328548153482e5d88bb025a5445e47f2c334030223a74e965ad0.jpg)



Figure 56: Rock sample with an inclined notch under uniaxial compression: fracturing process.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/2c92c29fd83682baa850c9deea4a56896a5d9fd608b499ea50405b8d418d17ac.jpg)



Figure 57: Fracture of a rock sample under uniaxial compression: crack pattern at the moment right before stage $\cdot _ { \mathrm { e } } ,$ in Fig. 56.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/17404153267bd2359ba3e3f3bdb660b19e1d2f62aabbd1dbc667bfcf763cc53f.jpg)



Figure 58: The rock sample with two parallel notches: (a) overall view and (b) detail where the coordinates of the tips can be found by a simple rotation of the ones given in (c).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/ecdc828b32708289b753eb0669a853359caf6ef7a4b16170ab54f549a737ae32.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/2504618ff2ab4619e44f239f96c94b700d4369598450b94d5d3fc9042f5001cf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/fc463dcb19d86918216b0dc1c6fd545b1ca78b0f71710dbbe4e918baf74f0030.jpg)



Figure 59: The rock sample with two parallel notches: load-displacement curve and comparison of the crack pattern with the experiment for the ’45-2a-2a’ geometry.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7d50544846c97068570dc4022b747605907f20c785e50a458730bb1d2e3c2d41.jpg)



Figure 60: The rock sample with two parallel notches: fracturing process for the ‘45-2a-2a’ geometry.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4f9f8756742ca8237a1cac49a6a74bf17eecbed369ef948920c93adc3acceda4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/19dfa820a8d262ad33c10d7f31b5d8c82abf236ab46ad18675ae385d8fd5e13f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/640e4acfe47a6a7ba999a337f952968ba4a6e6daa22f1bf2af75267855e942c7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f4e4e324287ecb5260298276d92d645c3f5086ec0be40f5430ec4a1f7e0ca2fd.jpg)



Figure 61: The rock sample with two parallel notches: fracturing process for the $^ { \cdot } 4 5 { - } 2 { \mathrm { a - } } 2 { \mathrm { a } } ^ { \cdot }$ geometry using the crack driving force given in Equations (172) and (173).


driving force is given again for convenience of reading 

$$
\bar {Y} = \frac {\psi_ {I 0} ^ {+} (\pmb {\epsilon})}{G _ {I c} / l _ {0}} + \frac {\psi_ {I I 0} ^ {+} (\pmb {\epsilon})}{G _ {I I c} / l _ {0}}\tag{172}
$$

where $\psi _ { I 0 } ^ { + } ( \epsilon )$ and $\psi _ { I I 0 } ^ { + } ( \epsilon )$ are now defined as 

$$
\varPsi_ {I} ^ {+} (\pmb {\epsilon}) = \frac {1}{2} K _ {0} \langle \mathbf {t r} (\pmb {\epsilon}) \rangle^ {2}, \qquad \varPsi_ {I I} ^ {+} (\pmb {\epsilon}) = \mu_ {0} \pmb {\epsilon} _ {D}: \pmb {\epsilon} _ {D}\tag{173}
$$

The corresponding crack pattern shown in Fig. 61 is different from the experimentally observed one. 

## 7.1.6 Asymmetrically notched beam under three-point bending

Finally, let us consider a set of asymmetrically notched beams under three-point bending experimentally tested by Ingraffea and Grigoriu [1990] and numerically analysed in Bittencourt et al. [1996]. The setup of the problem is shown in Figure 62. A plane stress state is assumed, with the out-of-plane thickness being 0.5 inch. The aim is to demonstrate that the cohesive PFM model of [Wu, 2017] can be used for brittle fracture as well [Wu and Nguyen, 2018]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/78fafa502441ca0b3c8bfb6482e104cdd2643ec5d441266765d6b181425f89fc.jpg)



Figure 62: Asymmetrically notched beams under three-point bending: Geometry (unit of length: inch), loading and boundary conditions. The notch’s width is 0.05 inch.


During the test various specimen configurations were performed to investigate the influence of the relative location between the holes and notch, characterised by the values $e _ { 1 }$ and $\begin{array} { r } { e _ { 2 } , } \end{array}$ on the crack pattern and on the global responses. It was found that the observed crack patterns were sensitive to the notch location. For instance, the two specimens with $e _ { 1 } = 5 . 0 $ inch and $e _ { 1 } = 4 . 7 5$ inch (with identical $e _ { 2 } = 1 . 5$ inch) exhibits distinct crack patterns though there was only a subtle difference (less than 2% of the beam span in these two cases) in the value of $e _ { 1 }$ . The following four cases are considered [Wu and Nguyen, 2018]: 

Specimen (0): a beam with no holes but with a pre-notch of distance $e _ { 1 } = 6$ inch and of length $e _ { 2 } = 1$ inch; 

Specimen (a): a pre-notched beam identical to Specimen (0), i.e., $e _ { 1 } = 6$ inch and $e _ { 2 } = 1$ , but with three holes; 

Specimen (b): a beam with three holes and a pre-notch defined by $e _ { 1 } = 5 . 1 5$ inch and $e _ { 2 } = 1 . 5$ inch; 

Specimen (c): a beam with three holes and a pre-notch defined by $e _ { 1 } = 4 . 7 5$ inch and $e _ { 2 } = 1 . 5$ inch. 

Regarding Specimen (0), Ingraffea and Grigoriu [1990] provided the load versus CMOD and load versus displacement (measured at the loaded point) data, which can be used to calibrate the material parameters. Specimen (a) has been frequently employed in the literature to validate various fracture models and numerical methods; see Miehe et al. [2010a] among many others in the context of phase-field models. Specimen (c) was considered in Cervera et al. [2017] using a local damage model (regualarised by the crack band method) in the context of the stabilised mixed FEM [Cervera et al., 2011]. Specimen (b) introduces a negligible difference (less than 1% of the beam span) in the value of $e _ { 1 }$ , mimicking the experimentally tested specimen with $e _ { 1 } = 5 . 0 $ inch and $e _ { 2 } = 1 . 5$ inch. 

In the numerical simulations, the material parameters are taken from Ingraffea and Grigoriu [1990]: Young’s modulus $E _ { 0 } = 4 . 7 5 \times 1 0 ^ { 5 }$ psi $( 3 . 2 7 5 \times 1 0 ^ { 3 } \ : \mathrm { M P a } )$ , Poisson’s ratio $\nu _ { 0 } = 0 . 3 5$ , the fracture energy $G _ { c } = 1$ .8 lbf/in (315 J/m<sup>2</sup>) and the failure strength $f _ { t } = 2 5 0 0$ psi (17.23 MPa), resulting into an internal length $l _ { \mathrm { c h } } = 3 . 4 7$ mm. As the aim of this example is to demonstrate the performance of the proposed model for complex brittle fracture, a single set of length scale parameter $l _ { 0 } = 0 . 0 2 5$ mm and mesh size $h = 0 . 0 0 5$ mm is employed. In order to track the complete failure process in case of snap-backs, the AM algorithm with the CMOD based control [Wu, 2018a] is employed. 

Let us first consider Specimen (0) with no holes. The numerically obtained crack pattern at CMOD $= 0 . 0 7$ inch is depicted in Figure 64a. The experimentally observed crack path is well captured. The numerical load versus CMOD and displacement are shown in Figures 63b and 63c, respectively. Not only the peak load but also the post-peak responses agree with the experimental results fairly well. The agreement, not only validates the proposed phase-field model for this example of mixed-mode brittle fracture, but also justifies the employed material parameters. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/a1de27b7335bc5487c41dbc87a5840bc004ea3e71b6511037ed629e21a2569d5.jpg)



(a) Crack patterns


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/66d4a148ef8faecdc10d8a72e06a497fe671eabde69ace5e165e3e1c3e13eebd.jpg)



(b) Curve of load versus CMOD


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/eacb7c1ce1da20b7514003e640c2b1b7dee4421790bfb8a840e88abf4f2a9d7d.jpg)



(c) Curve of load versus displacement



Figure 63: Asymmetrically notched beam under three-point bending: Numerical results for Specimen (0) with no holes.


The same material parameters are then adopted for the other three cases. As the test results of global responses are not available, only the influence of the holes on the crack patterns is investigated. The numerical crack pattern of Specimen (a) is compared against the experimental one in Figure 64a. The agreement is rather good and remarkably, the subtle fluctuation caused by the local stress concentration around the bottom hole is reproduced. As shown in Figure 64b, when the pre-notch is getting closer to the bottom hole as in Specimen (b), fluctuations of the crack path become more pronounced around the bottom hole. If the notch and the holes are not close enough, the crack bypasses the bottom hole, continues propagating upwards and eventually reaches the right hand of the middle hole. When $e _ { 1 }$ is small enough (the notch is close to the holes) as in Specimen (c) the crack propagating upwards is attracted and then arrested by the bottom hole, though eventually another crack nucleates at the opposite side and propagates upwards; see Figure 64c. The above results are consistent with the experimental observations, validating the proposed model in predicting complex fracture behavior of brittle solids. 

## 7.2 Quasi-static cohesive fracture

In this section, several benchmark tests for concrete under mode-I and mixed-model failure are simulated using the length-scale insensitive PFM of Wu [2017], Wu and Nguyen [2018]. Precisely, the hybrid isotropic/anisotropic formulation (82) is used with the effective driving force $\bar { Y }$ given by Equation $( 8 4 ) _ { 2 }$ The parameter $\beta = \infty$ is used, resulting in a Rankine based equivalent effective stress $\bar { \sigma } _ { \mathrm { e q } } = \langle \bar { \sigma } _ { 1 } \rangle$ . The discrete governing equations are solved by the AM algorithm summarised in Algorithm 1. The damage subproblem is solved by the bound-constrained optimisation solver while the displacement subproblem is further enhanced with the indirect displacement control [Wu, 2018a]. There are three length scales in this model: $h , l _ { 0 }$ and $l _ { \mathrm { c h } }$ , which should be $h \ll l _ { 0 } \ll l _ { \mathrm { c h } }$ . Our experience indicates that $h \leq l _ { 0 } / 5$ and $l _ { 0 } \approx L / 5 0$ or $l _ { 0 } \approx L / 1 0 0$ , where $L$ is the smallest length of the structure, gives good results. Note that this model has been compared with XFEM for some mode I and mixed-mode fracture problems and both gave similar results in terms of crack pattern and global response [Wu et al., 2018]. However, PFMs do not need an extra criterion to handle crack branching, see Fig. 65. 

## 7.2.1 Wedge splitting test

Let us first consider the wedge-splitting test conducted by Trunk [2000]. The square-shaped specimen, depicted in Fig. 66, is of dimensions 800 mm 800 mm 400 mm, with a vertical notch of about half the height of the specimen. It is vertically supported at the center of each half of the bottom edge. Two horizontal splitting forces $F ^ { * }$ are applied on the upper lateral faces of the notch by a vertically pushed wedge. The material properties are taken from the test, i.e., Young’s modulus $E _ { 0 } = 2 . 8 3 \times 1 0 ^ { 4 }$ MPa, Poisson’s ratio $\nu _ { 0 } = 0 . 1 8$ , the tensile strength $f _ { t } = 2 . 1 2$ MPa and the fracture energy $G _ { c } = 3 7 3 \ : \mathrm { J / m ^ { 2 } }$ 

Two length scale parameters $l _ { 0 } = 1 0$ mm and $l _ { 0 } = 5$ mm are adopted in the simulations. For each length scale, two different mesh sizes, i.e., a coarse one with $h = 0 . 5$ mm and a fine one with $h = 0 . 2 5$ mm, respectively, are considered. The numerically computed curves of the splitting force versus the CMOD (Crack Mouth Opening Displacement) are shown in Fig. 67. The numerical results given by various length scales and mesh sizes almost coincide, showing that the considered phase-field/gradient-damage model [Wu, 2017, 2018b] is insensitive to the length scale parameter and mesh size. This fact is in strong contrast to the standard one for brittle fracture. Though the peak load is somewhat underestimated, the overall global responses agree with the experimental results rather well. Moreover, the simulation leads to complete failure of the specimen with a vanishing load capacity. 

As the results given from both mesh sizes are un-distinguishable to each other, Fig. 68 only shows the damage profiles for the fine mesh. Consistently with that observed in the experimental test, a crack emerges from the notch tip and propagates downwards to the bottom edge of the specimen. As expected, the diffuse crack does localise within a localisation band of finite width that is characterised by the length scale parameter. This result is in strong contrast to some nonlocal or gradient-enhanced damage models in which the localisation band gets widened as shown in Fig. 17. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/b555fd59816d92f89e48d99fba098383b48cad3b73182e721fadf908911bb01c.jpg)



(a) Specimen (a) with $e _ { 1 } = 6$ inch and $e _ { 2 } = 1$ inch


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f1b5d24f69ecb328261d950ada18ebcf77947c1b612206c8664b47a295c3f400.jpg)



(b) Specimen (b) with $e _ { 1 } = 5 . 1 5$ inch and $e _ { 2 } = 1 . 5$ inch


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/caa61bad2519ad0c440694ebabb9f91f4e417f6af97a88af07094af50cf8a736.jpg)



(c) Specimen (c) with $e _ { 1 } = 4 . 7 5$ inch and $e _ { 2 } = 1 . 5$ inch



Figure 64: Asymmetrically notched beam under three-point bending: Comparison of the crack patterns (Left: experimentally observed crack patterns; Right: numerically predicted crack patterns).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/3e6cc700d377b6be262f3b9b7b0e4d7b9efeccbfe5f3da21915a7d3e57bd15f4.jpg)



(a) Problem description


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/de74a105caa1c12e5ca38f2ae3fd83a23d5645fb25ddba1eec5fa62694901071.jpg)



(b) XFEM


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f93d27179cc52383bf77409c813a2a9dcab8646d8ed69c205ceaa471d8c0960d.jpg)



Figure 65: Koyna dam under overflow pressure: the crack patterns predicted by XFEM and PF-CZM [Wu et al., 2018].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/ccc34312253024eedf9cdafac27a3ce9b39baaefb718286666ecd1751095c42f.jpg)



Figure 66: Wedge-splitting test: Geometry (unit of length: mm), boundary and loading conditions [Trunk, 2000].


## 7.2.2 L-shaped panel

The mixed-mode failure test of a L-shaped panel conducted by Winkler [2001] is then considered. The geometry, loading and boundary conditions of the specimen are shown in Fig. 69. The bottom edge of the specimen is fixed. A vertical point load $F ^ { * }$ is applied upward at a distance of 30 mm to the right edge of the horizontal leg, with the corresponding vertical displacement $u ^ { * }$ at the same place recorded. Note that the widely adopted failure criterion based on average stress gives spurious crack path with large noisy oscillation and random changes [Dumstorff and Meschke, 2007], the linear elastic fracture mechanics criterion in general has to be considered [Unger et al., 2007]. 

The material properties are: Young’s modulus $E _ { 0 } = 2 . 0 \times 1 0 ^ { 4 }$ MPa, Poisson’s ratio $\nu _ { 0 } = 0 . 1 8$ , the failure strength $f _ { t } ~ = ~ 2 . 5$ MPa and fracture energy $G _ { c } = 1 3 0 ~ \mathrm { J / m ^ { 2 } }$ [Unger et al., 2007]. In order to investigate the influences of the length scale parameter and of the mesh sizes, two different length scales, i.e., $l _ { 0 } = 1 0$ mm and $l _ { 0 } = 5$ mm, and two different mesh sizes, i.e., the coarse one with $h = 0 . 5$ mm and the fine one with $h = 0 . 2 5$ mm, respectively, are considered. 

As shown in Fig. 70, the numerical damage profiles are rather smooth and agree well with the experimentally observed crack patterns, with no additional tracking strategy. As expected, on the one hand, the mesh size h has little effects on the numerical damage profile, and on the other hand, the length scale $l _ { 0 }$ does affect the localisation bandwidth but does not affect the damage profile too much. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/097fda7fdff986a0431947a5fcb24cbb9642f2298d435cc1b4c87833e2cf0d2d.jpg)



Figure 67: Wedge-splitting test: Curves of splitting forces $F ^ { * }$ versus crack mouth opening displacement.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/aff7485c28b35722f61a59c0bd09130e797891873bc441c171838bc9a89a7dae.jpg)



(a) Damage profile for the length scale $l _ { 0 } = 1 0$ mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/46403033d826214663213d290e6c5db76990b696127edb7755f56905b8a52121.jpg)



(b) Damage profile for the length scale $l _ { 0 } = 5$ mm



Figure 68: Wedge-splitting test: Damage profiles for various length scale parameters.


Fig. 71 compare the numerical curves of load $F ^ { * }$ versus displacement $u ^ { * }$ for various mesh sizes and length scales. As can be seen, the numerical prediction is independent of mesh size and length scale $l _ { 0 } .$ , and all the global responses match the experimental peak loads and softening regimes fairly well. 

## 7.2.3 Mixed-mode failure of notched beams

Finally, let us consider a series of notched beam tests subjected to mixed-mode failure reported in Gálvez et al. [1998]. As depicted in Fig. 72, the specimen is of dimensions $6 7 5 \times 1 5 0 \times 5 0 \mathrm { m m ^ { 3 } }$ , with a vertical notch of sizes $2 \times 7 5 \times 5 0 \ : \mathrm { { m m ^ { 3 } } }$ at the bottom centre. In the first case, the stiffness at the upper left support is zero (i.e., three-point bending with $K = 0 )$ , whereas in the second one it is infinite (i.e., four-point bending with $K = \infty )$ . The load $F ^ { * }$ is applied under displacement control and the CMOD is monitored in both cases. 

The material properties are taken from Gálvez et al. [1998], i.e., Young’s modulus $E _ { 0 } = 3 . 8 \times 1 0 ^ { 4 }$ MPa, Poisson’s ratio $\nu _ { 0 } = 0 . 2$ , tensile strength $f _ { t } = 3 . 0 \mathrm { M P a }$ and fracture energy $G _ { c } = 0 . 0 6 9 \ : \mathrm { N / m m }$ . A single length scale $l _ { 0 } = 2 . 5$ mm is considered, with two different mesh sizes–the coarse one with $h = 0 . 5$ mm and the fine one with $h = 0 . 2 5$ mm. It is expected that the highly non-uniform damage field within the localisation band can be well resolved. 

The numerical damage profiles for both three- and four-point bending tests are shown in Fig. 73. As expected, for both tests the mesh size has no effect on the predicted damage profiles which capture the experimental crack rather well. Specifically, regarding the support condition at the upper left, the crack emerges from the notch tip and propagates with different skew angles (with respect to the beam axis) to the beam top. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/5c8bda1a84b782922de12c7175264cd2e496c953265dd71e9a790f6b8a70ea0f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7b545b911bf980f004ef0fafee86d29d52d519976191f96026c9f8ee5fe52e66.jpg)



Figure 69: L-shaped panel [Winkler, 2001]: Geometry, loading and boundary conditions (left; unit of length: mm); Crack paths (right).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/96c9c00c12d996900bab36822db02f054afc80723d93a364b9a71f8fef381e50.jpg)



(a) l<sub>0</sub> = 10 mm and h = 0.5 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/578ec0f5d80ec2c9276b173ebd35f73a37597dca5a50995d170811760025ee5f.jpg)



(b) l<sub>0</sub> = 10 mm and h = 0.25 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/56aa18984c7a33a8e82bf50d7b8494dff50797cc8d073edeefaabad6da93b458.jpg)



(c) $l _ { 0 } = 5$ mm and h = 0.5 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/80e3832d8f8b16658001f2056c53bba34d2f0e8ecea7bc811c1c8792f16003e5.jpg)



(d) $l _ { 0 } = 5$ mm and h = 02.5 mm



Figure 70: L-shaped panel: damage profiles for various length scale parameters $l _ { 0 }$ mm and mesh sizes h.


The calculated curves of load versus CMOD are depicted in Fig. 74. Though the ratio $l _ { 0 } / h$ varies, the numerical results obtained from both mesh sizes are very close to each other. For the three-point bending test, not only the peak loads but also the softening regimes match the test results rather well. For the four-point case, the concordance of numerical results with the experimental evidence is clear until a sudden collapse occurs at about $\mathrm { C M O D } = 0 . 1$ mm; see Cervera et al. [2010] for similar results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4748b91bab46500078976e35258fc3cb3c1934c7761ecb94daa93e957d53ffca.jpg)



(a) Length scale parameter $l _ { 0 }$ = 10 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/db97a5f36df128a949b4795de61be8e63d55cc6bdfd5b997731f9eb125bdcc5f.jpg)



(b) Length scale parameter $l _ { 0 }$ = 5 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/392fae32056ede4b4dd6000f2edee914aecb63bc4b4b253daed83470bc862f04.jpg)



(c) Coarse mesh $h = 0 . 5$ mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/0f691307aae1ffa04c7b4b7993e5edaca6dd7701ae44e8c17d7e01ee1782fad2.jpg)



(d) Fine mesh $h = 0 . 2 5$ mm



Figure 71: L-shaped panel: Curves of load versus displacement for various length scale parameters $l _ { 0 }$ and mesh sizes h.


## 7.3 Dynamic brittle fracture

In this section, two well-known dynamic fracture problems are considered to verify the performance of PFMs. The first is a dynamic crack branching test and the second is the Kalthoff-Winkler experiment which are benchmarks in the computational dynamic fracture literature. Unless otherwise stated, a plane strain condition is assumed for 2-D simulations. The Wu [2017] PFM and the staggered explicit solver presented in Section 5.4.2 are used. In this section, the length scale is denoted by b instead of $l _ { 0 }$ . In dynamic fracture the crack speed is well below the theoretical limiting speed [Ravi-Chandar, 2004] i.e., the so-called Rayleigh wave speed [Freund, 1998] 

$$
c _ {R} = \frac {0 . 8 6 2 + 1 . 1 4 \nu_ {0}}{1 + \nu_ {0}} c _ {s}, \qquad c _ {s} = \sqrt {\frac {\mu_ {0}}{\rho}},\tag{174}
$$

for the shear wave speed $c _ { s }$ . 

## 7.3.1 Dynamic crack branching

In this example, we consider a pre-cracked block loaded dynamically in tension. As shown in Figure 75, a uniform traction $\sigma _ { 0 }$ is applied at the top and bottom edges of the specimen as a step function in time. This problem has been widely adopted to study dynamic crack branching; see the experimental tests reported in Ramulu and Kobayashi [1985], Sharon and Fineberg [1996]. In the literature it has been numerically addressed by many authors using different methods such as XFEM, cohesive interface elements see e.g., Song et al. [2008], Park et al. [2012], Nguyen [2014b] and meshfree methods [Rabczuk and Belytschko, 2004]. In the phase-field community, this problem has been analysed by Borden et al. [2012], Schlüter et al. [2014] using the standard phase-field model $( \mathbf { i . e . , } \alpha ( d ) = d ^ { 2 } )$ and by Bleyer et al. [2017], Li et al. [2016] using the non-standard one $( \mathrm { i . e . , } \alpha ( d ) = d )$ , all for brittle fracture, i.e., $g ( d ) = \left( 1 - d \right) ^ { 2 }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f8b06b6892fbcffe34a377e6bc37e481a38d81270a9d288ae3e2d0715f365ae5.jpg)



Figure 72: Mixed-model failure test of notched beams [Gálvez et al., 1998]: Geometry (unit of length: mm), loading and boundary conditions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/6d546e85eaf2da66170d6c706d14cb1c817443848b3d57b1301604342d6abf52.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/ef7cce277e8a72164eb328b9d3e373732af17ae3d01b0c6918729f187b689f99.jpg)



Figure 73: Mixed-model failure test of notched beams: Damage profiles. Left column (three-point bending): Experimental crack pattern (top); Numerical damage profile for $l _ { 0 } = 2 . 5$ mm and $h = 0 . 5 0$ mm (middle); Numerical damage profile for $l _ { 0 } = 2 . 5$ mm and $h = 0 . 2 5$ mm (bottom). Right column (four-point bending): Experimental crack pattern (top); Numerical damage profile for $l _ { 0 } = 2 . 5$ mm and $h = 0 . 5 0$ mm (middle); Numerical damage profile for $l _ { 0 } = 2 . 5$ mm and $h = 0 . 2 5$ mm (bottom).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/eec1e67c3466b08d6d76f7ee5aa166e662ef5f4ce9bcf892d14c3822e47870c6.jpg)



(a) Three-point bending test (K = 0)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/705d41c07dfd0e7b9ce60bee6655e7e3042ca01270f92b32166d290c3cfad1d4.jpg)



(b) Four-point bending test (K = )



Figure 74: Mixed-model failure test of notched beams: Curves of load versus CMOD.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/095e584c81377327406b7849560280526d4de83bcd9b53c462afb9050d0a51f5.jpg)



Figure 75: Dynamic crack branching: geometry of the edge cracked block (left) and the loading history (right). Herein, $\sigma _ { 0 } = 1 . 0$ MPa is used. The notch has a width of 0.5 mm.


This example is herein numerically analysed using the unified PFM for cohesive fracture with linear softening. The material parameters used in the simulations are taken from Park et al. [2012]: Young’s modulus $E _ { 0 } = 3 . 2 \times 1 0 ^ { 4 }$ MPa, Poisson’s ratio of $\nu _ { 0 } = 0 . 2$ , the mass density of $\rho = 2 4 5 0 \mathrm { k g / m ^ { 3 } }$ , the failure strength $f _ { t } = 1 2  { \mathrm { M P a } }$ and the fracture energy $G _ { c } = 3 . 0 \ : \mathrm { J / m ^ { 2 } }$ , resulting in Griffith’s internal length $l _ { \mathrm { c h } } = 0 . 6 7$ mm and Rayleigh’s wave speed $c _ { R } = 2 1 1 9$ m/s. In order to investigate the influences of the length scale b and the mesh size h, the following three cases are considered: 

Case (a): b = 0.50 mm and $h = 0 . 1 0 \mathrm { m m } ( \mathrm { i . e . , } h = b / 5 )$ 

Case (b): b = 0.50 mm and $h = 0 . 0 5 \ : \mathrm { m m } ( \mathrm { i . e . , } h = b / 1 0 ) ;$ 

Case (c): b = 0.25 mm and $h = 0 . 0 5 \ : \mathrm { m m } \left( \mathrm { i . e . , } h = b / 5 \right) .$ 

The crack patterns at the end of the simulation $( t = 8 4 \times 1 0 ^ { - 6 } ~ \mathrm { s } )$ obtained with the above three cases are given in Figure 76. The crack propagates from the notch to the right with increasing speed. At a certain point, the crack branches into two cracks which agrees well with the experiment [Ramulu and Kobayashi, 1985]. The widening of the crack right before the moment of branching is similar to other phase-field simulations reported in Borden et al. [2012], Schlüter et al. [2014], to non-local integral damage model Pereira et al. [2017] and to peridynamics simulations [Ha and Bobaru, 2010]. This damage widening could be the signature of roughening of the crack surface experimentally observed to occur prior to branching [Ramulu and Kobayashi, 1985]. 

The global responses of the model are measured by the stored strain energy, dissipated surface energy and the crack tip velocity. The results are shown in Figure 77. Dynamic crack branching occurs around $3 6 . 5 \mu \mathrm { s }$ and the crack velocity never exceeds $0 . 6 v _ { R } .$ , which is in good agreement with the results given by other phase-field models [Borden et al., 2012, Schlüter et al., 2014]. 

In all of the three cases considered above, the crack localisation bandwidth is proportional to the incorporated length scale parameter b. However, the latter affects neither the crack pattern nor the global responses, and so does the mesh size: $h = b / 5$ is sufficient to resolve the damage field. This result further consolidates our previous findings that our model is insensitive to the length scale for static cohesive failure [Wu, 2017] and brittle fracture [Wu and Nguyen, 2018]. It is also the case for dynamic fracture. This allows us to select a small value for b to have Γ-convergence to sharp cracks. 

In order to test whether the proposed phase-field damage model can capture multiple crack branches, we reconsider Case (b) i.e., $b = 0 . 2 5$ mm and $h = 0 . 0 5$ mm but with $\sigma _ { 0 } = 2 . 5 \mathrm { M P a }$ . The result given in 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/05c37f5db60762220551b835452be0d8c0e7a6a74cc466bb8888469bc9a35948.jpg)



(a) b = 0.5 mm and h = 0.10 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7ed7e87504dfe3a0fbbce938832382cb3cb730b0793d7ebe2774df51ee440195.jpg)



(b) b = 0.5 mm and h = 0.05 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/dc8cd870fcfda5c51f7f84e3e55a383aa7c5d1216b9859dcc3d5b3afd8085d29.jpg)



(c) b = 0.25 mm and h = 0.05 mm



Figure 76: Dynamic crack branching: Numerical crack patterns at time 84 $\mu \mathbf { s } .$


Fig. 78 shows that crack branching happens sooner than $\sigma _ { 0 } = 1 . 0 \mathrm { M P a }$ , the crack angle is also smaller and there are multiple branches. All these are in good agreement with findings reported in Ha and Bobaru [2010], Pereira et al. [2017] using other methods. The crack patterns at various instants are shown in Fig. 79. As can be seen, the evolution of multiple crack branches can be seamlessly captured by the proposed phase-field damage model. There exists damage widening prior to branching events for later branches. Similar results were presented in Ha and Bobaru [2010] with a peridynamics model. 

## 7.3.2 Edge-cracked plate under impulsive loading

This section studies a doubly notched specimen under an impact load, which is often referred to as the Kalthoff-Winkler experiment. The geometry of the specimen is shown in Figure 80, and the impact loading is applied by a projectile. In the experiment [Kalthoff and Winkler, 1987], two different failure modes were observed by modifying the projectile speed, $v _ { 0 } ;$ at high impact velocities, a shear band is observed to emanate from the notch at an angle of $1 0 ^ { \mathrm { o } }$ with respect to the initial notch and at lower strain rates $( v _ { 0 } = 1 6 . 5 4 \mathrm { m / s } )$ , brittle failure with a crack propagation angle of about $7 0 ^ { \mathrm { { o } } }$ is observed. We are interested only in the velocity range that resulted in a brittle failure mode. The simulations of this problem have been reported by several researchers, see e.g., Song et al. [2008], Rabczuk and Belytschko [2004], Park et al. [2012], Nguyen [2014b] using different methods such as XFEM, adaptive cohesive interface elements and meshfree methods. In the phase-field community this problem has been analysed by Borden et al. [2012], Schlüter et al. [2014], Hofacker and Miehe [2012, 2013], Li et al. [2016]. 

The material parameters of Maraging steel 18Ni(300), which are taken from Park et al. [2012], are as follows: Young’s modulus $E _ { 0 } = 1 . 9 \times 1 0 ^ { 5 }$ MPa, Poisson’s ratio $\nu _ { 0 } = 0 . 3$ , the mass density $\rho = 8 0 0 0$ $\mathrm { k g / m ^ { 3 } }$ , the failure strength $f _ { t } = 2 8 1 2 . 2 5$ MPa and the fracture energy $G _ { c } = 2 2 . 2$ N/mm, resulting in Griffith’s internal length $l _ { \mathrm { c h } } = 0 . 5 3$ mm. The Rayleigh wave speed is $c _ { R } = 2 7 4 5 ~ \mathrm { m / s }$ . Two cases are considered to study the sensitivity of the results with respect to b: 

$b = 0 . 5 0$ mm and h = 0.10 mm; 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/22e8df97e49547b1e98f5b9968ae7121f875e45acdb7419c66b64472a288d212.jpg)



(a) Stored strain energy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/0b94aa97ac31747156a68c59e2380b66a9f2da956c48200f8adc3c14312d558f.jpg)



(b) Dissipated surface energy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/0f93fa9ceec3eef548fece58048a61e6b2fb9c82e4a97a0227d9a30aee791945.jpg)



(c) Crack tip velocity



Figure 77: Dynamic crack branching: Strain energy, surface energy and crack tip velocities in time.


$b = 0 . 2 5$ mm and $h = 0 . 0 5 \ : \mathrm { m m }$ 

Due to symmetry only the upper half was modeled at the impact velocity $v _ { 0 } = 1 6 . 5 4 \mathrm { m } / \mathrm { s }$ 

The notch is introduced in the mesh a a geometry discontinuity following Li et al. [2016] as phase-field induced crack did not result in crack initiation correctly. The crack pattern is shown in Figure 81 which agrees with available findings Borden et al. [2012], Li et al. [2016]. Initially the crack starts to grow at a larger angle (about $7 0 ^ { \mathrm { { o } } } )$ then the angle decreases as the crack grows. The average angle from the initial crack tip to the point where the crack intersects the top boundary is about $6 8 ^ { \mathrm { o } }$ and in fairly good agreement with the experimental result. The global responses of the model are measured by the stored strain energy, dissipated surface energy and the crack tip velocity. The results are shown in Figure 82. Again, the responses are independent with respect to the length scale and the mesh sizes. The final crack length, Figure 82d, is about 102 mm and the surface energy is 2460 J. If we assume that the crack is straight, then with the angle of $6 8 ^ { o }$ , its length would be 81 mm and its surface energy would be 1796 J. Our value is about 37% higher, but is significantly better than the value reported in Borden et al. [2012] (90% over-estimated) who used a phase-field model without an elastic regime. 

Next we use a larger impact velocity $v _ { 0 } = 1 0 0$ m/s [Li et al., 2016], and successive crack branching can be observed from Figure 83. Again, there exists damage widening prior to all branching events. This result is with $b = 0 . 2 5$ mm and $h = 0 . 0 5$ mm; the mesh consists of about two million nodes and four million elements. Note that large elements are used at the lower right corner (to reduce computational cost) and thus large damage bands occur at this region. Similar findings are reported in Li et al. [2016], Hofacker and Miehe [2012, 2013]. So, with sufficiently refined meshes, phase-field models can capture multiple dynamic crack branchings quite straightforwardly. Indeed, PFM was successfully used to model dynamic crack instability problem where there are many very small cracks along a major dominant one [Bleyer and Molinari, 2017]. Note that the resulting crack patterns are sensitive to the tension-compression split model [Li et al., 2016]. We recall that in the experiment a failure-mode transition from mode-I to mode-II was observed when the impact velocity increases. This cannot be captured using an elastic-damage model [Li et al., 2016]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/b3bd2f25d7de0707c6e42713a9b45cd1e404b8ec73b8fc39e04d7d587a598ba9.jpg)



Figure 78: Dynamic crack branching: influence of the load intensity. The higher the load amplitude the more branches are present. Crack branching also happens sooner and the crack angle (of the first branch) is smaller.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/52d6b297f1831c1a9c8c575ea68fdbf63ea8cd34c5da728822326b569e0ecaf9.jpg)



(a) t = 25.1µs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/be2e7770506dcac6c7206db3467645efbea7c78d738006eb3b57d757fd1c6a7a.jpg)



(b) t = 40.2µs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/ff7a9d2cfdc99d9a6484216c849d59e01ce5e6fc383a3fb8c044ff6475482bb8.jpg)



(c) t = 47.7µs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/d0deb012ea1b449e8c651a714833890d80c9ffcf0ef51a4e6fbd9ff84514bbbe.jpg)



(d) t = 61.9µs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f670bb4ebe6be1413423aa47de259ff4d8f49ec9c5e84beb3f753fea0904206b.jpg)



(e) t = 84.0µs



Figure 79: Dynamic crack branching: Crack patterns at various instants for the traction $\sigma _ { 0 } = 2 . 5 \mathrm { M P a }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/08d279cdfbc2e11d79dd6bc4e5ba8d15be43cec3b3d13b7a4eb24930e38a34a3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/cf50ddb2b60b62855c1b93d990b780a8cd78d1dd12cd23641df2ce4366d198be.jpg)



Figure 80: Edge-cracked plate under impulsive loading.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/e6688e12561c2c8175bb9875bf81f579e906e2c785406b4644dde519c761563b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/f1989689f7b68635a6dc3aa0808b378b874ccc6a7ebdc8fdccc55a525b49b0e1.jpg)



Figure 81: Edge-cracked plate under impulsive loading: Numerical crack patterns at time 90 $\mu \mathbf { s } .$ . Left $( b = 0 . 5 0$ mm and $h = 0 . 1 0$ mm) and right $( b = 0 . 2 5$ mm and $h = 0 . 0 5$ mm).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/44aa1c5bd3be964a5558a757f30fd6385d3fc3a934a20c27b67afc8a4f918b6d.jpg)



(a) Stored strain energy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/7af582c731b5e26965110ec45f1ef6f8b79fae50572b4b12c8d95ac125eae67e.jpg)



(b) Dissipated surface energy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/3dbebbb2f01e8b61096b07cfe4eab5e54a5cbcead3520f299a77289278230902.jpg)



(c) Crack tip velocity


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/8b1b278dd4fd05b3e4f2de890e57bfff23d883444892b1836c2a165fb5f0984f.jpg)



(d) Crack length



Figure 82: Edge-cracked plate under impulsive loading: Strain energy, surface energy, crack tip velocity and crack length.


## 8 Conclusions

This manuscript comes to an end and we provide a summary in Section 8.1. Issues identified while we have been experimenting with phase-field models are presented in Section 8.2 and anticipated future works are discussed in Section 8.3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/5cf2a52dfbc8be1ea65bae7f43d654025035aa281329bab71f1dff663786fae9.jpg)



(a) t = 40 µs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/56a2d641a02bd0b704a9a814118d812a9d675cc77f13bdcaf609563d7acfb5da.jpg)



(b) t = 53 µs



Figure 83: Edge-cracked plate under impulsive loading with a large impact velocity of 100 m/s: Numerical crack patterns


## 8.1 Summary

There is a plethora of fracture/damage mechanics theories and corresponding computational methods. One likely reason for this is the fact that no theory/method stands out from the remaining ones as fracture is a very complex phenomenon that involves multiple spatial and temporal scales. In fact, fracture remains a challenging problem, and new methods continue to arise, for example quantised fracture mechanics developed by Pugno and Ruoff [2004]. 

In the context of continuum mechanics and the finite element (FE) method, this manuscript attempted to give an overall picture of existing fracture/damage models and the associated computational methods with a particular emphasis on the variational approach to fracture or the phase-field (PF) fracture/damage theory. A comprehensive review of the literature on various PF models (PFMs) applicable to brittle, quasi-brittle and ductile fracture under static and dynamic loading regimes was presented. Within a unified framework of phase-field models for both brittle and quasi-brittle fracture, theoretical aspects (generic crack surface density function, various energetic degradation functions, different anisotropic tension/compression splits, crack driving forces and 1-D analytical solutions) and computational aspects (FE discretisation, monolithic and staggered solvers for both static and dynamic problems, existing computer codes, strategies in handling initial cracks) were discussed in great detail. Our discussion is based on an extensive set of numerical examples, conducted by the authors themselves using in-house FE codes, covering both brittle/cohesive fracture under quasi-static and dynamic loadings. A comparison between PFMs and gradient-enhanced damage models and gradient-damage models was given with the hope that it could lift the misunderstanding that a PF model is just a gradient damage model. And lastly, a preliminary study on the comparison between extended finite elements and PFMs was carried out for a multiple crack growth problem in a brittle solid. This problem reveals the strengths and weaknesses of these two models–XFEM is computationally efficient (yet the implementation is much more involved) whereas PFM is computationally demanding (yet the implementation is simpler, the transition from 2-D to 3-D is also less abrupt implementation wise). We refer to Wu et al. [2018] for a numerical comparison between PFM and XFEM for cohesive fracture problems. 

Based on our experience with many different fracture/damage theories and the literature survey presented in this manuscript, we believe that the key advantages of PFMs are at least four-fold: (i) crack nucleation, growth, branching and merging are automatically handled even in three dimensions (3-D), (ii) the variational structure of these models allows to study multiple physics fracture problems, and (iii) straightforward computer implementation in any dimensions. The latter allows researchers to focus on the physics rather on the computer implementations. 

One particular attribute of PFMs is that they require a minimal set of parameters, i.e., Young’s modulus, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/3719c32a22f3cfcc9be3bffcd85e3e8f9c4d64c2b0f7d60cc5f28206db2667d3.jpg)


Poisson’s ratio, the fracture energy (which are all experimentally measurable) and the length scale $l _ { 0 }$ (which can be determined based on the tensile strength of the material under consideration) for brittle materials. The Wu [2017, 2018b] PF-CZM, for quasi-brittle materials, demands one additional input – a target softening curve based on which the other involved material parameters are determined. In other words, PFMs do not rely on ad hoc user-defined parameters. Another reason to the popularity of this class of models is that phase-fields have been a well accepted concept in physics for decades, albeit with different flavours. 

The main drawback about PFMs is probably their high computational cost. Our view on this point is twofold. First, it is obvious that problems that were intractable decades ago are now solved routinely. Second, PFMs seem to be the only tool (within the framework of classical continuum mechanics) that can analyse complex 3-D crack problems using relatively standard finite element methods. Advancements in computer hardware and computing technologies (anisotropic mesh adaptivity, global/local methods, multi-scale methods, model order reduction methods) will definitely increase the efficiency of PF simulations. 

Based on our literature review, phase-field fracture/damage models have found successful applications in the following areas 

Static and dynamic fracture of brittle materials, both in 2-D and 3-D; 

Static and dynamic fracture of ductile materials, both in 2-D and 3-D; 

Static fracture of quasi-brittle materials in 2-D; 

Multi-field fracture: thermo-elastic-plastic materials, hydraulic fractures, piezzoelectric and ferroelectric materials etc. 

However, applications of PF models to the cracking of composite materials are very scarce; Carollo et al. [2017] presented a computational framework to simulate interlayer (with cohesive interface elements) and intralayer crack propagation (with the standard PFM) in composite structures. PF modelling of dynamic fracture of quasi-brittle materials (e.g., concretes) was presented in Nguyen and Wu [2018] but rate effects have not been considered. 

## 8.2 Issues

While solving some static fracture problems, we met several issues which deserves more investigations. Firstly, for the standard PFM with $\alpha ( \phi ) = \phi ^ { 2 }$ and $g ( \phi ) = ( 1 - \phi ) ^ { 2 }$ we observed damage widening when the cracks come close to external boundaries, cf. Fig. 84. This issue might be due to the infinite support of this model, but further studies are needed to clarify this problem. 


Figure 84: Damage widening close to boundaries.


Secondly, for problems with holes, we did not obtain crack paths in agreement with LEFM based results reported in the literature. Moreover, the crack pattern depends on the utilised phase-field model, cf. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/af0079ae390d885cdfb60f558575cdd9a517d77906045cfe5027ba261b542b6a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/fe8c3cdd29c1149db974b986e97b68c758678c3855054f7bc85b79cae8346c15.jpg)



(a) standard PFM with no damage prevention around the (b) standard PFM with no damage around the hole perimeter holes


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/19dd3f4f-c0b8-4fea-b204-7fffc80ecc7a/4209986464fc918b8d938c14089ef72469340b6b7c06928212019badf4eb0650.jpg)



(c) PFM with $\alpha = 2 \phi - \phi ^ { 2 }$ and $g = ( 1 - \phi ) ^ { 2 }$



Figure 85: Pre-cracked sample with two holes.


Fig. 85. We believe that further studies are needed to assess the performance of PFMs for problems with holes or inclusions. 

Thirdly, for fast crack propagation under dynamic loading, it was found that the crack band widens due to the finite relaxation time for stresses in elastodynamics [Agrawal and Dayal, 2017], resulting in crack velocity dependent overestimation of the fracture energy dissipation. 

## 8.3 Future work and perspectives

Despite the large volume of references and noteworthy recent contributions, the theoretical and numerical aspects of PFMs are still open issues, which include but are not limited to the following: 

the variational approach to fatigue fracture and its phase-field regularised counterpart; see Bourdin et al. [2008b], Alessi et al. [2018b]; 

the phase-field modelling of micro inertia induced rate effects and fast crack propagation under dynamics loading; 

the stochastic phase-field theory accounting for randomly distributed coefficients and noises; 

novel numerical implementations greatly increasing the robustness and computational efficiency such as model order reduction [Kerfriden et al., 2013], goal-oriented error-driven mesh adaption, symplectic time integrators [Kane et al., 1999] etc. 

Last but not the least, we believe that there is a need to assess the performance of PFMs in problems which involve extreme events such as 

failure of brittle and quasi-brittle materials subjected to impact and/or blast loadings; 

failure of brittle and quasi-brittle materials due to environmentally assisted fracture; 

failure of composite materials caused by both interlayer and intralayer crack propagation. 

which brought us to the paper of Moutsanidis et al. [2018] where a computational framework for simulating extreme events involving dynamic brittle fracture of materials subjected to blast loading using PFMs was proposed. 

## Acknowledgments

Funding support from the National Natural Science Foundation of China (51678246) to the first author (J.Y. Wu) and from the Australian Research Council via DECRA project (DE160100577) to the second author (V.P. Nguyen) is gratefully acknowledged. Support of Dr. Joris Remmers at TU Eindhoven, the Netherlands, by sending us his routines for writing parallel VTU files is appreciated. The authors would like to express the gratitude towards Dr. Erik Jan Lingen at the Dynaflow Research Group, Houtsingel 95, 2719 EB Zoetermeer, the Netherlands for providing support on the numerical toolkit JIVE. Dr Stefan May at inuTech (Nuremberg) is acknowledged for providing us his phase-field code. 

## A A brief recount on variational calculus

Calculus of variations, or variational calculus, is a sort of generalisation of the calculus that we know. The goal of variational calculus is to find the curve or surface that minimises (or maximises) a given function. This function is usually a function of other functions and is called a functional. Functionals are often expressed as definite integrals involving functions and their derivatives. The calculus of variations extends the ideas of maxima and minima of functions to functionals. As an example, one can counts the Eucledian geodesic problem: Finding the shortest path joining two points $( x _ { 1 } , y _ { 1 } )$ and $( x _ { 2 } , y _ { 2 } )$ . To this end, we are finding a function $f ( x )$ such that the following integral 

$$
l = \int_ {(x _ {1}, y _ {1})} ^ {(x _ {2}, y _ {2})} \mathrm{d} s = \int_ {x _ {1}} ^ {x _ {2}} \sqrt {1 + (f ^ {\prime} (x)) ^ {2}} \mathrm{d} x\tag{175}
$$

is minimum. 

In what follows we present the calculation of the first variation of the following functional 

$$
\varPsi_ {c} = \int_ {\mathcal {B}} G _ {c} \frac {1}{c _ {0}} \left[ \frac {1}{l _ {0}} \alpha (\phi) + l _ {0} \nabla \phi \cdot \nabla \phi \right] \mathrm{d} V\tag{176}
$$

which is the surface energy in the phase-field fracture model. To this end, we simply use the definition of the first variation of a functional as the Gateaux derivative i.e., 

$$
\delta \varPsi_ {c} = \frac {\mathrm{d}}{\mathrm{d} \epsilon} \varPsi_ {c} (\phi + \epsilon \delta \phi) \bigg | _ {\epsilon = 0}\tag{177}
$$

which results in 

$$
\begin{array}{l} \delta \Psi_ {c} = \frac {\mathrm{d}}{\mathrm{d} \epsilon} \int_ {\mathcal {B}} G _ {c} \frac {1}{c _ {0}} \left(\frac {\mathrm{d}}{\mathrm{d} \epsilon} \left[ \frac {1}{l _ {0}} \alpha (\phi + \epsilon \delta \phi) + l _ {0} \nabla (\phi + \epsilon \delta \phi) \cdot \nabla (\phi + \epsilon \delta \phi) \right]\right) _ {\epsilon} \mathrm{d} V \\ = \int_ {\mathcal {B}} G _ {c} \frac {1}{c _ {0}} \left[ \frac {1}{l _ {0}} \alpha^ {\prime} (\phi) \delta \phi + 2 l _ {0} \nabla \phi \cdot \nabla \delta \phi \right] \mathrm{d} V \end{array}\tag{178}
$$

In order to derive the Euler-Lagrange equation associated with $\delta \varPsi _ { c } = 0 \mathrm { i . e . }$ ., the evolution equation for the phase-field (with a null right hand side) and the associated Neumann boundary conditions, the term $\delta \varPsi _ { c }$ is elaborated as follows 

$$
\begin{array}{r l} & {\delta \varPsi_ {c} = \int_ {\mathcal {B}} G _ {c} \frac {1}{c _ {0}} \left[ \frac {1}{l _ {0}} \alpha^ {\prime} (\phi) \delta \phi + 2 l _ {0} \nabla \phi \cdot \nabla \delta \phi \right] \mathrm{d} V} \\ & {\quad = \int_ {\mathcal {B}} G _ {c} \frac {1}{c _ {0}} \left[ \frac {1}{l _ {0}} \alpha^ {\prime} (\phi) - 2 l _ {0} \Delta \phi \right] \delta \phi \mathrm{d} V + \int_ {\partial \mathcal {B}} \frac {2}{c _ {0}} G _ {c} l _ {0} (\nabla \phi \cdot \pmb {n} _ {\mathcal {B}}) \delta \phi \mathrm{d} A} \end{array}\tag{179}
$$

where the divergence theorem was used. In the above, $_ { \pmb { n } _ { B } }$ denotes the outward unit normal of the boundary ∂ . Using the fundamental lemma of variational calculus, from condition $\delta { \psi } _ { c } = 0$ one obtains the damage evolution equation and the corresponding Neumann boundary condition. 

## B Positive/negative projection and its application to phase-field fracture models

In the modelling of asymmetric tensile/compressive behavior and microcracks closure-reopening (MCR) effects exhibited by quasi-brittle solids, the positive/negative decomposition of a specified second-order symmetric tensor e.g., the strain , stress σ and effective stress $\bar { \pmb { \sigma } } ,$ , etc., is frequently adopted through the so-called projection operators. As clarified by Wu and Xu [2013], Wu and Cervera [2018] the positive/neg ative projection (PNP) is not unique and several alternatives have been proposed in the literature. In this appendix, two of them are presented to illustrate the application to PFMs. 

## B.1 General definition of the positive/negative projection

Let us consider the following spectral decomposition of the specified second-order tensor A 

$$
\boldsymbol {A} = \sum_ {n = 1} ^ {3} A _ {n} \boldsymbol {p} _ {n} \otimes \boldsymbol {p} _ {n} = \boldsymbol {A} ^ {+} + \boldsymbol {A} ^ {-},\tag{180}
$$

for the eigenvalues $A _ { n } = P _ { n n } : A = p _ { n } \cdot A \cdot p _ { n }$ and the associated eigenvectors ${ \pmb p } _ { n } ,$ , respectively, with the latter defining the second-order symmetric tensor $P _ { n n } : = p _ { n } \otimes p _ { n }$ . Note that the subscript n does not refer to the dummy index of a tensor (or vector), but rather, it represents the quantity associated with the n-th principal value. 

In Equation (180) the positive/negative components $A ^ { \pm }$ are coaxial to the parent tensor A. Without loss of generality, they are expressed as 

$$
\boldsymbol {A} ^ {+} = \sum_ {n} A _ {n} ^ {+} \boldsymbol {P} _ {n n} = \mathbb {P} ^ {+}: \boldsymbol {A}, \quad \boldsymbol {A} ^ {-} = \boldsymbol {A} - \boldsymbol {A} ^ {+} = \sum_ {n} A _ {n} ^ {-} \boldsymbol {P} _ {n n} = \mathbb {P} ^ {-}: \boldsymbol {A}\tag{181}
$$

where $A _ { n } ^ { + } = P _ { n n } ^ { + } : A \geq 0$ and $A _ { n } ^ { - } : = A _ { n } - A _ { n } ^ { + } = P _ { n n } ^ { - } : A \leq 0$ are the principal values of the positive component $A ^ { + }$ and the negative one A−, respectively; the fourth-order projection operators $\mathbb { P } ^ { \pm }$ are given by 

$$
\mathbb {P} ^ {+} = \sum_ {n} \boldsymbol {P} _ {n n} \otimes \boldsymbol {P} _ {n n} ^ {\pm}, \qquad \mathbb {P} ^ {-} = \mathbb {I} - \mathbb {P} ^ {+}\tag{182}
$$

with the second-order symmetric tensors $P _ { n n } ^ { \pm }$ dependent on the adopted PNP scheme. Note that the projection operators satisfy the idempotent property i.e., 

$$
\mathbb {P} ^ {\pm}: \mathbb {P} ^ {\pm}: \boldsymbol {A} = \mathbb {P} ^ {\pm}: \boldsymbol {A} ^ {\pm} = \boldsymbol {A} ^ {\pm} \quad \Longrightarrow \quad \mathbb {P} ^ {+}: \boldsymbol {A} ^ {-} = \mathbb {P} ^ {-}: \boldsymbol {A} ^ {+} = 0\tag{183}
$$

That is, the positive/negative decomposition is an orthogonal projection. Furthermore, it also follows that 

$$
\frac {\mathrm{d} \boldsymbol {A} ^ {\pm}}{\mathrm{d} \boldsymbol {A}} = \mathbb {Q} ^ {\pm}\tag{184}
$$

where the fourth-order tensor $\mathbb { Q } ^ { \pm }$ are expressed as [Wu and Xu, 2013] 

$$
\mathbb {Q} ^ {+} = \mathbb {P} ^ {+} + 2 \sum_ {n} \sum_ {m > n} \frac {A _ {n} ^ {+} - A _ {m} ^ {+}}{A _ {n} - A _ {m}} \boldsymbol {P} _ {n m} \otimes \boldsymbol {P} _ {n m}, \quad \mathbb {Q} ^ {-} = \mathbb {I} - \mathbb {Q} ^ {+}\tag{185}
$$

for the second-order symmetric tensor $\pmb { P } _ { n m } = \left( \pmb { p } _ { n } \otimes \pmb { p } _ { m } \right) ^ { \mathrm { s } }$ . Owing to the orthogonal property $P _ { n m } : A = 0$ for $m \neq n$ , the following identities hold 

$$
\mathbb {Q} ^ {\pm}: \boldsymbol {A} = \mathbb {P} ^ {\pm}: \boldsymbol {A} = \boldsymbol {A} ^ {\pm}, \quad \dot {\mathbb {Q}} ^ {\pm}: \boldsymbol {A} = \dot {\boldsymbol {A}} ^ {\pm} - \mathbb {Q} ^ {\pm}: \dot {\boldsymbol {A}} = \boldsymbol {0}\tag{186}
$$

That is, the fourth-order tensors $\mathbb { Q } ^ { \pm }$ extract the same positive/negative components $A ^ { \pm }$ as the irreducible PNP operators $\mathbb { P } ^ { \pm }$ do. In the following, the classical positive/negative projection and the novel one are briefly introduced. 

## B.2 Miehe’s strain energy decomposition

In the PF model proposed by Miehe et al. [2010b], the PNP of the strain tensor  is adopted such that the orthogonal condition $\epsilon ^ { + } : \epsilon ^ { - } = 0$ in the Frebrius norm holds for the positive/negative strains $\epsilon ^ { \pm }$ . This extra orthogonal condition results in the decomposition (74) which recovers the classical PNP scheme [Ortiz, 1985]. 

For the positive strain $\epsilon ^ { + }$ given in Equation (74), it follows that 

$$
\begin{array}{l} \frac {\partial \psi_ {0} ^ {+}}{\partial \epsilon} = \lambda_ {0} \langle \operatorname{tr} (\epsilon) \rangle \frac {\partial \langle \operatorname{tr} (\epsilon) \rangle}{\partial \epsilon} + \mu_ {0} \frac {\partial (\epsilon^ {+} : \epsilon^ {+})}{\partial \epsilon} \\ = \lambda_ {0} \langle \operatorname{tr} (\epsilon) \rangle H (\operatorname{tr} (\epsilon)) 1 + 2 \mu_ {0} \epsilon^ {+} = \lambda_ {0} \langle \operatorname{tr} (\epsilon) \rangle 1 + 2 \mu_ {0} \epsilon^ {+} \end{array}\tag{187}
$$

where the following relation has been considered 

$$
\frac {\partial \left(\boldsymbol {\epsilon} ^ {+} : \boldsymbol {\epsilon} ^ {+}\right)}{\partial \boldsymbol {\epsilon}} = 2 \left(\frac {\partial \boldsymbol {\epsilon} ^ {+}}{\partial \boldsymbol {\epsilon}}: \boldsymbol {\epsilon} ^ {+}\right) = 2 \left(\mathbb {Q} ^ {+}: \boldsymbol {\epsilon} ^ {+}\right) = 2 \boldsymbol {\epsilon} ^ {+}\tag{188}
$$

Similarly, it follows that 

$$
\frac {\partial \psi_ {0} ^ {-}}{\partial \epsilon} = - \lambda_ {0} \langle - \mathrm{tr} (\epsilon) \rangle {\bf 1} + 2 \mu_ {0} \epsilon^ {-}\tag{189}
$$

Accordingly, the stress tensor σ is evaluated as in Equation (76). 

## B.3 Wu and Cervera’s strain energy decomposition

In the PFM proposed in Wu and Nguyen [2018] the PNP of the effective stress tensor is considered such that the orthogonal condition given in Equation (77) is fulfilled [Wu and Cervera, 2018]. One of the advantage is that it ensues a minimal positive initial HFE potential which is consistent with the variational interpretation of PFMs. 

For the positive/negative effective stresses $\bar { \pmb { \sigma } } ^ { \pm }$ , it follows that 

$$
\frac {\partial \psi_ {0} ^ {\pm}}{\partial \pmb {\epsilon}} = \frac {\partial \psi_ {0} ^ {\pm}}{\partial \bar {\pmb {\sigma}}}: \mathbb {E} _ {0} = \mathbb {Q} ^ {\pm}: \frac {\partial \psi_ {0} ^ {\pm}}{\partial \bar {\pmb {\sigma}} ^ {+}}: \mathbb {E} _ {0} = \mathbb {Q} ^ {\pm}: \bar {\pmb {\sigma}} ^ {\pm} = \bar {\pmb {\sigma}} ^ {\pm}\tag{190}
$$

such that the stress tensor is given in Equation (81). 

## C Thermodynamics

There exists derivations of the governing equations of a phase-field fracture model based on the microforces concept, see e.g., Wilson et al. [2013], Borden et al. [2016]. We find that the introduction of microforces is unnecessary and misleading, since the Neumann boundary condition for the phase-field cannot be obtained. Therefore, in what follows we consider the standard thermodynamics. 

Let us consider a domain Ω having the boundary $\partial \varOmega$ with n being the outward unit normal vector. A localisation band $B \subseteq { \mathcal { Q } }$ is contained in the domain $\varOmega ,$ , with the outward unit normal of the boundary $\partial B$ denoted by $_ { n _ { B } }$ . The derivation is based on the principle of virtual powers. To this end, we define the external power $\mathcal { W }$ and the internal power $\mathcal { I }$ in what follows 

$$
\mathcal {W} (\tilde {\boldsymbol {v}}) = \int_ {\Omega} \boldsymbol {b} ^ {*} \cdot \tilde {\boldsymbol {v}} \mathrm{d} V + \int_ {\partial \Omega} \boldsymbol {t} ^ {*} \cdot \tilde {\boldsymbol {v}} \mathrm{d} A\tag{191a}
$$

$$
\mathcal {I} (\tilde {\boldsymbol {v}}, \tilde {\phi}) = \int_ {\Omega} \boldsymbol {\sigma}: \nabla^ {\mathrm{s}} \tilde {\boldsymbol {v}} \mathrm{d} V\tag{191b}
$$

where $b ^ { * }$ and $\pmb { t } ^ { * }$ denote the macroscopic body force and boundary tractions, respectively. 

To get the macroscopic balance equation, one chooses a virtual fields with $\tilde { \phi } = 0$ , the principle of virtual power yields the following equation 

$$
\int_ {\Omega} \boldsymbol {b} ^ {*} \cdot \tilde {\boldsymbol {v}} \mathrm{d} V + \int_ {\partial \Omega} \boldsymbol {t} ^ {*} \cdot \tilde {\boldsymbol {v}} \mathrm{d} A = \int_ {\Omega} \boldsymbol {\sigma}: \nabla \tilde {\boldsymbol {v}} \mathrm{d} V\tag{192}
$$

from which, upon standard calculations<sup>26</sup>, results in the balance of linear momentum equation and the Cauchy equation 

$$
\nabla \cdot \boldsymbol {\sigma} + \boldsymbol {b} ^ {*} = 0, \quad \boldsymbol {\sigma} \cdot \boldsymbol {n} = \boldsymbol {t} ^ {*}\tag{193}
$$

To proceed, we use the second law of thermodynamics that reads 

$$
\mathcal {W} (\dot {\boldsymbol {u}}) - \dot {\varPsi} (\dot {\boldsymbol {u}}, \dot {\phi}) \geq 0\tag{194}
$$

where the free energy potential is expressed as 

$$
\Psi (\boldsymbol {u}, \phi) = \int_ {\Omega} \psi (\boldsymbol {\epsilon}, \phi) \mathrm{d} V + \int_ {\mathcal {B}} G _ {c} \gamma (\phi ; \nabla \phi) \mathrm{d} V\tag{195}
$$

with the following time derivative 

$$
\dot {\Psi} = \int_ {\Omega} \frac {\partial \psi}{\partial \epsilon}: \dot {\epsilon} \mathrm{d} V + \int_ {\mathcal {B}} \left[ \left(\frac {\partial \psi}{\partial \phi} + G _ {c} \frac {\partial \gamma}{\partial \phi}\right) \dot {\phi} + G _ {c} \frac {\partial \gamma}{\partial \nabla \phi} \cdot \nabla \dot {\phi} \right] \mathrm{d} V\tag{196}
$$

Upon introduction of this into Equation (194), one arrives at 

$$
\int_ {\Omega} \left(\pmb {\sigma} - \frac {\partial \psi}{\partial \pmb {\epsilon}}\right): \dot {\pmb {\epsilon}} \mathrm{d} V + \int_ {\mathcal {B}} \left[ \left(- \frac {\partial \psi}{\partial \phi} - G _ {c} \frac {\partial \gamma}{\partial \phi}\right) \dot {\phi} - \left(G _ {c} \frac {\partial \gamma}{\partial \nabla \phi}\right) \cdot \nabla \dot {\phi} \right] \mathrm{d} V \geq 0\tag{197}
$$

With the generic assumption that the strain rate $\dot { \epsilon }$ can have arbitrarily prescribed values and is independent of the rate of the phase-field $\phi ,$ Equation (197) immediately yields the constitutive relation for the mechanical stresses 

$$
\pmb {\sigma} = \frac {\partial \psi}{\partial \pmb {\epsilon}}\tag{198}
$$

And thus, Equation (197) is simplified to 

$$
- \int_ {\mathcal {B}} \left[ \left(\frac {\partial \psi}{\partial \phi} + G _ {c} \frac {\partial \gamma}{\partial \phi}\right) \dot {\phi} + \left(G _ {c} \frac {\partial \gamma}{\partial \nabla \phi}\right) \cdot \nabla \dot {\phi} \right] \mathrm{d} V \geq 0\tag{199}
$$

$\mathbf { A } \mathbf { s } \ { \dot { \phi } }$ and $\nabla \dot { \phi }$ are not independent, one cannot apply the fundamental lemma of variational calculus to the above equation. Therefore, the divergence theorem is used in the second term to arrive at 

$$
\int_ {\mathcal {B}} \left[ - \frac {\partial \psi}{\partial \phi} - G _ {c} \frac {\partial \gamma}{\partial \phi} + G _ {c} \nabla \cdot \left(\frac {\partial \gamma}{\partial \nabla \phi}\right) \right] \dot {\phi} \mathrm{d} V - \int_ {\partial \mathcal {B}} G _ {c} \left(\frac {\partial \gamma}{\partial \nabla \phi}\right) \cdot \boldsymbol {n} _ {\mathcal {B}} \dot {\phi} \mathrm{d} A \geq 0\tag{200}
$$

which results in the Neumann boundary condition 

$$
\left(\frac {\partial \gamma}{\partial \nabla \phi}\right) \cdot \boldsymbol {n} _ {\mathcal {B}} = 0\tag{201}
$$

and Equation (200) is simplified to 

$$
f (\epsilon , \phi) \dot {\phi} \geq 0, \quad f (\epsilon , \phi) := - \frac {\partial \psi}{\partial \phi} - G _ {c} \delta_ {\phi} \gamma \leq 0\tag{202}
$$

where $\delta _ { \phi } \gamma$ is the variational derivative of $\gamma ( \phi )$ given in Equation (34). 

It is shown in Gurtin [1996], that the most general form of an evolution equation for $\phi ,$ which satisfies Equation (202) , is 

$$
\dot {\phi} = \tilde {M} \langle f (\epsilon , \phi) \rangle\tag{203}
$$

where $\tilde { M }$ denotes the kinetic coefficient or mobility parameter which is a scalar, non-negative function. Recall that, our energy density is given by 

$$
\psi = \int_ {\Omega} \left[ g (\phi) \psi_ {0} ^ {+} (\pmb {\epsilon}) + \psi_ {0} ^ {-} (\pmb {\epsilon}) \right] \mathrm{d} V + \int_ {\mathcal {B}} G _ {c} \frac {1}{c _ {0}} \left[ \frac {1}{l _ {0}} \alpha (\phi) + l _ {0} (\nabla \phi \cdot \nabla \phi) \right] \mathrm{d} V\tag{204}
$$

and thus 

$$
\dot {\phi} = \tilde {M} \langle f (\epsilon , \phi) \rangle , \quad f (\epsilon , \phi) = - g ^ {\prime} (\phi) \psi_ {0} ^ {+} - G _ {c} \frac {1}{c _ {0}} \left(\frac {1}{l _ {0}} \alpha^ {\prime} (\phi) - 2 l _ {0} \Delta \phi\right)\tag{205}
$$

which is identical to the result given in Wu [2017]. The simplest case, $\tilde { M } = M = c o n s t .$ leads to the standard Ginzburg-Landau evolution equation. The limit case $M \to \infty$ approximates the quasi static limit case. For finite values of $M$ , the model can be regarded as a viscous approximation of the quasi static case with viscosity $1 / M$ 

## D Comparison with other gradient-damage models

In existing gradient-damage models [Frémond and Nedjar, 1996, Liebe et al., 2001, Pham et al., 2011], the free energy density functional $\psi$ depends not only on the strain tensor  and damage variable $\phi ,$ , but also on the damage gradient $\nabla \phi$ 

$$
\psi (\pmb {\epsilon}, \phi , \nabla \phi) = \frac {1}{2} g (\phi) \pmb {\epsilon}: \mathbb {E} _ {0}: \pmb {\epsilon} + \frac {1}{2} E _ {g} \nabla \phi \cdot \nabla \phi\tag{206}
$$

where the first term is the classical local free energy density potential; the second one characterises microscopic nonlocal interactions in terms of the gradient parameter $E _ { g } \geq 0$ to be determined. 

As the damage gradient appears in the free energy density potential, the standard framework of thermodynamics cannot be used straightforwardly. To overcome this issue, Polizzotto and Borino [1998] introduced the so-called nonlocal energy residual and rewrote the local version of the global Clausius Duhem inequality as 

$$
\dot {\mathcal {D}} _ {\mathrm{loc}} = \boldsymbol {\sigma}: \dot {\epsilon} - \dot {\psi} + \mathcal {R} \geq 0 \quad \text { with } \quad \int_ {\mathcal {B}} \mathcal {R} \mathrm{d} V = 0\tag{207}
$$

where the nonlocal energy residual $\mathcal { R }$ accounts for microscopic interactions without modifying the classical constitutive relation and damage driving force. Accordingly, the local dissipation inequality reads 

$$
\dot {\mathcal {D}} _ {\mathrm{loc}} = Y \dot {\phi} - E _ {g} \nabla \phi \cdot \nabla \dot {\phi} + \mathcal {R} \geq 0, \quad Y := - \frac {\partial \psi}{\partial \phi}\tag{208a}
$$

which implies independent evolution laws for the damage $\phi$ and its gradient $\nabla \phi .$ . To reconcile their in-between compatibility, Polizzotto and Borino [1998] further introduced a non-local damage driving force $\bar { Y }$ and wrote the energy dissipation rate as a bilinear form 

$$
\dot {\mathcal {D}} _ {\mathrm{loc}} = \bar {Y} \dot {\phi} \geq 0, \qquad \mathcal {R} = \bar {Y} \dot {\phi} - Y \dot {\phi} + E _ {g} \nabla \phi \cdot \nabla \dot {\phi}\tag{208b}
$$

leading to 

$$
\int_ {\mathcal {B}} \mathcal {R} \mathrm{d} V = \int_ {\mathcal {B}} \big (\bar {Y} - Y - E _ {g} \Delta \phi \big) \dot {\phi} \mathrm{d} V + \int_ {\partial \mathcal {B}} E _ {g} \big (\nabla \phi \cdot \pmb {n} _ {\mathcal {B}} \big) \dot {\phi} \mathrm{d} A = 0\tag{209}
$$

where integration by part has been considered. It then follows that 

$$
\left\{ \begin{array}{l l} \bar {Y} = Y + E _ {g} \Delta \phi & \forall \dot {\phi} > 0 \\ \nabla \phi \cdot \boldsymbol {n} _ {\mathcal {B}} = 0 \end{array} \right. \quad \text {   in   } \mathcal {B} \quad \text {   on   } \partial \mathcal {B}\tag{210}
$$

Moreover, a failure criterion has to be constructed a priori in order to determine the damage evolution law. For the local energy dissipation inequality (208b) in bilinear form, the damage criterion is heuristically motivated as 

$$
f (\bar {Y}, \kappa) = \bar {Y} - \kappa (\phi) = Y + E _ {g} \Delta \phi - \kappa (\phi) \leq 0\tag{211}
$$

for a damage threshold $\kappa ( \phi )$ to be determined. 

In existing gradient-damage models, the gradient parameter $E _ { g }$ and damage threshold $\kappa ( \phi )$ are generally assumed ad hoc. Lorentz and Godard [2011] first suggested determining them from 1-D closed-form solution. In particular, comparison of the damage criterion (211) to Equation (67b) gives 

$$
E _ {g} = \frac {2 G _ {c}}{c _ {0} l _ {0}} l _ {0} ^ {2}, \quad \kappa (\phi) = \frac {G _ {c}}{c _ {0} l _ {0}} \alpha^ {\prime} (\phi)\tag{212}
$$

both dependent on the fracture energy $G _ { c }$ and length scale $l _ { 0 }$ . With the above gradient parameter $E _ { g }$ and damage threshold $\kappa ( \phi )$ , the resulting damage evolution law and governing equations are identical to those developed in this work. However, the second term in the free energy density potential (206), accounting for microscopic nonlocal interactions, is characterised by the damage parameter $E _ { g }$ dependent on the fracture energy $G _ { c }$ . Namely, it should be completely dissipative, but is assumed to be recoverable in existing models. 

Contrariwise, the aforementioned controversy does not arise in the geometrically regularised gradient damage model with energetic equivalence (i.e., the PFM model of Wu [2017, 2018b]). Moreover, only standard thermodynamic arguments are considered, whereas it is unnecessary to introduce any extra assumption to reconcile compatibility between the damage $\phi$ and its gradient $\nabla \phi$ 

## E Arc-length (path following) methods

The basic idea of path following methods, often called arc-length methods, is to consider the load parameter $\lambda$ as an additional unknown governed by a constraint function Riks [1979], Ramm [1981]. Hence, the system of equations to be solved reads 

$$
\left[ \begin{array}{c} \mathbf {f} ^ {\text {int}} (\mathbf {a}) - \lambda \mathbf {g} \\ \varphi (\mathbf {a}, \lambda) \end{array} \right] = \left[ \begin{array}{c} \mathbf {0} \\ 0 \end{array} \right]\tag{213}
$$

where a denotes the nodal unknowns vector, which for a PFM contains the nodal displacements and phase-field<sup>27</sup>, $\varphi$ is the constraint function and g is the reference constant load vector. Different choices for $\varphi$ result in different arc-length methods. 

The above system of equation, Equation (213), is solved by the Newton-Raphson method which is indeed a series of successive linearised equations. In what follows the superscript $" \mathrm { i n t } "$ in $\mathbf { f } ^ { \mathrm { i n t } }$ is skipped for notation convenience. Start from the known state $( \mathbf { a } ^ { ( k ) } , \lambda ^ { ( k ) } )$ ), 

$$
\left\{ \begin{array}{c} r ^ {(k)} \\ \varphi^ {(k)} \end{array} \right\} + \left[ \begin{array}{c c} \mathbf {K} & - \mathbf {g} \\ \mathbf {v} ^ {\mathrm{T}} & w \end{array} \right] \left\{ \begin{array}{c} \Delta \mathbf {a} \\ \Delta \lambda \end{array} \right\} = 0\tag{214}
$$

where 

$$
\mathbf {K} = \frac {\partial \mathbf {f}}{\partial \mathbf {a}}, \qquad \mathbf {v} = \frac {\partial \varphi}{\partial \mathbf {a}}, \qquad w = \frac {\partial \varphi}{\partial \lambda}\tag{215}
$$

with the residual $\mathbf { r } = \lambda \mathbf { g } - \mathbf { f } ( \mathbf { a } )$ . Therefore, the corrections are given by 

$$
\left[ \begin{array}{c} \Delta \mathbf {a} \\ \Delta \boldsymbol {\lambda} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {K} & - \mathbf {g} \\ \mathbf {v} ^ {\mathrm{T}} & w \end{array} \right] ^ {- 1} \left[ \begin{array}{c} \mathbf {r} \\ - \varphi (\mathbf {a} ^ {(k)}, \boldsymbol {\lambda} ^ {(k)}) \end{array} \right]\tag{216}
$$

Then the state vector and the load parameter are updated and this iterative procedure is repeated until the norm of the residuals r and $\phi$ satisfy predefined convergence criteria. 

In order to avoid the inverse of the Jacobian in Equation (216) which is neither symmetric nor banded, the Sherman-Morrison formula for the inverse of a non singular matrix plus a rank 1 matrix has been used. By defining the following vectors 

$$
\mathbf {u} ^ {I} = \mathbf {K} ^ {- 1} \mathbf {r}, \quad \mathbf {u} ^ {I I} = \mathbf {K} ^ {- 1} \mathbf {g}\tag{217}
$$

we can update the variables as 

$$
\left\{ \begin{array}{c} \Delta \mathbf {a} \\ \Delta \lambda \end{array} \right\} = \left[ \begin{array}{c} \boldsymbol {u} ^ {I} \\ 0 \end{array} \right] - \frac {\mathbf {v} ^ {\mathrm{T}} \mathbf {u} ^ {I} + \varphi}{\mathbf {v} ^ {\mathrm{T}} \mathbf {u} ^ {I I} + w} \left\{ \begin{array}{c} \mathbf {u} _ {I I} \\ 1 \end{array} \right\}\tag{218}
$$

In Gutiérrez [2004], Verhoosel et al. [2009], an energy-based arc-length method was proposed. The basic idea is that, by the second law of thermodynamics, the amount of energy dissipated in a system is positive and monotonically increasing. The discretised energy release rate reads [Gutiérrez, 2004] 

$$
G = \frac {1}{2} \lambda \dot {\mathbf {a}} ^ {\mathrm{T}} \mathbf {g} - \frac {1}{2} \dot {\lambda} \mathbf {a} ^ {\mathrm{T}} \mathbf {g}\tag{219}
$$

Hence the above equation is an ideal candidate to be a constraint equation $\phi .$ . The forward Euler integration scheme for the above rate equation gives the discrete arc-length function 

$$
\begin{array}{r} \varphi = \Delta \tau - \frac {1}{2} \left[ \lambda_ {n} (\mathbf {a} _ {n + 1} ^ {\mathrm{T}} - \mathbf {a} _ {n} ^ {\mathrm{T}}) - (\lambda_ {n + 1} - \lambda^ {(n)}) \mathbf {a} _ {n} ^ {\mathrm{T}} \right] \mathbf {g} \\ = \Delta \tau - \frac {1}{2} \left[ \lambda_ {n} \mathbf {a} _ {n + 1} ^ {\mathrm{T}} - \lambda_ {n + 1} \mathbf {a} _ {n} ^ {\mathrm{T}} \right] \mathbf {g} \end{array}\tag{220}
$$

(221) 

where $\Delta \tau \ [ \mathrm { N m } ]$ is the incremental path following parameter that represents the amount of energy to be released when going from load step n to load step $n + 1$ . Note that the second in Equation (221) is identical to the one used in May et al. [2016]. As the name implies, a dissipation based arc-length control can only be used when there is dissipation. Therefore the elastic response is usually handled using a displacement or force control Nguyen and Nguyen-Xuan [2012], van der Meer [2012]. May et al. [2016] presented yet another way to trace the elastic response with a rate of the internal energy. We refer to Nguyen and Nguyen-Xuan [2012], May et al. [2016] for details on implementation. 

Another path following strategy is the classical indirect displacement control method proposed by de Borst [1987], with the arc-length constraint expressed as 

$$
\varphi = \Delta \tau - \mathbf {S} \Delta \mathbf {a} = 0\tag{222}
$$

for the selection vector S [Wriggers and Simó, 1990]. Note that the constraint in Equation (222) also applies to the direct displacement control with an appropriate selection vector. In the indirect displacement control, the contributing dofs, which are local quantities, have to be selected a priori such that the pseudotime parameter $\varDelta \tau$ is always monotonically increasing. This is not a practical issue since they can be either identified from experimental test or selected heuristically. Usually, the crack mouth opening or sliding displacements, i.e., CMOD or CMSD, is considered dependent on the specific problems. In this case, the selection vector is given in the form $\mathbf { S } = \left\{ 0 , \cdots , 0 , 1 , 0 , \cdots , 0 , - 1 , 0 , \cdots , 0 \right\} ^ { 1 }$ , where the locations with non-zero values correspond to the normal or tangential dofs of the nodes at opposite sides of the crack mouth; see Wu [2018a] for more details. 

## References



K. Agathos, G. Ventura, E. Chatzi, and S. P. Bordas. Stable 3D XFEM/vector level sets for non-planar 3D crack propagation and comparison of enrichment schemes. International Journal for Numerical Methods in Engineering, 113(2):252–276, 2018. [Cited on page 18] 





V. Agrawal and K. Dayal. Dependence of equilibrium Griffith surface energy on crack speed in phase-field models for fracture coupled to elastodynamics. International Journal ofFracture, 207:243–249, 2017. [Cited on pages 17, 18, and 103] 





A. Agwai, I. Guven, and E. Madenci. Predicting crack propagation with peridynamics: a comparative study. International Journal ofFracture, 171(1):65, 2011. [Cited on pages 13 and 17] 





A. Ahmed, F. Van der Meer, and L. Sluys. A geometrically nonlinear discontinuous solid-like shell element (dsls) for thin shell structures. Computer Methods in Applied Mechanics and Engineering, 201:191–207, 2012. [Cited on page 19] 





F. Aldakheel, B. Hudobivnik, A. Hussein, and P. Wriggers. Phase-field modeling of brittle fracture using an efficient virtual element scheme. Computer Methods in Applied Mechanics and Engineering, 2018. [Cited on page 66] 





R. Alessi, J.-J. Marigo, and S. Vidoli. Gradient damage models coupled with plasticity: Variational formulation and main properties. Mechanics of Materials, 80, Part B:351 – 367, 2015. [Cited on pages 16, 32, and 36] 





R. Alessi, M. Ambati, S. Gerasimov, S. Vidoli, and L. De Lorenzis. Comparison of phase-field models of fracture coupled with plasticity. In E. d. S. N. M. C. E. Oñate, D. Peric, editor, Advances in Computational Plasticity: A Book in Honour ofD. Roger J. Owen, pages 1–21. Springer International Publishing, 2018a. [Cited on pages 16 and 28] 





R. Alessi, S. Vidoli, and L. D. Lorenzis. A phenomenological approach to fatigue with a variational phase-field model: The one-dimensional case. Engineering Fracture Mechanics, 190:53–73, 2018b. [Cited on pages 21 and 103] 





M. Alnaes, J. Blechta, J. Hake, A. Johansson, B. Kehlet, A. Logg, C.Richardson, J. Ring, M. Rognes, and G. Wells. The fenics project version 1.5. Archive ofNumerical Software, 3(100), 2015. [Cited on page 66] 





M. Ambati and L. D. Lorenzis. Phase-field modeling of brittle and ductile fracture in shells with isogeometric NURBS-based solid-shell elements. Computer Methods in Applied Mechanics and Engineering, 312:351 – 373, 2016. [Cited on page 19] 





M. Ambati, T. Gerasimov, and L. De Lorenzis. A review on phase-field models of brittle fracture and a new fast hybrid formulation. Computational Mechanics, 55(2):383–405, 2015a. [Cited on pages 10, 15, 37, 62, 69, and 76] 





M. Ambati, T. Gerasimov, and L. De Lorenzis. Phase-field modeling of ductile fracture. Computational Mechanics, 55(5):1017–1040, 2015b. [Cited on pages 16 and 28] 





M. Ambati, R. Kruse, and L. De Lorenzis. A phase-field model for ductile fracture at finite strains and its experimental verification. Computational Mechanics, 57(1):149–167, 2016. [Cited on pages 16, 18, 21, and 22] 





L. Ambrosio and V. M. Tortorelli. Approximation of functional depending on jumps by elliptic functional via t-convergence. Communications on Pure and Applied Mathematics, 43(8):999–1036, 1990. [Cited on pages 11, 13, 25, and 35] 





G. Amendola, M. Fabrizio, and J. Golden. Thermomechanics of damage and fatigue by a phase field model. Journal ofThermal Stresses, 39(5):487–499, 2016. [Cited on page 21] 





F. Amiri, D. Millán, Y. Shen, T. Rabczuk, and M. Arroyo. Phase-field modeling of fracture in linear thin shells. Theoretical and Applied Fracture Mechanics, 69:102 – 109, 2014. [Cited on page 19] 





H. Amor. Approche variationnelle des lois de Griffith et de Paris via des modeles non-locaux d’endommagement: Etude theorique et mise en oeuvre numérique. PhD thesis, Université Paris 13, Paris, France, 2008. [Cited on page 59] 





H. Amor, J.-J. Marigo, and C. Maurini. Regularized formulation of the variational brittle fracture with unilateral contact: Numerical experiments. Journal ofthe Mechanics and Physics ofSolids, 57(8):1209 – 1229, 2009. [Cited on pages 2, 12, 13, 34, 39, 45, 55, 59, 62, 67, 68, 75, 76, 78, 79, 80, and 82] 





I. S. Aranson, V. A. Kalatsky, and V. M. Vinokur. Continuum field description of crack propagation. Physic. Review Letters, 85:118–121, 2000. [Cited on pages 8 and 15] 





P. Areias, M. A. Msekh, and T. Rabczuk. Damage and fracture algorithm using the screened Poisson equation and local remeshing. Engineering Fracture Mechanics, 158:116 – 143, 2016a. [Cited on page 38] 





P. Areias, T. Rabczuk, and M. Msekh. Phase-field analysis of finite-strain plates and shells including element subdivision. Computer Methods in Applied Mechanics and Engineering, 312:322 – 350, 2016b. [Cited on page 19] 





F. Armero and C. Linder. Numerical simulation of dynamic fracture using finite elements with embedded discontinuities. International Journal ofFracture, 160(2):119–141, 2009. [Cited on page 8] 





M. Arroyo and M. Ortiz. Local maximum-entropy approximation schemes: a seamless bridge between finite elements and meshfree methods. International journalfor numerical methods in engineering, 65 (13):2167–2202, 2006. [Cited on page 19] 





M. Artina, M. Fornasier, S. Micheletti, and S. Perotto. Anisotropic mesh adaptation for crack detection in brittle materials. SIAM Journal on Scientific Computing, 37(4):B633–B659, 2015. [Cited on pages 11, 69, 70, and 78] 





S. Balay, S. Abhyankar, M. F. Adams, J. Brown, P. Brune, K. Buschelman, L. Dalcin, V. Eijkhout, W. D. Gropp, D. Kaushik, M. G. Knepley, L. C. McInnes, K. Rupp, B. F. Smith, S. Zampini, and H. Zhang. PETSc users manual. Technical Report ANL-95/11 - Revision 3.7, Argonne National Laboratory, 2016. URL http://www.mcs.anl.gov/petsc. [Cited on pages 59 and 62] 





A. A. L. Baldelli, J. F. Babadjian, B. Bourdin, D. Henao, and C. Maurini. A variational model for fracture and debonding of thin films under in-plane loadings. J. Mech. Phys. Solids, 70:320–348, October 2014. [Cited on page 21] 





G. Barenblatt. The formation of equilibrium cracks during brittle fracture. general ideas and hypotheses. axially-symmetric cracks. Journal ofApplied Mathematics and Mechanics, 23:622–636, 1959. [Cited on page 49] 





G. Barenblatt. The mathematical theory of equilibrium of cracks in brittle fracture. Advances in Applied Fracture, 7:55–129, 1962. [Cited on pages 8 and 49] 





Z. P. Bažant and M. Jirásek. Nonlocal integral formulations of plasticity and damage: survey of progress. Journal ofEngineering Mechanics, 128(11):1119–1149, 2002. [Cited on page 7] 





Z. P. Bažant, T. Belytschko, and T.-P. Chang. Continuum model for strain softening. Journal ofEngineering Mechanics, 110:1666–1692, 1984. [Cited on page 7] 





L. Beex, R. Peerlings, and M. Geers. A multiscale quasicontinuum method for lattice models with bond failure and fiber sliding. Computer Methods in Applied Mechanics and Engineering, 269:108–122, 2014. [Cited on page 7] 





T. Belytschko, J. Fish, and B. E. Engelmann. A finite element with embedded localization zones. Computer Methods in Applied Mechanics and Engineering, 70(1):59 – 89, 1988. [Cited on page 8] 





T. Belytschko, Y. Krongauz, D. Organ, M. Fleming, and P. Krysl. Meshless methods: An overview and recent developments. Computer Methods in Applied Mechanics and Engineering, 139(1):3 – 47, 1996. [Cited on page 8] 





T. Belytschko, H. Chen, J. Xu, and G. Zi. Dynamic crack propagation based on loss of hyperbolicity and a new discontinuous enrichment. International Journalfor Numerical Methods in Engineering, 58(12): 1873–1905, 2003. [Cited on page 8] 





T. Belytschko, S. Loehnert, and J.-H. Song. Multiscale aggregating discontinuities: a method for circumventing loss of material stability. International Journal for Numerical Methods in Engineering, 73(6): 869–894, 2008. [Cited on page 7] 





S. J. Benson and T. S. Munson. Flexible complementarity solvers for large-scale applications. Optimization Methods and Software, 21:155–168, 2006. [Cited on page 59] 





P. Bernard, N. Moës, and N. Chevaugeon. Damage growth modeling using the thick level set (tls) approach: Efficient discretization for quasi-static loadings. Computer Methods in Applied Mechanics and Engineering, 233-236:11–27, 2012. [Cited on page 10] 





M. A. Bessa, J. T. Foster, T. Belytschko, and W. K. Liu. A meshfree unification: reproducing kernel peridynamics. Computational Mechanics, 53(6):1251–1264, 2014. [Cited on page 11] 





S. Bhowmick and G. R. Liu. A phase-field modeling for brittle fracture and crack propagation based on the cell-based smoothed finite element method. Engineering Fracture Mechanics, 2018. [Cited on page 66] 





C. Bilgen, A. Kopanicáková, R. Krause, and K. Weinberg. A phase-field approach to conchoidal fracture.ˇ Meccanica, 53(6):1203–1219, 2018. [Cited on page 68] 





T. N. Bittencourt, P. A. Wawrzynek, A. R. Ingraffea, and J. L. Sousa. Quasi-automatic simulation of crack propagation for 2D LEFM problems. Engineering Fracture Mechanics, 55(321–334):911–944, 1996. [Cited on page 86] 





J. Bleyer and R. Alessi. Phase-field modeling of anisotropic brittle fracture including several damage mechanisms. Computer Methods in Applied Mechanics and Engineering, 336:213–236, 2018. [Cited on page 20] 





J. Bleyer and J.-F. Molinari. Microbranching instability in phase-field modelling of dynamic brittle fracture. Applied Physics Letters, 110(15):151903, Apr 2017. [Cited on pages 17 and 97] 





J. Bleyer, C. Roux-Langlois, and J.-F. Molinari. Dynamic crack propagation with a variational phase-field model: limiting speed, crack branching and velocity-toughening mechanisms. International Journal of Fracture, 204:79–100, 2017. [Cited on pages 17, 18, and 95] 





J. Boldrini, E. B. de Moraes, L. Chiarelli, F. Fumes, and M. Bittencourt. A non-isothermal thermodynamically consistent phase field framework for structural damage and fatigue. Computer Methods in Applied Mechanics and Engineering, 312:395–427, 2016. [Cited on page 21] 





S. Bordas, V. P. Nguyen, C. Dunant, A. Guidoum, and H. Nguyen-Dang. An extended finite element library. International Journalfor Numerical Methods in Engineering, 71(6):703–732, 2007. [Cited on pages 13, 67, and 80] 





S. Bordas, T. Rabczuk, and G. Zi. Three-dimensional crack initiation, propagation, branching and junction in non-linear materials by an extended meshfree method without asymptotic enrichment. Engineering Fracture Mechanics, 75(5):943–960, 2008. [Cited on pages 8 and 18] 





S. P. Bordas, T. Rabczuk, N.-X. Hung, V. P. Nguyen, S. Natarajan, T. Bog, N. V. Hiep, et al. Strain smoothing in fem and xfem. Computers & structures, 88(23-24):1419–1443, 2010. [Cited on page 57] 





M. J. Borden, C. V. Verhoosel, M. A. Scott, T. J. Hughes, and C. M. Landis. A phase-field description of dynamic brittle fracture. Computer Methods in Applied Mechanics and Engineering, 217-220:77 – 95, 2012. [Cited on pages 17, 18, 22, 30, 36, 39, 47, 57, 63, 64, 65, 66, 67, 71, 74, 95, 96, and 97] 





M. J. Borden, T. J. Hughes, C. M. Landis, and C. V. Verhoosel. A higher-order phase-field model for brittle fracture: Formulation and analysis within the isogeometric analysis framework. Computer Methods in Applied Mechanics and Engineering, 273:100 – 118, 2014. [Cited on pages 13, 18, 19, 66, 69, and 70] 





M. J. Borden, T. J. Hughes, C. M. Landis, A. Anvari, and I. J. Lee. A phase-field formulation for fracture in ductile materials: Finite deformation balance law derivation, plastic degradation, and stress triaxiality effects. Computer Methods in Applied Mechanics and Engineering, 312:130 – 166, 2016. [Cited on pages 16, 18, 21, 28, 35, 36, 74, and 106] 





R. Borst and L. J. Sluys. Localisation in a Cosserat continuum under static and dynamic loading conditions. Computer Methods in Applied Mechanics and Engineering, 90:805–827, 1991. [Cited on page 7] 





P. Bouchard, F. Bay, and Y. Chastel. Numerical modelling of crack propagation: automatic remeshing and comparison of different criteria. Computer Methods in Applied Mechanics and Engineering, 192(35-36): 3887 – 3908, 2003. [Cited on pages 8 and 78] 





B. Bourdin, G. Francfort, and J.-J. Marigo. Numerical experiments in revisited brittle fracture. Journal of the Mechanics and Physics ofSolids, 48(4):797 – 826, 2000. [Cited on pages 8, 11, 13, 15, 18, 20, 25, 31, 32, 33, 35, 36, 39, 45, 55, 62, 67, 68, and 76] 





B. Bourdin, G. Francfort, and J. Marigo. The variational approach to fracture. Journal ofElasticity, 91 (1-3):5–148, 2008a. doi: 10.1007/s10659-007-9107-3. [Cited on pages 16 and 75] 





B. Bourdin, G. Francfort, and J.-J. Marigo. The variational approach to fracture. Springer, Berlin, 2008b. [Cited on pages 9, 10, 12, 23, 24, 68, and 103] 





B. Bourdin, C. J. Larsen, and C. L. Richardson. A time-discrete model for dynamic fracture based on crack regularization. International Journal ofFracture, 168(2):133–143, 2011. [Cited on pages 15, 17, and 32] 





B. Bourdin, J.-J. Marigo, C. Maurini, and P. Sicsic. Morphogenesis and propagation of complex cracks induced by thermal shocks. Phys. Rev. Lett., 112:014301, Jan 2014. [Cited on page 19] 





A. Braides. Approximation of Free-Discontinuity Problems. Springer-Verlag, 1998. doi: 10.1007/ BFb0097344. [Cited on pages 9, 11, 25, and 29] 





E. C. Bryant and W. Sun. A mixed-mode phase field fracture model in anisotropic rocks with consistent kinematics. Computer Methods in Applied Mechanics and Engineering, 342:561–584, 2018. [Cited on page 20] 





E. Budyn, G. Zi, N. Moës, and T. Belytschko. A method for multiple crack growth in brittle materials without remeshing. International Journalfor Numerical Methods in Engineering, 61(10):1741–1770, 2004. [Cited on page 80] 





S. Burke, C. Ortner, and E. Süli. An adaptive finite element approximation of a variational model of brittle fracture. SIAM Journal on Numerical Analysis, 48(3):980–1012, 2010. [Cited on page 69] 





S. Burke, C. Ortner, and E. Süli. An adaptive finite element approximation of a generalized Ambrosio-Tortorelli functional. Mathematical Models and Methods in Applied Sciences, 23(09):1663–1697, Aug 2013. [Cited on page 55] 





M. Caputo and M. Fabrizio. Damage and fatigue described by a fractional derivative model. Journal of Computational Physics, 293:400–408, 2015. [Cited on page 21] 





J. Carlsson and P. Isaksson. Crack dynamics and crack tip shielding in a material containing pores analysed by a phase field method. Engineering Fracture Mechanics, 2018. [Cited on page 18] 





I. Carol and K. Willam. Spurious energies dissipation/generation in stiffness recovery models for elastic degradation and damage. International Journal ofSolids and Structures, 33(20-22):2939–2957, 1996. [Cited on page 35] 





V. Carollo, J. Reinoso, and M. Paggi. A 3d finite strain model for intralayer and interlayer crack simulation coupling the phase field approach and cohesive zone model. Composite Structures, 182:636–651, 2017. [Cited on page 102] 





V. Carollo, J. Reinoso, and M. Paggi. Modeling complex crack paths in ceramic laminates: A novel variational framework combining the phase field method of fracture and the cohesive zone model. Journal ofthe European Ceramic Society, 38(8):2994–3003, 2018. [Cited on page 21] 





F. Cazes and N. Moës. Comparison of a phase-field model and of a thick level set model for brittle and quasi-brittle fracture. International Journalfor Numerical Methods in Engineering, 103(2):114–143, 2015. [Cited on page 10] 





M. Cervera, L. Pelà, R. Clemente, and P. Roca. A crack-tracking technique for localized damage in quasi-brittle materials. Engineering Fracture Mechanics, 77:2431–2450, 2010. [Cited on page 93] 





M. Cervera, M. Chiumenti, and R. Codina. Mesh objective modeling of cracks using continuous linear strain and displacement interpolations. Int. J. Numer. Meth. Engng., 87(10):962–987, 2011. [Cited on page 87] 





M. Cervera, G. Barbat, and M. Chiumenti. Finite element modeling of quasi-brittle cracks in 2D and 3D with enhanced strain accuracy. Comput. Mech., 60(5):767–796, 2017. [Cited on page 87] 





P. Chakraborty, P. Sabharwall, and M. C. Carroll. A phase-field approach to model multi-axial and microstructure dependent fracture in nuclear grade graphite. Journal ofNuclear Materials, 475:200 – 208, 2016a. [Cited on page 66] 





P. Chakraborty, Y. Zhang, and M. R. Tonks. Multi-scale modeling of microstructure dependent intergranular brittle fracture using a quantitative phase-field based method. Computational Materials Science, 113:38 – 52, 2016b. [Cited on page 66] 





A. Chambolle. An approximation result for special functions with bounded deformation. Journal de Mathématiques Pures et Appliquées, 83(7):929 – 954, 2004. [Cited on page 25] 





A. Chambolle, G. Francfort, and J.-J. Marigo. When and how do cracks propagate? Journal of the Mechanics and Physics ofSolids, 57(9):1614 – 1622, 2009. [Cited on page 24] 





C.-H. Chen, E. Bouchbinder, and A. Karma. Instability in dynamic fracture and the failure of the classical theory of cracks. Nature Physics, 13(12):1186, 2017. [Cited on page 18] 





F. Cirak, M. Ortiz, and A. Pandolfi. A cohesive approach to thin-shell fracture and fragmentation. Computer Methods in Applied Mechanics and Engineering, 194(21-24):2604–2618, 2005. [Cited on page 19] 





J. D. Clayton and J. Knap. A geometrically nonlinear phase field theory of brittle fracture. International Journal ofFracture, 189(2):139–148, 2014. [Cited on pages 18 and 19] 





B. Coleman and M. Gurtin. Thermodynamics with internal state variables. Journal of Chemistry and Physics, 47:597–613, 1967. [Cited on page 42] 





C. Comi, S. Mariani, and U. Perego. An extended FE strategy for transition from continuum damage to mode I cohesive crack propagation. International Journal for Numerical and Analytical Methods in Geomechanics, 31(2):213–238, 2007. [Cited on page 10] 





H. Cornelissen, D. Hordijk, and H. Reinhardt. Experimental determination of crack softening characteristics of normalweight and lightweight concrete. Heron, 31(2):45–56, 1986. [Cited on pages 50, 52, 53, 54, and 55] 





J. A. Cottrell, T. J. Hughes, and Y. Bazilevs. Isogeometric Analysis: Toward Integration of CAD and FEA. Wiley, 2009. ISBN 9780470748372. [Cited on page 13] 





V. Crismale and G. Lazzaroni. Quasistatic crack growth based on viscous approximation: a model with branching and kinking. Nonlinear Differential Equations and Applications, 24:7, 2017. [Cited on page 24] 





P. A. Cundall and O. D. Strack. A discrete numerical model for granular assemblies. geotechnique, 29(1): 47–65, 1979. [Cited on page 7] 





S. Cuvilliez, F. Feyel, E. Lorentz, and S. Michel-Ponnelle. A finite element approach coupling a continuous gradient damage model and a cohesive zone model within the framework of quasi-brittle failure. Computer Methods in Applied Mechanics and Engineering, 237-240:244 – 259, 2012. [Cited on page 10] 





G. Dal Maso and R. Toader. A model for the quasi-static growth of brittle fractures based on local minimization. Mathematical Models and Methods in Applied Sciences, 12(12):1773–1799, 2002. [Cited on page 11] 





T. Dally and K. Weinberg. The phase-field approach as a tool for experimental validations in fracture mechanics. Continuum Mechanics and Thermodynamics, pages 1–10, 2015. [Cited on page 21] 





R. de Borst. Computation of post-bifurcation and post-failure behavior of strain-softening solids. Computers and Structures, 25:211–224, 1987. [Cited on page 110] 





R. de Borst and C. Verhoosel. Gradient damage vs phase-field approaches for fracture: Similarities and differences. Computer Methods in Applied Mechanics and Engineering, 312:78 – 94, 2016. [Cited on page 40] 





G. Del Piero. A variational approach to fracture and other inelastic phenomena. Journal ofElasticity, 112 (1):3–77, 2013. [Cited on pages 10 and 11] 





P. N. Demmie and S. A. Silling. An approach to modeling extreme loading of structures using peridynamics. Journal ofmechanics ofmaterials and structures, 2(10):1921 – 1945, 2007. [Cited on page 11] 





M. Diehl, M. Wicke, P. Shanthraj, F. Roters, A. Brueckner-Foit, and D. Raabe. Coupled crystal plasticity– phase field fracture simulation study on damage evolution around a void: Pore shape versus crystallographic orientation. JOM, 69(5):872–878, May 2017. [Cited on page 19] 





F. Duda, A. Ciarbonetti, S. Toro, and A. Huespe. A phase-field model for solute-assisted brittle fracture in elastic-plastic solids. International Journal ofPlasticity, pages –, 2017. [Cited on page 19] 





F. P. Duda, A. Ciarbonetti, P. J. Sánchez, and A. E. Huespe. A phase-field/gradient damage model for brittle fracture in elastic-plastic solids. International Journal ofPlasticity, 65:269 – 296, 2015. [Cited on page 16] 





D. Dugdale. Yielding of steel sheets containing slits. Journal ofthe Mechanics and Physics ofSolids, 8(2): 100–104, 1960. [Cited on pages 8 and 49] 





P. Dumstorff and G. Meschke. Crack propagation criteria in the framework of x-fem-based structural analyses. International Journal For Numerical And Analytical Methods In Geomechanics, 31:239–259, 2007. [Cited on pages 8 and 90] 





C. Dunant, V. P. Nguyen, M. Belgasmia, S. Bordas, A. Guidoum, and H. Nguyen-Dang. Architecture trade-offs of including a mesher in an object-oriented extended finite element code. European journal of computational mechanics, (16):237–258, 2007. Special issue on the extended finite element method (XFEM). [Cited on page 13] 





E. N. Dvorkin, A. M. Cuitino, and G. Gioia. Finite elements with displacement interpolated embedded localization lines insensitive to mesh size and distortions. International Journal for Numerical Methods in Engineering, 30:541–564, 1990. [Cited on page 8] 





F. Erdogan and G. C. Sih. On the crack extension in plates under plane loading and transverse shear. Journal of Basic Engineering, 85:519–527, 1963. [Cited on page 8] 





F. Facchinei and J.-S. Pang. Finite Dimensional Variational Inequalities and Complementarity Problems, Vol. 1 and Vol. 2. Springer-Verlag, New York, 2003. [Cited on page 59] 





P. Farrell and C. Maurini. Linear and nonlinear solvers for variational phase-field models of brittle fracture. International Journalfor Numerical Methods in Engineering, (109):648–667, 2017. [Cited on pages 15, 39, 57, 59, 63, 66, 67, and 68] 





A. Faye, Y. Lev, and K. Volokh. The effect of local inertia around the crack-tip in dynamic fracture of soft materials. Mechanics ofSoft Materials, 1(1):4, 2019. [Cited on page 18] 





D. C. Feng and J. Y. Wu. Phase-field regularized cohesive zone model (CZM) and size effect of concrete. Engineering Fracture Mechanics, 197:66–79, 2018. [Cited on pages 17, 23, and 56] 





G. Francfort and J.-J. Marigo. Revisiting brittle fracture as an energy minimization problem. Journal ofthe Mechanics and Physics of Solids, 46(8):1319 – 1342, 1998. [Cited on pages 7, 8, 11, 12, 13, 15, and 24] 





F. Freddi. Fracture energy in phase field models. Mechanics Research Communications, 2019. [Cited on page 29] 





F. Freddi and F. Iurlano. Numerical insight of a variational smeared approach to cohesive fracture. Journal ofthe Mechanics and Physics ofSolids, 98:156 – 171, 2017. [Cited on pages 17 and 55] 





F. Freddi and G. Royer-Carfagni. Regularized variational theories of fracture: A unified approach. Journal ofthe Mechanics and Physics ofSolids, 58(8):1154 – 1174, 2010. [Cited on page 13] 





F. Freddi and G. Royer-Carfagni. Variational fracture mechanics to model compressive splitting of masonry-like materials. Annals ofSolid and Structural Mechanics, 2(2):57–67, 2011. [Cited on page 20] 





M. Frémond and B. Nedjar. Damage, gradient of damage and principle of virtual power. International Journal ofSolids and Structures, 33(8):1083 – 1103, 1996. [Cited on pages 7, 40, 42, and 108] 





L. Freund. Dynamic Fracture Mechanics. Cambridge University Press, Cambridge, 1998. [Cited on page 93] 





A. Friedman and J. Spruck. Variational andfree boundary problems, volume 53. Springer Science & Business Media, 2012. [Cited on page 25] 





T.-P. Fries and M. Baydoun. Crack propagation with the extended finite element method and a hybrid explicit-implicit crack description. International Journalfor Numerical Methods in Engineering, 89(12): 1527–1558, 2012. [Cited on page 18] 





J. Gálvez, M. Elices, G. Guinea, and J. Planas. Mixed mode fracture of concrete under proportional and nonproportional loading. Int. J. Fract., 94:267–284, 1998. [Cited on pages 91 and 94] 





G. C. Ganzenmuller, S. Hiermaier, and M. May. On the similarity of meshless discretizations of Peridynamics and Smooth-Particle Hydrodynamics. Computers & Structures, 150:71 – 78, 2015. [Cited on page 11] 





D. Gaston, C. Newman, G. Hansen, and D. Lebrun-Grandié. Moose: A parallel computational framework for coupled systems of nonlinear equations. Nuclear Engineering and Design, 239(10):1768 – 1778, 2009. [Cited on page 66] 





R. J. M. Geelen, Y. Liu, J. E. Dolbow, and A. Rodriguez-Ferran. An optimization-based phase-field method for continuous-discontinuous crack propagation. International Journalfor Numerical Methods in Engineering, 2018. [Cited on pages 10 and 67] 





M. Geers, R. de Borst, W. Brekelmans, and R. Peerlings. Strain-based transient-gradient damage model for failure analyses. Computer Methods in Applied Mechanics and Engineering, 160:133–153(21), 1998. [Cited on pages 35, 40, and 41] 





M. G. Geers, V. G. Kouznetsova, and W. Brekelmans. Multi-scale computational homogenization: Trends and challenges. Journal ofcomputational and applied mathematics, 234(7):2175–2182, 2010. [Cited on page 7] 





T. Gerasimov and L. D. Lorenzis. A line search assisted monolithic approach for phase-field computing of brittle fracture. Computer Methods in Applied Mechanics and Engineering, 312:276 – 303, 2016. [Cited on pages 57, 60, 67, and 68] 





T. Gerasimov, N. Noii, O. Allix, and L. De Lorenzis. A non-intrusive global/local approach applied to phase-field modeling of brittle fracture. Advanced Modeling and Simulation in Engineering Sciences, 5 (1):14, 2018. [Cited on page 66] 





B. Giovanardi, A. Scotti, and L. Formaggia. A hybrid XFEM–Phase field (Xfield) method for crack propagation in brittle elastic materials. Computer Methods in Applied Mechanics and Engineering, 320: 396 – 420, 2017. [Cited on pages 10 and 67] 





C. Giry, F. Dufour, and J. Mazars. Stress-based nonlocal damage model. International Journal ofSolids and Structures, 48(25-26):3431 – 3443, 2011. [Cited on page 7] 





A. Gravouil, N. Moes, and T. Belytschko. Non-planar 3D crack growth by the extended finite element and level sets - part ii: Level set update. International Journalfor Numerical Methods in Engineering, 53: 2569–2586, 2002. [Cited on page 72] 





A. A. Griffith. The phenomena of rupture and flow in solids. Philosophical Transactions of the Royal Society ofLondres, 221:163–198, 1920. [Cited on pages 7, 8, and 23] 





O. Gültekin, H. Dal, and G. A. Holzapfel. A phase-field approach to model fracture of arterial walls: Theory and finite element analysis. Computer Methods in Applied Mechanics and Engineering, 312:542 – 566, 2016. [Cited on page 18] 





P. Gupta and C. A. Duarte. Simulation of non-planar three-dimensional hydraulic fracture propagation. International Journalfor Numerical and Analytical Methods in Geomechanics, 38(13):1397–1430, 2014. [Cited on page 18] 





E. Gurses and C. Miehe. A computational framework of three-dimensional configurational-force-driven brittle crack propagation. Computer Methods in Applied Mechanics and Engineering, 198(15-16): 1413–1428, 2009. [Cited on page 18] 





M. E. Gurtin. Generalized Ginzburg-Landau and Cahn-Hilliard equations based on a microforce balance. Physica D: Nonlinear Phenomena, 92(3–4):178 – 192, 1996. ISSN 0167-2789. [Cited on pages 27 and 108] 





M. A. Gutiérrez. Energy release control for numerical simulations of failure in quasi-brittle solids. Communications in Numerical Methods in Engineering, 20(1):19–29, 2004. [Cited on page 110] 





Y. D. Ha and F. Bobaru. Studies of dynamic crack propagation and crack branching with peridynamics. International Journal ofFracture, 162(1):229–244, 2010. [Cited on pages 13, 95, and 96] 





V. Hakim and A. Karma. Crack path prediction in anisotropic brittle materials. Physical Review Letters, 95(23):235–501, 2005. [Cited on page 19] 





J. S. Hale, L. Li, C. N. Richardson, and G. N. Wells. Containers for portable, productive, and performant scientific computing. Computing in Science & Engineering, 19(6):40–50, 2017. [Cited on page 66] 





A. C. Hansen-Dörr, R. de Borst, P. Hennig, and M. Kästner. Phase-field modelling of interface failure in brittle materials. Computer Methods in Applied Mechanics and Engineering, 346:25–42, 2019. [Cited on page 21] 





T. Heister, M. F. Wheeler, and T. Wick. A primal-dual active set method and predictor-corrector mesh adaptivity for computing fracture propagation using a phase-field approach. Computer Methods in Applied Mechanics and Engineering, 290:466 – 495, 2015. [Cited on pages 39, 57, 60, 66, 67, 68, 69, and 70] 





H. Henry. Study of the branching instability using a phase field model of inplane crack propagation. EPL (Europhysics Letters), 83(1):16004, 2008. [Cited on page 15] 





H. Henry and M. Adda-Bedia. Fractographic aspects of crack branching instability using a phase-field model. Physics Review E, 88:060401, 2013. [Cited on page 15] 





H. Henry and H. Levine. Dynamic instabilities of fracture under biaxial strain using a phase field model. Physics Review Letter, 93:105504, 2004. [Cited on page 15] 





C. Hesch and K. Weinberg. Thermodynamically consistent algorithms for a finite-deformation phase-field approach to fracture. International Journalfor Numerical Methods in Engineering, 99(12):906–924, 2014. [Cited on page 18] 





C. Hesch, M. Franke, M. Dittmann, and I. Temizer. Hierarchical NURBS and a higher-order phase-field approach to fracture for finite-deformation contact problems. Computer Methods in Applied Mechanics and Engineering, 301:242 – 258, 2016. [Cited on pages 18 and 66] 





C. Hesch, A. Gil, R. Ortigosa, M. Dittmann, C. Bilgen, P. Betsch, M. Franke, A. Janz, and K. Weinberg. A framework for polyconvex large strain phase-field methods to fracture. Computer Methods in Applied Mechanics and Engineering, pages –, 2017. [Cited on page 18] 





H. Hilber, T. Hughes, and R. Tayler. Improved numerical dissipation for time integration algorithms in structural dynamics. Earthquake Engrg. Struct. Dyn., 5:283–292, 1977. [Cited on page 63] 





A. Hillerborg, M. Modeer, and P. Petersson. Analysis of crack formation and crack growth in concrete by means of fracture mechanics and finite elements. Cement and Concrete Research, 6:773–782, 1976. [Cited on pages 8 and 49] 





M. Hofacker and C. Miehe. Continuum phase field modeling of dynamic fracture: variational principles and staggered FE implementation. International Journal ofFracture, 178(1):113–129, 2012. [Cited on pages 17, 18, 96, and 97] 





M. Hofacker and C. Miehe. A phase field model of dynamic fracture: Robust field updates for the analysis of complex crack patterns. International Journalfor Numerical Methods in Engineering, 93(3):276–301, 2013. [Cited on pages 17, 96, and 97] 





B. L. Holian and R. Ravelo. Fracture simulations using large-scale molecular dynamics. Physics Review B, 51:11275–11288, 1995. [Cited on page 7] 





A. Hrennikoff. Solution of problems of elasticity by the framework method. J. appl. Mech., 1941. [Cited on page 7] 





T. Hughes, J. Cottrell, and Y. Bazilevs. Isogeometric analysis: CAD, finite elements, NURBS, exact geometry and mesh refinement. Computer Methods in Applied Mechanics and Engineering, 194(39-41): 4135–4195, 2005. [Cited on pages 13 and 19] 





T. J. R. Hughes. The Finite Element Method - Linear Static and Dynamic Finite Element Analysis. Prentice-Hall, London, England, 1987. [Cited on pages 8 and 58] 





J. W. Hutchinson and Z. Suo. Mixed mode cracking in layered materials. In Advances in applied mechanics, volume 29, pages 63–191. Elsevier, 1991. [Cited on page 21] 





A. Ingraffea and M. Grigoriu. Probabilistic fracture mechanics: a validation of predictive capability. Technical report, DTIC Document, 1990. [Cited on pages 86 and 87] 





G. R. Irwin. Analysis of stresses and strains near the end of a crack traversing a plate. Journal ofApplied Mechanics, 24:361–364, 1957. [Cited on pages 7 and 8] 





H. Jeong, S. Signetti, T.-S. Han, and S. Ryu. Phase field modeling of crack propagation under combined shear and tensile loading with hybrid formulation. Computational Materials Science, 155:483–492, 2018. [Cited on pages 38 and 66] 





Y. Jin, O. González-Estrada, O. Pierard, and S. Bordas. Error-controlled adaptive extended finite element method for 3d linear elastic crack propagation. Computer methods in applied mechanics and engineering, 318:319–348, 2017. [Cited on pages 70 and 81] 





M. Jirásek. Mathematical analysis of strain localization. Revue Européenne de Génie Civil, 11(7-8): 977–991, 2007. [Cited on page 7] 





P. O. Judt and A. Ricoeur. Crack growth simulation of multiple cracks systems applying remote contour interaction integrals. Theoretical and Applied Fracture Mechanics, 75:78 – 88, 2015. [Cited on page 79] 





L. M. Kachanov. Time of the rupture process under creep conditions. Izv. Akad. Nauk SSR Otd. Tech., 8: 26–31, 1958. [Cited on page 7] 





A. Kaczmarczyk, Z. Ullah, and C. J. Pearce. Energy consistent framework for continuously evolving 3d crack propagation. Computer Methods in Applied Mechanics and Engineering, 324:54 – 73, 2017. [Cited on page 18] 





E. G. Kakouris and S. P. Triantafyllou. Material point method for crack propagation in anisotropic media: a phase field approach. Archive of Applied Mechanics, 2017. [Cited on page 15] 





J. F. Kalthoff and S. Winkler. Failure mode transition at high rates of shear loading. International Conference on Impact Loading and Dynamic Behavior of Materials, 1:185–195, 1987. [Cited on page 96] 





D. Kamensky, G. Moutsanidis, and Y. Bazilevs. Hyperbolic phase field modeling of brittle fracture: part I—theory and simulations. Journal ofthe Mechanics and Physics ofSolids, (121):81–98, 2018. [Cited on pages 17 and 27] 





C. Kane, J. E. Marsden, and M. Ortiz. Symplectic-energy-momentum preserving variational integrators. Journal ofmathematical physics, 40(7):3353–3371, 1999. [Cited on page 103] 





A. Karamnejad and L. J. Sluys. A dispersive multi-scale crack model for quasi-brittle heterogeneous materials under impact loading. Computer Methods in Applied Mechanics and Engineering, 278: 423–444, 2014. [Cited on page 7] 





A. Karamnejad, V. P. Nguyen, and L. J. Sluys. A multi-scale rate dependent crack model for quasi-brittle heterogeneous materials. Engineering Fracture Mechanics, 104:96 – 113, 2013. [Cited on page 10] 





A. Karma, D. A. Kessler, and H. Levine. Phase-field model of mode III dynamic fracture. Physics Review Letter, 87:045501, 2001. [Cited on pages 15, 32, 35, and 36] 





M. Kästner, P. Hennig, T. Linse, and V. Ulbricht. Phase-field modelling of damage and fracture— convergence and local mesh refinement. In K. Naumenko and M. Aßmus, editors, Advanced Methods of Continuum Mechanicsfor Materials and Structures, pages 307–324. 2016. [Cited on pages 66 and 69] 





P. Kerfriden, O. Goury, T. Rabczuk, and S. P.-A. Bordas. A partitioned model order reduction approach to rationalise computational expenses in nonlinear fracture mechanics. Computer methods in applied mechanics and engineering, 256:169–188, 2013. [Cited on page 103] 





I. Khisamitov and G. Meschke. Variational approach to interface element modeling of brittle fracture propagation. Comput. Meth. Appl. Mech. Eng., 328:452–476, 2018. [Cited on page 67] 





J. Kiendl, M. Ambati, L. D. Lorenzis, H. Gomez, and A. Reali. Phase-field description of brittle fracture in plates and shells. Computer Methods in Applied Mechanics and Engineering, 312:374 – 394, 2016. [Cited on page 19] 





M. Klinsmann, D. Rosato, M. Kamlah, and R. M. McMeeking. An assessment of the phase field formulation for crack growth. Computer Methods in Applied Mechanics and Engineering, 294:313 – 330, 2015. [Cited on pages 21, 39, 66, 69, 71, and 72] 





M. Klinsmann, D. Rosato, M. Kamlah, and R. M. McMeeking. Modeling crack growth during li insertion in storage particles using a fracture phase field approach. Journal of the Mechanics and Physics of Solids, 92(Supplement C):313 – 344, 2016. [Cited on page 19] 





D. Krajcinovic. Damage mechanics. Mechanics of Materials, 8(2–3):117–197, 1989. [Cited on page 7] 





C. Kuhn and R. Müller. A phase field model for fracture. Proceedings in Applied Mathematics and Mechanics, 8(1):10223–10224, 2008. [Cited on page 13] 





C. Kuhn and R. Müller. A continuum phase field model for fracture. Engineering Fracture Mechanics, 77 (18):3625 – 3634, 2010a. [Cited on page 14] 





C. Kuhn and R. Müller. Exponential finite elements for a phase field fracture model. Proceedings in Applied Mathematics and Mechanics, 10(1):121–122, 2010b. [Cited on page 66] 





C. Kuhn, A. Schuter, and R. Müller. On degradation functions in phase field fracture models. Computational Materials Science, 108, Part B:374 – 384, 2015. [Cited on pages 36, 53, and 66] 





C. Kuhn, T. Noll, and R. Müller. On phase field modeling of ductile fracture. GAMM-Mitteilungen, 39(1): 35–54, 2016. [Cited on page 16] 





G. Lancioni and V. Corinaldesi. Variational modelling of diffused and localized damage with applications to fiber-reinforced concretes. Meccanica, 2017. [Cited on page 32] 





G. Lancioni and G. Royer-Carfagni. The variational approach to fracture mechanics. A practical application to the French Panthéon in Paris. Journal of Elasticity, 95(1):1–30, 2009. [Cited on pages 2, 13, 28, and 34] 





C. J. Larsen, C. Ortner, and E. Sali. Existence of solutions to a regularized model of dynamic fracture. Mathematical Models and Methods in Applied Sciences, 20(07):1021–1048, 2010. [Cited on page 17] 





R. Larsson, J. Mediavilla, and M. Fagerström. Dynamic fracture modeling in shell structures based on XFEM. International Journalfor Numerical Methods in Engineering, 86(4-5):499–527, 2011. [Cited on page 19] 





S. Lee, A. Mikelic, M. F. Wheeler, and T. Wick. Phase-field modeling of proppant-filled fractures in a ´ poroelastic medium. Computer Methods in Applied Mechanics and Engineering, 312:509 – 541, 2016a. [Cited on pages 19 and 80] 





S. Lee, M. F. Wheeler, and T. Wick. Pressure and fluid-driven fracture propagation in porous media using an adaptive finite element phase field model. Computer Methods in Applied Mechanics and Engineering, 305:111 – 132, 2016b. [Cited on pages 18 and 19] 





S. Lee, M. F. Wheeler, and T. Wick. Iterative coupling of flow, geomechanics and adaptive phase-field fracture including level-set crack width approaches. Journal ofComputational and Applied Mathematics, 314:40 – 60, 2017a. [Cited on pages 19 and 80] 





S. Lee, M. F. Wheeler, T. Wick, and S. Srinivasan. Initialization of phase-field fracture propagation in porous media using probability maps of fracture networks. Mechanics Research Communications, 80:16 – 23, 2017b. [Cited on page 71] 





B. Li, A. Kidane, G. Ravichandran, and M. Ortiz. Verification and validation of the optimal transportation meshfree (OTM) simulation of terminal ballistics. International Journal ofImpact Engineering, 42:25 – 36, 2012. [Cited on page 15] 





B. Li, A. Pandolfi, and M. Ortiz. Material-point erosion simulation of dynamic fragmentation of metals. Mechanics ofMaterials, 80, Part B:288 – 297, 2015a. [Cited on page 15] 





B. Li, C. Peco, D. Millán, I. Arias, and M. Arroyo. Phase-field modeling and simulation of fracture in brittle materials with strongly anisotropic surface energy. International Journalfor Numerical Methods in Engineering, 102(3-4):711–727, 2015b. [Cited on pages 13, 19, and 67] 





B. Li, D. Millan, A. Torres-Sanchez, B. Roman, and M. Arroyo. A variational model of fracture for tearing brittle thin sheets. Journal of the Mechanics and Physics of Solids, (119):334–348, 2018. [Cited on pages 19 and 67] 





T. Li, J.-J. Marigo, D. Guilbaud, and S. Potapov. Gradient damage modeling of brittle fracture in an explicit dynamics context. International Journalfor Numerical Methods in Engineering, 108(11):1381–1405, 2016. [Cited on pages 17, 33, 39, 65, 66, 67, 71, 95, 96, 97, and 100] 





W. Li and T. Siegmund. An analysis of crack growth in thin-sheet metal via a cohesive zone model. Engineering Fracture Mechanics, 69(18):2073–2093, 2002. [Cited on page 19] 





T. Liebe, P. Steinmann, and A. Benallal. Theoretical and computational aspects of a thermodynamically consistent framework for geometrically linear gradient damage. Computer Methods in Applied Mechanics and Engineering, 190:6555–6576, 2001. [Cited on pages 42 and 108] 





T. Linse, P. Hennig, M. Kästner, and R. de Borst. A convergence study of phase-field models for brittle fracture. Engineering Fracture Mechanics, 184:307–318, 2017. [Cited on page 29] 





G. Liu, K. Dai, and T. T. Nguyen. A smoothed finite element method for mechanics problems. Computational Mechanics, 39(6):859–877, 2007. [Cited on page 57] 





G. Liu, Q. Li, M. A. Msekh, and Z. Zuo. Abaqus implementation of monolithic and staggered schemes for quasi-static and dynamic fracture phase-field model. Computational Materials Science, 121:35 – 47, 2016. [Cited on pages 18, 65, 66, and 69] 





E. Lorentz. A nonlocal damage model for plain concrete consistent with cohesive fracture. International Journal ofFracture, 207:123–159, 2017. [Cited on pages 21, 42, and 53] 





E. Lorentz and S. Andrieux. A variational formulation for nonlocal damage models. International Journal of Plasticity, 15(2):119 – 138, 1999. [Cited on pages 7 and 42] 





E. Lorentz and V. Godard. Gradient damage models: Toward full-scale computations. Computer Methods in Applied Mechanics and Engineering, 200(21-22):1927 – 1944, 2011. [Cited on pages 42, 53, and 109] 





E. Lorentz, S. Cuvilliez, and K. Kazymyrenko. Convergence of a gradient damage model toward a cohesive zone model. Comptes Rendus Mécanique, 339(1):20 – 26, 2011. [Cited on page 36] 





E. Lorentz, S. Cuvilliez, and K. Kazymyrenko. Modelling large crack propagation: from gradient-damage to cohesive zone models. Int. J. Fract., 178:85–95, 2012. [Cited on pages 36 and 53] 





L. E. Malvern. Introduction to the Mechanics of a Continuous Medium. Prentice-Hall International, Englewood Cliffs, New Jersey, 1969. [Cited on page 7] 





T. K. Mandal, V. P. Nguyen, and A. Heidarpour. Phase field and gradient enhanced damage models for quasi-brittle failure: A numerical comparative study. Engineering Fracture Mechanics, 207(48–67), 2019. [Cited on page 40] 





J. J. Marigo, C. Maurini, and K. Pham. An overview of the modelling of fracture by gradient damage models. Meccanica, 51(12):3107–3128, 2016. [Cited on page 42] 





E. Martínez-Pañeda, A. Golahmar, and C. F. Niordson. A phase field formulation for hydrogen assisted cracking. Computer Methods in Applied Mechanics and Engineering, 2018. [Cited on pages 19 and 22] 





S. May, J. Vignollet, and R. de Borst. A numerical assessment of phase-field models for brittle and cohesive fracture: γ-convergence and stress oscillations. European Journal ofMechanics - A/Solids, 52:72 – 84, 2015. [Cited on pages 16 and 66] 





S. May, J. Vignollet, and R. de Borst. A new arc-length control method based on the rates of the internal and the dissipated energy. Engineering Computations, 33(1):100–115, 2016. [Cited on pages 60, 67, 68 and 110] 





J. Mazars, Y. Berthaud, and S. Ramtani. The unilateral behavior of damaged concrete. Engineering Fracture Mechanics, 35:629–635, 1990. [Cited on page 33] 





J. Mediavilla, R. Peerlings, and M. Geers. A robust and consistent remeshing-transfer operator for ductile fracture simulations. Computers & Structures, 84(8-9):604 – 623, 2006. [Cited on page 10] 





A. Mesgarnejad, B. Bourdin, and M. Khonsari. A variational approach to the fracture of brittle thin films subject to out-of-plane loading. Journal ofthe Mechanics and Physics ofSolids, 61(11):2360 – 2379, 2013. [Cited on pages 19 and 21] 





A. Mesgarnejad, B. Bourdin, and M. Khonsari. Validation simulations for the variational approach to fracture. Computer Methods in Applied Mechanics and Engineering, 290:420 – 437, 2015. [Cited on pages 18, 21, 22, and 56] 





C. Miehe and S. Mauthe. Phase field modeling of fracture in multi-physics problems. Part III. crack driving forces in hydro-poro-elasticity and hydraulic fracturing of fluid-saturated porous media. Computer Methods in Applied Mechanics and Engineering, 304:619 – 655, 2016. [Cited on pages 19 and 80] 





C. Miehe and L.-M. Schänzel. Phase field modeling of fracture in rubbery polymers. part i: Finite elasticity coupled with brittle failure. Journal ofthe Mechanics and Physics ofSolids, 65:93 – 113, 2014. [Cited on page 18] 





C. Miehe, M. Hofacker, and F. Welschinger. A phase field model for rate-independent crack propagation: Robust algorithmic implementation based on operator splits. Computer Methods in Applied Mechanics and Engineering, 199(45-48):2765 – 2778, 2010a. [Cited on pages 45, 59, 63, 67, 68, and 87] 





C. Miehe, F. Welschinger, and M. Hofacker. Thermodynamically consistent phase-field models of fracture: Variational principles and multi-field FE implementations. International Journalfor Numerical Methods in Engineering, 83(10):1273–1311, 2010b. [Cited on pages 2, 12, 15, 18, 28, 29, 30, 31, 34, 37, 39, 45, 55, 57, 63, 66, 67, and 106] 





C. Miehe, M. Hofacker, L.-M. Schänzel, and F. Aldakheel. Phase field modeling of fracture in multi-physics problems. Part II. coupled brittle-to-ductile failure criteria and crack propagation in thermo-elastic-plastic solids. Computer Methods in Applied Mechanics and Engineering, 294:486 – 522, 2015a. [Cited on pages 16, 18, and 19] 





C. Miehe, L.-M. Schaenzel, and H. Ulmer. Phase field modeling of fracture in multi-physics problems. Part I. balance of crack surface and failure criteria for brittle crack propagation in thermo-elastic solids. Computer Methods in Applied Mechanics and Engineering, 294:449 – 485, 2015b. [Cited on pages 18, 19, 28, and 38] 





A. Mikelic, M. F. Wheeler, and T. Wick. A phase-field method for propagating fluid-filled fractures coupled´ to a surrounding porous medium. Multiscale Modeling & Simulation, 13(1):367–398, 2015. [Cited on page 19] 





S. J. Mitchell, A. Pandolfi, and M. Ortiz. Effect of brittle fracture in a metaconcrete slab under shock loading. Journal ofEngineering Mechanics, 142(4):04016010, 2016. [Cited on page 15] 





N. Moës, J. Dolbow, and T. Belytschko. A finite element method for crack growth without remeshing. International Journalfor Numerical Methods in Engineering, 46(1):133–150, 1999. [Cited on page 8] 





N. Moës, A. Gravouil, and T. Belytschko. Non-planar 3d crack growth by the extended finite element and level sets—part i: Mechanical model. International journalfor numerical methods in engineering, 53 (11):2549–2568, 2002. [Cited on page 72] 





N. Moës, C. Stolz, P.-E. Bernard, and N. Chevaugeon. A level set based model for damage growth: The thick level set approach. International Journalfor Numerical Methods in Engineering, 86(3):358–380, 2011. [Cited on pages 10 and 15] 





G. Molnár and A. Gravouil. 2D and 3D Abaqus implementation of a robust staggered phase-field solution for modeling brittle fracture. Finite Elements in Analysis and Design, 130:27 – 38, 2017. [Cited on page 66] 





P. Moonen, J. Carmeliet, and L. Sluys. A continuous-discontinuous approach to simulate fracture processes in quasi-brittle materials. Philosophical Magazine, 88(28-29):3281–3298, 2008. [Cited on page 10] 





G. Moutsanidis, D. Kamensky, J. Chen, and Y. Bazilevs. Hyperbolic phase field modeling of brittle fracture: Part II immersed iga–rkpm coupling for air-blast–structure interaction. Journal ofthe Mechanics and Physics ofSolids, 121:114–132, 2018. [Cited on pages 15, 18, and 104] 





M. A. Msekh, J. M. Sargado, M. Jamshidian, P. M. Areias, and T. Rabczuk. Abaqus implementation of phase-field model for brittle fracture. Computational Materials Science, 96, Part B:472 – 484, 2015. [Cited on page 66] 





D. Mumford and J. Shah. Optimal approximations by piecewise smooth functions and associated variational problems. Communications on Pure and Applied Mathematics, 42(5):577–685, 1989. [Cited on pages 11 and 13] 





S. Natarajan, S. P. Bordas, and E. T. Ooi. Virtual and smoothed finite elements: a connection and its application to polygonal/polyhedral finite element methods. International Journal for Numerical Methods in Engineering, 104(13):1173–1199, 2015. [Cited on page 66] 





N. Newmark. A method of computation for structural dynamics. Journal ofEngineering Mechanics, 85: 67–94, 1956. [Cited on page 63] 





D. Ngo and A. C. Scordelis. Finite element analysis of reinforced-concrete beams. Journal of the American Concrete Institute, 65(9):757–766, 1967. [Cited on page 8] 





T. Nguyen, J. Yvonnet, Q.-Z. Zhu, M. Bornert, and C. Chateau. A phase field method to simulate crack nucleation and propagation in strongly heterogeneous materials from direct imaging of their microstructure. Engineering Fracture Mechanics, 139:18 – 39, 2015a. [Cited on page 66] 





T. Nguyen, J. Yvonnet, Q.-Z. Zhu, M. Bornert, and C. Chateau. A phase-field method for computational modeling of interfacial damage interacting with crack propagation in realistic microstructures obtained by microtomography. Computer Methods in Applied Mechanics and Engineering, 312:567 – 595, 2016a. [Cited on pages 16, 17, and 21] 





T. T. Nguyen, J. Yvonnet, M. Bornert, C. Chateau, K. Sab, R. Romani, and R. Le Roy. On the choice of parameters in the phase field method for simulating crack initiation with experimental validation. International Journal ofFracture, 197(2):213–226, 2016b. [Cited on pages 12, 21, 22, and 56] 





T. T. Nguyen, J. Bolivar, J. Réthoré, M.-C. Baietto, and M. Fregonese. A phase field method for modeling stress corrosion crack propagation in a nickel base alloy. International Journal ofSolids and Structures, 112:65 – 82, 2017a. [Cited on pages 21 and 22] 





T. T. Nguyen, J. Bolivar, J. Rethore, M. C. Baietto, and M. Fregonese. A phase field method for modeling stress corrosion crack propagation in a nickel base alloy. Int. J. Solids Struct., 112:65–82, May 2017b. [Cited on page 19] 





T. T. Nguyen, J. Réthoré, and M. C. Baietto. Phase field modelling of anisotropic crack propagation. European Journal ofMechanics-A/Solids, 65:279–288, 2017c. [Cited on pages 19 and 20] 





T. T. Nguyen, D. Waldmann, and T. Bui. Role of interfacial transition zone in phase field modeling of fracture in layered heterogeneous structures. Submitted to Journal of Computational Physics, 2018. [Cited on page 21] 





V. Nguyen. An open source program to generate zero-thickness cohesive interface elements. Advances in Engineering Software, 74:27–39, 2014a. [Cited on page 67] 





V. Nguyen, T. Rabczuk, S. Bordas, and M. Duflot. Meshless methods: A review and computer implementation aspects. Mathematics and Computers in Simulation, 79(3):763–813, 2008. ISSN 0378-4754. [Cited on page 8] 





V. Nguyen, O. Lloberas-Valls, M. Stroeven, and L. J. Sluys. Homogenization-based multiscale crack modelling: from micro-diffusive damage to macro-cracks. Computer Methods in Applied Mechanics and Engineering, 200(9-12):1220–1236, 2011a. [Cited on page 10] 





V. Nguyen, M. Stroeven, and L. J. Sluys. An enhanced continuous-discontinuous multiscale method for modelling mode-I failure in random heterogeneous quasi-brittle materials. Engineering Fracture Mechanics, 79:78–102, 2012. [Cited on page 10] 





V. Nguyen, C. Nguyen, S. Najatarajan, and T. Rabczuk. On a family of convected particle domain integrators in the material point method. Finite Elements in Analysis and Design, 126:50–64, 2016c. [Cited on page 15] 





V. P. Nguyen. Discontinuous Galerkin/Extrinsic cohesive zone modeling: implementation caveats and applications in computational fracture mechanics. Engineering Fracture Mechanics, 128:37–68, 2014b. [Cited on pages 8, 17, 18, 74, 95, and 96] 





V. P. Nguyen and H. Nguyen-Xuan. High order B-splines based finite elements for the delamination analysis of laminated composites. Composite Structures, 200(9-12):1220–1236, 2012. [Cited on pages 8 and 110] 





V. P. Nguyen and J. Y. Wu. Modeling dynamic fracture of solids with a phase-field regularized cohesive zone model. Computer Methods in Applied Mechanics and Engineering, 340:1000–1022, 2018. [Cited on pages 17 and 102] 





V. P. Nguyen, M. Stroeven, and L. J. Sluys. Multiscale continuous and discontinuous modeling of heterogeneous materials: a review on recent developments. Journal of Multiscale Modelling, 3(04): 229–270, 2011b. [Cited on page 7] 





V. P. Nguyen, C. Anitescu, S. P. Bordas, and T. Rabczuk. Isogeometric analysis: An overview and computer implementation aspects. Mathematics and Computers in Simulation, 117:89 – 116, 2015b. [Cited on page 13] 





V. P. Nguyen, H. Lian, T. Rabczuk, and S. Bordas. Modelling hydraulic fractures in porous media using flow cohesive interface elements. Engineering Geology, 225:68–82, 2017d. [Cited on pages 56 and 67] 





A. A. Novotny and J. Sokolowski. Topological derivatives in shape optimization. Springer-Verlag, New York, 2013. [Cited on page 15] 





J. Oliver. Modelling strong discontinuities in solid mechanics via strain softening constitutive equations. part 1: Fundamentals. International journalfor numerical methods in engineering, 39(21):3575–3600, 1996. [Cited on page 8] 





M. Ortiz. A constitutive theory for inelastic behaviour of concrete. Mech. Mater., 4:67–93, 1985. [Cited on pages 34 and 106] 





M. Ortiz, Y. Leroy, and A. Needleman. A finite element method for localized failure analysis. Computer Methods in Applied Mechanics and Engineering, 61(2):189 – 214, 1987. [Cited on page 8] 





J. Ožbolt, J. Bošnjak, and E. Sola. Dynamic fracture of concrete compact tension specimen: Experimental and numerical study. International Journal ofSolids and Structures, 50(25):4270 – 4278, 2013. [Cited on page 17] 





M. Paggi and J. Reinoso. Revisiting the problem of a crack impinging on an interface: a modeling framework for the interaction between the phase field approach for brittle fracture and the interface cohesive zone model. Computer Methods in Applied Mechanics and Engineering, 321:145–172, 2017. [Cited on page 21] 





M. Paggi, M. Corrado, and J. Reinoso. Fracture of solar-grade anisotropic polycrystalline silicon: A combined phase field–cohesive zone model approach. Computer Methods in Applied Mechanics and Engineering, 330:123–148, 2018. [Cited on pages 21 and 69] 





Z. Pan, R. Ma, D. Wang, and A. Chen. A review of lattice type model in fracture mechanics: theory, applications, and perspectives. Engineering Fracture Mechanics, 190:382–409, 2018. [Cited on page 7] 





A. Pandolfi and M. Ortiz. An eigenerosion approach to brittle fracture. International Journalfor Numerical Methods in Engineering, 92(8):694–714, 2012. [Cited on page 15] 





A. Pandolfi, B. Li, and M. Ortiz. Modeling fracture by material-point erosion, pages 3–16. Springer International Publishing, Cham, 2014. [Cited on page 15] 





K. Park, G. H. Paulino, W. Celes, and R. Espinha. Adaptive mesh refinement and coarsening for cohesive zone modeling of dynamic fracture. International Journalfor Numerical Methods in Engineering, 92(1): 1–35, 2012. [Cited on pages 95 and 96] 





A. F. Parrinello. A Rate-Pressure-Dependent Thermodynamically-Consistent Phase Field Model for the Description of Failure Patterns in Dynamic Brittle Fracture. Phd thesis, University of Oxford, 2017. [Cited on pages 17 and 27] 





B. Patzák and M. Jirásek. Process zone resolution by extended finite elements. Engineering Fracture Mechanics, 70(7):957 – 977, 2003. [Cited on page 67] 





R. H. J. Peerlings, R. De Borst, W. A. M. Brekelmans, and J. H. P. De Vree. Gradient enhanced damage for quasi-brittle materials. International Journalfor Numerical Methods in Engineering, 39(19):3391–3403, 1996a. [Cited on pages 7, 40, 57, and 60] 





R. H. J. Peerlings, R. de Borst, W. A. M. Brekelmans, and J. de Wree. Gradient enhanced damage for quasi brittle materials. International Journal for Numerical Methods in Engineering, 39:3391–3403, 1996b. [Cited on page 41] 





L. Pereira, J. Weerheijm, and L. Sluys. A new rate-dependent stress-based nonlocal damage model to simulate dynamic tensile failure of quasi-brittle materials. International Journal ofImpact Engineering, 94:83 – 95, 2016. [Cited on pages 7 and 41] 





L. Pereira, J. Weerheijm, and L. Sluys. A numerical study on crack branching in quasi-brittle materials with a new effective rate-dependent nonlocal damage model. Engineering Fracture Mechanics, 182: 689–707, 2017. [Cited on pages 17, 95, and 96] 





K. Pham, H. Amor, J.-J. Marigo, and C. Maurini. Gradient damage models and their use to approximate brittle fracture. International Journal ofDamage Mechanics, 20(4):618–652, 2011. [Cited on pages 7, 15, 22, 23, 31, 32, 36, 42, 44, 49, 55, 56, 59, 62, and 108] 





K. H. Pham and K. Ravi-Chandar. The formation and growth of echelon cracks in brittle materials. International Journal ofFracture, 206(2):229–244, 2017. [Cited on page 18] 





K. H. Pham, K. Ravi-Chandar, and C. M. Landis. Experimental validation of a phase-field model for fracture. International Journal of Fracture, 205(1):83–101, 2017. [Cited on pages 21, 22, and 62] 





G. D. Piero, G. Lancioni, and R. March. A variational model for fracture mechanics: Numerical experiments. Journal of the Mechanics and Physics of Solids, 55(12):2513 – 2537, 2007. [Cited on pages 18, 69, and 70] 





G. Pijaudier-Cabot and Z. P. Bažant. Nonlocal damage theory. Journal ofEngineering Mechanics, 113: 1512–1533, 1987. [Cited on page 7] 





G. Pijaudier-Cabot and N. Burlion. Damage and localisation in elastic materials with voids. Int. J. Mechanics ofCohesive Frictional Materials, 1:129–144, 1996. [Cited on page 42] 





U. Pillai, Y. Heider, and B. Markert. A diffusive dynamic brittle fracture model for heterogeneous solids and porous materials with implementation using a user-element subroutine. Computational Materials Science, 153:36–47, 2018. [Cited on page 66] 





L. H. Poh and G. Sun. Localizing gradient damage model with decreasing interactions. International Journalfor Numerical Methods in Engineering, 110(6):503–522, 2017. [Cited on page 7] 





C. Polizzotto. Unified thermodynamic framework for nonlocal/gradient continuum theories. Eur. J. Mech. A/Solids, 22:651–668, 2003. [Cited on page 42] 





C. Polizzotto and G. Borino. A thermodynamics-based formulation of gradient-dependent plasticity. Eur. J. Mech. A/Solids, 17:741–761, 1998. [Cited on pages 42 and 108] 





N. M. Pugno and R. S. Ruoff. Quantized fracture mechanics. Philosophical Magazine, 84(27):2829–2845, 2004. [Cited on page 101] 





T. Rabczuk. Computational methods for fracture in brittle and quasi-brittle solids: State-of-the-art review and future perspectives. ISRN Applied Mathematics, 2013. doi: 10.1155/2013/849231. [Cited on page 10] 





T. Rabczuk and T. Belytschko. Cracking particles: a simplified meshfree method for arbitrary evolving cracks. International Journalfor Numerical Methods in Engineering, 61(13):2316–2343, 2004. [Cited on pages 17, 95, and 96] 





T. Rabczuk and T. Belytschko. A three-dimensional large deformation meshfree method for arbitrary evolving cracks. Computer Methods in Applied Mechanics and Engineering, 196(29-30):2777 – 2799, 2007. [Cited on page 17] 





T. Rabczuk, P. Areias, and T. Belytschko. A meshfree thin shell method for non-linear dynamic fracture. International Journalfor Numerical Methods in Engineering, 72(5):524–548, 2007. [Cited on page 19] 





T. Rabczuk, S. Bordas, and G. Zi. On three-dimensional modelling of crack growth using partition of unity methods. Computers & structures, 88(23-24):1391–1411, 2010. [Cited on pages 10 and 18] 





M. Radszuweit and C. Kraus. Modeling and simulation of non-isothermal rate-dependent damage processes in inhomogeneous materials using the phase-field approach. Computational Mechanics, 60(1):163–179, 2017. [Cited on page 19] 





A. Raina and C. Miehe. A phase-field model for fracture in biological tissues. Biomechanics and Modeling in Mechanobiology, 15(3):479–496, 2016. [Cited on page 18] 





E. Ramm. Strategies for tracing the nonlinear responses near limit points. In W. Wunderlich, E. Stein, and K. Bathe, editors, Nonlinear Finite Element Analysis in Structural Mechanics, pages 63–89. Springer-Verlag, 1981. [Cited on page 109] 





M. Ramulu and A. Kobayashi. Mechanics of crack curving and branching: a dynamic fracture analysis. International Journal of Fracture, 27(3-4):187–201, 1985. [Cited on page 95] 





Y. Rashid. Ultimate strength analysis of prestressed concrete pressure vessels. Nuclear Engineering and Design, 7(4):334 – 344, 1968. [Cited on page 8] 





K. Ravi-Chandar. Dynamic Fracture. Elsevier, Amsterdam, 2004. [Cited on page 93] 





H. Reinhardt and H. Cornelissen. Postpeak cyclic behavior of concrete in uniaxial tensile and alternating tensile and compressive loading. Cem. Concr. Res., 14:263–270, 1984. [Cited on page 33] 





J. Reinoso, M. Paggi, and C. Linder. Phase field modeling of brittle fracture for enhanced assumed strain shells at large deformations: formulation and finite element implementation. Computational Mechanics, pages 1–21, 2017. [Cited on page 19] 





B. Ren and S. Li. Modeling and simulation of large-scale ductile fracture in plates and shells. International Journal of Solids and Structures, 49(18):2373–2393, 2012. [Cited on page 19] 





E. Riks. An incremental approach to the solution of snapping and buckling problems. International Journal ofSolids and Structures, 15(7):529–551, 1979. [Cited on page 109] 





J. J. Ródenas, O. A. González-Estrada, J. E. Tarancón, and F. J. Fuenmayor. A recovery-type error estimator for the extended finite element method based on singular+ smooth stress field splitting. International Journalfor Numerical Methods in Engineering, 76(4):545–571, 2008. [Cited on pages 70 and 81] 





J. G. Rots. Smeared and discrete representations of localized fracture. International Journal of Fracture, 51(1):45–59, 1991. [Cited on page 8] 





C. L. Rountree, R. K. Kalia, E. Lidorikis, A. Nakano, L. V. Brutzel, and P. Vashishta. Atomistic aspects of crack propagation in brittle materials: Multimillion atom molecular dynamics simulations. Annual Review of Materials Research, 32(1):377–400, 2002. [Cited on page 7] 





P. Roy, S. Deepu, A. Pathrikar, and D. Roy. Phase field based peridynamics damage model for delamination of composite structures. Composite Structures, 180:972?993, 2017a. [Cited on page 9] 





P. Roy, A. Pathrikar, S. Deepu, and D. Roy. Peridynamics damage model through phase field theory. International Journal ofMechanical Sciences, 128-129:181–193, 2017b. [Cited on page 9] 





D. Santillán, J. C. Mosquera, and L. Cueto-Felgueroso. Phase-field model for brittle fracture. validation with experimental results and extension to dam engineering problems. Engineering Fracture Mechanics, 178:109 – 125, 2017. [Cited on pages 21 and 22] 





J. M. Sargado, E. Keilegavlen, I. Berre, and J. M. Nordbotten. High-accuracy phase-field models for brittle fracture based on a new family of degradation functions. Journal ofthe Mechanics and Physics ofSolids, 111:458–489, 2018. [Cited on page 36] 





S. Saroukhani, R. Vafadari, and A. Simone. A simplified implementation of a gradient-enhanced damage model with transient length scale effects. Computational Mechanics, 51(6):899–909, 2013. [Cited on page 41] 





D. Schillinger, M. J. Borden, and H. K. Stolarski. Isogeometric collocation for phase-field fracture models. Computer Methods in Applied Mechanics and Engineering, 284:583 – 610, 2015. [Cited on page 66] 





E. Schlangen and J. Van Mier. Simple lattice model for numerical simulation of fracture of concrete materials and structures. Materials and Structures, 25(9):534–542, 1992. [Cited on page 7] 





A. Schlüter, A. Willenbücher, C. Kuhn, and R. Müller. Phase field approximation of dynamic brittle fracture. Computational Mechanics, 54(5):1141–1161, 2014. [Cited on pages 17, 65, 71, 95, and 96] 





A. Schlüter, C. Kuhn, and R. Müeller. Simulation of laser-induced controlled fracturing utilizing a phase field model. ASME. Journal ofComputing and Information Science in Engineering, 2016. [Cited on page 19] 





B. Schmidt, F. Fraternali, and M. Ortiz. Eigenfracture: An eigendeformation approach to variational fracture. Multiscale Modeling & Simulation, 7(3):1237–1266, 2009. [Cited on page 15] 





L. Scholtès and F.-V. Donzé. Modelling progressive failure in fractured rock masses using a 3d discrete element method. International Journal ofRock Mechanics and Mining Sciences, 52:18–30, 2012. [Cited on page 7] 





M. Seiler, P. Hantschke, A. Brosius, and M. Kästner. A numerically efficient phase-field model for fatigue fracture - 1d analysis. PAMM, 18(1):e201800207, Dec 2018. [Cited on page 21] 





P. Seleson, M. L. Parks, M. Gunzburger, and R. B. Lehoucq. Peridynamics as an upscaling of molecular dynamics. Multiscale Modeling & Simulation, 8(1):204–227, 2009. [Cited on page 11] 





P. Shanthraj, B. Svendsen, L. Sharma, F. Roters, and D. Raabe. Elasto-viscoplastic phase field modelling of anisotropic cleavage fracture. Journal ofthe Mechanics and Physics ofSolids, 99:19 – 34, 2017. [Cited on page 19] 





E. Sharon and J. Fineberg. Microbranching instability and the dynamic fracture of brittle materials. Physical Review B, 54:7128–7139, 1996. [Cited on page 95] 





B. Shen and O. Stephansson. Modification of the G-criterion for crack propagation subjected to compression. Engineering Fracture Mechanics, 47(2):177 – 189, 1994. [Cited on page 20] 





P. Sicsic and J. Marigo. From gradient damage laws to Griffith’s theory of crack propagation. J. Elasticity, 113(1):55–74, 2013. [Cited on page 42] 





G. C. Sih. Energy-density concept in fracture mechanics. Engineering Fracture Mechanics, 5:1037–1040, 1973. [Cited on page 8] 





S. A. Silling. Reformulation of elasticity theory for discontinuities and long-range forces. Journal of the Mechanics and Physics ofSolids, 48(1):175–209, 2000. [Cited on page 8] 





S. A. Silling and E. Askari. A meshfree method based on the peridynamic model of solid mechanics. Computers & Structures, 83(17-18):1526 – 1535, 2005. [Cited on page 11] 





J. Simó and J. Ju. Strain- and stress-based continuum damage models. i: Formulation; ii: Computational aspects. Int. J. Solids Structure, 23(7):821–869, 1987. [Cited on page 39] 





J. C. Simo and J. W. Ju. Strain- and stress-based continuum damage models-I. formulation. International Journal of Solids and Structures, 23(7):821–840, 1987. [Cited on page 7] 





J. C. Simo, J. Oliver, and F. Armero. An analysis of strong discontinuities induced by strain-softening in rate-independent inelastic solids. Computational Mechanics, 12(5):277–296, 1993. [Cited on page 8] 





A. Simone, G. N. Wells, and L. J. Sluys. From continuous to discontinuous failure in a gradient-enhanced continuum damage model. Computer Methods in Applied Mechanics and Engineering, 192(41-42):4581 – 4607, 2003. [Cited on page 10] 





A. Simone, H. Askes, R. Peerlings, and L. Sluys. Interpolation requirements for implicit gradient-enhanced continuum damage models. Commun. Numer. Meth. Engng., 19:563–572, 2004. [Cited on page 57] 





L. Simoni and B. A. Schrefler. Multi field simulation of fracture. In Advances in Applied Mechanics, volume 47, pages 367–519. Elsevier, 2014. [Cited on page 56] 





S. Sinaie, V. P. Nguyen, C. T. Nguyen, and S. Bordas. Programming the material point method in Julia. Advances in Engineering Software, 105:17–29, Mar 2017. [Cited on page 15] 





S. Sinaie, T. D. Ngo, and V. P. Nguyen. A discrete element model of concrete for cyclic loading. Computers & Structures, 196:173 – 185, 2018a. [Cited on page 7] 





S. Sinaie, T. D. Ngo, V. P. Nguyen, and T. Rabczukc. Validation of the material point method for the simulation of thin-walled tubes under lateral compression. Thin-Walled Structures, 130:32–46, 2018b. [Cited on page 15] 





N. Singh, C. Verhoosel, R. de Borst, and E. van Brummelen. A fracture-controlled path-following technique for phase-field modeling of brittle fracture. Finite Elements in Analysis and Design, 113:14 – 29, 2016. [Cited on pages 60, 66, 67, 68, and 72] 





J.-H. Song, H. Wang, and T. Belytschko. A comparative study on finite element methods for dynamic fracture. Computational Mechanics, 42(2):239–250, 2008. [Cited on pages 17, 95, and 96] 





R. Spatschek, E. Brener, and A. Karma. Phase field modeling of crack propagation. Philosophical Magazine, 91:75 – 95, 2011. [Cited on pages 10 and 15] 





A. Staroselsky, R. Acharya, and B. Cassenti. Phase field modeling of fracture and crack growth. Engineering Fracture Mechanics, 2018. [Cited on page 27] 





C. Steinke and M. Kaliske. A phase-field crack model based on directional stress decomposition. Computational Mechanics, pages 1–28, 2018. [Cited on page 33] 





C. Steinke, K. Özenç, G. Chinaryan, and M. Kaliske. A comparative study of the r-adaptive material force approach and the phase-field method in dynamic fracture. International Journal of Fracture, 201(1): 97–118, 2016a. [Cited on page 66] 





C. Steinke, I. Zreid, and M. Kaliske. On the relation between phase-field crack approximation and gradient damage modelling. Computational Mechanics, pages 1–19, 2016b. [Cited on page 40] 





M. Stolarska, D. L. Chopp, N. Moës, and T. Belytschko. Modelling crack growth by level sets in the extended finite element method. International Journalfor Numerical Methods in Engineering, 51(8): 943–960, 2001. [Cited on page 72] 





M. Strobl and T. Seelig. On constitutive assumptions in phase field approaches to brittle fracture. Procedia Structural Integrity, 2:3705 – 3712, 2016. 21st European Conference on Fracture, ECF21, 20-24 June 2016, Catania, Italy. [Cited on page 71] 





N. Sukumar, J. E. Dolbow, and N. Moës. Extended finite element method in computational fracture mechanics: a retrospective examination. International Journal of Fracture, 196(1):189–206, 2015. [Cited on pages 8 and 10] 





D. Sulsky, Z. Chen, and H. Schreyer. A particle method for history-dependent materials. Computer Methods in Applied Mechanics and Engineering, 5:179–196, 1994. [Cited on page 15] 





D. Sutula, P. Kerfriden, T. van Dam, and S. P. Bordas. Minimum energy multiple crack propagation. Part I: Theory and state of the art review. Engineering Fracture Mechanics, 191:202–224, 2018a. [Cited on pages 8, 78, 79, 80, and 81] 





D. Sutula, P. Kerfriden, T. van Dam, and S. P. Bordas. Minimum energy multiple crack propagation. Part II: Discrete solutions with XFEM. Engineering Fracture Mechanics, 191:225–256, 2018b. [Cited on pages 78, 79, 80, and 81] 





D. Sutula, P. Kerfriden, T. van Dam, and S. P. Bordas. Minimum energy multiple crack propagation. Part III: XFEM computer implementation and applications. Engineering Fracture Mechanics, 191:257–276, 2018c. [Cited on pages 78, 79, 80, and 81] 





H. Talebi, M. Silani, S. P. A. Bordas, P. Kerfriden, and T. Rabczuk. Molecular dynamics/XFEM coupling by a three-dimensional extended bridging domain with applications to dynamic brittle fracture. International Journalfor Multiscale Computational Engineering, 11(6), 2013. [Cited on page 7] 





H. Talebi, M. Silani, S. P. A. Bordas, P. Kerfriden, and T. Rabczuk. A computational library for multiscale modeling of material failure. Computational Mechanics, 53(5):1047–1071, 2014. [Cited on page 7] 





E. Tanné, T. Li, B. Bourdin, J.-J. Marigo, and C. Maurini. Crack initiation in variational phase-field models of brittle fracture. Journal ofthe Mechanics and Physics ofSolids, 110:80–99, 2018. [Cited on pages 15 and 21] 





S. Teichtmeister, D. Kienle, F. Aldakheel, and M.-A. Keip. Phase field modeling of fracture in anisotropic brittle solids. International Journal ofNon-Linear Mechanics, 97:1 – 21, 2017. [Cited on pages 19, 20, and 67] 





B. Trunk. Einfluss der Bauteilgrösse aufdie Bruchenergie von Beton. Aedificatio Publishers, Freiburg, 2000. [Cited on pages 88 and 90] 





H. Ulmer, M. Hofacker, and C. Miehe. Phase field modeling of fracture in plates and shells. PAMM, 12(1): 171–172, 2012. [Cited on page 19] 





J. Unger, S. Eckardt, and C. Könke. Modelling of cohesive crack growth in concrete structures with the extended finite element method. Comput. Methods Appl. Mech. Engrg., 196:4087–4100, 2007. [Cited on page 90] 





F. P. van der Meer. Mesolevel modeling of failure in composite laminates: Constitutive, kinematic and algorithmic aspects. Archives ofComputational Methods in Engineering, 19(3):381–425, 2012. [Cited on pages 21 and 110] 





B. Vandoren and A. Simone. Modeling and simulation of quasi-brittle failure with continuous anisotropic stress-based gradient-enhanced damage models. Comput. Methods Appl. Mech. Engrg., 332:644–685, 2018. [Cited on pages 7 and 41] 





C. V. Verhoosel and R. de Borst. A phase-field model for cohesive fracture. International Journal for Numerical Methods in Engineering, 96(1):43–62, 2013. [Cited on pages 16 and 17] 





C. V. Verhoosel, J. J. C. Remmers, and M. A. Gutiérrez. A dissipation-based arc-length method for robust simulation of brittle and ductile failure. International Journal for Numerical Methods in Engineering, 77(9):1290–1321, 2009. [Cited on page 110] 





J. Vignollet, S. May, R. de Borst, and C. V. Verhoosel. Phase-field models for brittle and cohesive fracture. Meccanica, 49(11):2587–2601, 2014. [Cited on page 16] 





G. Vigueras, F. Sket, C. Samaniego, L. Wu, L. Noels, D. Tjahjanto, E. Casoni, G. Houzeaux, A. Makradi, J. M. Molina-Aldareguia, et al. An XFEM/CZM implementation for massively parallel simulations of composites fracture. Composite Structures, 125:542–557, 2015. [Cited on pages 13 and 21] 





K. Wang and W. C. Sun. A unified variational eigen-erosion framework for interacting brittle fractures and compaction bands in fluid-infiltrating porous media. Computer Methods in Applied Mechanics and Engineering, 318:1 – 32, 2017. [Cited on page 15] 





G. N. Wells and L. J. Sluys. A new method for modelling cohesive cracks using finite elements. International Journalfor Numerical Methods in Engineering, 50(12):2667–2682, 2001. [Cited on page 8] 





T. Wick. Goal functional evaluations for phase-field fracture using PU-based DWR mesh adaptivity. Computational Mechanics, 57(6):1017–1035, 2016. [Cited on page 69] 





T. Wick. Modified newton methods for solving fully monolithic phase-field quasi-static brittle fracture propagation. Comput. Methods Appl. Mech. Engrg., 325:577–611, 2017. [Cited on page 68] 





Z. A. Wilson, M. J. Borden, and C. M. Landis. A phase-field model for fracture in piezoelectric ceramics. International Journal ofFracture, 183(2):135–153, 2013. [Cited on pages 36 and 106] 





B. Winkler. Traglastuntersuchungen von unbewehrten und bewehrten Betonstrukturen aufder Grundlage eines objektiven Werkstoffgesetzesfür Beton. PhD thesis, Universitat Innsbruck, Austria, 2001. [Cited on pages 90 and 92] 





C. Wolff, N. Richart, and J.-F. Molinari. A non-local continuum damage approach to model dynamic crack branching. International Journal for Numerical Methods in Engineering, 101(12), 2015. [Cited on page 17] 





P. Wriggers and J. Simó. A general procedure for the direct computation of turning and bifurcation points. Int. J. Numer. Meth. Engng., 30:155–176, 1990. [Cited on page 110] 





J. Y. Wu. Unified analysis of enriched finite elements for modeling cohesive cracks. Computer Methods in Applied Mechanics and Engineering, 200:3031–3050, 2011. [Cited on pages 8, 55, and 67] 





J. Y. Wu. A unified phase-field theory for the mechanics of damage and quasi-brittle failure. Journal of the Mechanics and Physics ofSolids, 103:72 – 99, 2017. [Cited on pages 15, 17, 21, 23, 27, 30, 31, 32, 36, 37, 39, 42, 44, 48, 50, 51, 53, 55, 57, 63, 67, 86, 88, 93, 95, 102, 108, and 109] 





J. Y. Wu. Robust numerical implementation of non-standard phase-field damage models for failure in solids. Computer Methods in Applied Mechanics and Engineering, 340(767-797), 2018a. [Cited on pages 23, 37, 39, 63, 67, 69, 87, 88, and 110] 





J. Y. Wu. A geometrically regularized gradient-damage model with energetic equivalence. Computer Methods in Applied Mechanics and Engineering, 328:612–637, 2018b. [Cited on pages 15, 17, 21, 23, 27, 31, 37, 39, 42, 53, 55, 57, 63, 67, 88, 102, and 109] 





J. Y. Wu and M. Cervera. A novel positive/negative projection in energy norm for the damage modeling of quasi-brittle solids. International Journal ofSolids and Structures, 139-140:250–269, 2018. [Cited on pages 34, 35, 37, 105, and 106] 





J. Y. Wu and F. B. Li. An improved stable XFEM (Is-XFEM) with a novel enrichment function for the computational modeling of cohesive cracks. Computer Methods in Applied Mechanics and Engineering, 295:77–107, 2015. [Cited on page 8] 





J. Y. Wu and V. P. Nguyen. A length scale insensitive phase-field damage model for brittle fracture. Journal ofthe Mechanics and Physics ofSolids, 119:20–42, 2018. [Cited on pages 2, 17, 23, 35, 37, 49, 53, 55, 77, 86, 88, 95, and 106] 





J. Y. Wu and S. L. Xu. Reconsideration on the elastic damage/degradation theory for the modeling of microcrack closure-reopening (mcr) effects. International Journal ofSolids and Structures, 50:795–805, 2013. [Cited on pages 34, 35, and 105] 





J. Y. Wu, F. B. Li, and S. L. Xu. Extended embedded finite elements with continuous displacement jumps for the modeling of localized failure in solids. Computer Methods in Applied Mechanics and Engineering, 285:346–378, 2015. [Cited on page 8] 





J. Y. Wu, J.-F. Qiu, V. P. Nguyen, T. K. Mandal, and L. J. Zhuang. Computational modeling of localized failure in solids: XFEM vs PF-CZM. Computer Methods in Applied Mechanics and Engineering, 2018. [Cited on pages 13, 17, 23, 53, 57, 88, 90, and 101] 





T. Wu and L. D. Lorenzis. A phase-field approach to fracture coupled with diffusion. Computer Methods in Applied Mechanics and Engineering, 312:196 – 223, 2016. [Cited on page 19] 





T. Wu, A. Carpiuc-Prisacari, M. Poncelet, and L. D. Lorenzis. Phase-field simulation of interactive mixedmode fracture tests on cement mortar with full-field displacement boundary conditions. Engineering Fracture Mechanics, 182:658–688, 2017. [Cited on page 22] 





M. Xavier, E. A. Fancello, J. M. C. Farias, N. V. Goethem, and A. A. Novotny. Topological derivative-based fracture modelling in brittle materials: A phenomenological approach. Engineering Fracture Mechanics, 179:13–27, 2017. [Cited on page 15] 





X. Xu and A. Needleman. Numerical simulations of fast crack growth in brittle solids. Journal of the Mechanics and Physics ofSolids, 42(9), 1994. [Cited on page 8] 





T. Yalcinkaya, W. Brekelmans, and M. Geers. Deformation patterning driven by rate dependent non-convex strain gradient plasticity. Journal ofthe Mechanics and Physics ofSolids, 59(1):1 – 17, 2011. [Cited on page 14] 





Z.-J. Yang, B.-B. Li, and J. Y. Wu. X-ray computed tomography images based phase-field modeling of mesoscopic failure in concrete. Engineering Fracture Mechanics, 208:151–170, 2019. [Cited on page 17] 





O. Yılmaz, J. Bleyer, and J. F. Molinari. Influence of heterogeneities on crack propagation. International Journal ofFracture, 209(1-2):77–90, 2018. [Cited on page 18] 





P. D. Zavattieri. Modeling of crack propagation in thin-walled structures using a cohesive model for shell elements. Journal of applied mechanics, 73(6):948–958, 2006. [Cited on page 19] 





P. Zhang, X. Hu, X. Wang, and W. Yao. An iteration scheme for phase field model for cohesive fracture and its implementation in abaqus. Engineering Fracture Mechanics, 2018. [Cited on pages 66 and 69] 





X. Zhang, S. W. Sloan, C. Vignes, and D. Sheng. A modification of the phase-field model for mixed mode crack propagation in rock-like materials. Computer Methods in Applied Mechanics and Engineering, 322:123 – 136, 2017a. [Cited on pages 20, 38, and 82] 





X. Zhang, C. Vignes, S. W. Sloan, and D. Sheng. Numerical evaluation of the phase-field model for brittle fracture with emphasis on the length scale. Computational Mechanics, pages 1–16, 2017b. [Cited on pages 21, 22, and 56] 





H. Zheng, F. Liu, and X. Du. Complementarity problem arising from static growth of multiple cracks and mls-based numerical manifold method. Computer Methods in Applied Mechanics and Engineering, 295: 150 – 171, 2015. [Cited on page 78] 





S. Zhou, T. Rabczuk, and X. Zhuang. Phase field modeling of quasi-static and dynamic crack propagation: Comsol implementation and case studies. Advances in Engineering Software, 122:31–49, 2018a. [Cited on page 66] 





S. Zhou, X. Zhuang, and T. Rabczuk. A phase-field modeling approach of fracture propagation in poroelastic media. Engineering Geology, 240:189–203, 2018b. [Cited on page 19] 





S. Zhou, X. Zhuang, H. Zhu, and T. Rabczuk. Phase field modelling of crack propagation, branching and coalescence in rocks. Theoretical and Applied Fracture Mechanics, 96:174–192, 2018c. [Cited on page 20] 





V. Ziaei-Rad and Y. Shen. Massive parallelization of the phase field formulation for crack propagation with time adaptivity. Computer Methods in Applied Mechanics and Engineering, 312:224 – 253, 2016. [Cited on pages 65 and 66] 





V. Ziaei-Rad, L. Shen, J. Jiang, and Y. Shen. Identifying the crack path for the phase field approach to fracture with non-maximum suppression. Computer Methods in Applied Mechanics and Engineering, 312:304 – 321, 2016. [Cited on pages 65 and 74] 





O. C. Zienkiewicz and R. L. Taylor. The Finite Element Method for Solid and Structural Mechanics. Butterworth-Heinemann, Oxford, UK, sixth edition, 2006. [Cited on pages 8 and 58] 

