---
title: "Protein Engineering and Immobilization of Imine Reductases for Pharmaceutical Synthesis: Recent Advances and Applications"
authors: "Kaličanin, N.; Popović Kokar, N.; Spasojević Savković, M.; Stošić, A.; Prodanović, O.; Surudžić, N.; Prodanović, R."
year: 2026
doi: 10.3390/chemistry8040040
license: CC BY 4.0
url: https://doi.org/10.3390/chemistry8040040
source: MDPI PDF text layer
tags: [ired-88, full-text, open-access]
---

> Repo note. This file is the full text of an open-access article, kept so a coding agent can read what the literature says about IRED-88. It is not one of the short notes in `kb/papers/`. Cite the original paper. The paragraph below is a pointer written for this repo; everything after the horizontal rule is the article.

Why it is here: the longest secondary account of how IRED-88 and IRED-88-2 were mined, why IRED-88 was the machine-directed-evolution starting point, and the S220T and Q194L/S220T/H230Y numbers. The text is the publisher PDF's text layer, so line breaks follow the PDF.

---

# Kaličanin et al. 2026, Chemistry (MDPI)

DOI: [10.3390/chemistry8040040](https://doi.org/10.3390/chemistry8040040). © 2026 the authors. Licensee MDPI. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Review

Protein Engineering and Immobilization of Imine Reductases for
Pharmaceutical Synthesis: Recent Advances and Applications
Nevena Kaličanin 1, *, Nikolina Popović Kokar 2 , Milica Spasojević Savković 3 , Anja Stošić 3 ,
Olivera Prodanović 4 , Nevena Surudžić 4 and Radivoje Prodanović 2, *
1

2

3

4

*

University of Belgrade-Institute of Chemistry, Technology and Metallurgy, National Institute of the Republic
of Serbia, Njegoševa 12, 11000 Belgrade, Serbia
University of Belgrade-Faculty of Chemistry, Studentski trg 12, 11000 Belgrade, Serbia;
nikolina@chem.bg.ac.rs
Innovative Centre of the Faculty of Chemistry, University of Belgrade, Studentski trg 12-16,
11000 Belgrade, Serbia; smilica84@gmail.com (M.S.S.); anja@chem.bg.ac.rs (A.S.)
University of Belgrade-Institute for Multidisciplinary Research, National Institute of the Republic of Serbia,
Kneza Višeslava 1, 11030 Belgrade, Serbia; oliverap@imsi.bg.ac.rs (O.P.); nevena.pantic@imsi.bg.ac.rs (N.S.)
Correspondence: nevena.kalicanin@ihtm.bg.ac.rs (N.K.); radivojep@chem.bg.ac.rs (R.P.)

Abstract
Imine reductases (IREDs) have emerged as valuable biocatalysts for the asymmetric synthesis of chiral amines, key intermediates in numerous active pharmaceutical ingredients.
Their ability to operate under mild reaction conditions with high chemo- and stereoselectivity provides an attractive alternative to conventional metal-catalyzed or chemical reduction
processes. However, the broader industrial application of wild-type IREDs is often constrained by their limited substrate scope and moderate catalytic efficiency. Recent advances
in biocatalysis have demonstrated that engineered IREDs can catalyze the reduction of
a wide range of natural and non-natural imines, significantly expanding their applicability in pharmaceutical and fine chemical synthesis. In parallel, enzyme immobilization
strategies have proven highly effective for improving operational stability, facilitating
enzyme reuse, and enabling continuous flow biocatalytic processes. Efficient cofactor
regeneration systems have further enhanced the practical implementation of IRED-based
transformations. Advances in protein engineering, including structure-guided design,
semi-rational mutagenesis, and directed evolution, have generated enzyme variants with
improved catalytic activity, stereoselectivity, and substrate tolerance. The integration of
high-throughput screening technologies and machine-learning-assisted enzyme design
has further accelerated the discovery and optimization of efficient IRED biocatalysts. This
review summarizes recent progress in the protein engineering and immobilization of IREDs
and discusses future perspectives for their industrial application.

Academic Editor: Juan B. Rodriguez

Keywords: chiral amines; imine reductases; protein engineering; enzyme immobilization;
drug synthesis; biocatalysis

Received: 11 March 2026
Revised: 25 March 2026
Accepted: 26 March 2026
Published: 28 March 2026

1. Introduction

Copyright: © 2026 by the authors.

1.1. Pharmaceutical Importance and Synthetic Approaches to Chiral Amines

Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.

Chemistry 2026, 8, 40

Chiral amines and amino acids constitute essential structural motifs in the pharmaceutical, chemical, and agrochemical industries [1]. Analyses estimate that chiral amine
moieties are present in about 40% of active pharmaceutical ingredients (APIs) and 20%
of agrochemicals [2]. An evaluation of the US Food and Drug Administration database

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

2 of 30

revealed that 84% of approved small-molecule drugs contain at least one nitrogen atom [3],
of which over 40% of the top 200 drugs in retail incorporate chiral amine functionalities,
highlighting the pressing demand for efficient and convenient synthetic methodologies to
access these scaffolds [4].
At the onset of the 21st century, the global market for these active pharmaceutical
ingredients (APIs) was estimated to generate revenues exceeding $30 billion, with an
annual growth rate projected at approximately 7–8% [5].
Enantiomers of biologically active chiral compounds often exhibit distinct pharmacological and toxicological effects, which can significantly influence therapeutic outcomes
when such compounds are administered as racemic mixtures [6]. Owing to the differential
physiological activities exerted by individual enantiomers of chiral compounds on organisms, the selective synthesis and isolation of pure enantiomers remains a central focus and
ongoing challenge in medicinal chemistry and drug development [4].
Traditional chemical methods for the asymmetric synthesis of chiral amines include C–
H insertion, diastereoisomeric crystallization, enantioselective reduction of imines or enamines, and nucleophilic addition, which commonly require the use of expensive transitionmetal complexes or chiral ligands, coupled with side reactions, such as reduction of ketone/aldehyde or overalkylation, making them unsustainable in industrial processes [5,7].
In 2019, the global enzyme market size was worth 9.087 billion USD, and it is expected
to grow to USD 13.8152 billion by 2027, with a compound annual growth rate of 6.4%
during the period 2020–2027 [8]. Biocatalysis makes it possible to bypass some of the above
problems in the preparation of chiral amines and has a significant advantage by enabling
the sustainable and environmentally benign production of chiral amines by employing
biodegradable enzymes, operating under benign conditions, and presenting a high degree
of chemo-, regio-, and enantioselectivity [9]. These enzymes include transaminases, imine
reductases, amine dehydrogenases, monoamine oxidases, Picter-Spenglerases, and lipases
(Figure 1) [10].

Figure 1. Examples of drugs containing chiral amine moiety intermediates, along with the respective
biocatalysts that can be used for their synthesis.

ω-Transaminases (ω-TAs) catalyze the conversion of prochiral ketones to chiral amines
using an amine donor, typically L-alanine or isopropylamine. Donors are used by the
enzyme for the amination of the pyridoxal 5′ -phosphate (PLP) cofactor, converting it into

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

3 of 30

pyridoxamine 5′ -phosphate (PMP), which subsequently transfers its amino group to the
ketone substrate [11]. Despite their advantages, ω-TAs possess mechanistic limitations.
Due to their dependence on the PLP cofactor, the enzymes are restricted to generating
primary amines, thus requiring additional chemical transformations such as alkylation to
obtain chiral secondary and tertiary amines [9]. Besides, the formal reductive amination
of carbonyl compounds by ω-transaminases requires supra-stoichiometric amounts of an
amine donor and strategies for shifting the unfavorable thermodynamic equilibrium, such
as the use of an additional enzyme for removing the co-product or equipment for acetone
evaporation [12].
The other type of enzymes for chiral amine synthesis are monoamine oxidases, flavindependent enzymes that catalyse oxidation of amines to imines using molecular oxygen,
which is associated with FAD cofactor reduction and hydrogen peroxide generation [10].
One of the most well-known applications of monoamine oxidase in the pharmaceutical
industry is the use of the enzyme derived from Aspergillus niger in the synthesis of an
intermediate compound for boceprevir, a protease inhibitor that has been employed in the
treatment of hepatitis C [13].
The asymmetric reduction of imines catalyzed by NAD(P)H-dependent enzymes
represents a promising strategy for the biocatalytic synthesis of a wide range of primary,
secondary, and tertiary amines [2]. The catalytic mechanisms of these classes of enzymes
are similar, involving the formation of a carbinolamine intermediate, followed by hydride
transfer from the nicotinamide [14].
Amine dehydrogenases (AmDHs) catalyze reductive amination between carbonyl
compounds and ammonia, yielding valuable amines with excellent enantioselectivity. They
belong to the NAD(P)H-dependent oxidoreductases [15]. The applicability of this class
of enzymes for the efficient asymmetric synthesis of α-chiral amines was shown in the
experiments of Mutti and co-workers [12].
Opine dehydrogenases catalyze the reversible reductive condensation of an α or ωamino function of an α-amino acid with an α-keto acid, in the presence of a nicotinamide
cofactor NAD(P)H, resulting in the formation of N-(carboxyalkyl) amino acids [16]. The fact
that their natural substrates are chemically very different from the typical imine reductase
or reductive aminase substrates, and that they can perform reductive amination with
close to stoichiometric ratios of ketoacid/amino acid substrates, makes them promising
candidates for industrial biocatalysis [17]. Opine dehydrogenase from Arthrobacter sp. 1C
(CENDH) was subjected to extensive protein engineering studies to construct an enzyme
variant that can accept substrates largely deviating from their natural ones and perform the
synthesis of secondary and tertiary amines useful for the pharmaceutical industry [18].
1.2. Imine Reductases (IREDs)
Imine reductases (IREDs) are NAD(P)H-dependent oxidoreductases (EC 1.5.1.x) that
catalyze the asymmetric reduction of imines to chiral amines and are often grouped with
reductive aminases (RedAms), which catalyze both imine formation and reduction in a
single catalytic cycle, whereas classical IREDs typically reduce preformed imines [2,6,14].
IREDs catalyze the enantioselective reduction of imines as well as the reductive
amination of carbonyl compounds with ammonia or a variety of alkyl, aryl, and cyclic
amines, enabling access to chiral primary, secondary, and tertiary amines. A distinct
subset of IREDs, termed reductive aminases (RedAms), possesses the ability to bind both
carbonyl and amine substrates within their active sites, thereby facilitating in situ imine
formation before stereoselective hydrogenation [6]. For such transformations to proceed
efficiently, IREDs must exhibit high chemoselectivity to prevent the undesired reduction of
the carbonyl group to the corresponding alcohol [10]. The catalytic mechanism involves

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

4 of 30

hydride transfer from NADPH to the imine carbon, followed by protonation of the nitrogen
atom. Structurally, IREDs belong to the NAD(P)H-dependent dehydrogenase family and
contain a Rossmann-fold domain for cofactor binding, usually functioning as homodimers
with active sites located at the monomer interface [4,11,14].
IREDs were first reported in 2010 by Mitsukura et al., who identified two enantiocomplementary enzymes from Streptomyces sp. capable of producing both (R)- and
(S)-2-methylpyrrolidine [19]. The first resolved crystal structure of imine reductase was
that of R-IR from Streptomyces sp. GF3587 (PDB: 3ZHB), discovered in 2013 by Grogan’s
research group. Solved structures of Q1EQE0 in native form, and in complex with the
nicotinamide cofactor, NADPH, revealed that the enzyme functional unit is a homodimer.
A helix of 28 amino acids is a linker between the N-terminal Rossman-fold motif and a
helical C-terminal domain in the monomer unit. The dimer is formed through reciprocal
domain sharing in which the C-terminal domains are swapped. The N-terminal domain of
monomer A and the C-terminal domain of monomer B are included in the formation of a
substrate-binding cleft [20].
Direct reductive amination of ketones by IRED was first reported by Huber and coworkers in 2014, who utilized S-selective imine reductase from Streptomyces as catalysts
for the reductive amination of 4-phenyl-2-butanone using methylammonium as the amine
donor [21]. This work marked a significant advancement, establishing IREDs as viable
biocatalysts for imine reduction (IR) and direct reductive amination.
At the beginning, the synthetic applicability of IRED was limited because reductive
amination reactions required large excesses of amine donor equivalents and were carried
out at higher pH values, resulting in scopes that did not appear to be particularly broad [9].
These issues were partially overcome after the discovery of a reductive aminase from
Aspergillus oryzae (AspRedAm) in 2017, marking the first fungal enzyme in the field, as
reported by Turner and co-workers. A variety of primary and secondary amines and a
broad set of carbonyl compounds could be reductively coupled with up to >98% conversion
and >98% enantiomeric excess. If both carbonyl and amine showed high reactivity, it was
possible to employ a 1:1 ratio of the substrates, with up to 94% conversion to amine
product [22]. Since then, the field has expanded considerably, with IREDs and RedAms
becoming central tools in the biocatalytic synthesis of chiral amines.
Recently, Turner and co-workers reported the discovery of a multifunctional biocatalyst, termed EneIRED, identified from a metagenomic imine reductase (IRED) library
and originating from an unclassified Pseudomonas species, that exhibits dual functionality:
it catalyzes both amine-activated conjugate reduction (CR) of α,β-unsaturated carbonyl
compounds and subsequent reductive amination (RA) facilitating the efficient and stereoselective synthesis of structurally diverse chiral amines bearing up to three contiguous
stereocenters [23]. In the research of Turner and collaborators, a facile high-throughput
screening assay was developed to examine IREDs activity, which resulted in the discovery
of more than 300 new imine reductases through a panel of 384 enzymes [24]. The results
presented in this research highlight the importance of the metagenomic approach in the
discovery of novel enzymatic activities and the development of a robust high-throughput
screening platforms that further facilitate the rapid discovery of IREDs with desirable
activity toward sterically demanding substrates.
Imine reductases share a common quaternary structure described previously. However, four catalytic reactions (IR, RA, CR, and CR-RA) have been reported for these enzymes,
and varying catalytic residues within the active sites have been observed. These residues
highlight the correlations and differences among catalytic mechanisms. A detailed explanation of the active site architecture, the mechanistic basis for the diverse catalytic
activities of imine reductases (IREDs), and the similarities and differences in key amino

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

5 of 30

acid residues involved in the aforementioned reactions is provided in the review paper by
Shao et al. [25]. However, these aspects will not be discussed in detail herein, as they fall
outside the primary scope of this work.
1.3. Protein Engineering and Immobilization as Strategies for Enzyme Modification Towards
Industrial Application
The main limitations of enzymes isolated from natural sources are low solubility and
stability, low catalytic efficiency, denaturation in the presence of organic solvents and at
elevated temperatures, and inactivation by substrates, products, or other components [26].
The key factors in reducing costs when biocatalysts are used for industrial applications are
the reusability and enzyme stability [27].
The ability to evolve enzymes is crucial for improving the scope of wild-type enzymes
toward non-natural substrates, and to further enhance their activity and tolerance to the
demanding process parameters [28]. Process of enzyme development includes optimization
of chemo-, regio-, and stereoselectivity of biocatalysts, as well as properties related to the
conditions in which the process takes place, like enhancing stability at certain temperatures,
pH values, and in the presence of high concentrations of substrates or organic solvents [29].
In addition to protein engineering, the advancement of diverse enzyme immobilization
techniques has significantly improved the productivity, economic feasibility, and technical
performance of various industrial biocatalytic processes [30]. Advantages of immobilized
enzymes lie in enhanced stability (in most cases, they exhibit greater stability and resistance
to harsh environmental conditions), improved reactor performance (development of continuous flow reactors permits a better control of reaction conditions), reusability (enabling
cost reductions), and increased specificity, making catalysis more precise [31].
1.4. Scope of the Review
In recent years, numerous comprehensive reviews have been published regarding the
application of imine reductases (IREDs) in the synthesis of amine-containing pharmaceuticals [4,6,10,11,14]. This review aims to provide an overview of key advancements in the
field, with particular emphasis on discoveries in protein engineering and the immobilization of IREDs for use in scalable pharmaceutical intermediate synthesis and in small-scale
production of pharmaceutical metabolites, with potential for continued optimization and
broader implementation. This review highlights the extensive application of protein modification strategies, including directed evolution, rational design, and immobilization, as
pivotal approaches for developing efficient stereoselective pathways mediated by IREDs.

2. Engineering and Immobilization of Imine Reductases for
Drug Synthesis
A broad spectrum of physiological and pharmacological activities exhibited by compounds accessible through imine reductase-catalyzed transformations underscores the
importance of developing advanced strategies to engineer IREDs into robust, industrially
applicable biocatalysts. Over the past decade, imine reductases (IREDs) have attracted
considerable research interest, prompting extensive efforts to modify and optimize them
for broad applications across the pharmaceutical industry.
2.1. Scalable Synthetic Reactions and Industrial Drug Manufacturing with Engineered
Imine Reductases
Within this segment, the key details of modifications achieved through protein engineering of imine reductases are provided, to develop enzyme variants suitable for the
preparative-scale synthesis of active pharmaceutical ingredient (API) intermediates.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

6 of 30

In 2019, Roiban and colleagues developed an engineered imine reductase for the
manufacture of the lysine-specific demethylase-1 inhibitor GSK2879552, which is used
to treat small-cell lung cancer and acute leukemia. After screening the GSK IRED panel,
they identified IR-46 (from Saccharothrix espanaensis) as the best variant, which showed
73% conversion and >99% ee after 2 h on a 1 g scale using cell-free lysate. When the
reaction was scaled up to more than 5 g, it achieved 85.0% conversion, using more than
450% weight (w/w) of lyophilized enzyme, at pH 6.3, and yielded 42.9% of the isolated,
pure product with 99.9% ee. The enzyme underwent extensive engineering. According
to the structural homology model of IR-46, they initially targeted 256 out of 296 amino
acid positions for single-site saturation mutagenesis. They screened ~4000 variants in
cell lysates at 12 g/L of precursor compound in NaOAc buffer at pH 5.6. A 40-fold
improvement in conversion over parent (FIOP) was achieved with the most active variant,
Y142S. At the same time, identification of other beneficial mutations at that position, such
as Y142V, Y142R, and Y142T, indicated position 142 as a key residue influencing IR-46’s
activity and stability. Lyophilized mutant 1 resulted in a 87.8% conversion at a 68% yield
with reduced enzyme loading (61.4% w/w) and maintained selectivity at 99.9% ee in a
gram-scale reaction. Eight combinatorial libraries containing the beneficial mutations from
round 1 were constructed, which gave 132 variants with FIOP > 10 after the screening
of ~4000 variants with 20.1 g L−1 of precursor, reduced biocatalyst lysate loading, and
preincubation of lysate to select for stable variants. A secondary screen gave a mutant
for the next round of evolution containing mutations Y142S, L37Q, A187V, L201F, V215I,
Q231F, and S258N. With lyophilized enzyme loading of 12% w/w, using NaOAc pH 5.0,
mutant 2 gave 87.6% conversion, 5.6 g isolated yield (68.5%) with 99.4% ee. A total of
~1300 variants were screened in the third round of evolution and gave the best variant,
which contained an additional six mutations over mutant 2 (Y142S, L37Q, A187V, L201F,
V215I, Q231F, S258N, G44R, V92K, F97V, L198M, T260C, A303D). The reduced enzyme
loading of 1.2% w/w of the lyophilized mutant 3 was used to scale up the reaction to 1 L
(16.6 g of precursor compound) in NaOAc buffer at pH 4.6. A conversion rate of 91.4% was
reached with an isolated product yield of 72.2% (99.7% ee). The melting temperature of the
final variant was increased by 30 ◦ C compared to the wild type, and a more than 5000-fold
increase in half-life was achieved at pH 5.0. Specific activity increased 13-fold after three
rounds of evolution. The final reaction was run in three batches to afford 1.4 kg of the
GSK2879552 key intermediate, with an isolated yield of 84.4%, a purity greater than 99.9%,
and an enantiomeric excess (ee) of 99.7%. A 38,000-fold improvement in TON over wild
type was achieved [32]. A schematic representation of GSK2879552 intermediate synthesis
using engineered imine reductase is shown in Figure 2.
In the 2020 study by Zhu et al., a biocatalytic approach to 1,4-diazepanes via engineered imine reductase-catalyzed intramolecular asymmetric reductive amination was
developed, providing an environmentally friendly and economical method for the synthesis
of a Suvorexant intermediate (a dualorexin receptor antagonist for the treatment of primary
insomnia). When a library of 48 IREDs was screened against the precursor compound at a
substrate concentration of 10 mmol/L using cell-free extracts, an R-selective imine reductase
(IR1) from Leishmania major was found to catalyze the synthesis of Suvorexant intermediate
with a 99% ee value. An enantiocomplementary imine reductase, designated as IR25,
from Micromonospora echinaurantiaca, exhibited the highest enantioselectivity (>99% ee).
Determined specific activities of IR1 and IR25 were 0.065 and 0.418 U/mg, respectively. The
catalytic activity of IR1 was enhanced through enzyme engineering. A twenty-five amino
acid residues around the substrate and cofactor NADPH were selected to construct saturation mutagenesis libraries after docking of a cyclic imine of a precursor compound into
the active center of IR1. Among five mutants that displayed increased catalytic efficiency

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

7 of 30

(kcat /Km ) over the wild-type enzyme, mutants D232H and Y194F showed a significant
decrease in Km and an increase in kcat , resulting in a 17-fold and 12-fold improvement in the
catalytic efficiency, respectively. The double-mutant Y194F/D232H showed an additional
decrease in Km and an increase in kcat with a kcat /Km value of 1.646 s−1 mM−1 , which was
a 61-fold enhancement compared to the wild-type enzyme. Preparative-scale asymmetric
reductive amination of the precursor compound was performed in a 100 mL reaction
system using cell-free extracts of IR25, IR1, or its mutant Y194F/ D232H. The obtained
results showed that using the cell-free extracts of the mutant Y194F/D232H (10 g/L wet cell
weight), a 100 mM precursor could be completely converted to the suvorexant intermediate
within 10 h (Figure 3).

Figure 2. Schematic representation of GSK2879552 synthetic procedure using engineered imine
reductase IR-46 from Saccharothrix espanaensis.

Figure 3. Schematic representation of Suvorexant synthetic procedure using engineered imine
reductase IR1 from Leishmania major.

In comparison, the cell-free extracts of IR25 and IR1 (50 g/L wet cell weight) could
only convert 50 mM of precursor to the (S)- or (R)-intermediate of Suvorexant within 10 or
6 h, respectively. Compared with the mutant Y194F/D232H, IR1 exhibited lower activity,
and IR25 showed lower stability. The Tm’s of IR1, Y194F/D232H, and IR25 were 59, 58,
and 43 ◦ C, respectively [33].
Snajdrova and collaborators showed that machine-directed evolution can be used as
an enzyme engineering strategy for creating a library of high-activity mutants with a drastically shifted activity distribution compared to that of traditional directed evolution. First,
a wild-type IRED capable of catalyzing the reductive amination between the Cbz-protected
3-oxopyrrolidine and methylamine was identified to obtain an H4 receptor antagonist for
the treatment of atopic dermatitis. When they tested the bulkier ketone that would give direct access to the desired amine, only (R)-selective IRED-22 from Mycobacterium mageritense
catalyzed the reaction with a conversion of 12% but with a good enantioselectivity (ee
(R) 97%), and (S)-selective IRED-13 with a conversion of 77% and >99% ee. Afterwards,
they initiated genome mining to identify a wild-type IRED with higher activity toward

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

8 of 30

the desired (R)-enantiomer. In the first round, they identified (R)-selective IRED-88 with
a 70% conversion, but it showed decreased selectivity (ee (R) 30%) compared to IRED-22.
In the second round of mining, they identified IRED-88-2 with the 83% conversion rate
and ee (R) > 99%. IRED-88 was selected as a starting point for evaluating machine-directed
evolution because it offers the opportunity to engineer both activity and enantioselectivity. After enzyme expression in 384-well microtiter plates, the wells expressing IRED-88
yielded approximately 10% conversion. They ordered a synthetic deep mutational scanning
(DMS) library containing all 19 amino acid replacements with a single substitution at each
individual position of the IRED-88 sequence. It was determined that residue 220 forms
part of a helix at the entrance to a tunnel that leads to the nicotinamide cofactor group, and
the S220T mutation was identified as the most efficient, yielding 70% conversion and 96%
ee (R). They assumed that a preference for the (R)-product is a consequence of a change
from Ser to Thr, which imposes greater steric restraints either on entry into the Pro-(S)
conformer or on release of the (S)-product. In parallel with the deep mutational scanning,
error-prone PCR was performed. After three rounds of error-prone PCR, they obtained
mutant IRED-88-Q194L/S220T/H230Y, which was selected as the scale-up catalyst at a
substrate concentration of 100 mM (1.36 g in 55 mL, 10% (v/v) DMSO). By applying an
enzyme-to-substrate ratio of 1:5 (w/w), full conversion and 98% ee (R) were obtained. The
product was isolated as a tartrate salt, with a 72% yield, proving this variant as a sufficiently
robust catalyst for the gram-scale synthesis of the H4 receptor antagonist ZPL389 [34].
The synthetic procedure for the H4 receptor antagonist ZPL389 using engineered imine
reductase is presented in Figure 4.

Figure 4. Schematic representation of ZPL389 synthetic procedure using engineered imine reductase
IRED 88.

The first application of RedAm technology for the commercial-scale manufacturing of a
secondary amine via direct reductive amination of a ketone with methyl amine was demonstrated by Kumar and collaborators in 2021 during the synthesis of the drug Abrocitinib.
Abrocitinib is a JAK inhibitor for the treatment of atopic dermatitis. An N-methylaminesubstituted cis-cyclobutane headpiece of this compound was previously synthesized via
chemical reductive amination at low temperature, yielding approximately an 80:20 mixture
of cis:trans isomers. To identify an enzyme capable of performing reductive amination of a
ketone precursor with methyl amine to give the desired N-methyl amine, a screening of the
Pfizer in-house enzyme panel (80 wild-type IREDs from various sources) was performed.
The SpRedAm from Streptomyces purpureus was selected as the best candidate with high
selectivity (dr > 99:1) for the desired cis isomer. When SpRedAm was tested with 100 g/L
ketone and 1.5 g/L enzyme loading, it achieved only 0.75% conversion over 24 h while
retaining high selectivity. For initial site selection and library construction, they employed
a computational and bioinformatics-based approach, combined with a data-driven approach to identify hotspots and their synergistic recombination, thereby achieving the
desired performance.
Initial SSM libraries were screened at a substrate concentration of 20 g/L, with subsequent rounds at higher substrate loadings, resulting in the identification of more than

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

9 of 30

20 improved single-point variants. The top five round-1 variants achieved >75% conversion at 50 g/L substrate loading with >99:1 cis:trans selectivity. In round 2, libraries
were screened at 75 g/L substrate using 2 equivalents of methylamine, and recombination of beneficial mutations produced double mutants (Q13R/A170M, Q13R/N131H, and
A170C/F180M) that improved conversion by up to 3-fold while maintaining high selectivity. Multi-site random recombination of active variants yielded improved enzymes
containing 4–6 mutations. In round 3, recombination of earlier hits led to the identification
of SpRedAm-R3-V6 (N131H, A170C, F180M, G217D), of which F180M directly interacts
with the substrate. At the same time, the remaining mutations reside in the secondary shell
and influence active-site dynamics. The process was optimized for commercial scale (tens
of kilograms per batch), with consistent reaction performance exceeding 91% conversion in
48 h. A total of >3.5 MT of Abrocitinib intermediate as the succinate salt was manufactured
in >99% purity and >99:1 cis:trans. A schematic representation of Abrocitinib intermediate
synthesis using engineered imine reductase is shown in Figure 5 [35].

Figure 5. Schematic representation of Arocitinib synthetic procedure using engineered imine reductase SpRedAm from Streptomyces purpureus.

Zhang and associates successfully engineered an imine reductase (IR-G36) into a highly
efficient variant (M5) using a strategy that combined rational cavity design, combinatorial
active-site saturation mutagenesis (CAST), and thermostability engineering. During the
screening of the 86 IREDs panel against 5 mM N-Boc-3-piperidinone and 5.5 mM benzylamine hydrochloride using a cell-free extract, nine IREDs were able to afford the desired
product with low conversions (3–12%). Among them, they selected IR-G36, with the best
R-selectivity (ee 78%), as the target for the evolution. After the enzyme crystallization, its
three-dimensional structure in complex with NADP+ was solved by molecular replacement, and the docking of the imine intermediate of the desired product into the cavity
was done. Structural analysis revealed that IR-G36 poorly accommodated the bulky intermediate, prompting mutation of the key amine-recognition residue N121 to smaller
amino acids. Among these, N121T delivered a ~10-fold increase in conversion (77%) and
improved stereoselectivity (88% (R)). Considering that loop 252–261 interacts with the
nicotinamide moiety of NADP+ by forming hydrogen bonds at its residues V259, S260,
and N261, it could form a bottleneck that may hinder the entering and coupling of the
bulky substrates. Residue S260 was targeted and mutated based on sequence alignment
of IREDs, resulting in S260F with improved conversion (56%) and enhanced enantioselectivity (98% (R)). Combining N121T and S260F gave M1 (79% conversion, >99% (R) ee),

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

10 of 30

which was further evolved through NNK codon degeneracy for saturation mutagenesis.
Subsequent rounds identified multiple beneficial mutations, culminating in enzyme M5
(N121T/S260F/F207I/M238A/M264H/A267H/L197I/N271K/H189A/G145K), which exhibited a 4193-fold increase in catalytic efficiency, a 16.2 ◦ C gain in thermostability, and
>99% (R) enantioselectivity) for the synthesis of (R)-3-benzylamino-1-Boc-piperidine. M5
also displayed a broad substrate scope, enabling the synthesis of diverse azacycloalkylamines under industrial-scale conditions (up to 47 g/L substrate loading, >99% conversion,
and >99% enantiomeric excess). Optically active azacycloalkylamines are key ingredients in
the creation of large quantities of pharmaceuticals, such as Linagliptin, Alogliptin, Ibrutinib,
and Tofacitinib, which are widely used to treat hypertension, hyperglycemia, lymphoma,
and rheumatoid arthritis, respectively. This is a powerful and streamlined method for developing robust and commercially viable IREDs, with broad implications for pharmaceutical
manufacturing and synthetic biology [7].
Chiral pyrrolidines are fundamental components in the synthesis of pharmaceuticals such as Larotrectinib, a tropomyosin receptor kinase inhibitor approved by the U.S.
Food and Drug Administration for cancer treatment. Zheng and co-workers identified
WT imine reductase ScIRED from Streptomyces clavuligerus and used it for asymmetric
reduction of cyclic imine 2-(2,5-difluorophenyl)-pyrroline to the desired enantiomer (R)2-(2,5-difluorophenyl) pyrrolidine, an intermediate of Larotrectinib. The compound was
synthesized by the enzyme with up to 99% enantiomeric excess but with low activity
(0.18 U mg−1 ), and with the conversion of only 2 g L−1 of the substrate. After the substrate
docking into the binding site, all 10 residues surrounding the substrate were selected for
single-site saturation mutagenesis. The screening of the specific activity gave two hits
(F177W and V122C) with enhanced activity over the wild-type enzyme, which were combined in a variant with further improved activity (10-fold improvement in activity over WT).
With a substrate loading of 10 g L−1 , using ScIRED-R1-V1, a full transformation to the target
product could be achieved within 8 h. However, when the substrate loading was increased
to 15 g L−1 , only 44% conversion was achieved in 24 h, accompanied by a decrease in
stereoselectivity. In the second round, ScIRED-R1-V1 was subjected to single-site saturation
mutagenesis at 27 secondary-shell positions, identifying four beneficial mutations (M169W,
W185L, S211G, and M270E) located at the dimer interface. Combination of these mutations
yielded ScIRED-R2-V2, which exhibited a specific activity of 12.8 U mg−1 , corresponding to
a >70-fold improvement over the wild-type. After the additional two rounds of saturation
mutagenesis for the remaining 23 residues, additional mutations, G214F and V232A, were
identified, also located at the dimer interface. Combining all of the beneficial mutations
resulted in variant ScIRED-R2-V3 that exhibited a specific activity of 17.7 U mg−1 , almost
100-fold improvement over WT, over 25 ◦ C increase in melting temperature (Tm), and a
138-fold enhancement in half-life at 40 ◦ C. In the third round, three additional favorable
mutations (E45A, D53T, and F265L) were identified and incorporated into ScIRED-R2-V3.
The specific activity of the obtained variant ScIRED-R3-V4 was up to 19.2 U mg−1 (a
107-fold increase over WT), with an almost 32 ◦ C increase in Tm (from 24.6 to 56.5 ◦ C)
and 119-fold increase in the catalytic efficiency (kcat /Km ). Using the ScIRED-R3-V4, they
assessed asymmetric reduction of initial substrate at loadings of 80 g L−1 in 82.5% yield
within 5 h with >99.5% ee [36]. Synthetic procedure of Larotrectinib intermediate using
engineered imine reductase is presented in Figure 6.
The same group of researchers reported the direct synthesis of a wide range of sterically
demanding secondary amines via reductive amination of carbonyl substrates and bulky
amine nucleophiles employing imine reductases from Penicillium camemberti. Cinacalcet is a
calcimimetic approved by the US FDA and the EMA in 2004 for the treatment of secondary
hyperparathyroidism and parathyroid carcinoma, which manifests its activity through

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

