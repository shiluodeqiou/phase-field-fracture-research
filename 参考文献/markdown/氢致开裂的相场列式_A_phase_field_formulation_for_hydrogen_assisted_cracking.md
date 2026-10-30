# A phase field formulation for hydrogen assisted cracking

Emilio Martínez-Pañeda<sup>a,∗</sup>, Alireza Golahmar<sup>b</sup>, Christian F. Niordson<sup>b</sup> 

<sup>a</sup> Department ofEngineering, University ofCambridge, CB2 1PZ Cambridge, UK 

<sup>b</sup> Department of Mechanical Engineering, Technical University of Denmark, DK-2800 kgs. Lyngby, Denmark 

Received 26 January 2018; received in revised form 5 July 2018; accepted 19 July 2018 Available online 25 July 2018 

## Abstract

We present a phase field modeling framework for hydrogen assisted cracking. The model builds upon a coupled mechanica and hydrogen diffusion response, driven by chemical potential gradients, and a hydrogen-dependent fracture energy degradation law grounded on first principles calculations. The coupled problem is solved in an implicit time integration scheme, where displacements, phase field order parameter and hydrogen concentration are the primary variables. We show that phase field formulations for fracture are particularly suitable to capture material degradation due to hydrogen. Specifically, we model (i) unstable crack growth in the presence of hydrogen, (ii) failure stress sensitivity to hydrogen content in notched specimens, (iii) cracking thresholds under constant load, (iv) internal hydrogen assisted fracture in cracked specimens, and (v) complex crack paths arising from corrosion pits. Computations reveal a good agreement with experiments, highlighting the predictive capabilities of the present scheme. The work could have important implications for the prediction and prevention of catastrophic failures in corrosive environments. The finite element code developed can be downloaded from www.empaneda.com/codes. @ 2018 Elcevier R V, A1l ri 

Keywords: Phase field; Hydrogen embrittlement; Stress-assisted diffusion; Finite element analysis; Fracture 

## 1. Introduction

Hydrogen has been known for over a hundred years to cause catastrophic failure in metallic materials [1]. Hydrogen atoms enter the material, migrate through the crystal lattice and induce fracture, with cracking being observed in modern steels at one-tenth of the expected fracture toughness. Hydrogen embrittlement is a pervasive problem in the manufacturing, transport, and energy sectors and could compromise the key role of hydrogen as next-generation energy resource. There is a strong need to understand and model how hydrogen degrades the ductility and the fracture resistance of metals. 

Modeling efforts in the hydrogen embrittlement community have been largely restricted to discrete numerical methods. Crack initiation thresholds and growth rates have been computed through dislocation-based methods [2,3], weakest-link approaches [4,5], and, eminently, cohesive zone models [6–10], which can easily incorporate the cohesive strength reduction with hydrogen coverage. These methods are however limited when dealing with the complex conditions of practical applications and many important challenges (mixed mode, interacting cracks, complex distribution of initiation sites, etc.) remain unaddressed. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/f51fc7773cce9baa1863e701cbfedef45afd71e60e8586d07a1cdb32a2fa1f0b.jpg)



Fig. 1. Sharp (a) and diffusive (b) crack topologies.


The phase field method for fracture has emerged as a promising variational approach to overcome the limitations of discontinuity-based methods. The method has received increasing attention since the earlier work by Francfort and Marigo [11] and important efforts have been devoted to improve solution schemes [12,13], discretization strategies [14,15] and implementation aspects [16,17]. The model builds upon Griffith’s thermodynamics framework and has not only been successfully applied to model brittle fracture but also to ductile damage [18,19], hydraulic fracturing [20,21], composites delamination [22,23], and stress corrosion cracking [24,25], to name a few. The phase field method is particularly well suited to capture the fracture energy dependence on hydrogen concentration, and will allow addressing the complex cracking conditions intrinsic to hydrogen embrittlement in industrial components 

In this work, we develop a novel variational framework for hydrogen assisted cracking. Hydrogen transport towards the fracture process zone and subsequent cracking are investigated by means of a coupled mechanical-diffusion-phase field finite element framework. The numerical scheme is grounded on: (i) a phase field description of fracture, (ii) an extension of Fick’s law for mass diffusion, and (iii) a quantum-based relation between the hydrogen content and the fracture surface energy. We demonstrate the potential of the proposed modeling framework by means of representative case studies. The remainder of the paper is organized as follows. Section 2 describes the hydrogen-dependent phase field formulation. Section 3 provides details of the stress-assisted impurity diffusion scheme and its coupling with the phase field model. In Section 4 model predictions are benchmarked against relevant experimental measurements. Finally, concluding remarks are given in Section 5. 

## 2. A phase field formulation for hydrogen embrittlement

## 2.1. Phase field approximation of fracture

In a one-dimensional setting, the topology of a sharp crack (see Fig. 1a) can be described by an auxiliary field variable $\phi ( x ) \in [ 0 , 1 ]$ with 

$$
\phi (x) = \left\{ \begin{array}{l l} 1 & \quad \text { if } x = 0 \\ 0 & \quad \text { if } x \neq 0 \end{array} \right.\tag{1}
$$

which is referred to as the crack phase field order parameter, with $\phi = 0$ and $\phi = 1$ respectively denoting the intact and fully broken states of the material. The non-smooth crack phase field (1) can be approximated by the exponential function, 

$$
\phi (x) = \mathrm{e} ^ {- \frac {| x |}{\ell}}\tag{2}
$$

representing a regularized or diffusive crack topology, as illustrated in Fig. 1b. The length scale parameter ℓ determines the width of the smearing function, approaching the discrete crack topology as $\ell \to 0$ 

Consider a discrete internal discontinuity Γ in a solid body Ω (Fig. 2a), a regularized crack functional $\varGamma _ { \ell }$ can be defined (Fig. 2b) 

$$
\Gamma_ {\ell} (\phi) = \int_ {\Omega} \left(\frac {1}{2 \ell} \phi^ {2} + \frac {\ell}{2} | \nabla \phi | ^ {2}\right) d V = \int_ {\Omega} \gamma_ {\ell} (\phi , \nabla \phi) d V\tag{3}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/ece626ae38ff4be560f3ead37e348fe4bc4b5ae7d010d5372f2dbdde71a23381.jpg)



Fig. 2. Schematic representation of a solid body with (a) internal discontinuity boundaries, and (b) a phase field approximation of the discret discontinuities. Source: Adapted from [26]


that Γ-converges to the functional of the discrete crack surface for a vanishing length scale parameter $\ell \ \to \ 0$ Here, $\gamma _ { \ell } ( \phi , \nabla \phi )$ is the crack surface density function. Consequently, the phase field method for fracture circumvents numerical complications inherent to tracking the evolving discontinuity boundary Γ, enabling to robustly model interactions and branching of cracks of arbitrary topological complexity [26]. The fracture energy due to the formation of a crack is then approximated as, 

$$
\int_ {\Gamma} G _ {c} (\theta) \mathrm{d} S \approx \int_ {\Omega} G _ {c} (\theta) \left(\frac {1}{2 \ell} \phi^ {2} + \frac {\ell}{2} | \nabla \phi | ^ {2}\right) \mathrm{d} V\tag{4}
$$

where $G _ { c }$ is the critical Griffith-type energy release rate, which is dependent on the hydrogen coverage $\theta .$ . 

The phase field fracture method resembles traditional continuum damage mechanics models, where the scalar damage field may be interpreted as the phase field $\phi .$ . Accordingly, the loss of stiffness associated with mechanical degradation of the material is characterized as a function of $\phi .$ . This is done by means of the so-called degradation function $g \left( \phi \right)$ , which relates the stored bulk energy per unit volume to the strain energy density of the undamaged solid, 

$$
\psi = g (\phi) \psi_ {0} = \left[ (1 - \phi) ^ {2} + k \right] \psi_ {0}\tag{5}
$$

Here, k is a parameter chosen to be as small as possible to keep the system of equations well-conditioned; a value of $k = 1 \times 1 0 ^ { - 7 }$ is adopted throughout this work. Integrating over the volume of the body and adding the phase field free energy contribution (4), one reaches the total potential energy functional of the deformation-fracture problem 

$$
\varPsi = \int_ {\Omega} \left\{\left[ (1 - \phi) ^ {2} + k \right] \psi_ {0} + G _ {c} (\theta) \left(\frac {1}{2 \ell} \phi^ {2} + \frac {\ell}{2} | \nabla \phi | ^ {2}\right) \right\} d V\tag{6}
$$

The variation of (6) with respect to $\delta \phi$ renders the weak form of the phase field contribution, 

$$
\int_ {\Omega} \left[ - 2 (1 - \phi) \delta \phi \psi_ {0} + G _ {c} (\theta) \left(\frac {1}{\ell} \phi \delta \phi + \ell \nabla \phi \cdot \nabla \delta \phi\right) \right] d V = 0\tag{7}
$$

and the phase field equilibrium equation in $\varOmega .$ , 

$$
G _ {c} (\theta) \left(\frac {1}{\ell} \phi - \ell \Delta \phi\right) - 2 (1 - \phi) \psi_ {0} = 0\tag{8}
$$

