# Phase-field modeling of ductile fracture

Article  in  Computational Mechanics · April 2015 

DOI: 10.1007/s00466-015-1151-4 

CITATIONS 80 

3 authors: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/2f492e25ee9fadb021250dc4b4b2222ab787d0c7367fde865d4f620d1072f63e.jpg)


Marreddy Ambat Institut für Angewandte Mechanik 

11 PUBLICATIONS   370 CITATIONS 

READS 1,741 

SEE PROFILE 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/0f0ca747944c0da8d20fcd5dcd93bcfc966b0a70557e5e9adf3821bc9af75765.jpg)


Tymofiy Gerasimov Technische Universität Braunschweig 

20 PUBLICATIONS   354 CITATION 

SEE PROFIL 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/d442327974bcd6f8dbec922fa6d5afb9c9c2025397e864e5d4981d908bf07b6d.jpg)


Laura De Lorenzis 

Technische Universität Braunschweig 

160 PUBLICATIONS   4,762 CITATIONS 

SEE PROFILE 

Some of the authors of this publication are also working on these related projects: 

Project 

Reproducing Sneddon's solution using fracture PhF formulations accurately is not easy View project 

ORIGINAL PAPER 

# Phase-field modeling of ductile fracture

M. Ambati<sup>1</sup> T. Gerasimov<sup>1</sup> L. De Lorenzis<sup>1</sup> 

Received: 10 December 2014 / Accepted: 29 March 2015 

© Springer-Verlag Berlin Heidelberg 2015 

Abstract Phase-field modeling of brittle fracture in elastic solids is a well-established framework that overcomes the limitations of the classical Griffith theory in the prediction of crack nucleation and in the identification of complicated crack paths including branching and merging. We propose a novel phase-field model for ductile fracture of elasto-plastic solids in the quasi-static kinematically linear regime. The formulation is shown to capture the entire range of behavior of a ductile material exhibiting J -plasticity, encompassing plasticization, crack initiation, propagation and failure. Several examples demonstrate the ability of the model to reproduce some important phenomenological features of ductile fracture as reported in the experimental literature. 

Keywords Phase-field model · Elastic–plastic solids · Fracture · Finite element 

## 1 Introduction

In the past two decades, the ability to accurately predict fracture in ductile materials has gained increasing importance in several industrial fields, including e.g. the automotive, aerospace and marine sectors, due to the constant quest for optimal design and weight reduction of new components. The availability of computational predictive tools allows for substantial savings in the cost of experiments, especially in cases where these are extremely complex (such as e.g. for gas pipelines, aircraft fuselages, or nuclear vessels), as well as for design optimization. A computational model for ductile fracture is expected to predict a number of behavioral features, including state of stress, damage patterns, the stability of possibly existing cracks, crack propagation paths and corresponding load-carrying capacity. 

Since the late sixties, several modeling approaches have been proposed for ductile fracture, see [1] for a comprehensive review. Following the classification in [1] but with a slight modification of the terminology, we will here distinguish between global andfield approaches. In the former, one or a few parameters are assumed to completely characterize the crack tip conditions. Within this category, the classical choice is Rice’s J-integral which presents a number of important drawbacks [1]: i. it can assess the stability of pre-existing crack-like flaws but cannot predict crack initiation and propagation from a notch or other stress concentrators; ii. the critical value of the J integral is not a material property as it strongly depends on the specimen geometry [2,3], which led to the proposal of the two-parameters J–Q approach [4]; iii. the method is not applicable to arbitrarily complex geometries. Subsequently developed alternatives using the so-called critical crack tip opening displacement or crack tip opening angle share the same limitations [5–7]. Global approaches are either adopted within analytical models or implemented with the finite element (FE) method (FEM), where crack propagation is typically dealt with using remeshing algorithms, which adapt the mesh topology to the crack geometry [8]. 

Field approaches [9,10], rather than relying on global parameters, base the prediction of fracture on a detailed description of the damage phenomena in the process zone. In turn, within field approaches we can distinguish between continuum and discrete formulations, both typically implemented with the FEM. Continuum approaches refer the description of damage to the volume of the material bulk and consist in the use of constitutive equations coupling plasticity and damage at the material point level. A large number of models have been proposed in this framework, see [1] for a review. Here we just mention the micro-mechanically motivated model by Gurson [11], where the plastic yield surface depends on a damage variable associated to the void volume fraction (or porosity); its improved version known as the Gurson–Tvergaard–Needleman (GTN) model [12], which incorporates additional parameters to better describe the void growth kinetics; and the phenomenological (i.e. macroscopic), thermodynamically consistent damage mechanics modeling framework developed by Lemaitre [13,14]. In all these models, the constitutive equations lead to a strong soft ening behavior as the damage level increases, which leads to strain and damage localization. This in turn determines the loss of ellipticity of the governing differential equations and, in a numerical discretized setting, a strong mesh sensitivity of the computational results. A few different solutions to this issue have been proposed, most notably the incorporation of a material length scale through non-local or gradient damage approaches [15,16]. Being endowed with a length scale, these approaches are additionally capable of predicting size effects, which is not possible with local models. Non-local or gradient versions of the Gurson and of the GTN models have been proposed in [17,18], respectively. 

Continuum formulations are typically unable to describe the surface decohesion and crack propagation phase subsequent to the softening and damage localization phase. Conversely, this phase is naturally handled by the discrete formulations, which involve a surface description. In an FE framework the proper modelling of discrete cracks of arbitrary geometry requires either remeshing [8] or embedding techniques such as the extended FEM (XFEM) [19], both allowing for the (respectively explicit and implicit) tracking of discontinuities within an existing mesh. In both cases, additional assumptions are needed for the crack initiation and propagation criteria, as well as for crack growth direction criteria. Moreover, both approaches present significant implementational difficulties, such as the need for suitable transfer of the state variables in the case of remeshing [20] as well as integration, conditioning and data handling issues for the XFEM, most notably in the 3D setting. A widely used alternative is the so-called cohesive zone modeling approach, implemented through interface or generalized contact elements [21–23]. This approach describes explicitly the discrete fracture process and is straightforward for crack paths known apriori [24–26]. Its extension to unknown crack paths entails the insertion of cohesive elements between each pair of continuum elements in an FE mesh, which may lead to strong mesh dependency and over-estimated cracked areas [27]. XFEM and cohesive zone modeling can be possibly coupled [28]. All discrete approaches cannot describe diffuse ductile damage, which in metals typically precedes the localization of damage within a thin band, and their applications are currently largely limited to brittle fracture or small-scale yielding conditions. 

Very recently, there have been attempts to combine the continuum and the discrete approaches to capture the transition between damage, localization, crack initiation and propagation. These attempts involved e.g. the combination of a Lemaitre-based non-local or gradient damage model [29,30] or of the GTN model [31] with the XFEM. Obviously, the crack propagation phase inherits the difficulties of the XFEM framework, moreover additional complications arise from the need for a consistent and seamless transition between continuum and discrete descriptions in subsequent behavioral stages. 

Phase-field modeling, which shares many features with continuum approaches, has recently emerged as a competitive alternative to discrete methods for the description of brittle fracture phenomena. In general, the phase-field approach to model systems with sharp interfaces consists in incorporating a continuous field variable—the so-called order parameter— which differentiates between multiple physical phases within a given system through a smooth transition. In the context of fracture, such order parameter (the crack phase field) describes the smooth transition between the fully broken and intact material phases, thus approximating the sharp crack discontinuity. The evolution of the crack phase field as a result of the external loading conditions models the fracture process. What makes the approach particularly attractive is its ability to elegantly simulate complicated fracture processes, including crack initiation, propagation, merging, and branching, in general situations and for 3D geometries, without the need for additional ad-hoc criteria. Propagating cracks are tracked automatically by the evolution of the smooth crack field on a fixed mesh. This leads to a significant advantage over the discrete fracture description methods outlined earlier. On the other hand, as mentioned earlier the approach shares several features with gradient-enhanced local continuum damage models. Therefore, it is the perfect candidate to enable a seamless transition between the description of continuum damage and discrete crack propagation phases. 

Phase-field modeling of brittle fracture has been a topic of very intense research in the past few years and has already attained impressive results [32–39]. The currently available formulations encompass static and dynamic approaches to brittle fracture. The extension to ductile fracture has been the subject of very limited attempts. In [40,41], fracture of ductile elastic–plastic solids was investigated under dynamic loading conditions. The focus was placed on reproducing the experimentally observed ductile to brittle failure mode transition with increasing loading speed. In these works, the total (free) energy functional is taken as the sum of elastic, plastic and fracture contributions. The elastic contribution takes the classical form, the fracture contribution contains only the component of the classical form involving the gradient of the phase-field, and the plastic contribution is a chosen function of the phase field and of the hardening variable. Recently, Duda et al. [42] proposed a phase field model for quasi-static brittle fracture in elasto-plastic solids, a phenomenon typical of metals below the ductile–brittle transition temperature. In this case, limited plastic deformation is assumed to take place in the vicinity of the notch root or crack tip. Also in this case the total energy is the sum of elastic, plastic and fracture contributions. The elastic and fracture contributions take the classical form used in available brittle fracture formulations, whereas the plastic contribution is a chosen function of the accumulated plastic strain including as parameters the elastic modulus, the yield stress and the strain hardening exponent. 

Objective of this paper is to propose a new phase-field formulation of ductile fracture in elasto-plastic solids, in the quasi-static kinematically linear regime. The distinct feature of the proposed model is the introduction of a coupling between the degradation function applied to the tensile portion of the elastic energy and the plastic strain state. This coupling is shown to play a fundamental role for the correct prediction of some phenomenological aspects of ductile fracture evidenced from available experimental results, and is proved to be thermodynamically consistent. The paper is structured as follows. Section 2 revisits the main features of phase-field models of brittle fracture for elastic solids, which serves as a basis for the subsequent extension to the ductile regime. Section 3 illustrates the proposed model, whose algorithmic aspects are developed in Sect. 4. Section 5 presents several numerical examples to test the predictive ability of the model with respect to some effects evidenced by experimental tests in the literature. Finally, conclusions are drawn in Sect. 6. 

## 2 Point of departure: phase-field models of brittle fracture of elastic solids revisited

Phase-field approaches to brittle fracture of elastic solids have been independently developed and investigated in the physics and mechanics communities starting from the late ’90s and the literature on the subject is wide. Our previous paper [39] provides an overview of the existing quasi-static and dynamic phase-field fracture formulations accepted in both communities. Herein, we focus on quasi-static fracture. 

As follows, we recall particularly the phase-field models of brittle fracture which originate from the variational formulation ofbrittlefracture by Francfort and Marigo [43] and the related regularizedformulation of Bourdin et al. [32]. All these formulations have been applied to linearly elastic materials in the small deformation framework. 

In [43], the entire (quasi-static) process of crack initiation, propagation and branching is governed by a minimization problem of the free energy functional 

$$
E (\boldsymbol {u}, \Gamma) = \int_ {\Omega} \Psi_ {\mathrm{e}} (\pmb {\varepsilon} (\boldsymbol {u})) d \mathbf {x} + G _ {c} \int_ {\Gamma} d s,\tag{1}
$$

where $\Psi _ { \mathrm { e } }$ is the elastic energy density function defined as $\begin{array} { r } { \Psi _ { \mathrm { e } } : = \frac { 1 } { 2 } \pmb { \varepsilon } : \mathbb { C } : \pmb { \varepsilon } = \frac { 1 } { 2 } \lambda \mathrm { t r } ^ { \bar { 2 } } ( \pmb { \varepsilon } ) + \mu \mathrm { t r } ( \pmb { \varepsilon } ^ { 2 } ) } \end{array}$ , with ε as the second order infinitesimal strain tensor, C as the fourth-order elasticity tensor, λ and $\mu$ as the Lamé constants, and $G _ { c }$ as the material fracture toughness. The solution is an admissible crack set $\Gamma \subset \Omega$ and a displacement field u : $\Omega \to \mathbb { R } ^ { n }$ , which is discontinuous across -. The shortcomings of the classical Griffith theory of brittle fracture are proven to be overcome by formulation (1), see [43] and also [44] for further details and a comprehensive overview. 

To enable an efficient numerical treatment of (1), its regularizedformulation was devised by Bourdin et al. [32]: 

$$
\begin{array}{l} E _ {\ell} (\boldsymbol {u}, s) = \int_ {\Omega} g (s) \Psi_ {\mathrm{e}} (\boldsymbol {\varepsilon} (\boldsymbol {u})) d \mathbf {x} \\ \qquad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \ell} (1 - s) ^ {2} + \ell | \nabla s | ^ {2}\right) d \mathbf {x}, \end{array}\tag{2}
$$

with a field variable s which indicates the crack (the crack field parameter) and which varies smoothly from 1 (undamaged material) to 0 (totally broken). The transition zone of s is controlled by the parameter $\ell > 0$ with the dimension of a length. Function $g ( s ) : = s ^ { 2 } + \eta$ couples s with the elastic field and typically satisfies $g ( s ) > 0$ for $0 < s \le 1$ . The small dimensionless parameter η models an artificial residual stiffness of a totally broken phase $( s = 0 )$ and is essentially needed to prevent numerical difficulties. 

With $\ell  0 .$ , the formulation (2) approximates (1) in the sense of --convergence, thus establishing the link between regularized and free-discontinuity fracture energies. This implies that the zero set of the crack field s indeed recovers the crack set -. 

