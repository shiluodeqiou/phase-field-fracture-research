# Phase-field modeling of fracture with physics-informed deep learning

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/a2d451d9c45156e47c2f19d74ad8c5b072d26782e71345ea05e244fa0c15f82d.jpg)


M. Manav <sup>a</sup>, R. Molinaro <sup>b</sup>, S. Mishra <sup>b</sup>, L. De Lorenzis a,∗ 

<sup>a</sup> Department of Mechanical and Process Engineering, ETH Zurich, Tannenstrasse 3, Zurich, 8092, Switzerland 

<sup>b</sup> Seminar for Applied Mathematics, Department of Mathematics, ETH Zurich, Ramistrasse 101, Zurich, 8092, Switzerland 

## A R T I C L E I N F O

Keywords: Phase-field fracture Physics-informed machine learning Deep Ritz method Non-convex optimization Crack nucleation Crack propagation 

## A B S T R A C T

We explore the potential of the deep Ritz method to learn complex fracture processes such as quasistatic crack nucleation, propagation, kinking, branching, and coalescence within the unified variational framework of phase-field modeling of brittle fracture. We elucidate the challenges related to the neural-network-based approximation of the energy landscape, and the ability of an optimization approach to reach the correct energy minimum, and we discuss the choices in the construction and training of the neural network which prove to be critical to accurately and efficiently capture all the relevant fracture phenomena. The developed method is applied to several benchmark problems and the results are shown to be in qualitative and quantitative agreement with the finite element solution. The robustness of the approach is tested by using neural networks with different initializations. 

## 1. Introduction

Predictive modeling and simulation of fracture processes is critically important in design for many engineering applications and still poses significant challenges. In the past two decades, phase-field fracture modeling [1,2] has emerged as a game changer; it offers a unified variational framework and, upon discretization, a flexible computational method to encompass various aspects of fracture including crack nucleation, propagation, merging, and branching [2–4], while obviating the need for crack tracking procedures as well as for ad-hoc parameters and criteria. For these reasons, it has found applications and extensions to a variety of fracture problems including thermal cracks [5], ductile fracture [6], drying-induced cracks [7], and hydraulic fracture [8], among many others. Furthermore, it has been demonstrated to accurately capture topologically complex crack paths, even in three dimensions [5], while delivering quantitatively accurate predictions [9]. 

The first variational phase-field model for brittle fracture was derived by regularizing the free-discontinuity problem obtained from recasting Griffith’s fracture criterion in a variational form [1,10]. Regularization is performed by introducing an additional field, known as the phase field, ranging between 0 (representing the intact material) and 1 (representing the fully cracked material). l f h f ld b d h d h ll d b l h l h h d l to a smeared representation of a crack. Later, it was shown that a more flexible but substantially analogous variational modeling framework can be constructed from a special family of gradient damage models [11], whereby the phase field is interpreted as a damage variable and is therefore postulated to be irreversible. In the computational setting, the regularization of a sharp crack to a smeared representation overcomes the computational challenges encountered in handling an a priori unknown crack path. 

The crack is now represented implicitly by the continuous phase field; along with the displacement field, this field is obtained by solving the non-linear coupled partial differential equations (PDEs) stemming from the stationarity conditions of the governing energy functional. However, two challenging aspects remain: the energy functional is non-convex, which needs special attention in the numerics [12], and the resolution of the (small) length scale in the discretized setting is computationally expensive. This limitation restricts the applicability of the approach to e.g. optimization, uncertainty quantification and inverse problems. 

In recent years, considerable effort has been directed towards leveraging advances in machine learning to accurately model physical phenomena [13]; various physics-informed deep learning approaches [14] have been employed to solve PDEs and variational problems [15–18]. One prominent approach, known as physics-informed neural networks (PINNs), learns the solution of b h i d ( i i d) i i f l k ( ) [ ] b ild h i l approximation property of NNs [21–23], i.e. the ability of NNs to approximate any continuous function, which allows for the use of NNs as the ansatz space for PDE solutions. Notably, PINNs can seamlessly incorporate any available data and compute solutions to forward and inverse problems with the same NN architecture. They have demonstrated accurate approximation of solutions to a variety of PDEs and inverse problems, also in solid mechanics [24–31]. Rigorous estimates of the generalization error of PINNs approximations have also been established [20,32,33]. Furthermore, multiple variations of PINNs have been proposed, such as hp-VPINNs [17], cPINNs [34], xPINNS [35], FBPINNs [36], among others, to tailor them for different problems and to improve their performance. 

In PINNs, training of the NN representing the solution field involves the minimization of a loss function comprising the PDE residual and additional terms, which enforce initial and boundary conditions and possibly other constraints. An alternative approach, known as the deep Ritz method (DRM) [18,37,38], directly minimizes the energy functional instead of the PDE residual. The DRM is particularly useful in obtaining stable solutions when the governing energy functional is non-convex [39], as in phase-field fracture modeling. Additionally, since the computation of the energy requires a lower order of derivatives compared to the corresponding strong-form PDE, the DRM is expected to be computationally less expensive [37]. On the other hand, energy calculation requires integration over the entire domain, and only a few studies have investigated quadrature rules for NNs [40]. 

PINN approaches have been developed to solve phase-field problems (Cahn–Hilliard and Allen–Cahn equations) involving the phase field as the only scalar unknown [41,42]. In contrast, phase-field fracture modeling involves two coupled fields: the displacement (vector) field and the phase field. Furthermore, while the steep variation of the phase field at localization is governed by the regularization length scale, the displacement field undergoes a much sharper variation wherever the phase field localizes. These differences lead to additional and unique challenges in approximating the solution of phase-field fracture problems using NNs. While the DRM has shown some promise, its applicability has been demonstrated primarily in problems involving crack propagation with simple crack paths [43,44]. Crack initiation in the absence of a notch has only been demonstrated by assuming a very large value for the regularization length scale [43]. Additionally, these approaches have required a large number of quadrature points, exceeding the number needed to resolve the regularization length scale. Notably, a quantitative assessment of the solution accuracy is also lacking. The applicability of approaches other than the DRM has been partially investigated in [43,45]. An operator learning approach $[ 4 6 , 4 7 ]$ , namely variational DeepONets, has also been applied to predict the crack path in a problem involving crack propagation in quasi-brittle materials [48]. However, the applicability of physics-informed deep learning to phase-field fracture modeling hinges on the ability of NNs to learn all the fracture processes accurately, especially considering that this flexibility lies at the core of the phase-field approach and is also one of the key reasons for its success. 

In this work, we elucidate the challenges involved in learning the solution of phase-field fracture problems, and investigate the design of NNs and of their training strategies aimed at learning crack initiation, propagation, kinking, branching, and coalescence. We also address the challenges associated with learning the solution fields with the same level of domain discretization as required in finite element analysis (FEA). We systematically demonstrate the accuracy of the learned solution by comparing it with the FEA solution. Additionally, we test the robustness of our approach by training NNs with different random initializations. 

The paper is organized as follows. A brief review of the phase-field brittle fracture formulation is presented in Section 2. In Section 3, the DRM is summarized, and the challenges in learning the solution of a phase-field fracture problem are discussed along with the design of the NNs and their training strategy. This is followed by numerical examples of crack nucleation, propagation, kinking, branching, and coalescence in Section 4. Finally, we summarize the main conclusions in Section 5. 

## 2. Phase-field model of brittle fracture

In this section, we summarize the governing equations of the phase-field model of brittle fracture which we aim at solving with the deep learning approach proposed in the following sections. 

## 2.1. Basics of the formulation

Let $\Omega \subset \mathbb { R } ^ { d } , \ d \in \{ 1 , 2 , 3 \}$ be a bounded open domain occupied by a �-dimensional body. ${ \cal T } _ { D , 0 } , { \cal T } _ { D , 1 }$ and $T _ { N }$ are disioint sections of the boundary �� of � with prescribed homogeneous Dirichlet, non-homogeneous Dirichlet and Neumann boundary conditions, respectively. The body is assumed to be linear elastic with the strain energy density given by $\begin{array} { r } { \Psi ( \pmb \varepsilon ) = \frac 1 \gamma \lambda \mathrm { t r } ^ { 2 } ( \pmb \varepsilon ) + \mu \mathrm { t r } ( \pmb \varepsilon \cdot \pmb \varepsilon ) , } \end{array}$ , where λ and $\mu$ are the Lamé constants, and $\begin{array} { r } { \boldsymbol { \varepsilon } = \frac { 1 } { \gamma } ( \boldsymbol { \nabla } \boldsymbol { u } + \boldsymbol { \nabla } \boldsymbol { u } ^ { T } ) } \end{array}$ is the infinitesimal strain tensor. with $u : \mathcal { \Omega }  \mathbb { R } ^ { d }$ as the displacement field. The total energy functional for the body acted upon by body force �<sup>̄</sup> and surface traction �<sup>̄</sup> is given by: 

$$
\mathcal {E} (\boldsymbol {u}, \alpha) = \underbrace {\int_ {\Omega} \left(g (\alpha) \Psi^ {+} (\varepsilon (\boldsymbol {u})) + \Psi^ {-} (\varepsilon (\boldsymbol {u}))\right) \mathrm{d} \Omega} _ {\mathcal {E} ^ {e l}} + \underbrace {\frac {G _ {c}}{c _ {w}} \int_ {\Omega} \left(\frac {w (\alpha)}{l} + l | \nabla \alpha | ^ {2}\right) \mathrm{d} \Omega} _ {\mathcal {E} ^ {d}} - \int_ {\Omega} \bar {\boldsymbol {b}} \cdot \boldsymbol {u}   \mathrm{d} \Omega - \int_ {\Gamma_ {N}} \bar {\boldsymbol {t}} \cdot \boldsymbol {u}   \mathrm{d} s.\tag{1}
$$

Here $\mathcal { E } ^ { e l }$ and ${ \mathcal { E } } ^ { d }$ represent the elastic and damage parts of the energy, respectively. $\alpha : \varOmega  [ 0 ,$ 1] is the phase field (or damag field), with $\alpha = 0$ representing the undamaged state and $\alpha = 1$ the fully damaged state. The function $g ( \alpha ) _ { i }$ , known as degradation function, modulates the degradation of the elastic energy with increasing damage. �(�) is also known as local dissipation function, as it dictates the energy dissipated through damage in the unit volume of the material. The parameter � with $0 < l$ ≪ diam(�) is the regularization length controlling the thickness of the transition zone between undamaged and fully damaged material regions; $G _ { c }$ represents the fracture toughness of the material, and $c _ { w }$ is a normalization constant given by $\begin{array} { r } { c _ { w } = 4 \int _ { 0 } ^ { 1 } \sqrt { w ( t ) } d t } \end{array}$ . In this work, we adopt the following choices [11] based on the typical choices employed in the phase-field fracture literature: 

$$
\mathrm{AT1model:} \quad g (\alpha) := (1 - \alpha) ^ {2} + \eta , \quad w (\alpha) := \alpha , \quad c _ {w} = 8 / 3,\tag{2}
$$

$$
\mathrm{AT2model:} \quad g (\alpha) := (1 - \alpha) ^ {2} + \eta , \quad w (\alpha) := \alpha^ {2}, \quad c _ {w} = 2.\tag{3}
$$