11 of 30

lowering the levels of parathyroid hormone. After screening of 69 naturally existing IREDs
with a 1:1 ratio of 3-[3-(trifluoromethyl)phenyl]propanal to (R)-1-(1-naphthyl)ethylamine
[(R)-a], PcIRED was discovered with a 0.2% conversion to Cinacalcet. To further enhance the potential of PcIRED, iterative saturation mutagenesis was performed using
3-[3-(trifluoromethyl)phenyl]propanal and (R)-a as model substrates. After performing mutagenesis at seventeen residue sites around the active site into smaller residues (e.g., alanine,
glycine, and valine), six mutants (L180V, S181A, W219L, Q244A, Q244V, and S247A) that
displayed enhanced activity compared to the wild-type enzyme were identified. Among
them, the mutation of Q244, located at a key α-helix forming the substrate-binding pocket,
and close to the nicotinamide moiety of the NADPH, to Q244A exhibited the highest conversion of 28%. After combining Q244A with the other four beneficial mutations (L180V,
S181A, W219, and S247A), mutant Q244A/L180V was found to exhibit a 101-fold increase
in specific activity and a 6 ◦ C improvement in melting temperature (Tm) over the wild-type
enzyme, and it was selected as a template for the next round of evolution. The hotspots
discovered in the first round of evolution (S181, W219L, and S247), four residue sites (I241,
V243, D246, and H250) situated at the same α-helix with the key Q244 residue, and four
residue sites (A205, V210, L213, and L220) located at the dimer interface were targeted
for single-site saturation mutagenesis. Introduction of the mutations H250N and V210I
resulted in mutant M2, which exhibited a 251-fold increase in activity compared to the
wild-type enzyme. In the third round, after saturation mutagenesis of 19 amino acid sites,
they obtained mutant M3 (Q244A, L180V, H250N, M216T, S247A, S181A, C174N, and V210I)
with a 488-fold increase in activity, and enhanced stability over the wild-type enzyme (Tm
increased from 41 to 52 ◦ C). At a concentration of 500 mM (R)-1-(1-naphthyl)ethylamine
with 3-[3-(trifluoromethyl)phenyl]propanal at only a 1:1.2 molar ratio, with the pH maintained at 7.0, by using PcIRED-M3, they afforded 15.1 g of the product Cinacalcet in >99%
ee (R), at 84.7% isolated yield, and 75.6 g L−1 day−1 space-time yield (STY) (Figure 7) [37].