Using variational principles, the minimization problem (2) can be reformulated as the system of the stress equilibrium equation div $\pmb { \sigma } ( \pmb { u } , s ) = 0$ , with σ as the second-order Cauchy stress tensor 

$$
\sigma (\boldsymbol {u}, s) := g (s) \frac {\partial \Psi_ {\mathrm{e}} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} = g (s) \mathbb {C}: \boldsymbol {\varepsilon},\tag{3}
$$

and the evolution equation for s: 

$$
2 \ell \Delta s + \frac {1 - s}{2 \ell} = \frac {g ^ {\prime} (s)}{G _ {c}} \Psi_ {\mathrm{e}} (\pmb {\varepsilon}),\tag{4}
$$

see e.g. [33,34]. 

The formulation (2) does not distinguish between fracture behavior in tension and compression. Already in [32] examples of unrealistic crack patterns in compression were reported. To avoid such situations, and, additionally, to prevent the interpenetration of the crack faces under compression, a modified regularized formulation of (1) was proposed in Amor et al. [35] and Miehe et al. [36,37], 

$$
\begin{array}{l} E _ {\ell} (\boldsymbol {u}, s) = \int_ {\Omega} \left[ g (s) \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon}) + \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon}) \right] d \mathbf {x} \\ \qquad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \ell} (1 - s) ^ {2} + \ell | \nabla s | ^ {2}\right) d \mathbf {x}, \end{array}\tag{5}
$$

using a specific additive decomposition $\Psi _ { \mathrm { e } } = \Psi _ { \mathrm { e } } ^ { + } + \Psi _ { \mathrm { e } } ^ { - }$ of the elastic energy density $\Psi _ { \mathrm { e } } .$ In contrast to (2), the degradation of only the positive energy part is allowed herein, whereas the negative part remains undegraded. 

Two options for decomposition of $\Psi _ { \mathrm { e } }$ can be found in the literature, namely, the split into volumetric and deviatoric contributions, see [35], 

$$
\begin{array}{l} \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon}) := \frac {1}{2} K _ {n} \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \rangle_ {+} ^ {2} + \mu (\boldsymbol {\varepsilon} _ {\mathrm{dev}}: \boldsymbol {\varepsilon} _ {\mathrm{dev}}), \\ \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon}) := \frac {1}{2} K _ {n} \langle \mathrm{tr} (\boldsymbol {\varepsilon}) \rangle_ {-} ^ {2}, \end{array}\tag{6}
$$

where $\begin{array} { r } { K _ { n } \ = \ \lambda + \frac { 2 \mu } { n } , \langle a \rangle _ { \pm } : = \ \frac { 1 } { 2 } ( a \pm | a | ) } \end{array}$ and $\begin{array} { r l } { \pmb { \varepsilon } _ { \mathrm { d e v } } } & { { } : = } \end{array}$ ${ \pmb \varepsilon } - \frac { 1 } { 3 } \mathrm { t r } ( { \pmb \varepsilon } ) I$ , as well as the split based on the spectral decomposition of the strain tensor $\begin{array} { r } { \pmb { \varepsilon } = \sum _ { I = 1 } ^ { 3 } \langle \varepsilon _ { I } \rangle \pmb { n } _ { I } \otimes \pmb { n } _ { I } } \end{array}$ , where $\{ \varepsilon _ { I } \} _ { I = 1 } ^ { 3 }$ and $\{ { \pmb n } _ { I } \} _ { I = 1 } ^ { 3 }$ are the principal strains and principal strain directions, respectively, see [36,37]. In this case, $\begin{array} { r } { \pmb { \varepsilon } _ { \pm } : = \sum _ { I = 1 } ^ { 3 } \langle \varepsilon _ { I } \rangle _ { \pm } \pmb { n } _ { I } \otimes \pmb { n } _ { I } } \end{array}$ and, eventually, 

$$
\Psi_ {\mathrm{e}} ^ {\pm} (\boldsymbol {\varepsilon}) := \frac {1}{2} \lambda \langle \operatorname{tr} (\boldsymbol {\varepsilon}) \rangle_ {\pm} ^ {2} + \mu \operatorname{tr} \left(\boldsymbol {\varepsilon} _ {\pm} ^ {2}\right).\tag{7}
$$

The system of Euler–Lagrange equations of the functional $E _ { \ell }$ in (5) involves the stress–strain relation and the evolution equation of the crack phase field reading as 

$$
\sigma (\boldsymbol {u}, s) := g (s) \frac {\partial \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}} + \frac {\partial \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon})}{\partial \boldsymbol {\varepsilon}},\tag{8}
$$

and 

$$
2 \ell \Delta s + \frac {1 - s}{2 \ell} = \frac {g ^ {\prime} (s)}{G _ {c}} \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon}),\tag{9}
$$

respectively. By coupling s with $\Psi _ { \mathrm { e } } ^ { + }$ in $E _ { \ell }$ , the evolution of s in (9) is driven only by the dilatational part of the volumetric strain, thus providing cracking in tension. On the other hand, the absence of $\Psi _ { \mathrm { e } } ^ { - }$ in (9) prevents crack evolution in the (highly) compressed parts of a solid, in which $\Psi _ { \mathrm { e } } ^ { - }$ is expected to dominate $\Psi _ { \mathrm { e } } ^ { + }$ . Also, since the $\Psi _ { \mathrm { e } } ^ { - }$ part remains undegraded in $E _ { \ell } .$ , resulting in the presence of $\partial \Psi _ { \mathrm { e } } ^ { - } / \partial \varepsilon$ ε in the relation (8), it can be expected that in case of crack closure the crack lips interpenetration is also prevented. It can be noticed finally that regardless of the type of split used in (5), the constitutive relation (8) is non-linear which is in contrast to (3). 

The results on --convergence for the functional $E _ { \ell }$ in (5) are not available. That is, strictly speaking, it is not clear what kind of functional (and hence what kind of ’physical’ process) is to be recovered when $\ell  0$ in this case. The formulation (5) using different kinds of split of $\Psi _ { \mathrm { e } } ,$ , however, has been shown to provide adequate simulation results for brittle fracture processes in elastic bodies, see e.g. [35–37]. 

To enhance the efficiency of phase-field computations, the so-called higher-order and hybrid formulations were recently proposed in [38] and [39], respectively. Extension of the quasi-static formulations (2) and (5) to the dynamic setting has been presented in numerous contributions, see e.g. [45–50]. 

## 3 Phase-field model of ductile fracture

## 3.1 The conceptual background

To illustrate the prime difficulties in deriving the phase-field model for elasto-plastic ductile fracture, we first summarize the conceptual scheme underlying the phase-field framework for brittle fracture in Fig. 1. The process 1 (i.e. the pure linearly elastic regime) and the related (classical) formulation E(u) → min, where 

$$
E (\boldsymbol {u}) := \int_ {\Omega} \Psi_ {\mathrm{e}} (\boldsymbol {\varepsilon} (\boldsymbol {u})) d \mathbf {x},\tag{10}
$$

can naturally be viewed as an embedded part ofthe process $\textcircled{2}$ (linear elasticity, followed by fracture) and ofthe corresponding variational formulation E(u, -) → min, with E(u, -) as in (1). In the figure, we use the sign ⇒ to indicate the ’extension’ of case (10) to (1) both in terms of the process and of the formulation. The relation between the ’sharp crack’ and the ’phase-field’/’diffusive crack’ formulations—the latter being given by (2) or, more generally, by (5)—is indicated by the symbol -. In practice, with a reasonably small  in (2) and (5), the computed σ-ε response in this case recovers the one from the process $\textcircled{2}$ . Note that all functionals involved in the considered logical scheme 

$$
E (\boldsymbol {u}) \Longrightarrow E (\boldsymbol {u}, \Gamma) \leftrightarrow E _ {\ell} (\boldsymbol {u}, s)\tag{11}
$$

are available. 

Using Fig. 1 as a conceptual layout, one difficulty in constructing the phase-field model for the ductile case becomes clear, see Fig. 2. The contents of the left plot in this figure— the process 1 and the related energy description—are well-established: we may take e.g. the $J _ { 2 }$ -plasticity framework as a starting point, i.e. 

$$
E (\pmb {\varepsilon} ^ {\mathrm{e}}, \pmb {\varepsilon} ^ {\mathrm{p}}, \alpha) := \int_ {\Omega} \left[ \Psi_ {\mathrm{e}} (\pmb {\varepsilon} ^ {\mathrm{e}}) + \Psi_ {\mathrm{p}} (\alpha) \right] d \mathbf {x},\tag{12}
$$


Fig. 1 From linear elasticity towards phase-field modeling of brittle fracture via the variational formulation


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/cede67fe388173e26933c11b10940f3f7cced484ef3452f9762f34e3625caea9.jpg)



Fig. 2 From plasticity towards phase-field modeling of ductile fracture: the corresponding variational formulation is a missing link


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/a4c7359858b27805c59f2bae48775bf034f742bd6d7f3e25bcdf5f3f3ed9a673.jpg)


where 

$$
\Psi_ {\mathrm{p}} (\alpha) := \sigma_ {\mathrm{y}} \alpha + \frac {1}{2} h \alpha^ {2},\tag{13}
$$

is the plastic energy density function assuming linear isotropic hardening, with yield stress $\sigma _ { \mathrm { y } }$ , hardening variable α and hardening modulus $h > 0$ . In (12), $\pmb { \varepsilon } ^ { \mathrm { e } }$ and $\pmb { \varepsilon } ^ { \mathrm { p } }$ are respectively the elastic and the plastic strain tensors, which are assumed to additively contribute to the total strain, $\pmb { \varepsilon } = \pmb { \varepsilon } ^ { \mathrm { e } } + \pmb { \varepsilon } ^ { \mathrm { p } }$ . The plastic strain $\pmb { \varepsilon } ^ { \mathrm { p } }$ and the hardening variable α are treated as internal (state) variables, for which appropriate evolution equations are established, see e.g. Simo and Hughes [51] or Owen [52]. 

Unfortunately, and in contrast to the previous case, we do not have here a variational theory that describes the ductile fracture process (the dashed line of the process $\textcircled{2}$ in Fig. 2) 

in the way it was done in the brittle case. That is, within the logical scheme 

$$
E (\boldsymbol {\varepsilon} ^ {\mathrm{e}}, \boldsymbol {\varepsilon} ^ {\mathrm{p}}, \alpha) \Longrightarrow E (\boldsymbol {\varepsilon} ^ {\mathrm{e}}, \boldsymbol {\varepsilon} ^ {\mathrm{p}}, \alpha , \Gamma) \leftrightarrow E _ {\ell} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}, \boldsymbol {\varepsilon} ^ {\mathrm{p}}, \alpha , s),\tag{14}
$$

which formally mimics (11), the functional $E ( \pmb { \varepsilon } ^ { \mathrm { e } } , \pmb { \varepsilon } ^ { \mathrm { p } } , \alpha , \Gamma )$ is not available. Therefore, we cannot derive its regularized counterpart $E _ { \ell } ( \pmb { \varepsilon } ^ { \mathrm { e } } , \pmb { \varepsilon } ^ { \mathrm { p } } , \alpha , s )$ to be treated as the corresponding phase-field formulation. 

To overcome this difficulty the following option may be considered: taking the elasto-plastic formulation (12)—as the one that is already capable of reproducing the process 1 in Fig. 2—and ’enriching’ it by mimicking the regularization formalism (2) or (5). This implies introducing an appropriate coupling function $g$ into $E ( \pmb { \varepsilon } ^ { \mathrm { e } } , \pmb { \varepsilon } ^ { \mathrm { p } } , \alpha )$ in (12), as well as adding the (original or modified) surface energy functional from (2) and (5). The resulting formulation should then be able to reproduce the process $\textcircled{2} .$ , most importantly, including its fracturing (dashed) part. 

One of the first attempts in this direction can be found in [42]. The formulation proposed therein relies on the free energy functional 

$$
\begin{array}{l} E _ {\ell} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}, \boldsymbol {\varepsilon} ^ {\mathrm{p}}, \alpha , s) := \int_ {\Omega} \left[ g (s) \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}) + \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}) + \Psi_ {\mathrm{p}} (\alpha) \right] d \mathbf {x} \\ \qquad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \ell} (1 - s) ^ {2} + \ell | \nabla s | ^ {2}\right) d \mathbf {x}, \end{array}\tag{15}
$$

with $g ( s ) = s ^ { 2 } + \eta$ and $\Psi _ { \mathrm { p } } ( \alpha )$ slightly different from the one in (13). The formulation is termed by the authors a phase-field/gradient damage model for brittle fracture in elasto-plastic solids. To our understanding, the reference to brittle fracture is due to the choice of $g ,$ which corresponds to the original brittle model in elastic solids (2) and (5). As may be guessed, the fracture mechanism (i.e. the evolution of the phase-field) in this case will be driven primarily by the elastic strains, thus the contribution of the plastic strains will be minor. This will be illustrated by some of the numerical examples in Sect. 5. 

From the above observation, it becomes clear that a cornerstone of the ductile phase-field model derivation is the appropriate choice of the function g and, particularly, that this function should depend not only on the phase-field variable s but also on a certain measure of the plastic strain state. 

## 3.2 The proposed model

In this contribution, we propose the following free energy functional 