with $\eta = o ( l )$ . The elastic strain energy density Ψ is decomposed into active (i.e. damage-driving) and inactive (i.e. damage-resisting parts, $\psi ^ { + }$ and $\psi ^ { - }$ , respectively, and the degradation is applied only to $\psi ^ { + }$ [49–52]. While several energy decompositions are available [49–51,53], in this work we focus on the volumetric–deviatoric decomposition [49] whereby 

$$
\begin{array}{r l} & {\boldsymbol {\psi} ^ {+} = \frac {1}{2} K \big \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \big \rangle_ {+} ^ {2} + \mu \mathrm{tr} (\mathbf {e} \cdot \mathbf {e}),} \\ & {\boldsymbol {\psi} ^ {-} = \frac {1}{2} K \big \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \big \rangle_ {-} ^ {2},} \end{array}\tag{4}
$$

with $\langle a \rangle _ { + } = \mathrm { m a x } \{ 0 , a \} , \ : \langle a \rangle _ { - } = \mathrm { m i n } \{ 0 , a \}$ , the bulk modulus $\begin{array} { r } { K = \lambda + \frac { 2 } { 3 } \mu , } \end{array}$ , and the deviatoric strain tensor $\begin{array} { r } { \mathbf { e } = \varepsilon - \frac { t r ( \varepsilon ) } { 3 } \mathbf { I } _ { } } \end{array}$ , where � is the third-order identity tensor. 

## 2.2. Time-discrete evolution problem

In the time-discrete setting of the quasi-static evolution problem, the state of the system at the (pseudo-)time or loading step $n \geq 1$ is obtained as the solution of the minimization problem 

$$
\underset {\boldsymbol {u}, \alpha} {\operatorname{argmin}} \{\mathcal {E} _ {n} (\boldsymbol {u}, \alpha): \boldsymbol {u} \in V _ {\bar {\boldsymbol {u}} _ {n}}, \alpha \in \mathcal {D} _ {\alpha_ {n - 1}} \},\tag{5}
$$

where 

$$
\mathcal {E} _ {n} (\boldsymbol {u}, \alpha) = \mathcal {E} ^ {e l} (\boldsymbol {u}, \alpha) + \mathcal {E} ^ {d} (\alpha) - \int_ {\Omega} \bar {\boldsymbol {b}} _ {n} \cdot \boldsymbol {u} \mathrm{d} \Omega - \int_ {\Gamma_ {N}} \bar {\boldsymbol {t}} _ {n} \cdot \boldsymbol {u} \mathrm{d} s,\tag{6}
$$

$$
\boldsymbol {V} _ {\bar {\boldsymbol {u}} _ {n}} := \{\boldsymbol {u} \in (H ^ {1} (\Omega)) ^ {d}: \boldsymbol {u} = \boldsymbol {0} \text { on } \Gamma_ {D, 0}, \boldsymbol {u} = \bar {\boldsymbol {u}} _ {n} \text { on } \Gamma_ {D, 1} \}\tag{7}
$$

denotes the space of kinematically admissible displacement fields, and $\bar { \boldsymbol { b } } _ { n } , \bar { \boldsymbol { t } } _ { n }$ and ${ \bar { \pmb u } } _ { n }$ are respectively the prescribed body force, the prescribed traction and the prescribed displacement at loading step �. Furthermore, 

$$
\mathcal {D} _ {\alpha_ {n - 1}} := \{\alpha \in H ^ {1} (\Omega): \alpha \geq \alpha_ {n - 1} \text { in } \Omega \}\tag{8}
$$

denotes the space of admissible phase fields. The condition $\alpha \geq \alpha _ { n - 1 }$ represents the irreversibility of the phase field evolution. Note that here we are looking for the local minimum of the energy functional, motivated by the known drawbacks of global energy minimization, among which is the possible jump of the solution over energy barriers [2]. The first-order necessary conditions of the local minimization problem deliver the strong form of the governing equations 

$$
\pmb {\nabla} \cdot \pmb {\sigma} + \bar {\pmb {b}} _ {n} = 0,\tag{9}
$$

$$
\alpha - \alpha_ {n - 1} \geq 0,\tag{10}
$$

$$
g ^ {\prime} (\alpha) \Psi^ {+} + \frac {G _ {c}}{c _ {w}} \left(\frac {w ^ {\prime} (\alpha)}{l} - 2 l \Delta \alpha\right) \geq 0,\tag{11}
$$

$$
(\alpha - \alpha_ {n - 1}) \left[ g ^ {\prime} (\alpha) \Psi^ {+} + \frac {G _ {c}}{c _ {w}} \left(\frac {w ^ {\prime} (\alpha)}{l} - 2 l \Delta \alpha\right) \right] = 0,\tag{12}
$$

all valid in $\varOmega ,$ and represent the local equilibrium of forces, damage irreversibility, damage criterion, and loading–unloading conditions, respectively. The Cauchy stress is defined as $\begin{array} { r } { \sigma = g ( \alpha ) \frac { \partial \mathcal { W } ^ { + } } { \partial \varepsilon } + \frac { \partial \mathcal { W } ^ { - } } { \partial \varepsilon } } \end{array}$ , and $\begin{array} { r } { 0 ^ { \prime } = \frac { \partial } { \partial \alpha } ( ) } \end{array}$ . The whole set of boundary conditions reads as follows: 

$$
\begin{array}{r l} \pmb {u} = \pmb {0} & \mathrm{on} \Gamma_ {D, 0}, \\ \pmb {u} = \bar {\pmb {u}} _ {n} & \mathrm{on} \Gamma_ {D, 1}, \\ \sigma \pmb {n} = \bar {\pmb {t}} _ {n} & \mathrm{on} \Gamma_ {N}, \end{array}
$$

$$
\alpha - \alpha_ {n - 1} \geq 0, \nabla \alpha \cdot \boldsymbol {n} \geq 0, (\alpha - \alpha_ {n - 1}) (\nabla \alpha \cdot \boldsymbol {n}) = 0 \quad \text { on } \Gamma ,\tag{13}
$$

where � is the surface normal. 

## 2.3. Irreversibility of the phase field

One way to enforce the irreversibility of the phase field in the computations is to add to the energy functional in (1) the following energetic penalty [54]: 

$$
\mathcal {E} ^ {i r} (\alpha) = \int_ {\Omega} \frac {1}{2} \gamma_ {i r} \langle \alpha - \alpha_ {n - 1} \rangle_ {-} ^ {2} \mathrm{d} \Omega ,\tag{14}
$$

where $\gamma _ { i r }$ is the penalty parameter, whose value can be chosen as suggested in [54]: 

$$
\gamma_ {i r} = \frac {G _ {c}}{l} \frac {2 7}{6 4 \mathrm{TOL} _ {\mathrm{ir}} ^ {2}} \quad (\text {AT1 model}),\tag{15}
$$

$$
\gamma_ {i r} = \frac {G _ {c}}{l} \left(\frac {1}{\mathrm{TOL} _ {\mathrm{ir}} ^ {2}} - 1\right) (\mathrm{AT2model}).\tag{16}
$$

Here $0 < \mathrm { T } 0 \mathrm { L } _ { \mathrm { i r } } \leq 1$ is the prescribed irreversibility tolerance threshold; in this work, we set it to $\mathrm { T } 0 \mathrm { L } _ { \mathrm { i } \mathrm { r } } = 5 \times 1 0 ^ { - 3 }$ 

## 2.4. Non-dimensionalization scheme

Non-dimensionalization not only reduces the number of relevant physical parameters, but also aids in learning by ensuring that the inputs are ∼ 1. So, we non-dimensionalize the energy functional using the following scheme: 

$$
\tilde {\boldsymbol {x}} = \frac {\boldsymbol {x}}{L}, \quad \tilde {l} = \frac {l}{L}, \quad \tilde {\boldsymbol {u}} = \frac {\boldsymbol {u}}{L} \left(\frac {G _ {c}}{E l}\right) ^ {- 1 / 2}, \quad \tilde {\lambda} = \frac {\lambda}{E}, \quad \tilde {\mu} = \frac {\mu}{E}, \quad \mathrm{and} \quad \tilde {\mathcal {E}} = \frac {l \mathcal {E}}{L ^ {3} G _ {c}},\tag{17}
$$

where $\pmb { x } \in \mathcal { \Omega } \left( \tilde { \pmb { x } } \in \tilde { \mathcal { \Omega } } \right)$ is a material point coordinate, � is the characteristic length of the body, � is the Young’s modulus, and $\sqrt { \frac { G _ { c } } { E l } }$ is of the order of the critical strain for crack nucleation in a 1D bar [11]. Then the dimensionless form of the energy functional in (1), with no surface tractions and body forces, and including the energetic penalty to enforce the irreversibility of the phase field, reads 

$$
\tilde {\mathcal {E}} (\tilde {\boldsymbol {u}}, \alpha) = \underbrace {\int_ {\tilde {\Omega}} \left(g (\alpha) \tilde {\Psi} ^ {+} (\tilde {\varepsilon} (\tilde {\boldsymbol {u}})) + \tilde {\Psi} ^ {-} (\tilde {\varepsilon} (\tilde {\boldsymbol {u}}))\right) \mathrm{d} \tilde {\Omega}} _ {\tilde {\mathcal {E}} ^ {e l}} + \underbrace {\frac {1}{c _ {w}} \int_ {\tilde {\Omega}} \left(w (\alpha) + \tilde {l} ^ {2} | \tilde {\nabla} \alpha | ^ {2}\right) \mathrm{d} \tilde {\Omega}} _ {\tilde {\mathcal {E}} ^ {d}} + \underbrace {\int_ {\tilde {\Omega}} \frac {1}{2} \tilde {\gamma} _ {i r} \langle \alpha - \alpha_ {n - 1} \rangle_ {-} ^ {2} \mathrm{d} \tilde {\Omega}} _ {\tilde {\mathcal {E}} ^ {i r}},\tag{18}
$$

where $\begin{array} { r } { \tilde { \nabla } = L \nabla , \tilde { \varepsilon } = \varepsilon \left( \frac { G _ { c } } { E l } \right) ^ { - 1 / 2 } , \tilde { \psi } ^ { \pm } = \frac { l \psi ^ { \pm } } { G _ { c } } , \tilde { \gamma } _ { i r } = \frac { l \gamma _ { i r } } { G _ { c } } , \tilde { \mathcal { E } } ^ { e l } = \frac { l \mathcal { E } ^ { e l } } { L ^ { 3 } G _ { c } } , \tilde { \mathcal { E } } ^ { d } = \frac { l \mathcal { E } ^ { d } } { L ^ { 3 } G _ { c } } } \end{array}$ , and $\begin{array} { r } { \tilde { \mathcal { E } } ^ { i r } = \frac { l \mathcal { E } ^ { i r } } { L ^ { 3 } G _ { c } } } \end{array}$ . Also, the non-dimensional stress follows as $\begin{array} { r } { \tilde { \sigma } = g ( \alpha ) \frac { \partial \tilde { \psi } ^ { + } } { \partial \tilde { \varepsilon } } + \frac { \partial \tilde { \psi } ^ { - } } { \partial \tilde { \varepsilon } } } \end{array}$ . Furthermore, leveraging the relation among Lamé constants, Young’s modulus and Poisson’s ratio $\nu ,$ we obtain $\begin{array} { r } { \tilde { \lambda } = \frac { \nu } { ( 1 + \nu ) ( 1 - 2 \nu ) } } \end{array}$ and $\begin{array} { r } { \tilde { \mu } = \frac { 1 } { 2 ( 1 + \nu ) } } \end{array}$ . Notably, as a consequence, the only parameters in the non-dimensional energy are � and <sup>̃</sup>� For simplicity of notation, from here onwards, we only use non-dimensional quantities but omit the <sup>̃</sup>(⋅) symbol. 

## 3. A deep Ritz method for phase-field fracture modeling

## 3.1. The deep Ritz method

In the DRM, as in any other physics-informed deep learning approach for solving PDEs and variational problems, the solution field is represented by an NN, frequently a feedforward NN (also known as a multilayer perceptron). A feedforward NN is a composition of affine transformations and scalar non-linear activation functions. Given an input $\ b { y } \in \mathbb { R } ^ { n }$ , the NN maps it to the output $\boldsymbol { z } _ { \boldsymbol { \theta } } \in \mathbb { R } ^ { m }$ as follows 

$$
\boldsymbol {z} _ {\theta} (\boldsymbol {y}) = C _ {K} \circ \sigma \circ C _ {K - 1} \dots \circ \sigma \circ C _ {1} (\boldsymbol {y}),\tag{19}
$$

where $C _ { k }$ (with $1 \leq k \leq K )$ represents an affine transformation, also known as the �th layer of the NN. Specifically, $C _ { k } ( z _ { k } ) =$ $\mathbf { W } _ { k } z _ { k } +  { b _ { k } }$ , where $\mathbf { W } _ { k }$ and $\pmb { b } _ { k }$ are trainable weights and biases and $\pmb { z } _ { k }$ is the input to the layer. The symbol ◦ represents the composition of functions, and σ is a scalar activation function applied elementwise. Commonly used activation functions are the ReLU. sigmoid. and hyperbolic tangent (tanh) functions [55]. � denotes the set of all trainable parameters of the NN, i.e $\boldsymbol { \theta } = \{ \mathbf { W } _ { k } , \ \pmb { b } _ { k } \} _ { k = 1 } ^ { K }$ 

Training of the NN aims to find � such that $\scriptstyle z _ { \theta }$ approximates the target solution. It involves constructing an appropriate loss function and then minimizing the loss with respect to the parameters in �. The minimization is typically performed using stochastic gradient decent algorithms such as Adam [56] or higher-order optimization algorithms such as L-BFGS [57]. 

For our problem, we define the displacement and phase fields obtained from the NN as ${ \pmb u } _ { \theta } ( { \pmb x } )$ and $\alpha _ { \theta } ( { \pmb x } )$ . Then the loss function is expressed as 

$$
\mathcal {L} = \log (\mathcal {E} _ {\theta}),\tag{20}
$$

where $\mathcal { E } _ { \theta } = \mathcal { E } ( \boldsymbol { u } _ { \theta } , \boldsymbol { \alpha } _ { \theta } )$ is obtained from (18). Taking the log of the energy in (20) makes the loss function $\sim 1$ , allowing us to set the same weight for weight regularization (to be discussed later) and the same stopping criterion for the optimizer for all the problems investigated in this work 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/e5d213ceaa8b4dd4561a7b76ea814948439c2a35a921afd95f29fd29956bb962.jpg)



