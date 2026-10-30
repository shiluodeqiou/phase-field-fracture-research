# Thermodynamically consistent phase-field models of fracture: Variational principles and multi-field FE implementations

C. Miehe<sup>∗,</sup>†, F. Welschinger and M. Hofacker 

Institut fur Mechanik ¨ (Bauwesen) Lehrstuhl I, Universitat Stuttgart ¨ , 70550 Stuttgart, Pfaffenwaldring 7, German 

## SUMMARY

The computational modeling of failure mechanisms in solids due to fracture based on sharp crack discontinuities suffers in situations with complex crack topologies. This can be overcome by a diffusive crack modeling based on the introduction of a crack phase-field. In this paper, we outline a thermodynamically consistent framework for phase-field models of crack propagation in elastic solids, develop incrementa variational principles and consider their numerical implementations by multi-field finite element methods. We start our investigation with an intuitive and descriptive derivation of a regularized crack surface func tional that --converges for vanishing length-scale parameter to a sharp crack topology functional. This functional provides the basis for the definition of suitable convex dissipation functions that govern the evolution of the crack phase-field. Here, we propose alternative rate-independent and viscous over-force models that ensure the local growth of the phase-field. Next, we define an energy storage function whose positive tensile part degrades with increasing phase-field. With these constitutive functionals at hand, we derive the coupled balances of quasi-static stress equilibrium and gradient-type phase-field evolution in the solid from the argument of virtual power. Here, we consider a canonical two-field setting for rate-independent response and a time-regularized three-fieldformulation with viscous over-force response. It is then shown that these balances follow as the Euler equations of incremental variational principles that govern the multi-field problems. These principles make the proposed formulation extremely compact and provide a perfect base for the finite element implementation, including features such as the symmetry of the monolithic tangent matrices. We demonstrate the performance of the proposed phase-field formulation of fracture by means of representative numerical examples. Copyright q 2010 John Wiley & Sons, Ltd. 

Received 11 August 2009; Revised 4 January 2010; Accepted 8 January 2010 

KEY WORDS: fracture; crack propagation; phase-fields; gradient-type damage; incremental variational principles; finite elements; coupled multi-field problems 

## 1. INTRODUCTION

Fracture is one of the main failure mechanisms of engineering materials and structural components. The prediction of crack initiation and propagation through computational models is of grea importance for engineering applications. Theoretical foundations of the classical theory of brittle fracture in solids are outlined in the works of Griffith [1], Irwin [2] and Barenblatt [3]. Following Griffith and Irwin, the crack propagates if the energy release rate reaches a critical value. The Griffith theory provides a criterion for crack propagation but is insufficient to determine curvilinear crack paths, crack kinking and branching angles. In particular, such a theory is unable to predict crack initiation. These defects of the classical Griffith-type theory of brittle fracture can be overcome by variational methods based on energy minimization as suggested by Francfort and Marigo [4], see also Bourdin et al. [5], Dal Maso and Toader [6] and Buliga [7]. The regularized setting of their framework, considered in Bourdin et al. [8, 5], is obtained by --convergence inspired by the work of image segmentation by Mumford and Shah [9]. We refer to Ambrosio and Tortorelli [10] and the reviews of Dal Maso [11] and Braides [12, 13] for details on --convergent approximations of free discontinuity problems. The approximation regularizes a sharp crack surface topology in the solid by diffusive crack zones governed by a scalar auxiliary variable. This variable can be considered as a phase-field that interpolates between the unbroken and the broken states of the material. Conceptually similar are recently outlined phase-field approaches to brittle fracture based on the classical Ginzburg–Landau-type evolution equation as reviewed in Hakim and Karma [14], see also Karma et al. [15] and Eastgate et al. [16]. These models may be considered as time-dependent viscous regularizations of the above-mentioned rate-independent theories of energy minimization. 

The variational-based phase-field approaches to fracture offer important new perspectives toward the theoretical and computational modeling of complex crack topologies. Recall that finite-element based numerical implementations of sharp crack discontinuities, such as interface element formula tions, element and nodal enrichment strategies, suffer in the case of three-dimensional applications with crack branching, see for example the advanced concepts by Belytschko and coworkers [17, 18] on xfem methods and by Gurses and Miehe¨ [19] and Miehe et al. [20, 21] on the modeling of configurational-force-driven sharp crack propagation. In contrast, phase-field-type diffusive crack approaches avoid the modeling of discontinuities and can be implemented in a straightforward manner by coupled multi-field finite element solvers. However, the above-mentioned approaches to fracture still have a few drawbacks that limit their application to particular model problems. The model outlined in Hakim and Karma [14] is based on a Ginzburg–Landau-type evolution equation of the fracture phase-field, which is fully viscous in nature and does not differentiate between energy storage and dissipation. These are very strong simplifications of the physica mechanisms of brittle fracture. The formulation of rate-independent diffusive fracture proposed by Bourdin et al. [8] models the irreversibility of the process only on a time-discrete level by setting hard Dirichlet-type conditions on the phase-field. Furthermore, both existing phase-field models consider energy-release-driven fracture in both tension and compression. Clearly, these fully symmetric formulations are unrealistic for most materials and restricted to the modeling o boundary value problems with tensile stresses in the full solid domain. These approaches are, in general, not thermodynamically consistent and are applicable only in the particular situation of monotonous loading of arbitrary sub-domains of a fracturing solid. Finally, a more intuitive approach alternative to the formal and mathematically demanding results of --convergence to free discontinuity problems seems to be important in order to make phase-field models of fracture more attractive in the engineering community. 

In this work, we outline a thermodynamically consistent framework of phase-field-type brittle fracture that overcomes the above-mentioned difficulties. Of particular interest is a careful, descrip tive and comprehensive representation of the basic ingredients that enter this framework. The proposed approach is embedded in the theory of gradient-type materials with a characteristic length scale, such as outlined in a very general context in Capriz [22], Mariano [23] and Fremond´ [24]. From the viewpoint of material modeling, a phase-field approach to fracture is conceptually in line with models of continuum damage mechanics, see for example Kachanov [25] or Fremond and´ Nedjar [26], where a scalar damage field may be interpreted as the phase-field. In this sense, the subsequent framework of regularized brittle crack propagation may be considered as a gradient-type damage model with particular definitions of an energy function with a gradient-type regularized surface energy. Focusing on quasi-static problems, we construct for dissipative crack propagation in solids accompanied by bulk energy degradation two characteristic multi-field formulations, which are well-suited for numerical implementation: 

• Model I. Two-field setting: A rate-independent phase-field model of fracture that incorporates the displacement and the fracture phase-fields, see Euler equations (61). 

• Model II. Three-field setting: A viscous over-force model, incorporating the displacement, the fracture phase and a dual driving force field, see Euler equations (63). 

The first model is close to that of Bourdin et al. [8] based on Ambrosio and Tortorelli [10], derived, however, in an alternative format that differentiates between energetic and dissipative mechanisms and accounts for the irreversibility of the phase-field evolution in a different way. The second model may be considered as a time-dependent regularization of the first model, where the phase-field evolution may be recast into a characteristic Ginzburg–Landau-type structure. Both models describe, for limits of the model-inherent length scale and viscosity parameters, quasi-static crack propagation in solids based on the classical Griffith criterion of critical energy release. We embed the multi-field models in an incremental variational framework of gradient-type standard dissipative materials. This is of particular importance for the computational implementation by finite element methods, which appears in an extremely compact format with symmetric tangents of the coupled multi-field problems. Numerical tests demonstrate that the viscous over-force model II provides the more robust algorithmic setting for general applications due to the stabilizing effect of the viscosity. 

We start our investigation in Section 2 with a descriptive motivation of a regularized crack topology based on a phase-field. This phase-field is first introduced for the one-dimensional setting and then generalized to the multi-dimensional case. This treatment results in the definition of a regularized crack surface functional, depending on the crack phase-field that --converges for vanishing length-scale parameter to a sharp crack topology. We consider this crack functional as the crack surface itself and postulate that it should stay constant or grow for arbitrary loading processes. In a subsequent step, we introduce dissipation functions related to the evolution of the crack surface functional. The evolution of the crack surface is assumed to be fully dissipative in nature. As a consequence, the dissipation function depends on the rate of the phase-field and its gradient, representing a gradient-type dissipative material. We construct specific dissipation functions per unit volume for purely rate-independent crack propagation (model I) as well as for a time-regularized viscous crack propagation (model II). The latter concept is accompanied by the use of the dissipative force field dual to the fracture phase-field. The dissipation functions are formulated such that they model growing cracks by enforcing the local growth of the phase-field. 

The next modeling step in Section 3 is concerned with the constitutive definition of the elastic bulk energy of the solid that degrades with growing fracture phase-field. To this end, we use a simple degradation function that acts in a multiplicative format on the stored energy function of an undamaged solid. Here, we consider first a fully symmetric formulation with an unrealistic degradation in tension and compression. Such a model can only be applied to the modeling of monotonic loading processes in tension. In order to get a more realistic treatment, we consider stored energy functions where the degradation due to the growing phase-field acts only on the positive part of the stored energy. This positive part is defined in terms of the principal strains and requires the spectral decomposition of the strain tensor. The proposed model accounts for crack closing in reverse loading processes and provides an advanced setting of phase-field-type fracture. 

With the dissipation and energy storage functions at hand, we derive in Section 4 the governing balance equations from the argument of virtual power. For the quasi-static processes under consid eration, the coupled balances consist of the static equilibrium condition for the degraded stresses and the evolution equation for the phase-field. They characterize the two-field problem of model I with the displacement field and the phase-field as the primary variables. For the extended viscous formulation of model II, we have a three-field formulation where a local dissipative force dua to the phase-field appears as an additional field. For these coupled field problems, we develop in Section 5 incremental variational structures. We show that the above-mentioned coupled balances are the Euler equations of characteristic variational functionals. For the two-field problem, we have a minimization structure and for the three-field problem a stationary principle. The proposed varia tional structure of the coupled problem is exploited in the spatial discretization by the finite element method. To this end, we construct discrete counterparts of the continuous variational principles. These statements provide extremely compact representations of the highly nonlinear algebraic problem. The problems are solved by Newton-type solvers. Owing to the variational structure, the monolithic tangent matrices of the coupled problems are symmetric. Finally, Section 6 outlines representative numerical examples that demonstrate the features of the proposed phase-field models of fracture. 

## 2. PHASE-FIELD APPROXIMATION OF CRACK TOPOLOGY

## 2.1. Motivation: one-dimensional bar with a crack

Consider an infinitely expanded bar of cross-section - occupying the domain $\mathscr { B } { = } \Gamma \times L$ with $L = [ - \infty , + \infty ]$ and position $x \in L$ of its axis. Assume a crack of the bar at the axial position $x = 0 .$ where - represents the fully broken crack surface. This sharp crack topology may be described by an auxiliary field variable $d ( x ) \in [ 0 , 1 ]$ with 

$$
d (x) := \left\{ \begin{array}{l l} 1 & \text { for } x = 0 \\ 0 & \text { otherwise } \end{array} \right.\tag{1}
$$

characterizing for $d = 0$ the unbroken state and for $d = 1$ the fully broken state of the material. Figure 1(a) gives a visualization. We denote the auxiliary variable $d ( x )$ as the crack phase-field. Clearly, such an approach is related to the continuum theory of damage, where the scalar damage field d describes in a homogenized macroscopic sense the development of micro-cracks and micro-voids. With this viewpoint in mind, we approximate the non-smooth phase-field (1) by the exponential function 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/2723795f360e75b78623af0a4e719b3883879d53a41c9b47db78d795d80916ed.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/5e6cac04bf5ad7c8fa3733d419dad3eb37f5a29f062bc19296b714d80a5f298f.jpg)



Figure 1. Sharp and diffusive crack modeling. (a) Sharp crack at $x = 0$ and (b) diffusive crack at x =0 modeled with the length scale l.


$$
d (x) = \mathrm{e} ^ {- | x | / l}.\tag{2}
$$

It smears out the crack over the axial domain L of the bar, representing a regularized or diffusive crack topology as depicted in Figure 1(b). The regularization is governed by the length-scale parameter l and gives for $l  0$ the function (1). The exponential function (2) has the property 

$$
d (0) = 1 \quad \mathrm{and} \quad d (\pm \infty) = 0.\tag{3}
$$

Now observe that (2) is the solution of the homogeneous differential equation 

$$
d (x) - l ^ {2} d ^ {\prime \prime} (x) = 0 \quad \mathrm{in} \mathcal {B}\tag{4}
$$

subject to the Dirichlet-type boundary conditions (3). This differential equation is the Euler equation of the variational principle 

$$
d = \operatorname{Arg} \left\{\inf _ {d \in W} I (d) \right\}\tag{5}
$$

with $W = \{ d | d ( 0 ) = 1 , d ( \pm \infty ) = 0 \}$ , in terms of the functional 

$$
I (d) = \frac {1}{2} \int_ {\mathcal {B}} \{d ^ {2} + l ^ {2} d ^ {\prime 2} \} \mathrm{d} V.\tag{6}
$$

This functional can easily be constructed by integrating a Galerkin-type weak form of the differential equation (4). Now observe that the evaluation of the functional for the solution (2) gives with d $. V { = } \Gamma$ dx the identification 

$$
I (d = \mathrm{e} ^ {- | x | / l}) = l \Gamma ,\tag{7}
$$

Copyright q 2010 John Wiley & Sons, Ltd. 

which relates the functional I to the crack surface -. As a consequence, we may introduce the functional 

$$
\boxed {\Gamma_ {l} (d) := \frac {1}{l} I (d) = \frac {1}{2 l} \int_ {\mathscr {B}} \left\{d ^ {2} + l ^ {2} d ^ {\prime 2} \right\} \mathrm{d} V}\tag{8}
$$

alternatively to (6). Clearly, the minimization of this scaled functional also gives the regularized crack topology (2) depicted in Figure 1(b). However, the scaling by the length-scale parameter l has the consequence that the functional $\Gamma _ { l } ( d )$ may be considered as the crack surface itself. In the one-dimensional problem under consideration, the evaluation of $\Gamma _ { l } ( d )$ at the solution point gives for arbitrary length scales l the crack surface -. This property characterizes the functional $\Gamma _ { l }$ as an important ingredient of the subsequent constitutive modeling of diffusive crack propagation.‡ 

## 2.2. Variational problem of regularized crack topology

2.2.1. Continuous formulation. The formulation for cracks in one-dimensional solids outlined above can be extended to multi-dimensional solids in a straightforward manner. Let $\mathcal { B } \subset \mathcal { R } ^ { \delta }$ be the reference configuration of a material body with dimension $\delta \in [ 1 , 2 , 3 ]$ in space and $\partial \mathcal { B } \subset \mathcal { R } ^ { \delta - 1 }$ its surface as depicted in Figure 2. In the subsequent treatment, we intend to study cracks in the solid evolving in the range $\mathcal { T } \subset \mathcal { R }$ of time. To this end, we introduce the time-dependent crack phase-field 