$$
\begin{array}{l} E _ {\ell} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}, \boldsymbol {\varepsilon} ^ {\mathrm{p}}, \alpha , s) \\ := \int_ {\Omega} \left[ g (s, p) \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}) + \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon} ^ {\mathrm{e}}) + \Psi_ {\mathrm{p}} (\alpha) \right] d \mathbf {x} \\ \quad + G _ {c} \int_ {\Omega} \left(\frac {1}{4 \ell} (1 - s) ^ {2} + \ell | \nabla s | ^ {2}\right) d \mathbf {x}, \end{array}\tag{16}
$$

where we define 

$$
g (s, p) := s ^ {2 p} + \eta ,\tag{17}
$$

with 

$$
p := \frac {\varepsilon_ {\mathrm{eq}} ^ {\mathrm{p}}}{\varepsilon_ {\mathrm{eq,crit}} ^ {\mathrm{p}}}, \quad \varepsilon_ {\mathrm{eq}} ^ {\mathrm{p}} (t) := \sqrt {\frac {2}{3}} \int_ {0} ^ {t} \sqrt {\dot {\boldsymbol {\varepsilon}} ^ {\mathrm{p}} : \dot {\boldsymbol {\varepsilon}} ^ {\mathrm{p}}}   d \tau ,\tag{18}
$$

and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ as a threshold value. $\varepsilon _ { \mathrm { e q } } ^ { \mathrm { p } }$ is often referred to as the von Mises equivalent plastic strain. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/af210d99f6d1330bf880ce9f1f911f2163135a4844e15b765533e32e68ed84f8.jpg)



Fig. 3 The conceptual backbone of the proposed model: a the plastic strain accumulation and localization zone within  and the related $p = p ( \pmb { \varepsilon } ^ { \mathrm { p } } ( \mathbf { x } , t ) ) ;$ t stands for the pseudo-time; b the phase-field s(x, t) triggered by p and occurring in the plastic strain localization zone


The variable $p$ accounts for accumulation and localization of plastic strains, and our idea of devising (17), i.e. incorporation of $p$ into the coupling function $^ { g , }$ , is to make s dependent on $p ,$ , thereby assuming that the fracture process is the result of the accumulation of the ductile damage. 

As shown in the following, due to (17) p enters the evolution equation for s, thus already providing their implicit relation. The explicit interaction between s and p (or rather the influence of p upon s) is clarified in Appendix 1, using an asymptotic (perturbation) analysis, and is shown to obey 

$$
s \sim 1 - \frac {4 \ell}{G _ {c}} p \Psi_ {\mathrm{e}} ^ {+} (\pmb {\varepsilon} ^ {\mathrm{e}}).\tag{19}
$$

The latter particularly means that, owing to (17)–(18), the contribution of the plastic strains to the phase-field development should be, at least, competitive with the contribution of the elastic strains. In the numerical examples in Sect. 5, we will observe that $p$ takes even a dominating role over $\Psi _ { \mathrm { e } } ^ { + }$ , thus ’delaying’ the brittle-like fracture development and enabling the desired plasticity-driven fracture initiation and propagation mechanism, as depicted in Fig. 3. 

The variational derivative of $E _ { \ell }$ with respect to $\pmb { \varepsilon } ^ { \mathrm { e } }$ leads to the equilibrium equation div ${ \pmb \sigma } = { \bf 0 } .$ , where the stress takes the form 

$$
\sigma (\boldsymbol {\varepsilon} ^ {\mathrm{e}}, s, p) := g (s, p) \frac {\partial \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon} ^ {\mathrm{e}})}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}} + \frac {\partial \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon} ^ {\mathrm{e}})}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}}.\tag{20}
$$

For the current formulation, we assume the material obeys J -plasticity with linear isotropic hardening, thus Eq. (13) holds. Moreover, the yielding function is defined as 

$$
f (\pmb {\sigma}, \alpha , s, p) = \sqrt {3 J _ {2} (\pmb {\sigma} _ {\mathrm{dev}})} + t _ {\alpha} \leq 0,\tag{21}
$$

where $J _ { 2 } ( \pmb { \sigma } _ { \mathrm { d e v } } )$ ) is the second invariant of the deviatoric stress tensor $\begin{array} { r } { \pmb { \sigma } _ { \mathrm { d e v } } : = \pmb { \sigma } - \frac { 1 } { 3 } \mathrm { t r } ( \pmb { \sigma } ) \pmb { I } } \end{array}$ and $t _ { \alpha }$ is the hardening thermodynamical force obtained from (16) and (13) as 

$$
t _ {\alpha} := - \frac {\partial E _ {\ell}}{\partial \alpha} = - (\sigma_ {\mathrm{y}} + h \alpha).\tag{22}
$$

Assuming associative plasticity, the evolution equation for the plastic strain $\pmb { \varepsilon } ^ { \mathrm { p } }$ and the internal hardening variable α are 

$$
\dot {\pmb {\varepsilon}} ^ {\mathrm{p}} (\pmb {\sigma}, s, p) = \dot {\lambda} \frac {\partial f}{\partial \sigma},
$$

$$
\dot {\alpha} = \dot {\lambda} \frac {\partial f}{\partial t _ {\alpha}},\tag{23}
$$

where $\dot { \lambda }$ is the plastic consistency factor. Note that these evolution equations are the same of classical J<sub>2</sub>-plasticity, where they automatically ensure satisfaction of the second law of thermodynamics. The fact that the same evolution equations can be used in the present model while still guaranteeing thermodynamic consistency is demonstrated in Appendix 2. Loading and unloading conditions are governed by the Kuhn–Tucker relations 

$$
\dot {\lambda} \geq 0, \quad f \leq 0, \quad \dot {\lambda} f = 0.\tag{24}
$$

The evolution equation for the crack phase-field reads 

$$
2 \ell \Delta s + \frac {1 - s}{2 \ell} = \frac {g _ {, s} (s , p)}{G _ {c}} \Psi_ {\mathrm{e}} ^ {+} (\pmb {\varepsilon} ^ {\mathrm{e}}),
$$

where $\begin{array} { r } { g _ { , s } = \frac { \partial g } { \partial s } } \end{array}$ and with g as in (17) it turns into 

$$
2 \ell \Delta s + \frac {1 - s}{2 \ell} = \frac {2 s ^ {2 p - 1}}{G _ {c}} p \Psi_ {\mathrm{e}} ^ {+} (\pmb {\varepsilon} ^ {\mathrm{e}}).\tag{25}
$$

As was already mentioned and as it can now be seen from (25), the phase-field s is not only driven by the tensile part of the elastic energy but it also depends on the introduced plastic variable $p .$ The explicit relation between s and $p$ is given by (19), see Appendix 1 for the derivation details. 

The irreversibility of the crack phase-field during loading/unloading is ensured by the introduction of the following local history variable into (25) 

$$
\mathcal {H} _ {\mathrm{e}} (\mathbf {x}, t) := \max _ {\tau \in [ 0, t ]} \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon} ^ {\mathrm{e}} (\mathbf {x}, \tau)),\tag{26}
$$

This represents the maximum positive elastic energy obtained in a loading process and stems from the work of Miehe and co-workers on brittle fracture models [37]. Note that the introduction of (26) also enables algorithmic decoupling of the governing system of equations and the application of a staggered approach, which is extremely robust for computing phase-field models. 

The system of governing equations of the proposed elastoplastic ductilefracture model is summarized in Table 1. 

The following Neumann and Dirichlet boundary conditions apply 

Table 1 Governing equations of the proposed elasto-plastic ductile fracture model 

$$
\operatorname{div} \boldsymbol {\sigma} = \mathbf {0}\tag{a}
$$

$$
\sigma := (s ^ {2 p} + \eta) \frac {\partial \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon} ^ {\mathrm{e}})}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}} + \frac {\partial \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon} ^ {\mathrm{e}})}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}}\tag{b}
$$

$$
f = \sqrt {3 J _ {2} (\pmb {\sigma} _ {\mathrm{dev}})} - (\sigma_ {\mathrm{y}} + h \alpha) \leq 0\tag{c}
$$

$$
\dot {\pmb {\varepsilon}} ^ {\mathrm{p}} = \dot {\lambda} \sqrt {\frac {3}{2}} \frac {\pmb {\sigma} _ {\mathrm{dev}}}{\| \pmb {\sigma} _ {\mathrm{dev}} \|}, \quad \dot {\alpha} = \dot {\lambda}\tag{d}
$$

$$
\dot {\lambda} \geq 0, f \leq 0, \dot {\lambda} f = 0\tag{e}
$$

$$
p := \frac {\varepsilon_ {\mathrm{eq}} ^ {\mathrm{p}}}{\varepsilon_ {\mathrm{eq,crit}} ^ {\mathrm{p}}}\tag{f}
$$

$$
2 \ell \Delta s + \frac {1 - s}{2 \ell} = \frac {2 s ^ {2 p - 1}}{G _ {c}} p \mathcal {H} _ {\mathrm{e}}\tag{g}
$$

Table 2 Governing equations ofthe elasto-plastic brittle fracture model 

$$
\operatorname{div} \boldsymbol {\sigma} = \mathbf {0}\tag{a}
$$

$$
\sigma := (s ^ {2} + \eta) \frac {\partial \Psi_ {\mathrm{e}} ^ {+} (\boldsymbol {\varepsilon} ^ {\mathrm{e}})}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}} + \frac {\partial \Psi_ {\mathrm{e}} ^ {-} (\boldsymbol {\varepsilon} ^ {\mathrm{e}})}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}}\tag{b}
$$

$$
f = \sqrt {3 J _ {2} (\sigma_ {\mathrm{dev}})} - (\sigma_ {\mathrm{y}} + h \alpha) \leq 0\tag{c}
$$

$$
\dot {\pmb {\varepsilon}} ^ {\mathrm{p}} = \dot {\lambda} \sqrt {\frac {3}{2}} \frac {\pmb {\sigma} _ {\mathrm{dev}}}{\| \pmb {\sigma} _ {\mathrm{dev}} \|}, \quad \dot {\alpha} = \dot {\lambda}\tag{d}
$$

$$
\dot {\lambda} \geq 0, \quad f \leq 0, \quad \dot {\lambda} f = 0
$$

$$
2 \ell \Delta s + \frac {1 - s}{2 \ell} = \frac {2 s}{G _ {c}} \mathcal {H} _ {\mathrm{e}}\tag{e}
$$

(f) 

$$
\begin{array}{c} \boldsymbol {u} = \bar {\boldsymbol {u}} \text {on} \partial \Omega_ {\bar {u}}, \\ \boldsymbol {\sigma} \cdot \boldsymbol {n} = \bar {\boldsymbol {t}} \text {on} \partial \Omega_ {\bar {t}}, \\ \nabla s \cdot \boldsymbol {n} = 0 \text {on} \partial \Omega , \end{array}\tag{27}
$$

<sub>where u</sub>¯ <sub>and</sub> ¯<sub>t are prescribed on</sub> $\partial \Omega _ { \bar { u } }$ and $\partial \Omega _ { \bar { t } } ,$ , respectively, $\partial \Omega = \partial \Omega _ { \bar { u } } \cup \partial \Omega _ { \bar { t } }$ and $\partial \Omega _ { \bar { u } } \cap \partial \Omega _ { \bar { t } } = \emptyset .$ . Finally, n is the outward normal unit vector to the boundary. 

Remark 1 Setting formally $p \equiv 1$ in (16) one recovers a formulation similar to the one in [42], which we will term elasto-plastic brittlefracture model. The corresponding governing system of equations is summarized in Table 2. The boundary conditions (27) apply in this case as well. 

Note that the evolution equation (f) is the same as (9), which is valid for brittle fracture of elastic solids, where s is driven only by the tensile part of the elastic stored energy. It has no interaction with the plastic flow mechanism and thus does not account for the plastic strain localization. 

## 3.3 Generalization of the coupling function

The coupling function $g ( s , p ) = s ^ { 2 p } + \eta$ introduced above can be generalized as follows 

$$
g (s, p) := s ^ {2 p ^ {m}} + \eta ,\tag{28}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/25ff275da7b9704c204a6e71ba9632a029536b32443bbb53f4ad260c2d047cae.jpg)



Fig. 4 The plastic variable $p ^ { m }$ for $m = 1 , 2 , 3$ as a function of the equivalent plastic strain $\varepsilon _ { \mathrm { e q } } ^ { \mathrm { p } }$


where $m ~ \in ~ \{ 1 , 2 , 3 , \ldots \}$ . The purpose of introducing an additional parameter in $g$ is to enable a greater flexibility in controlling the ’speed’ of a ductile fracture mechanism. Indeed, the increase of the order of $\begin{array} { r } { p = \frac { \varepsilon _ { \mathrm { e q } } ^ { \mathrm { p } } } { \varepsilon _ { \mathrm { e q , c r i } } ^ { \mathrm { p } } } } \end{array}$ is expected to slow down the accumulation of damage before reaching the threshold value $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ , that is when $p \ < \ 1$ , see Fig. 4, and to accelerate it when the threshold is exceeded $( p > 1 )$ ). The effect of m is studied in some of the examples in Sect. 5. 

## 4 Algorithmic aspects

## 4.1 Staggered solution strategy

Following the ideas of algorithmic decoupling by Miehe et al. [37], we solve the weak formulations of equations (a) and (g) from Table 1, as well as of (a) and (f) from Table 2, using a staggered strategy. The strategy adopted for the proposed model is slightly different from the one of brittle fracture implementations, and is therefore illustrated in Figure 5. 