follows immediately upon making use of the product rule and Gauss’ divergence theorem. 

## 2.2. Hydrogen-dependent surface energy degradation

Hydrogen embrittles metallic materials by lowering the bond energy between metal atoms, which translates into a reduction of the fracture resistance. A number of authors have employed Density Functional Theory (DFT) to investigate the decohesion of fracture surfaces with varying hydrogen coverage (see, e.g., [27–29] and references therein). For example, Alvaro et al. [28] computed the change in ideal fracture energy in the presence of hydrogen atoms at Σ3 and Σ5 grain boundaries in nickel. Their results, in terms of normalized surface energy $\gamma \left( \theta \right) / \gamma \left( 0 \right)$ versus hydrogen coverage θ, are shown in Fig. 3, along with a linear fit to the data. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/c349e8ce4bd17f9d7d949bb2cfe8f51718ea3bb0cf1d8f4aab1b2a29fe1aa293.jpg)



Fig. 3. Effect of hydrogen on the surface energy of nickel. Linear fit to the DFT calculations by Alvaro et al. [28] for Σ3 and Σ5 grain boundaries



Table 1



Weighting factor estimation from first principles quantum mechanics.


<table><tr><td>Material</td><td>Damage coefficient <eq>\chi</eq></td><td>DFT analysis</td></tr><tr><td>Iron</td><td>0.89</td><td>Jiang and Carter (2004) [27]</td></tr><tr><td>Nickel</td><td>0.41</td><td>Alvaro et al. (2015) [28]</td></tr><tr><td>Aluminum</td><td>0.67</td><td>Jiang and Carter (2004) [27]</td></tr></table>

Equivalently, one can define the critical energy release rate dependence on the hydrogen coverage as, 

$$
\frac {G _ {c} (\theta)}{G _ {c} (0)} = 1 - \chi \theta\tag{9}
$$

where $G _ { c } \left( 0 \right)$ is the critical energy release rate in the absence of hydrogen and $\chi$ is the damage coefficient that weights the hydrogen-lowering of the fracture energy. χ can be estimated for other materials by fitting DFT data from the literature. The damage coefficient for iron and aluminum is obtained from the work by Jiang and Carter [27]—see Table 1. 

The effect of hydrogen on the fracture resistance can be illustrated by examining the analytical homogeneous solution of a one-dimensional quasi-static problem. Under these circumstances, the Cauchy stress is given by $~ \sigma ~ = ~ g ( \phi ) E \epsilon$ , where E denotes Young’s modulus and ϵ the strain. Given a strain energy density $\psi _ { 0 } ~ = ~ E \epsilon ^ { 2 } / 2$ one can readily obtain the homogeneous phase field from the strong form (8), 

$$
\phi = \frac {E \epsilon^ {2} \ell}{G _ {c} (\theta) + E \epsilon^ {2} \ell}\tag{10}
$$

and substituting into the constitutive equation renders the characteristic relation between the homogeneous strain and the homogeneous stress, 

$$
\sigma = \left(\frac {G _ {c} (\theta)}{G _ {c} (\theta) + E \varepsilon^ {2} \ell}\right) ^ {2} E \varepsilon\tag{11}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/f68a28b97e4b0bfaa46eb2ceec17d7a09f5654dfa72c91dd4e6f052d5ffdf03d.jpg)



Fig. 4. Effect of hydrogen coverage θ on the damage constitutive law for iron-based materials. The stress–strain response is normalized by the corresponding θ = 0 quantities.


The homogeneous solution for the stress reaches a maximum at a critical stress quantity, 

$$
\sigma_ {c} = \sqrt {\frac {2 7 E G _ {c} (\theta)}{2 5 6 \ell}}\tag{12}
$$

with the strain counterpart given by, 

$$
\epsilon_ {c} = \sqrt {\frac {G _ {c} (\theta)}{3 \ell E}}\tag{13}
$$

Thus, ℓ may be interpreted as a material parameter, which governs the magnitude of the critical stress at which damage initiates. This necessarily implies that the value of $G _ { c }$ is intrinsically related to the choice of ℓ, being equal to the Griffith’s critical energy release rate for ℓ → 0. From (12) an analogy with cohesive zone formulations can be established. With this in mind, it is interesting to note that the characteristic element size h in cohesive zone analyses is typically chosen to be 

$$
h <   \frac {\pi}{1 6 0} \frac {E G _ {c}}{\sigma_ {c} ^ {2}}\tag{14}
$$

so as to resolve the fracture process zone with at least 20 elements [30,31]. This implies that h should be at least 5.4 times smaller than ℓ in the phase field problem. The constitutive relation of the homogeneous phase field problem is shown in Fig. 4 as a function of hydrogen coverage. 

As shown in Fig. 4 for the case of iron, hydrogen significantly degrades the strength and the fracture resistance. The present modeling framework quantitatively accounts for the sensitivity of the surface energy to hydrogen coverage, as observed in first principles calculations; other mechanisms of hydrogen damage can also be incorporated. 

Finally, we use the Langmuir–McLean isotherm to compute the surface coverage from the bulk hydrogen concentration $C ,$ 

$$
\theta = \frac {C}{C + \exp \left(\frac {- \varDelta g _ {b} ^ {0}}{R T}\right)}\tag{15}
$$

with C given in units of impurity mole fraction. Here, R is the universal gas constant, T the temperature and $\varDelta g _ { b } ^ { 0 }$ is the Gibbs free energy difference between the decohering interface and the surrounding material. As in [6], a value of 30 kJ/mol is assigned to $\varDelta g _ { b } ^ { 0 }$ based on the spectrum of experimental data available for the trapping energy at grain boundaries. Thus, the present formulation accounts for the effect of microstructural traps on cracking and can incorporate the influence on mass transport through an effective diffusion coefficient. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/67c0d890507d7a0f950e7922e8f29f319f2ae2420451b0f2b8b6bac6993adde6.jpg)



Fig. 5. Schematic representation of the three-field boundary value problem: (a) deformation, (b) phase field, and (c) mass transport.


## 3. Stress-assisted hydrogen diffusion coupled with phase field fracture

The formulation presented in this section refers to the response of a solid body Ω with external surface ∂Ω of outward normal n—see Fig. 5. With respect to the displacement field u, the outer surface of the body is decomposed into a part $\partial \varOmega _ { u } .$ , where the displacement is prescribed by Dirichlet-type boundary conditions, and a part $\partial \varOmega _ { h } .$ , where the traction h is prescribed by Neumann-type boundary conditions (see Fig. 5a). A body force field per unit volume b can also be prescribed. The fracture phase field $\phi$ is driven by the displacement field of the solid. A Dirichlet-type boundary condition can be prescribed at $\varGamma$ , a given crack surface inside the solid (see Fig. 5b). Additionally, a phase field fracture microtraction $f$ can be prescribed on $\partial \varOmega _ { f }$ . With respect to the hydrogen concentration C, the external surface consists of two parts (see Fig. 5c): $\partial \varOmega _ { q }$ , where the hydrogen flux J is known (Neumann-type boundary conditions), and $\partial \varOmega _ { C }$ where the hydrogen concentration is prescribed (Dirichlet-type boundary conditions). Accordingly, a concentration flux entering the body across $\partial \varOmega _ { q }$ can be defined as $q = \pmb { J } \cdot \pmb { n }$ 

## 3.1. Governing balance equations

The principle of virtual work, in the absence of body forces, reads 

$$
\int_ {\Omega} \left(\boldsymbol {\sigma}: \nabla \delta \boldsymbol {u} + \omega \delta \phi + \boldsymbol {\zeta} \cdot \nabla \delta \phi - \frac {d C}{d t} \delta \mu + \boldsymbol {J} \cdot \nabla \delta \mu\right) d V = \int_ {\partial \Omega} (\boldsymbol {h} \cdot \delta \boldsymbol {u} + f \delta \phi + q \delta \mu) d S\tag{16}
$$

where $\mu$ is the chemical potential that drives the flux of hydrogen, σ is the symmetric Cauchy tensor, and ω and $\boldsymbol { \zeta }$ are microstress quantities work conjugate to the phase field $\phi$ and the phase field gradient $\nabla \phi$ , respectively. Applying the product rule and Gauss’ divergence theorem to the internal virtual work – left hand side of Eq. (16) – renders, 

$$
\begin{array}{l} \delta \mathcal {W} _ {i} = \int_ {\partial \Omega} (\boldsymbol {\sigma} \boldsymbol {n} \cdot \delta \boldsymbol {u} + \boldsymbol {\zeta} \cdot \boldsymbol {n} \delta \phi + \boldsymbol {J} \cdot \boldsymbol {n} \delta \mu) d S - \int_ {\Omega} \left((\nabla \cdot \boldsymbol {\sigma}) \cdot \delta \boldsymbol {u} \right. \\ \left. + (\nabla \cdot \boldsymbol {\zeta} - \omega) \delta \phi + \left(\nabla \cdot \boldsymbol {J} + \frac {d C}{d t}\right) \delta \mu\right) d V \end{array}\tag{17}
$$

Since the second integral on the right-hand side of Eq. (17) should vanish for arbitrary variations, a set of three equilibrium equations can be obtained, 

