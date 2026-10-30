# A review on phase-field models of brittle fracture and a new fast hybrid formulation

Article  in  Computational Mechanics · December 2014 DOI: 10.1007/s00466-014-1109-y 

CITATIONS 168 

READS 2,725 

3 authors: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/0556dbe5a01e815692bcd3c528d4ca8ea559b209742e6ad442a1b850df63894e.jpg)


11 PUBLICATIONS   388 CITATIONS 

SEE PROFILE 

SEE PROFIL 

Laura De Lorenzis 

161 PUBLICATIONS   4,876 CITATIONS 

SEE PROFILE 

Some of the authors of this publication are also working on these related projects: 

Project 

Reproducing Sneddon's solution using fracture PhF formulations accurately is not easy View project 

ORIGINAL PAPER 

# A review on phase-field models of brittle fracture and a new fast hybrid formulation

Marreddy Ambati Tymofiy Gerasimov Laura De Lorenzis 

Received: 25 August 2014 / Accepted: 29 November 2014 / Published online: 12 December 2014 

© Springer-Verlag Berlin Heidelberg 2014 

Abstract In this contribution we address the issue of efficient finite element treatment for phase-field modeling of brittle fracture. We start by providing an overview of the existing quasi-static and dynamic phase-field fracture for mulations from the physics and the mechanics communities. Within the formulations stemming from Griffith’s theory, we focus on quasi-static models featuring a tension-compression split, which prevent cracking in compression and interpenetration of the crack faces upon closure, and on the staggered algorithmic implementation due to its proved robustness. In this paper, we establish an appropriate stopping criterion for the staggered scheme. Moreover, we propose and test the so-called hybrid formulation, which leads within a staggered implementation to an incrementally linear problem. This enables a significant reduction of computational cost— about one order of magnitude—with respect to the available (non-linear) models. The conceptual and structural similarities of the hybrid formulation to gradient-enhanced continuum damage mechanics are outlined as well. Several benchmark problems are solved, including one with own experimental verification. 

Keywords Phase-field modeling · Brittle fracture Review · Hybrid formulation · Staggered scheme · FEM 

## 1 Introduction

Phase-field modeling of brittle fracture in elastic solids dates back to the late ’1990s and, since then, has been the subject of extensive theoretical and computational investigations. In general, the phase-field approach to model systems with sharp interfaces consists in incorporating a continuous field variable– -the field order parameter—which differentiates between multiple physical phases within a given system through a smooth transition. In the context of fracture, such order parameter describes the smooth transition between the fully broken and intact material phases, thus approximating the sharp crack discontinuity, and is, therefore, referred to as the crack field. The evolution of this field as a result of the external loading conditions models the fracture process. The mathematical description consists of a coupled non-linear system of (quasi-static or dynamic) stress equilibrium equations and a gradient-type evolution equation for the crack phase-field. 

What makes the approach particularly attractive is its ability to elegantly simulate complicated fracture processes, including crack initiation, propagation, merging, and branching, in general situations and for 3D geometries, without the need for additional ad-hoc criteria. Propagating cracks are tracked automatically by the evolution of the smooth crack field on a fixed mesh. This leads to a significant advantage over the discrete fracture description, whose numerical implementation requires explicit (in the classical finite element setting [1,2]) or implicit (within extended finite element methods [3]) handling of the discontinuities. The possibility to avoid the tedious task of tracking complicated crack surfaces in 3D significantly simplifies the implementation. 

Several phase-field approaches to brittle fracture have been independently developed and investigated in the physics community [4–9] and in the mechanics community [10– 17]. Interestingly, the conceptual and technical backgrounds for deriving the constitutive and phase-field evolution equations are substantially different for the two communities. The dynamic models developed within the physics community are derived by adapting the phase transition formalism of Landau and Ginzburg [18]. In contrast, the models proposed within the mechanics community are based on the variational formulation of brittle fracture by Francfort and Marigo [19], regularized by Bourdin et al. [10], which extends the classical Griffith’s theory of fracture. The early quasi-static formulations have been extended to the dynamic case in [20–25]. In this paper, we will focus on this category of models, due to their tight relationship to Griffith’s theory which is well understood and widely applied by engineers. In our developments, we will limit ourselves to quasi-static fracture. 

As will be detailed in the following sections, all phasefield models introduce a regularization parameter, which is related to the diffusive approximation of the sharp crack. In the models from the mechanics community, this parameter has dimensions of a length and can be interpreted as the width of the regularized crack. An important feature of some of these models is that they are provably convergent (in the sense of the so-called Γ-convergence) to Griffith’s theory of brittle fracture as the length scale parameter tends to zero. Within a finite element formulation, the size of the elements must be sufficiently small to adequately resolve the length scale parameter. This typically leads to the need for very fine meshes, and thus to a significant computational cost, unless an appropriate adaptive local mesh refinement strategy is implemented. 

Algorithmically, phase-field approaches may be implemented with monolithic or with staggered schemes, where, respectively, the displacement and the crack phase-field are computed simultaneously or alternately. While monolithic schemes are more efficient, as they only need one loop of (typically Newton–Raphson) iterations, staggered implementations have proved to lead to a significantly better robustness [16] and thus will be considered in this paper. 

Within the models related to Griffith’s theory, in this paper we will in particular focus on those featuring a tensioncompression split. In absence of such split, such as in the basic formulations in [10–13] (herein referred to as isotropic models), cracking may arise also under compressive load states, thus leading to unphysical crack propagation patterns. Moreover, contact conditions at the crack faces upon closure of an existing crack are not automatically enforced. For these reasons, models incorporating a tension-compression split (here indicated as anisotropic models) have been proposed by Amor et al. [14] and Miehe et al. [15,16]. From the computational standpoint and focusing on the staggered algorithmic implementation, anisotropic models are significantly more expensive than the isotropic ones, since the balance of momentum equations become non-linear as a result of the split. 

Within the context outlined above, the purpose of this contribution is two-fold. 

First, we provide a concise overview of the quasi-static and dynamic phase-field models of fracture proposed to date in the physics and mechanics communities. This is not to be intended as a comprehensive state of the art review, but rather as an attempt to delineate the main development lines of the topic in the two communities and, in particular, to trace their intersection points and highlight their fundamental differences. 

The second goal of the paper is to address the question of computational efficiency of phase-field models. On one hand, we establish an appropriate stopping criterion for the staggered scheme. On the other hand, we propose and test what we term a hybrid formulation. This formulation formally comprises features from both the isotropic and anisotropic models. It is shown to lead to results very similar to those of the anisotropic model by Miehe et al. [15,16]. However, within a staggered implementation it leads to an incrementally linear problem, which enables a significant reduction of computational cost—about one order of magnitude—with respect to the available anisotropic models. The only seeming disadvantage of the hybrid formulation is its variational inconsistency. In order to deepen our understanding of this new model, we show how it can be derived through a nonvariational procedure, inspired by conceptual and structural similarities with gradient-enhanced continuum damage formulations. 

The paper is structured as follows. In Sect. 2 we provide a brief overview of phase-field models for brittle fracture proposed within the physics and mechanics communities. Section 3 introduces the hybrid formulation for quasistatic fracture. The similarities to gradient-enhanced damage mechanics models are outlined. From the algorithmic standpoint, we address the issue of establishing a stopping criterion for the outer loop within a staggered scheme. In Sect. 4 we present numerous benchmark examples and compare the performance of the hybrid model with that of the available isotropic and anisotropic models in terms of crack phase-field, load–displacement behavior and computational cost. For one of these examples we also performed experimental verification for the crack pattern. Section 5 closes the contribution. 

The following notations are used throughout the paper: $\Omega \subset \mathbb { R } ^ { n } , n = 2 , 3 ,$ , is an open bounded domain, representing an elastic n-dimensional body, and x denotes a point in Ω. The vectors and second-order tensors are indicated by boldface letters, like u, ε and σ for the displacement, strain and stress fields, respectively. Symbols · and : stand for a contraction (a product) and a double contraction (a double product) of two second-order tensors, respectively, so that e.g. for the strain tensor we have $\pmb { \varepsilon } \cdot \pmb { \varepsilon } = : \pmb { \varepsilon } ^ { 2 }$ and ε : $\pmb { \varepsilon } = \operatorname { t r } ( \pmb { \varepsilon } ^ { 2 } )$ . Also, Ψ indicates the elastic energy density function, which is defined as $\begin{array} { r } { \psi _ { 0 } ( \pmb { \varepsilon } ) : = \frac { 1 } { 2 } \pmb { \varepsilon } : \mathbb { C } : \pmb { \varepsilon } = \frac { 1 } { 2 } \lambda \mathrm { t r } ^ { 2 } ( \pmb { \varepsilon } ) + \mu \mathrm { t r } ( \pmb { \varepsilon } ^ { 2 } ) } \end{array}$ , with $\mathbb { C }$ as the fourth-order elasticity tensor, and $\lambda$ and $\mu$ as the Lamé constants. 

## 2 Phase-field models for brittle fracture at a glance

In this section, we provide an overview of the phase-field approaches to fracture that have been devised, investigated and favored in the physics and mechanics communities. The models are presented in chronological order. In general, we tend to keep the original symbols and notations of the various authors, however in some cases deviations are implemented for unification purposes. 

## 2.1 In physics: models based on Landau–Ginzburg phase transition

In the physics community, starting from 2000, there have been several attempts to adapt the generalphase-fieldformalism to fracture mechanics, particularly to dynamic fracture problems. 

## • Aranson-Kalatsky-Vinokur model [4], 2000.

This model is seemingly one of the first phase-field like descriptions of crack propagation in brittle materials, focusing on Mode I fracture in two dimensions. 

In this model, the displacement field u obeys the standard elastodynamic equation with a damping term, $\rho \ddot { \pmb u } =$ $\eta \Delta \dot { \pmb { u } } + \mathrm { d i v } \pmb { \sigma }$ , where $\rho$ is the constant mass density, $\Delta$ and div are the Laplace and the divergence operators, respectively, a superposed dot stands for the partial differentiation with respect to time, and $\eta > 0$ is a viscous damping parameter. The stress-strain relation differs from the one used in the isotropic linear elasticity ${ \pmb { \sigma } } = \mathbb { C }$ : ε via dependencies on an order parameter $\phi ,$ which distinguishes between broken and unbroken phases of a solid: it takes the value $\phi = 1$ in the solid, vanishes inside the crack, $\phi = 0$ , and varies smoothly at the crack surfaces on a scale that is large in comparison to the atomic spacing, to justify the continuum description. The stress is given by 

$$
\boldsymbol {\sigma} (\boldsymbol {u}, \phi) := \phi \mathbb {C}: \boldsymbol {\varepsilon} + \chi \dot {\phi} \boldsymbol {I},\tag{1}
$$

with I as the second-order identity tensor and $\chi > 0$ as an additional material parameter associated with the hydrostatic stress due to the creation of new defects. 

The evolution of $\phi$ is assumed to be governed by dissipative dynamics $\begin{array} { r } { \dot { \phi } = - \frac { \delta \mathcal { F } } { \delta \phi } } \end{array}$ , where $\mathcal { F }$ is a specific ’free-energy’ functional and $\delta / \delta \phi$ stands for the variational differentiation with respect to $\phi .$ . The simplest form for 

$$
\mathcal {F} \sim \int_ {\Omega} \left[ P (\phi) + D _ {\phi} | \nabla \phi | ^ {2} \right] \mathrm{d} \boldsymbol {x},
$$

where $P$ is a polynomial function and $D _ { \phi }$ is a positive constant, is adapted following Landau’s ideas on phase transition [18]. The resulting (nonlinear) evolution equation reads 

$$
\begin{array}{c} \dot {\phi} = D _ {\phi} \Delta \phi - \phi (1 - \phi) \Big [ \alpha \Big (1 + (\operatorname{tr} (\boldsymbol {\varepsilon}) - \beta) \phi \Big) \\ - \gamma \dot {\boldsymbol {u}} \cdot \nabla \phi \Big ], \end{array}\tag{2}
$$

where $\alpha , \beta$ and $\gamma$ are the model parameters, including the material-related ones, see [4] for details. 

The phenomenological phase-field model Eqs. (1)–(2) was shown to capture essential behavioral features like crack initiation, propagation, branching, dynamic fracture instability, sound emission and fragmentation. However, when applied to Mode I crack propagation in a rectangular strip of finite width, some discrepancies between the numerical results and the predictions of the classical fracture theory were observed [4]. 

## • Karma-Kessler-Levine model [5], 2001.

In 2001, Karma and co-workers proposed a phase-field approach for fracture that emanates from the original phasefield models for solidification. The model was restricted to Mode III fracture (antiplane shear) to make the description simpler since only the out-of-plane displacement component exists in a two dimensional setting in this case. We consider here its three-dimensional generalization by Hakim and Karma [6], 2009, to make it more easily comparable with the model of Aranson et al. [4], as well as with the models in Sect. 2.2. 

Herein, in contrast to [4], the governing system of equations, including the momentum balance equation, the stressstrain relation and the crack phase-field evolution equation, follows variationally from a free energy functional [6]: 