At each pseudo-time/loading step, we must solve the weak counterparts of the momentum equation (a) and evolution equation (g). Both equations involve the variables u, s, as well as the internal plastic variables $\pmb { \varepsilon } ^ { \mathrm { p } }$ , α and the additional variable $p .$ . We group these variables in two sets, set A including u, $\pmb { \varepsilon } ^ { \mathrm { p } }$ (from which ε and $\pmb { \varepsilon } ^ { \mathrm { e } }$ can be computed) and α, and set B including s and $p .$ . 

First, the momentum equation (a) is solved for frozen set B, to determine the new set A. Along with equation (a), the evolution equations (d) are also solved while ensuring conditions (c) and (e), using the return mapping algorithm presented in Sect. 4.2. Using the updated elastic and plastic strains, the variable $p$ is computed and the phase-field evolution equation (g) is solved for frozen A. 

Note that there are different possible ways to group the governing variables in the two sets A and B. The chosen one, where $p$ and $\pmb { \varepsilon } ^ { \mathrm { p } }$ are included in different sets, might appear counter-intuitive but greatly simplifies the return mapping algorithm presented in Sect. 4.2. We use the same implementation strategy for the model in Table 2, with the only difference that, in this case, p is not present as additional variable. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/f2ca9ec5f1fadd54fce28d1ca8937d1991299b3ad0d3a3a3e20341362ee6ceb4.jpg)



Fig. 5 Staggered solution strategy adopted for the proposed mode


Finally, we comment on the convergence and the stopping criterion of the staggered iterative process in Fig. 5. We control the (monotonically decreasing) sequence of energies $\{ E _ { \ell , i } \} , i \ = \ 1 , 2 , . . . x$ and the iterative process is stopped when the user-prescribed tolerance for the quantity $\gamma ( E _ { \ell , i } ) , i = 1 , 2 , \ldots$ is achieved. Herein, γ represents the normalized energy- and number-of-iterations-related scales. We refer to our recent paper [39] for further details. 

## 4.2 Time integration

The time integration algorithm for the elasto-plastic constitutive equations for the models of Tables 1 and 2 is briefly presented as follows. The evolution equations of the plastic variables in Tables 1(d) and 2(d) can be integrated with the backward Euler scheme, obtaining 

$$
\pmb {\varepsilon} _ {n + 1} ^ {\mathrm{p}} = \pmb {\varepsilon} _ {n} ^ {\mathrm{p}} + \Delta \lambda \sqrt {\frac {3}{2}} \pmb {n} _ {n + 1}, \quad \alpha_ {n + 1} = \alpha_ {n} + \Delta \lambda ,\tag{29}
$$

with $\begin{array} { r } { n = \frac { \pmb { \sigma } _ { \mathrm { d e v } , n + 1 } } { \left\| \pmb { \sigma } _ { \mathrm { d e v } , n + 1 } \right\| } } \end{array}$ and $\Delta \lambda > 0$ as the incremental plastic multiplier. The subscripts $( \cdot ) _ { n }$ and $( \cdot ) _ { n + 1 }$ define the values of (·) at $t _ { n }$ and $t _ { n + 1 }$ , respectively. The discrete versions of the yielding and of the Kuhn-Tucker conditions read 

$$
\begin{array}{c} f (\sigma_ {n + 1}, \alpha_ {n + 1}) = \sqrt {3 J _ {2} \left(\sigma_ {\mathrm{dev} , n + 1}\right)} - (\sigma_ {\mathrm{y}} + h \alpha_ {n + 1}) \leq 0 \\ \Delta \lambda \geq 0, \quad f (\sigma_ {n + 1}, \alpha_ {n + 1}) \leq 0, \quad \Delta \lambda f (\sigma_ {n + 1}, \alpha_ {n + 1}) = 0. \end{array}\tag{30}
$$

In order to solve (29) while satisfying (30), we adopt the classical elastic predictor and plastic corrector (return-mapping) algorithm outlined in [52]. Given the elastic strain, plastic strain and internal variables $\pmb { \varepsilon } _ { n } ^ { \mathrm { e } } , \pmb { \varepsilon } _ { n } ^ { \mathrm { p } }$ and $\alpha _ { n }$ at the beginning of the pseudo-time interval $[ t _ { n } , t _ { n + 1 } ]$ ] and with the prescribed incremental strain $\Delta \pmb \varepsilon$ for this interval, we consider an elastic trial state obtained by freezing plastic flow $( \Delta \lambda = 0 )$ ). For the $J _ { 2 } \cdot$ -plasticity model with linear isotropic hardening, the trial deviatoric stress and the trial yielding condition are given by 

$$
\begin{array}{c} \boldsymbol {\sigma} _ {\mathrm{dev}, n + 1} ^ {\mathrm{tr}} = \hat {g} 2 \mu \boldsymbol {\varepsilon} _ {\mathrm{dev}, n + 1} ^ {\mathrm{e,tr}} \\ f _ {n + 1} ^ {\mathrm{tr}} = \sqrt {3 J _ {2} \left(\boldsymbol {\sigma} _ {\mathrm{dev} , n + 1} ^ {\mathrm{tr}}\right)} - (\sigma_ {\mathrm{y}} + h \alpha_ {n}) \leq 0 \end{array}
$$

where $( \cdot ) ^ { \mathrm { t r } }$ denotes a trial quantity and $\hat { g } = g ( \hat { s } , \hat { p } )$ (model in Table 1) or ${ \hat { g } } = g ( { \hat { s } } )$ (model in Table 2) with sˆ and $\hat { p }$ as frozen variables of the current staggered iteration. If $f _ { n + 1 } ^ { \mathrm { t r } } \leq 0$ then the process is purely elastic and the elastic trial state is the solution. $\operatorname { I f } ,$ on the other hand, $f _ { n + 1 } ^ { \mathrm { t r } } ~ > ~ 0 .$ , the trial stress is not admissible, the process is elasto-plastic and a plastic corrector step is needed. For the present case, the incremental plastic multiplier can be obtained from the following scalar equation having $\Delta \lambda > 0$ as the only unknown 

$$
\sqrt {3 J _ {2} \left(\sigma_ {\mathrm{dev} , n + 1} ^ {\mathrm{tr}}\right)} - (\sigma_ {\mathrm{y}} + h \alpha_ {n}) - h \Delta \lambda - \hat {g} 3 \mu \Delta \lambda = 0.
$$

With the solution $\Delta \lambda$ at hand, the state variables are updated as follows 

$$
\pmb {\varepsilon} _ {n + 1} ^ {\mathrm{p}} = \pmb {\varepsilon} _ {n} ^ {\mathrm{p}} + \Delta \lambda \sqrt {\frac {3}{2}} \pmb {n} _ {n + 1} ^ {\mathrm{tr}}, \quad \alpha_ {n + 1} = \alpha_ {n} + \Delta \lambda ,
$$

where 

$$
\boldsymbol {n} _ {n + 1} ^ {\mathrm{tr}} = \frac {\boldsymbol {\sigma} _ {\mathrm{dev} , n + 1} ^ {\mathrm{tr}}}{\left\| \boldsymbol {\sigma} _ {\mathrm{dev} , n + 1} ^ {\mathrm{tr}} \right\|},
$$

and the final stress state $\pmb { \sigma } _ { \mathrm { d e v } , n + 1 }$ is the projection of the trial stress onto the yield surface as 

$$
\boldsymbol {\sigma} _ {\mathrm{dev}, n + 1} = \boldsymbol {\sigma} _ {\mathrm{dev}, n + 1} ^ {\mathrm{tr}} - \Delta \lambda \hat {g} 2 \mu \sqrt {\frac {3}{2}} \boldsymbol {n} _ {n + 1} ^ {\mathrm{tr}}.
$$

The above return mapping closely resembles the standard return mapping of $J _ { 2 } – \mathrm { p l a s t i c i t y }$ with linear isotropic hardening from which it only differs for the presence of $\hat { g }$ in some of the equations. The same equations are obtained for the models in Table 1 and Table 2, the only difference being in the definition of ${ \hat { g } } .$ . However, for the model of Table 1, the above results are valid within a staggered implementation where s and $p$ are frozen while solving the momentum equation. Should we let $p$ evolve with $\pmb { \varepsilon } ^ { \mathrm { p } }$ (i.e. should $p$ belong to group A in Figure 5), the return mapping would assume a more complicated non-linear form, for which a local numerical iterative solution would be needed. 

## 5 Numerical examples

We now investigate through several examples the ability of the proposed approach to capture representative aspects of the fracture processes in ductile materials. In the first two examples (an I-shaped specimen and an asymmetrically notched specimen), we aim at illustrating the effect on the numerical predictions of the proposed coupling between the phase field and the equivalent plastic strain. Moreover, we also assess the role of the critical equivalent plastic strain. In the third example we investigate notched specimens with two different notch radii, and test the ability of the model to predict the experimentally observed influence of the notch radius on the fracture pattern. In the subsequent single edge tension/shear test we focus on the effect of the loading angle on results. Finally, we illustrate for completeness two additional problems, namely a double notched specimen and a compact tension specimen. 

All numerical computations are performed within the finite element framework using fully integrated 4-node quadrilateral elements and assuming plain strain conditions, with the material properties shown in Table 3. Displacement controlled conditions are always assumed. We adopt the staggered solution strategy presented in Sect. 4.1. 

## 5.1 I-shaped specimen

To gain the first insight into the performance of the model, we analyze a tensile test on an I-shaped specimen, with the geometric properties and boundary conditions shown in Fig. 6. A vertical displacement is applied to the top edge, which 


Table 3 Material parameters used in the numerical simulations [20]


<table><tr><td>Properties</td><td>Material I</td><td>Material II</td></tr><tr><td>Shear modulous</td><td>27,280 MPa</td><td>70,300 MPa</td></tr><tr><td>Bulk modulus</td><td>71,660 MPa</td><td>1,36,500 MPa</td></tr><tr><td>Yield stress</td><td>345 MPa</td><td>443 MPa</td></tr><tr><td>Hardening modulus</td><td>250 MPa</td><td>300 MPa</td></tr><tr><td>Fracture toughness</td><td>9.31 MPa mm</td><td>20.9 MPa mm</td></tr></table>

is restrained horizontally, whereas the bottom edge is completely fixed. The material parameters are those of Material I in Table 3, moreover we assume $\ell { = } 0 . 2$ mm and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 1 0 \%$ A uniform mesh with 8847 quadrilateral elements is first used in order to eliminate any mesh-related effects. For specimens in plane strain conditions, the experimental evidence shows that the crack forms in the middle of the specimen with an inclination of about $\pm 4 5 ^ { 0 }$ with respect to the major principal stress direction [54]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/d62ea52838d33f6eaae34fd1ff36494f8ac2561708aa5d9cf09a46b8796dfa96.jpg)



Fig. 6 I-shaped specimen. Geometry and boundary conditions [31]. Dimensions in mm


First, we compare the predictions of the proposed model with those of its uncoupled counterpart. For both models, Fig. 7a shows the equivalent plastic strain field at incipient cracking, whereas Fig. 7b–e illustrate the evolution of the crack phase field from incipient cracking to complete failure. The stages indicated in the diagram correspond to the points labeled accordingly in the load–displacement curves of Fig. 8. With the uncoupled model, the first crack appears at one of the notches, i.e. at the location of the elastic stress concentration, and then gradually propagates towards the center. Conversely, according to the proposed model the evolution of the crack phase field is driven by the plastic strain localization which takes place in the middle of the specimen. Therefore, this is also the location of the first crack. As the localized damage band bifurcates into two inclined branches, the crack propagates by following one of the two directions with a consequent loss of symmetry. Failure occurs when the boundary of the specimen is reached. Unlike those of the uncoupled model, predictions of the proposed model correctly reproduce the experimental evidence described in [54]. 

Next, we assess the effect of the critical equivalent plastic strain on the model predictions. Here we refine the mesh in the central region of the specimen where crack propagation 

Fig. 7 I-shaped specimen. a Equivalent plastic strain field at the onset of cracking and b–e crack phase field at various fracture stages (see labels in Fig. 8). Red corresponds to damaged and blue to undamaged material. (Color figure online) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/50cfc14d9af71ceca73de959c826b4a9e662e40c06c59be7aef284aa74ae2391.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/863d9358df5dddce81e6ba65a81294c5fce7ee4bdcaf4d991e3efdf513b872a5.jpg)



Fig. 8 I-shaped specimen. Load–displacement curves


Fig. 9 I-shaped specimen. Effect of $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ on the fracture process. a–d Crack phase field at various fracture stages (see labels in Fig. 10) and e equivalent plastic strain field at the final stage 

is expected, so that the mesh now contains 10,499 quadrilateral elements. The effect of $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ on the crack path and on the load–displacement curve is shown respectively in Figs. 9 and 10. It can be observed that a change in $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ does not affect the fracture process in terms of crack path but influences the load bearing capacity. Finally, the influence of the length scale parameter  on crack path and load– displacement behavior is shown respectively in Figs. 11 and 12 for $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 1 0 \%$ 

## 5.2 Asymmetrically notched specimen

We now examine the asymmetrically notched specimen illustrated in Fig. 13. The top edge is restrained horizontally and displaced vertically, whereas the bottom edge is fixed. The material parameters are those of Material I in Table 3, 

# 0.14 eq,crit =10 % 0.08 10.2 0.24 p =20 % (a) (b) (c) (d)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/ecdaa0b3ab9660ff9e258817a2ba70b20959811efb4a5724a3be56d54374c0d7.jpg)