$$
d \colon \left\{ \begin{array}{l} \mathcal {B} \times \mathcal {T} \to [ 0, 1 ] \\ (\boldsymbol {x}, t) \mapsto d (\boldsymbol {x}, t) \end{array} \right.\tag{9}
$$

defined on the solid ${ \mathcal { B } } .$ . Then, a multi-dimensional extension of the regularized crack functional (8) reads 

$$
\Gamma_ {l} (d) = \int_ {\mathcal {B}} \gamma (d, \nabla d) \mathrm{d} V,\tag{10}
$$

where we have introduced the crack surface density function per unit volume of the solid 

$$
\boxed {\gamma (d, \nabla d) = \frac {1}{2 l} d ^ {2} + \frac {l}{2} | \nabla d | ^ {2}.}\tag{11}
$$

This function, which depends on the crack phase-field d and its spatial gradient $\nabla d ,$ , plays a critical role in the subsequent modeling of crack propagation. Assuming a given sharp crack surface topology $\Gamma ( t ) \subset \dot { \mathcal { R } } ^ { \delta - 1 }$ inside the solid B at time t, as depicted in Figure 2(a), we obtain in analogy to (5) the regularized crack phase field $d ( { \pmb x } , t )$ on ${ \mathcal { B } } ,$ , visualized in Figure 2(b), from the minimization principle 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/77ef0c9cd71d068320f7d431a674722fa5d51ea121dfe1e2b3a228841959b109.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/4b1fc1e6dbe0faa652eb333d6daa963fb86b0d036e87697c37e18d5a97737c99.jpg)



(b)



Figure 2. Sharp and diffusive crack topology. (a) Sharp crack surface - embedded into the solid $\mathcal { B }$ and (b) the regularized crack surface $\Gamma _ { l } ( d )$ is a functional of the crack phase-field $d .$


$$
d (\boldsymbol {x}, t) = \operatorname{Arg} \left\{\inf _ {d \in W _ {\Gamma (t)}} \Gamma_ {l} (d) \right\}\tag{12}
$$

subject to the Dirichlet-type constraints 

$$
W _ {\Gamma (t)} = \{d | d (\boldsymbol {x}, t) = 1 \text {   at   } \boldsymbol {x} \in \Gamma (t) \}.\tag{13}
$$

The Euler equations of the above variational principle are 

$$
d - l ^ {2} \Delta d = 0 \quad \mathrm{in} \mathcal {B} \quad \mathrm{and} \quad \nabla d \cdot \boldsymbol {n} = 0 \quad \mathrm{on} \partial \mathcal {B},\tag{14}
$$

where d is the Laplacian of the phase-field and n the outward normal on $\partial \mathcal { B } .$ 

2.2.2. Spatial discretization. Let $\mathfrak { T } ^ { h }$ denote a finite element triangulation of the solid domain B. The index h indicates a typical mesh size based on $E ^ { h }$ finite element domains $\mathcal { B } _ { e } ^ { h } \in \mathfrak { T } ^ { h }$ and $N ^ { h }$ global nodal points. Associated with $\mathfrak { T } ^ { h }$ , we write the finite element interpolations of the phase-field and its gradient by 

$$
\mathfrak {c} ^ {h} := \{d, \nabla d \} ^ {h} = \boldsymbol {B} (\boldsymbol {x}) \boldsymbol {d} (t)\tag{15}
$$

in terms of the nodal phase-field vector $\pmb { d } \in \mathcal { R } ^ { N ^ { h } }$ . B is a symbolic representation of a global interpolation matrix, containing the shape functions and its derivatives.<sup>§</sup> Then the discretized variational principle (12) 

$$
\boldsymbol {d} = \operatorname{Arg} \left\{\inf _ {\boldsymbol {d} \in W _ {\Gamma (t)} ^ {h}} \int_ {\mathscr {B} ^ {h}} \gamma (\boldsymbol {B} \boldsymbol {d}) \mathrm{d} V \right\}\tag{17}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/eb4e21f7fab30d139e72f144b50b7f64afc374d51e84f5d2c394dc21d568c00d.jpg)



Figure 3. Model problem. Two-dimensional domain $\mathcal { B }$ with a sharp crack surface $\Gamma { = } 0 . 5$


determines for a given sharp crack topology at time t the nodal values of the phase-field for the regularized topology. The associated Euler equation is linear and can be solved in closed form 

$$
\boldsymbol {d} = - \left[ \int_ {\mathcal {B} ^ {h}} \boldsymbol {B} ^ {\mathrm{T}} [ \partial_ {\mathfrak {c c}} ^ {2} \gamma ] \boldsymbol {B} \mathrm{d} V \right] ^ {- 1} \int_ {\mathcal {B} ^ {h}} \boldsymbol {B} ^ {\mathrm{T}} [ \partial_ {\mathfrak {c}} \gamma ] \mathrm{d} V.\tag{18}
$$

2.2.3. A numerical model problem. The following numerical example demonstrates the regulariza tion of a crack topology for an elementary model problem. We consider a continuum of dimension $\delta = 2$ with a sharp crack surface - from the left side to the center as depicted in Figure 3. On the exterior boundary $\partial \mathcal { B }$ the Neumann condition $( 1 4 ) _ { 2 }$ is prescribed. On the crack surface Γ, we set the Dirichlet condition $d = 1$ for the crack phase field. We consider the finite element computation of the crack phase-field d in the domain $\mathcal { B }$ according to the linear solution procedure (18) for given values of the length-scale parameter l. The finite element mesh requires a certain minimum element size h in order to resolve this length scale. This is demonstrated in Figure 4 for finite element meshes with a constant element size $h ,$ consisting of four node quadrilateral elements This elementary study shows that an element size 

$$
h <   l / 2\tag{19}
$$

is needed in order to resolve the regularized crack surface $\Gamma _ { l } ( d )$ , such that we have $\Gamma _ { l } ( d ) \approx \Gamma$ in the finite element approximation. Clearly, this resolution is only needed in subdomains close to the crack surface. Hence, an h-adaptive finite element solution procedure with a minimum element size close to (19) is appropriate. Figure 5 shows finite element simulations for different length scales $l = 0 . 2 0 , 0 . 1 0 , 0 . 0 2 , 0 . 0 0 7$ based on a very fine mesh with constant mesh size $h = 0 . 0 0 3 5$ consisting of 90 000 four node quadrilaterals. The large length scale $l { = } 0 . 0 2$ yields the approximated regularized crack surface $\Gamma _ { l } = 0 . 5 9 4 4$ depicted in Figure 5(a). The small length scale $l { = } 0 . 0 0 7$ gives $\Gamma _ { l } = 0 . 5 0 9 0 { \approx } \Gamma { = } 0 . 5$ as shown in Figure 5(d). 

## 2.3. Dissipation function for crack evolution

We now focus on a time-dependent crack evolution by exploiting the above-outlined definition of the regularized crack surface. The evolution of cracks is driven by some energetic driving forces as outlined below. However, the cracking itself is considered to be $f u l l y$ dissipative in nature. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/c775c0197f5a235dc53dcb7511160b596a6580c411bd78bc2931b891a4697fc9.jpg)



Figure 4. Minimum size of finite elements. A reasonable accuracy of the crack topology approximation $\Gamma _ { l } { \approx } \Gamma$ requires for quadrilateral element meshes an element size of $\mathbf { \bar { \boldsymbol { h } } } < \bar { \boldsymbol { l } } \bar { \mathbf { \bar { \boldsymbol { 2 } } } }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/6736089584eea34022a50284fcd209a562490d58cca4c8ee402daff58d91a79e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/d233155cdfe89dc23e699e54d02c15e48ec6c9a01c7babe89096b3b395bfeaa8.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/292372df0464eb7da972229809bc8e3f9a74bb380a29838dd09c5b1e15bfb416.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/a3ba90075a00af8064692fc5daf0cc222d7806f1faa24551e0a119a81d2dc1ba.jpg)



(c)



(d)



Figure 5. Regularized crack surfaces $\Gamma _ { l } ( d )$ governed by the crack phase-field d for different length scales. (a) $l { = } 0 . 2 0$ with $\Gamma _ { l } = 0 . 5 9 4 4$ ; (b) $l { = } 0 . 1 0$ with $\Gamma _ { l } = 0 . 5 \dot { 5 } 0 7 \dot { }$ $\left( \mathrm { c } \right) l { = } \hat { 0 } . 0 2$ with $\Gamma _ { l } = 0 . 5 1 1 3 ;$ and $\mathrm { ( d ) } \ l = 0 . 0 0 7$ with $\Gamma _ { l } = 0 . 5 0 9 0$ obtained with a mesh of size $h { = } 0 . 0 0 3 5$


As a consequence, we postulate as a basic feature of the irreversibility of the cracking process the growth of the regularized crack surface in time, i.e. 

$$
\dot {\Gamma} _ {l} := \frac {\mathrm{d}}{\mathrm{d} t} \Gamma_ {l} (d (\boldsymbol {x}, t)) \geqslant 0.\tag{20}
$$

The evolution of the crack surface can be reformulated based on representation (10) as 

$$
\dot {\Gamma} _ {l} = \int_ {\mathcal {B}} \dot {\gamma} \mathrm{d} V = \int_ {\mathcal {B}} (\delta_ {d} \gamma) \dot {d} \mathrm{d} V \geqslant 0,\tag{21}
$$

where we have introduced the variational or functional derivative of the crack surface density function 

$$
\delta_ {d} \gamma := \partial_ {d} \gamma - \mathrm{Div} [ \partial_ {\nabla d} \gamma ] = \frac {1}{l} [ d - l ^ {2} \Delta d ].\tag{22}
$$

Observe that we may satisfy the global irreversibility constraint of crack evolution by ensuring locally a positive variational derivative of the crack surface function and a positive evolution of the crack phase-field 

$$
\delta_ {d} \gamma \geqslant 0 \quad \text { and } \quad \dot {d} \geqslant 0.\tag{23}
$$

The former condition is ensured in the subsequent treatment by a constitutive assumption that relates the functional derivative to a positive energetic driving force. The latter constraint is a natural assumption that relates the fracture phase-field for the non-reversible evolution of micro-cracks and micro-voids. 

2.3.1. Model I: Rate-independent setting with approximated indicator function. The constraint (23) must be satisfied by defining a proper evolution equation for the crack phase-field. This is achieved by the introduction of a global constitutive dissipation functional for a rate-independent fracture process 

$$
D (\dot {d}; d) = \int_ {\mathcal {B}} \phi (\dot {d}, \nabla \dot {d}; d, \nabla d) \mathrm{d} V\tag{24}
$$

in terms of a constitutive dissipation function per unit volume 

$$
\phi = g _ {\mathrm{c}} \dot {\gamma} (\dot {d}, \nabla \dot {d}; d, \nabla d) + I _ {+} (\dot {d}).\tag{25}
$$

The parameter $g _ { \mathrm { c } }$ is a constitutive threshold value related to the critical Griffith-type fracture energy. Note that the first term characterizes the local energy release due to the crack evolution, because $\gamma$ is the crack surface per unit volume. $I _ { + } ( x )$ is the non-smooth indicator function of the set $\mathcal { R } _ { + }$ of positive real numbers, defined by 

$$
I _ {+} (x) = \left\{ \begin{array}{l l} 0 & \text { for } x > 0 \\ \infty & \text { otherwise } \end{array} \right.\tag{26}
$$

and visualized in Figure 6(a). It ensures the constraint $( 2 3 ) _ { 2 }$ of positive evolution of the phase-field d. We now introduce the approximated indicator function 

$$
I _ {+} ^ {\varepsilon} (x) = \frac {\varepsilon}{2} \langle x \rangle_ {-} ^ {2}\tag{27}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/780ad4199babcfce40ba1bfe01cc2355e6c6183474a424ebb35e1605a3e5dda6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/1e1e21492bed5bc846f9dce141c3f8086171182fcba56045059cecfe26384abc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/1bdd10f66d707af66e1fad5b2a3efd5b512b8d3f8f61c45491a46684e04a3dab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/ed1a4e9aad4c3005d2acbaeee3f468f29dc348841cbb7912c783b9150b9568ab.jpg)



Figure 6. Convex functions: (a) Indicator function of $\mathcal { R } _ { + ; } \thinspace ( \mathsf { b } )$ ) regularized indicator function of the $\mathcal { R } _ { + }$ $\bar { I } _ { + } ^ { \varepsilon } ( x ) = \varepsilon / 2 \langle x \rangle _ { - } ^ { 2 }$ . Ramp functions; (c) $\langle x \rangle _ { + } { : = } ( | x | + x ) / 2$ of $\mathcal { R } _ { + } ;$ and (d) $\langle x \rangle _ { - } : = ( | x | - x ) / 2$ of $\mathcal { R } _ { - }$


as visualized in Figure 6(b), where $\langle x \rangle _ { - } : = [ | x | - x ] / 2$ depicted in Figure 6(d) is the ramp function of $\mathcal { R } _ { - }$ −. The constant  is a regularization parameter that ensures for the limit $\varepsilon \to \infty$ exactly the growth condition (23) . We then propose the use of the dissipation function 

$$
\phi_ {\varepsilon} (\dot {d}, \nabla \dot {d}; d, \nabla d) = \left(\frac {g _ {\mathrm{c}}}{l} d\right) \dot {d} + (g _ {\mathrm{c}} l \nabla d) \cdot \nabla \dot {d} + \frac {\varepsilon}{2} \langle \dot {d} \rangle_ {-} ^ {2}\tag{28}
$$

as a first model approach to regularized fracture. 

2.3.2. Model II: Rate-dependent setting with threshold function. Alternative formulations that ensure the irreversibility constraint (23) can be constructed by taking into account the variable dual to the phase-field $d$ 