$$
\begin{array}{c} F (\boldsymbol {u}, \phi) = \int_ {\Omega} \Big [ g (\phi) \Big (\Psi_ {0} (\boldsymbol {\varepsilon} (\boldsymbol {u})) - \Psi_ {c} \Big) \\ + V (\phi) + \frac {1}{2} D _ {\phi} | \nabla \phi | ^ {2} \Big ] \mathrm{d} \boldsymbol {x}, \end{array}\tag{3}
$$

where $\phi$ is the order parameter (defined analogously to Aranson et al. [4]), g is the function that couples φ with the elastic field and satisfies $g ( \phi ) > 0$ for $0 < \phi \leq 1$ , and $V ( \phi ) =$ $\phi ^ { 2 } ( 1 - \phi ^ { 2 } ) / 4$ is the so-called Ginzburg–Landau double-well potential. Furthermore, $\psi _ { c }$ stands for a critical strain energy to be used as a threshold for crack initiation and, finally, $D _ { \phi }$ is a positive constant [identical to the corresponding one in Eq. (2)]. An additional specific property $g ( \phi ) = \phi ^ { 2 + \alpha }$ as $\phi  0$ , with $\alpha > 0$ [(a dimensionless parameter not to be confused with α entering Eq. (2)], is imposed on g in order to ‘obtain full stress relaxation in a completely broken solid in the limit of large system sizes’. Also, V is specifically chosen to favor the preferred states $\phi = 0$ and $\phi = 1$ of the system and to create an energy barrier between them, see Hakim and Karma [6] and Spatschek et al. [7] for details. 

Using the variational derivative of F with respect to u, the equilibrium equation $\rho \ddot { \pmb { u } } = \mathrm { d i v } \pmb { \sigma }$ is obtained, where the stress takes the form 

$$
\sigma (\boldsymbol {u}, \phi) := g (\phi) \frac {\partial \Psi_ {0} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} = g (\phi) \mathbb {C}: \boldsymbol {\varepsilon}.\tag{4}
$$

The proposed relaxation law $\begin{array} { r } { \tau \dot { \phi } = - \frac { \delta F ( \pmb { u } , \phi ) } { \delta \phi } } \end{array}$ , where $\tau \geq 0$ is a kinetic modulus, yields a nonlinear diffusion equation that governs the evolution of $\phi$ : 

$$
\tau \dot {\phi} = D _ {\phi} \Delta \phi - V ^ {\prime} (\phi) - g ^ {\prime} (\phi) \Bigl (\Psi_ {0} (\pmb {\varepsilon}) - \Psi_ {c} \Bigr).\tag{5}
$$

• Henry and Levine model [9], 2004. 

This model is an extension of the original Karma et al. [5] formulation to the two dimensional plane strain situation in order to investigate crack growth under Mode I and II conditions. A modification of the elastic energy part of the free energy functional is also suggested to prevent the compressed regions of the body from cracking, that is, 

$$
\begin{array}{c} F (\boldsymbol {u}, \phi) = \int_ {\Omega} \Big [ g (\phi) \Big (\widetilde {\Psi} (\boldsymbol {\varepsilon} (\boldsymbol {u})) - \Psi_ {c} \Big) \\ + V (\phi) + \frac {1}{2} D _ {\phi} | \nabla \phi | ^ {2} \Big ] \mathrm{d} \boldsymbol {x}. \end{array}\tag{6}
$$

Herein, $\widetilde { \psi }$ coincides with the standard elastic energy den-<sub>sity when the material undergoes positive volume change</sub> and contains a breaking symmetry term (the contribution of shear) in case of negative volume change, as follows 

$$
\widetilde {\Psi} (\pmb {\varepsilon}) := \left\{ \begin{array}{l l} \Psi_ {0} (\pmb {\varepsilon}) & \text {if} \quad \operatorname{tr} (\pmb {\varepsilon}) > 0, \\ \Psi_ {0} (\pmb {\varepsilon}) - \frac {1}{2} \alpha K \operatorname{tr} ^ {2} (\pmb {\varepsilon}) & \text {if} \quad \operatorname{tr} (\pmb {\varepsilon}) <   0. \end{array} \right.\tag{7}
$$

where $K : = K _ { n } | _ { n = 2 } .$ , with $K _ { n } = \lambda + \frac { 2 \mu } { n }$ as the n-dimensional bulk modulus, and α is an arbitrary coefficient chosen to be larger than 1. Finally, the coupling function g iss chosen here as $g ( \phi ) = ( 4 - 3 \phi ) \phi ^ { 3 }$ 

The resulting stress–strain relation and the evolution equation for φ in this case modify to 

$$
\pmb {\sigma} (\pmb {u}, \phi) := g (\phi) \frac {\partial \widetilde {\Psi} (\pmb {\varepsilon})}{\partial \pmb {\varepsilon}},\tag{8}
$$

and 

$$
\tau \dot {\phi} = D _ {\phi} \Delta \phi - V ^ {\prime} (\phi) - g ^ {\prime} (\phi) \Bigl (\widetilde {\Psi} (\pmb {\varepsilon}) - \Psi_ {c} \Bigr),\tag{9}
$$

respectively. 

In [9], the results of two dimensional simulations for model Eqs. (8)–(9) were shown to agree well with experimentally observed fracture patterns including crack branching and oscillations. 

## 2.2 In mechanics: models based on Griffith’s theory

Other phase-field models for quasi-static brittle fracture have been developed independently in the mechanics community and are by now well accepted therein. They originate from the variational formulation of brittle fracture by Francfort and Marigo [19], 1998 and from the related regularizedformulation of Bourdin et al. [10], 2000. 

In [19], the entire (quasi-static) process of crack initiation, propagation and branching is governed by a minimization problem of the energy functional 

$$
E (\boldsymbol {u}, \Gamma) = \int_ {\Omega} \Psi_ {0} (\boldsymbol {\varepsilon} (\boldsymbol {u})) \mathrm{d} \boldsymbol {x} + G _ {c} \int_ {\Gamma} \mathrm{d} s,\tag{10}
$$

with the elastic energy density function $\psi _ { 0 }$ and the material fracture toughness $G _ { c }$ yielding an admissible crack set $T \subset \varOmega$ and a displacement field $u : \varOmega \to \mathbb { R } ^ { n }$ , which is discontinuous across Γ. The shortcomings of the classical Griffith theory of brittle fracture are proven to be overcome by formulation Eq. (10), see [19] and also [11] for further details and a comprehensive overview. 

To enable an efficient numerical treatment of Eq. (10), its regularized formulation was devised by Bourdin et al. [10] in 2000, reading as 

$$
\begin{array}{l} E _ {\epsilon} (\boldsymbol {u}, s) = \int_ {\Omega} (s ^ {2} + \eta) \Psi_ {0} (\boldsymbol {\varepsilon} (\boldsymbol {u}))   \mathrm{d} \boldsymbol {x} \\ \qquad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \epsilon} (1 - s) ^ {2} + \epsilon | \nabla s | ^ {2}\right)   \mathrm{d} \boldsymbol {x}, \end{array}\tag{11}
$$

where s is a field variable, which is introduced to indicate the crack and therefore called the crackfieldparameter. Its value varies smoothly from 1 (undamaged material) to 0 (totally broken). Furthermore, the parameter $\epsilon > 0$ has the dimension of a length and controls the width of the transition zone of $s .$ . The small dimensionless parameter η models an artificial residual stiffness of a totally broken phase $( s ~ = ~ 0 )$ and is essentially needed to prevent numerical difficulties. With $\epsilon  0$ , the formulation Eq. (11) approximates Eq. (10) in the sense of Γ-convergence, thus establishing the link between regularized and free-discontinuity fracture energies. This implies that the zero set of the crack field s indeed recovers the crack set Γ. To solve for $( { \pmb u } , s )$ , the functional $E _ { \epsilon }$ is minimized directly, using, in the numerical implementations, the so-called alternate minimization and back-tracking algorithms, see Bourdin et al. [10,11]. 

• Kuhn and Müller model [12], 2008. 

Kuhn and Müller, using the framework of Gurtin [26] on the thermodynamics of order parameter based models, reformulated the minimization problem Eq. (11) as the system of the stress equilibrium equation −div $\pmb { \sigma } ( \pmb { u } , s ) = 0$ , where 

$$
\pmb {\sigma} (\pmb {u}, s) := (s ^ {2} + \eta) \frac {\partial \Psi_ {0} (\pmb {\varepsilon})}{\partial \pmb {\varepsilon}} = (s ^ {2} + \eta) \mathbb {C}: \pmb {\varepsilon},\tag{12}
$$

and a Ginzburg–Landau type evolution equation for s: 

$$
\dot {s} = - M \left[ 2 s \Psi_ {0} (\pmb {\varepsilon}) - G _ {c} \left(2 \epsilon \Delta s + \frac {1 - s}{2 \epsilon}\right) \right].\tag{13}
$$

The latter was also complemented by the crack evolution irreversibility constraint. The so-called mobility parameter $M \geq 0$ is responsible for the dissipation upon stable crack growth. The limit case $M  \infty$ approximates quasi-static crack propagation, simply yielding 

$$
0 = 2 s \Psi_ {0} (\boldsymbol {\varepsilon}) - G _ {c} \left(2 \epsilon \Delta s + \frac {1 - s}{2 \epsilon}\right),\tag{14}
$$

whereas for finite values of M the model can be regarded as a viscous approximation of the quasi-static case. We refer to [12,13] for further details. 

The evolution Eq. (13) resembles the related Eq. (5) of Karma et al. [6] and Eq. (9) of Henry and Levine [9], as the similar derivation formalism was used in this case as well. 

Remark 1 Note that Eqs. (12) and (14) corresponding to a quasi-static case can straightforwardly be derived via variational principle, that is, they are the Euler-Lagrange equations of the functional $E _ { \epsilon }$ in Eq. (11). 

It is also worth noting that Kuhn and Müller were seemingly the first in the engineering community to name the formulation Eq. (11) and the resulting system Eqs. (12)–(13) a phase-field model for fracture, by interpreting the crack parameter s that enters Eq. (11) as a phase-field variable. In the remainder of this paper, the term ’phase-field model’ will be used with respect to Eqs. (11), (12)–(13) and all related extensions. 

## • Amor, Marigo, Maurini model [14], 2009.

The phase-field formulation Eq. (11) does not distinguish between fracture behavior in tension and compression. Already in [10] examples ofunrealistic crack patterns in compression were reported (see also Sect. 4). To avoid such situations, and, additionally, to prevent the interpenetration of the crack faces under compression, a modified regularized formulation of Eq. (10) was proposed in [14] using an additive decomposition of the elastic energy density $\psi _ { 0 }$ into volumetric and deviatoric contributions. Thus, with $\psi _ { 0 } = \psi _ { 0 } ^ { + } + \psi _ { 0 } ^ { - }$ where 

$$
\left. \begin{array}{l} \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon}) := \frac {1}{2} K _ {n} \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \rangle_ {+} ^ {2} + \mu (\boldsymbol {\varepsilon} ^ {\mathrm{dev}}: \boldsymbol {\varepsilon} ^ {\mathrm{dev}}) \\ \Psi_ {0} ^ {-} (\boldsymbol {\varepsilon}) := \frac {1}{2} K _ {n} \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \rangle_ {-} ^ {2} \end{array} \right\}\tag{15}
$$

and, in turn, $\begin{array} { r } { K _ { n } = \lambda + \frac { 2 \mu } { n } , \langle a \rangle _ { \pm } : = \frac { 1 } { 2 } ( a \pm | a | ) } \end{array}$ and $\pmb { \varepsilon } ^ { \mathrm { d e v } } : =$ ${ \pmb \varepsilon } - \frac { 1 } { 3 } \mathrm { t r } ( { \pmb \varepsilon } ) I$ , the energy functional Eq. (11) was replaced by 

$$
\begin{array}{l} E _ {\epsilon} (\boldsymbol {u}, s) = \int_ {\Omega} \left((s ^ {2} + \eta) \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon}) + \Psi_ {0} ^ {-} (\boldsymbol {\varepsilon})\right) \mathrm{d} \boldsymbol {x} \\ \qquad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \epsilon} (1 - s) ^ {2} + \epsilon | \nabla s | ^ {2}\right) \mathrm{d} \boldsymbol {x}. \end{array}\tag{16}
$$

Similarly to the model of Henry and Levine [9], yet in contrast to Eq. (11), the degradation of only the positive energy part is allowed herein, whereas the negative part remains undegraded. As mentioned in [14], the results on Γ-convergence for the functional $E _ { \epsilon }$ in Eq. (16) are not available. That is, it is not clear what kind of functional (and hence what kind of ’physical’ process) is to be recovered when $\epsilon  0$ in this case. The formulation Eq. (16), however, has been shown to provide adequate simulation results, see [14] and the numerical examples in Sect. 4. In [14], the numerical solution $( { \pmb u } , s )$ of the minimization problem for $E _ { \epsilon }$ was obtained by means of the alternate minimization algorithm of Bourdin et al. [10,11]. 