Fig. 10 I-shaped specimen. Effect o $\cdot _ { \varepsilon _ { \mathrm { q } , \mathrm { c r i t } } }$ on the load–displacement curve


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/1b39b02c9ca45aa018f61bc446fdfd0bc927448fde1b97fe63fea2983a8172f4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/72618adebbf889b615500b2ec7e8b7bdb1fed14a194ced6ff958cfcad903a555.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/95ed49f665c71acd502a662f531ec535516469e1eb9efe13b78ce26f8403f51e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/790513556c97724167a41f99e449368af5693c71057b7c34fed3ebdb64655e8a.jpg)



Fig. 11 I-shaped specimen. Effect of  (mm) on the fracture process. a1–c2 Crack phase field at the initial and final fracture stages and d equivalent plastic strain field at the final stage


in addition to =0.08 mm and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 1 0 \ \%$ . The spatial discretization of the model comprises 10,800 quadrilateral elements, with refinement in the central region between the notches where the crack is expected to form. 

The evolution of the equivalent plastic strain and crack phase fields is provided in Fig. 14 for both the uncoupled and the proposed models. As expected, the equivalent plastic strain is maximum at both notch roots and localization branches form between the notches at an angle of about $4 5 ^ { \circ }$ dictated by the specific geometry. Both models are able to predict crack initiation at the notches. However, during the subsequent stages, the standard model predicts the initial cracks to propagate sub-horizontally towards the center of the specimen, leading to a final crack pattern which deviates from the region ofplastic strain localization. Conversely, with the proposed model the initial cracks propagate within the plastic strain localization band and eventually merge leading to complete failure. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/d0a2facd71891c1bf1d07180761bffaf5e6f7ff146770c154c17035b01f20a14.jpg)



Fig. 12 I-shaped specimen. Effect of (mm) on the load–displacement curve



Fig. 13 Asymmetrically notched specimen. Geometry and boundary conditions. Dimensions in mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/ff945db064f53d075d291fdff8c36882bac58f276d0b70dba1ab55be5ba023df.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/14eb513196576fd1f4b1e355bd8276d896f4ce8c60127eb2629e8617eb97b876.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/cae0b9425a3c219732ec202176a5a787c5a0051a68ea3e0bfe4203bebc9773c8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/962bf0c2db1cde47b6a612068e49aad9fbe36a52553f69bdb586d24b1cdd3f25.jpg)



Fig. 14 Asymmetrically notched specimen. a1–c1 Equivalent plastic strain field and a2–c2 crack phase field at various fracture stages


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/94e8eb691631e9b20c079cc2efbe9c67492e17d960d1c7ce3d51046745c35fbf.jpg)



Fig. 15 Asymmetrically notched specimen. Effect of $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ on the fracture process. a1–c1 Equivalent plastic strain field and a2–c2 crack phase field at various fracture stages (see labels in Fig. 16)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/53c936b6f60ba0cd7ac977e09b64de7e5336b4630fa4630b69dd802d8e8b2da0.jpg)



Fig. 16 Asymmetrically notched specimen. Effect of $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } }$ on the load–displacement curve


The effect of the critical equivalent plastic strain on results in terms of crack path and load–displacement curve is evaluated respectively in Figs. 15 and 16. As for the previous example, the crack path is not appreciably influenced, whereas the fracture branch of the load–displacement curve corresponds to increasing values of displacement for increasing $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } ^ { \mathrm { - } } }$ . Additionally, the role played by the exponent m in the coupling term $p ^ { m }$ is investigated in Figs. 17 and 18 with $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 1 2 \ \bar { \% }$ . As the order m increases, the inclination of the incipient crack pattern increasingly follows the direction of the plastic strain localization band, whereas the fracture branch ofthe load–displacement curve becomes more abrupt. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/5867815cd2e306e59bbf187696c8696796bd9e097f85f74e59847475407a41f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/8b2aff197ace5083adf5763186a8c426ff7dda7eb3fee467f182a8f6f11a1ef0.jpg)



Fig. 17 Asymmetrically notched specimen. Effect of the order m on the fracture process. a1–c1 Equivalent plastic strain field and a2–c2 crack phase field at various fracture stages (see labels in Fig. 18)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/c4b7ae9ea7aa5388c0918235057faa58b42b9bc08991696957cfd65fe551bb09.jpg)



Fig. 18 Asymmetrically notched specimen. Effect of the order m on the load–displacement curve



Fig. 19 Asymmetrically notched specimen. Effect of the mesh size (5459, 10,800 and 15,394 elements) on the fracture process. (a-c)(1-2) Crack phase field at the initial and final fracture stages (see labels in Fig. 20)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/8139c3cb791fa297fd5f12d4e16f17b8c3f4909151839254bc5d1c290a6f34b6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/caa63e1a8740558ba16298be806806635969ae1c526f33f107662cbafb160370.jpg)



Fig. 20 Asymmetrically notched specimen. Effect of the mesh size (5459, 10,800 and 15,394 elements) on the load–displacement curve


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/b01528a3153326d9b15e5c8d928f89e46e3ab3a8c7186ee2d6c2ad5c78d21618.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/b425832ba019b5726aa62a651c7f0ee977499bd458ccc6cefdace6d3c2a2cb6d.jpg)



Fig. 21 Notched specimens. Dimensions in mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/95675084e3ca4e45670a49e681f9b34c99559db2de4900c6f3640efbff4c1e63.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/9dd21529a22f1b67a37218a87f5e9d12d3b2fa28f74bb9bea192d3a47344b8b8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/06da5668240859445b885d3a22d271a5b0d0805675e01d303f27f9af3fbe53b2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/4fd2fc74411179ffbcc8226c7fc2012c7b92b5153ac2a30a9a401558f50ef759.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/06fd22243f961b9a6dc93289e93303ec34e78825f6d1b7e17ce7657fd5a96157.jpg)



Fig. 22 Notched specimens. Effect of the notch radius on the fracture process. a1–c1 Equivalent plastic strain field and a2–c2 crack phase field at various fracture stages (see labels in Fig. 23)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/c94889f632326c2a78f72c7131b5e44d5b9befa98cab267df0f5040baaf2af0a.jpg)



Fig. 23 Notched specimens. Effect of the notch radius on the load– displacement curves


Results for $m = 2$ and $m = 3$ are however quite similar. Finally, Fig. 19 focuses on the effect of the mesh size on the fracture pattern, with the corresponding load–displacement curves reported in Fig. 20. For all discretizations the model delivers similar initial and final crack shapes, however the finest mesh resolves the crack profile most accurately. As visible in Fig. 20, the decreasing branch appears smoother for the finest discretizations. Convergence of the results as the mesh is refined is also evident. 

## 5.3 Notched specimens

In this example, we aim at reproducing the experimental evidence that, in tensile tests on notched specimens, the crack initiates at the notch root or in the middle of the specimen depending on the notch radius [56]. We thus examine two notched specimens with different notch radii and investigate the failure mechanisms predicted by the model. The geometry and boundary conditions of the problem are illustrated in Fig. 21, whereas the material parameters are those of Material I in Table 3, as well as =0.08 mm and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 1 0$ %. A discretization with 10,713 (specimen with notch radius of 5 mm) and 10,142 (specimen with notch radius of 2.5 mm) elements is used with local mesh refinement between the notches. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/a73728edb187cadba2be5cdc96ef1c03ea707e540a6a4e2da758d3450d88d206.jpg)



Fig. 24 Single-edge notched tension/shear test. Geometry and boundary conditions [53]. Dimensions in mm


Figure 22 reports the evolution of the equivalent plastic strain field and of the crack phase field at three loading stages whereas the load–deflection curves are given in Fig. 23. For a notch radius of 5 mm, the model predicts crack initiation at the center of the specimen, followed by formation of two shear bands at an angle of about $\pm 4 5 ^ { \circ }$ to the loading direction and by crack propagation along one of the two directions. Conversely, for the specimen with the smallest notch radius the crack initiates at the notch roots, where the largest plastic strain occurs. Subsequently, we observe an unsymmetric crack propagation from the notches inward, and at the same time the initiation of an additional inclined crack slightly offset from the middle of the specimen. Merging of all these cracks leads to final failure. Interestingly, the different crack pattern for the two notch radii is associated to a significantly different load–displacement behavior, the specimen with the larger notch radius failing more abruptly than the other one. 

## 5.4 Single-edge notched tension/shear test

In [20,53,57,58] the single-edge notched test is investigated in detail, both experimentally and numerically, for different 


Fig. 25 Single-edge notched tension/shear test. $\bar { \beta } = 9 0 ^ { 0 }$ . a–c Equivalent plastic strain field and crack phase field at various fracture stages (see labels in Fig. 28)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/1591fe3d1e860f4e8deb3b3e16ddd1ddf9dc880077f36760e90d2714812bd3d9.jpg)



Fig. 26 Single-edge notched tension/shear test. $\beta = 0 ^ { 0 }$ . a–c Equivalent plastic strain field and crack phase field at various fracture stages (see labels in Fig. 28)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/6775eff552ed36b72ce6700cd1b6b26eeac72de6b117314fadd28c95316c03d4.jpg)



Fig. 27 Single-edge notched tension/shear test. $\bar { \beta } = 4 5 ^ { 0 }$ . a–c Equivalent plastic strain field and crack phase field at various fracture stages (see labels in Fig. 28)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/90a425c0eb0300ca95fb6e9e0c9387f4b7f7287175610f280bdbefa7db112c9f.jpg)



(a)


values of the loading angle β (Fig. 24). Experiments [57] and numerical simulations [53] agree in predicting mode-I crack growth for $\beta = 3 0 ^ { \circ } \le \beta \le 9 0 ^ { \circ }$ and mode-II for $\beta = 1 5 ^ { \circ }$ and $\beta = 0 ^ { \circ }$ 

Here we perform the same investigation to compare predictions of the proposed phase-field model with the aforementioned results. The geometric properties and bound ary conditions of the specimen are shown in Fig. 24. The material parameters are those of Material II in Table 3, moreover $\ell { = } 0 . 0 5$ mm and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 1 0 ~ \%$ . Loading is applied at three different angles (namely, 90<sup>◦</sup>, 0<sup>◦</sup> and 45<sup>◦</sup>) to obtain different modes of fracture. The spatial discretization contains 10,600 $( \beta ~ = ~ 9 0 ^ { \circ } )$ , 10,262 $( \beta = 0 ^ { \circ } )$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/084e2b29322a868c5a7d67b4f4501b867614857b481826015891cef04a76ac9a.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/cb080ba2b0a161aba4f1090c7aebbb2414d7e7c3610928c1d93d88fac26e3256.jpg)



(c)



and 19,256 $( \beta \ ) \ = \ 4 5 ^ { \circ } )$ quadrilateral elements with a refinement in the region where the crack is expected to form.



Figures 25, 26 and 27 depict the evolution ofthe equivalent plastic strain field and of the corresponding crack phase field at several stages of loading. In pure mode I $( \beta = 9 0 ^ { \circ } )$ as well as in mode-II $( \beta = 0 ^ { \circ } )$ the crack propagates horizontally. A bending upwards of the crack from the initial tip occurs for a loading angle $\beta = 4 5 ^ { 0 }$ . A phenomenon that is observed in these simulations is that the plastic strain localization takes place mainly in front of the crack tip which results in a stable crack propagation. The load–displacement curves are given in Fig. 28 for all loading angles.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/24ee042a6c4e8138812a46a088ea25eac9c61fd79bc75771f3a8c5174db0fd07.jpg)



Fig. 28 Single-edge notched tension/shear test. Effect of the loading angle on the load–displacement curve


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/953f52440b1ceefa518d61d1440114bf656b8059f571a3269b69bef35e9d8788.jpg)



Fig. 29 Double notched specimen. Geometry and boundary conditions [20]. Dimensions in mm


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/8ab2d63ef12d00e8f59f3c39baa12407ea46b710cf09cbdd31719e0ec5d644e0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/0680833b4669f81d18060aaa711907ab40bfe805b2a40453f3bec377277704d6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/69ecff6eb85675be901a4d0c9c574525ff07e154fdd4d8630d34fee84ec9f01e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/a748b83dd114d6b60307d27929bf31425bc80d73e2923f0bdebf021998f268b6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/6e9fa8eaeefd87e6116162f1fa279d7c8be967e891993827ed7a5bc04eecdccf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/9b5fe2c9d2e0caec68e77c0f5caa94d2eeb715a9decf81422b5dc057ba358a15.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/939a19f4a59ac4f9bafb1020924cb1a6299579573d5e6e4dc9f13c8fe32335e4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/9bb7953c7183095bfcb611399059f13fbd7c232e40d0a867bb6ac5e2b9815b35.jpg)



(d1)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/93ed9ba930637ffae35da4b261e4451dc0d895ed1995cf34d4eac153f968bd1d.jpg)



(a2)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/fec58bd9420ffd0e8995b6225600e2432862ca41031ad7a2c8c6eae23ade679d.jpg)



(b2)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/007006297f716589b0915da0c771626bffd6e9e3a2f483c996263aa8c29bfe33.jpg)



(c2)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/9ffe906f9ffec8301f7f1b6101b777c95ef390234e3cd70a34f06a8408e15d5d.jpg)



(d2)



Fig. 30 Double notched specimen. a–d Equivalent plastic strain field and crack phase field at various fracture stages (see labels in Fig. 31)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/68b18a9f9d8b860029aff01bc4a2b815ca4dadc077c59de0d09b896a1f5bc507.jpg)