Fig. 1. Scheme of our deep Ritz method for the two-dimensional case (left); function constraining the phase field between 0 and 1 (right).


Note that, in our experience, the enforcement of the Dirichlet boundary conditions using a soft constraint in DRM is challenging. Hence, we enforce them by constructing an ansatz, following the approach employed in [14], see Section 3.2.1. For a genera domain shape for which an ansatz is not feasible, general approaches for the enforcement of boundary conditions as in [58,59] can be employed. 

## 3.2. Construction and training of the NN

Our aim is to obtain an NN-based approximation of the solution fields employing the DRM in learning. This approach entails two key challenges. The first challenge lies in ensuring that the NN-based approximation of the energy surface, $\varepsilon _ { \theta } ,$ is a faithfu projection of the energy landscape in the space of NN-parameters. Specifically, it is crucial that the energy barriers and minima are appropriately represented. In turn, the representation of the energy surface relies on three ingredients: the construction of the NN(s) representing the fields, the computation of the gradients of the fields, and the integration over the domain. The second challenge lies in the choice of the optimization algorithm. This algorithm needs to respect the energy barriers and reach the correct local energy minimum regardless of the complexity of the solution associated with that energy minimum. As follows, we discuss all these aspects and refer to some Appendices for additional details. 

## 3.2.1. Choice of the NN architecture

Physically distinct fields such as the displacement field and the phase field are expected to be learned efficiently when represented by independent NNs. However, we find that an intimate coupling between the fields, facilitated by representing the displacement and phase fields as the outputs of the same NN, helps in learning the nucleation of a crack as shown in Appendix A. Hence, we construct an NN which takes as input the position vector of a point in the domain (2 components in 2D, 1 in 1D) and delivers outputs which correspond to the components of the displacement vector and the value of the phase field at that point (3 outputs in 2D, 2 in 1D), see Fig. 1. The non-dimensionalization scheme outlined in Section 2.4 ensures that the inputs are ∼ 1. In constructing an ansatz to apply Dirichlet boundary conditions, we ensure that the outputs of the NN corresponding to the displacement field are also approximately ∼ 1 as follows: 

$$
\begin{array}{r} u _ {\theta} = f _ {u} (\pmb {x}, \hat {u} _ {\theta}) U _ {p}, \\ v _ {\theta} = f _ {v} (\pmb {x}, \hat {v} _ {\theta}) U _ {p}, \end{array}\tag{21}
$$

(22) 

where $\hat { u } _ { \theta }$ and $\hat { v } _ { \theta }$ are the direct NN outputs corresponding to the displacement components, and $U _ { p }$ is the prescribed displacement. $f _ { u }$ and $f _ { v }$ are designed for each problem. To ensure that $\alpha _ { \theta } \in [ 0 , 1 ]$ , the application of the sigmoid function to the direct NN output corresponding to the phase field, $\hat { \alpha } _ { \theta } ,$ is an attractive choice; however, it turns out that its vanishing slope hinders crack nucleation. Therefore, we design the following function, plotted in Fig. 1, to overcome this problem: 