Remark 2 A good physical insight into the outcome of the split of $\psi _ { 0 }$ and the particular form of coupling between s and u implemented in Eq. (16) can be done by reviewing the resulting stress-strain relation 

$$
\begin{array}{c} \boldsymbol {\sigma} (\boldsymbol {u}, s) := (s ^ {2} + \eta) \frac {\partial \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} + \frac {\partial \Psi_ {0} ^ {-} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} \\ = (s ^ {2} + \eta) \left[ K _ {n} \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \rangle_ {+} \boldsymbol {I} + 2 \mu \boldsymbol {\varepsilon} ^ {\mathrm{dev}} \right] \\ + K _ {n} \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \rangle_ {-} \boldsymbol {I}, \end{array}\tag{17}
$$

and the evolution equation of the crack phase-field 

$$
\dot {s} = - M \left[ 2 s \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon}) - G _ {c} \left(2 \epsilon \Delta s + \frac {1 - s}{2 \epsilon}\right) \right],\tag{18}
$$

It can first be observed that by coupling s with $\psi _ { 0 } ^ { + }$ in $E _ { \epsilon }$ the evolution of s in Eq. (18) appears to be driven only by the dilatational part of the volumetric strain, thus providing cracking in tension. On the other hand, the absence of $\psi _ { 0 } ^ { - }$ in Eq. (18) prevents crack evolution in the (highly) compressed parts of a solid, in which ${ \psi } _ { 0 } ^ { - }$ is expected to dominate $\psi _ { 0 } ^ { + }$ Finally, since the $\psi _ { 0 } ^ { - }$ <sup>−</sup> part remains undegraded in $E _ { \epsilon } ,$ , resulting in the presence of $\partial \pmb { \psi } _ { 0 } ^ { - } / \partial \pmb { \varepsilon }$ in the relation Eq. (17), it can be expected that in case of crack closure the crack faces interpenetration is also prevented. 

The above remark will be recalled in Sect. 3 when establishing and motivating our hybrid phase-field formulation. 

• Miehe et al. model [15,16], 2010. 

Miehe and co-workers presented a thermodynamically consistent phase-field model of brittle fracture [15,16]. The model derivation is based upon continuum mechanics and thermodynamic arguments and, to some extent, may be viewed as an alternative to the frameworks of Francfort-Marigo [19] and Bourdin et al. [10,11]. 

The proposed formulation contains the auxiliary variable $d \in [ 0 , 1 ]$ , termed as the regularized crack phase-field, such that $d = 0$ and $d = 1$ correspond to the unbroken and fully broken states, respectively. Also, in this case a length scale parameter  is introduced to account for the thickness of a transition zone between the two states. The assumed additive decomposition of the elastic energy $\psi _ { 0 } = \psi _ { 0 } ^ { + } + \psi _ { 0 } ^ { - }$ uses in this case the spectral decomposition of the strain tensor $\begin{array} { r } { \pmb { \varepsilon } = \sum _ { I = 1 } ^ { 3 } \langle \varepsilon _ { I } \rangle \pmb { n } _ { I } \otimes \pmb { n } _ { I } } \end{array}$ , where $\{ \varepsilon _ { I } \} _ { I = 1 } ^ { 3 }$ and $\{ { \pmb n } _ { I } \} _ { I = 1 } ^ { 3 }$ are the principal strains and principal strain directions, respectively. This yields $\begin{array} { r } { \pm \ : = \ \sum _ { I = 1 } ^ { 3 } \langle \varepsilon _ { I } \rangle _ { \pm } \pmb { n } _ { I } \otimes \pmb { n } _ { I } } \end{array}$ and, eventually, 

$$
\psi_ {0} ^ {\pm} (\pmb {\varepsilon}) := \frac {1}{2} \lambda \langle \mathrm{tr} (\pmb {\varepsilon}) \rangle_ {\pm} ^ {2} + \mu \mathrm{tr} (\pmb {\varepsilon} _ {\pm} ^ {2}).\tag{19}
$$

The governing system of equations is the system of the balance equation −div $\pmb { \sigma } ( \pmb { u } , d ) = 0$ , where 

$$
\boldsymbol {\sigma} (\boldsymbol {u}, d) := \left[ (1 - d) ^ {2} + k \right] \frac {\partial \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} + \frac {\partial \Psi_ {0} ^ {-} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}}\tag{20}
$$

and the evolution equation 

$$
\eta \dot {d} = 2 (1 - d) \Psi_ {0} ^ {+} (\pmb {\varepsilon}) + \frac {G _ {c}}{\ell} \left(d - \ell^ {2} \Delta d\right).\tag{21}
$$

Also here k is the small artificial residual stiffness of the totally broken phase and $\eta \geq 0$ is the viscosity parameter [not to be confused with η entering Eq. (11), Eqs. (12) and (16), (17)]. 

The structure of Eqs. (20)–(21) resembles Eqs. (17)–(18) by Amor et al. Indeed, by setting $d : = 1 - s , \ell : = 2 \epsilon$ and $\begin{array} { r } { \eta : = \frac { 1 } { M } } \end{array}$ , the identity of the corresponding formulations is recovered. Moreover, the authors’ intent to split Ψ<sub>0</sub> and then to enable degradation of only the tensile energy $\psi _ { 0 } ^ { + }$ to avoid cracking in compression and, in particular, crack clo sure is similar to that of Henry and Levine [9] and Amor et al. [14]. As noticed e.g. in [22], the difference between decompositions Eqs. (15) and (19) becomes evident in a situation when e.g. all three principal strains are negative. In this case, according to Eq. (15) the deviatoric strain energy will be still degraded and the related phase-field model will produce cracking in the corresponding regions, as can be observed e.g. in Fig. 12. It is also worth noticing that the split Eq. (19) results in a strongly non-linear stress-strain relation Eq. (20), what typically requires a higher computational effort than the corresponding case Eq. (17) of Amor et al. In general, numerical results in either case are qualitatively and quantitatively rather similar, see Sect. 4. 

The key novelty of Miehe et al.’s model, which enhances the ’preceding’ phase-field formulations and overcomes some of their inherent implementation difficulties, is the following. Noticing that the ’load term’ $\psi _ { 0 } ^ { + }$ entering Eq. (21) determines the ’amount’ of $d ,$ the authors introduce the history-field variable of the maximum positive reference energy 

$$
\mathcal {H} (\boldsymbol {x}, t) := \max _ {\tau \in [ 0, t ]} \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon} (\boldsymbol {x}, \tau)),
$$

obtained in a loading process. Replacing $\psi _ { 0 } ^ { + }$ in Eq. (21) by , they end up with the evolution equation 

$$
\eta \dot {d} = 2 (1 - d) \mathcal {H} + \frac {G _ {c}}{\ell} \left(d - \ell^ {2} \Delta d\right),\tag{22}
$$

which is now to be coupled with Eq. (20). The introduction of , in the first place, naturally handles the irreversibility of the crack phase-field evolution in a general, possibly cyclic, loading/unloading scenario. Moreover, it enables an elegant algorithmic decoupling of the (new) governing system Eqs. (20)–(22) and the application of a staggered scheme for computing $( { \pmb u } , d )$ . This scheme is simple and extremely robust in comparison with the monolithic scheme, where u and d are simultaneously solved for, making it a very appealing ingredient of the proposed model. 

• Borden et al. higher-order model [17], 2014. 

A higher-order phase-field model formulation was recently presented by Borden et al. [17] to gain more regular and, hence, faster converging solutions of the variational problem of brittle fracture. 

Adopting Bourdin’s formalism along with the notion of the crack surface densityfunction of Miehe et al., the devised energy functional resembles Eq. (16) in the elastic energy part, yet the corresponding surface energy integral involves higher-order derivatives of the crack phase-field, namely, 

$$
\begin{array}{l} E _ {\epsilon} (\boldsymbol {u}, s) = \int_ {\Omega} \left((s ^ {2} + \eta) \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon}) + \Psi_ {0} ^ {-} (\boldsymbol {\varepsilon})\right) \mathrm{d} \boldsymbol {x} \\ \qquad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \epsilon} (1 - s) ^ {2} + \frac {1}{2} \epsilon | \nabla s | ^ {2} + \frac {1}{4} \epsilon^ {3} (\Delta s) ^ {2}\right) \mathrm{d} \boldsymbol {x}. \end{array}\tag{23}
$$

Herein, $\psi _ { 0 } ^ { \pm }$ are assumed to be given either by Eqs. (15) or (19). The resulting evolution equation for s is now the fourthorder partial differential equation: 

$$
\dot {s} = - M \left[ 2 s \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon}) - G _ {c} \left(- \frac {\epsilon^ {3}}{2} \Delta^ {2} s + \epsilon \Delta s + \frac {1 - s}{2 \epsilon}\right) \right].\tag{24}
$$

In the above, we intentionally preserved the structure of the corresponding second-order Eq. (18), in order to evidence the related similarities and extensions. 

For resolving the higher-order model, the isogeometric analysis framework was employed in [17]. Finally, it is worth noting that Γ-convergence results for the related functional $E _ { \epsilon }$ have not yet been derived. 

• Dynamic models. 

The quasi-static formulations listed above have all been extended by the corresponding authors to the dynamic setting: see e.g. Larsen et al. [20], 2010, Bourdin et al. [21], 2011, Borden et al. [22], 2012, Hofacker and Miehe [23,24], 2012, 2013, Schlüter et al. [25], 2014. 

## 2.3 A brief comment on the models from physics

Both the Karma-Kessler-Levine [5,6] and the Henry-Levine [9] models preserve a variational structure and therefore suggest a connection to the regularized variational description of fracture by Bourdin et al. [10] and the formulation of Amor et al. [14], respectively. These models, however, are unrelated to Griffith’s theory in the sense that the $G _ { c }$ quantity does not enter in any way the corresponding formulations. Furthermore, the use of a double-well potential instead of the single-well ’standard’ one in the energy functional makes it rather difficult to interpret the Γ-convergence results, see Bourdin et al. [21] and the reference therein for a brief discussion. On the other hand, in these models, attention was paid to the appropriate choice of the degradation (coupling) function g in order to ensure ’full stress relaxation in a completely broken solid’, as discussed in [5]. Finally, since the physics models are formulated directly in a dynamic setting, it is difficult to judge the computational results obtained— the comparisons with the benchmark (quasi-static) problems of engineering interest are seemingly not available. 

## 3 Hybrid formulation, motivating analogies and algorithmic aspects

In this section, we introduce a so-called hybrid formulation for quasi-static brittle fracture. We outline the structural similarities of this formulation to gradient-enhanced damage mechanics models, and present a non-variational derivation. Finally, although this is not strictly related to the hybrid formulation, we address the algorithmic issue of establishing a suitable stopping criterion for a staggered iterative scheme. 

## 3.1 Hybrid formulation

Based on the background in Sect. 2, and favoring, in particular, the quasi-static phase-field models which stem from the regularized variational formulation of Bourdin et al. [10], we may conclude that two formulations can be treated as ’basic ones. These are 

• Isotropic formulation 

$$
\left\{ \begin{array}{l} \boldsymbol {\sigma} (\boldsymbol {u}, d) := (1 - d) ^ {2} \frac {\partial \Psi_ {0} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}}, \\ - \ell^ {2} \Delta d + d = \frac {2 \ell}{G _ {c}} (1 - d) \mathcal {H}, \end{array} \right.\tag{25}
$$

where $\begin{array} { r } { \mathcal { H } : = \operatorname* { m a x } _ { \tau \in [ 0 , t ] } \psi _ { 0 } ( \pmb { \varepsilon } ( \pmb { x } , \tau ) ) } \end{array}$ , and 

• Anisotropic formulation 

$$
\left\{ \begin{array}{l} \boldsymbol {\sigma} (\boldsymbol {u}, d) := (1 - d) ^ {2} \frac {\partial \Psi_ {0} ^ {+} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} + \frac {\partial \Psi_ {0} ^ {-} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}}, \\ - \ell^ {2} \Delta d + d = \frac {2 \ell}{G _ {c}} (1 - d) \mathcal {H} ^ {+}, \end{array} \right.\tag{26}
$$

where $\begin{array} { r } { \mathcal { H } ^ { + } : = \operatorname* { m a x } _ { \tau \in [ 0 , t ] } \varPsi _ { 0 } ^ { + } ( \pmb { \varepsilon } ( \pmb { x } , \tau ) ) } \end{array}$ 

Herein, we have adopted the phase-field notations of Miehe et al. [15,16] as for d and . This is done in order to unify the formulations above with the gradient-enhanced damage model equations to be recalled in Sect. 3.2. We also use the original terminology from [15,16] as for the terms isotropic and anisotropic, which, in the context of fracture phase-field modeling, specifically indicate the way the elastic energy density function is degraded, and which are not related to (should not be confused with) the conventional notions of isotropy and anisotropy from continuum mechanics. Finally, both the residual stiffness and the viscous terms in the corresponding equations are neglected, and it assumed that either of the splits for Ψ presented in Sect. 2.2 is applicable. 