$$
\beta \colon \left\{ \begin{array}{l} \mathcal {B} \times \mathcal {T} \to \mathcal {R} \\ (\pmb {x}, t) \mapsto \beta (\pmb {x}, t), \end{array} \right.\tag{29}
$$

in what follows denoted as the local driving force field. In the rate-independent formulation (25), this force field is constrained by the threshold function 

$$
f (\beta ; d) = \beta - \frac {g _ {\mathrm{c}}}{l} d \leqslant 0,\tag{30}
$$

which characterizes for $f { < } 0$ a range without diffusive crack accumulation. The threshold of the force is a linear function of the phase-field itself and is related to the first term in the dissipation function (28). With this notion at hand, we define the dissipation function by the constrained optimization problem 

$$
\phi (\dot {d}, \nabla \dot {d}; d, \nabla d) = \sup _ {\beta , \lambda \geqslant 0} \left[ \beta \dot {d} - \lambda \left(\beta - \frac {g _ {\mathrm{c}}}{l} d\right) \right] + (g _ {\mathrm{c}} l \nabla d) \cdot \nabla \dot {d}\tag{31}
$$

with the Lagrange parameter . The necessary conditions of this constraint optimization problem identify the Lagrange parameter $\lambda { = } \dot { d }$ with the evolution of the phase-field and result in the conditions 

$$
\dot {d} \geqslant 0, \quad \beta \leqslant \frac {g _ {\mathrm{c}}}{l} \mathrm{d}, \quad \dot {d} \left(\beta - \frac {g _ {\mathrm{c}}}{l} d\right) = 0.\tag{32}
$$

Note that these conditions determine the local evolution $\dot { d }$ of the phase-field in terms of the local driving force $\beta$ and the phase-field $d$ itself. Observe that (32) includes explicitly the desired irreversibility condition. A viscous regularization of the above rate-independent formulation can be based on the dissipation function 

$$
\boxed {\phi_ {\eta} (\dot {d}, \nabla \dot {d}; d, \nabla d) = \sup _ {\beta} \left[ \beta \dot {d} - \frac {1}{2 \eta} \left\langle \beta - \frac {g _ {\mathrm{c}}}{l} d \right\rangle_ {+} ^ {2} \right] + (g _ {\mathrm{c}} l \nabla d) \cdot \nabla \dot {d}.}\tag{33}
$$

$\langle x \rangle _ { + } { : = } [ | x | + x ] / 2$ is the ramp function of the $\mathcal { R } _ { + }$ , as visualized in Figure 6(c). The necessary condition of this optimization problem is 

$$
\dot {d} = \frac {1}{\eta} \left\langle \beta - \frac {g _ {\mathrm{c}}}{l} d \right\rangle_ {+},\tag{34}
$$

which satisfies the desired property of irreversibility (23) . Note that the viscosity  determines a viscous over-force response that governs the evolution of the phase-field. The model degenerates for $\eta \to 0$ to the rate-independent model considered above. 

## 3. DEGRADATION OF ENERGY IN THE FRACTURING SOLID

We focus now on the description of the bulk response of a fracturing solid and consider constitutive assumptions concerning the degradation of energy. Here, we differentiate between a simple isotropic assumption, where fracture occurs in tension and compression, and a more realistic anisotropic assumption, where the fracture occurs only in tension. 

## 3.1. Displacement field and strain tensor

In the small-strain context, we describe the motion of the fracturing solid by the macro-motion field 

$$
\boldsymbol {u}: \left\{ \begin{array}{l} \mathcal {B} \times \mathcal {T} \to \mathcal {R} ^ {\delta} \\ (\boldsymbol {x}, t) \mapsto \boldsymbol {u} (\boldsymbol {x}, t). \end{array} \right.\tag{35}
$$

$\pmb { u } \in \mathcal { R } ^ { \delta }$ is the displacement of the material point $\boldsymbol { x } \in \mathcal { B }$ at time $t \in \mathcal { T }$ . The strains are assumed to be small. Thus, the norm of the macroscopic displacement gradient $| | \nabla u | | < \varepsilon$ is bounded by a smal number . The symmetric part of this gradient defines the standard strain tensor 

$$
\boldsymbol {\varepsilon} (\boldsymbol {u}) = \nabla_ {s} \boldsymbol {u} := \frac {1}{2} [ \nabla \boldsymbol {u} + \nabla^ {\mathrm{T}} \boldsymbol {u} ]\tag{36}
$$

of the geometrically linear theory. 

## 3.2. Isotropic degradation of stored bulk energy

We focus on the standard linear theory of elasticity for isotropic solids by considering the global energy storage functional 

$$
E (\boldsymbol {u}, d) = \int_ {\mathcal {B}} \psi (\varepsilon (\boldsymbol {u}), d) \mathrm{d} V\tag{37}
$$

that depends on the displacement u and the fracture phase-field $d .$ The energy storage function $\psi$ describes the energy stored in the bulk of the solid per unit volume. A fully isotropic constitutive assumption for the degradation of energy due to fracture has the form 

$$
\boxed {\psi_ {0} (\boldsymbol {\varepsilon}, d) = [ g (d) + k ] \psi_ {0} (\boldsymbol {\varepsilon}).}\tag{38}
$$

In this multiplicative ansatz, $\psi _ { 0 }$ is a standard free energy function of an undamaged elastic solid 

$$
\psi_ {0} (\pmb {\varepsilon}) = \lambda \mathrm{tr} ^ {2} [ \pmb {\varepsilon} ] / 2 + \mu \mathrm{tr} [ \pmb {\varepsilon} ^ {2} ]\tag{39}
$$

with elastic constants $\lambda { > } 0$ and $\mu { > } 0$ . The monotonically decreasing function $g ( d )$ describes the degradation of stored energy due to evolving damage by the properties 

$$
g (0) = 1, \quad g (1) = 0, \quad g ^ {\prime} (1) = 0.\tag{40}
$$

The first two conditions include the limits for the unbroken and the fully broken case. The last constraint ensures that the elastic driving force $\beta ^ { \mathrm { e } } { : = } \hat { o } _ { d } \psi$ converges to a final value if the damage converges to the fully broken state $d = 1$ . A simple function that has the above properties i 

$$
g (d) = (1 - d) ^ {2}.\tag{41}
$$

The small positive parameter $k \approx 0$ in (38) circumvents the full degradation of the energy by leaving the artificial elastic rest energy density $k \psi _ { 0 } ( \pmb { \varepsilon } )$ at a fully broken state $d = 1$ . It is chosen as smal as possible such that the algebraic conditioning number of the applied numerical discretization method remains well-posed for partly-broken systems. 

With these constitutive assumption at hand, the evolution of stored energy 

$$
\dot {E} (\dot {\boldsymbol {u}}, \dot {d}) = \int_ {\mathcal {B}} \dot {\psi} \mathrm{d} V = \int_ {\mathcal {B}} \left\{\left(\partial_ {d} \psi\right) \dot {d} + \left(\partial_ {\boldsymbol {\varepsilon}} \psi\right): \dot {\boldsymbol {\varepsilon}} \right\} \mathrm{d} V\tag{42}
$$

is governed by the constitutive expressions 

$$
\beta^ {\mathrm{e}} := \partial_ {d} \psi = - 2 (1 - d) \psi_ {0} (\pmb {\varepsilon}) \quad \mathrm{and} \quad \pmb {\sigma} := \partial_ {\pmb {\varepsilon}} \psi = [ (1 - d) ^ {2} + k ] \pmb {\sigma} _ {0} (\pmb {\varepsilon})\tag{43}
$$

in terms of the stress tensor of a fictitious undamaged solid 

$$
\boldsymbol {\sigma} _ {0} := \lambda \operatorname{tr} [ \varepsilon ] \mathbf {1} + 2 \mu \varepsilon .\tag{44}
$$

Note that $\beta ^ { \mathrm { e } }$ is strictly negative and converges to a final value if the fracture phase-field converges to the fully broken state $d = 1$ 

## 3.3. Anisotropic degradation of stored bulk energy

In the above isotropic model, the stress degradation affects the full stress tensor. Thus, energy is released due to fracture in both tension and compression. This is physically unrealistic and limits the application of this framework to problems with exclusive presence of tensile stresses. In order to overcome this problem, we modify the assumption (38) by defining an anisotropic energy storage function 

$$
\boxed {\psi (\boldsymbol {\varepsilon}, d) = [ g (d) + k ] \psi_ {0} ^ {+} (\boldsymbol {\varepsilon}) + \psi_ {0} ^ {-} (\boldsymbol {\varepsilon})}\tag{45}
$$

based on an assumed additive decomposition of the stored energy $\psi _ { 0 }$ of the undamaged solid 

$$
\psi (\pmb {\varepsilon}) = \psi_ {0} ^ {+} (\pmb {\varepsilon}) + \psi_ {0} ^ {-} (\pmb {\varepsilon})\tag{46}
$$

into a positive part $\psi _ { 0 } ^ { + }$ due to tension and a negative part $\psi _ { 0 } ^ { - }$ due to compression. Note tha the degradation function $g$ acts only on the tension part of the stored energy. This models crack closing for different loading paths in case the strains enter the fully compressive range. We base the definition of the positive and negative parts of the energy on the spectral decomposition of the strain tensor 

$$
\pmb {\varepsilon} = \sum_ {a = 1} ^ {3} \varepsilon_ {a} \pmb {n} _ {a} \otimes \pmb {n} _ {a},\tag{47}
$$

where $\{ \varepsilon _ { a } \} _ { a = 1 \ldots 3 }$ are the principal strains and $\{ { \pmb n } _ { a } \} _ { a = 1 \ldots 3 }$ the principal strain directions. The standard quadratic energy storage function of an isotropic undamaged solid reads 

$$
\psi_ {0} (\pmb {\varepsilon}) = \lambda (\varepsilon_ {1} + \varepsilon_ {2} + \varepsilon_ {3}) ^ {2} / 2 + \mu (\varepsilon_ {1} ^ {2} + \varepsilon_ {2} ^ {2} + \varepsilon_ {3} ^ {2})\tag{48}
$$

in terms of principal strains. Based on these representations, we define the positive and the negative parts of the energies by 

$$
\psi_ {0} ^ {\pm} (\pmb {\varepsilon}) := \lambda \langle \varepsilon_ {1} + \varepsilon_ {2} + \varepsilon_ {3} \rangle_ {\pm} ^ {2} / 2 + \mu (\langle \varepsilon_ {1} \rangle_ {\pm} ^ {2} + \langle \varepsilon_ {2} \rangle_ {\pm} ^ {2} + \langle \varepsilon_ {3} \rangle_ {\pm} ^ {2})\tag{49}
$$

in terms of the two ramp functions $\langle x \rangle _ { + }$ and x<sub>−</sub> of $\mathcal { R } _ { + }$ and $\mathcal { R } _ { - }$ depicted in Figures $6 ( \mathrm { c } )$ and $6 ( \mathrm { d } )$ respectively. Note that the positive/negative parts contain contributions due to positive/negative dilatation and contributions due to positive/negative principal strains. For the anisotropic model, the evolution of free energy (42) is governed by the constitutive expressions for the energetic force and the stress tensor 

$$
\beta^ {\mathrm{e}} := \partial_ {d} \psi = - 2 (1 - d) \psi_ {0} ^ {+} (\pmb {\varepsilon}) \quad \mathrm{and} \quad \pmb {\sigma} := \partial_ {\pmb {\varepsilon}} \psi = [ (1 - d) ^ {2} + k ] \pmb {\sigma} _ {0} ^ {+} - \pmb {\sigma} _ {0} ^ {-},\tag{50}
$$

in terms of the positive and negative parts of the stress tensor 

$$
\boldsymbol {\sigma} _ {0} ^ {\pm} := \sum_ {a = 1} ^ {3} [ \lambda \langle \varepsilon_ {1} + \varepsilon_ {2} + \varepsilon_ {3} \rangle_ {\pm} + 2 \mu \langle \varepsilon_ {a} \rangle_ {\pm} ] \boldsymbol {n} _ {a} \otimes \boldsymbol {n} _ {a}\tag{51}
$$

of a fictitious undamaged solid. Here, we have used the standard result $\partial _ { \pmb { \mathscr { E } } } \varepsilon _ { a } = \pmb { n } _ { a } \otimes \pmb { n } _ { a }$ . The energetic driving force $\beta ^ { \mathrm { e } }$ is now related to the positive part of the energy and the stress degradation affects only the positive part of the stress tensor. 

## 4. GOVERNING BALANCE EQUATIONS OF COUPLED PROBLEM

## 4.1. Basic fields and boundary conditions

With the constitutive formulation of the dissipation and the energy storage in a fracturing solid outlined above, we are now able to formulate the governing equations. These equations determine the displacement field u of the solid and the fracture phase-field d introduced in (9) and (35), respectively. The extended multi-field formulation additionally uses the local driving force field $\beta$ dual to $d$ introduced in (29). With regard to the displacement field, the exterior surface of the body is decomposed via $\partial \mathcal { B } = \partial \mathcal { B } _ { u } \cup \partial \mathcal { B } _ { t }$ into a part $\partial \mathcal { B } _ { u }$ , where the displacement is prescribed by the Dirichlet condition 

$$
\pmb {u} (\pmb {x}, t) = \pmb {u} _ {\mathrm{D}} (\pmb {x}, t) \quad \text {at} \pmb {x} \in \partial \mathcal {B} _ {u}\tag{52}
$$

and a part $\partial \mathcal { B } _ { t }$ where the traction $\pmb { t } _ { \mathrm { N } } ( \pmb { x } , t )$ is prescribed by Neumann-type boundary conditions. See Figure 7(a) for a visualization. Clearly, we have $\partial \mathcal { B } _ { u } \cap \partial \mathcal { B } _ { t } = 0$ . The external mechanical loading is defined by the external power functional 

$$
P (\dot {\boldsymbol {u}}) := \int_ {\mathcal {B}} \gamma (\boldsymbol {x}, t) \cdot \dot {\boldsymbol {u}} d V + \int_ {\partial \mathcal {B} _ {t}} \boldsymbol {t} _ {N} (\boldsymbol {x}, t) \cdot \dot {\boldsymbol {u}} d A,\tag{53}
$$

where $\gamma$ is a given body force field per unit volume. With regard to the fracture phase-field, we assume Dirichlet-type condition 

$$
d (\boldsymbol {x}, t) = 1 \quad \text {   at   } \boldsymbol {x} \in \Gamma_ {\mathrm{D}},\tag{54}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/914c0c4f7d0add909e0f134e14fefc9e6a91331554094005a57ebfc921aa1ef4.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/b60d0bd16f18666395266101f52bb729e92c6670866fecb11cbc96937c478210.jpg)



(b)



Figure 7. Two-field problem of phase-field-type crack propagation in deformable solids. The displacement field u and the fracture phase-field $d$ are defined on the solid domain ${ \mathcal { B } } ,$ where gradients of the latter account for the length scales l. c is a prescribed body force field. (a) The displacement field is constrained by the Dirichlet- and Neumann-type boundary conditions $\pmb { u } = \pmb { u } _ { \mathrm { D } }$ on $\partial \mathcal { B } _ { u }$ and ${ \pmb \sigma } \cdot { \pmb n } = { \pmb t } _ { \mathrm { N } }$ on -B with $\mathcal { \bar { O } B } = \mathcal { \hat { O } B } _ { u } \cup \mathcal { \hat { O } B } _ { t }$ and (b) the fracture phase-field is constrained by the possible Dirichlet-type boundary condition $d = 1$ on $\Gamma$ and the Neumann condition $\nabla d \cdot \boldsymbol { n } = 0$ on the full surface -B.


where $\Gamma _ { \mathrm { D } } \subset \mathcal { B }$ is a possible a-priori-given sharp crack surface. The fracture phase-field $d$ is considered to be driven by the displacement u of the solid. As a consequence, we consider no prescribed external loading associated with the phase-field. 

## 4.2. Coupled balances of the two-field problem

We derive the macro- and micro-balance equations from the standard argument of virtual power. With the rate of energy storage functional (42), the dissipation functional (24) and the external power functional (53) at hand, we demand 

$$
\boxed {\dot {E} (\dot {\boldsymbol {u}}, \dot {d}) + D (\dot {d}) - P (\dot {\boldsymbol {u}}) = 0}\tag{55}
$$

for all admissible rates $\dot { \pmb u }$ and $\dot { d }$ of the displacement field and the phase-field, which satisfy the homogeneous form of the Dirichlet boundary conditions, i.e. 

$$
\dot {\boldsymbol {u}} \in \mathscr {W} _ {u} := \{\dot {\boldsymbol {u}} | \dot {\boldsymbol {u}} = \boldsymbol {0} \text {   on   } \partial \mathscr {B} _ {\boldsymbol {u}} \} \quad \text { and } \quad \dot {d} \in \mathscr {W} _ {d} := \{\dot {d} | \dot {d} = 0 \text {   on   } \partial \mathscr {B} _ {d} \}.\tag{56}
$$

The balance (55) equilibrates the external and internal virtual powers for the quasi-static process, where the latter includes energetic and dissipative parts. Insertion of the functionals and application of the Gauss theorem gives the explicit representation 

$$
\begin{array}{l} \int_ {\mathcal {B}} \{- [ \mathrm{Div} [ \partial_ {\boldsymbol {\varepsilon}} \psi ] + \gamma ] \cdot \dot {\boldsymbol {u}} + [ \partial_ {d} \psi + \partial_ {\dot {d}} \phi - \mathrm{Div} [ \partial_ {\nabla \dot {d}} \phi ] ] \dot {d} \} \mathrm{d} V \\ + \int_ {\partial \mathcal {B} _ {t}} [ \partial_ {\boldsymbol {\varepsilon}} \psi \cdot \boldsymbol {n} - t _ {\mathrm{N}} ] \cdot \dot {\boldsymbol {u}}   \mathrm{d} A + \int_ {\partial \mathcal {B} _ {f}} [ \partial_ {\nabla \dot {d}} \phi \cdot \boldsymbol {n} ] \dot {d}   \mathrm{d} A = 0. \end{array}\tag{57}
$$

Thus, we obtain for the phase-field model of fracture in elastic solids the two coupled balance equations 

$$
\boxed { \begin{array}{c} \operatorname{Div} [ \partial_ {\boldsymbol {\varepsilon}} \psi ] + \gamma = \mathbf {0} \\ \operatorname{Div} [ \partial_ {\nabla \dot {d}} \phi ] - [ \partial_ {d} \psi + \partial_ {\dot {d}} \phi ] = 0 \end{array} }\tag{58}
$$

along with the Neumann-type boundary conditions 

$$
\partial_ {\boldsymbol {\varepsilon}} \psi \cdot \boldsymbol {n} = \boldsymbol {t} _ {\mathrm{N}} \quad \text { on } \partial \mathcal {B} _ {t} \quad \text { and } \quad \partial_ {\nabla \dot {d}} \phi \cdot \boldsymbol {n} = 0 \quad \text { on } \partial \mathcal {B}.\tag{59}
$$

$( 5 8 ) _ { 1 }$ is the macroscopic equilibrium condition. (58) may be considered as a micro-balance that determines the evolution of the crack phase-field 

## 4.3. Specific equations of two- and three-field problem

We now specify the model equations for the specific choices of the dissipation function $\phi$ and the free energy function $\psi$ outlined in the Sections 1 and 2. 

4.3.1. Model I: Rate-independent setting with approximated indicator function. For the rateindependent diffuse fracture model governed by the regularized dissipation function (28), the balances (58) assume the specific form 

$$
\begin{array}{r} \mathrm{Div} [ ((1 - d) ^ {2} + k) \partial_ {\varepsilon} \psi_ {0} (\nabla_ {s} \pmb {u}) ] = \pmb {0} \\ \frac {g _ {\mathrm{c}}}{l} [ d - l ^ {2} \Delta d ] - [ 2 (1 - d) \psi_ {0} (\nabla_ {s} \pmb {u}) + \varepsilon \langle \dot {d} \rangle_ {-} ] = 0 \end{array}\tag{60}
$$

for the fully isotropic case with energy storage function (38) and 

$$
\begin{array}{r l} & {\mathrm{Div} [ ((1 - d) ^ {2} + k) \partial_ {\varepsilon} \psi_ {0} ^ {+} (\nabla_ {s} \pmb {u}) + \partial_ {\varepsilon} \psi_ {0} ^ {-} (\nabla_ {s} \pmb {u}) ] = \pmb {0}} \\ & {\frac {g _ {\mathrm{c}}}{l} [ d - l ^ {2} \Delta d ] - [ 2 (1 - d) \psi_ {0} ^ {+} (\nabla_ {s} \pmb {u}) + \varepsilon \langle \dot {d} \rangle_ {-} ] = 0} \end{array}\tag{61}
$$

for the anisotropic case with energy storage function (45). Observe that the regularization term may be interpreted as artificial viscous hardening that penalizes the energy release in the non physical range $\dot { d } { < } 0 .$ . Such a formulation can be implemented in a straightforward manner by the canonical two-fieldformulation, however, by paying the price of the penalty-type approximation of the growth constraint $( 2 3 ) _ { 2 }$ . The parameter  is an artificial regularization parameter with no direct physical meaning, which needs to be related in the numerical implementation to the conditioning number of the system matrices. Such an estimate is given in (110). The characteristics of the models in cyclic loading are depicted in Figures 8 and 10. 

4.3.2. Model II: Rate-dependent setting with thresholdfunction. For the viscous over-force model governed by the regularized dissipation function (33), the balance equations (58) assume the specific form 

$$
\begin{array}{r} \mathrm{Div} [ ((1 - d) ^ {2} + k) \partial_ {\varepsilon} \psi_ {0} (\nabla_ {s} \pmb {u}) ] = \pmb {0} \\ g _ {\mathrm{c}} l \Delta d + 2 (1 - d) \psi_ {0} (\nabla_ {s} \pmb {u}) - \beta = 0 \\ \dot {d} - \frac {1}{\eta} \Bigl \langle \beta - \frac {g _ {\mathrm{c}}}{l} d \Bigr \rangle_ {+} = 0 \end{array}\tag{62}
$$

for the $f u l l y$ isotropic case with energy storage function (38) and 

$$
\begin{array}{r l} \mathrm{Div} [ ((1 - d) ^ {2} + k) \partial_ {\varepsilon} \psi_ {0} ^ {+} (\nabla_ {s} \boldsymbol {u}) + \partial_ {\varepsilon} \psi_ {0} ^ {-} (\nabla_ {s} \boldsymbol {u}) ] = & \boldsymbol {0} \\ g _ {\mathrm{c}} l \Delta d + 2 (1 - d) \psi_ {0} ^ {+} (\nabla_ {s} \boldsymbol {u}) - \beta = & 0 \\ \dot {d} - \frac {1}{\eta} \Big \langle \beta - \frac {g _ {\mathrm{c}}}{l} d \Big \rangle_ {+} = & 0 \end{array}\tag{63}
$$

for the anisotropic case with energy storage function (45). This setting is a three-fieldformulation due to the presence of the local driving force field. The characteristics of the models in cyclic loading are depicted in Figures 9 and 10. For the case of fracture loading we may recast $( 6 3 ) _ { 3 }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/9cabecb0f521e195b1702a1a8bd17daa6d7cd69d085e2e362df143ffc7d4854c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/cd6cfe255c0909703acd23d2129e07fc43561b88b8dc14628a48387b6b72aa4e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/07293c402d7b03fa067c57e5b512e8f48c160acd6de45ab67bfbf17b45e196f4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/ba5bae49bade689810b66e21af2f01ab614db7ee6dadaf6435c225cf4838b8f9.jpg)