Figure 6. Schematic representation of the Larotrectinib synthetic procedure using engineered imine
reductase ScIRED from Streptomyces clavuligerus.

Figure 7. Schematic representation of Cinacalcet synthetic procedure using engineered imine reductase PcIRED from Penicillium camemberti.

Building on these advances, another study explored the enzymatic asymmetric reduction of heteroaryl-substituted tetrahydroisoquinolines (THIQs) using a broad panel of
137 IREDs, leading to the identification of enantiocomplementary biocatalysts for the synthesis of key pharmaceutical intermediates, including the intermediate for kinase inhibitor
TAK-981 (a first-in-class inhibitor of SUMO-activating enzyme used for the treatment of can-

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

12 of 30

cer). IR141 from Promicromonospora sp. CF082 exhibited the highest conversion (45%) of precursor compound into 7-chloro-1-(2-methylthiophen-3-yl)-1,2,3,4-tetrahydroisoquinoline.
After docking of the precursor into the active pocket of IR141, 45 amino acid residues were
selected to construct saturation mutagenesis libraries that resulted in finding three mutants
(L172C, T235S, and Y267F) with higher activity than IR141. Among them, mutant L172C
displayed a 35-fold improvement in the catalytic efficiency and conversion rate of >99%
with 10 mM precursor compound by using cell-free extracts, with >99% ee. Six single-site
saturation mutagenesis libraries were constructed, yielding double mutants L172C/T235S,
L172M/Y267F, and L172C/Y267F, which showed a 136-, 98-, and 95-fold improvement
in catalytic efficiency compared to the wild-type enzyme. To obtain the catalytic efficiency of single-site mutant L172M, this mutant was constructed by the site-directed
mutation of the wild-type enzyme, and showed a higher kcat/ Km (11.940 min−1 mM−1 ).
Triple mutants L172C/ T235S/Y267F and L172M/T235S/Y267F were constructed, and
L172C/T235S/Y267F showed a considerably higher kcat /Km (68.031 min−1 mM−1 ) and a
170-fold enhancement compared with IR141. Double and triple mutants were screened
against 50 mM precursor by using cell-free extracts, with stereoselectivities of 99% ee (R).
Still, only the mutant L172M/Y267F achieved complete conversion within 20 h, due to
its highest thermal stability, with a 13 ◦ C improvement in melting temperature (Tm) over
the wild-type enzyme. This variant enabled a preparative-scale reduction of substrate
7-chloro-1-(2-methylthiophen-3-yl)-3,4-dihydroisoquinoline (50 mM) to obtain product
7-chloro-1-(2-methylthiophen-3-yl)-1,2,3,4-etrahydroisoquinoline in >99% ee, providing a
green and economically viable synthetic route. Additionally, L172M/Y267F and IR40 were
successfully applied to the synthesis of a series of 1-heteroaryl-substituted THIQs, delivering high isolated yields (80–94%) and excellent enantioselectivities (82–>99% ee). These
results further demonstrate the versatility of IREDs as valuable tools for the stereoselective
synthesis of structurally diverse chiral amines [38].
In 2023, Steflik and co-workers reported the identification and engineering of a RedAm
to catalyze the synthesis of a key intermediate for cyclin-dependent kinase (CDK) inhibitors,
using benzylamine as an amine partner, which is relevant in the synthesis of highly watersoluble amine derivatives. The cyclin-dependent kinases (CDKs) comprise a 21-member
family of serine-threonine kinases involved in a wide range of cellular processes, including
transcriptional regulation, splicing, DNA repair, and the regulation of the cell cycle. After
screening of Pfizer in-house IRED panel (88 wild-type IRED) to identify enzymes capable
of the reductive amination of the initial ketone with benzylamine, IR007, a hypothetical
protein identified initially in Amycolatopsis azurea, exhibited the desired selectivity, showing
21% conversion with 96% enantiomeric excess (ee). Using 200 mM of ketone substrate loading and 4.6 g/L of IR007 in the form of lyophilized cell-free lysate, the reaction was scaled
to 0.5 g and gave 35% conversion to benzylamino alcohol with 97% ee after 50 h. After
optimizing the reaction temperature and DMSO concentration, the conversion increased
to 38% after 48 h while maintaining the high % ee. In the first round of engineering, 94 of
286 positions in IR007 were selected for single-site saturation mutagenesis (SSM), including
both active site and secondary shell residues as well as other residues identified by bioinformatic analysis. Screening at 35 g/L ketone substrate and the enzyme load equivalent of
10 g/L of wet cell paste identified multiple beneficial single substitutions, yielding variants
with 1.61–2.8 FIOP. In phase 2, structure-guided recombination of proximal residues produced improved double mutants, including IR007-41 (A213R/A214H, 3.17 FIOP), IR007-42
(A214H/Q217N, 3.57 FIOP), and the top variant IR007-49 (E120R/A213F, 5.53 FIOP). Phase
3 employed these variants as templates for targeted substitutions, iterative saturation mutagenesis (ISM), and combinatorial active site saturation testing (CASTing) libraries, as well
as libraries randomly incorporating all the beneficial substitutions identified in phase 1.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