$$
\begin{array}{c c c} \nabla \cdot \boldsymbol {\sigma} = \mathbf {0} & \text {on} & \Omega \\ \nabla \cdot \boldsymbol {\zeta} - \omega = 0 & \text {on} & \Omega \\ \frac {d C}{d t} + \nabla \cdot \boldsymbol {J} = 0 & \text {on} & \Omega \end{array}\tag{18}
$$

The first integral on the right hand side of (17) may be identified as part of the external virtual work. Thus, by accounting for the right hand side of (16), the corresponding set of boundary conditions is obtained, 

$$
\begin{array}{r l} \boldsymbol {h} = \boldsymbol {\sigma} \boldsymbol {n} & \text {on} \partial \Omega_ {h} \\ f = \boldsymbol {\zeta} \cdot \boldsymbol {n} & \text {on} \partial \Omega_ {f} \\ q = \boldsymbol {J} \cdot \boldsymbol {n} & \text {on} \partial \Omega_ {q} \end{array}\tag{19}
$$

## 3.2. Energy imbalance

The first two laws of thermodynamics within a dynamical process of specific internal energy E and specific entropy Λ read 

$$
\frac {d}{d t} \int_ {\Omega} \mathcal {E} \mathrm{d} V = W _ {e} (\Omega) - \int_ {\partial \Omega} \boldsymbol {Q} \cdot \boldsymbol {n} \mathrm{d} S + \int_ {\Omega} Q \mathrm{d} V\tag{20}
$$

$$
\frac {d}{d t} \int_ {\Omega} A \mathrm{d} V \geq \int_ {\partial \Omega} \frac {\boldsymbol {Q}}{\Theta} \cdot \boldsymbol {n} \mathrm{d} S + \int_ {\Omega} \frac {\boldsymbol {Q}}{\Theta} \mathrm{d} V\tag{21}
$$

where $W _ { e }$ is the external work, Q is the heat flux, Q is the heat absorption and Θ the absolute temperature. Within an isothermal process $( \Theta = \Theta _ { 0 } )$ the thermodynamic laws can be readily combined by considering the free energy $\varPsi = \mathcal { E } - \theta _ { 0 } \varLambda$ , such that 

$$
\frac {d}{d t} \int_ {\Omega} \Psi \mathrm{d} V \leq W _ {e} (\Omega)\tag{22}
$$

which is generally referred to as Clausius–Duhem inequality or the principle of dissipation [32]. Given (16), the local free-energy inequality takes the form 

$$
\frac {d}{d t} \int_ {\Omega} \Psi \mathrm{d} V \leq \int_ {\partial \Omega_ {h}} \boldsymbol {h} \cdot \dot {\boldsymbol {u}} \mathrm{d} S + \int_ {\partial \Omega_ {f}} f \dot {\phi} \mathrm{d} S + \int_ {\partial \Omega_ {q}} q \dot {\mu} \mathrm{d} S\tag{23}
$$

Employing the divergence theorem and considering (18)–(19) one reaches the local dissipation postulate, 

$$
\pmb {\sigma}: \nabla \dot {\pmb {u}} + \omega \dot {\phi} + \pmb {\zeta} \cdot \nabla \dot {\phi} + \mu \dot {C} + \pmb {J} \cdot \nabla \mu - \dot {\Psi} \leq 0\tag{24}
$$

## 3.3. Constitutive theory

The constitutive prescriptions are constructed, in a thermodynamically consistent manner, by ensuring that the dissipation condition (24) is satisfied. The free energy is defined as, 

$$
\begin{array}{l} \Psi (\epsilon , \phi , \nabla \phi , C) = \underbrace {(1 - \phi) ^ {2} \psi_ {0} (\epsilon) - K \bar {V} _ {H} (C - C ^ {0}) \operatorname{tr} \epsilon} _ {\Psi^ {b}} \\ \qquad + \underbrace {G _ {c} (\theta) \left(\frac {1}{2 \ell} \phi^ {2} + \frac {\ell}{2} | \nabla \phi | ^ {2}\right)} _ {\Psi^ {s}} \\ \qquad + \underbrace {\mu^ {0} C + R T N (\theta_ {L} \ln \theta_ {L} + (1 - \theta_ {L}) \ln (1 - \theta_ {L}))} _ {\Psi^ {c}} \end{array}\tag{25}
$$

where $\varPsi ^ { b } ( \epsilon , \phi , C ) , \varPsi ^ { s } ( \phi , \nabla \phi , C )$ and $\varPsi ^ { c } \left( C \right)$ respectively denote the chemo-elastic energy stored in the bulk [33], the crack surface energy, and the chemical free energy. Here, ϵ is the strain tensor, K the bulk modulus, $\bar { V } _ { H }$ the partial molar volume of hydrogen in solid solution, $C ^ { 0 }$ the reference lattice hydrogen concentration, $\mu ^ { 0 }$ the reference chemical potential, $\theta _ { L }$ the occupancy of lattice sites and N the number of lattice sites. We subsequently develop a constitutive theory from the free energy that couples deformation, fracture and hydrogen diffusion. 

## 3.3.1. Mechanical deformation

We define $\psi _ { 0 }$ as the elastic strain energy density for the undamaged solid, 

$$
\psi_ {0} (\pmb {\epsilon}) = \frac {1}{2} \pmb {\epsilon} ^ {T}: \mathbf {C _ {0}}: \pmb {\epsilon}\tag{26}
$$

where $\mathbf { C } _ { 0 }$ is the linear elastic stiffness matrix. A linear elastic description of the material response is considered appropriate to characterize the brittle behavior of metals in the presence of hydrogen. Implicitly multi-scale plasticity formulations (e.g., strain gradient plasticity) have shown that crack tip stresses obtained via linear elasticity are more accurate than those computed by means of conventional plasticity theories [34–36]. We assume small strains and define the strain tensor as, 

$$
\pmb {\epsilon} = \frac {1}{2} \left[ \nabla \mathbf {u} ^ {T} + \nabla \mathbf {u} \right]\tag{27}
$$

Accordingly, the Cauchy stress tensor can be derived from (25) as, 

$$
\boldsymbol {\sigma} = \frac {\partial \Psi}{\partial \epsilon} = g (\phi) \left(\boldsymbol {C} _ {0}: \epsilon\right) - K \bar {V} _ {H} (C - C ^ {0}) \boldsymbol {I}\tag{28}
$$

with the second term having a negligible effect in hydrogen embrittlement phenomena [37] and being subsequently disregarded in the analysis. As shown in (28), and discussed in Section 2.1, the phase field model characterizes the loss in stiffness associated with bond breakage by means of the degradation function $g \left( \phi \right)$ 

## 3.3.2. Phasefieldfracture

The scalar microstress $\omega _ { \mathrm { { i } } }$ , work conjugate to the phase field $\phi .$ 

$$
\omega = \frac {\partial \Psi}{\partial \phi} = - 2 (1 - \phi) \psi_ {0} (\epsilon) + G _ {c} (\theta) \frac {1}{\ell} \phi\tag{29}
$$

and the vector microstress $\zeta .$ , work conjugate to the phase field gradient $\nabla \phi$ , 

$$
\boldsymbol {\zeta} = \frac {\partial \Psi}{\partial \nabla \phi} = G _ {c} (\theta) \ell \nabla \phi\tag{30}
$$

can be readily derived from the free energy (25). Inserting these constitutive relations in the local balance (18b) renders (8) if the concentration gradient along the small region where $\nabla \boldsymbol \phi \neq 0$ is neglected. On the one hand, the deformation of the solid drives the fracture phase field through the strain energy density $\psi _ { 0 } .$ . On the other hand, the coupling between the phase field fracture and hydrogen transport is introduced by defining a hydrogen concentrationdependent crack surface energy that models decohesion enhancement by hydrogen. We provide this connection in a multi-scale fashion by presenting a quantum-mechanically informed phase field degradation law (see Section 2.2). 

## 3.3.3. Transport ofdiluted species

The gradient of the chemical potential is the driving force for hydrogen diffusion. One can readily derive the chemical potential from the free energy (25) by considering the relation between the occupancy and the number of sites, $\theta _ { L } = C / N$ , 

$$
\mu = \frac {\partial \Psi}{\partial C} = \mu^ {0} + R T \ln \frac {\theta_ {L}}{1 - \theta_ {L}} - \bar {V} _ {H} \sigma_ {H} + G _ {c} ^ {\prime} (\theta) \theta^ {\prime} \left(\frac {1}{2 \ell} \phi^ {2} + \frac {\ell}{2} | \nabla \phi | ^ {2}\right)\tag{31}
$$

and the constitutive framework is completed by the definition of the mass flux, which follows a linear Onsager relationship, 

$$
\boldsymbol {J} = - \frac {D C}{R T} \nabla \mu\tag{32}
$$

where $D$ is the diffusion coefficient. Thus, hydrogen atoms migrate from regions of high chemical potential to regions of low chemical potential. The coupling with the deformation of the solid is given by the stress-dependent part of $\mu .$ As evident from (31), hydrostatic tensile stresses increase hydrogen solubility in the lattice (lattice dilatation) by lowering the chemical potential. Correspondingly, the last term in (31) enhances diffusion from cracked regions to pristine regions. However, the appropriate chemical boundary conditions in a propagating crack require careful consideration. 