Fig. 31 Double notched specimen. Effect of p on the load– displacement curve


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/1afcd9abc9cc95daa7cf6b39d9694c89359d94331059d16644c31b453958c1d7.jpg)



Fig. 32 CT specimen. Geometry and loading conditions [55]. Dimensions in mm


## 5.5 Double notched specimen

In this example, we model a double notched specimen with a vertical displacement imposed to the top edge and left edge. 


Fig. 33 CT specimen. a–d Equivalent plastic strain field and crack phase-field at various fracture stages (see labels in Fig. 34)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/fd6481600b1a33c005445d873f9686a7fa0175d1eb549071ecb3532f66954cc9.jpg)


These edges are both restrained horizontally, whereas the bottom and right edges are fixed, as illustrated in Fig. 29. In the context of ductile fracture, the same problem has been addressed in [20] using a non-local damage model for the initial continuum damage phase, followed by a discontinuous crack propagation phase predicted through a remeshing strategy. Results showed the development of a plastic shear band diagonally across the specimen, which in turn results in a curved crack trajectory which initiates at both the notches and propagates towards the center of the specimen where the two crack branches merge (Fig. 30). 

The material parameters are those ofMaterial II in Table 3, also it is =0.03 mm and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } = 2 5$ %. The adopted discretization contains 10,300 quadrilateral elements with mesh refinement in the expected crack propagation region. 

Figure 30 shows the evolution of equivalent plastic strain and the corresponding crack phase field at several stages of fracture process. The load-deflection curves are shown in Fig. 31. The obtained behavior is in very good agreement with the results in [20]. 

## 5.6 Compact tension (CT) specimen

Finally, we model crack initiation and propagation for a CT specimen. The geometry and boundary conditions are shown in Fig. 32. The specimen contains an horizontal notch at its mid-height, and load is applied by a top pin which is displaced vertically, whereas the lower pin is fixed. The material parameters are those of Material I in Table 3, additionally =0.09 mm and $\varepsilon _ { \mathrm { e q , c r i t } } ^ { \mathrm { p } } { = } 5 \ \%$ . The mesh comprises 10,097 quadrilateral elements with refinement in the areas where the crack is expected to form. 

The results are shown in Figs. 33 and 34. It can be observed as the plastic deformations concentrate ahead of the notch (and later of the crack) tip, forming what can be considered as a plastic hinge. Accordingly, an horizontal crack propagates inward from the notch tip and, at the last stage, a secondary crack starts from the left edge of the specimen until failure results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/3442107fe27b0285086da041f5a0c80126b4fb886a7275e540e07ee21ef1ac13.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/4b27164dc2bf31b42c668e79c83c179f79ad48c56ae02e3b4d7408a66170af49.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/5589144ed5bad5cb04a7ee9c907ed0549c1f373ee1955fab3cebe5669d72cdf4.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/def3b9df-9b96-4a6a-93df-b7304b5026dc/dadc6f1b33ef8f9993a6494c0f67c2e107f1b6bb8a8d463f2e68e9c8fd5261a1.jpg)



Fig. 34 CT specimen. Load–displacement curve


## 6 Conclusions

In this paper, we proposed a new phase-field model for ductile fracture in elasto-plastic solids, within the quasi-static kinematically linear regime. The distinct feature of the model is that it couples the evolution of the crack phase field with the accumulation of the plastic strains in a thermodynamically consistent way. As demonstrated by several numerical examples, this coupling enables the formulation to predict the initiation of fracture in the regions of plastic strain localization, in agreement with the experimental evidence. As a result, the model is able to predict several features of the phenomenology of quasi-static ductile fracture, including the shape and location of the crack pattern in a tensile specimen, the role played by the notch radius in notched specimens, and the change in fracture mode with the inclination of the applied load. With respect to brittle phase-field models, the proposed ductile fracture model includes two additional parameters, a threshold equivalent plastic strain and an exponent in the coupling function, which can facilitate the quantitative prediction of test results. While requiring further investigations, including e.g. the extension to the three-dimensional large deformation framework, the study of volumetric locking effects and a thorough experimental validation, the proposed model appears a very promising tool for the investigation of ductile fracture within the phase-field framework. Overall, this framework seems to be the ideal candidate to unify the prediction of diffuse ductile damage and (within the diffusive approximation) of discrete crack propagation, thus overcoming the difficulties of many other approaches. 

Acknowledgments This research was funded by the European Research Council, ERC Starting Researcher Grant INTERFACES, Grant Agreement N. 279439. 

## Appendix

## Perturbation analysis for the s and p mutual interaction

One of the most important aspects in our phase-field model of elasto-plastic ductile fracture is the coupling function $g ( s , p ) : = s ^ { 2 p }$ . Introduction of the exponent p, which accounts for the accumulation and localization of plastic strains, into the classic brittle-case function $g ( s ) = s ^ { 2 }$ allows us to let s explicitly depend also on the plastic energy density $\Psi _ { \mathrm { p } } .$ , and not only on the elastic one, $\Psi _ { \mathrm { e } } .$ . This can be formally seen from the corresponding evolution equation for s (25). More importantly, we show below that the evolution of s in this case will mainly be governed by $p \sim \Psi _ { \mathsf { p } }$ rather than $\Psi _ { \mathrm { e } }$ , thus delaying the brittle-like fracture development and enabling the desired plastic-driven fracture mechanism. 

Without loss of generality, we restrict ourselves to the pure tensile loading situation so that no split of the elastic energy density function $\Psi _ { \mathrm { e } }$ is required and the evolution equation for s is given by 

$$
- 4 \ell^ {2} \Delta s + s + \frac {4 \ell}{G _ {c}} \Psi_ {\mathrm{e}} (\pmb {\varepsilon}) p s ^ {2 p - 1} = 1.\tag{31}
$$

Equation (31) is a non-linear partial differential equation whose explicit analytical solution for s is out ofreach: one can only conclude that with $p \equiv 0$ (zero plastic strains), a trivial solution is s = 1 (no phase-field development occurs). With a suitable rescaling of variables (i.e. non-dimensionalization), one can obtain a dimensionless version of (31) containing a small (perturbation) parameter. An approximate analytical solution of such perturbed non-linear equation can then be constructed explicitly, establishing a relation between s and $p .$ 

Let L be the maximal macroscopic dimension of the considered body. We introduce the following non-dimensional quantities: 

$$
(\bar {x}, \bar {y}) := \left(\frac {x}{L}, \frac {y}{L}\right), \quad \bar {\boldsymbol {u}} := \frac {\boldsymbol {u}}{A}, \quad \bar {\mathbb {C}} := \frac {\mathbb {C}}{E}, \quad \bar {\ell} := \frac {\ell}{\frac {1}{2} L},\tag{32}
$$

where $A > 0$ is a constant whose particular choice will be motivated below. The scaled strain tensor $\bar { \pmb { \varepsilon } } = \frac { 1 } { 2 } ( \bar { \nabla } \bar { \pmb { u } } + \bar { \nabla } \bar { \pmb { u } } ^ { T } )$ , <sub>with</sub> ∇¯ <sub>denoting the gradient w.r.t. the non-dimensional vari-</sub> ables (x¯, y¯), relates to the actual strain tensor ε as 

$$
\boldsymbol {\varepsilon} (\boldsymbol {u}) = \frac {A}{L} \bar {\boldsymbol {\varepsilon}} (\bar {\boldsymbol {u}}),\tag{33}
$$

yielding for $\Psi _ { \mathrm { e } }$ the relation 

$$
\Psi_ {\mathrm{e}} (\boldsymbol {\varepsilon}) = \frac {1}{2} \mathbb {C} \boldsymbol {\varepsilon} ^ {2} = \frac {1}{2} E \bar {\mathbb {C}} \left(\frac {A}{L}\right) ^ {2} \bar {\boldsymbol {\varepsilon}} ^ {2} = E \left(\frac {A}{L}\right) ^ {2} \bar {\Psi} _ {\mathrm{e}} (\bar {\boldsymbol {\varepsilon}}).\tag{34}
$$

Also, we set $\bar { s } : = s$ so that $\begin{array} { r } { \Delta s = \frac { 1 } { L ^ { 2 } } \bar { \Delta } \bar { s } . } \end{array}$ , with $\bar { \Delta }$ standing for the Laplace operator w.r.t. $( { \bar { x } } , { \bar { y } } )$ . Finally, a non-dimensional plastic strain variable is defined as $\overline { { \pmb { \varepsilon } ^ { \mathrm { p } } } } : = \pmb { \varepsilon } ^ { \mathrm { p } }$ leading to the corresponding definition of ${ \bar { p } } \colon$ 

$$
\bar {p} := \frac {\overline {{\varepsilon_ {\mathrm{eq}} ^ {\mathrm{p}}}}}{\varepsilon_ {\mathrm{eq,crit}} ^ {\mathrm{p}}}, \quad \overline {{\varepsilon_ {\mathrm{eq}} ^ {\mathrm{p}}}} (t) := \sqrt {\frac {2}{3}} \int_ {0} ^ {t} \sqrt {\dot {\overline {{\boldsymbol {\varepsilon} ^ {\mathrm{p}}}}} : \dot {\overline {{\boldsymbol {\varepsilon} ^ {\mathrm{p}}}}}}   d \tau .\tag{35}
$$

Note that the denominator remains the same as in the definition of $p .$ 

Using (32)–(35) we turn (31) into 

$$
- \bar {\ell} ^ {2} \bar {\Delta} \bar {s} + \bar {s} + \frac {2 \bar {\ell} L}{G _ {c}} E \left(\frac {A}{L}\right) ^ {2} \bar {\Psi} _ {\mathrm{e}} (\bar {\boldsymbol {\varepsilon}}) \bar {p} \bar {s} ^ {2 \bar {p} - 1} = 1.
$$

In the above, the scaling constant A can be chosen to provide $\begin{array} { r } { \frac { 2 L } { G _ { c } } E \left( \frac { A } { L } \right) ^ { 2 } = 1 } \end{array}$ , that is, $A : = \sqrt { \frac { G _ { c } L } { 2 E } }$ , and the dimensionless counterpart of (31) we end up with reads as 

$$
- \bar {\ell} ^ {2} \bar {\Delta} \bar {s} + \bar {s} + \bar {\ell} \bar {\Psi} _ {\mathrm{e}} (\bar {\pmb {\varepsilon}}) \bar {p} \bar {s} ^ {2 \bar {p} - 1} = 1.\tag{36}
$$

In what follows, we set $\gamma : = { \bar { \ell } }$ and also drop the bars over all remaining variables in (36). This yields 

$$
- \gamma^ {2} \Delta s + s + \gamma \Psi_ {\mathrm{e}} (\pmb {\varepsilon}) p s ^ {2 p - 1} = 1,\tag{37}
$$

where, by definition, γ is a small (perturbation) parameter, that is, $0 < \gamma \ll 1$ 

According to the perturbation analysis framework [59], an asymptotic expansion of s is taken in a form of a power series in $\gamma \colon$ 

$$
s = s _ {0} + \gamma s _ {1} + \gamma^ {2} s _ {2} + \dots ,\tag{38}
$$

what yields for $\Delta s$ and $s ^ { 2 p - 1 }$ the expansions 

$$
\Delta s = \Delta s _ {0} + \gamma \Delta s _ {1} + \gamma^ {2} \Delta s _ {2} + \dots ,\tag{39}
$$

and 

$$
\begin{array}{c} s ^ {2 p - 1} = s _ {0} ^ {2 p - 1} + \gamma (2 p - 1) s _ {0} ^ {2 p - 2} s _ {1} \\ \qquad + \gamma^ {2} (2 p - 1) s _ {0} ^ {2 p - 3} \left(s _ {0} s _ {2} + s _ {1} ^ {2} (p - 1)\right) + \dots , \end{array}\tag{40}
$$

respectively. In (39) and (40), only the terms up to order $O ( \gamma ^ { 2 } )$ have been retained, consistently with the assumed expansion (38). We now substitute (38)–(40) into the governing equation (37) and collect the coefficients of like powers of $\gamma$ to obtain: 

$$
\begin{array}{l} s _ {0} + \gamma \left(s _ {1} + p \Psi_ {\mathrm{e}} s _ {0} ^ {2 p - 1}\right) \\ \quad + \gamma^ {2} \left(- \Delta s _ {0} + s _ {2} + p (2 p - 1) \Psi_ {\mathrm{e}} s _ {0} ^ {2 p - 2} s _ {1}\right) + \dots = 1. \end{array}\tag{41}
$$

Equating the coefficients of each power of $\gamma$ to zero we ’extract’ the equations for $s _ { 0 } , s _ { 1 }$ and $s _ { 2 }$ . The corresponding solutions are 

$$
s _ {0} = 1, \quad s _ {1} = - p \Psi_ {\mathrm{e}}, \quad s _ {2} = p ^ {2} (2 p - 1) \Psi_ {\mathrm{e}} ^ {2},\tag{42}
$$

and, due to (38), we finally obtain 

$$
s = 1 - \gamma p \Psi_ {\mathrm{e}} + \gamma^ {2} p ^ {2} (2 p - 1) \Psi_ {\mathrm{e}} ^ {2} + \dots ,\tag{43}
$$

to be treated as an approximate analytical solution ofequation (37). Note that with $\gamma  0 .$ , equation (37) reduces to $s = 1$ Sending γ to zero also in (43), we recover the same result, i.e. $s = 1$ , as expected. Recall also that setting $p = 0 \mathrm { i n } ( 3 7 )$ the trivial solution of the reduced equation is $s = 1$ . Similar result is obtained while substituting $p = 0$ in (43). 