$$
\alpha_ {\theta} = f _ {\alpha} (\hat {\alpha} _ {\theta}) = \left\{ \begin{array}{l l} \frac {\hat {\alpha} _ {\theta}}{4} + \frac {1}{2}, & \mathrm{for} | \hat {\alpha} _ {\theta} | \leq 2 \\ \beta (\hat {\alpha} _ {\theta} + 2), & \mathrm{for} \hat {\alpha} _ {\theta} <   - 2 \\ \beta (\hat {\alpha} _ {\theta} - 2) + 1, & \mathrm{for} \hat {\alpha} _ {\theta} > 2 \end{array} \right.\tag{23}
$$

By setting $\alpha _ { \theta } = f _ { \alpha } ( \hat { \alpha } _ { \theta } )$ in the 1D bar problem, we find that the order of the smallest � for which an NN can learn the correct critical load for crack nucleation is $1 0 ^ { - 3 }$ . So, we set $\beta = 1 0 ^ { - 3 }$ in this paper. 

## 3.2.2. Choice of the activation function

Another important aspect of the NN design is the choice of the non-linear activation function. In PINNs, smooth activations like tanh are frequently employed. However, we find that an NN with this activation fails to learn the correct crack path (see Appendix B). The evolution of the loss during training suggests that an NN with tanh activation fails to represent the energy barrier in the loss landscape which would prevent crack propagation in an incorrect direction. Therefore, we employ ReLU activation with the following modification: 

$$
\boldsymbol {z} _ {k + 1} = \max \{0, m _ {k} (\mathbf {W} _ {k} \boldsymbol {z} _ {k} + \boldsymbol {b} _ {k}) \},\tag{24}
$$

where $m _ { k }$ are learnable coefficients. While initializing the NN, we set $m _ { k } = m _ { 0 } ,$ , where $m _ { 0 }$ is a constant. We observe that while the value of $m _ { k }$ does not change significantly during training, some choices of $m _ { 0 } ,$ , as detailed in Section 4.1, facilitate learning the critical applied displacement for crack initiation or propagation with higher accuracy. 

## 3.2.3. Gradient computation and quadrature

Computation of the gradients poses another challenge. Since the gradient computation using autodifferentiation is known not to work well when the activation function is non-smooth, we use an NN with a smooth activation function to assess the performance of autodifferentiation. When computing the gradients of the fields represented by an NN with tanh activation using autodifferentiation, the learned fields display high-frequency oscillations (similar to those resulting from Gibbs phenomena) leading to the localization of the stress in random directions near the crack tip (see Appendix C). This can be viewed as an undesired modification of the energy barrier, allowing for crack propagation in unexpected directions and leading to an inaccurate crack path prediction. 

To address it, we discretize the domain as we would do in FEA. The field values at the nodes are obtained from the NN, whereas the field values and their gradients within each element, in particular at the Gauss points, are computed using shape functions like in FEA, as follows 

$$
\pmb {u} _ {\theta} ^ {h} (\pmb {x}) = \sum_ {a = 1} ^ {n} N ^ {a} (\pmb {x}) \pmb {u} _ {\theta} ^ {a},
$$

$$
\alpha_ {\theta} ^ {h} (\boldsymbol {x}) = \sum_ {a = 1} ^ {n} N ^ {a} (\boldsymbol {x}) \alpha_ {\theta} ^ {a},
$$

$$
\nabla \pmb {u} _ {\theta} ^ {h} (\pmb {x}) = \sum_ {a = 1} ^ {n} \pmb {u} _ {\theta} ^ {a} \otimes \nabla N ^ {a} (\pmb {x}),
$$

$$
\nabla \alpha_ {\theta} ^ {h} (\boldsymbol {x}) = \sum_ {a = 1} ^ {n} \alpha_ {\theta} ^ {a} \nabla N ^ {a} (\boldsymbol {x}),\tag{25}
$$

where the superscript ℎ denotes the finite element approximation of the fields, $N ^ { a } ( { \pmb x } )$ is the shape function corresponding to node � of the finite element discretization, and $\pmb { u } _ { \theta } ^ { a }$ and $\alpha _ { \theta } ^ { a }$ are the values of $\scriptstyle { u _ { \theta } }$ and $\alpha _ { \theta }$ at the same node, respectively, with $a = 1$ ...� and � as the number of nodes. This approach to gradient computation also makes the training considerably faster. 

We use the finite element discretization also for the purpose of approximating the integral in (18) in order to compute the energy using the NN-based representation of the displacement and phase fields. We evaluate the integral employing Gauss quadrature at each element of the finite element discretization [37]. 

## 3.2.4. Weight regularization

Weight regularization plays an important role in obtaining the correct solution of a phase-field fracture problem using the same level of domain discretization as needed in FEA. In the problem of crack nucleation in a 1D bar in Section $4 . 2 ,$ when employing autodifferentiation for strain computation, the NN learns incorrect solutions with approximately zero energy after crack nucleation. An analysis of the governing PDEs (see Appendix D) reveals that the phase-field model does not constrain the maximum slope of the displacement field near the localized phase field, thus this slope depends on the expressivity of the NN. Therefore, if the training points are not fine enough to resolve the sharply changing displacement field expressible by the NN, and not only the length scale $l ,$ the DRM vields incorrect solutions as shown in Fig. D.26. Correct results can be obtained by a finer discretization of h d h d d l h l l h l h h ll ff finer resolution than needed for FEA computations. Note that, while we first recognized the issue when adopting autodifferentiation, the employment of gradient computation by finite element discretization (as illustrated in Section 3.2.3) does not solve this issue. Instead, a solution is to limit $\left( \frac { \mathrm { d } u _ { \theta } ^ { - } } { \mathrm { d } x } \right)$ by introducing weight regularization. This leads to a computationally efficient approach, in <sup>���</sup>which the discretization of the domain needed for an accurate solution is comparable to the one used in FEA. Therefore, we employ weight regularization throughout the examples in this paper, see Section 4.1 for more details. 

## 3.2.5. Choice of the optimization algorithm

Optimization algorithms play a key role in the training of an NN and selecting one that respects energy barriers and reaches the correct local energy minimum is essential. In this study, we consider the second-order L-BFGS algorithm [57] and the first-order resilient backpropagation (RPROP) algorithm [60]. While L-BFGS is the fastest of the two, it is unable to reach a good energy minimum with the localized phase field and the sharply varying displacement field (see Appendix E). In contrast, the RPROP algorithm is observed to respect energy barriers and reach the desired energy minimum. It should be noted that the performance of other first-order optimization algorithms like Adam for these problems was considerably poorer compared to L-BFGS and RPROP, hence we do not consider them further in this work. 

## 3.2.6. Transfer learning

As loading is applied in incremental steps, we utilize transfer learning to learn the solution quickly. The trained network from the previous loading step is used as the initial network for training in the current loading step. We observe that transfer learning enables learning the solution field in typically fewer than 500 steps of the RPROP optimizer provided a load step does not lead to a sudden crack propagation and associated jump in energy. 


Table 1



Summary of the final setup of the DRM approach


<table><tr><td>Feature</td><td>Value</td></tr><tr><td>Number of Networks</td><td>One</td></tr><tr><td>Activation</td><td>Adaptive ReLU</td></tr><tr><td>Dirichlet boundary conditions</td><td>Hard enforcement</td></tr><tr><td>Phase-field constraint</td><td><eq>f_{\alpha}(\hat{\alpha}_{\theta})</eq></td></tr><tr><td>Gradient computation</td><td>Numerical</td></tr><tr><td>Integration</td><td>Gauss quadrature</td></tr><tr><td>Optimizer</td><td>RPROP</td></tr></table>

## 3.2.7. Nucleation and damage evolution

Our experience shows that crack nucleation is more challenging to learn than crack propagation. In the AT1 model, the phase field does not evolve slowly with increasing load but jumps abruptly from 0 to 1 at the location of crack nucleation when the threshold loading for crack nucleation is reached. This poses a formidable challenge for NNs to learn crack nucleation in 2D. Therefore, for 2D problems involving crack nucleation we employ the AT2 model, which allows for a slow evolution of the phase field to nonzero values before it jumps to 1 at the threshold loading condition. 

## 3.2.8. Summary

To summarize, our approach involves one NN with adaptive ReLU activation expressing both the displacement and phase fields. Dirichlet boundary conditions are enforced employing an ansatz which also ensures that the NN outputs corresponding to the displacement field are approximately ∼ 1. To incentivize the phase field to lie between 0 and 1 without hindering crack nucleation, we design a new function $f _ { \alpha } ( \hat { \alpha } _ { \theta } )$ . Field gradients are computed numerically like in FEA. To estimate the integral in the computation f h d i l d f h l i di i d d i h i i f h k i h regularization is employed to constrain the maximum strain expressible by the NN. The RPROP algorithm is found to perform best in trainin the NN to learn the solution fields. We also emplo transfer learnin to learn the solution efficientl . Additionall , while the NN learns crack propagation, branching, and coalescence using the AT1 model, it is able to learn crack nucleation in 2D only with the AT2 model. A summary of the approach is also provided in Table 1. 

## 4. Numerical examples

In this section, we first demonstrate crack nucleation in a 1D homogeneous bar and an L-shaped panel. We then study crack propagation in a single-edge notched (SEN) specimen under both tensile and shear loading conditions. To illustrate crack branching, we again model a SEN specimen under shear loading without strain energy decomposition. Crack coalescence is demonstrated by subjecting a specimen with three preexisting cracks to tensile loading. 

Since these examples are taken from the phase-field fracture literature, for each example we use the same material properties as in the corresponding paper. This not only enables an easier comparison with the results of the referenced papers; it also demonstrates that the developed approach works robustly for different material properties (and geometries). Throughout the 2D examples, we assume plane-strain conditions. 

## 4.1. Numerical setup

For the 1D problem, we use an NN of 4 hidden layers and 50 neurons in each layer. The coefficient in the activation function is set to $m _ { 0 } = 1$ , and we do not include $m _ { k }$ among the learnable parameters. The L-BFGS optimizer is found to be sufficient to learn the solution in this case. Eight NNs with different initializations obtained by using Xavier initialization [61] with random seeds are trained for this problem. 

For the 2D problems, we use an NN of 8 hidden lavers and 400 neurons in each laver. The size of the network is chosen based on the numerical experiment conducted for the problem of crack nucleation in an L-shaped panel (see Appendix F). We set $m _ { 0 } = 2$ f k h h d l d $m _ { 0 } = 3$ for the remaining 2D problems. We train 8 NNs with different initializations for each problem employing Xavier initialization with random seeds. In the first loading step, an NN is first trained with L-BFGS before training it with RPROP; for all the subsequent loading steps only RPROP is used. For RPROP, the learning rate is set to $1 0 ^ { - 5 }$ with the smallest and largest step sizes of $1 0 ^ { - 1 0 }$ and $^ { 5 0 , }$ respectively. The remaining optimizer parameters are kept as in the standard implementation in Pytorch. The stopping criterion is set to correspond to a relative change in the loss function of less than $5 \times 1 0 ^ { - 6 }$ for 10 consecutive optimization steps, with a maximum of 10000 optimization steps. Additionally, we apply $L _ { 2 }$ weight regularization with a weight of $1 0 ^ { - 5 }$ . The Pytorch library [62] is used for implementation and training. 

In the 1D problem, we discretize the domain into elements of size $l / 5$ and assume linear shape functions. In the 2D problems, we utilize triangular elements with linear shape functions. Only the regions of the domain where the crack is expected to propagate are finely discretized with elements of size $l / 5 _ { \mathrm { : } }$ , to limit the computational cost. Away from these regions, the element size smoothly increases up to 4�. Discretization is performed using Gmsh [63]. We use one Gauss point per element to compute the integral in the expression of the energy in (18) 

The numerical setup for the reference FEA computations is detailed in Appendix $\mathrm { G } .$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/8bba05cafa7219897c3bc7135fbb1be5956f0fb0dd95fcd1add5ed5595b2f401.jpg)



Fig. 2. 1D bar: geometry and boundary conditions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/2be1858270e17bbb39bacc75159c555d910c92ec9b92731f47293f437a39950a.jpg)



Fig. 3. 1D bar: elastic and fracture energies vs prescribed displacement from NN and FEA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/9ffbba257b6b6a71b83a684dde684b34d1777e37f5cfaf29afd966d8dbba0089.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/4f5c9977ffb76a245f7a8a8fa732e21dbe65fb9d0b2cebb28cfbdb6cdbcbcbe6.jpg)



Fig. 4. 1D bar: displacement and phase fields before and after crack nucleation from NN and FEA.


## 4.2. Crack nucleation in a 1D homogeneous bar

We first study crack nucleation in a linear elastic bar shown in Fig. 2. This problem lends itself to an analysis that sheds light on the reason for the occurrence of incorrect solutions when the domain is not discretized sufficiently finely. 

In this case, the expression of the energy in (18) simplifies to the following form: 

$$
\mathcal {E} (u, \alpha) = \int_ {- 0. 5} ^ {0. 5} \frac {1}{2} g (\alpha) \left(\frac {\mathrm{d} u}{\mathrm{d} x}\right) ^ {2} \mathrm{d} x + \frac {1}{c _ {w}} \int_ {- 0. 5} ^ {0. 5} \left(w (\alpha) + l ^ {2} \left| \frac {\mathrm{d} \alpha}{\mathrm{d} x} \right| ^ {2}\right) \mathrm{d} x.\tag{26}
$$

The only parameter in the above expression is $l ,$ and we set $l = 0 . 0 5$ . We employ the AT1 model (see (2)). The following ansatz is employed to apply the boundary conditions: 

$$
\begin{array}{l} {u _ {\theta} = [ (x + 0. 5) (x - 0. 5) \hat {u} _ {\theta} + (x + 0. 5) ] U _ {p},} \\ {\alpha_ {\theta} = (x + 0. 5) (x - 0. 5) \hat {\alpha} _ {\theta}.} \end{array}\tag{27}
$$

Note that, since fracture at the boundaries requires less energy compared to fracture inside the domain, the NN (as well as the FEA) has a tendency to choose the solution with fracture at the boundary. To suppress this solution, we set $\alpha _ { \theta } = 0$ at the boundaries using the above ansatz. Furthermore, we observe that the constraint $f _ { \alpha } ( \hat { \alpha } _ { \theta } )$ is not required to obtain the solution in this case. Hence, we do not use it here. 

For the 1D bar, the energies obtained from the NN are compared with the FEA solution in Fig. $^ { 3 , }$ showing close agreement. Additionally, the displacement and phase fields before and after crack nucleation are compared with the FEA solution in Fig. 4, again showing that the DRM achieves a quite accurate solution. 

## 4.3. Crack nucleation in an L-shaped panel

This problem illustrates crack nucleation in 2D. The geometry of the panel and the boundary conditions are as shown in Fig $^ { 5 , }$ whereas the material properties are set to $\nu = 0 . 1 8$ and � = 0.01 [54]. To prescribe homogeneous and nonhomogeneous Dirichlet boundary conditions, we construct distance functions $d _ { 1 } ( x , y )$ and $d _ { 2 } ( x , y ) ,$ , respectively, such that $d _ { 1 } ( x , y )$ equals 1 at $y = - 0 . 5$ and smoothly decreases to 0 away from it, and $d _ { 2 } ( x , y )$ equals 1 at the section of the boundary where $U _ { p }$ is applied and smoothly decreases to 0 away from it (see Appendix H for more details): 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/5a2913cf9fe17e7dc025260c8aa34a6638af65afb578a887003875c9460ceeff.jpg)



Fig. 5. L-shaped panel: geometry and boundary conditions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/026a9e22420abe46639841b097d2003c9bf4cc03f97229d3fb0e4ea3af1a0c07.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/dc5e1f5e80c815ce6aaba99ae18ac39f94b8ba20500b3370f0a3f0eff0fcd589.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/0a0e33edc978d7649993116a308b6324266ff7e436a655ec556fd7ed0d5fb845.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/4e934c59f6aef904521eae908aa13c97e42f3497f7323295f3f2e506e757bf27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/7f4176daa56224766d630299ab8f50361cf4f607ae7495cfac697c120b03ff12.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/f254a1690cc174c4c7c26def91511f0d795658f8e9f12f899589a38af348f8c8.jpg)