First, one should note that the discussion is only relevant to experiments where the specimen is charged in-situ, as opposed to tests where hydrogen has been dissolved within the material prior to loading. Secondly, one would typically expect that the environment will promptly occupy the space created with crack advance. Consequently, a constant hydrogen concentration $C _ { e n v } ~ \mathrm { o r } ,$ more appropriately, a constant chemical potential $\mu _ { e n v } ,$ should be prescribed on a moving boundary $\partial B _ { e n v }$ as dictated by the phase field φ. In the finite element model this could be enforced by mean of Dirichlet, Neumann or mixed boundary conditions [9,38]. However, we note in passing that crack growth rates $d a / d t$ in hydrogen containing environments become load independent due to chemical reaction or mass transport limitation. A constant $\mu _ { e n v }$ prescribed on a moving crack surface will fail to predict $d a / d t$ measurements if a critical distance is not introduced in the failure criterion; such scheme could require a highly complex implementation. A physically sound framework could be key to quantitatively capture crack growth rates during the stage II plateau; since this regime has not been addressed in the present work, we assume for simplicity a negligible influence of the phase field on hydrogen diffusion. 

## 3.4. Numerical implementation

The finite element (FE) method is used to solve the coupled mechanical-diffusion-phase field problem. Using Voigt notation, the nodal values of the displacements, phase field and hydrogen concentration are interpolated as follows, 

$$
\boldsymbol {u} = \sum_ {i = 1} ^ {m} N _ {i} \boldsymbol {u} _ {i}, \quad \phi = \sum_ {i = 1} ^ {m} N _ {i} \phi_ {i}, \quad C = \sum_ {i = 1} ^ {m} N _ {i} C _ {i}\tag{33}
$$

where m is the number of nodes and $N _ { i }$ are the interpolation matrices, diagonal matrices with the nodal shape functions $N _ { i }$ as components. Accordingly, the corresponding gradient quantities can be discretized by, 

$$
\boldsymbol {\varepsilon} = \sum_ {i = 1} ^ {m} \boldsymbol {B} _ {i} ^ {u} \boldsymbol {u} _ {i}, \quad \nabla \phi = \sum_ {i = 1} ^ {m} \boldsymbol {B} _ {i} \phi_ {i}, \quad \nabla C = \sum_ {i = 1} ^ {m} \boldsymbol {B} _ {i} C _ {i}\tag{34}
$$

Here, $\pmb { B } _ { i }$ are vectors with the spatial derivatives of the shape functions and $\pmb { B } _ { i } ^ { u }$ denotes the standard strain–displacement matrices. 

## 3.4.1. FE discretization ofthe deformation-phasefield problem

The weak form for the deformation problem can be written, in its most general form, as 

$$
\int_ {\Omega} (g (\phi) \boldsymbol {\sigma} _ {0}: \delta \boldsymbol {\epsilon} - \mathbf {b} \cdot \delta \mathbf {u}) d V - \int_ {\partial \Omega_ {h}} (\mathbf {h} \cdot \delta \mathbf {u}) d S = 0\tag{35}
$$

where $\pmb { \sigma } _ { 0 }$ is the Cauchy stress tensor of the undamaged solid. Making use of the finite element discretization outlined above and considering that (35) must hold for arbitrary values of δu, the discrete equation corresponding to the equilibrium condition can be expressed as the following residual with respect to the displacement field, 

$$
\boldsymbol {r} _ {i} ^ {u} = \int_ {\Omega} \left[ (1 - \phi) ^ {2} + k \right] (\boldsymbol {B} _ {i} ^ {u}) ^ {T} \boldsymbol {\sigma_ {0}} d V - \int_ {\Omega} \boldsymbol {N} _ {i} ^ {T} \boldsymbol {b} d V - \int_ {\partial \Omega_ {h}} \boldsymbol {N} _ {i} ^ {T} \boldsymbol {h} d S\tag{36}
$$

Similarly, the out-of-balance force residual with respect to the evolution of the crack phase field is obtained by discretizing (7) and considering the contribution from the scalar phase field microtraction (16), 

$$
r _ {i} ^ {\phi} = \int_ {\Omega} \left[ - 2 (1 - \phi) N _ {i} H + G _ {c} (\theta) \left(\frac {1}{\ell} N _ {i} \phi + \ell \pmb {B} _ {i} ^ {T} \nabla \phi\right) \right] \mathrm{d} V - \int_ {\partial \Omega_ {f}} N _ {i} f \mathrm{d} S\tag{37}
$$

where we have introduced the so-called history variable field H to ensure irreversibility, 

$$
H = \left\{ \begin{array}{l l} \psi_ {0} (\boldsymbol {\epsilon}) & \quad \text { if } \psi_ {0} (\boldsymbol {\epsilon}) > H _ {t} \\ H _ {t} & \quad \text { otherwise } \end{array} \right.\tag{38}
$$

Here, $H _ { t }$ is the previously calculated energy at time increment t. Thus, the history field satisfies the Kuhn–Tucker conditions. The components of the consistent stiffness matrices can be obtained by differentiating the residuals with 

respect to the incremental nodal variables: 

$$
\boldsymbol {K} _ {i j} ^ {\boldsymbol {u}} = \frac {\partial \boldsymbol {r} _ {i} ^ {\boldsymbol {u}}}{\partial \boldsymbol {u} _ {j}} = \int_ {\Omega} \left[ (1 - \phi) ^ {2} + k \right] (\boldsymbol {B} _ {i} ^ {\boldsymbol {u}}) ^ {T} \boldsymbol {C} _ {0} \boldsymbol {B} _ {j} ^ {\boldsymbol {u}} \mathrm{d} V\tag{39}
$$

$$
\boldsymbol {K} _ {i j} ^ {\phi} = \frac {\partial r _ {i} ^ {\phi}}{\partial \phi_ {j}} = \int_ {\Omega} \left[ \left(2 H + \frac {G _ {c} (\theta)}{\ell}\right) N _ {i} N _ {j} + G _ {c} (\theta) \ell \boldsymbol {B} _ {i} ^ {T} \boldsymbol {B} _ {j} \right] \mathrm{d} V\tag{40}
$$

## 3.4.2. FE discretization of mass transport

Substituting the constitutive equation for the chemical potential (31) into the Fick-type relation for the mass flux (32), one reaches 

$$
\boldsymbol {J} = - \frac {D C}{(1 - \theta_ {L})} \left(\frac {\nabla C}{C} - \frac {\nabla N}{N}\right) + \frac {D}{R T} C \bar {V} _ {H} \nabla \sigma_ {H}\tag{41}
$$

which, after making the common assumptions of low occupancy $( \theta _ { L } \ll 1 )$ and constant interstitial sites concentration $( \nabla N = 0 )$ , renders 

$$
\boldsymbol {J} = - D \nabla C + \frac {D}{R T} C \bar {V} _ {H} \nabla \sigma_ {H}\tag{42}
$$

Substituting in (16), the hydrogen transport equation becomes 

$$
\int_ {\Omega} \left[ \delta C \left(\frac {1}{D} \frac {d C}{d t}\right) + \nabla \delta C \nabla C - \nabla \delta C \left(\frac {\bar {V} _ {H} C}{R T} \nabla \sigma_ {H}\right) \right] \mathrm{d} V = - \frac {1}{D} \int_ {\partial \Omega_ {q}} \delta C q \mathrm{d} S\tag{43}
$$

A residual vector can be readily obtained by discretizing (43), given that $\delta C$ indicates an arbitrary virtual variation of the hydrogen concentration: 

$$
r _ {i} ^ {C} = \int_ {\Omega} \left[ N _ {i} ^ {T} \left(\frac {1}{D} \frac {d C}{d t}\right) + \boldsymbol {B} _ {i} ^ {T} \nabla C - \boldsymbol {B} _ {i} ^ {T} \left(\frac {\bar {V} _ {H} C}{R T} \nabla \sigma_ {H}\right) \right] \mathrm{d} V + \frac {1}{D} \int_ {\partial \Omega_ {q}} N _ {i} ^ {T} q \mathrm{d} S\tag{44}
$$

From which a diffusivity matrix can be defined, 

$$
\pmb {K} _ {i j} ^ {C} = \int_ {\Omega} \left(\pmb {B} _ {i} ^ {T} \pmb {B} _ {j} - \pmb {B} _ {i} ^ {T} \frac {\bar {V} _ {H}}{R T} \nabla \sigma_ {H} N _ {j}\right) \mathrm{d} V\tag{45}
$$

where the discretization given in Eq. (33) has also been employed to interpolate the time derivatives of the nodal concentrations. The diffusivity matrix is affected by the gradient of the hydrostatic stress, $\sigma _ { H }$ , which is computed at the integration points from the nodal displacements, extrapolated to the nodes by means of the shape functions, and subsequently multiplied by B to compute $\nabla \sigma _ { H }$ . We employ 8-node quadrilateral finite elements with $C _ { 0 }$ continuity. 

At the same time, one can readily identify a concentration capacity matrix, 

$$
\pmb {M} _ {i j} = \int_ {\Omega} N _ {i} ^ {T} \frac {1}{D} N _ {j} \mathrm{d} V\tag{46}
$$

and a diffusion flux vector, 

$$
\boldsymbol {F} _ {i} = - \frac {1}{D} \int_ {\partial \Omega_ {q}} N _ {i} ^ {T} q \mathrm{d} S\tag{47}
$$

Accordingly, the discretized hydrogen transport equation reads, 

$$
\boldsymbol {K} ^ {C} \boldsymbol {C} + \boldsymbol {M} \dot {\boldsymbol {C}} = \boldsymbol {F}\tag{48}
$$

## 3.4.3. Coupled scheme

The deformation, diffusion and phase field fracture problems are weakly coupled. First, mechanical deformation impacts diffusion through the stress field, governing the pressure dependence of the bulk chemical potential. Secondly, mass transport affects the fracture resistance via hydrogen buildup in the fracture process zone, reducing the critical energy release rate. And thirdly, the hydrogen-sensitive phase field degrades the strain energy density of the solid. 

We solve the linearized finite element system, 

$$
\left[ \begin{array}{c c c} \boldsymbol {K} ^ {u} & 0 & 0 \\ 0 & \boldsymbol {K} ^ {\phi} & 0 \\ 0 & 0 & \boldsymbol {K} ^ {C} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {u} \\ \boldsymbol {\phi} \\ \boldsymbol {C} \end{array} \right] + \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & \boldsymbol {M} \end{array} \right] \left[ \begin{array}{c} \dot {\boldsymbol {u}} \\ \dot {\boldsymbol {\phi}} \\ \dot {\boldsymbol {C}} \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {r} ^ {u} \\ \boldsymbol {r} ^ {\phi} \\ \boldsymbol {r} ^ {C} \end{array} \right]\tag{49}
$$