The practical advantage of the isotropic model over the anisotropic is that, within a staggered approach, Eq. (25a) is linear, whereas Eq. (26a) is not. Yet, the use of this model is restricted to very simple scenarios, since the model allows for cracking in compression and interpenetration of the crack faces, therefore it may yield physically unrealistic crack evolution patterns. The anisotropic formulation, where only the tensile energy is degraded and drives the evolution of the crack field, naturally overcomes such drawback (see Remark 2). However, even within a staggered approach, Eq. (26) is non-linear due to the decomposition of the strain tensor, which makes the numerical treatment much more expensive. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/6099a8815e54d00b4d20e614dea39e2b03ef53ba26865b39f3ec57e6c8b1398d.jpg)



Fig. 1 a Specimen geometry and b Loading history


In this paper, we propose and test what we call an 

• Hybrid (isotropic–anisotropic) formulation 

$$
\left\{ \begin{array}{l} \boldsymbol {\sigma} (\boldsymbol {u}, d) := (1 - d) ^ {2} \frac {\partial \Psi_ {0} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}}, \\ - \ell^ {2} \Delta d + d = \frac {2 \ell}{G _ {c}} (1 - d) \mathcal {H} ^ {+}, \\ \forall   \boldsymbol {x}:   \Psi_ {0} ^ {+} <   \Psi_ {0} ^ {-} \Rightarrow d := 0. \end{array} \right.\tag{27}
$$

The reason for this terminology is that the formulation formally contains features of the previous two. 

The general idea in devising the hybrid model is to retain a linear momentum balance equation within a staggered scheme, in order to keep a computational cost comparable to that of the isotropic model. This results in retaining Eq. (27a) from the isotropic model. However, we still want the evolution of d to be driven merely by the tensile elastic energy $\psi _ { 0 } ^ { + }$ to avoid cracking in the compressed regions. This motivates keeping Eq. (27b). Furthermore, we want to retain the ability to prevent crack faces interpenetration, which holds for the anisotropic models (see Remark 2) but is violated herein due to the ’postulated’ relation Eq. (27a). To circumvent this issue, we introduce the constraint Eq. (27c) complementing the first two governing equations. 

The role of the constraint Eq. (27c) is illustrated in Figs. 1 and 2. In this simple example, a cyclic displacement loading is imposed on a pre-cracked specimen, Fig. 1, and the loaddisplacement curves computed by Eq. (27) with and without the enforcement of condition Eq. (27c) are compared, Fig. 2. The results are identical at all loading stages except for stage C, when the system with a closed crack undergoes compression, and the following stage D. More precisely, the unconstrained model yields a secant elastic response at the C-stage (an effect of crack faces interpenetration). In contrast, the constrained model guarantees a residual resistance in compression and therefore simulates the behavior of an undamaged elastic system at the corresponding stage. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/bba39c7614616c4308734e614a3bb70881f3fa206acf0470ecd5caf39f778ce3.jpg)



Fig. 2 Load–displacement curve: comparison of the constrained and unconstrained results at the loading stages in Fig. 1


In Sect. 4 we bring numerical evidence that the hybrid model is capable of producing physically adequate results, which are qualitatively and quantitatively similar to those of the anisotropic model. On the other hand, by recovering the linearity of the momentum equations (within a staggered scheme), the hybrid model leads to a computational effort that is comparable to that of the isotropic model, and up to 90 % (i.e. one order of magnitude) lower than that of the anisotropic model. In Sect. 3.3 we address the issue of the variational inconsistency of the hybrid model. Indeed, in contrast to Eqs. (25) and (26), the system Eq. (27) does not preserve a variational structure, since with the postulated assumption $\begin{array} { r } { E _ { \mathrm { e l a s t i c } } : = \int _ { \Omega } ( 1 - d ) ^ { 2 } \psi _ { 0 } ( \pmb \varepsilon ) } \end{array}$ dx, which would result in relation Eq. (27a), one is not able to obtain the corresponding evolution Eq. (27b). We propose an alternative— non-variational—approach to derive Eq. (27), employing the similarity between Eq. (27) and the gradient-enhanced formulation of continuum damage mechanics. 

## 3.2 Gradient-enhanced formulation of a damage model

From the material modeling standpoint, phase-field fracture models are conceptually similar to models of continuum damage mechanics (CDM). Restricting ourselves to isotropic damage models, in which one or several scalar damage parameters are responsible for the degradation of material stiffness, and focusing in particular on the so-called gradient-enhanced damage formulation by Peerlings et al. [27], it becomes feasible to trace also the structural similarities between phase-field and damage models. 

The fundamentals of the CDM theory including an extensive overview can be found in the monographs of Kachanov [28] and Murakami [29]. Herein, we only briefly recall the cornerstones of CDM and the corresponding gradient formulation that will enable the derivation of Eq. (27). 

In isotropic damage models, the loss ofstiffness associated to mechanical degradation of the material is represented by a scalar parameter $D ,$ , according to the stress-strain relation $\pmb { \sigma } ( \pmb { u } , D ) : = ( 1 - D ) \mathbb { C } : \pmb { \varepsilon }$ , where D ranges between 0 (virgin material, with elastic stiffness) and 1 (completely damaged material, with no stiffness). It is furthermore assumed that D depends on a state variable Y, which in turn depends on the strain, $Y = Y ( \pmb \varepsilon )$ 

In local damage models, Y coincides with the so-called equivalent strain ${ \widetilde { \varepsilon } } .$ Various specific definitions of $\widetilde { \varepsilon } ( \pmb \varepsilon )$ to  account appropriately for those features of the strain field which are assumed to be responsible for damage inception and propagation have been proposed in the literature, and a few of them are summarized as follows: 