13 of 30

As they identified improved variants, they were subsequently used as templates for additional mutagenesis. The final engineered enzyme, IR007−143, was used for kilogram-scale
manufacturing with a substrate load of 50 g/L, achieving 43% conversion, 98.4% ee, and
an increased Tm by approximately 5 ◦ C [39]. A schematic representation of CDK 2/4/6
intermediate synthesis using engineered imine reductase is shown in Figure 8.

Figure 8. Schematic representation of CDK 2/4/6 inhibitor intermediate synthetic procedure using
engineered imine reductase IR007 from Amycolatopsis azurea.

Among the notable contributions in this field, Zhu and co-workers developed an efficient biocatalytic process combining dynamic kinetic resolution with asymmetric reductive
amination to produce β-branched chiral amines featuring two consecutive stereocenters. To
optimize enzyme performance, they employed targeted saturation mutagenesis to pinpoint
key amino acid residues, followed by an iterative combinatorial approach to combine the
most promising mutations. β-Branched chiral amines containing contiguous stereocenters are prevalent in biologically active molecules, such as Tofacitinib, a protein tyrosine
kinase inhibitor used to treat rheumatoid arthritis, active psoriatic arthritis, and ulcerative colitis. A direct DKR-ARA of racemic 1-benzyl-4-methylpiperidin-3-one (15 mM,
3 g L− 1 ) with methylamine (200 mM) was chosen as a model reaction. A library screening
of 125 IREDs was performed, and only PocIRED, IRED-7, and IRED-18 afforded the desired
(R)-enantiomer, but with low conversion, and insufficient diastereo- and enantioselectivity.
Enantiomeric excess (from 74% to 88%) and diastereomeric ratio (from 90:10 dr to 92:8 dr)
increased after increasing the ratio of substrate to enzyme (S/C) from 2:1 to 200:1, but the
conversion dropped from 95–22%. Additionally, the enantiomeric excess increased from
82–89%, and the conversion increased from 84–91% after the pH was raised from 8.0 to
9.5. Since high pH accelerates substrate racemization, it was necessary to improve the
tolerance of PocIRED under the high pH conditions. The first round of mutagenesis yielded
mutant M1 (Q239G), which increased enantiomeric excess from 88% to >99.9%, improved
the diastereomeric ratio from 9:1 to 13:1, and enhanced conversion 1.8-fold over the wild
type. In the second round, a combinatorial library integrating beneficial single mutations
and a CAST library identified mutant M2 (M1 + P125T), which achieved an excellent
diastereomeric ratio (99:1) while maintaining >99.9% ee. In the third round, the 48 sites
from the first round were chosen for mutagenesis using the NNK codon set, and 110 sites
from the middle and outer layers of the enzyme active pocket were chosen for saturation
mutagenesis that resulted in the discovery of various positive mutations, with a 1.2- to

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

14 of 30

4-fold improvement in conversion relative to M2. In the fourth round, these advantageous
mutations were combined using multicodon combinatorial mutagenesis to improve enzyme performance further. After several iterative rounds of combinatorial mutation library
screening, a 20-point mutant variant, PocIREDM6, was identified, displaying > 99.9% ee
and >99:1 dr, compared with WT (88% ee and 9:1 dr), and enhanced thermostability (Tm
63.5 ◦ C) compared to WT (Tm 48.1 ◦ C). The resulting variant, M6, exhibited excellent performance, handling substrate concentrations of up to 110 g/L, achieving a 93% conversion
and a 74% isolated yield, with exceptional stereoselectivity (Figure 9).

Figure 9. Schematic representation of Tofacitinib synthetic procedure using engineered imine reductase PocIRED from Pochonia chlamydosporia.

Notably, M6 also displayed improved activity and substrate flexibility compared to
the wild-type enzyme, enabling the synthesis of a broader range of β-branched chiral
amines. These advancements underscore the potential of engineered IREDs in expanding the synthetic capabilities of dynamic kinetic resolution systems for pharmaceutical
applications [40].
Another example is the directed evolution of IR61 from Jiangella muralis, which enabled
the asymmetric reduction of a key intermediate in the synthesis of Dextromethorphan. (S)1-(4-Methoxybenzyl)-1,2,3,4,5,6,7,8-octahydroisoquinoline ((S)-2a) was synthesized from
1-(4-methoxybenzyl)-3,4,5,6,7,8-hexahydroisoquinoline (1a). IR61 from Jiangella muralis was
identified through the screening of 127 IREDs against 10 mM 1a using cell-free extracts,
and exhibited the highest (S)-stereoselectivity (>99% ee) toward 1a. After docking 1a into
the active pocket of IR61, 45 residues were selected to construct saturation mutagenesis
libraries, and five mutants (P123A, P123G, W179A, W179G, and F182S) were identified
with enhanced activity over WT. To further enhance the activity, they generated four double mutants, P123A/W179A, P123A/W179G (M1), P123G/W179A, and P123G/W179G,
that showed 6-, 39-, 26-, and 8-fold improvements in catalytic efficiency over WT, respectively. The saturation mutagenesis of F182 was performed using the most prominent
mutant, P123A/W179G (M1), which yielded two triple mutants, P123A/W179G/F182S
and P123A/W179G/F182I (M2), with 61- and 160-fold improvements in catalytic efficiency,
respectively. It was determined that residue P123 was cited at the substrate entrance tunnel,
and its mutation led to favorable changes in activity. Saturation mutagenesis was performed
at six additional positions (L212, D215, S216, E219, D232, and V233) located at the substrate
entrance tunnel. This led to the identification of mutant M3 (P123A/W179G/F182I/L212V),
which exhibited a 298-fold increase in catalytic efficiency and was subsequently subjected
to further saturation mutagenesis at positions V69 and T238. Mutant (M4) containing
mutations V69Y/P123A/W179G/F182I/L212V was obtained with a 766-fold improvement in catalytic efficiency compared to that of wild type IR61. When a preparative-scale
asymmetric reduction of 1a at a 200 mM concentration in a 50 mL reaction mixture was
performed using cell-free extracts (50 g/L wet cell weight) with 20% v/v glycerol, complete
conversion to (S)-2a was achieved within 2 h. The conversion rate using IR61 under the
same conditions was only 6%. The reaction was scaled up to 500 mL, achieving >99%
conversion within 2 h, a 77% isolated product yield, >99% ee, and a space-time yield (STY)
of 542 g L−1 d−1 . Beyond this application, M4 also exhibited high activity toward various

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

15 of 30

phenyl-substituted 1-benzyl-HHIQ derivatives, underscoring the broader utility of IREDs
for the synthesis of pharmaceutically relevant chiral amines [41]. The synthetic procedure
for the Dextromethorphan intermediate using an engineered imine reductase is presented
in Figure 10.

Figure 10. Schematic representation of Dextrometrophan synthetic procedure using engineered imine
reductase IR61 from Jiangella muralis.

Li and co-workers investigated the asymmetric synthesis of chiral N-hydroxyethyl
amino indane derivatives, including (S)-1-((2-hydroxyethyl)amino)-2,3-dihydro-1H-indene4-carbonitrile ((S)-3a), a key intermediate in the synthesis of Ozanimod, an FDA-approved
sphingosine-1-phosphate (S1P) receptor modulator for the treatment of relapsing forms
of multiple sclerosis. First activity of 272 IREDs toward 1-((2-hydroxyethyl)imino)-2,3dihydro-1Hindene-4-carbonitrile (2a) was determined. The (S)-IR262 from the Polyangiaceae
bacterium was selected for further improvement of activity through enzyme engineering
based on the obtained analytical yield. After docking 2a to the active pocket of IR262,
50 residues were selected for alanine scanning. Using cell-free extracts of all obtained
mutants, the reduction of 2a (10 mM) was achieved with analytic yields from 48–60%
(S110A, F185A, and T225A) and from 5–7% with M191A, F229A, and T248A. Further
mutations of these six amino acid residues into the 19 other amino acid residues gave
mutants F185E, M191H, M191L, M191T, F229L, F229Y, and T248Y. These mutants showed
higher analytical yields (65–79%) than the wild-type enzyme (60%). When the enzyme
loadings were reduced from 10 to 5 mg of wet cell weight/mL, markedly higher conversion
yields were obtained with M191L, F185E, and F229L (61%, 55%, and 54%, respectively)
compared to IR262 (39%), with >99% ee. In the last round, double mutants F185E/M191L,
F185E/F229L, and M191L/F229L were constructed, and as a result, a mutant F185E/F229L
with a 1.8-fold enhanced analytic yield (72%) compared to that of IR262 was obtained.
Using cell-free extracts of F185E/F229L, a preparative scale asymmetric reduction of a key
chiral intermediate of Ozanimod was performed in a 50 mL reaction system. Final reaction
gave product in 70% (1.42 g) isolated yield and >99% enantiomeric excess (ee). Additionally,
four (S)-N-hydroxyethyl amino indane derivatives were synthesized at a 1 mmol scale with
high isolated yields (57–75%) and excellent stereoselectivities (>99% ee). This represents a
green and scalable biocatalytic route to a pharmaceutically relevant compound [42]. The
synthetic procedure for the Ozanimod intermediate using engineered imine reductase is
presented in Figure 11.

Figure 11. Schematic representation of Ozanimod synthetic procedure using engineered imine
reductase IR262 from Polyangiaceae bacterium.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

16 of 30

In another study, performed by Li and collaborators, a combination of computeraided semi-rational design and experimental screening was applied to the imine reductase NaIRED from Nocardiopsis aiba to enable the efficient reduction of myosmine to (S)Nornicotine, a pharmacologically active tobacco alkaloid that enhances cognition, regulates
mood, manages pain, and assists in tobacco cessation. NaIRED achieved a conversion rate
of 75.4% for 2.5 g/L myosmine, with an enantiomeric excess value of 96.10%. Based on the
results from HotSpots analysis, molecular docking, three-dimensional protein structure
coupling, and conservation analysis, 16 key sites (T99, I124, M125, A126, T127, M130,
D174, L178, M181, Y182, L212, 246 W214, A215, M216, W241, and T242) were selected
for modification. Exceptional conversion rates and ee exceeding 99.0% were achieved
with mutants A126N, T127P, 273 D174E, and L178C. Conversion rates of 36.6% and 31.2%
were achieved with mutants A126N and M181L, respectively, when the myosmine concentration was increased to 30 mg/mL. In the second round of combinatorial mutations,
an increased conversion rate of up to 50.8% at a myosmine concentration of 30 mg/mL
was reached with mutant A126N/M181. Structural analysis and molecular dynamics
simulations revealed that reorganization of the hydrogen-bonding network, remodeling of
the binding pocket, and increased conformational flexibility underpinned the improved
catalytic activity and stereoselectivity. Furthermore, optimized bioprocessing enabled complete substrate conversion at 50 g/L using sarcosinase catalysis, allowing the gram-scale
production of enantiopure (S)-Nornicotinic acid. These findings not only demonstrate
the utility of NaIRED in asymmetric synthesis but also highlight its potential to reduce
production costs of (S)- Nornicotine and related compounds in industrial applications [43].
2.2. Engineered Imine Reductases for API and API Intermediate Synthesis on a Small Scale
While several imine reductases (IREDs) have already found commercial applications
in the large-scale synthesis of pharmaceuticals, many promising IREDs are still being
explored at the laboratory or pilot scale, where their catalytic potential is being assessed
under various process conditions. These lower-scale applications serve as a critical testing
ground for evaluating enzyme performance, substrate scope, and scalability. Engineering
efforts continue to focus on improving the efficiency, selectivity, and robustness of IREDs
to meet the specific demands of active pharmaceutical ingredient (API) and intermediate
synthesis. This phase of development is crucial for expanding the enzyme toolbox available
to process chemists and for enabling more sustainable and cost-effective synthetic strategies
in early-stage drug development and niche manufacturing.
Accessing complex chiral amines with multiple stereocenters remains a significant
challenge in drug discovery. Casamajo et al. developed a biocatalytic method to selectively
produce a specific (S,S,S)-diastereomer of a chiral amine building block from a racemic
ketone, using an engineered reductive aminase (RedAm). In this case, the RedAm IR-09 was
engineered via structure-guided mutagenesis, yielding the W204R variant, which achieved
45% conversion and 95% enantiomeric excess (ee) in the selective synthesis of the desired
stereoisomer. The product was further processed via palladium-catalyzed deallylation,
yielding the target primary amine in 73% yield. Notably, the engineered enzyme retained its
stereoselectivity and catalytic efficiency on a preparative scale, demonstrating its potential
for further optimization and industrial application [44].
RedAms have also been explored for the selective synthesis of cyclic tertiary amines
through the reductive amination of cyclic secondary amines with aldehydes and ketones.
This transformation, which remains challenging for traditional chemical methods, was
enabled by engineered variants, such as RedAm-361, which showed significantly improved
activity and enantioselectivity. Through directed evolution, RedAm-361 was engineered
to efficiently couple cyclic amines with carbonyl compounds, enabling both dynamic

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

17 of 30