by means of a time parametrization and an incremental-iterative scheme in conjunction with the Newton–Raphson method. Due to its robustness, the staggered solution scheme proposed by Miehe et al. [39] is adopted to solve the deformation-phase field coupling; a time increment sensitivity analysis is conducted in all computations. 

The modeling framework is implemented in the commercial finite element package ABAQUS via a user element subroutine. The code can be downloaded from www.empaneda.com/codes, including documentation describing the details of the implementation in ABAQUS, verification case studies and integration strategies. Post-processing of the results is carried out by means of Abaqus2Matlab [40]. 

## 4. Results

A number of case studies of particular interest are addressed to show the capabilities of the modeling framework presented. Firstly, we model the benchmark problem of a cracked square plate subjected to tension, verifying our implementation with the results by Miehe et al. [39], and we subsequently assess the role of hydrogen (Section 4.1). Then, in Section 4.2, hydrogen assisted failure in notched components is investigated, and model predictions are compared with the experimental results of Wang et al. [41]. The experimental work by Olden et al. [42] is reproduced in Section 4.3, where the model is used to estimate cracking thresholds under constant loading conditions. We investigate internal hydrogen assisted cracking and compare with the compact tension experiments by Thomas et al. [43] in Section 4.4. Finally, Section 4.5 deals with complex crack propagation from defects that typically arise due to pitting corrosion. 

## 4.1. Cracked square plate subjected to tension in a hydrogenous environment

We model a square plate with a horizontal crack going from the left side to the center of the specimen. The geometric setup, dimensions and boundary conditions are given in Fig. 6. We load the plate by prescribing the vertical displacement in the upper edge, and restrict both vertical and horizontal displacements in the lower boundary. A uniform distribution of hydrogen concentration is assigned throughout the specimen as initial boundary condition: $C ( t = 0 ) = C _ { 0 }$ . In addition, a constant hydrogen concentration $C = C _ { b }$ is prescribed at the boundaries during the entire numerical experiment. All the outer boundaries of the specimen, including the crack faces, are in contact with the environment. These boundary conditions mimic the usual scenario in field applications and laboratory experiments, where the specimen is pre-charged before loading in the same aggressive environment; accordingly, we assume $C _ { b } = C _ { 0 }$ . For materials with high hydrogen diffusivity, the use of generalized Neumann-type boundary conditions [44] or σ -dependent Dirichlet boundary conditions [33,45,46] could provide a more accurate description of the electrochemistry-diffusion interface. As in [39], we adopt the following material properties: Young’s modulus $E = 2 1 0 ~ \mathrm { G P a }$ , Poisson’s ratio $\nu = 0 . 3$ , and critical energy release rate $G _ { c } \left( 0 \right) = 2 . 7$ MPa mm. We assume an iron-based material and consequently adopt a hydrogen damage coefficient of $\chi = 0 . 8 9$ and a partial molar volume of $\bar { V } _ { H } = 2 0 0 0 \mathrm { m m } ^ { 3 } / \mathrm { m o l }$ [37]. For this benchmark study, we assume that the load is prescribed at a sufficiently low rate such that hydrogen equilibrium can be achieved. Thus, from the diffusion coefficient and the test time $t _ { f }$ one can define a diffusion length $\ell _ { C } = \sqrt { D t _ { f } }$ , which is taken to be significantly larger than the characteristic length of the fracture problem $( \ell _ { C } \gg \ell )$ . A very fine mesh is employed in the expected crack propagation area after a sensitivity study, ensuring that the characteristic element length h is sufficiently small to resolve the fracture process zone $( h < \ell / 7 . 5 )$ . Namely, the square plate is discretized by means of 43 110 plane strain quadratic elements. 

To assess the capabilities of the model in capturing hydrogen-induced damage we compute the mechanical response under three different environments that range from 1 wt ppm, which corresponds to a 3% NaCl aqueous solution, to 0.1 wt ppm. Fig. 7 shows the results computed in terms of the load–displacement curve. As shown in the figure, the model shows a strong sensitivity to the environment, with the peak load decreasing with the hydrogen content, in agreement with experimental observations. The numerical results in the absence of hydrogen quantitatively agree with those by Miehe et al. [39], verifying the numerical implementation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/a5ce888e8e4082f05246fb7d36ae0d5170677ec4e1668d53143734280ac1f91f.jpg)



Fig. 6. Schematic description of the geometry and configuration of the cracked square plate case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/e61c9ae3be292df4d5fef7faf484c10b69bfc9217e14aa713d92139bf2e200cf.jpg)



Fig. 7. Cracked square plate subjected to tension. Load–deflection curves for different environments. The computations for $C _ { 0 } = C _ { b } = 0$ wt ppm match the results by Miehe et al. [39] (symbols). Material properties: $E = 2 1 0 \mathrm { \ G P a } , \nu = 0 . 3 , G _ { c } = 2 . 7 \mathrm { \ k J / m } ^ { 2 } , \ell = 0 . 0 0 7 5$ mm, $\bar { V } _ { H } = 2 0 0 0$ mm<sup>3</sup>/mol, $\ell _ { C } \gg \ell ,$ and $T = 3 0 0 \mathrm { K }$


As shown in Fig. 8, hydrogen accumulates in the vicinity of the crack as the external load and the hydrostatic stress increase. 

Atomic hydrogen concentration lowers the critical energy release rate of the material, facilitating crack initiation and subsequent propagation. Fig. 9 shows the resulting fracture patterns at different load steps with the red color denoting the case where $\phi = 1$ . The trend depicted by the crack path is the same in all the environments considered. 

## 4.2. Hydrogen assistedfailure in notched cylindrical bars

We now turn our attention to hydrogen assisted failure from notched specimens under rising load and different environmental conditions. We reproduce the experimental work by Wang et al. [41] on cylindrical bars. The plane strain implementation can be readily modified to deal with axisymmetric samples by changing the strain–displacement matrix and integrating the discretized equations in polar coordinates. Fig. 10 shows the specimens geometry, the mesh employed and the path depicted by the crack that initiates at the notch tip. A total of 52 955 axisymmetric 8-node elements are used to discretize the bar. The length of the characteristic element is chosen to be 10 times smaller than ℓ to assure mesh-independent results and resolve the fracture process zone. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/eb10bb1bd3f0ef588d37f34c3cc3b4da3d78e27625dd42c7496981d8a5289240.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/a994ea5a8864041aa213f51fdbbf648c94484f85992d09135b0c0fb11d3b970b.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/198c7e919691077aa8c34a5f68103381764421ed00baa972e1a7d88b993fb149.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/a2efbc17b153270a984ba2f3b73972f26d3029c464caa77660f4ffb66abd6732.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/86197d2329e934e2a0ac7eed4d21f7d31bc080e3a351a0b67b229d37fc965f68.jpg)



(d)



Fig. 8. Hydrogen buildup in the fracture process zone. Contours at (a) $u \ : = \ : 0 . 0 0 1 5 \mathrm { m m } .$ , (b) $u \ : = \ : 0 . 0 0 1 9$ mm, (c) u = 0.0021 mm, and (d) $u = 0 . 0 0 2 3$ mm for $C _ { 0 } = 0 . 5 \mathrm { w t }$ ppm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/d2d798d24c97f74a978191db413d1966965074dd8b8a6df6d8ba742d5070e6b1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/e183cc15de6e74631a643ea22cc7f385994593cd14212cc6823183eb2b260cd9.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/1de62130bea61ef2037404fa58719caedfb0382b3d42ae7d706985b83754d3c6.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/e6c306e86661f72a5b7abaf2767a2b8c9d417a37088334975e6a2e4f999b4bd7.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/d404411e753cc07f4571bebbec0087acf292d3671d5e644e8ed192b3a04c76f3.jpg)