Fig. 6. L-shaped panel: displacement and phase fields at $U _ { p } = 1 . 2$ from NN and FEA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/4e9e3263e1a33f80ce43a758512ebe32a5bd7c7b5a31e0ec30a04b2c1e70c900.jpg)



Fig. 7. L-shaped panel: elastic and fracture energies vs prescribed displacement from NN and FEA.


$$
\begin{array}{r l} & u _ {\theta} = [ (1 - d _ {1} (x, y)) \hat {u} _ {\theta} ] U _ {p}, \\ & v _ {\theta} = [ (1 - d _ {1} (x, y)) (1 - d _ {2} (x, y)) \hat {v} _ {\theta} + d _ {2} (x, y) ] U _ {p}, \\ & \alpha_ {\theta} = f _ {\alpha} (\hat {\alpha} _ {\theta}). \end{array}\tag{28}
$$

As discussed in Section 3.2, the NN finds it difficult to learn crack nucleation when the AT1 model is employed; therefore, we use the AT2 model in this problem. Fig. 6 compares the solution obtained from the NN with the FEA solution at $U _ { p } = 1 . 2$ . The crack path in the NN solution closely resembles that in the FEA solution, although the FEA solution shows comparatively sharper turning of the crack. Note that, due to the non-convexity of the governing energy functional, even the FEA solution is in general not unique, and changes in the obtained crack patterns may be induced by small perturbations as discussed in [64]. Fig. 7 illustrates the mean and standard deviation of the energies obtained from 8 trained NNs with different initializations, and compares them with the energies obtained from FEA. The energies are in close agreement before crack nucleation, and the NN accurately captures the critical $U _ { p }$ at which nucleation takes place. However. in the subsequent stage the damage energy obtained from the NN is higher than in FEA. This discrepancy results from the difficulty in learning a curving crack and can be improved by reducing the loading step sizes and imposing a stricter stopping criterion for the optimizer, which however would increase the computational cost 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/0eb1ad77ba1b5b3ceaca7b049a34155b58e4026ae9c7d7e18c829c200df7ff8b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/426877a60b4794068d1903dc8ef42ae8f029089686bd21c52d09758e80135e99.jpg)



Fig. 8. SEN specimen: geometry and boundary conditions (left); phase field from NN at the smallest applied tensile load (right).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/75133580bdd1211319c51b1765bc3d44bf53028466416b59a496d16de806226f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/bd48f58ed1fa0302b25383057be52d24fb8312ac043246ead95d917b534d30fb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/3b2f12499ea957b7ef4fab4849f8f18c33f75fb0b56c0026da98777e3d502607.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/97458ef06cfc968d445bfbfb4ae04fbea7d1cbaf8c5f64c05bb39813264aaeee.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/c8968e7b192fd2d1cb96f843960de8291e8875eac222825092a8320b65c1a8bc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/9e2311e16ca5d4d0b5b50f62f7432aaae2bf11104898b14ef2a530b4263953a6.jpg)



Fig. 9. SEN specimen under tensile loading $\scriptstyle ( \omega = \pi / 2 ) :$ displacement and phase fields at $U _ { p } = 0 . 2$ from NN and FEA.


## 4.4. Crack evolution in a notched specimen

The geometry of the SEN specimen and boundary conditions are as shown in Fig. 8, while the material properties are $\nu = 0 . 3$ and � = 0.01 [54]. We define the following ansatz to apply the boundary conditions and to compute �: 

$$
\begin{array}{r} u _ {\theta} = [ (y + 0. 5) (0. 5 - y) \hat {u} _ {\theta} + (y + 0. 5) \cos (\omega) ] U _ {p}, \\ v _ {\theta} = [ (y + 0. 5) (0. 5 - y) \hat {v} _ {\theta} + (y + 0. 5) \sin (\omega) ] U _ {p}, \end{array}
$$

$$
\alpha_ {\theta} = f _ {\alpha} (\hat {\alpha} _ {\theta}).\tag{29}
$$

We define the notch in the sample by setting an initial phase field as described in Appendix I; the NN learns the notch as a localized phase field as shown in Fig. 8. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/8b12e4fd7ddbc944689c392d707698e775c80acaa1799faa659acd585adfd075.jpg)



Fig. 10. SEN specimen under tensile loading $\scriptstyle ( \omega = \pi / 2 ) :$ elastic and fracture energies vs prescribed displacement from NN and FEA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/7a6c4ab7c735e43d46fdc8465d92be94204efcb969f9eb2b43dcb4b04a4fa07f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/b51b1fe406956af70be28eeae78d3b175b97e6b28d12a263b6e87ccdc9de08cb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/22596582db59d82b7f5c671839966a711d8b091f6347c301246ea3a4fa6d0865.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/8e6d1818b62384297e70e4872ce93e1c24a76975efbd15e7d286703bfa957efb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/38cb41818c17b03fa07756f0aa31dbf5485cbda03c48050774ca39480bb1ec50.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/f5fcafa0d1a80163eb79f4ba9e2c2bd23b9b417628ce062bdc2689a3fdd3a502.jpg)



Fig. 11. SEN specimen under shear loading $( \omega = 0 ) \mathrm { : }$ displacement and phase fields at $U _ { p } = 0 . 4$ from NN and FEA.


## 4.4.1. Tensile loading

With this problem. we demonstrate the ability of the NN to learn crack propagation. We subiect the SEN specimen to tensile loading, i.e. the loading angle is $\omega = \pi / 2 ,$ , and adopt the AT1 model. Fig. 9 compares the fields obtained from NN and FEA at $U _ { p } = 0 . 2$ , showing close agreement. In this example, the simplicity of the crack path allows the NN to easily and accurately learn the cracked solution. Fig. 10 compares the energies associated with the NN solution with the energies from FEA, exhibiting once again a close agreement. Note that the comparatively higher standard deviation near the critical load for crack propagation results from differences in the prediction of the critical load for different initializations of the NN. 

## 4.4.2. Shear loading

This problem demonstrates the ability of the NN to learn crack kinking, i.e. the change in direction of a crack. To this aim, we subject the SEN specimen to shear loading, i.e. the loading angle is $\omega = 0 ,$ and again use the AT1 model. The displacement and phase fields obtained from the NN at $U _ { p } = 0 . 4$ are compared with the FEA solution in Fig. 11. showing close agreement. Note that FEA encounters convergence issues for $U _ { p } > 0 . 4 _ { : }$ while the NN does not exhibit any problem even in that range, as demonstrated by Fig. 12, which shows the fields at $U _ { p } = 0 . 4 7$ 

The energies associated with the NN solution are compared with the energies from FEA in Fig. 13. They are also very close, although the critical load for crack propagation in the NN solution is slightly higher than in FEA. Moreover, higher standard deviations in the energies result from slight variations in the critical loads for different NN initializations. 

## 4.5. Crack branching in a notched plate

To demonstrate crack branchin , we a ain prescribe the shear loadin condition on the SEN specimen, i.e. $\omega = 0 .$ . In this problem, in the absence of the strain energy decomposition in (4), which differentiates between tensile and compressive stresses, unphysical branching of the crack occurs [3]. Since in this case we do not seek a physically realistic prediction of the behavior but rather an accurate solution of the governing PDEs, we purposefully omit the strain energy decomposition, i.e. we take $\psi ^ { + } = \psi$ and $\psi ^ { - } = 0 .$ Fig. 14 illustrates that the NN is able to learn crack branching. The fields obtained from the NN at $U _ { p } = 0 . 3 7$ are compared with the FEA solution in Fig. 14, displaying again a good agreement, with some differences in the prediction of the curvature of the crack path. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/f2fa6d1dcecc8f786ec001a0e1cd85212a3a734e2b84af5537be74966bf6de4d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/2b1346ebc10ff871238fc0467ccc7c02990c02a8629889ec498ac01ad7ed4a51.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/9be11f7147ca46a23f2aaf319b159c74f360e0aea7878bfc2b67210a96401872.jpg)



Fig. 12. SEN specimen under shear loading (� = 0): displacement and phase fields at $U _ { p } = 0 . 4 7$ from NN.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/c0b8f1b68d34ddfb5210ccc019d5fc564766eab6024e7ad3c94ed4919fe670b2.jpg)



Fig. 13. SEN specimen under shear loading (� = 0): elastic and fracture energies vs prescribed displacement from NN and FEA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/6d1de878bdd8458acbd41fd8d6cd1ba3fcf448d70e844015a19b1888c8d3e50d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/c68961dc9ea3f47fcfef9a730c39a59b9acbfbc93aca1c046c227e1fc028280e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/e9cfcc2f31037b8f661d948d1b0d94fa67fa302498e6fe4d777674201eea327a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/24d67596e622d2a91bdd311fb59b8153bf3c0de212a31d3f5647d50286eaed39.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/8502c54fe2088cfb7514d8b226f56f9f389ddb2bd4ca5661288bb282bb3598b5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/c424448c147d15557733bfafb7bbb66a93b5c96454c6783ddd3d8b66eab3b783.jpg)



Fig. 14. Crack branching test: displacement and phase fields at $U _ { p } = 0 . 3 7$ from NN and FEA.


The evolution of the energies with $U _ { p }$ obtained from the NN are compared with the FEA energies in Fig. 15. The critical load at which branching initiates shows variability for different NN initializations, leading to a higher standard deviation; however, the average value is close to the critical load predicted by FEA. Also. the difficulty encountered by the NN in learning the curvature of h k h fl d h d f h f h d f f h l l d h f h 8 NNs had difficulty in learning branching; the corresponding result is not included in the computation of the mean and standard deviation of the energies. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/e3861a286b08909127757a56ef2e0d3ddf27d91c747f27fe04a9667ff0ba3ecc.jpg)



Fig. 15. Crack branching test: elastic and fracture energies vs prescribed displacement from NN and FEA


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/66d65e400a39dc533f080da9005ca6feba96ede2230181e1614aa1a5d8b121a9.jpg)



Fig. 16. Crack coalescence test: geometry of the specimen and boundary conditions (left) and phase field at the location of the cracks from NN at the smalles applied load in training (right).


## 4.6. Crack coalescence in a plate with cracks

To demonstrate crack coalescence, tensile loading is applied on a specimen with preexisting cracks (Fig. 16). In this case, we again adopt (29) with loading angle $\omega = \pi / 2 ,$ , and the material properties are $\nu = 1 / 3$ and $l = 0 . 0 1 \ [ 6 5 ]$ . We use a larger value for � in comparison to [65] to reduce the computational cost. 

Fig. 17 demonstrates that the NN is able to learn crack coalescence. Unlike in the FEA solution, cracks starting from the initial cracks and reaching the domain boundaries are at an angle from the horizontal direction. On the other hand, as discussed earlier, the FEA solution itself is not guaranteed to be unique [64]. 