Figure 8. Model I: Rate-independent setting with approximated indicator function. (a) Cyclic loading and stress–strain curves for (b)  =0.01; (c) =0.05; and (d) =2.0. For small penalty parameters $\varepsilon ,$ the model shows a non-physical hysteresis in unloading–reloading.


into the form 

$$
g _ {c} \delta_ {d} \gamma + \eta \dot {d} = 2 (1 - d) \psi_ {0} ^ {+} \geqslant 0 \quad \text { for } \dot {d} > 0,\tag{64}
$$

which proves the demands (23) for thermodynamic consistency.<sup>¶</sup> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/95636bc2166c070521b018dbadb35f06a488569618b0ce68274057d2fced3fde.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/76be70c6cfe403e07a6ca6727401dcd598c6feb1fc034dd5d1c9d1cb849d77f2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/0ee3b1336fff1cd2f53911529fec7aec7e1de507ba299eb5337811003fd03ead.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/08fa090fbb77043029246a6e96e4d08f6b526b97263f1eba695931c1a1b8bb55.jpg)



Figure 9. Model II: Rate-dependent setting with threshold function. (a) Cyclic loading and stress–strain curves for (b) $\eta { = } 1 . 2 5 \times 1 0 ^ { - 4 } ; \mathrm { ( c ) } \ \eta { = } 5 . 0 \times 1 0 ^ { - 5 } ;$ and (d) $\eta = 1 \times 1 0 ^ { - 6 }$ . For large viscosity $\eta ,$ the model shows the typical effect of viscous over-stresses.


## 5. INCREMENTAL VARIATIONAL PRINCIPLES OF REGULARIZED FRACTURE

## 5.1. Time-discrete field variables in an incremental setting

The above-coupled field equations for regularized fracture can be obtained from incremental variational principles. To this end, we consider time-discrete solutions of the field variables at the discrete times $\mathbf { 0 } , t _ { 1 } , t _ { 2 } , \ldots , t _ { n } , t _ { n + 1 } , \ldots , T$ of the process interval [0, T]. In order to advance the solution within a typical time step, we focus on the finite time increment $[ t _ { n } , t _ { n + 1 } ]$ , where 

$$
\tau_ {n + 1} := t _ {n + 1} - t _ {n} > 0\tag{67}
$$

denotes the step length. In the subsequent treatment, all field variables at time $t _ { n }$ are assumed to be known. The goal then is to determine the fields at time $t _ { n + 1 }$ based on variational principles valid for the time increment under consideration. In order to obtain a compact notation, we drop in what follows the subscript n +1 and consider all variables without subscript to be evaluated at time $t _ { n + 1 }$ . In particular, we write 

$$
\boldsymbol {u} (\boldsymbol {x}) := \boldsymbol {u} (\boldsymbol {x}, t _ {n + 1}) \quad \text { and } \quad d (\boldsymbol {x}) := d (\boldsymbol {x}, t _ {n + 1})\tag{68}
$$

for the displacement and fracture phase-field at the current time $t _ { n + 1 }$ and 

$$
\boldsymbol {u} _ {n} (\boldsymbol {x}) := \boldsymbol {u} (\boldsymbol {x}, t _ {n}) \quad \text { and } \quad d _ {n} (\boldsymbol {x}) := d (\boldsymbol {x}, t _ {n})\tag{69}
$$

Copyright q 2010 John Wiley & Sons, Ltd. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/db149923982a2facbbbe56697473a27d2e60e4a072e415617fd592c8e7d2416a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/a8aff735d5b32167564bbf6e2bd021ac7d7f782aacd1033b03a1a1bc6fc6f856.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/7cff6168bc473e3f0f42ff3d9815fc5e507a7e91983325cbdc1a487017ca0b52.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/fa25ba536347dceea7b22cf0db16cc243ccdd7add2ab1b5a5ef346188d4c9117.jpg)



Figure 10. Model I: Rate-independent setting with approximated indicator function. Model Ia: damage evolution in compression and tension with (a) cyclic loading in positive and negative ranges and (b) stress–strain curve for $\varepsilon { = } 2 . 0$ . Model Ib: damage evolution in tension only with (c) cyclic loading in positive and negative ranges and (d) stress–strain curve for $\varepsilon { = } 2 . 0$


for the fields at time $t _ { n }$ . As a consequence, the rates of the displacement and the fracture phase-field are considered to be constant in the time increment (67) under consideration and defined by 

$$
\dot {\boldsymbol {u}} := (\boldsymbol {u} - \boldsymbol {u} _ {n}) / \tau \quad \text { and } \quad \dot {d} := (d - d _ {n}) / \tau .\tag{70}
$$

Note that, due to the given fields at time $t _ { n }$ , the above rates associated with the time increment (67) are linear functions of the variables (68) at the current time $t _ { n + 1 }$ . Furthermore, we use in the subsequent variational setting the dissipative driving force field 

$$
\beta (\boldsymbol {x}) := \beta (\boldsymbol {x}, t _ {n + 1})\tag{71}
$$

evaluated at the current time $t _ { n + 1 }$ as a variable in addition to the fields (68) 

## 5.2. Incremental work, energy and dissipation functionals

The construction of incremental variational principles, which determine the current field variables (68) and (71), depends critically on the definitions of the external and internal incremental work done in a typical time step. In this context, we balance the prescribed external incremental work with the internal incremental work. The latter splits into an incremental energy storage and an incremental dissipation. Associated with the time interval (67), we define the increment of work due to the external actions on the multi-field problem by 

$$
P ^ {\tau} := \int_ {t _ {n}} ^ {t _ {n + 1}} P \mathrm{d} t,\tag{72}
$$

where $P$ is the external power functional defined in (53). Taking into account the above definitions (70) of the rates, we consider the incremental work as a functional of the field variables (68) at the current time $t _ { n + 1 }$ , defined by the algorithmic expression 

$$
P ^ {\tau} (\boldsymbol {u}) = \int_ {\mathcal {B}} \gamma \cdot (\boldsymbol {u} - \boldsymbol {u} _ {n}) \mathrm{d} V + \int_ {\partial \mathcal {B} _ {t}} \boldsymbol {t} _ {\mathrm{N}} \cdot (\boldsymbol {u} - \boldsymbol {u} _ {n}) \mathrm{d} A.\tag{73}
$$

The functional has been obtained by time integration of the power functional (53). Here, $\gamma { : = }$ $\gamma ( { \pmb x } , t _ { n + 1 } )$ and $t _ { \mathrm { N } } { : = } t _ { \mathrm { N } } ( { \pmb x } , t _ { n + 1 } )$ are the prescribed body force fields and tractions evaluated at the current time $t _ { n + 1 }$ . Furthermore, we define the increment of energy stored in the solid associated with the time interval (67) by 

$$
E ^ {\tau} := \int_ {t _ {n}} ^ {t _ {n + 1}} \dot {\psi} \mathrm{d} t = E (t _ {n + 1}) - E (t _ {n}),\tag{74}
$$