$$
\widetilde {\varepsilon} := \left\{ \begin{array}{l l} \sqrt {2 \Psi_ {0} (\boldsymbol {\varepsilon})}, & \text {   Simo   and   Ju   [30] }, \\ \sqrt {\sum_ {I = 1} ^ {3} \langle \varepsilon_ {I} \rangle_ {+} ^ {2}}, & \text {   Mazars   [31] }, \\ \frac {\kappa - 1}{2 \kappa (1 - 2 \nu)} I _ {1} (\boldsymbol {\varepsilon}) \\ + \frac {1}{2 \kappa} \left[ \left(\frac {\kappa - 1}{1 - 2 \nu} I _ {1} (\boldsymbol {\varepsilon})\right) ^ {2} \right. \\ + \left. \frac {1 2 \kappa}{(1 + \nu) ^ {2}} J _ {2} (\boldsymbol {\varepsilon}) \right] ^ {\frac {1}{2}}, & \text {   de   Vree   et   al.   [32] }, \end{array} \right.\tag{28}
$$

where $\langle \varepsilon _ { I } \rangle _ { + } , I = 1 , 2 , 3$ stand for the positive part of the principal strains, $I _ { 1 } ( \pmb \varepsilon ) : = \operatorname { t r } ( \pmb \varepsilon )$ and $J _ { 2 } ( \pmb \varepsilon ) : = \operatorname { t r } ( \pmb \varepsilon ^ { 2 } ) -$ $\scriptstyle { \dot { \frac { 1 } { 3 } } } \operatorname { t r } ^ { 2 } ( { \dot { \pmb { \varepsilon } } } )$ are the first invariant of the strain tensor and the second invariant of the deviatoric strain tensor, respectively, and κ is the parameter that controls the sensitivity to tensile and compressive strains. The last expression in Eq. (28) is usually referred to as the modified von Mises definition. 

Due to the fact that the damage parameter depends only on the strain state at the point under consideration, the local models are known to suffer from spurious mesh sensitivity, yielding physically unrealistic results. Moreover, they are unable to interpret size effects which are often observed experimentally. 

To overcome these drawbacks, various regularization techniques have been suggested, including non-local damage models [33–35]. Herein, D is made to depend on the strain state in a neighborhood (associated to a characteristic length) of the point under consideration, e.g. on the nonlocal equivalent strain $\overline { { \varepsilon } } ,$ defined (in the simplest case) as a weighted spatial averaging of the equivalent strain, resulting in the formulation 

$$
\left\{ \begin{array}{l} \boldsymbol {\sigma} (\boldsymbol {u}, D) := (1 - D (\bar {\varepsilon})) \mathbb {C}: \boldsymbol {\varepsilon}, \\ \bar {\varepsilon} (\boldsymbol {x}) := \frac {1}{| V |} \int_ {V} g (\boldsymbol {\xi}) \widetilde {\varepsilon} (\boldsymbol {x} + \boldsymbol {\xi})   \mathrm{d} \boldsymbol {\xi}. \end{array} \right.\tag{29}
$$

In the above, $V \subset \varOmega$ is an averaging volume, $\pmb { \xi } \in V$ , and $g$ is a bell-shaped function, typically a Gaussian, $g ( \pmb { \xi } ) : =$ $\bar { A } \exp ( - | \pmb { \xi } | ^ { 2 } / ( 2 l _ { c } ^ { 2 } ) )$ , with $l _ { c }$ related to the size (radius) of $V$ and representing the characteristic length of the non-local continuum. Constant A is chosen to provide $\begin{array} { r } { \frac { 1 } { | V | } \int _ { V } g ( \pmb { \xi } ) \mathrm { d } \pmb { \xi } = } \end{array}$ $1 . l _ { c }$ acts as a localization limiter, thus regularizing the problem [36] and the pathological mesh dependence of local damage models is avoided. Also, the introduction ofa length scale enables the description of size effects. 

The use of a Taylor series expansion o $\widetilde { \varepsilon }$ and the specific properties of $g _ { \ i }$ , 

$$
\begin{array}{l} \int_ {\Omega} g (\boldsymbol {\xi}) \xi_ {i}   \mathrm{d} \boldsymbol {\xi} = 0, i = 1, 2, \\ \int_ {\Omega} g (\boldsymbol {\xi}) \xi_ {1} \xi_ {2}   \mathrm{d} \boldsymbol {\xi} = 0, \\ \int_ {\Omega} g (\boldsymbol {\xi}) \xi_ {1} ^ {2}   d \boldsymbol {\xi} = \int_ {\Omega} g (\boldsymbol {\xi}) \xi_ {2} ^ {2}   \mathrm{d} \boldsymbol {\xi}, \end{array}
$$

turn Eq. (29b) into $\overline { { \varepsilon } } ( \mathbf { x } ) = \widetilde { \varepsilon } ( \mathbf { x } ) + c \Delta \widetilde { \varepsilon } ( \mathbf { x } ) + O ( l _ { c } ^ { 3 } )$ , where $c \sim$ $l _ { c } ^ { 2 } .$ Neglecting $O ( l _ { c } ^ { 3 } )$  , one obtains the gradient approximation of relation Eq. (29b): 

$$
\bar {\varepsilon} (\pmb {x}) = \widetilde {\varepsilon} (\pmb {x}) + c \Delta \widetilde {\varepsilon} (\pmb {x})\tag{30}
$$

(the notion of ’gradient’ is suggested due to $\Delta = \nabla ^ { 2 } )$ , whose coupling with Eq. (29a) yields the gradient-enhanced damage model. As the term $\Delta \widetilde { \varepsilon }$ requires a $C ^ { 1 }$ -continuous FE approximation for the displacement field, an alternative formulation was proposed by Peerlings et al. [27] to circumvent this requirement. Some extra manipulations recast Eq. (30) as a partial differential equation for $\overline { { \varepsilon } } ,$ and one ends up with the system 

$$
\left\{ \begin{array}{l} \boldsymbol {\sigma} (\boldsymbol {u}, D) := (1 - D (\bar {\varepsilon})) \mathbb {C}: \boldsymbol {\varepsilon}, \\ - c \Delta \bar {\varepsilon} + \bar {\varepsilon} = \widetilde {\varepsilon} (\boldsymbol {\varepsilon}), \end{array} \right.\tag{31}
$$

where $\bar { \varepsilon }$ now is an independent extra variable to be solved for. A straightforward use of $C ^ { 0 }$ -continuous finite element interpolation is enabled in this case. 

The structural similarities between Eq. (31) and all three phase-field formulations Eqs. (25)–(27) are now evident, also see [37]. 

In particular, we want to focus on the similarities between Eq. (31) and our hybrid model Eq. (27). The main observation here is that the system of Eq. (31) is ’variationally uncoupled’, that is, variationally inconsistent. Indeed, this is a phenomenological formulation, where 

• the stress–stress relation Eq. (31a) is postulated, including the assumption that D is driven by $\overline { { \varepsilon } } ,$ , and 

• the gradient-type evolution Eq. (31b) for ε¯ is viewed as an auxiliary one. The quantity ε entering the right-hand side of this gradient equation (i.e. the source term for ε¯) is not unique, admitting various specific mechanically motivated choices, as given by Eq. (28). Moreover, this equation itself stems from the heuristic, yet physically meaningful averaging assumption Eq. (29b) on ε. 

Adaptation of these two observations to Eq. (27) results in a non-variational derivation of the hybrid model to be sketched below. 

## 3.3 Non-variational derivation of the hybrid model

An underlying energy functional, whose minimization problem yields the coupled system Eq. (27) as the Euler-Lagrange equations, does not exist. Instead, following the above considerations, we may view Eq. (27) as a ’variationally uncoupled’ system with the postulated stress-stress relation Eq. (27a) and the joint gradient-type evolution Eq. (27b). We will show that Eq. (27b) can be obtained from some physically reasonable averaging-like assumption for d. 

In what follows, we prove that there exist the (scalarvalued) functions $F ( s )$ and $\varPhi ( \ell ; x )$ such that assuming 

$$
d (\boldsymbol {x}) := F \left(\frac {1}{| V |} \int_ {V} g (\boldsymbol {\xi}) \Phi (\ell ; \boldsymbol {x} + \boldsymbol {\xi}) \mathrm{d} \boldsymbol {\xi}\right),\tag{32}
$$

where V has the size of  and $g ( \pmb { \xi } ) : = A \exp ( - \vert \pmb { \xi } \vert ^ { 2 } / ( 2 \ell ^ { 2 } ) )$ one recovers Eq. (27b). Importantly, it will be seen that Φ depends on $\psi _ { 0 } ^ { + }$ in such a way that the generic properties of d are preserved. 

The derivation of F and Φ for Eq. (32) is rather straightforward. We start with Eq. (32) and employing the Taylor series expansion of Φ along with integration, we first obtain 

$$
d (\boldsymbol {x}) = F \left(\Phi (\ell ; \boldsymbol {x}) + \ell^ {2} \Delta \Phi (\ell ; \boldsymbol {x}) + O (\ell^ {3})\right),
$$

where $\begin{array} { r } { \ell ^ { 2 } : = \frac { 1 } { 2 | V | } \int _ { V } g ( \pmb { \xi } ) \xi _ { 1 } ^ { 2 } \mathrm { d } \pmb { \xi } } \end{array}$ . The properties of $g$ mentioned in Sect. $\dot { 3 } . \dot { 2 }$ were also used. Taylor series expansion of F yields 

$$
d (\boldsymbol {x}) = F \left(\Phi (\ell ; \boldsymbol {x})\right) + \ell^ {2} F ^ {\prime} \left(\Phi (\ell ; \boldsymbol {x})\right) \Delta \Phi (\ell ; \boldsymbol {x}) + O (\ell^ {3}),
$$

which, inserted into both sides of Eq. (27b), results in 

$$
- \ell^ {2} \Delta d + d := F (\varPhi) - \ell^ {2} F ^ {\prime \prime} (\varPhi) | \nabla \varPhi | ^ {2} + O (\ell^ {3}),
$$

and 

$$
\frac {2 \ell}{G _ {c}} (1 - d) \Psi_ {0} ^ {+} := \frac {2 \ell}{G _ {c}} (1 - F (\Phi)) \Psi_ {0} ^ {+} + O (\ell^ {3}),
$$

respectively. The equation that links F and $\phi$ then reads 

$$
\begin{array}{r l} & F (\varPhi) - \ell^ {2} F ^ {\prime \prime} (\varPhi) | \nabla \varPhi | ^ {2} + O (\ell^ {3}) \\ & = \frac {2 \ell}{G _ {c}} (1 - F (\varPhi)) \varPsi_ {0} ^ {+} + O (\ell^ {3}). \end{array}\tag{33}
$$

Imposing $F ^ { \prime \prime } ( s ) \equiv 0$ on F, we obtain that $F ^ { \prime } ( s ) = c \in \mathbb { R }$ and $F ( s ) = c s$ . Then, neglecting $O ( \ell ^ { 3 } )$ and plugging the result for F in Eq. (33), we arrive at 

$$
\varPhi = c ^ {- 1} \frac {\frac {2 \ell}{G _ {c}} \varPsi_ {0} ^ {+}}{1 + \frac {2 \ell}{G _ {c}} \varPsi_ {0} ^ {+}}.
$$

Our final result reads as follows 

$$
d (\boldsymbol {x}) := \frac {1}{| V |} \int_ {V} g (\boldsymbol {\xi}) \frac {\frac {2 \ell}{G _ {c}} \varPsi_ {0} ^ {+} (\boldsymbol {x} + \boldsymbol {\xi})}{1 + \frac {2 \ell}{G _ {c}} \varPsi_ {0} ^ {+} (\boldsymbol {x} + \boldsymbol {\xi})} \mathrm{d} \boldsymbol {\xi}.\tag{34}
$$

Note that Eq. (34) is physically meaningful, as it provides the desired basic properties of $d ,$ namely, $d \ \to \ 1$ (totally broken phase) when $\psi _ { 0 } ^ { + }  \infty$ , and $d \to 0$ (undamaged phase) when $\psi _ { 0 } ^ { + } \  \ 0$ . The former considers that |V | 1 $\begin{array} { r } { \int _ { V } g ( \pmb { \xi } ) \mathrm { d } \pmb { \xi } = 1 } \end{array}$ 

## 3.4 Algorithmic aspects

An accurate finite element treatment ofthe phase-field formulations of fracture is currently a computationally demanding task even in two dimensions, for the following main reasons: 

• the need to resolve the small length-scale  calls for extremely fine meshes, at least locally near the support of the phase-field variable d. In the absence of an efficient fully adaptive mesh refinement strategy, it has recently been typical to compute the models on fine (nonadaptive) fixed meshes, requiring high computational effort; 

• in order to properly account for the different cracking behavior in tension and compression, a specific split of an elastic energy density function is required, as suggested by Henry and Levine [9], Amor et al. [14] and Miehe et al. [15,16] (see Sect. 2.2), thus resulting in a (strongly) non-linear constitutive relation to be solved iteratively. Particularly, the split in [15,16] is based on the strain spectral decomposition and thus the need to update a significant amount of data at each Newton–Raphson iteration makes the corresponding formulation computationally very expensive; 

• following the ideas of algorithmic decoupling by Miehe et al. [16], the corresponding weak formulations of Eqs. (25)–(27) are to be solved using the staggered approach, which has proven extremely robust. However, in general, decoupling of the strongly coupled (and possibly non-linear) system of equations at hand seems justified only for ’small enough’ loading increments. Hence, the staggered scheme is in general rather expensive even for an isotropic phase-field formulation. The nested Newton–Raphson cycle needed for the anisotropic model adds further significant costs. 

The first issue is out of the scope of this contribution. We only note that some preliminary and very technical results on adaptive algorithms with application to the regularized formulation of Bourdin et al. [10] can be found in Burke et al. [38]. The authors are also addressing this issue in ongoing research. 

The second issue is the main focus of this paper, and is addressed by proposing the hybrid formulation which leads to a linear stress–strain relation. This is further elaborated as follows. 

As usual, let the domain Ω represent the configuration of an elastic isotropic body in the absence of applied forces. We assume that the boundary ∂Ω consists, in general, of four disjoint parts such that $\partial \Omega = { { T } _ { D , 0 } } \cup { { T } _ { D , 1 } } \cup { { T } _ { N , 0 } } \cup { { T } _ { N , 1 } }$ with $T _ { D , }$ and $T _ { N , \astrosun }$ being the portions where Dirichlet and Neumann boundary conditions are imposed, respectively. The second subscript of Γ indicates that the related condition is homogeneous (0) or inhomogeneous (1). 

With the admissible and test spaces for the displacement field, defined as 

$$
\mathbf {V} _ {1} := \left\{\boldsymbol {v} \in \mathbf {H} ^ {1} (\Omega): \boldsymbol {v} = \boldsymbol {0} \text {   on   } \Gamma_ {D, 0}, \boldsymbol {v} = \bar {\boldsymbol {u}} \text {   on   } \Gamma_ {D, 1} \right\},
$$

and 

$$
\mathbf {V} _ {0} := \left\{\boldsymbol {v} \in \mathbf {H} ^ {1} (\Omega): \boldsymbol {v} = \mathbf {0} \text {   on   } \Gamma_ {D, 0} \cup \Gamma_ {D, 1} \right\},
$$

respectively, the weak formulation of the models considered above reads: given $f ,$ <sub>u</sub>¯ <sub>and</sub> ¯<sub>t, find</sub> $( { \pmb u } , d ) \in { \bf V } _ { 1 } \times H ^ { 1 } ( \Omega )$ such that 

$$
\begin{array}{l} \int_ {\Omega} \boldsymbol {\sigma} (\boldsymbol {u}, d): \boldsymbol {\varepsilon} (\boldsymbol {v})   \mathrm{d} \boldsymbol {x} = \int_ {\Omega} \boldsymbol {f} \cdot \boldsymbol {v}   \mathrm{d} \boldsymbol {x} + \int_ {\Gamma_ {N, 1}} \bar {\boldsymbol {t}} \cdot \boldsymbol {v}   \mathrm{d} s, \\ \int_ {\Omega} \left[ \ell^ {2} \nabla d \cdot \nabla w + \Big (\frac {2 \ell}{G _ {c}} \mathcal {H} ^ {\star} (\boldsymbol {u}) + 1 \Big) d   w \right]   \mathrm{d} \boldsymbol {x} \\ = \frac {2 \ell}{G _ {c}} \int_ {\Omega} \mathcal {H} ^ {\star} (\boldsymbol {u}) w   \mathrm{d} \boldsymbol {x}, \end{array}\tag{35}
$$

(36) 

for any $( \pmb { v } , \pmb { w } ) \in \mathbf { V } _ { 0 } \times H ^ { 1 } ( \Omega )$ . Herein, f are the body forces, <sub>u</sub>¯ <sub>and</sub> ¯<sub>t are the displacement and traction loadings, respec-</sub> tively, and ${ \mathcal { H } } ^ { \star }$ stands either for or $\mathcal { H } ^ { + }$ , depending on the type of model. Also, since the homogeneous boundary conditions of Neumann type are prescribed for d on the entire ∂Ω, no surface integration appears in Eq. (36). 


Table 1 The core computations for the various models


<table><tr><td>Isotropic</td><td><eq>\varepsilon, \sigma, \frac{\partial \sigma}{\partial \varepsilon} = \mathbb{C}</eq></td></tr><tr><td>Anisotropic (Miehe)</td><td><eq>\varepsilon</eq>, eigenvalues/eigenvectors of <eq>\varepsilon</eq>,<eq>\varepsilon^{\pm}, \sigma^{\pm}, \frac{\partial \sigma^{\pm}}{\partial \varepsilon} =: \mathbb{C}^{\pm}(\varepsilon)</eq></td></tr><tr><td>Anisotropic (Amor)</td><td><eq>\varepsilon, \varepsilon^{\text{vol}}, \varepsilon^{\text{dev}}, \sigma^{\text{vol}}, \sigma^{\text{dev}}, \frac{\partial \sigma^{\pm}}{\partial \varepsilon} =: \mathbb{C}^{\pm}</eq></td></tr><tr><td>Hybrid</td><td><eq>\varepsilon, \sigma, \frac{\partial \sigma}{\partial \varepsilon} = \mathbb{C}</eq></td></tr></table>

In case of the anisotropic model, regardless of the type of split used for $\psi _ { 0 }$ (below, we will term them for simplicity as the Amor and Miehe splits), the linearization of Eq. (35) applies, 

$$
\begin{array}{l} \int_ {\Omega} \boldsymbol {\sigma} (\boldsymbol {u} ^ {\mathrm{i}}, d): \boldsymbol {\varepsilon} (\boldsymbol {v}) \mathrm{d} \boldsymbol {x} + \int_ {\Omega} \boldsymbol {\varepsilon} (\delta \boldsymbol {u} ^ {\mathrm{i}}): \frac {\partial \boldsymbol {\sigma}}{\partial \boldsymbol {\varepsilon}} (\boldsymbol {u} ^ {\mathrm{i}}, d): \boldsymbol {\varepsilon} (\boldsymbol {v}) \\ = \int_ {\Omega} \boldsymbol {f} \cdot \boldsymbol {v} \mathrm{d} \boldsymbol {x} + \int_ {\Gamma_ {N, 1}} \bar {\boldsymbol {t}} \cdot \boldsymbol {v} \mathrm{d} s, \end{array}\tag{dx}
$$

(37) 

where $\pmb { u } ^ { \mathrm { i } }$ stands for the displacement at iteration i within a Newton–Raphson iterative procedure and $\delta \boldsymbol { u } ^ { \mathrm { i } }$ is the unknown increment to be solved for to obtain $\pmb { u } ^ { \mathrm { i + 1 } } : = \pmb { u } ^ { \mathrm { i } } + \delta \pmb { u } ^ { \mathrm { i } }$ . The quantities to be computed at each iteration are reported in Table 1. The anisotropic model using Miehe’s split is obviously more expensive than the one using Amor’s decomposition. More importantly, the isotropic and the hybrid model lead to a constant stiffness matrix and thus converge in one iteration. 

Finally, we study the issue of the convergence of a staggered iterative process. The general framework ofa staggered scheme with application to the system Eqs. (35)–(36) can be found e.g. in [16]. We will focus on establishing of adequate stopping criterion for this process. 

Let $\bar { \mathbf { \ b { u } } } _ { l } , \bar { \mathbf { \ b { t } } } _ { l }$ and $\bar { \mathbf { u } } _ { l + 1 } , \bar { \mathbf { t } } _ { l + 1 }$ be the fixed external loadings at two consequent loading steps l and $l + 1 .$ , respectively, and <sub>such that the corresponding increments u</sub>¯ <sub>and </sub>¯<sub>t are posi-</sub> tive (monotonic loading). Let also the solution pair $( { \pmb u } _ { l } , d _ { l } )$ to the system Eqs. (35)–(36) at the loading step l be known and we seek for the solution pair at step $l + 1 . \mathrm { L e t }$ , furthermore, $\big \{ ( { \boldsymbol { u } } _ { l + 1 } ^ { k } , { \boldsymbol { d } } _ { l + 1 } ^ { k } ) \big \} , k = 1 , 2 , . .$ . be the sequence of the staggered solutions to Eqs. (35)–(36) computed using $( { \pmb u } _ { l } , d _ { l } )$ as an initial guess. In what follows, the subscript $l + 1$ will be dropped. Finally, we call a sequence of staggered iterations a staggered cycle. 

The natural quantity to control convergence of the staggered cycle is the energy of the system. We compute for every $k \geq 1$ the quantity $E _ { k } \ : = \ E ( { \pmb u } ^ { k } , d ^ { k } )$ ), where E is the energy functional of the adopted phase-field formulation. The sequence $\{ E _ { k } \} , k = 1 , 2 , . . . ,$ is expected to be a decreasing one, since we know that with $k  \infty$ the sequence $\big \{ ( { \bar { \pmb u } } ^ { k } , d ^ { k } ) \big \}$ has to converge to a minimizer $( \pmb { u } , d )$ of E. With an introduced quantity $f ( E _ { k } )$ , we stop the staggered cycle at iteration $k = N$ if the condition 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/0caf4c1570cbfbd488175154831e7989b7347dfebab99f02687b98cafcf75fff.jpg)



Fig. 3 System geometry and loading setup


$$
f (E _ {k}) _ {| k = N} \leq \mathrm{Tol},\tag{38}
$$

where Tol is a user-prescribed tolerance, is fulfilled. 

It turns out that the definition of $f$ in Eq. (38) is a delicate task, as it directly affects the choice of Tol. This will be illustrated by the following simple example. 

We consider a square specimen with a preexisting crack, subjected on its top part to an increasing, displacementcontrolled shear loading, as depicted in Fig. 3. The bottom part is completely fixed. With such a setup, the crack propagates towards the lower right corner of the specimen (see also Sect. 4). 

Following the procedure described above, we solve the system Eqs. (35)–(36) at load $u _ { l + 1 }$ . This load level is chosen such that the increment $\Delta u : = u _ { l + 1 } - u _ { l }$ , with $u _ { l }$ as the load at the previous step, is reasonably small. Also, the corresponding solution at load u is known and is used as the initial guess for the staggered cycle. We choose two quantities 

$$
\alpha (E _ {k}) := \frac {E _ {k} - E _ {k + 1}}{E _ {k + 1}} \times 100 \%,\tag{39}
$$

and 

$$
\beta (E _ {k}) := \arctan \left(\frac {E _ {k} - E _ {k + 1}}{(k + 1) - k}\right) \times \frac {1 8 0 ^ {\circ}}{\pi},\tag{40}
$$

$k = 1 , 2 , . . . ,$ to trace the convergence of the computed $E _ { k }$ $k = 1 , 2 , \ldots$ . and to check if they are suitable to be used in Eq. (38). Both appear rather natural, as e.g. the former aims at stopping the cycle when the increment $E _ { k } - E _ { k + 1 }$ becomes small in comparison to $E _ { k + 1 }$ . The latter assesses the slope of $E _ { k }$ at every $k \geq 1$ and aims at stopping the cycle when the slope becomes small enough. The plots of $E _ { k }$ $\alpha ( E _ { k } )$ and $\beta ( E _ { k } )$ ) are depicted in Fig. 4. Therein, we interrupt the staggered cycle at $k \ = \ 6 1$ when the ’stabilization’ of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/e22f94f19f73e197b8f1a2909b16d1574bfba3410778a043b4cd5eed2d83f163.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/4266314c26222d17c6627cb00ecc9fb6ab5cbfa0425ca063312ef9b1b8b7d2db.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/3fe21cddd93f3bdbae7f0cf55e695c052dda007204f1088426e590dc6f1c5500.jpg)