The energies obtained from the NN with increasing $U _ { p }$ are compared with the FEA energies in Fig. 18. The critical load at which propagation and merging occurs, while close to the FEA prediction, shows slight variability for different NN initializations, leading to a higher standard deviation near the critical load. The energies obtained from the NN after the crack propagates through the sample are in close agreement with the FEA energies even though the crack paths show differences. This suggests that different crack path may be competing at similar energy levels, which is a known phenomenon in phase-field fracture modeling [64]. An alternative explanation may be that the NN is not reaching a sufficiently deep energy minimum, in which case results can be improved by prescribing a stricter stopping criterion for the optimizer. Note that here two NNs (out of 8) exhibit difficulty in learning the correct crack evolution, thus the corresponding results are not included in the computation of the mean and standard deviation of the energies. 

## 4.7. Computational cost

Training of the NNs is performed on NVIDIA GeForce RTX 2080 Ti GPUs. whereas FEA computations are performed on Intel(R) Xeon(R) W-2223 CPUs. While our DRM approach is robust and we are able to learn solutions involving various fracture phenomena, we observe that the DRM is computationally more expensive compared to FEA. with the training for NNs taking up to one order of magnitude longer than the corresponding FEA computations in some cases. This observation is not surprising; our aim in this work was not to deliver an alternative solution framework for a single boundary value problem in phase-field fracture, but rather to develop a robust approach which can lay the foundation to solve parametric phase-field fracture problems with the DRM. 

## 5. Conclusions

To harness physics-informed deep learning for phase-field fracture modeling, we propose the design of an NN and of a learning approach based on the DRM, aimed at learning complex fracture processes. The main conclusions of this work are as follows: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/6fcfeb2ab5ab1c4dd3840cfff2f94b6309b10b23413da36656c0d3c6cdcad711.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/bfb08ecebae4e31d4f59bc4be160db4eddcc7a7068258ef065ca349136ef257e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/503633a0d448eb3847c3cc584d08f1b065b9ad82d050a922d044fefdaf43d781.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/12512333160788ae4050a0909c3ac14c2dd90c87437ba408f31365dbed7d854f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/60aad34ba25b596a50eb8cc9a872deb520923a0f2947eebb27b4855ee76dd06b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/b77793c1b3527e66f1e37d4c9b57f95c26363c83a7e4ed829b425fefe29ba5c1.jpg)



Fig. 17. Crack coalescence test: displacement and phase fields at $U _ { p } = 0 . 2$ from NN and FEA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/ac5a53f467349fcdd7f4875a729283605402712cd1b1eb6021ed385f92b371db.jpg)



Fig. 18. Crack coalescence test: elastic and fracture energies vs prescribed displacement from NN and FEA.


• <sub>Phase-field fracture modeling requires solving a coupled problem which involves fields with sharp spatial variations. Training</sub> l h f ld h ll f l l h d h b l f h l approximate the energy surface and, on the other hand, on the ability of an optimizer to reach the correct local minimum respecting the energy barriers. 

• We empirically establish that fully connected feed-forward NNs. with a modified ReLU activation and an appropriate ansatz in the construction of the solution fields, along with weight regularization and numerical gradient computation, is able to learn complex fracture processes. Furthermore, RPROP is found to be the most effective optimization algorithm for training. 

• <sub>Our approach can solve examples of crack initiation, propagation, kinking, branching, and coalescence taken from the</sub> phase-field fracture literature, within one single numerical setup. Results in terms of solution fields and energy vs. applied displacement curves are in quantitatively excellent agreement with the respective FEA results. Additionally, our approach is robust to different network initializations. 

In this work, we focused on the design of a robust NN and learning approach to learn the solution of boundary value problems involving diverse fracture phenomena in phase-field fracture modeling. While our approach is computationally expensive compared to FEA, our aim is not to deliver an alternative solution framework for a single boundary value problem in phase-field fracture; rather, the present work is intended as the first step in the direction of learning solutions to parametric phase-field fracture models with the DRM. In this setting, NNs can be trained on a few realizations of the parameter space and results can then be inferred online for all other realizations, leveraging the true potential of the DRM. Learning solutions to parametric phase-field fracture models will b h l f f h 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/14b297a24c0be27306e24a3c950c5961e5e395199f0d00d60c23e98bdf6453f7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/e77ea5c4667478f34d0f9b148198409001bd88ac70f6a1de12a96f3049c2eee2.jpg)



Fig. A.19. Phase field at $U _ { p } = 0 . 4$ after crack propagation (left) and energies (right) for the SEN specimen under shear loading (� = 0) when the displacement and phase fields are represented by two separate NNs.


## CRediT authorship contribution statement

M. Manav: Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. R. Molinaro: Writing – review & editing, Methodology, Conceptualization. S. Mishra: Writing – review & editing, Methodology, Conceptualization. L. De Lorenzis: Writing – review & editing, Supervision, Methodology, Funding acquisition, Conceptualization 

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## Data availability

Data will be made available on request. 

## Acknowledgments

We acknowledge funding from the Swiss National Science Foundation through Grant No. 200021-219407 ‘Phase-field modeling of fracture and fatigue: from rigorous theory to fast predictive simulations’. 

## Code availability

The code used to produce the numerical results in the paper is available at https://gitlab.ethz.ch/compmech/phase-field-fracturewith-pidl. 

## Appendix A. Independent nns for the displacement and phase fields

Using independent NNs for the physically different fields to learn their unique features separately can be expected to make training faster. We construct two NNs, each with 8 hidden layers and 200 neurons, which represent the displacement and phase fields separately, with all the other settings as in Section 4. Note that this NN configuration lowers the number of the learnable parameters. The displacement and phase fields obtained from the two networks are then used to compute the energy and construct the loss function using (20). The parameters of both networks are simultaneously trained to minimize the loss. We first study the SEN specimen under shear loading described in Section 4.4.2, and conclude that the NNs are able to learn crack propagation, as shown in Fig. A.19. Subsequently. we use the two NNs to learn crack nucleation in an L-shaped panel as described in Section 4.3: here, the NNs are unsuccessful, as shown in Fig. A.20. So, we use one NN to represent both the fields for all the problems. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/c6fbeca3939b7fa57b273f0f2486e23890c2e0d6dd45fff3a1b57a5878eb82f7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/b3df34039aeb113fbaabc4f0f0bc7cac749d76a88bf9a5031dcb28a9ab1f82fd.jpg)



Fig. A.20. Phase field at $U _ { p } = 1 . 2$ (left) and energies (right) for the L-shaped panel when the displacement and phase fields are represented by two separate NNs. In this case, the crack fails to nucleate.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/6388ca3483e474619338d5aaad2a71fdcaafa603aa98a1e12ee760d898c46401.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/59f7d54e715ff1733f0d8fac4dd246996de4cdb2beb90a9ebb6d6a6fbff474b9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/a40edb137fb6c4572c5f579f6bf456749b3d6f986b64042204ad6454c0135c9d.jpg)



Fig. B.21. Stress field at $U _ { p } = 0 . 3 1$ in the SEN specimen under shear loading (� = 0) when tanh activation is employed.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/164d13fe4025b027c6f4553f427d6f893846881b7f9820ceb5310656c0255a7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/6436447fa286c5809f96cc6462bbd2ad646c14d4c9c109cc59b06297eb271c1d.jpg)



Fig. B.22. Phase field at $U _ { p } = 0 . 3 2$ in the SEN specimen under shear loading (� = 0) (left) and evolution of the loss function during training (right) when tanh activation is employed.


## Appendix B. Activation functions

We assess the ability of the NNs with different activation functions in learning crack propagation in the SEN specimen under shear loading. We use the same NN size and optimizer settings as in Section 4.4.2, but set the activation function to be tanh. As shown in Fig. B.21, the NN is able to learn the displacement and phase fields which yield sharp stress fields near the crack tip. 

It also learns the critical $U _ { p }$ for crack propagation accurately. However, it fails to learn the correct crack path as shown in Fig. B.22. Furthermore, the smoothly decreasing loss and the comparison of the phase fields at two different optimization steps shown in Fig. B.22 suggest that the NN-based representation of the loss lacks the energy barrier which could prevent the NN from learning the incorrect solution. 

## Appendix C. Autodifferentiation for gradient computation

When employing a smooth activation and autodifferentiation for gradient computation, the solution field exhibits spurious ll h d l f ld h b bl $4 . 2 ,$ learned using an NN with 2 hidden lavers and 20 neurons with the tanh activation function, exhibits oscillations as shown in Fig. C.23. We also train an NN with 6 hidden lavers and 50 neurons with tanh activation to learn the solution of the SEN specimen under shear loading. While spurious oscillations in the displacement field are not apparent, they can be observed in the stress field as shown in Fig. C.24. Furthermore, at the critica $U _ { p } ,$ the crack propagates in an incorrect direction as shown in Fig. C.25. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/45ffbdeecffaaa83b81026e67bf5f4228719e48d067757829f5b9d99a5e0f2fc.jpg)



Fig. C.23. Spurious oscillations observed in the displacement field after the localization of the phase field in the 1D bar problem when the gradient is computed using autodifferentiation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/a814ee7fc6d87199b84b8dbe8d0130cfa8c017ea28d6ed226d72377f0785aa7d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/d7175399371fae2f3f0b4e3e7e8982faf8c88372aba398fb0bb08e08d03f524f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/7419f0fc117c181881792ed905632e31f327669847e567934b0dccc1e4af8d52.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/970e26546157cfbbd52a3978767212ab996f0527d37cce6528cd0e1c140b9d26.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/47f4a10bd6f275e63f4cd2be56e4b77d7bc39e8c60af393b02eb90eed78cfa35.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/9e05463f1fcf413df1935bdda8cf1223ccc9e8f2e9275179fe1382cf6bf970b4.jpg)



Fig. C.24. Displacement field, phase field, and stress field at $U _ { p } = 0 . 3 1$ in the SEN specimen under shear loading (� = 0) when the gradient is computed using autodifferentiation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/e7d5f031c2b8de0dc6220c5c6fddf308f041dd15f5abb327f730027842ea6bfc.jpg)



Fig. C.25. Phase field at $U _ { p } = 0 . 3 2$ in the SEN specimen under shear loading (� = 0) when the gradient is computed using autodifferentiation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/1db9904467bd69e40bcabdf5839c2a8e84c72ac4d2214f26ed5d52fe4da02796.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/3ce7280ec2a8945194aa43d38b9a827000eb98a4826e60cad42960cc8ff0c253.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/2c1f2f661dbbcaee9a67f261c8b47b947fccbd882c3a1e88d69a7910590a7584.jpg)



Fig. D.26. Incorrect displacement field, phase field and energies when the maximum strain expressed by the NN solution is not controlled. The plots are obtained using an NN with 2 hidden layers and 20 neurons with the tanh activation. The correct solution fields and energies are shown in Fig. 4 and Fig. 3, respectively.


## Appendix D. The maximum strain in the 1D bar

For the bar described in Section 4.2, the equilibrium equation is given by 

$$
\frac {\mathrm{d} \sigma}{\mathrm{d} x} = 0,\tag{D.1}
$$

hence, the stress in the bar is uniform. Since $\begin{array} { r } { \sigma = g ( \alpha ) \frac { \mathrm { d } u } { \mathrm { d } x } } \end{array}$ , the strain can be expressed as $\begin{array} { r } { \frac { \mathrm { d } u } { \mathrm { d } x } = \frac { \sigma } { g ( \alpha ) } = S ( \alpha ) \sigma , } \end{array}$ , where $S ( \alpha ) = 1 / g ( \alpha )$ is the compliance. 