From (43) the influence of $p$ on the phase-field s can be grasped. In the linear elastic regime (no plastic strains, $p = 0 )$ and at the beginning of the plastic regime (plastic strains are still negligibly small, $0 ~ < ~ p ~ \ll ~ 1 )$ , the evolution of s is minor even with a (possibly large) non-zero contribution of $\Psi _ { \mathrm { e } } .$ . In other words, the presence of p in $g ( s , p ) = s ^ { 2 p }$ delays the brittle-like fracture formation. This is in a contrast to the brittle phase-field formulation, when the use of $g ( s ) = s ^ { 2 }$ results in s depending solely on $\Psi _ { \mathrm { e } }$ (expansion (43) with $p \equiv$ 1) meaning that the crack development occurs independently of the evolution of the plastic strains. 

## Proof of thermodynamic consistency

In this Appendix, the governing equations of the proposed model are rewritten in the framework of the principle of virtual power as developed by Gurtin, see [60,61], and their thermodynamic consistency is investigated. 

## Kinematics

The kinematics is based on the decomposition of the displacement gradient into elastic and plastic components $\nabla \mathbf { u } =$ $\mathbf { H } ^ { \mathrm { e } } + \mathbf { H } ^ { \mathrm { p } }$ . Correspondingly, we define the elastic and plastic strain tensors as 

$$
\boldsymbol {\varepsilon} ^ {\mathrm{e}} = \frac {1}{2} \left(\mathbf {H} ^ {\mathrm{e}} + \mathbf {H} ^ {\mathrm{e} T}\right) \quad \boldsymbol {\varepsilon} ^ {\mathrm{p}} = \frac {1}{2} \left(\mathbf {H} ^ {\mathrm{p}} + \mathbf {H} ^ {\mathrm{p} T}\right)\tag{44}
$$

so that the total strain tensor is given by $\pmb { \varepsilon } = \pmb { \varepsilon } ^ { \mathrm { e } } + \pmb { \varepsilon } ^ { \mathrm { p } }$ . Finally, we assume that $\mathbf { H } ^ { \mathrm { p } }$ is purely deviatoric, i.e. tr $\mathbf { H } ^ { \mathrm { p } } = \mathrm { t r } \pmb { \varepsilon } ^ { \mathrm { p } } = 0$ 

Balance equations 

Let us introduce the internal power in the form 

$$
\begin{array}{l} \mathcal {I} (P) = \int_ {P} \boldsymbol {\sigma} ^ {\mathrm{e}}: \dot {\mathbf {H}} ^ {\mathrm{e}} d v + \int_ {P} \boldsymbol {\sigma} ^ {\mathrm{p}}: \dot {\mathbf {H}} ^ {\mathrm{p}} d v + \int_ {P} \boldsymbol {\xi} \cdot \nabla \dot {s} d v \\ \quad + \int_ {P} \zeta \cdot \dot {s} d v \end{array}\tag{45}
$$

where $\pmb { \sigma } ^ { \mathrm { e } }$ and ${ \pmb { \sigma } } ^ { \mathrm { p } }$ are respectively an elastic stress, powerconjugate to $\dot { \bf H } ^ { \mathrm { e } }$ , and a plastic stress, power-conjugate to $\dot { \mathbf { H } } ^ { \mathrm { p } }$ Since $\mathbf { H } ^ { \mathrm { p } }$ is deviatoric, we may assume without loss of generality that ${ \pmb { \sigma } } ^ { \mathrm { p } }$ is deviatoric, i.e. that $\operatorname { t r } \pmb { \sigma } ^ { \mathrm { p } } = 0$ . Moreover, ξ is the microscopic stress power-conjugate to ∇ ˙s, and ζ is the microscopic internal body force power-conjugate to ${ \dot { s } } ,$ where s is the crack field parameter, $0 \leq s \leq 1$ . The integration domain is any subregion $P$ of the body under consideration. The external power is given by 

$$
\begin{array}{l} \mathcal {W} (P) = \int_ {\partial P} \boldsymbol {t} (\boldsymbol {n}) \cdot \dot {\boldsymbol {u}} d a + \int_ {P} \boldsymbol {b} \cdot \dot {\boldsymbol {u}} d v \\ \qquad + \int_ {\partial P} \chi (\boldsymbol {n}) \dot {s} d a + \int_ {P} \gamma \dot {s} d v \end{array}\tag{46}
$$

where t is the traction vector on the elementary area da of the surface of P, ∂ P, with outward unit normal n, b is the body force, χ and γ are respectively the microscopic external traction and the microscopic external body force, both powerconjugate to s˙. Considering a generalized virtual velocity 

$$
\mathcal {V} = \left(\tilde {\boldsymbol {u}}, \tilde {\mathbf {H}} ^ {\mathrm{e}}, \tilde {\mathbf {H}} ^ {\mathrm{p}}, \tilde {s}\right)\tag{47}
$$

satisfying the kinematical constraints above, the principle of virtual power reads 

$$
\begin{array}{l} \int_ {P} \boldsymbol {\sigma} ^ {\mathrm{e}}: \tilde {\mathbf {H}} ^ {\mathrm{e}} d v + \int_ {P} \boldsymbol {\sigma} ^ {\mathrm{p}}: \tilde {\mathbf {H}} ^ {\mathrm{p}} d v + \int_ {P} \boldsymbol {\xi} \cdot \nabla \tilde {s} d v + \int_ {P} \zeta \cdot \tilde {s} d v \\ = \int_ {\partial P} t (\boldsymbol {n}) \cdot \tilde {\boldsymbol {u}} d a + \int_ {P} \boldsymbol {b} \cdot \tilde {\boldsymbol {u}} d v + \int_ {\partial P} \chi (\boldsymbol {n}) \tilde {s} d a + \int_ {P} \gamma \tilde {s} d v \end{array}\tag{48}
$$

for any subregion $P$ of the body and any . Frame invariance implies that $\pmb { \sigma } ^ { \mathrm { e } }$ is symmetric, therefore $\pmb { \sigma } ^ { \mathrm { e } } : \tilde { \mathbf { H } } ^ { \mathrm { e } } = \pmb { \sigma } ^ { \mathrm { e } } : \tilde { \pmb { \varepsilon } } ^ { \mathrm { e } }$ 

Applying Eq. (48) with $\mathcal { V } = ( \tilde { \pmb { u } } , \nabla \tilde { \pmb { u } } , \mathbf { 0 } , 0 )$ leads to the macroscopicforce balance divσ+b = 0 and to the expression ofthe macroscopic traction t $\mathbf { \Pi } ( n ) = \pmb { \sigma } \cdot \pmb { n }$ , where we have introduced $\pmb { \sigma } : = \pmb { \sigma } ^ { \mathrm { e } }$ as the (standard) Cauchy stress. Considering next a virtual velocity ${ \boldsymbol { \nu } } = \left( \mathbf { 0 } , - \tilde { \mathbf { H } } ^ { \mathrm { p } } , \tilde { \mathbf { H } } ^ { \mathrm { p } } , 0 \right)$ delivers the plastic microscopic force balance [61], $\pmb { \sigma } _ { d e v } \overset { \cdot } { = } \pmb { \sigma } ^ { \mathrm { p } }$ , where $\pmb { \sigma } _ { d e v }$ is the deviatoric component of the stress tensor. Note that thus also ${ \pmb { \sigma } } ^ { \mathrm { p } }$ is symmetric, therefore $\pmb { \sigma } ^ { \mathrm { p } } : \tilde { \mathbf { H } } ^ { \mathrm { p } } = \pmb { \sigma } ^ { \mathrm { p } } : \tilde { \pmb { \varepsilon } } ^ { \mathrm { p } }$ . Finally, insertion in Eq. (48) of a virtual velocity $\mathcal { V } = ( \mathbf { 0 } , \mathbf { 0 } , \mathbf { 0 } , \tilde { s } )$ yields 

$$
\int_ {P} \boldsymbol {\xi} \cdot \nabla \tilde {s} d v + \int_ {P} \zeta \cdot \tilde {s} d v = \int_ {\partial P} \chi (\boldsymbol {n}) \tilde {s} d a + \int_ {P} \gamma \tilde {s} d v.\tag{49}
$$

Through the divergence theorem, Eq. (49) leads to thephasefield microscopic force balance 

$$
\operatorname{div} \boldsymbol {\xi} - \zeta + \gamma = 0\tag{50}
$$

and to the expression of the phase-field microscopic traction $\chi \mathbf { \Psi } ( \pmb { n } ) = \pmb { \xi } \cdot \pmb { n }$ 

As a consequence of the above, and if we further introduce the codirectionality constraint valid for $J _ { 2 }$ plasticity, $\begin{array} { r } { \frac { \dot { \pmb { \varepsilon } } ^ { \mathrm { p } } } { \lVert \dot { \pmb { \varepsilon } } ^ { \mathrm { p } } \rVert } = } \end{array}$ ${ \pmb n } ^ { \mathrm { p } }$ with $\begin{array} { r } { n ^ { \mathrm { p } } = \frac { \pmb { \sigma } _ { d e v } } { \parallel \pmb { \sigma } _ { d e v } \parallel } } \end{array}$ , the power balance takes the final form 

$$
\begin{array}{l} \int_ {P} \boldsymbol {\sigma}: \dot {\boldsymbol {\varepsilon}} ^ {\mathrm{e}} d v + \int_ {P} \tau^ {\mathrm{p}} \dot {e} ^ {\mathrm{p}} d v + \int_ {P} \boldsymbol {\xi} \cdot \nabla \dot {s} d v + \int_ {P} \zeta \cdot \dot {s} d v \\ = \int_ {\partial P} t (\boldsymbol {n}) \cdot \dot {\boldsymbol {u}} d a + \int_ {P} \boldsymbol {b} \cdot \dot {\boldsymbol {u}} d v + \int_ {\partial P} \chi (\boldsymbol {n}) \dot {s} d a + \int_ {P} \gamma \dot {s} d v, \end{array}
$$

where 

$$
\tau^ {\mathrm{p}} := \left\| \boldsymbol {\sigma} _ {d e v} \right\|, \quad \dot {e} ^ {\mathrm{p}} := \left\| \dot {\boldsymbol {\varepsilon}} ^ {\mathrm{p}} \right\| \geq 0, \quad e ^ {\mathrm{p}} (t) = \int_ {0} ^ {t} \left\| \dot {\boldsymbol {\varepsilon}} ^ {\mathrm{p}} \right\| d \tau\tag{51}
$$

## Dissipation inequality and constitutive laws

Based on the formulation in Sect. 1, the dissipation inequality can be written (in local form) as 

$$
\dot {E} _ {\ell} - \pmb {\sigma}: \dot {\pmb {\varepsilon}} ^ {\mathrm{e}} - \tau^ {\mathrm{p}} \dot {e} ^ {\mathrm{p}} - \pmb {\xi} \cdot \nabla \dot {s} - \zeta \cdot \dot {s} = - D \leq 0\tag{52}
$$

with $E _ { \ell }$ as the free energy and D as the dissipation rate, both per unit volume. Let us consider the following form of the free energy 

$$
E _ {\ell} = E _ {\ell} \left(\boldsymbol {\varepsilon} ^ {\mathrm{e}}, e ^ {\mathrm{p}}, \alpha , s, \nabla s\right).\tag{53}
$$

This postulated form contains the “standard” dependencies on the elastic strain $\pmb { \varepsilon } ^ { \mathrm { e } }$ and on the hardening variable α, plus further dependencies on the phase field and on its gradient, as well as on $e ^ { \mathfrak { p } }$ . The latter is a scalar measure of plastic strain accumulation defined in Eq. (51). The dependency of the free energy on $e ^ { \mathfrak { p } }$ is needed to realize a coupling between the evolution of the phase-field parameter and the accumulation of plastic strains, and is an essential ingredient of the proposed model. Substitution of Eq. (53) in the dissipation inequality (52) leads to 

$$
\begin{array}{l} \left(\frac {\partial E _ {\ell}}{\partial \boldsymbol {\varepsilon} ^ {\mathrm{e}}} - \boldsymbol {\sigma}\right): \dot {\boldsymbol {\varepsilon}} ^ {\mathrm{e}} + \left(\frac {\partial E _ {\ell}}{\partial e ^ {\mathrm{p}}} - \tau^ {\mathrm{p}}\right) \dot {e} ^ {\mathrm{p}} + \frac {\partial E _ {\ell}}{\partial \alpha} \dot {\alpha} \\ \quad + \left(\frac {\partial E _ {\ell}}{\partial s} - \zeta\right) \dot {s} + \left(\frac {\partial E _ {\ell}}{\partial \nabla s} - \boldsymbol {\xi}\right) \cdot \nabla \dot {s} = - D \leq 0. \end{array}\tag{54}
$$

Well-known arguments lead immediately to the elastic stress-strain relationship 

$$
\pmb {\sigma} = \frac {\partial E _ {\ell}}{\partial \pmb {\varepsilon} ^ {e}}.\tag{55}
$$

Additional consequences can be driven by applying the inequality individually to the group of terms related to the phase field 

$$
\left(\frac {\partial E _ {\ell}}{\partial s} - \zeta\right) \dot {s} + \left(\frac {\partial E _ {\ell}}{\partial \nabla s} - \boldsymbol {\xi}\right) \cdot \nabla \dot {s} \leq 0.\tag{56}
$$