kinetic resolution of α-functionalized aldehydes and enantioselective reductive amination
of ketones. Notably, introducing just one or two mutations into RedAm-361 resulted in a
29-fold increase in activity, highlighting its high evolvability. These engineered variants
proved effective in preparative-scale biotransformations, making them promising scaffolds
for the development of industrial biocatalysts aimed at producing cyclic tertiary amines
commonly found in bioactive compounds [45].
A chemoenzymatic synthesis of Rotigotine was developed using an engineered IR-36M5 IRED mutant, optimized through structure-guided semi-rational design. By targeting
two key active-site residues (F260 and M147), a double mutant F260W/M147Y was created,
showing excellent S-selectivity (>99%) and good yield in the synthesis of (S)-2-aminotetralin
from bulky amine donors. This biocatalytic reductive amination served as the key step in a
three-step gram-scale synthesis of Rotigotine, achieving 62% overall yield and highlighting
the mutant’s utility for producing chiral amines relevant to pharmaceuticals like Parkinson’s
treatments [46].
Zhu and colleagues engineered an imine reductase (IRED) for the asymmetric synthesis
of a key chiral intermediate of Evocalcet, addressing longstanding challenges in its chemical
synthesis (Figure 12).

Figure 12. Schematic representation of Evocalcet synthetic procedure using engineered imine reductase PcIRED from Penicillium camemberti.

Evocalcet, a second-generation calcimimetic used to treat secondary hyperparathyroidism, requires a complex, multistep synthesis of its chiral intermediate, (3S)-3-1-[(2methylpropan-2-yl)oxycarbonyl]pyrrolidine (1a). Traditional synthetic routes involve
multiple protection/deprotection steps, challenging chromatographic separations, and
limited stereocontrol, making the process inefficient and industrially cumbersome. To
overcome these limitations, Zhu et al. applied computational enzyme design to develop
the PcIRED-M3 W219L variant, which demonstrated an 8.9-fold improvement in catalytic
efficiency and an enantiomeric excess (S) of greater than 99%, compared to 63.15% with the
wild-type enzyme. Molecular docking studies revealed that the W219L mutation reduces
steric hindrance with the bulky naphthyl group and enhances hydride transfer by optimizing the substrate-cofactor geometry. Under optimized conditions, the W219L variant
achieved 62.7% conversion within 48 h, establishing the first enzymatic route to Evocalcet
intermediates. This study not only provides a more efficient and stereoselective alternative
to traditional methods but also showcases the broader utility of rational IRED engineering
in sustainable pharmaceutical manufacturing [47].
A concise two-step chemoenzymatic route was developed for the synthesis of (R)Selegiline (Figure 13), a key medication for early-stage Parkinson’s disease.

Figure 13. Schematic representation of (R)-Selegiline synthetic procedure using engineered imine
reductase IR36-M5.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

18 of 30

The key transformation involves a stereoselective biocatalytic reductive amination
using the engineered imine reductase IR36-M5, which achieved 97% conversion and 97% ee
in the reaction of phenylacetone and propargylamine, forming the chiral intermediate (R)desmethylselegiline [48]. In their previous research, they had demonstrated that IR36-M5
could catalyze reductive amination reactions involving piperidine and azepane alkylamines,
including the ability to enhance and invert stereocenters, depending on the substrate [49,50].
In particular, they developed a biocatalytic platform for the enantio-complementary synthesis of pyrrolidinamines using engineered IREDs from Actinoalloteichus hymeniacidonis,
identifying two variants with opposite stereoselectivity (>99% ee) through structure-guided
mutagenesis. This strategy enabled short syntheses of intermediates for drug candidates
such as Leniolisib and a JAK1 inhibitor, showcasing the utility of tailored IREDs in pharmaceutical synthesis [49]. Building on this, they further engineered the IR36 scaffold to
achieve, for the first time, asymmetric synthesis of chiral S-azepane-4-amines. By identifying three key residues (149, 200, and 234) through structure-guided design, they developed
a triple mutant (I149Y/L200H/W234K) with high S-selectivity (>99% ee), offering valuable
chiral building blocks for pharmaceutical development [50]. Encouraged by these advances,
the researchers turned their attention to linear ketone substrates such as phenylacetone,
aiming to improve stereoselectivity with propargylamine as the donor. Using a structureguided semi-rational design strategy focused on active-site residues interacting with the
ketone moiety, they identified five new IR36 variants with slightly improved R-selectivity
(98% ee) compared to M5 (97% ee), albeit with lower conversion. Ultimately, IR36-M5 was
selected as the optimal biocatalyst due to its balance of efficiency and stereoselectivity. The
second step, a reductive amination of (R)-1a with formaldehyde, completed the synthesis
of (R)-Selegiline [48].
Engineered IRED was used for the synthesis of both R- and S-alkylated amphetamines
and their derivatives through asymmetric reductive amination. By combining structural
analysis, semi-rational design, and mechanistic insights, key active-site residues were identified that control stereoselectivity, even with less bulky ketone substrates. Two enzyme
variants, I149Y-W234L and L200M-F260M, were developed, exhibiting enhanced and reversed stereoselectivity with enantiomeric excesses of up to 99% S and 99% R, respectively.
These variants also demonstrated high conversion and selectivity across a range of substrates. The platform’s synthetic utility was proven through the successful production of
pharmaceutical intermediates such as benzphetamine, Selegiline, and Formoterol, offering
a sustainable and green approach to chiral amine synthesis [51].
In another example, a biocatalytic dynamic kinetic resolution (DKR) approach was
established for the atroposelective synthesis of axially chiral biaryl aminoalcohols. By
engineering an imine reductase from Streptomyces sp. (variant S-IRED-Ss-M11) through
directed evolution, the authors enabled a transient aza-acetal bridge-promoted racemization
coupled with an IRED-catalyzed stereoselective reduction, effectively constructing the
stereogenic axis under ambient conditions. The optimized enzyme exhibited a broad
substrate scope, delivering products in up to 98% yield and >99:1 enantiomeric ratio under
mild conditions. Molecular dynamics simulations helped elucidate the structural basis for
the enzyme’s enhanced activity and selectivity. This study expands the synthetic utility of
IREDs toward constructing challenging atropisomeric biaryls [52].
In another study, efforts were made to enhance the catalytic efficiency of IRED enzymes toward sterically demanding substrates, such as α-methylphenylethylamine. The
engineered IRED M5 exhibited low activity with this bulky amine, prompting a rational
design approach to enhance its performance. Two key mutations, F260A and M203V, were
introduced. The F260A variant led to more than a twofold increase in tert-butyl 3-(((R)-1phenylethyl)amino)piperidine-1-carboxylate yield and a significant improvement in stere-

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

19 of 30

oselectivity when applied to tert-butyl 4-(((S)-1-phenylethyl)amino)azepane-1-carboxylate,
with enantiomeric excess rising from 9.03% to 86.40% for the (S)-enantiomer. M203V
mutant also improved yields for 3-(((R/S)-1-phenylethyl)amino)piperidine-1-carboxylate.
Additionally, the study provided insights into the possible molecular mechanisms behind
these enhancements, contributing to a deeper understanding of rational IRED design for
challenging substrates [53].
Developing sustainable and selective methods for synthesizing chiral hydrazines is
of growing interest, particularly given their relevance as intermediates in pharmaceutical
synthesis. A recent study presents a novel biocatalytic approach using imine reductases
(IREDs) for the reductive amination of ketones with hydrazine hydrate, enabling the efficient formation of chiral hydrazines, a transformation not previously reported for this
enzyme class. Starting from a wild-type IRED with almost no activity, the researchers applied a mechanism-driven protein engineering strategy, guided by transition state analogue
(TSA) modeling, to redesign the enzyme’s active site. This rational approach led to the
development of the M6 variant, which showed dramatically improved catalytic performance. The engineered M6 enzyme efficiently converted 3-cyclopentyl-3-oxopropanenitrile
into a key chiral intermediate for Ruxolitinib, achieving high conversion and excellent
enantioselectivity (Figure 14).

Figure 14. Schematic representation of Ruxolitinib synthetic procedure using engineered imine
reductase IRED from Streptosporangium roseum.

Beyond this specific application, the work demonstrates a generalizable framework
for transforming non-reactive enzymes into highly active biocatalysts through precise
active-site modifications [54].
Expanding the synthetic utility of IREDs further, this study demonstrated their ability
to control two vicinal stereocenters within an N-heterocyclic scaffold, using a reversed
oxidative mode. Specifically, PRO-IRED-128 was employed in an oxidative kinetic resolution (KR) of a racemic intermediate of Avacopan, selectively leaving the desired (2R,3S)enantiomer intact (99.5% ee) while oxidizing the undesired one to an enamine byproduct. A
1 kg-scale biocatalytic process was developed that integrates alcohol dehydrogenase (ADH)
for efficient cofactor regeneration, using acetone as a sacrificial substrate for the first time in
this context. Importantly, the oxidized enamine was recycled via catalytic hydrogenation,
enabling multiple KR-recycle cycles and thereby boosting the overall theoretical yield
to 72%, which surpasses the typical 50% limit of classical resolution. Additionally, the
enantio-complementary PRO-IRED-351 was utilized in a dynamic kinetic reduction of the
enamine back to the desired diastereomer, achieving excellent stereoselectivity and further
enhancing the process efficiency. This work highlights a highly innovative application of
IREDs in oxidative resolution and dynamic kinetic transformations, especially valuable for
complex pharmaceutical intermediates [55].
A distinct approach was taken in the engineering of Mesorhizobium imine reductase
(MesIRED) to improve the synthesis of N-benzyl cyclo-tertiary amines, essential intermediates in the synthesis of natural products and pharmaceuticals. Unlike traditional
methods, which often suffer from low activity and selectivity for these sterically hindered

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

20 of 30

substrates, this study applied alanine scanning and consensus mutagenesis, leading to the
identification of two highly active variants: mutant for conversion of N-benzylpyrrolidine
MesIREDV212A/I213V (M1) and conversion of N-benzylpiperidine MesIREDV212A/I177A/A241I
(M2). These mutants demonstrated notable improvements in conversion, from ~23% in the
wild-type to 74.3% and 66.8%, respectively. Further analysis revealed that both variants possess more efficient tunnels, facilitating the transformation of bulkier amine products. The
use of whole-cell biocatalysts coexpressing MesIRED and glucose dehydrogenase (GDH)
in E. coli enabled high conversions of 75.1% for N-benzylpyrrolidine (M1) and 88.8% for
N-benzylpiperidine (M2). A preparative-scale reaction with M2 yielded 86.2% conversion
and 60.2% isolated yield, confirming the system’s practicality for scale-up [56].
Further expanding the synthetic utility of imine reductases and related reductive
aminases (RedAms), a novel reductive aminase, SiRA, identified via genome mining
from Streptomyces iridochromogenes, was shown to efficiently catalyze the formation of
N-substituted β-amino esters, a valuable class of chiral amines used extensively in pharmaceutical synthesis. SiRA demonstrated outstanding diastereo- and enantioselectivity (up
to >99% ee, 97% de) in the reductive amination of 2-oxocyclohexane-1-carboxylate with
cyclopropylamine, operating optimally at pH 7.0 and 40 ◦ C. Importantly, SiRA displayed
substrate-dependent enantioselectivity, producing different stereoisomers when using alternative amine donors such as methylamine and pyrrolidine. Through alanine scanning,
key residues M183 and H244 were identified as critical for controlling enantioselectivity
towards methylamine and pyrrolidine. According to interaction analysis, enantioselectivity
is highly influenced by the position of the ester group within the active site. These results
highlight SiRA as promising RedAm biocatalysts for the tailored, enantioselective synthesis
of structurally diverse N-substituted β-amino esters [57].
Another illustrative example is the engineering of the imine reductase SIR46 from
Streptomyces sp. GF3546, which was initially limited by low stability and modest activity.
Through directed mutagenesis, an improved variant, SIR46 M9, was obtained, exhibiting a
twofold increase in activity compared to the wild type, enhanced thermostability (maintaining activity even at 50 ◦ C), and remarkable storage stability at 4 ◦ C for over one month.
When implemented as a whole-cell biocatalyst in Rhodococcus erythropolis together with
a glucose dehydrogenase gene from Bacillus subtilis (BsGDH) for cofactor regeneration,
this system enabled efficient and scalable synthesis of (S)-2-methylpyrrolidine from high
concentrations of 2-methyl-1-pyrroline (up to 500 mM). In addition, the variant exhibited
improved activity toward other cyclic imines and reductive amination reactions, confirming
its potential as a robust and versatile biocatalyst for industrial synthesis of valuable chiral
amines [58].
Another significant advancement was achieved by engineering the Myxococcus stipitatus IRED to alter both (S)-selectivity and NADH specificity in the asymmetric reduction
of 2-methylpyrroline. Through semi-rational mutagenesis of the NADH-dependent variant (NADH-IRED-Ms), a quintuple mutant (A241V/H242Y/N243D/V244Y/A245L) was
obtained that completely inverted stereopreference, affording the (S)-amine product with
>99% conversion and 91% ee. Crystal structures of the wild-type and engineered enzymes,
together with molecular dynamics simulations, revealed how targeted changes in the
substrate-binding pocket govern stereochemical outcome. This study represents the first
report of an (S)-selective NADH-dependent IRED and illustrates how combining mutagenesis with structural and computational analysis can rationally guide stereoselectivity
switching in these biocatalysts [59].
A summary of protein engineering efforts and results for imine reductase, developed
for potential industrial application, is given in Table 1.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

21 of 30

Table 1. Summary of developed imine reductases using protein engineering methods with potential for industrial application.
Engineering Strategy

Key Mutations

Effect/Improvement

Application

Ref.

IR-46 (Saccharothrix
espanaensis)

Semi-rational design

Y142S/L37Q/A187V/L201F/V215I/Q231F,
S258N/G44R/V92K,
F97V/L198M/T260C/A303D