where $E$ is the energy functional defined in (37). Taking into account the objective constitutive assumption (38) and (45), we consider the incremental energy as a functional of the field variables (68) at the current time $t _ { n + 1 }$ 

$$
E ^ {\tau} (\boldsymbol {u}, d) = \int_ {\mathcal {B}} \left\{\psi \left(\nabla_ {s} \boldsymbol {u}, d; \boldsymbol {x}\right) - \psi \left(\nabla_ {s} \boldsymbol {u} _ {n}, d _ {n}; \boldsymbol {x}\right) \right\} \mathrm{d} V\tag{75}
$$

governed by the free energy function $\psi .$ . Finally, we introduce an expression for the incremental dissipation in the solid associated with the time interval (67) 

$$
D ^ {\tau} := \int_ {t _ {n}} ^ {t _ {n + 1}} D \mathrm{d} t,\tag{76}
$$

where $D$ is the dissipation functional defined in (24). For the dissipation function $\phi _ { \varepsilon }$ of the rateindependent model defined in (28), we consider the incremental dissipation as a functional of the crack phase-field $( 6 8 ) _ { 2 }$ at the current time $t _ { n + 1 }$ defined by the algorithmic expression 

$$
D _ {\varepsilon} ^ {\tau} (d) = g _ {\mathrm{c}} \left[ \Gamma_ {l} (d) - \Gamma_ {l} \left(d _ {n}\right) \right] + \frac {\varepsilon}{2 \tau} \int_ {\mathscr {B}} \langle d - d _ {n} \rangle_ {-} ^ {2} \mathrm{d} V.\tag{77}
$$

Note that the dissipated work in the time increment is proportional to the increment of the fracture surface governed by the crack surface functional $\Gamma _ { l }$ defined in (8) and (10). The penalty term ensures for $\varepsilon \to \infty$ the local growth of the crack phase-field. With the crack surface density function $\gamma$ defined in (11), we write the incremental dissipation functional 

$$
D _ {\varepsilon} ^ {\tau} (d) = \int_ {\mathcal {B}} \left\{g _ {\mathrm{c}} [ \gamma (d, \nabla d) - \gamma (d _ {n}, \nabla d _ {n}) ] + \frac {\varepsilon}{2 \tau} \langle d - d _ {n} \rangle_ {-} ^ {2} \right\} \mathrm{d} V\tag{78}
$$

with the explicit representation 

$$
D _ {\varepsilon} ^ {\tau} (d) = \int_ {\mathcal {B}} \left\{\frac {g _ {\mathrm{c}}}{2 l} [ d ^ {2} - d _ {n} ^ {2} ] + \frac {g _ {\mathrm{c}} l}{2} [ | \nabla d | ^ {2} - | \nabla d _ {n} | ^ {2} ] + \frac {\varepsilon}{2 \tau} \langle d - d _ {n} \rangle_ {-} ^ {2} \right\} \mathrm{d} V.\tag{79}
$$

For the dissipation function $\phi _ { \eta }$ of the rate-dependent model defined in (33), we use the incremental dissipation functional 

$$
D _ {\eta} ^ {\tau} (d, \beta) = \int_ {\mathcal {B}} \{\beta [ d - d _ {n} ] - \frac {\tau}{2 \eta} \left\langle \beta - \frac {g _ {\mathrm{c}}}{l} d _ {n} \right\rangle_ {+} ^ {2} + \frac {g _ {\mathrm{c}} l}{2} [ | \nabla d | ^ {2} - | \nabla d _ {n} | ^ {2} ] \} \mathrm{d} V\tag{80}
$$

that additionally contains the dissipative force field $\beta$ evaluated at the current time $t _ { n + 1 }$ as defined in (71). Recall that we obtain for the limit $\eta \to 0$ of the viscosity parameter the rate-independent setting. 

## 5.3. Incremental variational principles of regularized fracture

5.3.1. A two-field variational principle for model I. A canonical incremental minimization prin ciple of phase-field-type regularized fracture in elastic solids is based on the functional 

$$
\underbrace {\Pi_ {\varepsilon} ^ {\tau} (\boldsymbol {u} , d)} _ {\text { potential }} := \underbrace {E ^ {\tau} (\boldsymbol {u} , d)} _ {\text { energy }} + \underbrace {D _ {\varepsilon} ^ {\tau} (d)} _ {\text { dissipation }} - \underbrace {P ^ {\tau} (\boldsymbol {u})} _ {\text { work }}\tag{81}
$$

formulated in terms of the incremental energy, dissipation and work functionals defined in (75), (77) and (73), respectively. In order to obtain a compact notation of the two-field variational principle, we assemble in what follows the displacement and the fracture phase-field (68) at the discrete time $t _ { n + 1 }$ in a generalized displacement vector 

$$
\pmb {\mathfrak {u}} (\pmb {x}) := [ \pmb {u} (\pmb {x}), d (\pmb {x}) ] ^ {\mathrm{T}} \in \mathcal {R} ^ {\delta + 1}.\tag{82}
$$

Furthermore, we define the objective constitutive state vector at the discrete time $t _ { n + 1 }$ 

$$
\mathfrak {c} (\boldsymbol {u}) := \left[ \nabla_ {s} \boldsymbol {u} (\boldsymbol {x}), d (\boldsymbol {x}), \nabla d (\boldsymbol {x}) \right] ^ {\mathrm{T}} \in \mathscr {R} ^ {\delta (\delta + 1) / 2 + 1 + \delta},\tag{83}
$$

which contains the strains, the fracture phase-field and its gradient. With this compact notation at hand, we may write the variational functional (81) 

$$
\Pi_ {\varepsilon} ^ {\tau} (\mathfrak {u}) = \int_ {\mathcal {B}} \{\pi_ {\varepsilon} ^ {\tau} (\mathfrak {c} (\mathfrak {u}), \mathfrak {c} (\mathfrak {u} _ {n})) - \mathfrak {g} \cdot (\mathfrak {u} - \mathfrak {u} _ {n}) \} \mathrm{d} V - \int_ {\partial \mathcal {B} _ {t}} \mathbf {t} _ {\mathrm{N}} \cdot (\mathfrak {u} - \mathfrak {u} _ {n}) \mathrm{d} A,\tag{84}
$$

where we have introduced generalized volume force and traction vectors $\mathfrak { g } : = [ \gamma , 0 ] ^ { \mathrm { T } } \in \mathcal { R } ^ { \delta + 1 }$ and $\mathbf { t } _ { \mathrm { N } } : = [ t _ { \mathrm { N } } , 0 ] ^ { \mathrm { T } } \in \mathcal { R } ^ { \delta + 1 }$ of the coupled problem at the discrete time $t _ { n + 1 }$ . We call $\pi _ { \varepsilon } ^ { \tau }$ the incremental internal work density. It has the representation 

$$
\pi_ {\varepsilon} ^ {\tau} = \psi (\nabla_ {s} \pmb {u}, d) - \psi_ {n} + \frac {g _ {\mathrm{c}}}{2 l} [ d ^ {2} + l ^ {2} | \nabla d | ^ {2} ] - g _ {\mathrm{c}} \gamma_ {n} + \frac {\varepsilon}{2 \tau} \langle d - d _ {n} \rangle_ {-} ^ {2}.\tag{85}
$$

Then, a finite-step-sized incremental minimization principle 

$$
\{\boldsymbol {u}, d \} = \operatorname{Arg} \left\{\inf _ {\boldsymbol {u}} \inf _ {d} \Pi_ {\varepsilon} ^ {\tau} (\boldsymbol {u}, d) \right\}\tag{86}
$$

determines the displacement u and the fracture phase-field d at the current time $t _ { n + 1 }$ as the minimum of the incremental functional $\Pi _ { \varepsilon } ^ { \tau }$ . The variation of the minimum principle gives the necessary condition 

$$
\delta \Pi_ {\varepsilon} ^ {\tau} = \int_ {\mathcal {B}} \left\{\left[ \partial_ {\mathfrak {c}} (\mathbf {u}) \pi_ {\varepsilon} ^ {\tau} \right] \cdot \mathfrak {c} (\delta \mathbf {u}) - \mathfrak {g} \cdot \delta \mathbf {u} \right\} d V - \int_ {\partial \mathcal {B} _ {t}} \mathbf {t} _ {\mathrm{N}} \cdot \delta \mathbf {u} d A = 0.\tag{87}
$$

Here, $\delta \mathbf { u } : = [ \delta \pmb { u } , \delta d ] ^ { \mathrm { T } }$ with $\delta \pmb { u } \in \mathcal { W } _ { u }$ and $\delta d \in \mathcal { W } _ { d }$ contains admissible variations of the displacement and the fracture phase-field at the current time according to (56). A re-formulation of (87) identifies by application of the Gauss theorem the field equations (60) or (61) and the Neumann type boundary conditions (59), evaluated at the discrete time $t _ { n + 1 }$ , as the Euler equations of the incremental variational principle (86). 

5.3.2. A three-field variational principle for model II. An extended incremental variational prin ciple of phase-field-type regularized fracture in elastic solids is formulated in terms of the functiona 

$$
\underbrace {\Pi_ {\eta} ^ {\tau} (\boldsymbol {u} , d , \beta)} _ {\text { potential }} := \underbrace {E ^ {\tau} (\boldsymbol {u} , d)} _ {\text { energy }} + \underbrace {D _ {\eta} ^ {\tau} (d , \beta)} _ {\text { dissipation }} - \underbrace {P ^ {\tau} (\boldsymbol {u})} _ {\text { work}},\tag{88}
$$

where we have used the penalty-type incremental dissipation functional (80). In order to obtain a compact notation of the three-field variational principle, we define the extended generalized displacement vector 

$$
\boldsymbol {u} (\boldsymbol {x}) := [ \boldsymbol {u} (\boldsymbol {x}), d (\boldsymbol {x}), \beta (\boldsymbol {x}) ] ^ {\mathrm{T}} \in \mathscr {R} ^ {\delta + 2}\tag{89}
$$

and the extended constitutive state vector 

$$
\mathfrak {c} (\boldsymbol {u}) := \left[ \nabla_ {s} \boldsymbol {u} (\boldsymbol {x}), d (\boldsymbol {x}), \nabla d (\boldsymbol {x}), \beta (\boldsymbol {x}) \right] ^ {\mathrm{T}} \in \mathscr {R} ^ {\delta (\delta + 1) / 2 + 2 + \delta}\tag{90}
$$

at the discrete time $t _ { n + 1 }$ . We then write the variational functional (88) 

$$
\Pi_ {\eta} ^ {\tau} (\mathfrak {u}) = \int_ {\mathscr {B}} \left\{\pi_ {\eta} ^ {\tau} \left(\mathfrak {c} (\mathfrak {u}), \mathfrak {c} \left(\mathfrak {u} _ {n}\right)\right) - \mathfrak {g} \cdot \left(\mathfrak {u} - \mathfrak {u} _ {n}\right) \right\} d V - \int_ {\partial \mathscr {B} _ {t}} \mathbf {t} _ {\mathrm{N}} \cdot \left(\mathfrak {u} - \mathfrak {u} _ {n}\right) d A\tag{91}
$$

in terms of the generalized volume force and traction vectors $\begin{array} { r } { \mathbf { g } : = [ \gamma , 0 , 0 ] ^ { \mathrm { T } } \in \mathcal { R } ^ { \delta + 2 } } \end{array}$ and $\mathbf { t } _ { \mathrm { N } } : =$ $[ \pmb { t } _ { \mathrm { N } } , 0 , 0 ] ^ { \mathrm { T } } \in \mathcal { R } ^ { \delta + \widetilde { 2 } }$ at discrete time $t _ { n + 1 }$ . We define the incremental internal work density of the three-field problem by 

$$
\pi_ {\eta} ^ {\tau} = \psi (\nabla_ {s} \pmb {u}, d) - \psi_ {n} + \beta [ d - d _ {n} ] - \frac {\tau}{2 \eta} \left\langle \beta - \frac {g _ {\mathrm{c}}}{l} d _ {n} \right\rangle_ {+} ^ {2} + \frac {g _ {\mathrm{c}} l}{2} [ | \nabla d | ^ {2} - | \nabla d _ {n} | ^ {2} ].\tag{92}
$$

Then, the finite-step-sized incremental minimization principle 

$$
\{\boldsymbol {u}, d, \beta \} = \operatorname{Arg} \left\{\inf _ {\boldsymbol {u}} \inf _ {d} \sup _ {\beta} \Pi_ {\eta} ^ {\tau} (\boldsymbol {u}, d, \beta) \right\}\tag{93}
$$

determines the current displacement ${ \pmb u } ,$ , the fracture phase-field $d$ and its dissipative dual $\beta$ at the current time $t _ { n + 1 }$ as a saddle point of the incremental functional $\Pi _ { \eta } ^ { \tau }$ . The necessary condition of the above principle reads 

$$
\delta \Pi_ {\eta} ^ {\tau} = \int_ {\mathcal {B}} \left\{\left[ \partial_ {\mathfrak {c} (\mathbf {u})} \pi_ {\eta} ^ {\tau} \right] \cdot \mathfrak {c} (\delta \mathbf {u}) - \mathfrak {g} \cdot \delta \mathbf {u} \right\} d V - \int_ {\partial \mathcal {B} _ {t}} \mathbf {t} _ {\mathrm{N}} \cdot \delta \mathbf {u} d A = 0.\tag{94}
$$

Here, $\delta \mathbf { u } : = [ \delta \pmb { u } , \delta d , \delta \beta ] ^ { \mathrm { T } }$ with -u $\in \mathcal { W } _ { u }$ and $\delta d \in \mathcal { W } _ { d }$ contains admissible variations of the displacement, the fracture phase-field and the dissipative force at the current time according to (56). 

The reformulation based on the Gauss theorem identifies the field equations (62) and (63) and Neumann-type boundary conditions (59) at discrete time $t _ { n + 1 }$ as the Euler equations of the incremental variational principle (93). 

## 5.4. FE-discretization of incremental variational principles

5.4.1. Discrete two-field variational principle for model I. tion of the coupled problem by a finite element method. Let $\mathfrak { T } ^ { h }$ denote a finite element triangulation of the solid domain B. The index h indicates a typical mesh size based on $E ^ { h }$ finite element domains $\mathcal { B } _ { e } ^ { h } \in \mathfrak { T } ^ { h }$ and $N ^ { h }$ global nodal points. Associated with the triangulation $\mathfrak { T } ^ { h }$ , we write the finite element interpolations of the above-introduced generalized displacement vector (82) and the constitutive state vector (83) of the two-field formulation in the compact form 

$$
\mathfrak {u} ^ {h} (\boldsymbol {x}) = \boldsymbol {N} (\boldsymbol {x}) \boldsymbol {d} \quad \mathrm{and} \quad \mathfrak {c} ^ {h} (\boldsymbol {d}) = \boldsymbol {B} (\boldsymbol {x}) \boldsymbol {d}\tag{95}
$$