During evolution of the phase field, Eq. (11) (written as equality since $\alpha > \alpha _ { n - 1 } ) .$ , reads 

$$
- \frac {1}{2} S ^ {\prime} (\alpha) \sigma^ {2} + w _ {1} \left[ w ^ {\prime} (\alpha) - 2 l ^ {2} \frac {\mathrm{d} ^ {2} \alpha}{\mathrm{d} x ^ {2}} \right] = 0,\tag{D.2}
$$

where $\begin{array} { r } { w _ { 1 } = \frac { 1 } { c _ { w } } } \end{array}$ and the first term has been modified to express it in terms of compliance and stress. Multiplying the above equation with $\frac { \mathrm { d } \alpha } { \mathrm { d } x }$ and integrating with respect to � yields 

$$
- \frac {1}{2} S (\alpha) \sigma^ {2} + w _ {1} \left[ w (\alpha) - l ^ {2} \left(\frac {\mathrm{d} \alpha}{\mathrm{d} x}\right) ^ {2} \right] = C,\tag{D.3}
$$

h h f f h f l l f h h f ld d d h h $w = 0$ and $S = 1 )$ , we obtain $\begin{array} { r } { C = - \frac { 1 } { 2 } \sigma ^ { 2 } ; } \end{array}$ f h b f $\begin{array} { r } { \frac { \mathrm { d } u } { \mathrm { d } x } = S ( \alpha ) \sigma } \end{array}$ yields 

$$
\frac {\mathrm{d} u}{\mathrm{d} x} = \sigma + \frac {2 w _ {1}}{\sigma} \left[ w (\alpha) - l ^ {2} \left(\frac {\mathrm{d} \alpha}{\mathrm{d} x}\right) ^ {2} \right].\tag{D.4}
$$

At the location in the bar where the maximum strain occurs, the following condition holds 

$$
\frac {\mathrm{d}}{\mathrm{d} x} \left(\frac {\mathrm{d} u}{\mathrm{d} x}\right) = \left(w ^ {\prime} (\alpha) - 2 l ^ {2} \frac {\mathrm{d} ^ {2} \alpha}{\mathrm{d} x ^ {2}}\right) \frac {\mathrm{d} \alpha}{\mathrm{d} x} = 0,\tag{D.5}
$$

hence, $\begin{array} { r } { \frac { \mathrm { d } \alpha } { \mathrm { d } x } = 0 } \end{array}$ and 

$$
\left(\frac {\mathrm{d} u}{\mathrm{d} x}\right) _ {m a x} = \sigma + \frac {2 w _ {1} w (\alpha)}{\sigma}.\tag{D.6}
$$

When the phase field localizes, the stress in the bar goes from a positive value to 0 (however, for $\sigma = 0$ h ll d l f l forms, where $\textstyle { \frac { \mathrm { d } \alpha } { \mathrm { d } x } } \neq 0$ at the center). When the stress approaches $^ { 0 , }$ the maximum of strain. given by $\left( \mathrm { D } . 6 \right) ,$ is unbounded. In FEA. the maximum strain is set by the element size which is chosen small enough to resolve the length scale �. In contrast, the maximum strain in the DRM is dictated by the expressivity of the NN. Consequently, if the training points are not fine enough to resolve the sharp slope of the displacement field expressible by an NN and not only the length scale $l ,$ the DRM yields an incorrect solution as shown in Fig. D.26. 

## Appendix E. The limitations of the L-BFGS optimizer

To probe the ability of the L-BFGS optimizer in learning the sharp fields in the DRM, we apply it to learn the solution of the SEN sample under shear loading as described in Section 4.4.2. We train the same NN used in Section 4.4.2. As shown in Fig. E.27, the NN fails to learn the sharp displacement field even before crack propagation begins. It also does not learn crack propagation as $U _ { p }$ is increased. 

## Appendix F. Network size estimation

We conduct numerical experiments with different network sizes for the problem of crack nucleation in an L-shaped panel in Section 4.3. The energies associated with the solutions obtained from networks with different sizes are compared in Fig. F.28. d h h k h h dd l d f ll h bl l d h k 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/e917f85fa5fe7334956eb21741c5d9f48e3996908826f72b6506c4542a42f0cc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/86f66b62d2376ee2bda0aab27dfeec7a8131ca6112c6de7f8cad1c22bf681bff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/853bebefb56b64701435ab73135ea8177bf4ef8f50aad01d3af8319769f650ee.jpg)



Fig. E.27. Displacement and phase fields at $U _ { p } = 0 . 3 1$ for the SEN specimen under shear loading $\left( \omega = 0 \right)$ when the fields are learned using only the L-BFGS optimizer.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/b9ac3fcd1538a091b0477dad7b6089616e54085681d11f85155d75d42e56e463.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/cc21047d18789790e312ddc0e5003ea57a681ff37fd8a362ae87384d4a2f2909.jpg)



Fig. F.28. Energy associated with the solutions learned with different network sizes vs prescribed displacement. In the left $\mathsf { p l o t } .$ , the number of neurons is 400; h h l h b f h dd l hl h dd l


## Appendix G. Numerical setup for FEA

In the FEA computation for the 1D problem in Section 4.2, we discretize the domain into elements of size $l / 5$ and assume linear shape functions. To obtain the solution of the 2D problems, we employ quadrilateral elements with bilinear shape functions and two Gauss points per parametric direction. To compute the energy using (18), we employ elementwise Gauss quadrature with the same setup. The regions of the domain where the crack is expected to propagate are discretized with elements of size $l / 5 .$ . The element size smoothly increases up to 4� away from these regions. 

Initial cracks are modeled by prescribing $\alpha = 1$ at the location of the crack and solving a so-called recovery problem. We set an irreversibility tolerance of $\mathrm { T } \mathsf { O L } _ { i r } = 1 0 ^ { - 3 }$ . The staggered solution algorithm together with the Newton–Raphson procedure is employed to iteratively converge to the solution [54]. We set an error tolerance on the residual norm of $1 0 ^ { - 4 }$ for the staggered scheme and $1 0 ^ { - 6 }$ for the Newton–Raphson procedure. Moreover, we set a maximum of 500 iterations for the Newton–Raphson procedure and 1000 iterations for the staggered scheme. 

The FEA computation is performed using the GRIPHFiTH code available at https://gitlab.ethz.ch/compmech/GRIPHFiTH. 

## Appendix H. Distance functions for the L-shaped panel

To ensure the strict enforcement of the Dirichlet boundary conditions in the problem in Section 4.3, we construct distance functions that satisfy $C ^ { 1 }$ continuity. For applying the fixed boundary condition at $y = - 0 . 5$ , we construct the following distance function: 