~38,000-fold TON over wt; increased
stability and specific activity over wt

GSK2879552 intermediate
in 84.4% yield and 99.7% ee

[32]

IR1 (Leishmania major)

Structure-guided saturation
mutagenesis

Y194F/D232H

61-fold increase in catalytic efficiency

Suvorexant intermediate

[33]

IRED-88

Machine-directed
evolution/DMS/epPCR

Q194L/S220T/H230Y

Improved activity and (R)-selectivity

H4 receptor antagonist ZPL389
in 98% ee and 72% yield

[34]

SpRedAm
(Streptomyces
purpureus)

Computationally guided and
data-driven mutagenesis

N131H/A170C/F180M/G217D

High yield and cis-selectivity

Abrocitinib intermediate in
>99% purity and >99:1 cis:trans

[35]

IR-G36
(Actinoalloteichus
hymeniacidonis)

Rational cavity design and
NNK codon degeneracy
saturation mutagenesis

N121T/S260F/F207I/M238A/M264H/
A267H/L197I/N271K/H189A/G145K

4193-fold higher catalytic efficiency;
+16.2 ◦ C increase in Tm

Azacycloalkylamines in
>99% ee/pharma building
blocks

[7]

ScIRED (Streptomyces
clavuligerus)

Docking-guided SSM and
interface engineering

F177W/V122C/M169W/
W185L/S211G/M270E/G214F/V232A/E45A/
D53T/F265L

~107-fold specific activity increase; 32 ◦ C
increase in Tm

Larotrectinib intermediate

[36]

PcIRED (Penicillium
camemberti)

Iterative saturation
mutagenesis

Q244A/L180V/H250N/M216T/S247A/
S181A/C174N/V210I (M3)

Up to 488-fold activity increase; 9 ◦ C
increase in Tm
75.6 g L−1 day−1 (STY)

Cinacalcet synthesis in >99% ee
(R), at 84.7%
isolated yield

[37]

IR141
(Promicromonospora
sp. CF082)

Docking-guided saturation
mutagenesis

L172M/Y267F

catalytic efficiency improvement and
increase in Tm over wt

TAK-981-related THIQ
intermediates

[38]

IR007 (Amycolatopsis
azurea)

SSM, ISM, CASTing,
recombination

E120A/M197W/D238G/I240L/M206S/A213P

Improved conversion and
thermostability

CDK 2/4/6 inhibitor
intermediate in 43% conversion
and 98.4% ee

[39]

PocIRED (Pochonia
chlamydosporia)

Multi-round combinatorial
mutagenesis, CAST library;
NNK saturation mutagenesis

Q239G/P125T/S40E/V124T/I127E/L128Y/
S72N/Y73Q/T76V/K195A/G180S/R220V/
A47P/V50A/F210L/K212A/W217Q/I178V/
H224R/L236I

Improved thermostability; >99.9% ee,
>99:1 dr

β-Branched
amines/Tofacitinib-type targets
in 74% isolated yield

[40]

IR61 (Jiangella
muralis)

Docking-guided saturation
mutagenesis

P123A/W179G/F182I/L212V/V69Y

Up to 766-fold catalytic efficiency
improvement;
STY of 542 g L−1 d−1

Dextromethorphan
intermediate in 77% isolated
yield; >99% ee

[41]

IR262 (Polyangiaceae
bacterium)

Alanine scanning + targeted
mutagenesis

F185E/F229L

Improved analytical yield and
maintained >99% ee

Ozanimod intermediate

[42]

NaIRED (Nocardiopsis
alba)

Computer-aided semi-rational
design

A126N/M181L

Improved catalytic activity and
stereoselectivity; Increased conversion at
high myosmine loading

(S)-Nornicotine synthesis

[43]

RedAm IR-09

Structure-guided mutagenesis

W204R

Improved conversion and ee

Chiral building blocks with
multiple stereocenters

[44]

Enzyme (Source)

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

22 of 30

Table 1. Cont.
Enzyme (Source)

Engineering Strategy

Key Mutations

Effect/Improvement

Application

Ref.

RedAm-361

Directed evolution

One- and two-point mutants

Up to 29-fold activity increase

Cyclic tertiary amines

[45]

IR-36-M5

Structure-guided semi-rational
design

F260W/M147Y

High S-selectivity (>99%) and useful
conversion

Rotigotine synthesis

[46]

PcIRED-M3
(Penicillium
camemberti)

Rational engineering

W219L

8.9-fold increase in catalytic efficiency;
>99% ee

Evocalcet intermediate

[47]

IR36-M5

Structure-guided semi-rational
design

Retained M5 scaffold; compared with new
active-site variants

Best balance of conversion and
R-selectivity

Selegiline synthesis

[48]

IR36 (Actinoalloteichus
hymeniacidonis)

Structure-guided semi-rational
design

S241L/F260D
S241L/F260E
S241L/F260N
I149D/W234I
I149H/W234I

>99% ee for pyrrolidinamines

Pyrrolidinamine intermediates

[49]

IR36 (Actinoalloteichus
hymeniacidonis)

Semi-rational design

I149Y/L200H/W234K

High S-selectivity (>99% ee)

Alkylated S-4-azepanamines

[50]

IRED variants
(Actinoalloteichus
hymeniacidonis)

Semi-rational
design/mechanistic
engineering

I149Y-W234L/L200M-F260M

Enantiodivergent synthesis up to 99% ee

Alkylated amphetamines

[51]

S-IRED-Ss-M11
(Streptomyces sp.)

Directed evolution

R158L/V48T/S209R/A103M/A90V/A41P/
A162P/M207T/V88T/M236T/
P122N

Improved yield and enantioselectivity

Axially chiral biaryls
aminoalcohols

[52]

IR-G36-M5

Rational design

F260A, M203V

Improved conversion/stereoselectivity
for bulky amines

α-Methyl-benzylamino
N-heterocycles

[53]

IRED
(Streptosporangium
roseum)

Mechanism-driven protein
engineering

A233C/
F215L/F132M/L92F/A118I/G278S

Yield of 98% and an ee of 99%.

Ruxolitinib intermediate

[54]

PRO-IRED-128/PROIRED-351

Engineering for oxidative
KR/DKR

Engineered proprietary variants

Excellent stereoselectivity and scalable
process

Avacopan intermediate

[55]

MesIRED
(Mesorhizobium sp.)

Alanine scanning + consensus
mutagenesis

V212A/I213V (M1) V212A/I177A/A241I (M2)

A preparative-scale reaction with M2
yielded 86.2% conversion and 60.2%
isolated yield for N-benzylpiperidine

N-benzyl cyclo-tertiary amines

[56]

Novel IRED
(Streptomyces
viridochromogenes)

Alanine scanning/mutagenesis

M183, H244 identified as key enantioselectivity
residues

Tailored enantioselectivity

Cyclic β-ketoester reductive
amination

[57]

GF3546 IRED
(Streptomyces sp.
GF3546)

Directed mutagenesis

R158L/V48T/S209R/A103M/A90V/A41P/
A162P/M207T/V88T

Higher activity, better thermostability,
and storage stability

(S)-2-methylpyrrolidine/cyclic
amines

[58]

NADH-IRED-Ms
(Myxococcus
stipitatus)

Semi-rational mutagenesis

A241V/H242Y/N243D/V244Y/A245L

Inverted stereoselectivity;
NADH-dependent (S)-selective variant
with >99% conversion and 91% ee

2-Methylpyrroline reduction

[59]

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

23 of 30

2.3. Immobilized Imine Reductases in Drug Synthesis
Immobilization of enzymes enhances their stability across various temperatures and
organic solvents, improving operational stability and reusability across consecutive cycles.
This, in turn, makes the enzyme-catalyzed process more economically viable. There have
been a few reports on the production of active substances using immobilized imine reductases. Benítez-Mateos et al. have studied the reduction of heterocyclic imines with N, S, or O
substitution at C-4, compounds crucial for antibiotic synthesis, in the presence of six imine
reductases and glucose dehydrogenase from Bacillus megaterium. Of the six IREDs, four were
suitable for immobilization on porous microparticles, and their immobilization efficiency
and reusability were investigated. IRED-4 from Goodfellowiella coeruleoviolacea immobilized
on a methacrylate support EP400SS/EDA and IRED-5 from Labilithrix luteola immobilized
on agarose-based carrier Ag/epoxy-metal have shown the most promising efficiency and
reusability, and were further applied in combination with GDH immobilized on a support
composed of methacrylate with long-chain amino-epoxy (HFA403/S, Figure 15).

Figure 15. Schematic representation of imine substrate reduction by IRED-4 from Goodfellowiella
coeruleoviolace immobilized on EP400SS/EDA or IRED-5 from Labilithrix luteola immobilized on
Ag/epoxy-metal in combination with GDH immobilized on HFA403/S, in continuous flow mode.

The reaction conditions were optimized (37 ◦ C, IRED: GDH ratio of 1:1, and 2 equiv of
glucose). The conversion of 90% (±4.9) was achieved after 10 reaction cycles, each lasting
2 h. In the continuous-flow reactor, high conversions (98% and 91% for IRED-4 and IRED-5,
respectively) of 5-methyl-3,6-dihydro-2H-1,4-thiazine into the corresponding amine were
obtained at a substrate concentration of 10 mM. In contrast, lower conversions (61% for
IRED-4 and 46% for IRED-5) were observed with 100 mM substrate. Both enzymes are
stereoselective (>99% ee); with IRED-4, the corresponding (S)- amine was synthesized,
whereas its (R)- form was obtained when IRED-5 catalyzed the process. Operational stability
in the continuous flow was demonstrated over 20 column volumes, each corresponding
to 30 min at 37 ◦ C, with high conversions of nearly 90% maintained after each column
volume [60].
Guan and co-workers have synthesized (S)-Nornicotine, an intermediate in Nicotine
preparation, from myosmine using the enzyme IRED from Aeromonas veronii and GDH from
Bacillus megaterium, co-immobilized on LXTE either with amino or epoxy resins (Figure 16).

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

24 of 30

Figure 16. Schematic representation of myosmine conversion to (S)-nornicotine by using the enzyme
IRED from Aeromonas veronii and GDH from Bacillus megaterium, co-immobilized on LXTE support in
continuous flow mode.

Thirteen different resins were tested as carriers for the enzyme immobilization. LXTE706 and LXTE-707 are the most promising, as the highest enzyme recovery and specific activity were achieved when IRED was immobilized on these carriers (39.66% and 21.54 U/g
resin, respectively, for IRED@LXTE-706, and 26.62% and 14.44 U/g resin, respectively, for
IRED@LXTE-707). The coimmobilized enzyme system IRED&GDH@LXTE-706 demonstrated the highest recovery rate and specific activity and was used in further experiments.
The immobilization process was optimized with respect to the IRED:GDH ratio, pH, temperature, and time to achieve maximum catalytic activity (IRED:GDH = 3:1, pH 6, 25 ◦ C,
4 h). The thermal stability of co-immobilized enzymes in the temperature range of 10 to
40 ◦ C was substantially improved compared to that of free enzymes. Additionally, the pH
tolerance of co-immobilized IRED and GDH was considerably enhanced across a wide
pH range. Residual activities of IRED and GDH of 74.44% and 99.41%, respectively, were
obtained when storing IRED&GDH@LXTE-706 at 4 ◦ C for 22 days. The coimmobilized
enzyme system IRED&GDH@LXTE-706 was employed for the synthesis of (S)-Nornicotine
in batch mode. High conversion rates of more than 99.00% were obtained over 40 cycles
of use. The prepared product had a high chiral purity (99.90%). However, the enzyme
activity gradually decreased up to 61.00%. In continuous-flow mode at the optimal flow
rate (2.99 mL/min) over 40 cycles, complete conversion was achieved upon addition of
NADP. A space-time yield of the continuous flow reaction system was 289.7 times higher
than that of the batch reaction system. The final yield of (S)-Nornicotine was 78.54% [61].
The reduction of 2-methylpyrroline with immobilized either IRED from Streptomyces
GF3587 (IR-Sgf3587) or its K40A variant was studied by Gand and coworkers. Purified
IRED and K40A variants were immobilized on six different EziGTM carriers with nickel
chelated on the surface (Figure 17).
The greatest protein binding, exceeding 90%, was achieved with the EziGTM E2 carrier
and was substantially higher than that of other tested carriers. The enzyme leaked from
3 different carriers (E1, E2, and E3) was in the range of 4.4 ± 0.1 to 7.8 ± 1.4%. The reusability
of immobilized IRED and K40A, prepared from crude extract or purified enzymes, was
studied by reducing 2-methylpyrroline using these immobilisates over 13 cycles. Among
the 3 tested carriers, EziGTM E2 has shown to be the most promising in terms of reusability.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

25 of 30

The highest conversion, nearly 100%, was achieved after 6 cycles when enzymes were
immobilized on the EziGTM E2 carrier. After the sixth cycle, considerable loss of activity was
observed. Higher conversion rates were achieved with the immobilized material from the
crude extract than with the purified enzyme. The authors studied the effect of the cofactor
on the conversion degree and reaction time. Complete conversion was achieved after 31 h
when NADPH was used as a cofactor in conjunction with WT IRED. When using the NADH
cofactor, 24% lower conversion was obtained after 66.5 h. When combining the K40A variant
with NADH, improved conversion (88%) was achieved in a shorter time (51 h) [62].

Figure 17. Schematic representation of 2-methylpyrroline reduction by using the IRED from Streptomyces
GF3587 or its K40A variant immobilized on an EziGTM E2 support in continuous flow mode.