Fig. 4 The plots of $E _ { k } , \alpha ( E _ { k } )$ and $\beta ( E _ { k } )$ . The dimensions of α and $\beta$ are % and <sup>◦</sup> (degrees), respectively


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/ace73a9831af82290f1a47231e13c5294d96803552eb49752d04d72b95cec993.jpg)



Fig. 5 Crack phase-field at a staggered iteration $k \in \{ 1 0 , 2 0 , 6 0 \}$ corresponding to the energy ’levels’ $E _ { 1 0 }$ $E _ { 2 0 }$ $E _ { 6 0 }$ in Fig. 4


$E _ { k }$ becomes evident (i.e. when $E _ { k }$ tends asymptotically to a constant value). 

Our first observation is that, even with a reasonably small loading increment $\Delta u ,$ numerous staggered iterations may be needed in order for $E _ { k }$ to converge. An adequate stopping criterion is required, or an inaccurate crack phase-field will be obtained, as illustrated in Fig. 5 where a significant difference between the d field corresponding to $E _ { 1 0 }$ and $E _ { 6 0 }$ is visible. 

The second observation is that the quantities α and $\beta$ defined in Eqs. (39) and (40), respectively, appear inappropriate to define a stopping criterion, since it is not evident what value of Tol should be adopted in conjunction with these two measures. It can be seen in the plots for α and $\beta$ in Fig. 4 that setting in the corresponding cases $\mathrm { e . g . }$ . Tol = 1 % and $\mathrm { T o l } = 1 ^ { \circ }$ (what may seem a reasonable choice) will lead to stopping the cycle after two staggering iterations, thus yielding an incorrect solution. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/ef9c20f36eca3811b53c38d3b547fff2dde5219465456a37083f50107f0ead14.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/c5d758a74ae4ee22d3deaf0fe1ccc04d7d5c0507607ad81a9d2e1bc43a8d5dd0.jpg)



Fig. 6 The plots of $E _ { k } ^ { \mathrm { n o r m } }$ versus $s _ { k } ,$ , on the left, and $\gamma ( E _ { k } )$ versus $k ,$ on the right. The dimension of γ is <sup>◦</sup> (degrees)


The reason for the inadequacy of the above α and $\beta$ is that none of them accounts for the fact that the scales of $E _ { k }$ and k may be very different, see Fig. 4: $E _ { k }$ ranges approximately from 3.14 to 3.25, whereas k varies from 1 to 61 in this case. 

A simple remedy is an appropriate rescaling. Let $N > 1$ be the current staggered iteration. Having at hand the sequence $\{ E _ { k } \} _ { k = 1 } ^ { N } = \{ E _ { 1 } , E _ { 2 } , . . . , E _ { N } \}$ , we introduce the following normalized quantities 

$$
\left\{E _ {k} ^ {\mathrm{Norm}} \right\} _ {k = 1} ^ {N}, E _ {k} ^ {\mathrm{Norm}} := \frac {E _ {k} - E _ {N}}{E _ {1} - E _ {N}},\tag{41}
$$

and 

$$
\{s _ {k} \} _ {k = 1} ^ {N}, s _ {k} := \frac {k}{N}.\tag{42}
$$

The plot of $E _ { k } ^ { \mathrm { n o r m } }$ versus $s _ { k } ,$ obtained with $N ~ = ~ 6 1$ , is depicted in Fig. 6, left. 

Using Eqs. (41) and (42) we furthermore define 

$$
\gamma (E _ {k}) := \arctan \left(\frac {E _ {k} ^ {\text { Norm }} - E _ {k + 1} ^ {\text { Norm }}}{s _ {k + 1} - s _ {k}}\right) \times \frac {1 8 0 ^ {\circ}}{\pi},\tag{43}
$$

$k = 1 , 2 , \cdots , N$ , which may be viewed as a normalized analogue of Eq. (40). The plot of $\gamma$ is presented in Fig. $^ { 6 , }$ right. It can be concluded that $\gamma$ offers a more realistic choice of Tol $( \mathrm { e . g . 1 0 ^ { \circ } } )$ , at least in this particular case. 

Further analysis regarding the influence of the magnitude of the load increment on the number of staggered iterations required to meet the prescribed tolerance are presented in Sects. 4.1 and 4.2. 

## 4 Illustrative examples and comparisons

In this section, through numerous representative examples we test the proposed hybrid phase-field model against 

• the capability to adequately simulate crack initiation and propagation, including prevention of cracking in compression and interpenetration of the crack faces upon closure, as well as 

• the proclaimed inexpensiveness of the formulation with respect to the available canonical ones. 

We start with two classical benchmark problems, such as the single-edge notched tension and shear tests. For these two examples the qualitative and quantitative results obtained with our formulation and the isotropic and anisotropic models will be compared, also in terms of the corresponding computational costs. We will outline the influence of the number of staggered iterations at a fixed loading step upon the solution accuracy, also in relation to the magnitude of the loading increment between two loading steps. 

We continue with the more complex example of an $L -$ shaped panel under the cyclic loading. Herein, our particular goal is to demonstrate once again the role of the constrain we introduced into the hybrid formulation for prevention of the crack faces interpenetration. 

The group oflast three examples consists ofthe three-point bending test, an asymmetrically notched beam and a notched plate with hole. They aim at comparison between our hybrid model and the anisotropic model which uses Miehe’s split. The critical comparison of the computational effort in the corresponding situations will be in our main focus therein. 

The numerical computations are performed within the finite element framework using fully integrated bilinear quadrilaterals. The plain strain state is considered. We adopt the staggered solution stopping criterion presented in Sect. 3.4. 

## 4.1 Single-edge notched tension test

We apply all models to a square plate containing a straight horizontal notch located at mid-height of the left edge with a length of 0.5 mm. The geometric properties and boundary conditions of the specimen are shown in Fig. 7a. A verti-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/2aab7c5318c11c4c5d01ffb94ddf334f23bcbccbc935855af666a18e5aa12ba2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/7bfa1559d0dd6375318c05ca6947eda4ad10625cb951c908396b4c0a17d7156e.jpg)



Fig. 7 Geometry and boundary conditions of single-edge notched a Tension test and b Shear test


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/e09de4e3834ab8039ffbff51b2dbdeb0a16ae6d4031f17370b988156c62e914d.jpg)



Fig. 8 Single-edge notched tension test. Crack phase-field at displacements a $u = 5 . 5 \times 1 0 ^ { - 3 } \mathrm { m m } , \boldsymbol { \mathbf { b } } u = 5 . 7 \times 1 0 ^ { - 3 }$ mm and $\mathbf { c } u = 6 . 0 \times 1 0 ^ { - 3 }$ mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/5cef49f30901851b8f8a11959679b496db5708b5a86e29d08231fe7d9d126769.jpg)



Fig. 9 Single-edge notched tension test. Load–displacement curves


cal displacement is applied to the complete top edge. The material parameters are chosen as $\lambda ~ = ~ 1 2 1 . 1 5 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ 8 $\mu = 8 0 . 7 7 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ $G _ { c } = 2 . 7 \times 1 0 ^ { - 3 }$ kN/mm and $\ell =$ 

$4 . 0 \times 1 0 ^ { - 3 }$ mm to match the parameters of the same example in Miehe et al. [16]. The spatial discretization of the model contains 12735 quadrilateral elements, with an a priori refined mesh in the central region of the specimen where the crack propagation is expected. The displacement control is used with increments $\Delta u \ = \ 1 \times 1 0 ^ { - 5 }$ mm up to $u \ : = \ : 5 \times 1 0 ^ { - 3 }$ mm, and then $\Delta u \ = \ 1 \times 1 0 ^ { - 6 }$ mm up to failure. 

Figure 8 shows the crack patterns at several stages of loading for all tested models. Here the red and blue colors indicate to the damaged and undamaged material, respectively. The load–displacement curves are given in Fig. 9. For this simple setup all models, including the hybrid formulation, yield very similar results in terms of crack path and load– displacement behavior. Table 2 reports a comparison of the minimum and average numbers ofiterations required in order to obtain the solution for the displacement field at each load step. The values are reported separately for the pre-peak and 

Table 2 Single-edge notched tension test 

Comparison of the number of iterations per load step to solve the momentum equation for the displacement field 

<table><tr><td rowspan="3">Model</td><td colspan="4">Number of iterations per load step (2 staggered iterations)</td><td rowspan="3">Total comput. time w.r.t. hybrid model</td></tr><tr><td colspan="2">Min-max</td><td colspan="2">Average</td></tr><tr><td>Pre-peak</td><td>Post-peak</td><td>Pre-peak</td><td>Post-peak</td></tr><tr><td>Isotropic</td><td>1</td><td>1</td><td>1</td><td>1</td><td>Comparable</td></tr><tr><td>Anisotropic (Miehe)</td><td>2–6</td><td>6–12</td><td>3.8</td><td>6.4</td><td><eq>\approx 83 \%</eq> higher</td></tr><tr><td>Anisotropic (Amor)</td><td>2–6</td><td>6–14</td><td>3.5</td><td>6.6</td><td><eq>\approx 74 \%</eq> higher</td></tr><tr><td>Hybrid</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/510e445666605bbe92282d56860e13e4c51eb75dc7fac153b6ea1afe76b0b61b.jpg)