$$
d _ {1} (x, y) = \left\{ \begin{array}{l l} \left(\frac {y + 0 . 5}{a} - 1\right) ^ {2}, & \text { for } y + 0. 5 \leq a \\ 0, & \text { otherwise } \end{array} \right.\tag{H.1}
$$

To apply the prescribed displacement on a section of the boundary shown in ${ \mathrm { F i g . ~ } } 5 ,$ we construct the following distance function: 

$$
d _ {2} (x, y) = \left\{ \begin{array}{l l} \left(\frac {| y |}{a} - 1\right) ^ {2}, & \text { for } x \geq 0. 4 4 \text { and } | y | \leq a \\ \left(\frac {\sqrt {(0 . 4 4 - x) ^ {2} + y ^ {2}}}{a} - 1\right) ^ {2}, & \text { for } x \leq 0. 4 4 \text { and } \sqrt {(0 . 4 4 - x) ^ {2} + y ^ {2}} \leq a \\ 0, & \text { otherwise } \end{array} \right.\tag{H.2}
$$

In this work, we set $a = 0 . 1$ 1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/00021c96-67b9-4cad-9e1c-140d6c34efca/32d64479cb913762bb1594e66af7a17f26b85f20c0b42541248b2a982d49dc84.jpg)



Fig. I.29. A sample with an initial crack.


## Appendix I. Initial � in a notched sample

To define the initial � in a notched sample, we make use of the analytical expression for � in a 1D bar upon crack nucleation [4]. Below we provide the expression for the initial � in a notched sample shown in Fig. I.29 in the AT1 model. Note that $x ^ { \prime } - y ^ { \prime }$ is the transformed coordinate system aligned with the crack and with its origin at one end of the crack. 

$$
\alpha_ {0} = \left\{ \begin{array}{l l} \left(1 - \frac {| y ^ {\prime} |}{2 l}\right) ^ {2}, & \text {for 0 <   x^{\prime} <   L_{c} and |y^{\prime}| <   2l} \\ \left(1 - \frac {\sqrt {x ^ {\prime 2} + y ^ {\prime 2}}}{2 l}\right) ^ {2}, & \text {for x^{\prime} <   0 and \sqrt {x^{\prime 2} + y^{\prime 2}} <   2l} \\ \left(1 - \frac {\sqrt {(x ^ {\prime} - L _ {c}) ^ {2} + y ^ {\prime 2}}}{2 l}\right) ^ {2}, & \text {for x^{\prime} > L_{c} and \sqrt {(x^{\prime} - L_{c})^{2} + y^{\prime 2}} <   2l} \\ 0, & \text {otherwise} \end{array} \right.\tag{I.1}
$$

## References



[1] B. Bourdin, G.A. Francfort, J.-J. Marigo, Numerical experiments in revisited brittle fracture, J. Mech. Phys. Solids 48 (4) (2000) 797–826. 





[2] B. Bourdin, G.A. Francfort, J.-J. Marigo, The variational approach to fracture, J. Elasticity 91 (1) (2008) 5–148 





[3] M. Ambati, T. Gerasimov, L. De Lorenzis, A review on phase-field models of brittle fracture and a new fast hybrid formulation, Comput. Mech. 55 (2) (2015) 383–405. 





[4] J.-Y. Wu, V.P. Nguyen, C.T. Nguyen, D. Sutula, S. Sinaie, S.P. Bordas, Phase-field modeling of fracture, Adv. Appl. Mech. 53 (2020) 1–183. 





[5] B. Bourdin, J.-J. Marigo, C. Maurini, P. Sicsic, Morphogenesis and propagation of complex cracks induced by thermal shocks, Phys. Rev. Lett. 112 (1) (2014) 014301. 





[6] R. Alessi, M. Ambati, T. Gerasimov, S. Vidoli, L. De Lorenzis, Comparison of phase-field models of fracture coupled with plasticity, in: Advances in computational plasticity: A book in honour of D. Roger J. Owen, Springer, 2018, pp. 1–21. 





[7] C. Luo, L. Sanavia, L. De Lorenzis, Phase-field modeling of drying-induced cracks: Choice of coupling and study of homogeneous and localized damage, Comput. Methods Appl. Mech. Engrg. 410 (2023) 115962. 





[8] Y. Heider, A review on phase-field modeling of hydraulic fracturing, Eng. Fract. Mech. 253 (2021) 107881. 





[9] T. Wu. A. Carpiuc. M. Poncelet, L. De Lorenzis, Phase-field simulation of interactive mixed-mode fracture tests on cement mortar with full-field displacement boundary conditions, Eng. Fract. Mech. 182 (2017) 658–688. 





[ ] f i i i i b i l f i i i i bl h h lid ( ) ( ) 





[11] K. Pham, H. Amor, J.-J. Marigo, C. Maurini, Gradient damage models and their use to approximate brittle fracture, Int. J. Damage Mech, 20 (4) (2011) 618–652. 





[12] LD. Lorenzis, T. Gerasimoy, Numerical implementation of phase-field models of brittle fracture, in: Modeling in Engineering using Innovative Numerica h d f l d d l d 





[13] G.E. Karniadakis, I.G. Kevrekidis, L. Lu. P. Perdikaris, S. Wang, L. Yang, Physics-informed machine learning, Nat. Rey, Phys, 3 (6) (2021) 422–440 





k d f l l k f l d d l d ff l l 987–1000. 





[15] J. Sirignano, K. Spiliopoulos, DGM: A deep learning algorithm for solving partial differential equations, J. Comput. Phys. 375 (2018) 1339–1364. 





[16] M. Raissi, P. Perdikaris, G.E. Karniadakis, Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, J. Comput. Phys. 378 (2019) 686–707. 





[17] E. Kharazmi, Z. Zhang, G.E. Karniadakis, Hp-VPINNs: Variational physics-informed neural networks with domain decomposition, Comput. Methods Appl. Mech. Engrg. 374 (2021) 113547. 





[18] W. E, B. Yu, The deep Ritz method: a deep learning-based numerical algorithm for solving variational problems, Commun. Math. Stat. 6 (1) (2018) 1–12 





[19] S. Mishra, A machine learning framework for data driven acceleration of computations of differential equations, Math. Eng. 1 (1) (2019) 118–146. 





[20] S. Mishra, R. Molinaro, Estimates on the generalization error of physics-informed neural networks for approximating PDEs, IMA J. Numer, Anal. (2022) 





[21] G. Cybenko, Approximation by superposition of sigmoidal functions, Math, Control Signals Systems 2 (4) (1989) 303–314. 





[22] K. Hornik, M. Stinchcombe, H. White, Multilaver feedforward networks are universal approximators, Neural Netw, 2 (5) (1989) 359–366 





[23] D. Yarotsky, Error bounds for approximations with deep ReLU networks, Neural Netw. 94 (2017) 103–114. 





[24] E. Haghighat, M. Raissi, A. Moure, H. Gomez, R. Juanes, A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics, Comput. Methods Appl. Mech. Engrg. 379 (2021) 113741. 





[25] C. Rao, H. Sun, Y. Liu, Physics-informed deep learning for computational elastodynamics without labeled data, J. Eng. Mech. 147 (8) (2021) 04021043 





[26] E. Zhang, M. Dao, G.E. Karniadakis, S. Suresh, Analyses of internal structures and defects in materials using physics-informed neural networks, Sci. Adv. 8 (7) (2022) eabk0644. 





[27] S. Rezaei, A. Harandi, A. Moeineddin, B.-X. Xu, S. Reese, A mixed formulation for physics-informed neural networks as a potential solver for engineering problems in heterogeneous domains: comparison with finite element method, Comput. Methods Appl. Mech. Engrg. 401 (2022) 115616. 





[28] A. Henkes, H. Wessels, R. Mahnken, Physics informed neural networks for continuum micromechanics, Comput. Methods Appl. Mech. Engrg. 393 (2022) 114790. 





[29] J.-H. Bastek, D.M. Kochmann, Physics-informed neural networks for shell structures, Eur. J. Mech. A Solids 97 (2023) 104849 





[30] S. Niu, E. Zhang, Y. Bazilevs, V. Srivastava, Modeling finite-strain plasticity using physics-informed neural network and assessment of the network performance, J. Mech. Phys. Solids 172 (2023) 105177. 





[31] S.A. Faroughi, N.M. Pawar, C. Fernandes, M. Raissi, S. Das, N.K. Kalantari, S. Kourosh Mahjour, Physics-guided, physics-informed, and physics-encoded neural networks and operators in scientific computing: Fluid and solid mechanics, J. Comput. Inf. Sci. Eng. 24 (4) (2024). 





[32] Y. Shin, J. Darbon, G.E. Karniadakis, On the convergence and generalization of physics informed neural networks, 2020, arXiv e-prints, arXiv–2004. 





[33] S. Mishra, R. Molinaro, Estimates on the generalization error of physics-informed neural networks for approximating a class of inverse problems for PDEs IMA J. Numer. Anal. 42 (2) (2022) 981–1022. 





[34] A.D. Jagtap, E. Kharazmi, G.E. Karniadakis, Conservative physics-informed neural networks on discrete domains for conservation laws: Applications to forward and inverse problems, Comput. Methods Appl. Mech. Engrg. 365 (2020) 113028. 





[35] A.D. Jagtap, G.E. Karniadakis, Extended physics-informed neural networks (XPINNs): A generalized space-time domain decomposition based deep learning framework for nonlinear partial differential equations, in: AAAI Spring Symposium: MLPS, 2021, pp. 2002–2041. 





[36] B. Moseley, A. Markham, T. Nissen-Meyer, Finite basis physics-informed neural networks (FBPINNs): a scalable domain decomposition approach for solving differential equations, Adv. Comput. Math. 49 (4) (2023) 62. 





[37] V.M. Nguyen-Thanh, X. Zhuang, T. Rabczuk, A deep energy method for finite deformation hyperelasticity, Eur. J. Mech. A Solids 80 (2020) 103874. 





[38] E. Samaniego, C. Anitescu, S. Goswami, V.M. Nguyen-Thanh, H. Guo, K. Hamdia, X. Zhuang, T. Rabczuk, An energy approach to the solution of partial differential equations in computational mechanics via machine learning: Concepts, implementation and applications, Comput. Methods Appl. Mech. Engrg. 362 (2020) 112790. 





[39] E.S. Mistakidis, G.E. Stavroulakis, Nonconvexity in engineering applications, in: Nonconvex Optimization in Mechanics: Algorithms, Heuristics and Engineering Applications By the F.E.M., Springer US, Boston, MA, 1998, pp. 3–21. 





[40] S. Berrone, C. Canuto, M. Pintore, Variational physics informed neural networks: the role of quadratures and test functions, J. Sci. Comput. 92 (3) (2022) 100. 





[41] C.L. Wight, J. Zhao, Solving Allen-Cahn and Cahn-Hilliard equations using the adaptive physics informed neural networks, 2020, arXiv preprint arXiv:2007.04542 





[42] R. Mattey, S. Ghosh, A novel sequential method to train physics informed neural networks for Allen Cahn and Cahn Hilliard equations, Comput. Methods Appl, Mech, Engrg, 390 (2022) 114474 





[43] S. Goswami, C. Anitescu, S. Chakraborty, T. Rabczuk, Transfer learning enhanced physics informed neural network for phase-field modeling of fracture, Theor. Appl. Fract. Mech. 106 (2020) 102447. 





[44] S. Goswami, C. Anitescu, T. Rabczuk, Adaptive fourth-order phase field analysis using deep energy minimization, Theor. Appl. Fract. Mech. 107 (2020) 102527. 





[45] Y. Ghaffari Motlagh, P.K. Jimack, R. de Borst, Deep learning phase-field model for brittle fractures, Internat. J. Numer. Methods Engrg. (2022). 





[46] L. Lu, P. Jin, G. Pang, Z. Zhang, G.E. Karniadakis, Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators, Nat. Mach. Intell. 3 (3) (2021) 218–229. 





[47] Z. Li, H. Zheng, N. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, A. Anandkumar, Physics-informed neural operator for learning partial differential equations, 2021, arXiv preprint arXiv:2111.03794. 





[48] S. Goswami, M. Yin. Y. Yu. G.E. Karniadakis, A physics-informed variational DeepONet for predicting crack path in quasi-brittle materials, Comput. Methods Appl. Mech. Engrg. 391 (2022) 114587. 





[49] H. Amor, J.-J. Marigo, C. Maurini, Regularized formulation of the variational brittle fracture with unilateral contact: Numerical experiments, J. Mech Phys. Solids 57 (8) (2009) 1209–1229. 





[50] F. Freddi, G. Royer-Carfagni, Regularized variational theories of fracture: a unified approach, J. Mech. Phys. Solids 58 (8) (2010) 1154–1174. 





[51] C. Miehe, F. Welschinger, M. Hofacker, Thermodynamically consistent phase-field models of fracture: Variational principles and multi-field FE implementations, Int. J. Numer. Methods Eng. 83 (10) (2010) 1273–1311. 





[52] C. Miehe, M. Hofacker, F. Welschinger, A phase field model for rate-independent crack propagation: Robust algorithmic implementation based on operator splits, Comput. Methods Appl. Mech. Engrg. 199 (45–48) (2010) 2765–2778. 





[53] F. Vicentini, C. Zolesi, P. Carrara, C. Maurini, L. De Lorenzis, On the energy decomposition in variational phase-field models for brittle fracture under multi-axial stress states, Eng. Fract. Mech. 182 (2017) 658–688. 





[54] T. Gerasimov, L. De Lorenzis, On penalization in variational phase-field models of brittle fracture, Comput. Methods Appl. Mech. Engrg. 354 (2019) 990–1026. 





[55] S.R. Dubey, S.K. Singh, B.B. Chaudhuri, Activation functions in deep learning: A comprehensive survey and benchmark, Neurocomputing 503 (2022) 92–108. 





[56] D.P. Kingma, J. Ba, Adam: A method for stochastic optimization, 2014, arXiv preprint arXiv:1412.6980. 





[57] D.C. Liu. J. Nocedal, On the limited memory BFGS method for large scale optimization, Math, Program, 45 (1) (1989) 503–528 





[ ] ifi d d ifi i l l k h i l diff i l i i l i i ( ) 28–41. 





[59] C. Leake, D. Mortari, Deep theory of functional connections: A new method for estimating the solutions of partial differential equations, Mach. Learn. Knowl. Extr. 2 (1) (2020) 37–55. 





[60] M. Riedmiller, H. Braun, A direct adaptive method for faster backpropagation learning: The rprop algorithm, in: IEEE International Conference on Neural Networks. JEEE. 1993. pp. 586–591. 





[61] X. Glorot, Y. Bengio, Understanding the difficulty of training deep feedforward neural networks, in: Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics, JMLR Workshop and Conference Proceedings, 2010, pp. 249–256. 





[62] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, S. Chintala, PyTorch: An imperative style, high-performance deep learning library, in: H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché-Buc, E. Fox, R. Garnett (Eds.), Advances in Neural Information Processing Systems 32, Curran Associates. Inc.. 2019. pp. 8024–8035. 





[63] C. Geuzaine, J.-F. Remacle, Gmsh: A 3-D finite element mesh generator with built-in pre-and post-processing facilities, Int. J. Numer. Methods Eng. 79 (11) (2009) 1309–1331. 





[64] T. Gerasimov, U. Römer, J. Vondrejc, H. Matthies, L. De Lorenzis, Stochastic phase-field modeling of brittle fracture: computing multiple crack patterns and their probabilities, Comput. Methods Appl. Mech. Engrg. 372 (2020) 113353. 





[65] S. Zhou, X. Zhuang, H. Zhu, T. Rabczuk, Phase field modelling of crack propagation, branching and coalescence in rocks, Theor. Appl. Fract. Mech. 96 (2018) 174–192. 