In a combined approach, through site-directed mutagenesis of IR-G36-M5 and subsequent immobilization in ZIF-8, Ren et al. developed the process for chemoenzymatic
synthesis of first-in-class SLC6A19 inhibitor JNT-517, which is undergoing Phase II clinical trials for phenylketonuria. This same research group previously engineered IRED (IR-G36-M5)
capable of catalyzing the reductive amination of N-Boc-3-piperidinone with cyclopropylamine. In their latest research, the enzyme was subjected to further evolution, yielding
double mutant M203A/S241L, whose enantioselectivity was enhanced from 87% to >99% ee
for the R-configuration, and it showed 38% increase in catalytic efficiency (Figure 18).

Figure 18. Schematic representation of (R)-N-cyclopropylpiperidin-3-amine synthesis by using the
IRED-G36-M5 mutant M203A/S241L immobilized in ZIF-8.

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

26 of 30

They demonstrated that the obtained mutant immobilized within ZIF-8 retained 40%
residual activity after 21 days at ambient temperature with a >80% conversion maintained
after 5 reuse cycles, and a space–time yield of 4.7 g g−1 h−1 in batch operations. The
enzymatically produced (R)-N-cyclopropylpiperidin-3-amine was converted to JNT-517 in
three chemical steps, demonstrating a synthetic route with reduced reliance on hazardous
reagents and offering a greener manufacturing alternative for this compound [63].
An overview of imine reductase immobilization methods and results is given in Table 2.
Table 2. Overview of imine reductases immobilization methods and results.
Enzyme (Source)

Immobilization Support

IRED-4 from Goodfellowiella
coeruleoviolacea
IRED-5 from Labilithrix
luteola
GDH from Bacillus
megaterium

IRED 4—methacrylate
support EP400SS/EDA
IRED 5—agarosebased carrier
GDH—HFA403/S

IRED from Aeromonas veronii
GDH from Bacillus
megaterium

Co-immobilization on
LXTE support with amino
or epoxy resins
(IRED&GDH@LXTE-706)

IRED from Streptomyces
GF3587 or its K40A variant

EziGTM carriers with Ni2+
chelated on the surface

Mutant M203A/S241L of
engineered IR-G36 M5

ZIF-8

Immobilization
Method/Type

Effect/Improvement

Ref.

Covalent
immobilization

Improved stability and
reusability. IRED-4—98% and
IRED-5—91% conversion of
10 mM 5-methyl-3,6-dihydro-2H1,4-thiazine.

[60]

Covalent
immobilization

Improved thermal, pH and
storage stability. Synthesis of
(S)-Nornicotine (78.54% yield) in
continuous-flow mode over
40 cycles. STY—289.7 times
higher than that of the batch
reaction system.

[61]

Affinity immobilization

Nearly 100% conversion after
6 cycles when reducing
2-methylpyrroline with EziGTM
E2 carrier.

[62]

In situ encapsulation/Biomineralization

Synthesis of
(R)-N-cyclopropylpiperidin-3amine—80% conversion after
5 reuse cycles. STY of
4.7 g g−1 h−1 in batch
operations.

[63]

3. Conclusions and Future Directions
Imine reductases have evolved from promising laboratory curiosities into powerful
and broadly applicable biocatalysts for the sustainable synthesis of chiral amines. Over
the past decade, advances in protein engineering have produced enzyme variants with
markedly improved catalytic activity, stereoselectivity, thermostability, and tolerance to
demanding process conditions. These improvements have enabled their application in
preparative and even kilogram-scale synthesis of pharmaceutical intermediates. In parallel,
developments in enzyme immobilization have facilitated the transition from laboratory
studies to industrial implementation by improving operational stability, enabling enzyme
reuse, and supporting integration into continuous-flow biocatalytic systems.
Future research will likely focus on expanding the substrate scope of IREDs, particularly toward sterically demanding imines. Structure-guided mutagenesis, directed
evolution, and machine-learning-assisted library design are expected to accelerate the
discovery of improved biocatalysts. Equally important will be the development of advanced high-throughput screening platforms that integrate microfluidics, automation, and
real-time activity detection, allowing rapid evaluation of large mutant libraries under
process-relevant conditions. Surface display technologies may further enhance both screening and immobilization strategies by enabling the direct presentation of enzyme variants
on cell surfaces or synthetic carriers.
The discovery of novel IREDs from metagenomic resources will likely reveal enzymes
with new catalytic properties, while enzymes derived from extremophilic organisms may

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

27 of 30

provide improved robustness under challenging process conditions such as extreme pH,
organic solvents, or elevated temperatures. In addition, the development of continuousflow biocatalytic processes, combined with advanced immobilization supports, including
metal–organic frameworks and functionalized resins, offers significant potential to improve
space–time yields and process efficiency. Continued progress in cofactor regeneration
strategies, including electrochemical approaches and the design of cofactor-efficient enzyme
variants, will further enhance the industrial viability of IRED-based transformations.
Overall, the integration of protein engineering, high-throughput discovery, enzyme
immobilization, and process intensification will play a key role in establishing IREDcatalyzed synthesis as a versatile and sustainable platform for the industrial production of
chiral amines.
As the field of biocatalysis continues to advance, imine reductases are poised to become
central tools in next-generation sustainable synthesis, integrating enzyme engineering,
process intensification, and green chemistry principles to efficiently produce chiral amines.
Author Contributions: Conceptualization, N.K. and R.P.; writing—original draft preparation, N.K.,
N.P.K., A.S. and M.S.S.; writing- review and editing, N.K. and R.P.; visualization, M.S.S., N.S. and
O.P.; funding acquisition, O.P. and N.S. All authors have read and agreed to the published version of
the manuscript.
Funding: This work was supported by the Ministry of Science, Technological Development and
Innovation of the Republic of Serbia. [Contract No. 451-03-136/2025-03/200026, University of
Belgrade- Institute for Chemistry, Technology and Metallurgy, National Institute of the Republic
of Serbia; Contract No. 451-03-136/2025-03/200168, University of Belgrade-Faculty of Chemistry;
Contract No. 451-03-136/2025-03/200288, University of Belgrade-Innovative Centre of the Faculty
of Chemistry; and Contract No. 451-03-33/2026-03/200053, University of Belgrade-Institute for
Multidisciplinary Research, National Institute of the Republic of Serbia].
Data Availability Statement: No new data were created or analyzed in this study. Data sharing is
not applicable to this article.
Acknowledgments: During the preparation of this manuscript, the author(s) used Grammarly PRO
v1.2.242.1855 for the purposes of English language editing. The authors have reviewed and edited
the output and take full responsibility for the content of this publication.
Conflicts of Interest: The authors declare no conflicts of interest.

References
1.

2.
3.
4.
5.
6.
7.

8.

Heinks, T.; Merz, L.M.; Liedtke, J.; Höhne, M.; van Langen, L.M.; Bornscheuer, U.T.; Fischer von Mollard, G.; Berglund, P.
Biosynthesis of Furfurylamines in Batch and Continuous Flow by Immobilized Amine Transaminases. Catalysts 2023, 13, 875.
[CrossRef]
Schrittwieser, J.H.; Velikogne, S.; Kroutil, W. Biocatalytic Imine Reduction and Reductive Amination of Ketones. Adv. Synth. Catal.
2015, 357, 1655–1685. [CrossRef]
Vitaku, E.; Smith, D.T.; Njardarson, J.T. Analysis of the Structural Diversity, Substitution Patterns, and Frequency of Nitrogen
Heterocycles among U.S. FDA Approved Pharmaceuticals. J. Med. Chem. 2014, 57, 10257–10274. [CrossRef]
Wang, Z.; Gao, G.-S.; Gao, Y.-D.; Yang, L.-C. Application of Imine Reductase in Bioactive Chiral Amine Synthesis. Org. Process Res.
Dev. 2024, 28, 3035–3054. [CrossRef]
Ghislieri, D.; Turner, N.J. Biocatalytic Approaches to the Synthesis of Enantiomerically Pure Chiral Amines. Top. Catal. 2014,
57, 284–300. [CrossRef]
Aleku, G.A. Imine Reductases and Reductive Aminases in Organic Synthesis. ACS Catal. 2024, 14, 14308–14329. [CrossRef]
Zhang, J.; Liao, D.; Chen, R.; Zhu, F.; Ma, Y.; Gao, L.; Qu, G.; Cui, C.; Sun, Z.; Lei, X.; et al. Tuning an Imine Reductase for
the Asymmetric Synthesis of Azacycloalkylamines by Concise Structure-Guided Engineering. Angew. Chem. Int. Ed. 2022,
61, e202201908. [CrossRef]
Mao, S.; Jiang, J.; Xiong, K.; Chen, Y.; Yao, Y.; Liu, L.; Liu, H.; Li, X. Enzyme Engineering: Performance Optimization, Novel
Sources, and Applications in the Food Industry. Foods 2024, 13, 3846. [CrossRef]

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

9.
10.
11.
12.
13.

14.
15.
16.
17.
18.
19.
20.

21.
22.
23.

24.

25.
26.

27.
28.
29.
30.
31.
32.

33.

28 of 30

Sangster, J.J.; Marshall, J.R.; Turner, N.J.; Mangas-Sanchez, J. New Trends and Future Opportunities in the Enzymatic Formation
of C−C, C−N, and C−O bonds. ChemBioChem 2022, 23, e202100464. [CrossRef]
Zawodny, W.; Montgomery, S.L. Evolving New Chemistry: Biocatalysis for the Synthesis of Amine-Containing Pharmaceuticals.
Catalysts 2022, 12, 595. [CrossRef]
Gilio, A.K.; Thorpe, T.W.; Turner, N.; Grogan, G. Reductive aminations by imine reductases: From milligrams to tons. Chem. Sci.
2022, 13, 4697–4713. [CrossRef]
Knaus, T.; Böhmer, W.; Mutti, F.G. Amine dehydrogenases: Efficient biocatalysts for the reductive amination of carbonyl
compounds. Green Chem. 2017, 19, 453–463. [CrossRef]
Mijts, B.; Muley, S.; Liang, J.; Newman, L.M.; Zhang, X.; LaLonde, J.; Clay, M.D.; Zhu, J.; Gruber, J.M.; Colbeck, J.; et al. Biocatalytic
Processes for the Preparation of Substantially Stereomerically Pure Fused Bicyclic Proline Compounds WO2010008828, 21 January
2010.
Yuan, B.; Yang, D.; Qu, G.; Turner, N.J.; Sun, Z. Biocatalytic reductive aminations with NAD(P)H-dependent enzymes: Enzyme
discovery, engineering and synthetic applications. Chem. Soc. Rev. 2024, 53, 227–262. [CrossRef]
Tseliou, V.; Masman, M.F.; Knaus, T.; Mutti, F.G. Current Status of Amine Dehydrogenases: From Active Site Architecture to
Diverse Applications Across a Broad Substrate Spectrum. ChemCatChem 2024, 16, e202400469. [CrossRef]
Sharma, M.; Mangas-Sanchez, J.; Turner, N.J.; Grogan, G. NAD(P)H-Dependent Dehydrogenases for the Asymmetric Reductive
Amination of Ketones: Structure, Mechanism, Evolution and Application. Adv. Synth. Catal. 2017, 359, 2011–2025. [CrossRef]
Telek, A.; Molnár, Z.; Takács, K.; Varga, B.; Grolmusz, V.; Tasnádi, G.; Vértessy, B.G. Discovery and biocatalytic characterization of
opine dehydrogenases by metagenome mining. Appl. Microbiol. Biotechnol. 2024, 108, 101. [CrossRef]
Ducrot, L.; Bennett, M.; Grogan, G.; Vergne-Vaxelaire, C. NAD(P)H-Dependent Enzymes for Reductive Amination: Active Site
Description and Carbonyl-Containing Compound Spectrum. Adv. Synth. Catal. 2021, 363, 328–351. [CrossRef]
Mitsukura, K.; Suzuki, M.; Tada, K.; Yoshida, T.; Nagasawa, T. Asymmetric synthesis of chiral cyclic amine from cyclic imine by
bacterial whole-cell catalyst of enantioselective imine reductase. Org. Biomol. Chem. 2010, 8, 4533–4535. [CrossRef]
Rodríguez-Mata, M.; Frank, A.; Wells, E.; Leipold, F.; Turner, N.J.; Hart, S.; Turkenburg, J.P.; Grogan, G. Structure and Activity of
NADPH-Dependent Reductase Q1EQE0 from Streptomyces kanamyceticus, which Catalyses the R-Selective Reduction of an
Imine Substrate. ChemBioChem 2013, 14, 1372–1379. [CrossRef]
Huber, T.; Schneider, L.; Präg, A.; Gerhardt, S.; Einsle, O.; Müller, M. Direct Reductive Amination of Ketones: Structure and
Activity of S-Selective Imine Reductases from Streptomyces. ChemCatChem 2014, 6, 2248–2252. [CrossRef]
Aleku, G.A.; France, S.P.; Man, H.; Mangas-Sanchez, J.; Montgomery, S.L.; Sharma, M.; Leipold, F.; Hussain, S.; Grogan, G.; Turner,
N.J. A reductive aminase from Aspergillus oryzae. Nat. Chem. 2017, 9, 961–969. [CrossRef]
Thorpe, T.W.; Marshall, J.R.; Harawa, V.; Ruscoe, R.E.; Cuetos, A.; Finnigan, J.D.; Angelastro, A.; Heath, R.S.; Parmeggiani,
F.; Charnock, S.J.; et al. Multifunctional biocatalyst for conjugate reduction and reductive amination. Nature 2022, 604, 86–91.
[CrossRef]
Marshall, J.R.; Yao, P.; Montgomery, S.L.; Finnigan, J.D.; Thorpe, T.W.; Palmer, R.B.; Mangas-Sanchez, J.; Duncan, R.A.M.; Heath,
R.S.; Graham, K.M.; et al. Screening and characterization of a diverse panel of metagenomic imine reductases for biocatalytic
reductive amination. Nat. Chem. 2021, 13, 140–148. [CrossRef]
Wu, K.; Huang, J.; Shao, L. Imine Reductases: Multifunctional Biocatalysts with Varying Active Sites and Catalytic Mechanisms.
ChemCatChem 2022, 14, e202200921. [CrossRef]
Ishak, S.N.H.; Saad, A.H.M.; Latip, W.; Rahman, R.N.Z.R.A.; Salleh, A.B.; Kamarudin, N.H.A.; Leow, A.T.C.; Ali, M.S.M.
Enhancing industrial biocatalyst performance and cost-efficiency through adsorption-based enzyme immobilization: A review.
Int. J. Biol. Macromol. 2025, 316, 144278. [CrossRef]
Zhao, Z.; Zhou, M.-C.; Liu, R.-L. Recent Developments in Carriers and Non-Aqueous Solvents for Enzyme Immobilization.
Catalysts 2019, 9, 647. [CrossRef]
France, S.P.; Lewis, R.D.; Martinez, C.A. The Evolving Nature of Biocatalysis in Pharmaceutical Research and Development. JACS
Au 2023, 3, 715–735. [CrossRef]
Singh, R.K.; Tiwari, M.K.; Singh, R.; Lee, J.-K. From Protein Engineering to Immobilization: Promising Strategies for the Upgrade
of Industrial Enzymes. Int. J. Mol. Sci. 2013, 14, 1232–1277. [CrossRef]
Nguyen, H.H.; Kim, M. An Overview of Techniques in Enzyme Immobilization. Appl. Sci. Converg. Technol. 2017, 26, 157–163.
[CrossRef]
Grace, M. Enzyme Immobilization: Its Advantages, Applications and Challenges. Enz. Eng. 2024, 13, 248.
Schober, M.; MacDermaid, C.; Ollis, A.A.; Chang, S.; Khan, D.; Hosford, J.; Latham, J.; Ihnken, L.A.F.; Brown, M.J.B.; Fuerst,
D.; et al. Chiral synthesis of LSD1 inhibitor GSK2879552 enabled by directed evolution of an imine reductase. Nat. Catal. 2019,
2, 909–915. [CrossRef]
Xu, Z.; Yao, P.; Sheng, X.; Li, J.; Li, J.; Yu, S.; Feng, J.; Wu, Q.; Zhu, D. Biocatalytic Access to 1,4-Diazepanes via Imine ReductaseCatalyzed Intramolecular Asymmetric Reductive Amination. ACS Catal. 2020, 10, 8780–8787. [CrossRef]

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