in terms of the generalized nodal displacement vector $\pmb { d } \in \mathcal { R } ^ { ( \delta + 1 ) N ^ { h } }$ , which contains the displacements and the fracture phase-field at a typical nodal point of the finite element mesh. N and B are symbolic representations of the global matrices of shape functions for the coupled problem. Clearly, these global arrays are never formulated explicitly, but represent symbolically the interpo lations on all finite element domains $\mathcal { B } _ { e } ^ { h } \in \mathfrak { T } ^ { h }$ . In the subsequent numerical model problems, we use identical $C ^ { 0 }$ -compatible interpolations for the displacement and the fracture phase-field. Note that the global displacement vector $\pmb { d } = \mathsf { A } _ { e = 1 } ^ { E ^ { h } } \pmb { d } ^ { \mathrm { e } }$ is formed from the generalized element displacement vectors $\pmb { d } ^ { \mathrm { e } }$ by a standard finite element assembling procedure.<sup></sup> 

The shape matrices $N ( x )$ and $\pmb { { \cal B } } ( \pmb { x } )$ introduced above govern the algebraic expressions of the incremental work, energy and dissipation functionals. With the discretization of the generalized displacement and the constitutive state fields (95), we write the spatial discretization of the incre mental two-field functional (97) 

$$
\Pi_ {\varepsilon} ^ {h} (\boldsymbol {d}) = \int_ {\mathcal {B}} \left\{\pi_ {\varepsilon} ^ {\tau} \left(\boldsymbol {B} \boldsymbol {d}, \boldsymbol {B} \boldsymbol {d} _ {n}\right) \mathrm{d} V - \mathfrak {g} \cdot N (\boldsymbol {d} - \boldsymbol {d} _ {n}) \right\} \mathrm{d} V - \int_ {\partial \mathcal {B} _ {t}} \mathfrak {t} _ {\mathrm{N}} \cdot N (\boldsymbol {d} - \boldsymbol {d} _ {n}) \mathrm{d} A.\tag{97}
$$

Then, the finite-step-sized discrete minimization principle 

$$
\{\pmb {d} \} = \mathrm{Arg} \left\{\inf _ {\pmb {d}} \Pi_ {\varepsilon} ^ {h} (\pmb {d}) \right\}\tag{98}
$$

determines the generalized nodal displacement d of the finite element mesh at the current time $t _ { n + 1 }$ . The necessary condition of the discrete variational problem (98) reads 

$$
\Pi_ {\varepsilon , \boldsymbol {d}} ^ {h} = \int_ {\mathcal {B}} \left\{\boldsymbol {B} ^ {\mathrm{T}} \left[ \partial_ {\boldsymbol {\mathfrak {c}} ^ {h} (\boldsymbol {d})} \pi_ {\varepsilon} ^ {\tau} \right] - N ^ {\mathrm{T}} \mathfrak {g} \right\} \mathrm{d} V - \int_ {\partial \mathcal {B} _ {t}} \boldsymbol {N} ^ {\mathrm{T}} \mathbf {t} _ {\mathrm{N}} \mathrm{d} A = \mathbf {0}\tag{99}
$$

and provides a nonlinear algebraic system for the determination of the generalized nodal displace ments $\mathbf { \delta } \mathbf { \mathbf { \ d } } .$ In a standard Newton-type iteration of the nonlinear algebraic system (99), we update the generalized displacements by the algorithm 

$$
\boldsymbol {d} \Leftarrow \boldsymbol {d} - [ \Pi_ {\varepsilon , \boldsymbol {d}} ^ {h} \boldsymbol {d} ] ^ {- 1} [ \Pi_ {\varepsilon , \boldsymbol {d}} ^ {h} ]\tag{100}
$$

in terms of the monolithic tangent matrix of the coupled problem 

$$
\Pi_ {\varepsilon , \boldsymbol {d} \boldsymbol {d}} ^ {h} = \int_ {\mathscr {B}} \boldsymbol {B} ^ {\mathrm{T}} [ \partial_ {\boldsymbol {\mathfrak {c}} ^ {h} (\boldsymbol {d}) \boldsymbol {\mathfrak {c}} ^ {h} (\boldsymbol {d})} ^ {2} \pi_ {\varepsilon} ^ {\tau} ] \boldsymbol {B} \mathrm{d} V.\tag{101}
$$

Observe that the symmetry of the tangent matrix is directly related to the variational structure of the phase-field model of fracture under consideration. The iterative update (100) is performed until convergence is achieved in the sense $| \Pi _ { \varepsilon , d } ^ { h } | { < } \mathrm { t o l }$ . Observe that the finite element residual and tangent are governed by the generalized stress and tangent arrays 

$$
\boldsymbol {S} _ {\varepsilon} := \partial_ {\mathfrak {c}} \pi_ {\varepsilon} ^ {\tau} (\mathfrak {c} ^ {h}, \mathfrak {c} _ {n} ^ {h}; \boldsymbol {x}) \quad \text {and} \quad \mathbb {C} _ {\varepsilon} := \partial_ {\mathfrak {c c}} ^ {2} \pi_ {\varepsilon} ^ {\tau} (\mathfrak {c} ^ {h}, \mathfrak {c} _ {n} ^ {h}; \boldsymbol {x})\tag{102}
$$

as the first and second derivatives of the incremental internal work density $\pi _ { \varepsilon } ^ { \tau }$ defined in (85) by the discretized constitutive state vector $\mathbf { c } ^ { h }$ at current time $t _ { n + 1 }$ . These arrays are a critical ingredient of the proposed variational formulation and make the notation extremely compact.<sup>∗∗</sup> 

5.4.2. Discrete three-field variational principle for model II. Associated with the triangulation $\mathfrak { T } ^ { h }$ , we write the finite element interpolations of the above-introduced generalized displacement vector (89) and the constitutive state vector (90) of the three-field formulation in the compact form 

$$
\mathfrak {u} ^ {h} (\boldsymbol {x}) = N (\boldsymbol {x}) \boldsymbol {d} \quad \text { and } \quad \mathfrak {c} ^ {h} (\boldsymbol {d}) = B (\boldsymbol {x}) \boldsymbol {d}
$$

(103) 

in a notation identical to the two-field setting (95); however, in terms of an extended generalized nodal displacement vector $\pmb { d } \in \mathcal { R } ^ { ( \delta + 2 ) N ^ { h } }$ . It contains the displacements, the fracture phase-field and additionally the dissipative force at a typical nodal point of the finite element mesh. N and B are symbolic representations of global matrices of shape functions for the three-field problem.†† We write the spatial discretization of the incremental two-field functional (105) 

$$
\Pi_ {\eta} ^ {h} (\boldsymbol {d}) = \int_ {\mathcal {B}} \left\{\pi_ {\eta} ^ {\tau} \left(\boldsymbol {B} \boldsymbol {d}, \boldsymbol {B} \boldsymbol {d} _ {n}\right) \mathrm{d} V - \mathfrak {g} \cdot N (\boldsymbol {d} - \boldsymbol {d} _ {n}) \right\} \mathrm{d} V - \int_ {\partial \mathcal {B} _ {t}} \mathfrak {t} _ {\mathrm{N}} \cdot N (\boldsymbol {d} - \boldsymbol {d} _ {n}) \mathrm{d} A.\tag{105}
$$

Then, the finite-step-sized discrete minimization principle 

$$
\{\boldsymbol {d} \} = \operatorname{Arg} \left\{\underset {\boldsymbol {d}} {\text { stat }} \Pi_ {\eta} ^ {h} (\boldsymbol {d}) \right\}\tag{106}
$$

determines the generalized nodal displacement $\pmb { d }$ of the finite element mesh at the current time $t _ { n + 1 }$ . The necessary condition of the discrete variational problem (106) reads 

$$
\Pi_ {\eta , \boldsymbol {d}} ^ {h} = \int_ {\mathcal {B}} \left\{\boldsymbol {B} ^ {\mathrm{T}} \left[ \partial_ {\boldsymbol {\mathfrak {c}} ^ {h} (\boldsymbol {d})} \pi_ {\eta} ^ {\tau} \right] - N ^ {\mathrm{T}} \mathfrak {g} \right\} \mathrm{d} V - \int_ {\partial \mathcal {B} _ {t}} N ^ {\mathrm{T}} \mathbf {t} _ {\mathrm{N}} \mathrm{d} A = \mathbf {0}\tag{107}
$$

and provides a nonlinear algebraic system for the determination of the generalized nodal displacements d. The solution of this nonlinear algebraic system by a Newton-type solver is in full analogy to (100) based on the symmetric tangent matrix 

$$
\Pi_ {\eta , \boldsymbol {d} \boldsymbol {d}} ^ {h} = \int_ {\mathcal {B}} \boldsymbol {B} ^ {\mathrm{T}} [ \partial_ {\boldsymbol {\mathfrak {c}} ^ {h} (\boldsymbol {d}) \boldsymbol {\mathfrak {c}} ^ {h} (\boldsymbol {d})} ^ {2} \pi_ {\eta} ^ {\tau} ] \boldsymbol {B} \mathrm{d} V\tag{108}
$$

of the coupled three-field problem. The finite element residual and tangent are governed by the extended generalized stress and tangent arrays 

$$
\boldsymbol {S} _ {\eta} := \partial_ {\mathfrak {c}} \pi_ {\eta} ^ {\tau} (\mathfrak {c} ^ {h}, \mathfrak {c} _ {n} ^ {h}; \boldsymbol {x}) \quad \text {and} \quad \mathbb {C} _ {\eta} := \partial_ {\mathfrak {c c}} ^ {2} \pi_ {\eta} ^ {\tau} (\mathfrak {c} ^ {h}, \mathfrak {c} _ {n} ^ {h}; \boldsymbol {x}),\tag{109}
$$

i.e. the first and second derivatives of the incremental internal work density $\pi _ { \eta } ^ { \tau }$ defined in (92) by the discretized extended constitutive state vector $\mathbf { c } ^ { h }$ at current time $t _ { n + 1 }$ 

## 6. REPRESENTATIVE NUMERICAL EXAMPLES

We demonstrate the performance of the proposed regularized brittle fracture models by means of some representative numerical studies. 

††Shapes for Three-field Setting. For two-dimensional plane strain problems $\delta = 2$ , the extended generalized displacement and the constitutive state vectors read $\mathbf { u } = [ u _ { 1 } , \tilde { u _ { 2 } } , d , \beta ]$ and $\pmb { \mathfrak { c } } = [ u _ { 1 , 1 } , u _ { 2 , 2 } , u _ { 1 , 2 } + u _ { 2 , 1 } , d , d , _ { 1 } , d , _ { 2 } , \beta ] .$ . Associated with node I of a standard finite element e, the finite element interpolation matrices have the form 

$$
\boldsymbol {N} _ {I} ^ {\mathrm{e}} = \left[ \begin{array}{c c c c} N & 0 & 0 & 0 \\ 0 & N & 0 & 0 \\ 0 & 0 & M & 0 \\ 0 & 0 & 0 & G \end{array} \right] _ {I} \quad \text { and } \quad \boldsymbol {B} _ {I} ^ {\mathrm{e}} = \left[ \begin{array}{c c c c c c c} N _ {, 1} & 0 & N _ {, 2} & 0 & 0 & 0 & 0 \\ 0 & N _ {, 2} & N _ {, 1} & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & M & M _ {, 1} & M _ {, 1} & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & G \end{array} \right] _ {I} ^ {\mathrm{T}}\tag{104}
$$

in terms of the shape function $N _ { I } , \ M _ { I } , \ G _ { I }$ at note I and their derivatives. In the subsequent examples, we use identical interpolations of the displacement, the fracture phase-field and the dissipative force by setting $\dot { G _ { I } } = M _ { I } = N _ { I }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/c7996ead24cdbba9a12e9cb58e0f4a657d40ccfb7d392bae744f4eba3c533ee9.jpg)



Figure 11. Single-edge-notched tension test. Boundary conditions and geometry, discretized with three-noded triangular elements.


## 6.1. Single-edge-notched tension test

We first investigate a squared plate with a horizontal notch placed at middle height from the left outer surface to the center of the specimen. The geometric setup is depicted in Figure 11. In order to capture the crack pattern properly, the mesh is refined in areas where the crack is expected to propagate, i.e. in the center strip of the specimen. For a discretization with 20 000 elements an effective element size of $h { \approx } 1 . 0 \times 1 0 ^ { - 3 } \mathrm { m m }$ , for a discretization with 30 000 elements an effective element size of $h \approx 0 . 6 \times 1 0 ^ { - 3 }$ mm in the critical zone is obtained. The elastic constants are chosen as $\lambda = 1 2 1$ $1 5 3 8 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ and $\mu { = } 8 0 . 7 6 9 2 \mathrm { k N / m m } ^ { 2 }$ , the critical energy release rate as $g _ { \mathrm { c } } { = } 2 . 7 \times 1 0 ^ { - 3 } \mathrm { k N / m m }$ . The computation is performed in a monotonic displacement-driven context with constant displacement increments $\Delta u { \stackrel { - } { = } } 1 \times 1 0 ^ { - 5 }$ mm. In order to point out the effects that arise due to the length-scale parameter l and the viscosity $\eta ,$ , different simulations with both models (61) and (63) are performed. For fixed length-scale parameters $l _ { 1 } = 0 . 0 3 7 5$ mm and $l _ { 2 } { = } 0 . 0 0 7 5 \mathrm { m m }$ the influence of the viscosity is analyzed. The obtained load-deflection curves are depicted in Figure 12. We observe for vanishing viscosity $\eta \to 0$ the rate-independent limit, which is given by the two-field model (61). Comparing (85) and (92), we relate in the subsequent simulations the regularization parameters  and  by 

$$
\eta \approx \frac {\tau^ {2}}{\varepsilon} \Leftrightarrow \varepsilon \approx \frac {\tau^ {2}}{\eta}.\tag{110}
$$

The resulting crack patterns at different stages of the deformation are illustrated in Figure 13. As expected, the sharpest crack pattern is obtained for the smallest length-scale parameter $l _ { 2 } =$ 0.0075 mm. The subsequent study analyzes the influence of the discretization on the global response. For a discretization with 20 000 elements, an approximate effective element size in the critical zone of $h \approx 1 . 0 \times 1 0 ^ { - 3 }$ mm is obtained. In order to check objectivity, the same simulation as discussed in Figure 12(b) is repeated with a finer discretization of 30 000 elements, leading to an effective element size of $h \approx 0 . 6 \times 1 0 ^ { - 3 }$ mm. The comparison of both structural responses in Figure 14 leads to the conclusion that results are mesh-independent. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/d891eac23a8cd7f57f101c4f0330c8f4db04f7c7e58410727c4143c7231b3f6c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/35630603e10c2c886b5d0b9bb42a7bbf08e51aa96c1ef42f042e7e0b2b5c44c2.jpg)