(d)



Fig. 9. Crack propagation contours at (a) u = 0.0057 mm, (b) $u = 0 . 0 0 5 9$ mm, (c) u = 0.0061 mm, and (d) u = 0.0062 mm for $C _ { 0 } = 0$ wt ppm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/4593d849adb5e2093efae6fddc129a1a187dacf2799c537189d603d58aea569a.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/c73eca089aa45532a8315f7c57a6fbcc271515148a9f7156e14ee56b06c66588.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/4b791141e0f747d8204b688c99c19465a7d700e6a33f5ef746f3b35294868211.jpg)



(c)



Fig. 10. Schematic description of the notch cylindrical bar: (a) geometry, (b) mesh and (c) crack path when the remote stress equals $\sigma _ { f } .$ . Dimensions are given in mm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/14cc1a93ff3ca43c53b64c6c666e494c94f9b9e104e79373de5fdf20e39473cd.jpg)



Fig. 11. Notched bar subjected to tension test. Net section strength σ as a function of the hydrogen concentration C in AISI 4135 steel. Materia properties: $E = 2 1 0 ~ \mathrm { G P a } , \nu = 0 . 3 , \bar { V } _ { H } = 2 0 0 0 ~ \mathrm { m m } ^ { 3 } / \mathrm { m o l } , D = 3 . 8 \times 1 0 ^ { - 5 } ~ \mathrm { m m } ^ { 2 } / \mathrm { s } , \ell = 0 . 0 1 5 ~ \mathrm { m m }$ , and $G _ { c } = 6 4 \mathrm { k J } / \mathrm { m } ^ { 2 }$


We mimic the conditions of the experiments on AISI 4135 steel bars by Wang et al. [41]. Uniaxial tension tests are conducted at a nominal strain rate of $\dot { \varepsilon } = 8 . 3 \times 1 0 ^ { - 7 } ~ \mathrm { s ^ { - 1 } }$ . The experiments are conducted at room temperature. The material properties for AISI 4135 steel are: Young’s modulus $E = 2 1 0 \mathrm { G P a }$ , Poisson’s ratio $\nu = 0 . 3 .$ , partial molar volume of $\bar { V } _ { H } = 2 0 0 0 \mathrm { m m } ^ { 3 } / \mathrm { m o l }$ , and diffusion coefficient $D = 3 . 8 \times 1 0 ^ { - 5 } \ \mathrm { m m ^ { 2 } / s }$ . The specimens are precharged and subsequently loaded in the same environment; hydrogen concentrations range from 0.08 to 2.2 wt ppm. For each case, the maximum net section stress is computed at the remote boundary. Fig. 11 shows the failure stress obtained in each numerical experiment as a function of the hydrogen content. The results from Wang et al. [41] are also shown; a critical energy release rate of $G _ { c } = 6 4 \mathrm { k J } / \mathrm { m } ^ { 2 }$ provided the best fit to the data. 

Phase field predictions reveal a good agreement with the experimental data. Increasing the hydrogen content translates into a reduction of the critical energy release rate, which in turn lowers the strength. Hydrogen accumulates in the vicinity of the notch tip, where tensile hydrostatic stresses are larger. The strength changes drastically within low hydrogen levels but eventually saturates: increasing the hydrogen content beyond 0.5 wt ppm leads to minor changes in the failure stress. The saturation stage is captured due to the presence of the Langmuir–McLean isotherm (15). The embrittlement law seems to capture the experimentally observed response well. Discrepancies are larger in the experiments with very low hydrogen concentrations, where grain boundary decohesion may not be the only mechanism assisting failure. 

## 4.3. Cracking thresholdfor duplex steels in sea water under constant load

We investigate the capabilities of the present model to capture hydrogen damage under constant mechanical load by reproducing the experiments by Olden and co-workers [42]. In their work, single-edge notched tensile (SENT) specimens were immersed in slowly circulating artificial sea water at $4 ~ ^ { \circ } \mathbf { C }$ under cathodic protection conditions. The material under consideration is a 25% Cr duplex stainless steel with $E = 2 0 0$ GPa and $\nu = 0 . 3 ;$ despite its wide use in sub-sea applications, duplex steels are sensitive to hydrogen embrittlement at low corrosion protection potentials [42]. The geometry of the fatigue pre-cracked SENT specimens is shown in Fig. 12, along with the finite element mesh employed. A total of 98 748 plane strain quadratic elements are used in the discretization. A constant net stress is prescribed at the remote boundaries and a subsurface concentration of 1 wt ppm is assumed in the outer surfaces, based on the experimental conditions (3.5% NaCl solution and a corrosion protection potential of −1050 $\mathrm { m V } _ { S C E } )$ . The tests have been conducted at room temperature and the diffusion coefficient has been measured as $D = 3 . 7 \times 1 0 ^ { - 6 } \mathrm { { m m ^ { 2 } / s } }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/ac75059532b28e8eda39600fd30dcebbfbf42818a6128a93f7fec3354a6d2b41.jpg)



Fig. 12. Geometry and mesh of the single edge notched specimen. Dimensions are given in mm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/b953d7aa3ce078831f145bec3e2ae135f4c4d205172f062ec35b26ab9d857886.jpg)



Fig. 13. SENT specimen subjected to constant load. Net section stress $\sigma _ { n e t }$ as a function of time in duplex stainless steel. Material properties: E = 200 GPa, ν = 0.3, V<sup>¯</sup> = 2000 mm<sup>3</sup>/mol, $D = 3 . 7 \times 1 0 ^ { - 6 }$ mm<sup>2</sup>/s, ℓ = 0.06 mm, and $G _ { c } = 2 7 . 4 \mathrm { k J } / \mathrm { m } ^ { 2 }$


The initial mechanical load introduces a certain amount of damage that is insufficient to propagate the crack. The magnitude of the phase field variable increases and eventually triggers crack growth as time goes by and hydrogen diffuses towards the fracture process zone. Since the mechanical load is kept constant, damage is caused by the reduction in the critical energy release rate with time due to hydrogen diffusion. 

We compare our cracking threshold predictions with the experimental data by Olden et al. [42]. Results are shown in Fig. 13 in terms of net stress versus time. As shown in the figure, we are able to reach a good agreement with the tests and extend our predictions over time scales that are impractical in laboratory experiments. This allows us to identify the net stress level below which cracking will not occur: $\sigma _ { T H } = 5 1 0 \mathrm { M P a }$ . Thus, safe regimes of operation can be efficiently identified by means of the present phase field formulation. However, one should note that the lack of experimental data at larger time scales introduces a degree of uncertainty in the numerical predictions of this case study. Specifically, more tests within the range of 1000–2000 h would have been desirable given the scatter observed for net stresses of 540–560 MPa. 

## 4.4. Internal hydrogen assisted cracking in compact tension specimens

Hydrogen assisted cracking frequently takes place from hydrogen dissolved within the material prior to loading. This phenomenon is termed internal hydrogen assisted cracking, and atomic hydrogen is typically introduced by manufacturing operations, such as casting, welding, electrochemical machining, or heat treatments. Mechanical loading redistributes the internal hydrogen content to the fracture process zone and promotes cracking. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/855597fdd5434453506fee5d6bade0104dfc3c597ab2273e33b83fae4b2844ea.jpg)



Fig. 14. Schematic description of the Compact Tension experiment: (a) geometry, (b) mesh and (c) crack path. Dimensions are given in mm.


We show the capabilities of the present phase field formulation to model internal hydrogen assisted cracking by mimicking the experiments by Thomas et al. [43] on AerMet100. AerMet100 is a secondary-hardening quenched and tempered martensitic steel developed for high-performance aerospace applications. An electroplated coating is used for corrosion resistance, but atomic hydrogen can be codeposited in the plating and steel substrate [43]. In this case study, we model pre-cracked Compact Tension specimens that have been pre-charged prior to loading. Our aim is to predict the threshold stress intensity for internal hydrogen embrittlement $K _ { T H }$ as a function of the hydrogen content. Fig. 14a shows the geometry and dimensions of the specimens, following [43], and in agreement with the ASTM E 1820 Standard. Fig. 14 also shows the mesh (Fig. 14b) and the characteristic mode I crack propagation path (Fig. 14c). A total of 34 792 quadratic plane strain elements have been used and the stress intensity factor at crack initiation is computed following the ASTM E 1820 Standard. The material properties related to the mechanical response are Young’s modulus $E = 1 9 4 4 0 0 \mathrm { M P a }$ , and Poisson’s ratio $\nu = 0 . 3$ . The experiments have been conducted at room temperature and the diffusion coefficient for AerMet100 has been measured as $D = 2 \times 1 0 ^ { - 4 } \mathrm { m m } ^ { 2 } / \mathrm { s } [ 4 3 ]$ . Mimicking the experiments a loading rate of $\dot { K } = 2 . 2 \times 1 0 ^ { - 4 }$ MPa $\sqrt { \mathrm { m } } / \mathrm { s }$ is employed. The length parameter is chosen to be $\ell = 0 . 3$ mm; 7 times larger than the characteristic element length along the extended crack plane. 