Fig. 10 Single-edge notched tension test. Effect of the number of staggered iterations on the crack phase-field with larger load increment $\Delta u = 1 \times 1 0 ^ { - 5 }$ mm and smaller load increment $\Delta u = 1 \times 1 0 ^ { - 6 }$ mm


post-peak regimes, as the latter is more challenging from the computational standpoint. It is evident that the anisotropic models lead to a substantially higher computational cost in comparison to the isotropic and hybrid models, due to the non-linearity of the momentum equation resulting from the tension-compression split. 

The convergence and stopping criteria for the staggered iteration have been discussed in Sect. 3.4. Herein, with Figs. 10 and 11 we intend to illustrate the effect of the number of staggered iterations in relation to the size of the loading increment. It can be clearly seen that an insufficient number of staggered iterations results in significantly inaccurate results, especially when relatively large loading increments are used. 

## 4.2 Single-edge notched shear test

The same specimen is now subjected to a pure shear loading, as depicted in Fig. 7(b). As we already mentioned, this example has become a canonical one in the phase-field literature, see e.g. [10,15,16] and [22], enabling to test the phasefield method in general, as well as the performance of the various particular formulations. Herein, we use a relatively fine uniform mesh with 20592 quadrilateral elements, which seems to be enough to eliminate the mesh-related effects. The pre-existing crack is modeled by defining an initial strainhistory field as in [22]. Fixed displacement increments of $\Delta u = 1 \times 1 0 ^ { - 5 }$ mm are used throughout the loading history. 

The crack patterns and load–displacement curves are shown in Figs. 12 and 13. For the isotropic model, two symmetric crack branches form, as was originally reported in [10]. This is due to the fact that related formulation allows cracking in the compressed regions of a body. In contrast, the other models, including our hybrid one, simulate the one-sided crack extensions. The anisotropic model with Miehe’s split yields a stiffer response in the last load-


at u = 0.0056 mm: a 1 staggered iteration, b 2 staggered iterations, c 4 staggered iterations and d 8 staggered iterations


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/6ef9b7182ac7fa4a75a1a1cfef60c5d9cf6d429d090d2b9f36078546e9122483.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/75b8a4acfa6e49d27c3cd631a69dd1a30bc94f926b109118375a1f46a183bcb7.jpg)



Fig. 11 Single-edge notched tension test. Effect of the number of staggered iterations on the load–displacement curve with a larger load increment $\Delta u \ = \ 1 \ \times \ 1 0 ^ { - 5 }$ mm and b smaller load increment $\Delta u = 1 \times 1 0 ^ { - 6 }$ mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/8e1798c058e5c5ad94adb2c566b00a3becf79890e302ebac61c4ed1b938d0ceb.jpg)



Fig. 12 Single-edge notched shear test. Crack phase-field at displacements a u = 0.012 mm, b u = 0.015 mm c u = 0.020 mm and d u = 0.030 mm, Anisotropic (Amor): c u = 0.016 mm and d u = 0.017 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/a96ff25fcc40e00731393f169ebf97a3e69b94de79d75e3202f2790d39790779.jpg)



Fig. 13 Single-edge notched shear test. Load–displacement curves


ing stage and never attains complete failure, as the cracked structure reaches a stage where no further evolution of the phase-field in the lower-right corner is possible. The subsequent behavior corresponds to the linearly elastic response of the cracked specimen clamped at the undamaged lowerright portion of the boundary, also see in [15]. On the other hand, the anisotropic model with Amor’s split features the development of a secondary crack at the lowerright corner of the specimen, so that complete failure is reached. In the absence of experimental results, it is difficult to judge which result is more physically relevant. Interestingly, our hybrid model delivers intermediate results between those obtained by the isotropic and anisotropic (Miehe) formulations. Table 3 shows the critical comparison of the computational costs required to solve the momentum equation. 

The effect of the number of staggered iterations on the crack pattern at a prescribed displacement and on the load– displacement curves for two different load increments are shown in Figs. 14 and 15. The same consideration made for the previous example applies here as well. 


Table 3 Single-edge notched shear test



Comparison of the number of iterations per load step to solve the momentum equation for the displacement field



Fig. 14 Single-edge notched shear test. Effect of the number of staggered iterations on the crack phase-field with larger load increment



$\Delta u = 1 \times 1 0 ^ { - 4 }$ mm and smaller load increment $\Delta u = 1 \times 1 0 ^ { - 5 }$ mm at $u = 0 . 0 1 5$ mm: a 1 staggered iteration, b 2 staggered iterations, c 4 staggered iterations and d 8 staggered iterations


<table><tr><td rowspan="3">Model</td><td colspan="4">Number of iterations per load step (2 staggered iterations)</td><td rowspan="3">Total comput. time w.r.t. hybrid model</td></tr><tr><td colspan="2">Min-max</td><td colspan="2">Average</td></tr><tr><td>Pre-peak</td><td>Post-peak</td><td>Pre-peak</td><td>Post-peak</td></tr><tr><td>Isotropic</td><td>1</td><td>1</td><td>1</td><td>1</td><td>comparable</td></tr><tr><td>Anisotropic (Miehe)</td><td>2–6</td><td>6–12</td><td>4</td><td>7.1</td><td><eq>\approx 85\%</eq> higher</td></tr><tr><td>Anisotropic (Amor)</td><td>2–6</td><td>6–14</td><td>3.7</td><td>7.3</td><td><eq>\approx 74\%</eq> higher</td></tr><tr><td>Hybrid</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/d2a0ff7826d7ceaf4151e334c6a3fd3afb57794fb05ca7bf35a9f61b155741bc.jpg)


## 4.3 L-shaped panel test

We now simulate crack propagation in an L-shaped slab. The geometry and boundary conditions of the problem are depicted in Fig. 16a. The experimental results are taken from [39], see Fig. 16b. The material parameters are chosen as follows: $\lambda \ : = \ : 6 . 1 6 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ 4 $\mu \ : = \ : 1 0 . 9 5 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ $\begin{array} { l l } { { G _ { c } } } & { { = } } \end{array}$ $8 . 9 \times 1 0 ^ { - 5 }$ kN/mm and $\ell = 1 . 1 8 7 5 \mathrm { m m }$ . A discretization with 9650 quadrilateral elements is used, with local mesh refinement in the areas where the crack is expected to form. 

Herein, we investigate the capability of the hybrid formulation to deal with crack closure. Recall that the anisotropic formulation a priori avoids the crack faces overlapping upon the crack closure, whereas in the hybrid model this is achieved by implementing the corresponding constrains. To simulate the desired effect, a cyclic displacement-controlled loading as in Fig. 17, with a fixed increment $\Delta u \ : = \ : 1 \ : \times$ $1 0 ^ { - 3 }$ mm, is imposed. 

The results we obtain with the hybrid formulation are compared with those of the anisotropic model using Miehe’s split. Thus, Fig. 18 illustrates the crack progression at several loading stages. The corresponding load–displacement curves are presented in Fig. 19. Both models are in fairly good agreement with the experimental results in terms of crack pattern. Importantly, with a marginal difference of the 


simulated crack patterns, the anisotropic model with Miehe’s split requires approximately 85 % higher time than the proposed hybrid formulation.


## 4.4 Three-point bending test

We now model three-point bending of a simply supported notched beam, see e.g Miehe et al. [16]. The setup for the simulation is given in Fig. 20. The material parameters are as follows: $\lambda = 1 2 . 0 0 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ $\mu = 8 . 0 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ $G _ { c } = 5 . 4 \times$ $1 0 ^ { - 4 } \mathrm { k N / m m }$ and $\ell = 0 . 0 3$ mm. A discretization with 9974 quadrilateral elements is used with an a priori refined mesh in the expected crack propagation region. The simulation is performed with displacement increments of $\Delta u = 1 \times$ $1 0 ^ { - 3 }$ mm for the first 40 steps, $\Delta u \ = \ 1 \times 1 0 ^ { - 5 }$ mm for the next 2,500 load steps and $\Delta u = 1 \times 1 0 ^ { - 4 }$ mm in the subsequent steps until complete failure. 

Figure 21 depicts the phase-field at several stages of loading, whereas the load–displacement curves are shown in Fig. 22. Both comparisons involve the hybrid and the anisotropic (Miehe) models, with practically identical results. The load–displacement curve features a nearly vertical load drop after the peak value, which might hide a snapback branch that cannot be captured in displacement controlled conditions without an arc-length control. Similarly to the previous example, the hybrid model required a significantly lower (≈ 82 %) computational time. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/b76984a5ce1e6d24c7a1dbe2a47e76de97b1fd52dd002b8bdec2c0b47f20fcfc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/112b33a7395744b03f968ff28906ab00135af5f5f52dd59fddac069e8eb95ad5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/8fea7b78b5ce3238260c3953f100515f0b410fa04eea7e9635aeb6a0bfb903ed.jpg)



Fig. 15 Single-edge notched shear test. Effect of the number of staggered iterations on the load–displacement curve with a Larger load increment $\Delta u = 1 \times 1 0 ^ { - 4 }$ mm and b Smaller load increment $\Delta u =$ $1 \times 1 0 ^ { - 5 } \mathrm { m m }$



Fig. 18 L-shaped panel test. Crack phase-field at displacements a u = 0.22 mm, b u = 0.30 mm, c u = 0.45 mm and d u = 1.0 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/3fbe1c35c2534df7c040317eea98d0a02bc749e7f1ac443ad28d9954fda6fbe7.jpg)



Fig. 16 L-shaped panel test. a Geometry and boundary conditions and b Experimentally observed crack pattern [39]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/927933faf007adaf1944ad500b390a8e20ead9b0bfd6d6a43ee4eaa6ba8b0139.jpg)



Fig. 17 L-shaped panel test. Loading history


## 4.5 Asymmetrically notched beam test

In this example, we model an asymmetrically-notched beam with an imposed displacement in the center and supported at two points, as illustrated in Fig. 23. The corresponding experimental results are taken from [40] and the material parameters $\lambda ~ = ~ 1 2 . 0 0 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ 4 $\mu \ = \ 8 . 0 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/ee25e3614fbdc4f773f368a2e207d4287e0029abf081181da307823cb3cedd13.jpg)



Fig. 19 L-shaped panel test. Load–displacement curves


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/080210c52e9ab37d7b971b10cd805f7de9bc43cd4dad74741693991d6f663c72.jpg)



Fig. 20 Three-point bending test. Geometry and boundary conditions [16]


$G _ { c } ~ = ~ 1 \times 1 0 ^ { - 3 }$ kN/mm and $\ell \ = \ 0 . 0 1$ mm are adopted from [16]. The discretization contains 30740 quadrilateral elements with a mesh refinement in the expected crack propagation region. For details on the influence of the mesh size on results of the phase-field model simulations we refer to [16]. 

The simulation has been performed with fixed displacement increments of $\Delta u = 1 \times 1 0 ^ { - 3 }$ mm for the first 200 steps and $\Delta u = 1 \times 1 0 ^ { - 4 }$ mm in the following steps. Figures 24 and 25 show that the hybrid and the anisotropic (Miehe) formulations are in excellent agreement with the experiments and with each other. As before, the hybrid model requires a significantly lower (≈ 85 %) computational time compared to the anisotropic model. 


Fig. 22 Three-point bending test. Load–displacement curves


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/f1ab9cfe232fa6c6171f173bdca29e8c29a6c013188f657801a5d6afe16143f8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/f54a5dbfa7f2ae58f5b0664784bb15ec434a2d87b9b0ba9c65f8d5939123a8c7.jpg)



Fig. 23 Asymmetrically notched beam test. a Geometry and boundary conditions and b Experimentally observed crack pattern [40]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/789d1d3257e90a02f206a467edd79a0728859dc2bdd53830bda87ba826877ff5.jpg)


## 4.6 Notched plate with hole

Finally, we model crack initiation and propagation for a notched plate with a hole. For this problem, we have conducted an experimental test in our laboratory to compare the crack trajectory obtained experimentally with the numerical predictions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/f5e1bad8fbc9a5f8389112b696a92f20f9154a28dfbcc051f24e5fa5bb9066b2.jpg)



Fig. 21 Three-point bending test. Crack phase-field at displacements a $u = 0 . 0 4 0$ mm, b $u = 0 . 0 5 0$ mm and $\mathbf { c } u = 0 . 1 2$ mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/a1c2daf2a79e6e58bd2a843a9fd76ca4c978899670cec0770e49e93eb440b319.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/4aacc7d0ad6642ccc23debc2c0dbc30dca6d3e3275834e963cbbdce7a3825d85.jpg)



Fig. 24 Asymmetrically notched beam test. Crack phase-field at displacements a $u \ : = \ : 0 . 2 2 3 \mathrm { m m }$ , b $u \ : = \ : 0 . 2 2 5$ mm, c $: u = 0 . 2 2 7$ mm and d u = 0.230 mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/21bc1afd98570f6ba100ac26a2c5acf4ecd21df21dec92c94945120a3485a45e.jpg)