34.
35.

36.
37.

38.
39.
40.

41.
42.
43.
44.

45.
46.
47.
48.
49.
50.
51.
52.
53.
54.
55.

56.
57.

29 of 30

Ma, E.J.; Siirola, E.; Moore, C.; Kummer, A.; Stoeckli, M.; Faller, M.; Bouquet, C.; Eggimann, F.; Ligibel, M.; Huynh, D.; et al.
Machine-Directed Evolution of an Imine Reductase for Activity and Stereoselectivity. ACS Catal. 2021, 11, 12433–12445. [CrossRef]
Kumar, R.; Karmilowicz, M.J.; Burke, D.; Burns, M.P.; Clark, L.A.; Connor, C.G.; Cordi, E.; Do, N.M.; Doyle, K.M.; Hoagland, S.;
et al. Biocatalytic reductive amination from discovery to commercial manufacturing applied to abrocitinib JAK1 inhibitor. Nat.
Catal. 2021, 4, 775–782. [CrossRef]
Chen, Q.; Li, B.-B.; Zhang, L.; Chen, X.-R.; Zhu, X.-X.; Chen, F.-F.; Shi, M.; Chen, C.-C.; Yang, Y.; Guo, R.-T.; et al. Engineered Imine
Reductase for Larotrectinib Intermediate Manufacture. ACS Catal. 2022, 12, 14795–14803. [CrossRef]
Chen, F.-F.; He, X.-F.; Zhu, X.-X.; Zhang, Z.; Shen, X.-Y.; Chen, Q.; Xu, J.-H.; Turner, N.J.; Zheng, G.-W. Discovery of an Imine
Reductase for Reductive Amination of Carbonyl Compounds with Sterically Challenging Amines. J. Am. Chem. Soc. 2023,
145, 4015–4025. [CrossRef]
Liu, T.; Xu, Z.; Feng, J.; Yu, S.; Wang, M.; Yao, P.; Wu, Q.; Zhu, D. Enantiodivergent Synthesis of 1-Heteroaryl Tetrahydroisoquinolines Catalyzed by Imine Reductases. Org. Lett. 2023, 25, 2438–2443. [CrossRef]
Steflik, J.; Gilio, A.; Burns, M.; Grogan, G.; Kumar, R.; Lewis, R.; Martinez, C. Engineering of a Reductive Aminase to Enable the
Synthesis of a Key Intermediate to a CDK 2/4/6 Inhibitor. ACS Catal. 2023, 13, 10065–10075. [CrossRef]
Zhu, Z.-Y.; Shi, M.; Li, C.-L.; Gao, Y.-F.; Shen, X.-Y.; Ding, X.-W.; Chen, F.-F.; Xu, J.-H.; Chen, Q.; Zheng, G.-W. An Engineered
Imine Reductase for Highly Diastereo- and Enantioselective Synthesis of β-Branched Amines with Contiguous Stereocenters.
Angew. Chem. Int. Ed. 2024, 63, e202408686. [CrossRef]
Lin, X.; Li, Y.; Xu, Z.; Yu, S.; Feng, J.; Diao, A.; Yao, P.; Wu, Q.; Zhu, D. Engineered Imine Reductase for Asymmetric Synthesis of
Dextromethorphan Key Intermediate. Org. Lett. 2024, 26, 4463–4468. [CrossRef]
Li, J.; Xu, Z.; Feng, J.; Mao, S.; Yao, P.; Wu, Q.; Zhu, D. Asymmetric Synthesis of N-Hydroxyethyl Amino Indane Derivatives
Catalyzed by an Engineered Imine Reductase. Org. Lett. 2025, 27, 4063–4067. [CrossRef]
Du, Z.; Li, H.; Kuang, X.; Zhang, L.; Li, S. Semi-rational design and modification of imine reductases and their utilization for the
synthesis of (S)-nornicotine. Bioorganic Chem. 2025, 163, 108705. [CrossRef]
Casamajo, A.R.; Yu, Y.; Schnepel, C.; Morrill, C.; Barker, R.; Levy, C.W.; Finnigan, J.; Spelling, V.; Westerlund, K.; Petchey, M.;
et al. Biocatalysis in Drug Design: Engineered Reductive Aminases (RedAms) Are Used to Access Chiral Building Blocks with
Multiple Stereocenters. J. Am. Chem. Soc. 2023, 145, 22041–22046. [CrossRef]
Burke, A.J.; Lister, T.M.; Marshall, J.R.; Brown, M.J.B.; Lloyd, R.; Green, A.P.; Turner, N.J. Engineered Biocatalysts for Enantioselective Reductive Aminations of Cyclic Secondary Amines. ChemCatChem 2023, 15, e202300256. [CrossRef]
Tang, D.; Ma, Y.; Bao, J.; Gao, S.; Man, S.; Cui, C. Chemoenzymatic total synthesis of rotigotine via IRED-catalyzed reductive
amination. Org. Biomol. Chem. 2024, 22, 3843–3847. [CrossRef]
Zhu, M.; Lin, Q.; Zhong, M.; Dong, J.; Zhao, L.; Wu, Q.; Ren, H.; Du, W.; Li, J. Rational engineering of an imine reductase unlocks
stereochemical gatekeeping for efficient synthesis of Evocalcet chiral intermediate. Mol. Catal. 2025, 586, 115415. [CrossRef]
Hu, Y.; Bao, J.; Tang, D.; Gao, S.; Wang, F.; Ding, Z.; Cui, C. Chemoenzymatic Synthesis of Selegiline: An Imine ReductaseCatalyzed Approach. Molecules 2024, 29, 1328. [CrossRef]
Zhang, J.; Ma, Y.; Zhu, F.; Bao, J.; Wu, Q.; Gao, S.-S.; Cui, C. Structure-guided semi-rational design of an imine reductase for
enantio-complementary synthesis of pyrrolidinamine. Chem. Sci. 2023, 14, 4265–4272. [CrossRef]
Zhu, F.; Zhang, J.; Ma, Y.; Yang, L.; Gao, Q.; Gao, S.; Cui, C. Semi-rational design of an imine reductase for asymmetric synthesis
of alkylated S-4-azepanamines. Org. Biomol. Chem. 2023, 21, 4181–4184. [CrossRef]
Ma, Y.; Gao, S.-S.; Li, X.; Wu, J.; Bao, J.; Wang, L.; Cui, C. Engineered Imine Reductase Catalyzed Enantiodivergent Synthesis of
Alkylated Amphetamines. Org. Lett. 2024, 26, 7565–7570. [CrossRef]
Hao, X.; Tian, Z.; Yao, Z.; Zang, T.; Song, S.; Lin, L.; Qiao, T.; Huang, L.; Fu, H. Atroposelective Synthesis of Axial Biaryls by
Dynamic Kinetic Resolution Using Engineered Imine Reductases. Angew. Chem. Int. Ed. 2024, 63, e202410112. [CrossRef]
Lin, Q.; Lv, X.; Zeng, X.; Zhong, M.; Wu, Q.; Ren, H.; Xu, S.; Chen, W.; Du, W.; Li, J. Rational design of imine reductase for
asymmetric synthesis of α-methyl-benzylaminonitrogen heterocycles. Mol. Catal. 2024, 552, 113678. [CrossRef]
Huang, A.; Zhang, X.; Yang, Y.; Shi, C.; Zhang, B.; Tuo, X.; Shen, P.; Jiao, X.; Zhang, N. Biocatalytic Synthesis of Ruxolitinib
Intermediate via Engineered Imine Reductase. J. Org. Chem. 2024, 89, 11446–11454. [CrossRef]
Juhász Pótáriné, Z.; Paál, T.; Mészáros, L.; Bánóczi, G.; Kondor, Z.; Kavalecz, N.; Ujvárosi, A.Z.; Végh, J.; Eszenyi, D.; Zahuczky,
G.J.; et al. Imine Reductase-Catalyzed Synthesis of a Key Intermediate of Avacopan: Enzymatic Oxidative Kinetic Resolution
with Ex Situ Recovery and Dynamic Kinetic Reduction Strategies toward 2,3-Disubstituted Piperidine. Org. Process Res. Dev.
2025, 29, 1093–1102. [CrossRef]
Zhang, Z.-H.; Wang, A.-Q.; Ma, B.-D.; Xu, Y. Rational Engineering of Mesorhizobium Imine Reductase for Improved Synthesis of
N-Benzyl Cyclo-tertiary Amines. Catalysts 2024, 14, 23. [CrossRef]
Zheng, X.; Dou, Z.; Xiang, W.; Zhang, W.; Ni, Y.; Xu, G. Engineering the enantioselectivity of a novel imine reductase from
Streptomyces viridochromogenes for the dynamic kinetic reductive amination of cyclic β-ketoester. Mol. Catal. 2024, 559, 114039.
[CrossRef]

https://doi.org/10.3390/chemistry8040040

Chemistry 2026, 8, 40

58.
59.
60.
61.
62.
63.

30 of 30

Fukawa, Y.; Yoshida, K.; Degura, S.; Mitsukura, K.; Yoshida, T. Improvement of (S)-selective imine reductase GF3546 for the
synthesis of chiral cyclic amines. Chem. Commun. 2022, 58, 13222–13225. [CrossRef]
Stockinger, P.; Borlinghaus, N.; Sharma, M.; Aberle, B.; Grogan, G.; Pleiss, J.; Nestl, B.M. Inverting the Stereoselectivity of an
NADH-Dependent Imine-Reductase Variant. ChemCatChem 2021, 13, 5210–5215. [CrossRef] [PubMed]
Benítez-Mateos, A.I.; Lim, D.; Roura Padrosa, D.; Marchini, V.; Wu, H.; Buono, F.; Paradisi, F. Biocatalytic Reduction of Heterocyclic
Imines in Continuous Flow with Immobilized Enzymes. ACS Sustain. Chem. Eng. 2025, 13, 5009–5018. [CrossRef]
Guan, S.; Zhou, W.; Yue, Y.; Wang, S.; Chen, B.; Yang, H. Efficient Synthesis of (S)-Nornicotine using Co-Immobilized IRED and
GDH in Batch and Continuous Flow Reaction Systems. Org. Process Res. Dev. 2024, 28, 2050–2060. [CrossRef]
Gand, M.; Thöle, C.; Müller, H.; Brundiek, H.; Bashiri, G.; Höhne, M. A NADH-accepting imine reductase variant: Immobilization
and cofactor regeneration by oxidative deamination. J. Biotechnol. 2016, 230, 11–18. [CrossRef] [PubMed]
Ren, M.; Zhang, L.; Song, J.; Chen, W.; Zhang, L.; Liao, D.; Gao, S.-S.; An, H.; Xie, B.; Luo, D.-Q.; et al. Engineering and
immobilization of imine reductase enable chemoenzymatic synthesis of SLC6A19 inhibitor JNT-517. Bioresour. Technol. 2026,
440, 133403. [CrossRef] [PubMed]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

https://doi.org/10.3390/chemistry8040040