Figure 12. Single-edge-notched tension test. Load-deflection curves for a length scale: (a) $l _ { 1 } = 0 . 0 3 7 5$ mm and (b) $l _ { 2 } = 0 . \bar { 0 } 0 7 5$ mm obtained for different viscosities  of model (63). Results are compared with the rate-independent limit case given by the two-field formulation (61) for $\varepsilon { = } 1 0 . 0 \mathrm { k N s } / \mathrm { m m } ^ { 2 }$


## 6.2. Pure shear test of notched specimen

We now apply the formulation of regularized fracture to a shear test of a rectangular notched specimen. This example has previously been studied by Bourdin et al. [8]. The boundary value problem depicted in Figure 15 is discretized by 30 000 triangular elements. A pure shear deforma tion is applied where the displacement load direction u has the angle $\alpha = 0 ^ { \circ }$ toward the horizontal plane. In the above-mentioned reference, this system was analyzed for different angles , where for $0 ^ { \circ } \leqslant \alpha \leqslant 7 ^ { \circ }$ crack branching was observed. Throughout the analysis, the Lame constants are chosen as $\lambda { = } 1 2 1 . 1 5 3 8 \mathrm { k N / m m } ^ { 2 }$ and $\mu { = } 8 0 . 7 6 9 2 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ , the critical energy release rate as $g _ { \mathrm { c } } =$ $2 . 7 \times 1 0 ^ { - 3 } \mathrm { k N } _ { / }$ /mm, the length scale as $l { = } 0 . 0 1$ mm and the viscosity as $\eta { = } 2 . 5 \times 1 0 ^ { - 5 } \mathrm { k N s / m m } ^ { 2 }$ The specimen is subject to a displacement-driven deformation by prescribed incremental displace ments $\Delta u = 1 \times 1 0 ^ { - 4 }$ mm in the first 100 iterations. The subsequent deformation demands an adjustment of the displacement increments to $\Delta u = 1 \times 1 0 ^ { - 6 }$ mm up to the final deformation. Fo a small amount of the viscosity in model (63), this behavior is characterized by a brutal crack growth. In Figure 16, the crack evolution at different stages of the deformation is displayed fo the models (62) and (63), respectively. Following Bourdin et al. [8], crack branching for an angle $0 ^ { \circ } \leqslant \alpha \leqslant 7 ^ { \circ }$ can be observed. This case is depicted in Figures 16(a), (b), (c), (d). The branching is directly related to the specific choice of the free energy, which allows for cracking in compression. As discussed in the previous section this drawback can be overcome by model (63), where only tensile energies are regarded as crack driving quantities. The corresponding crack approximations are depicted in Figures 16(e), (f), (g), (h). The associated load-deflection curves are shown in Figure 17, where the model restricted to tensile cracks of course shows a stiffer response in the post-critical range. Clearly, the improved model (63) represents the physically realistic approach. In the subsequent treatment, we analyze with this model more complex boundary value problems. 

## 6.3. Symmetric three point bending test

This benchmark represents a three point bending test of a simply supported notched beam. The geometric setup as well as the loading are illustrated in Figure 18. The discretization is refined in the expected crack propagation zone, yielding a discretization with 20 000 elements and an effective element size of $h \tilde { \approx } \bar { 0 } . 8 \times 1 0 ^ { - 3 }$ mm. The elastic parameters are chosen as $\lambda { = } 1 2 . 0 0 \mathrm { k N / m m } ^ { 2 }$ and $\mu { = } 8 . 0 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ , the critical energy release rate as $g _ { \mathrm { c } } { = } 5 . 0 \times 1 0 ^ { - 4 } \mathrm { k N / m m }$ . The computation is performed in a monotonic displacement-driven context with constant displacement increments $\Delta \bar { u } = 1 \times 1 0 ^ { - 3 }$ mm in the first 40 steps. The subsequent simulation then demands an adjustment of the displacement increment to $\Delta u = 1 \times 1 0 ^ { - 5 }$ mm. Figure 19 compares the global response of the system with the results obtained from a model based on configurational-force-driven crack prop agation introduced by Guerses and Miehe [20], for a simulation with 10 360 elements. Figure 19 compares for the length-scale parameter $l { = } 0 . 0 3$ mm the solutions obtained by the rate-independent two-field formulation (61) involving the parameter  and the extended viscous three-field formulation (63) involving the viscosity . Clearly, the load-deflection curves of the three-field formu lation depend on the viscosity parameter . It can be observed that for the small viscosit $\eta =$ $1 \times 1 0 ^ { - 6 } \mathrm { { \bar { k } N s / m m } } ^ { 2 }$ , the results of the three-field formulation almost coincide with those of the two-field formulation. In this range,  plays the role of a numerical stabilization parameter with almost no visible physical effect. In the post-critical range, the results of the phase-field model differ from those of the sharp crack model due to the remaining artificial rest energy $k \psi _ { 0 } ^ { + }$ . The resulting contour plots of the two-field formulation (61) with $\varepsilon { = } 1 0 \mathrm { k N s } / \mathrm { m m } ^ { 2 }$ and the extended three-field formulation (63) with $\eta { = } 1 \times 1 0 ^ { - 6 } \mathrm { k N s / m m } ^ { 2 }$ with the length scale $l { = } 0 . 0 3$ mm are shown in Figure 20. Blue and red colors correspond to the undamaged and the fully cracked material, respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/a220acccba6ef8f7fa751f9d07ac8807b0785a74399604aac4ba57e1ca69478b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/9d9de40e9094ff9880827fd34825a1ab3cd0a9ee43baa4eca346f9a86cf68a3a.jpg)



(a)



(d)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/e28cd94d8494c7ebb4229b813488db790e5dbaacb0c55326b2e17471136d2faf.jpg)



(e)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/fff7292c2e24280bacdfa3ef5c078dbddadab4316d1a58513586b57df06a279d.jpg)



(f)



Figure 13. Single-edge-notched tension test. Crack pattern of the three-field formulation (63) at a displacement of (a) $u = 5 . 5 \times 1 0 ^ { - 3 }$ mm; (b) $u = 5 . 9 \times 1 0 ^ { - 3 }$ mm; (c) $u = 6 . 3 \times 1 0 ^ { - 3 }$ mm for a length scale of $l _ { 1 } { = } 0 . 0 3 7 5 \mathrm { m m } ;$ (d) $u = 5 . 5 \times 1 0 ^ { - 3 }$ mm; (e) $u = 5 . 9 \times 1 0 ^ { - 3 }$ mm; and (f) $u = 6 . 3 \times 1 0 ^ { - 3 }$ mm for a length scale of $l _ { 2 } { = } 0 . 0 0 7 5 \mathrm { m m }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/9582440ca708332129c31ddfa186adc66b9b79157e30aff53b53bb11880361a6.jpg)



Figure 14. Single-edge-notched tension test. Objective load-deflection curves for simulations with 20 000 and 30 000 elements carried out with the same viscosity $\eta { = } 4 \times 1 0 ^ { - 6 } \mathrm { k N s / m m } ^ { 2 }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/f6ed9b0a57ebf8c31cf8f502cd1cdae55a87370b83bb1ba536aa18031f3585ce.jpg)



Figure 15. Pure shear test. Boundary value problem and discretization.


## 6.4. Asymmetric notched three point bending test

Aim of this benchmark is the investigation of curved crack patterns. The asymmetric three point bending test was analyzed experimentally and numerically in Bittencourt et al. [28]. It concerns an asymmetrically-notched beam with three holes. The setup of the problem is shown in Figure 21. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/069a05d0e364048904ca659e7b8f3c39f5c42517e14566ace0770e7331c5fc6f.jpg)



(d)



(h)



Figure 16. Pure shear test. Crack patterns of the three-field formulation with model II version (62) are depicted on the left-hand side at the deformation state: (a) $u { = } 9 . 0 \times 1 0 ^ { - 3 } \mathrm { m m } ;$ (b) $u = 1 1 . 0 \times 1 0 ^ { - 3 }$ <sup>3</sup> mm; (c) $u = 1 5 . 0 \times 1 0 ^ { - 3 } \mathrm { m m } ;$ (d) $u = 1 7 . 0 \times 1 0 ^ { - 3 } \mathrm { m m }$ . Results obtained with model II version (63) are given on the right-hand side at the deformation state: (e) $u { = } 9 . 0 \times 1 0 ^ { - 3 } \mathrm { m m } ;$ (f) $u = 1 1 . 0 \times 1 0 ^ { - 3 } \mathrm { m m } ;$ (g) $u = 1 5 . 0 \times 1 0 ^ { - 3 }$ mm; and (h) $u = 1 7 . 0 \times 1 0 ^ { - 3 } \mathrm { m m }$


The material parameters are the elastic constants $\lambda { = } 1 2 . 0 0 \mathrm { k N / m m } ^ { 2 } , ~ \mu { = } 8 . 0 \mathrm { k N / m m } ^ { 2 }$ and the critical energy release rate $g _ { \mathrm { c } } { = } 1 \times 1 0 ^ { - 3 } \mathrm { k N / m m }$ . A first aspect of the investigation is to point out the influence of the mesh density as well as the regularization parameter l on the results. Figure 22 shows the crack trajectories for different discretizations. According to (19), the length scale parameter l is always chosen to be twice the element size. The viscosity parameter is set to $\eta { = } 2 . \dot { 5 } \times 1 0 ^ { - 5 } \mathrm { k N s / m m } ^ { 2 }$ . For a coarse mesh we observe a crack initiation at the first hole. This crack path does not agree with the experimental observation. With increasing mesh density, the crack initiation at the first hole disappears and one obtains the accurate crack path. This demonstrates the dramatic influence of the finite element mesh on the results. Observe that an extremely fine mesh is needed to resolve the right crack pattern. Figure 23 compares the simulation with the experimental crack trajectories obtained by Bittencourt et al. [28]. Figures 23(a)–(c)) are based on the three-field regularized fracture model (63), Figure 23(d) is a result of the configurational force model obtained in Miehe and Guerses [20] and finally, Figure 23(e) is the experimental result of Bittencourt et al. [28]. The first two pictures illustrate the contour plots of a mesh with 58 000 elements. While the first crack path is computed with the viscosity $\dot { \eta } { = } 2 . 5 \times 1 0 ^ { - 5 } \mathrm { k N s / m m } ^ { 2 }$ , the value $\eta =$ $0 . 1 \times 1 0 ^ { - 5 } \mathrm { k N s } / \mathrm { m m } ^ { 2 }$ was used for the second one. In the first picture, one observes a slight crack initiation at the first hole. In order to obtain the accurate crack path with $\eta { = } 2 . 5 \times 1 0 ^ { - 5 } \mathrm { k } \mathrm { \bar { N } s } / \mathrm { m m } ^ { 2 }$ a higher mesh density was needed, see 23(c)). Again, this shows the strong influence of both the mesh density as well as the viscosity on the results. A comparison of the results 23(b)–(e) shows that both models capture the curved crack pattern very well. The configurational force model with the adaptive reorientation of the segments at the crack tip yields crack trajectories for quite rough meshes. However, such a formulation is of limited applicability, because it cannot be applied to the modeling of crack initiation in perfect solids and does not allow for crack branching. These problems are overcome by the regularized crack modeling. However, note that the sharp limit case is recovered only for very small length-scale parameters l. Thus, we need an extremely fine mesh resolution in order to obtain the accurate crack path. Figure 24 shows the evolution of the contou plots of the mesh with 79 000 elements. Again, blue and red colors correspond to the undamaged and the fully damaged, i.e. the cracked material, respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/8c9f6cea6ed60a1cd2e631d3abbd867fabd0a8e718aaf12bb74443fba202ec88.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/bb384d981af8a6947ed9b377f0780eab6fa06d842425a6c0af61f9a235c8361a.jpg)



Figure 17. Pure shear test. Load-deflection curves for model II: (a) version (62) and (b) version (63).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/3f8e31a563a996206f52661ff78dc922f4d7a06731f7b904e8e9de58e6cebf2d.jpg)



Figure 18. Symmetric three-point bending test. Boundary value problem.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/d30d91871773af5bb56b5fb98ed9cdb37bfce9f597df2a1b0d8905a3a9d82754.jpg)



Figure 19. Symmetric three-point bending test. Load-deflection curves of two-field formulation (61) and extended three-field formulation (63) for a length scale l =0.03mm obtained for different viscosities . Both formulations are compared with the material force-based algorithm, see Miehe and Gurses¨ [20].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/8f6b25876308cfe169d41c733c9cccd297ec69562d3ad104a34de99fd13d58ad.jpg)



(d)



(h)



Figure 20. Symmetric three-point bending test. Results of the two-field model (61) are depicted on the left-hand side at the deformation state: (a) $u = 4 . 0 \times 1 0 ^ { - 2 }$ mm; (b) $u = 4 . 2 \times 1 0 ^ { - 2 }$ mm; (c) $u = 5 . 0 \times 1 0 ^ { - 2 }$ mm; and (d) $u = 7 . 1 \times 1 0 ^ { - 2 }$ mm. Results of the time-regularized three-field formulation (63) are shown on the right-hand side at the deformation state: (e) $u = 4 . \overset { \cdot } { 0 } \times 1 0 ^ { - 2 }$ mm; (f) $u = 4 . 2 \times 1 0 ^ { - 2 }$ mm; (g) $u = 5 . 0 \times 1 0 ^ { - 2 }$ mm; and (h) $u { = } 7 . 1 \times 1 0 ^ { - 2 } \mathrm { m m }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/1a445933313e1678bb07f3add5349a67ec8c9622b85d7ece25cd311ecd9ad90b.jpg)



Figure 21. Asymmetric notched three-point bending test. Geometry, loading and boundary conditions from Bittencourt et al. [28]. The three holes have a diameter of 0.5.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/353407ba6ad5cd662693e3dba31dc16217a7f0f32778b9561d6f0d87fa94ad35.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/dae90ae01b13515cb1b6304af17ccffd2244d410eff5bd93b6ca88837c777286.jpg)



(b)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/9977ff55ffed2b88f0454da3e11359015009d6ec477bcc7058198970aa0bbad2.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/3da6280c944bd5b8005e422abb44796e60159bfb001bccb518dcd15246be99c0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/ccc1e9252ac2c6fc7d6a2a0835408521620c4d6bfe94ed723dd2445b25400d0d.jpg)



(e)



Figure 22. Asymmetric notched three-point bending test. Crack topology of the viscous three-field formulation (63) for different discretizations and corresponding length-scale parameters: (a) 20000 elements with $l { = } 0 . 1 5 \mathrm { m m } ;$ (b) 25 000 elements with l =0.05mm; (c) 35 000 elements with l =0.035mm; (d) 58 000 elements with l =0.025 mm; and (e) 79 000 elements with $l { = } 0 . 0 1 \mathrm { m m }$


## 6.5. Three-dimensional mode-I tension test