Fig. 15 shows the results obtained in terms of $K _ { T H }$ versus the uniform hydrogen concentration attained prior to loading. A value of $G _ { c } = 3 0 \mathrm { k J } / \mathrm { m } ^ { 2 }$ is assigned to the critical energy release rate to fit the experiments in air. As shown in Fig. 15. the numerical predictions qualitatively capture the experimental trends. Namely, the cracking threshold decreases significantly with increasing hydrogen content. Internal hydrogen embrittlement is particularly severe for this very high strength steel, with $K _ { T H }$ being roughly a tenth of the fracture toughness in inert environments. While the agreement with experiments is considered satisfactory, finite element results fail to quantitatively predict the degree of embrittlement at large hydrogen concentrations. Plausibly, the differences are a consequence of fitting $G _ { c }$ with stress intensity measurements that pertain to fracture processes where nucleation, growth and coalescence of microvoids are the mechanisms governing fracture. The value assigned to the trapping energy at grain boundaries may constitute another source of discrepancy; accurate measurements of trap characteristics remain a challenging task. 

## 4.5. Crack coalescencefrom corrosion pits

Hydrogen assisted cracking frequently manifests in combination with other corrosion damaging effects. For example, this is often the case in aqueous solutions where cathodic protection has been used to enhance corrosion resistance [47]. Cracking in pipelines and other structural components often commences at the sites of corrosion pits, and is accelerated by hydrogen embrittlement. We investigate the capabilities of the present phase field formulation to predict complex crack propagation due to existing defects. This capability could be a game-changer in the energy industry, where structural integrity assessment often involves estimating crack growth and coalescence from wellmapped corrosion pits as a function of time. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/e5ea8700472a67ac6c43ab0e7bd6139f51425ca024dc684cf859c0ba38b7ba02.jpg)



Fig. 15. Internal hydrogen cracking in Compact Tension specimens. Cracking threshold $K _ { T H }$ as a function of the hydrogen concentration C AerMet100. Material properties: E = 194 400 MPa, ν = 0.3, V<sup>¯</sup> = 2000 mm<sup>3</sup>/mol, $D = 2 \times 1 0 ^ { - 4 }$ mm<sup>2</sup>/s, ℓ = 0.3 mm, and $G _ { c } = 3 0 \mathrm { k J } / \mathrm { m } ^ { 2 }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/b64e005e404cde474728709d2e8f5243667487f61f38fc42a62fe588b6fca7f3.jpg)



Fig. 16. Geometry and loading configuration of a plate with existing defects, dimensions are given in mm. The defects are introduced in the initial rectangular geometry by prescribing the initial condition $\phi = 1$


We consider a plate with three preexisting defects, as outlined in Fig. 16. The defects, which typically originate due to anodic dissolution, are defined in the numerical model by prescribing an initial history field $\phi = 1$ . Introducing pre-existing cracks as heterogeneities in the phase field order parameter (as opposed to discrete geometrical discontinuities) has proven to yield predictions closer to analytic fracture mechanics solutions [48]. We assume $E = 2 0 0 \mathrm { G P a } , \nu = 0 . 3$ , and energy release rate $G _ { c } = 9 0 ~ \mathrm { k J } / \mathrm { m } ^ { 2 }$ . The length parameter is 6 times larger than the characteristic element size, $\ell = 0 . 6 \mathrm { m m }$ . A mesh of 30 908 quadratic quadrilateral plane strain elements is employed to model the plate. We consider a diffusion coefficient on the order of that of fcc iron at room temperature, $D = 1 \times 1 0 ^ { - 8 }$ $\mathrm { m m } ^ { 2 } / \mathrm { s } .$ , and prescribe an initial hydrogen concentration of $C _ { 0 } = 1$ wt ppm throughout the specimen. This hydrogen concentration is maintained during the test at the sides of the specimen and in the corrosion pits. As outlined in Fig. 16, we prescribe a uniform displacement at the sides, being the loading rate $\dot { u } = 0 . 0 4 1 6 \mu \mathrm { m } / \mathrm { s }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/56240eafe4945a6c6304fbc1422839c5f52cd71c2d61b7d79bc04da61951fcb1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/27496f04642870cb66619606982109bc53bb1681db086f93966c465eb64e3c16.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/1f7951f7d9550dbfa7c6f77197cbad2e8f5796736c94ec669fb6ca1cb889ffcd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/4fa6f878f2ffa4525aa82ad2bb7b0bc487bb6adffc4feb3b58d156145f4b180e.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/429d5969f046464500731ac702f50bb99351536b574a58810696c9a94fa01ba6.jpg)



(e)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/5154e879-8747-47a0-8781-900aa889d9b9/ee760de2ba6f11e9944663147d286cf029911fe88477cf355861929a0f22ccf0.jpg)



(f)



Fig. 17. Rectangular plate with pre-existing corrosion defects. Fracture pattern at times (a) 1 s, (b) 5040 s, (c) 5721 s, (d) 6322 s, (e) 6948 s, and (f) 7560 s.


The crack propagation contours are shown as a function of time in Fig. 17. Blue and red colors correspond to the completely intact and the fully broken state of the material, respectively. First, damage is restricted to the corrosion pits, which act as stress risers and attract the hydrogen (Fig. 17a). Then, cracking initiates at the largest defect (Fig. 17b) and eventually coalesces with the central hole (Fig. 17c). After arresting at the center defect, the crack reappears at its left corner (Fig. 17d) and continues to propagate. At the same time, cracking initiates at the smaller pit (Fig. 17e) and both propagating cracks eventually coalescence (Fig. 17f). Crack initiation takes place after 5040 s while the final coalescence occurs 2520 s later. This benchmark problem shows the robustness and capacity of the present phase field scheme to model complex cracking conditions that may arise in practical applications; crack deflection, arrest, restart and coalescence are successfully captured. 

## 5. Conclusions

A phase field formulation for the long-standing problem of hydrogen assisted cracking has been presented. A coupled deformation-diffusion-phase field scheme has been developed in the framework of the finite element method. The model builds upon a hydrogen-dependent surface energy degradation law based on Density Functional Theory that adequately characterizes the sensitivity of the fracture energy to atomic hydrogen concentration. A wide variety of case studies have been addressed to benchmark the potential of the present phase field formulation for hydrogen embrittlement. First, the cracked plate benchmark is modeled to verify the numerical implementation and examine the influence of hydrogen in the load–displacement curve. Then, the failure stress in notched cylindrical bars is computed for a very wide range of environmental conditions, with finite element results showing a good agreement with the experiments. The model is also used to estimate exposure times for fracture in sea water under constant loads; numerical predictions enable to identify the cracking threshold without the need for time consuming laboratory tests. Numerical experiments in Compact Tension specimens are then conducted to compute internal hydrogen stress intensity thresholds as a function of hydrogen content. Finally, the capabilities of the model to capture complex crack propagation arising from defects intrinsic to corrosive environments are investigated. Computations show that phase field methods for fracture are a suitable tool to achieve the elusive goal of lifetime prediction of engineering components undergoing hydrogen assisted cracking. 

## Acknowledgments

E. Mart´ınez-Paneda acknowledges financial support from the Ministry of Economy and Competitiveness of Spain˜ through grant MAT2014-58738-C3 and the People Programme (Marie Curie Actions) of the European Union’s Seventh Framework Programme (FP7/2007-2013) under REA grant agreement no. 609405 (COFUNDPostdocDTU). C.F. Niordson acknowledges financial support from the Danish Independent Research Fund (DFF-7017-00121). 

## References



[1] W.H. Johnson, On some remarkable changes produced in iron and steel by the action of hydrogen and acids, Proc. Phys. Soc. London 23 (1875) 168–179. 





[2] E. Martínez-Pañeda, C.F. Niordson, R.P. Gangloff, Strain gradient plasticity-based modeling of hydrogen environment assisted cracking, Acta Mater. 117 (2016) 321–332. 





[3] J.T. Burns, Z.D. Harris, J.D. Dolph, R.P. Gangloff, Measurement and modeling of hydrogen environment-assisted cracking in a Ni-Cu-Al-T superalloy, Metall. Mater. Trans. A 47 (3) (2016) 990–997. 





[4] P. Novak, R. Yuan, B.P. Somerday, P. Sofronis, R.O. Ritchie, A statistical, physical-based, micro-mechanical model of hydrogen-induced intergranular fracture in steel. J. Mech. Phys, Solids 58 (2) (2010) 206–226. 





[5] C. Ayas, V.S. Deshpande, N.A. Fleck, A fracture criterion for the notch strength of high strength steels in the presence of hydrogen, J. Mech. Phys, Solids 63 (1) (2014) 80–93. 