Fig. 25 Asymmetrically notched beam test. Load–displacement curves


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/f45834b56c79245a78d079bc07bfbc6cbd429905c648f369a1f92e1a59655285.jpg)



Fig. 26 Notched plate with hole. a Geometry and boundary conditions and b Experimental setup


## 4.6.1 Experiment

The geometry, boundary conditions and experimental setup are shown in Fig. 26. The specimen is a notched plate, with load application by a top pin and a fixed lower pin, and with a hole offset from the center to induce mixed-mode fracture. 

The material used was cement mortar, composed of 22 % cement (cement I 32.5:high alumina cement 4:1), 66 % sand (grain size < 1 mm) and 12 % water, leading to a watercement ratio of 0.55. The material is expected to behave linearly elastic until brittle fracture occurs. The material parameters were measured on a compact tension specimen. The Young’s modulus was measured based on the compliance of the sample in accordance with [41] and the critical stress intensity factor follows from ASTM E399-12. The Poisson ratio was assumed to be 0.22, see e.g. [42]. The material parameters are $\lambda = 1 . 9 4 \mathrm { k N } / \mathrm { m m } ^ { 2 } , \mu = 2 . 4 5 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ and $G _ { c } = 2 . 2 8 \times 1 0 ^ { - 3 } \mathrm { k N / m m }$ . Experimentally, displacement controlled loading was applied at a rate of 0.1 mm/min. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/07077e8d62174cf207959614d442deaec1ec6849bae201f1c21a2bbf24798280.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/ba7c8e21619e7c51df0a40e5da830794518b6e432ad72020f0b8215873c76207.jpg)



(b)



Fig. 27 Notched plate with hole. a Fractured specimen and b Grayshaded area marking the experimentally observed crack patterns for the four tested samples


One of the fractured specimens is shown in Fig. 27a. A curved crack develops from the notch to the large hole. Later, a secondary straight crack appears from the hole to the sample edge. In Fig. 27b the envelope of crack paths found for four tested samples is marked by the grey area. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/3b1a6204060de8c43bf774c0ac64415ae7b7a3df061753b6695b56173e995675.jpg)



Fig. 29 Notched plate with hole. Load–displacement curves


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/6e0e19922a19e9acec667e2ce63639b9aa66ba101169700134b33563b309522d.jpg)


## 4.6.2 Numerical simulations


(a)



(b)


The numerical simulations have been performed with fixed displacement increments of $\Delta u = 1 \times 1 0 ^ { - 3 }$ mm throughout the simulation, with a length scale parameter $\ell = 0 . 1$ 1 mm. The mesh consists of 25085 quadrilateral elements with refinement in the areas where the crack is expected to form. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/a04d56ecb51cf9cc6c13ad63ffdd0af1d0f268d410c93a8a437831bc73f369e1.jpg)


The computational results are shown in Figs. 28 and 29. Both the hybrid and the anisotropic (Miehe) formulations capture well the experimentally observed crack pattern. In particular, the anisotropic model predicts a slightly more inclined secondary crack. The load–displacement curves are virtually identical up to an advanced failure stage, after which they differ by an offset due to a different magnitude of the post-peak load drop. As expected, the hybrid model enabled saving computational time compared to the anisotropic (Miehe) model, with an approximate difference of 85 % in favor of the hybrid formulation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/cb2eaa2edb450bd19f672900cf668da44ec59aad06d41c967030160df2966c44.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/172c948b-eb4a-47da-b321-e5b77cf98221/1a746dac302a5f2b9dca37cd566599494c3fa3ef766c6e3de3f1f476cc322209.jpg)



(d)



Fig. 28 Notched plate with hole. Crack phase-field at displacements $\mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm  ~ \ \ \mathrm { ~ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm { ~ \ \ } \mathrm \mathrm { ~ \ ~ \ \ } \mathrm  ~ \mathrm \ ~ \ \mathrm { ~ \ } \mathrm \mathrm { ~ \ ~ \ } \mathrm \mathrm { ~ \ \ ~ \ } \mathrm \mathrm \mathrm  ~ \ ~ \mathrm \mathrm { ~ \ ~ } \mathrm \mathrm \mathrm  ~ \ ~ \ \ \mathrm ~ \ \ \mathrm ~ \mathrm \ ~ \mathrm \ \mathrm ~ \ \mathrm { ~ } \mathrm \mathrm \mathrm \mathrm \mathrm$ , b u = 0.65 mm, $\textbf { c } u = 0 . 7 5$ mm and d $u = 2 . 2 3$ mm


## 5 Conclusions

Phase-field modeling of brittle fracture is a promising computational tool to handle fracture problems for 3D geometries with arbitrarily complex topologies of the crack surfaces. In this paper, we first provided a concise overview of the quasistatic and dynamic phase-field models offracture proposed to date in the physics and mechanics communities. The second goal of the paper was to address the question of computational efficiency, with focus on quasi-static fracture, on models based on Griffith’s theory featuring a tension-compression split (anisotropic models) and on staggered implementation schemes. Anisotropic models are the only ones able to handle the physically different cracking behavior of materials in tension and compression, as well as the contact conditions at the crack faces upon their closure. Staggered schemes have been proved to be the most robust option for complex fracture problems. 

On one hand, we proposed a simple but effective stopping criterion for the staggered scheme. This criterion was shown to lead to consistent results, as opposed to the possible misleading outcomes of more immediate alternatives. On the other hand, we introduced and tested a new hybrid (isotropic– anisotropic) formulation. This formulation was shown to lead to results very similar to those of the available anisotropic models, at a small fraction of their computational cost. The reason is that, unlike anisotropic models, the proposed hybrid formulation leads to an incrementally linear problem within a staggered implementation, which delivers a saving in computational cost of about one order of magnitude. The models were comparatively tested with numerous 2D benchmark examples, including one with own experimental verification for the crack pattern. 

As the hybrid model reproduces the predictive performance of anisotropic models at the cost of isotropic models, it is expected to be of even greater convenience for 3D fracture problems, where the significant advantages of phasefield modeling over alternative computational treatments can be best exploited. 

Acknowledgments This research was funded by the European Research Council, ERC Starting Researcher Grant INTERFACES, 

Grant Agreement No. 279439. The assistance of Dr. Roland Kruse (Institute of Applied Mechanics, TU Braunschweig) with the experimental tests for example 6 in Sect. 4 is gratefully acknowledged. 

## References



1. Krueger R (2004) Virtual crack closure technique: history, approach, and applications. Appl Mech Rev 57(2):109–143 





2. Ortiz M, Pandolfi A (1999) Finite-deformation irreversible cohesive elements for three-dimensional crack-propagation analysis. Int J Numer Methods Eng 44:1267–1282 





3. Moës N, Dolbow J, Belytschko T (1999) A finite element method for crack growth without remeshing. Int J Numer Methods Eng 46(1):131–150 





4. Aranson IS, Kalatsky VA, Vinokur VM (2000) Continuum field description of crack propagation. Phys Rev Lett 85:118–121 





5. Karma A, Kessler DA, Levine H (2001) Phase-field model of mode III dynamic fracture. Phys Rev Lett 87:045501 





6. Hakim V, Karma A (2009) Laws of crack motion and phase-field models of fracture. J Mech Phys Solids 57:342–368 





7. Spatschek R, Brener E, Karma A (2011) Phase field modeling of crack propagation. Philos Mag 91:75–95 





8. Eastgate LO, Sethna JP, Rauscher M, Cretegny T, Chen CS, Myers CR (2002) Fracture in mode I using a conserved phase-field model. Phys Rev E 71:036117 





9. Henry H, Levine H (2004) Dynamic instabilities of fracture under biaxial strain using a phase field model. Phys Rev Lett 93:105504 





10. Bourdin B, Francfort GA, Marigo JJ (2000) Numerical experiments in revisited brittle fracture. J Mech Phys Solids 48:797–826 





11. Bourdin B, Francfort GA, Marigo JJ (2008) The variationa approach to fracture. J Elast 91:5–148 





12. Kuhn C, Müller R (2008) A phase field model for fracture. Proc Appl Math Mech 8:10223–10224 





13. Kuhn C, Müller R (2010) A continuum phase field model for fracture. Eng Fract Mech 77:3625–3634 





14. Amor H, Marigo JJ, Maurini C (2009) Regularized formulation of the variational brittle fracture with unilateral contact: numerical experiments. J Mech Phys Solids 57:1209–1229 





15. Miehe C, Welschinger F, Hofacker M (2010) Thermodynamically consistent phase-field models of fracture: variational principles and multi-field FE implementations. Int J Numer Methods Eng 83:1273-1311 





16. Miehe C, Hofacker M, Welschinger F (2010) A phase field model for rate-independent crack propagation: robust algorithmic implementation based on operator splits. Comput Methods Appl Mech Eng 199:2765–2778 





17. Borden MJ, Hughes TJR, Landis CM, Verhoosel CV (2014) A higher-order phase-field model for brittle fracture: formulation and analysis within the isogeometric analysis framework. Comput Methods Appl Mech Eng 273:100–118 





18. Landau LD, Lifshitz EM (1980) Statistical physics. Pergamon Press, Oxford 





19. Francfort GA, Marigo JJ (1998) Revisiting brittle fractures as an energy minimization problem. J Mech Phys Solids 46:1319–1342 





20. Larsen CJ, Ortner C, Süli E (2010) Existence of solutions to a regularized model of dynamic fracture. Math Models Methods Appl Sci 20:1021–1048 





21. Bourdin B, Larsen CJ, Richardson C (2011) A time-discrete model for dynamic fracture based on crack regularization. Int J Fract 168:133–143 





22. Borden MJ, Verhoosel CV, Scott MA, Hughes TJR, Landis CM (2012) A phase-field description of dynamic brittle fracture. Comput Methods Appl Mech Eng 217—-220:77–95 





23. Hofacker M, Miehe C (2012) Continuum phase field modeling of dynamic fracture: variational principles and staggered FE implementation. Int J Fract 178:113–129 





24. Hofacker M, Miehe C (2013) A phase-field model of dynamic fracture: robust field updates for the analysis of complex crack patterns. Int J Numer Methods Eng 93:276–301 





25. Schlüter A, Willenbücher A, Kuhn C, Müller R (2014) Phase field approximation of dynamic brittle fracture. Comput Mech 54:1141– 1161 





26. Gurtin ME (1996) Generalized Ginzburg–Landau and Cahn– Hilliard equations based on a microforce balance. Phys D 92(3– 4):178–192 





27. Peerlings RHJ, de Borst R, Brekelmans WAM, de Vree JHP (1996) Gradient-enhanced damage for quasi-brittle materials. Int J Numer Methods Eng 39:3391–3403 





28. Kachanov LM (1986) Introduction to continuum damage mechanics. Springer, Netherland 





29. Murakami S (2012) Continuum damage mechanics. Springer Science and Business Media, Netherlands 





30. Simo JC, Ju JW (1987) Strain- and stress-based continuum damage models: I. Formulation. Int J Solids Struct 23:821–840 





31. Mazars J (1986) A description of micro- and macro-scale damage of concrete structures. J Eng Fract Mech 25:729–737 





32. de Vree JHP, Brekelmans WAM, Gils MAJ (1995) Comparison of nonlocal approaches in continuum damage mechanics. Comput Struct 55:581–588 





33. Pijaudier-Cabot G, Ba˘zant ZP (1987) Nonlocal damage theory. J Eng Mech 118:1512–1533 





34. Ba˘zant ZP, Pijaudier-Cabot G (1988) Nonlocal continuum damage, localization instability and convergence. ASME J Appl Mech 55:287–293 





35. Mazars J, Pijaudier-Cabot G (1989) Continuum damage theory: application to concrete. ASCE J Eng Mech 115:345–365 





36. Pijaudier-Cabot G, Huerta A (1991) Finite element analysis of bifurcation in nonlocal strain softening solids. Comput Methods Appl Mech Eng 90:905–919 





37. Verhoosel CV, de Borst R (2013) A phase-field model for cohesive fracture. Int J Numer Methods Eng 96:43–62 





38. Burke S, Ortner C, Süli E (2010) An adaptive finite element approximation of a variational model of brittle fracture. SIAM J Numer Anal 48:980–1012 





39. Winkler B (2001) Traglastuntersuchungen von unbewehrten und bewehrten Betonstrukturen auf der Grundlage eines objektiven Werkstoffgesetzes für Beton, Dissertation. University ofInnsbruck, Austria 





40. Bittencourt TN, Wawrzynek PA, Ingraffea AR, Sousa JL (1996) Quasi-automatic simulation of crack propagation for 2d LEFM problems. Eng Fract Mech 55:321–334 





41. Saxena A, Hudak SJ (1987) Review and extension of compliance information for common crack growth specimens. Int J Fract 14:453–468 





42. Watanabe T (2011) Analytical research on method for applying interfacial fracture mechanics to evaluate strength of cementitious adhesive interfaces for thin structural finish details. In: Cuppolett J (ed) Nanocomposites with unique properties and applications in medicine and industry, pp 67–82, ISBN: 978-953-307-351-4 