From (56) follow the phase-field microscopic constitutive equations 

$$
\pmb {\xi} = \frac {\partial E _ {\ell}}{\partial \nabla s}, \qquad \zeta = \frac {\partial E _ {\ell}}{\partial s}.\tag{57}
$$

Substituting eqs. (57) into (50) leads to the phase-field evolution equation 

$$
\operatorname{div} \left(\frac {\partial E _ {\ell}}{\partial \nabla s}\right) - \frac {\partial E _ {\ell}}{\partial s} = 0,\tag{58}
$$

where we have further assumed $\gamma = 0$ 

As a result of Eq. (55) and inequality (56), and introducing the thermodynamic force power-conjugate to ${ \dot { \alpha } } ,$ 

$$
t _ {\alpha} := - \frac {\partial E _ {\ell}}{\partial \alpha},\tag{59}
$$

the following reduced dissipation inequality is obtained from (54) 

$$
D := \tau^ {\mathrm{p}} \dot {e} ^ {\mathrm{p}} + t _ {\alpha} \dot {\alpha} - \frac {\partial E _ {\ell}}{\partial e ^ {\mathrm{p}}} \dot {e} ^ {\mathrm{p}} \geq 0.\tag{60}
$$

Note that, being $\dot { e } ^ { \mathrm { p } } \geq 0 ;$ , inequality (60) can be further reduced to its “classical” version 

$$
\tau^ {\mathrm{p}} \dot {e} ^ {\mathrm{p}} + t _ {\alpha} \dot {\alpha} \geq 0,\tag{61}
$$

(whose satisfaction is ensured by the “classical” flow rule and hardening evolution equation of $J _ { 2 } \cdot$ -plasticity used in this work) provided that the following inequality holds 

$$
\frac {\partial E _ {\ell}}{\partial e ^ {\mathrm{p}}} \leq 0.\tag{62}
$$

From the specific choice of the free energy in Eq. (16) follows $\begin{array} { r } { \frac { \partial E _ { \ell } } { \partial e ^ { \mathrm { p } } } = \frac { \dot { \underline { \partial } } g } { \partial e ^ { \mathrm { p } } } \Psi _ { \mathrm { e } } ^ { + } ( \pmb { \varepsilon } ^ { \mathrm { e } } ) } \end{array}$ and therefore inequality (62) holds [and the reduced dissipation inequality takes the form (61)] provided that 

$$
\frac {\partial g}{\partial e ^ {p}} \leq 0.\tag{63}
$$

A possible specific choice of degradation function g complying with (63) is the following 

$$
g \left(s, e ^ {\mathrm{p}}\right) = s ^ {2 e ^ {\mathrm{p}} / e _ {\mathrm{crit}} ^ {\mathrm{p}}} + \eta\tag{64}
$$

with coincides with the one in Eq. (17) by taking 

$$
e _ {\mathrm{crit}} ^ {\mathrm{p}} = \sqrt {\frac {3}{2}} \varepsilon_ {\mathrm{eq,crit}} ^ {\mathrm{p}}\tag{65}
$$

This proves the thermodynamic consistency of the proposed model. 

## References



1. Besson J (2010) Continuum models of ductile fracture: a review. Int J Damage Mech 19(1):3–52 





2. Sumpter JDG, Forbes AT (1992) Constraint based analysis of shallow cracks in mild steel. In: TWI/EWI/IS international conference on shallow crack fracture mechanics, toughness tests and applications, Cambridge 





3. Sumpter JDG (1993) An experimental investigation of the T stress approach. In: Constraint effects in fracture, ASTM STP 1171 





4. ODowd NP, Shih CF (1991) Family ofcrack-tip fields characterized by a triaxiality parameter I. Structure of fields. J Mech Phys Solids 39(8):9891015 





5. Dawicke DS, Piascik RS, Jr Newman JC (1997) Prediction ofstable tearing and fracture of a 2000 series aluminium alloy plate using a CTOA criterion. In: Piascik RS, Newman JC, Dowlings NE (eds) Fatigue and fracture mechanics, ASTM STP 1296, 27:90–104 





6. James MA, Newman JC (2003) The effect of crack tunneling on crack growth: experiments and CTOA analyses. Eng Fract Mech 70:457–468 





7. Mahmoud S, Lease K (2003) The effect of specimen thickness on the experimental characterisation of critical crack tip opening angle in 2024–T351 aluminum alloy. Eng Fract Mech 70:443–456 





8. Trädegard A, Nilsson F, Östlund S (1998) FEM-remeshing technique applied to crack growth problems. Comput Methods Appl Mech Eng 160:115–131 





9. Pineau A (1980) Review of fracture micromechanisms and a local approach to predicting crack resistance in low strength steels. In: Proceedings of ICF5 conference, vol 2, Cannes 





10. Berdin C, Besson J, Bugat S, Desmorat R, Feyel F, Forest S, Lorentz E, Maire E, Pardoen T, Pineau A, Tanguy B (2004) Local approach to fracture. Presses de l’Ecole des Mines, Paris 





11. Gurson AL (1977) Continuum theory of ductile rupture by void nucleation and growth: part I yield criteria and flow rules for porous ductile media. J Eng Mater Technol 99:215 





12. Tvergaard V, Needleman A (1984) Analysis of the cup–cone fracture in a round tensile bar. Acta Metall 32:157169 





13. Lemaitre J (1985) A continuous damage mechanics model for ductile fracture. J Eng Mater Technol 107:8389 





14. Lemaitre J (1996) A course on damage mechanics. Springer, New York 





15. Bazant ZP, Pijaudier-Cabot G (1988) Non local continuum damage. Localization, instability and convergence. J Appl Mech 55:287294 





16. Peerlings RHJ, De Borst R, Brekelmans WAM, De Vree JHP, Spee I (1996) Some Observations on localisation in non-local and gradient damage models. Eur J Mech 15A(6):937–953 





17. Enakoutsa K, Leblond JB, Perrin G (2007) Numerical implementation and assessment of a phenomenological nonlocal model of ductile rupture. Comput Methods Appl Mech Eng 196(1316):19461957 





18. Reusch F, Svendsen B, Klingbeil D (2003) Local and non-local Gurson-based ductile damage and failure modelling at large deformation. Eur J Mech 22A:779792 





19. Moës N, Dolbow J, Belytschko T (1999) A finite element method for crack growth without remeshing. Int J Numer Methods Eng 46(1):131150 





20. Mediavilla J, Peerlings RHJ, Geers MGD (2006) Discrete crack modelling of ductile fracture driven by non-local softening plasticity. Int J Numer Methods Eng 66(4):661688 





21. Ortiz M, Pandolfi A (1999) Finite-deformation irreversible cohesive elements for three-dimensional crack-propagation analysis. Int J Numer Methods Eng 44(9):1267–1282 





22. Alfano G, Crisfield MA (2001) Finite element interface models for the delamination analysis oflaminated composites: mechanical and computational issues. Int J Numer Methods Eng 50:17011736 





23. De Lorenzis L, Fernando D, Teng JG (2013) Coupled mixed-mode cohesive zone modeling of interfacial debonding in simply supported plated beams. Int J Solids Struct 50:2477–2494 





24. Roychowdhury YDA, Jr Dodds RH (2002) Ductile tearing in thin aluminum panels: experiments and analyses using largedisplacement, 3D surface cohesive elements. Eng Fract Mech 69:983–1002 





25. Cornec A, Scheider I, Schwalbe KH (2003) On the practical application of the cohesive model. Eng Fract Mech 70(14):1963– 1987 





26. Dimitri R, De Lorenzis L, Wriggers P, Zavarise G (2014) NURBSand T-spline-based isogeometric cohesive zone modeling of interface debonding. Comput Mech 54:369–388 





27. Scheider I, Brocks W (2003) Simulation ofcup–cone fracture using the cohesive model. Eng Fract Mech 70(14):1943–1961 





28. Moes N, Belytschko T (2002) Extended finite element method for cohesive crack growth. Eng Fract Mech 69(7):813–833 





29. Seabra MRR, Sustari´c P, Cesar de Sa JMA, Rodi´c T (2013) Damage driven crack initiation and propagation in ductile metals using XFEM. Comput Mech 52:161–179 





30. Broumand P, Khoei AR (2013) The extended finite element method for large deformation ductile fracture problems with a non-local damage-plasticity model. Eng Fract Mech 112–113:97–125 





31. Crété JP, Longère P, Cadou JM (2014) Numerical modelling of crack propagation in ductile materials combining the GTN model and X-FEM. Comput Methods Appl Mech Eng 275:204–233 





32. Bourdin B, Francfort GA, Marigo JJ (2000) Numerical experiments in revisited brittle fracture. J Mech Phys Solids 48:797–826 





33. Kuhn C, Müller R (2008) A phase field model for fracture. Proc Appl Math Mech 8:10223–10224 





34. Kuhn C, Müller R (2010) A continuum phase field model for fracture. Eng Fract Mech 77:3625–3634 





35. Amor H, Marigo JJ, Maurini C (2009) Regularized formulation of the variational brittle fracture with unilateral contact: numerical experiments. J Mech Phys Solids 57:1209–1229 





36. Miehe C, Welschinger F, Hofacker M (2010) Thermodynamically consistent phase-field models of fracture: variational principles and multi-field FE implementations. Int J Numer Methods Eng 83:1273–1311 





37. Miehe C, Hofacker M, Welschinger F (2010) A phase field mode for rate-independent crack propagation: robust algorithmic implementation based on operator splits. Comput Methods Appl Mech Eng 199:2765–2778 





38. Borden MJ, Hughes TJR, Landis CM, Verhoosel CV (2014) A higher-order phase-field model for brittle fracture: formulation and analysis within the isogeometric analysis framework. Comput Methods Appl Mech Eng 273:100–118 





39. Ambati M, Gerasimov T, De Lorenzis L (2014) A review on phasefield models of brittle fracture and a new fast hybrid formulation. Comput Mech. doi:10.1007/s00466-014-1109-y 





40. Hofacker M, Miehe C (2012) A phase field model for ductile to brittle failure mode transition. Proc Appl Math Mech 12:173–174 





41. Ulmer H, Hofacker M, Miehe C (2013) Phase field modeling of brittle and ductile fracture. Proc Appl Math Mech 13:533–536 





42. Duda FP, Ciarbonetti A, Sanchez PJ, Huespe AE (2014) A phasefield/gradient damage model for brittle fracture in elastic–plastic solids. Int J Plast. doi:10.1016/j.ijplas.2014.09.005 





43. Francfort GA, Marigo JJ (1998) Revisiting brittle fractures as an energy minimization problem. J Mech Phys Solids 46:1319–1342 





44. Bourdin B, Francfort GA, Marigo JJ (2008) The variational approach to fracture. J Elast 91:5–148 





45. Larsen CJ, Ortner C, Süli E (2010) Existence of solutions to a regularized model of dynamic fracture. Math Models Methods Appl Sci 20:1021–1048 





46. Bourdin B, Larsen CJ, Richardson C (2011) A time-discrete model for dynamic fracture based on crack regularization. Int J Fract 168:133–143 





47. Borden MJ, Verhoosel CV, Scott MA, Hughes TJR, Landis CM (2012) A phase-field description of dynamic brittle fracture. Comput Methods Appl Mech Eng 217–220:77–95 





48. Hofacker M, Miehe C (2012) Continuum phase field modeling of dynamic fracture: variational principles and staggered FE implementation. Int J Fract 178:113–129 





49. Hofacker M, Miehe C (2013) A phase-field model of dynamic fracture: robust field updates for the analysis of complex crack patterns. Int J Numer Methods Eng 93:276–301 





50. Schlüter A, Willenbücher A, Kuhn C, Müller R (2014) Phase field approximation ofdynamic brittle fracture. Comput Mech 54:1141– 1161 





51. Simo JC, Hughes TJR (1998) Computational Inelasticity. Springer, New York 





52. Neto EdS, Peri´c D, Owen DRJ (2008) Computational methods for plasticity. Wiley, New York 





53. Mediavilla J, Peerlings RHJ, Geers MGD (2006) A robust and consistent remeshing-transfer operator for ductile fracture simulations. Comput Struct 84:604–623 





54. Xue L (2007) Ductile fracture modeling: theory, experimental investigation and numerical verification. Massachusetts Institute of Technology, Cambridge 





55. Xue L (2008) Ductile fracture initiation and propagation modeling using damage plasticity theory. Eng Fract Mech 75:3276–3293 





56. Alves M, Jones N (1999) Influence of hydrostatic stress on failure of axisymmetric notched specimens. J Mech Phys Solids 47:643– 667 





57. Amstutz BE, Sutton MA, Dawicke DS, Boone ML (1997) Effects of mixed mode I/II loading and grain orientation on crack initia-





tion and stable tearing in 2024–T3 aluminum. Fatigue Fract Mech 27:24–217 





58. Arcan M, Hashin Z, Voloshin A (1978) Method to produce uniform plane stress states with applications to fiber-reinforced materials. Exp Mech 18:6–141 





59. Nayfeh AH (2011) Introduction to perturbation techniques. Wiley-VCH, Weinheim 





60. Gurtin ME (1996) Generalized Ginzburg–Landau and Cahn– Hilliard equations based on a microforce balance. Phys D 92(3– 4):178–192 





61. Gurtin M, Fried E, Anand L (2010) The mechanics and thermodynamics of continua. Cambridge University Press, New York 