[6] S. Serebrinsky, E.A. Carter, M. Ortiz, A quantum-mechanically informed continuum model of hydrogen embrittlement, J. Mech. Phys. Solids 52 (10) (2004) 2403–2430. 





[7] I. Scheider, M. Pfuff, W. Dietzel, Simulation of hydrogen assisted stress corrosion cracking using the cohesive model, Eng. Fract. Mech 75 (15) (2008) 4283–4291. 





[8] C. Moriconi, G. Hénaff, D. Halm, Cohesive zone modeling of fatigue crack propagation assisted by gaseous hydrogen in metals, Int. J. Fatigue 6 56 66 





[9] S. del Busto, C. Betegón. E. Martínez-Pañeda. A cohesive zone framework for environmentally assisted fatigue. Eng. Fract. Mech. 185 (2017 210–226. 





[10] H. Yu, J.S. Olsen, V. Olden, A. Alvaro, J. He, Z. Zhang, Continuum level simulation of the grain size and misorientation effects on hydrogen embrittlement in nickel. Eng. Fail. Anal. 81 (2017) 79–93 





[11] G. Francfort, J.-J. Marigo, Revisiting brittle fracture as an energy minimization problem, J. Mech. Phys. Solids 46 (8) (1998) 1319–1342. 





[12] C. Miehe, F. Welshinger, M. Hofacker, Thermodynamically consistent phase-field models of fracture: Variational principles and multi-field FE implementations, Internat. J. Numer. Methods Engrg. 83 (2010) 1273–1311. 





[13] T. Gerasimov, L. De Lorenzis, A line search assisted monolithic approach for phase-field computing of brittle fracture, Comput. Methods Appl. Mech. Engrg. 312 (2016) 276–303. 





[14] M.J. Borden, T.J. Hughes, C.M. Landis, C.V. Verhoosel, A higher-order phase-field model for brittle fracture: Formulation and analysis within the isogeometric analysis framework, Comput. Methods Appl. Mech. Engrg. 273 (2014) 100–118. 





[15] D. Schillinger, M.J. Borden, H.K. Stolarski, Isogeometric collocation for phase-field fracture models, Comput. Methods Appl. Mech. Engrg 284 (2015) 583–610. 





[16] B. Bourdin, G.A. Francfort, J.J. Marigo, Numerical experiments in revisited brittle fracture, J. Mech. Phys. Solids 48 (4) (2000) 797–826. 





[17] J. Reinoso, A. Arteiro, M. Paggi, P. Camanho, Strength prediction of notched thin ply laminates using finite fracture mechanics and the phase field approach, Compos. Sci. Technol. 150 (2017) 205–216. 





[18] M.J. Borden, T.J. Hughes, C.M. Landis, A. Anvari, I.J. Lee, A phase-field formulation for fracture in ductile materials: Finite deformation balance law derivation, plastic degradation, and stress triaxiality effects, Comput. Methods Appl. Mech. Engrg, 312 (2016) 130–166. 





[19] C. Miehe, F. Aldakheel, A. Raina, Phase field modeling of ductile fracture at finite strains: A variational gradient-extended plasticity-damage theory, Int. J. Plast. 84 (2016) 1–32. 





[20] A. Mikelic, M. Wheeler, T. Wick, A phase-field method for propagating fluid-filled fractures coupled to a surrounding porous medium, Multiscale Model. Simul. 13 (2015) 367–398. 





[21] Z.A. Wilson, C.M. Landis, Phase-field modeling of hydraulic fracture, J. Mech. Phys. Solids 96 (2016) 264–290. 





[22] J. Reinoso, M. Paggi, C. Linder, Phase field modeling of brittle fracture for enhanced assumed strain shells at large deformations: formulation and finite element implementation, Comput. Mech. 59 (6) (2017) 981–1001. 





[23] V. Carollo, J. Reinoso, M. Paggi, A 3D finite strain model for intralayer and interlayer crack simulation coupling the phase field approach and cohesive zone model, Compos. Struct. 182 (2017) 636–651. 





[24] W. Mai, S. Soghrati, R.G. Buchheit, A phase field model for simulating the pitting corrosion, Corros. Sci. 110 (2016) 157–166. 





[25] W. Mai, S. Soghrati, A phase field model for simulating the stress corrosion cracking initiated from pits, Corros. Sci. 125 (2017) 87–98. 





[26] M.J. Borden, C.V. Verhoosel, M.A. Scott, T.J.R. Hughes, C.M. Landis, A phase-field description of dynamic brittle fracture, Comput. Methods Appl. Mech. Engrg. 217–220 (2012) 77–95. 





[27] D.E. Jiang, E.A. Carter, First principles assessment of ideal fracture energies of materials with mobile impurities: Implications for hydrogen embrittlement of metals, Acta Mater. 52 (16) (2004) 4801–4807. 





[28] A. Alvaro, I. Thue Jensen, N. Kheradmand, O.M. Løvvik, V. Olden, Hydrogen embrittlement in nickel, visited by first principles modeling, cohesive zone simulation and nanomechanical testing, Int. J. Hydrogen Energy 40 (47) (2015) 16892–16900. 





[29] A. Tehranchi, X. Zhang, G. Lu, W.A. Curtin, Hydrogen vacancy dislocation interactions in α -Fe, Modelling Simulation Mater. Sci. Eng. 25 (2017) 025001 (13 pp). 





[30] J.R. Rice, Mathematical analysis in the mechanics of fracture, Math. Fundam. 2 (B2) (1968) 191–311. 





[31] N. Moës, T. Belytschko, Extended finite element method for cohesive crack growth, Eng. Fract. Mech. 69 (7) (2002) 813–833. 





[32] M.E. Gurtin, E. Fried, L. Anand, The Mechanics and Thermodynamics of Continua, Cambridge University Press, 2010. 





[33] C.V. Di Leo, L. Anand, Hydrogen in metals: A coupled theory for species diffusion and large elastic-plastic deformations, Int. J. Plast. 43 (2013) 42–69. 





[34] E. Martínez-Pañeda, C. Betegón, Modeling damage and fracture within strain-gradient plasticity, Int. J. Solids Struct. 59 (2015) 208–215. 





[35] E. Martínez-Pañeda, C.F. Niordson, On fracture in finite strain gradient plasticity, Int. J. Plast. 80 (2016) 154–167. 





[36] E. Martínez-Pañeda, S. Natarajan, S. Bordas, Gradient plasticity crack tip characterization by means of the extended finite element method, Comput. Mech. 59 (5) (2017) 831–842. 





[37] J.P. Hirth, Effects of hydrogen on the properties of iron and steel, Metall. Trans. A 11 (6) (1980) 861–890. 





[38] Y. Zhao, B.X. Xu, P. Stein, D. Gross, Phase-field study of electrochemical reactions at exterior and interior interfaces in Li-ion battery electrode particles, Comput. Methods Appl. Mech. Engrg. 312 (2016) 428–446. 





[39] C. Miehe, M. Hofacker, F. Welschinger, A phase field model for rate-independent crack propagation: Robust algorithmic implementation based on operator splits, Comput. Methods Appl. Mech. Engrg. 199 (45–48) (2010) 2765–2778. 





[40] G. Papazafeiropoulos, M. Muñiz-Calvente, E. Martínez-Pañeda, Abaqus2Matlab: A suitable tool for finite element post-processing, Adv. Eng. Softw. 105 (2017) 9–16. 





[41] M. Wang, E. Akiyama, K. Tsuzaki, Effect of hydrogen and stress concentration on the notch tensile strength of AISI 4135 steel, Mater. Sci. Eng. A 398 (1–2) (2005) 37–46. 





[42] V. Olden, C. Thaulow, R. Johnsen, E. Østby, T. Berstad, Influence of hydrogen from cathodic protection on the fracture susceptibility of 25%Cr duplex stainless steel - Constant load SENT testing and FE-modelling using hydrogen influenced cohesive zone elements, Eng. Fract. Mech. 76 (7) (2009) 827–844. 





[43] R.L.S. Thomas, J.R. Scully, R.P. Gangloff, Internal hydrogen embrittlement of ultrahigh-strength AERMET 100 steel, Metall. Mater. Trans. A 34 (2) (2003) 327–344. 





[44] A. Turnbull, Perspectives on hydrogen uptake, diffusion and trapping, Int. J. Hydrogen Energy 40 (47) (2015) 16961–16970. 





[45] E. Martínez-Pañeda, S. del Busto, C.F. Niordson, C. Betegón, Strain gradient plasticity modeling of hydrogen diffusion to the crack tip, Int. J. Hydrogen Energy 41 (24) (2016) 10265–10274. 





[46] A. Díaz, J.M. Alegre, I.I. Cuesta, Coupled hydrogen diffusion simulation using a heat transfer analogy, Int. J. Mech. Sci. 115–116 (2016) 360–369. 





[47] J. Sanchez, J. Fullea, C. Andrade, Fracto-surface mobility mechanism in high-strength steel wires, Eng. Fract. Mech. 186 (2017) 410–422. 





[48] M. Klinsmann, D. Rosato, M. Kamlah, R.M. McMeeking, An assessment of the phase field formulation for crack growth, Comput. Methods Appl, Mech, Engrg, 294 (2015) 313–330. 