We now investigate the mode-I fracture problem of a three-dimensional tension test. The geometric setup of the problem and the boundary conditions are given in Figure 25(a). The same boundary value problem has been studied numerically by Miehe and Guerses¨ [20]. We discretize a notched prismatic specimen with an unstructured mesh consisting of 60 675 linear tetrahedral elements. The mesh is refined in an area where the crack is expected to propagate in order to approximate the sharp limit case $l  0$ . We apply the regularization parameter of l = 0.2 mm, which is approximatively twice times the element size to resolve the crack zone properly. The material parameters chosen are the bulk modulus $\lambda { = } 1 2 \mathrm { k N } / \mathrm { m m } ^ { 2 }$ , the shear modulus $\overset { \cdot } { \mu } { = } \overset { \cdot } { 8 } \mathrm { k } \overset { \cdot } { \mathrm { N } } / \mathrm { m } \mathrm { m } ^ { 2 }$ and the critical energy release rate $g _ { \mathrm { c } } { = } 5 \times 1 0 ^ { - 4 } \mathrm { k N / m m }$ . The boundary value problem is treated with the more robust three-field formulation (63). The viscosity parameter is set to $\eta { = } 5 \times 1 0 ^ { - 5 } \mathrm { k N / m m } ^ { 2 }$ . Figure 25(b) visualizes the crack in its final position in the undeformed configuration. Here, the crack is characterized by the iso-surface of the damage field for the fully damaged state $d ( x ) = 1$ . Figures 26(a)–(d)) depict the evolution of the phase-field at different stages of the deformation. As expected, the crack starts at the notch tip and propagates straight through the specimen. Figure 25(c) shows the final crack topology obtained by the configurational-force-driven sharp crack model. Here, crack propagation is based on the adaptive reorientation of critical segments and subsequent node doubling, see Guerses and Miehe¨ [19]. In this scenario, the specimen is discretized with only 3738 linear tetrahedra. The crack shows some roughness but is almost planar. The final crack surfaces of both models are in very good agreement. The main drawback of the phase-field model lies in the usage of an enormous number of elements that are needed to approximate the sharp limit case. In the three-dimensional setting, the number of elements grows dramatically. However, as already pointed out above, the configurational-force-driven model is of limited applicability due to its problems with crack initiation and branching. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/2f585e17b623cd5b0854bd9677790cb287b49b51f5c5862ce53638f43a3df041.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/183c537ab55cb71979c16f6a3d68f399d2a22e40c5068661f8ef01720993f8d7.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/f5232d26a5c5edf04fcb0f444f88670a492d6f7cb58f682c8501ed39c02fcb94.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/c989252e00b7dba024ecab11a98e7731ee0c3db5682fb4870497e6a58915486f.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/4175ee9e55fcbf53978fb6b2fb205891d2c86c5f5245536df01c7d55bbe252f8.jpg)



(f)



Figure 23. Asymmetric notched three-point bending test. Crack topology of the viscous three-field formulation (63) for (a) 58000 elements and $\eta { = } 2 . 5 \times 1 0 ^ { - 5 } \mathrm { k N s / m m } ^ { 2 } ;$ (b) 58 000 elements and $\eta { = } 1 . 0 \times 1 0 ^ { - 6 } \mathrm { k N s / m m } ^ { 2 }$ ; (c) 79 000 elements and $\eta { = } 2 . 5 \times 1 0 ^ { - 5 } \mathrm { k N s / m m } ^ { 2 } .$ ; (d) crack trajectories obtained by Miehe and Guerses¨ [20]; and (e) experimental crack patterns by Bittencourt et al. [28].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/9dbb339b24f3da7ed2acc0e199da5c6d7a93426dbe24b4283d65744a497081ca.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/14dc0754d81f2904aa26bb6a9458c1f4bac52a4a8ecb79a6b924508410a365b7.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/e4813a32d00b27ebc12c6a89dffa88180a17f78fbff613ce23c7f0daa0cf5e92.jpg)



(d)



Figure 24. Asymmetric notched three-point bending test. Crack topology (a)–d) for a mesh with 79 000 elements and a length-scale parameter l =0.01mm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/76efc9b400c0edeece846b3c7f9de2935c7a1409fe748cc016c6a17db08c1574.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/1d1af3b424921b45fa8235d3eba8fda832815ba3ac5ad10ccc2edcf98d44e6d8.jpg)



(b)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/c95624cc2613d5ebe96dd4328b5bcaa765b1645bffb13ad39cd7b74c8de6995d.jpg)



(a)



Figure 25. Three-dimensional mode-I tension test. (a) Geometry, loading and boundary condition; (b) final crack surface obtained by the regularized brittle fracture model (63), i.e. the isosurface of the damage field d(x) for the fully damaged state $d = 1 . 0 ;$ and (c) final crack surface obtained by the configurational-force-driven brittle fracture model discussed in Miehe and Guerses¨ [20].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/7024fb40c167d08c10d5bdea9ee103ea30e3e11d9fa59062b9bae5684a7cf89f.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/4d00d2e3168615315ca98881fcfb8b295593d7308b3e0ca7aa724cb0835166dc.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/75c0781d03856f9e36ea886ac5dc7b7b6c18e181c95777463d64bfbf38cb6442.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/b50ff38d7265db6aaa632a6472f466b8aa25fe661d86e88977c4f1dd201d7663.jpg)



(d)



Figure 26. Three-dimensional mode-I tension test. Evolution of the crack topology, i.e. the iso-surface of the damage field for $d ( x ) = 1 . 0$ at a deformation of (a) $3 . 5 2 \times 1 0 ^ { - 1 }$ mm; (b) $3 . 7 7 \times 1 0 ^ { - 1 }$ mm; (c) $4 . 0 2 \times 1 0 ^ { - 1 }$ mm; and (d) $4 . 1 1 \times 1 0 ^ { - 1 }$ mm. Localization starts at the tip of the crack and progresses straight through the material.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/e6dd7389fd341eb3e8faf51443a5a64c4fed74e581ec042c86f314c6f58b3406.jpg)



Figure 27. Boundary value problem of a tension test of a rigid spherical inclusion in a unit cube.


## 6.6. Tension test of cube with spherical inclusion

In this final example, we analyze the performance of the three-dimensional regularized fracture model with respect to crack initiation. To this end, we consider a cube with spherical inclusion subject to tensile loading. As depicted in Figure 27, the sphere is considered as rigid and has a diameter of 2.0. The cube has an edge length of 4.0. Note that the specimen is free of loca defects. It is discretized by 258 032 four-noded tetrahedral elements. The mesh is refined in areas where the crack is expected to evolve. Exploiting the symmetry of the problem, only one quarter of the cube is discretized. The computation is performed in a displacement-controlled context with a residual-based auto time stepping method. Here, the displacement increment is in the range of $1 \times 1 0 ^ { - 3 }$ mm to $0 . 4 \times 1 0 ^ { - 3 }$ mm. The material parameters are identical with those used in the previous example. The regularization parameter is chosen to be l = 0.1 mm. The problem is solved for the robust viscous three-field formulation (63). The viscosity parameter  has a value of $5 \times 1 0 ^ { - 5 } \mathrm { k N s } / \mathrm { m m } ^ { 2 }$ . Figure 28 depicts the evolution of the crack topology at different stages of the deformation. When a critical deformation state is reached, localization suddenly starts at the top surface of the sphere. For the subsequent deformation, the crack evolves horizontally until the outer surface is reached. The example shows that crack initiation in a body free of local defects can be achieved by the regularized fracture model under consideration. However, the price to pay is the enormous number of elements needed for a good approximation of the sharp limit case. Thus, further research on adaptive mesh refinement procedures is an important ingredient for the improvement of the proposed computational models. 

## 7. CONCLUSION

We have outlined a thermodynamically consistent framework for phase-field models of crack propagation in elastic solids, developed incremental variational principles and considered its numerical implementation by multi-field finite element methods. To this end, we first derived a regularized crack surface functional that converges for vanishing spatial length-scale parameter to a sharp crack topology functional. This functional provided the basis for the definition of convex dissipa tion functions, which govern the evolution of the crack phase-field. Here, we proposed alternative rate-independent and rate-dependent models that ensure the local growth of the phase field. We then defined an energy storage function whose positive tensile part degrades with increasing phase-field. With these constitutive functionals at hand, we derived the coupled balances of quasi static stress equilibrium and gradient-type phase-field evolution in the solid from the argument of virtual power. Here, we considered a canonical two-field setting for rate-independent response and a three-field formulation for a time-regularized over-force response. The latter formulation was shown to be consistent with a specific Ginzburg–Landau-type phase-field evolution. It was then shown that the coupled balances follow as the Euler equations of incremental variationa principles that govern the multi-field problems. These principles provide a compact basis for the finite element implementation. The time-regularized three-field formulation is very convenient for a straightforward finite element implementation due to the local character of the inherent fracture loading condition. Furthermore, the viscous stabilization effect provides a robust computational setting suitable for straightforward monolithic Newton-type solvers of the coupled problem. We have demonstrated the performance of the proposed phase-field formulations of fracture by means of representative numerical examples. A key problem of the phase-field formulations is the mesh density required for the resolution of the diffusive crack patterns. In follow up work, we plan to embed the computational framework into an adaptive mesh refinement strategy that resolves the fracture process zones. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/627c638e592bad9b18f0f5c358334433482698e658edf6572924fbdc22490406.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/639cfc341f3cfda72c065bcb9ad8c6cd3738a56d5ec180f35e9cc7870c3f2efd.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/e97c96002712e01de945b9630a72bced58ffaf5ddb111ebd153f145b13f1fb36.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/b1fcf794-1d01-48a0-b39b-244c57556234/c586c0f764f14ae2a3e8f8f937d14fe8c428cf5b6bb78db894d5e06acf0cfad0.jpg)



(d)



Figure 28. Tension test of a cube with a spherical inclusion. Evolution of the crack topology, i.e. iso-surface of the damage field $d ( x ) = 1 . 0$ at a deformation of (a) $1 . 0 \times 1 0 ^ { - 2 } \mathrm { m m } ;$ (b) $1 . 8 2 \times 1 0 ^ { - 2 }$ mm; (c) $2 . 2 2 \times \bar { 1 0 } ^ { - 2 }$ mm; and (d) $3 . 0 1 \times 1 0 ^ { - 2 }$ mm. Localization starts at the top surface of the sphere and evolves horizontally.


## ACKNOWLEDGEMENTS

Support for this research was provided by the German Research Foundation (DFG) under grant Mi 295/11-1. 

## REFERENCES



1. Griffith AA. The phenomena of rupture and flow in solids. Philosophical Transactions of the Royal Society London, Series A 1921; 221:163–198 





2. Irwin GR. Elasticity and plasticity: fracture. In Encyclopedia of Physics, Flugge S (ed.), vol. 6. Springer: Berlin,¨ 1958; 551–590. 





3. Barenblatt GI. The mathematical theory of equilibrium cracks in brittle fracture. Advances in Applied Mechanics 1962; 7:55–129. 





4. Francfort GA, Marigo JJ. Revisiting brittle fracture as an energy minimization problem. Journal of the Mechanics and Physics of Solids 1998; 46:1319–1342 





5. Bourdin B, Francfort GA, Marigo JJ. The Variational Approach to Fracture. Springer: Berlin, 2008. 





6. Dal Maso G, Toader R. A model for the quasistatic growth of brittle fractures: existence and approximation results. Archive for Rational Mechanics and Analysis 2002; 162:101–135. 





7. Buliga M. Energy minimizing brittle crack propagation. Journal of Elasticity 1999; 52:201–238. 





8. Bourdin B, Francfort GA, Marigo JJ. Numerical experiments in revisited brittle fracture. Journal of the Mechanics and Physics of Solids 2000; 48:797–826. 





9. Mumford D, Shah J. Optimal approximations by piecewise smooth functions and associated variational problems. Communications on Pure and Applied Mathematics 1989; 42:577–685 





10. Ambrosio L, Tortorelli VM. Approximation of functionals depending on jumps by elliptic functionals via --convergence. Communications on Pure and Applied Mathematics 1990; 43:999–1036 





11. Dal Maso G. An Introduction to --convergence. Birkhauser Verlag: Boston, 1993.¨ 





12. Braides DP. Approximation of Free Discontinuity Problems. Springer: Berlin, 1998. 





13. Braides DP. --convergence for Beginners. Oxford University Press: New York, 2002 





14. Hakim V, Karma, A. Laws of crack motion and phase-field models of fracture. Journal of the Mechanics and Physics of Solids 2009; 57:342–368. 





15. Karma A, Kessler DA, Levine H. Phase-field model of mode III dynamic fracture. Physical Review Letters 2001; 92:8704.045501. 





16. Eastgate LO, Sethna JP, Rauscher M, Cretegny T, Chen CS, Myers CR. Fracture in mode I using a conserved phase-field model. Physical Review E 2002; 65:036117-1-036117-10 





17. Belytschko T, Chen H, Xu J, Zi G. Dynamic crack propagation based on loss of hyperbolicity and a new discontinuous enrichment. International Journal for Numerical Methods in Engineering 2003; 58:1873–1905. 





18. Song JH, Belytschko T. Cracking node method for dynamic fracture with finite elements. International Journal for Numerical Methods in Engineering 2009; 77:360–385. 





19. Gurses E, Miehe C. A computational framework of three-dimensional configurational-force-driven brittle crack¨ propagation. Computer Methods in Applied Mechanics and Engineering 2009; 198:1413–1428. 





20. Miehe C, Gurses E. A robust algorithm for configurational-force-driven brittle crack propagation with r-adaptive¨ mesh alignment. International Journal for Numerical Methods in Engineering 2007; 72:127–155. 





21. Miehe C, Gurses E, Birkle M. A computational framework of configurational-force-driven brittle fracture based¨ on incremental energy minimization. International Journal of Fracture 2007; 145:245–259. 





22. Capriz G. Continua with Microstructure. Springer: Berlin, 1989. 





23. Mariano PM. Multifield theories in mechanics of solids. Advances in Applied Mechanics 2001; 38:1–93. 





24. Fremond M.´ Non-smooth Thermomechanics. Springer: Berlin, 2002. 





25. Kachanov LM. Introduction to Continuum Damage Mechanics. Maritinus Nijhoff Publishers, Springer: Netherlands, 1986. 





26. Fremond M, Nedjar B. Damage, gradient of damage and principle of virtual power.´ International Journal of Solids and Structures 1996; 33:1083–1103. 





27. Gurtin ME. Generalized Ginzburg–Landau and Cahn–Hilliard equations based on a microforce balance. Physica D: Nonlinear Phenomena 1996; 92:178–192 





28. Bittencourt TN, Wawrzynek PA, Ingraffea AR, Sousa JL. Quasi-automatic simulation of crack propagation for 2D LEFM problems. Engineering Fracture Mechanics 1996; 55:321–334. 

