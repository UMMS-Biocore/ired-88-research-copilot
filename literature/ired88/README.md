# IRED-88 literature

Full text of open-access papers that discuss the Novartis imine reductase
IRED-88 (also written IRED88), the enzyme behind PDB 7OG3 and the ZPL389
reductive amination. These files are for a coding agent reading while it
drives a marimo notebook. They are not the short notes in `kb/papers/`,
and notebook 03 does not load them.

Searches: PubMed, Europe PMC (phrase queries for `IRED-88`, `IRED88`,
`7OG3`, `ZPL389`, `Q194L`, `S220T`, and `machine-directed evolution`),
and OpenAlex (works matching those phrases, plus the 111 papers that cite
Ma et al. 2021, DOI 10.1021/acscatal.1c02786). Almost every citation of
Ma et al. is a general machine-learning or biocatalysis review that does
not add facts about this enzyme. Those were not copied in.

Each file begins with a short repo note, then the article. Cite the paper,
not this folder.

## Full text included

All six are CC BY 4.0.

| File | What it adds about IRED-88 |
|------|----------------------------|
| [gilio-2022-chem-sci-reductive-aminations.md](gilio-2022-chem-sci-reductive-aminations.md) | Dedicated ZPL389 case: mining, S220T, Q194L/S220T/H230Y, PDB 7OG3, and the ML variants. DOI [10.1039/d2sc00124a](https://doi.org/10.1039/d2sc00124a). |
| [kalicanin-2026-mdpi-ired-engineering.md](kalicanin-2026-mdpi-ired-engineering.md) | Longest secondary retelling, including IRED-22, IRED-13, and IRED-88-2, plus the plate, DMS, and gram-scale conditions. DOI [10.3390/chemistry8040040](https://doi.org/10.3390/chemistry8040040). |
| [braun-2023-acs-catalysis-ml-biocatalysis.md](braun-2023-acs-catalysis-ml-biocatalysis.md) | Walks through the machine-directed evolution workflow on ZPL389 as a worked example. DOI [10.1021/acscatal.3c03417](https://doi.org/10.1021/acscatal.3c03417). |
| [siirola-2023-chimia-novartis-biocatalysis.md](siirola-2023-chimia-novartis-biocatalysis.md) | The Novartis group on the 2017 genome-mined IRED library (~15,000 sequences) and the machine-directed evolution platform. ZPL389 is on the timeline; the mutant table is not restated. DOI [10.2533/chimia.2023.376](https://doi.org/10.2533/chimia.2023.376). |
| [sangster-2021-cbic-enzymatic-bond-formation.md](sangster-2021-cbic-enzymatic-bond-formation.md) | One paragraph citing the ZPL389 comparison of machine learning, deep mutational scanning, and error-prone PCR. DOI [10.1002/cbic.202100464](https://doi.org/10.1002/cbic.202100464). |
| [xing-2025-jacs-au-redam-detect.md](xing-2025-jacs-au-redam-detect.md) | One structural comparison: IRED-88 Asn178 at the BacRedAm D188-equivalent position. DOI [10.1021/jacsau.5c00512](https://doi.org/10.1021/jacsau.5c00512). |

The two MDPI and CHIMIA files are the publisher PDF text layer, so line
breaks follow the PDF. The other four are Europe PMC JATS converted to
markdown. PubMed Central identifiers are in those files' frontmatter.

## Not copied

| Paper | Why it is not in this folder |
|-------|------------------------------|
| Ma, Siirola, Moore, et al. *ACS Catalysis* 2021, 11, 12433–12445. DOI [10.1021/acscatal.1c02786](https://doi.org/10.1021/acscatal.1c02786). | The primary paper. Closed access, and OpenAlex reports no repository copy. Do not paste it in. The curated note is `kb/papers/ma-2021-machine-directed-evolution.md`. The DMS and ee tables are already in `data/raw/`. The public abstract states full conversion, >99% ee (R), and 72% yield for the gram-scale ZPL389 synthesis. |
| France et al. *JACS Au* 2023. DOI [10.1021/jacsau.2c00712](https://doi.org/10.1021/jacsau.2c00712). PMC10052283. | Mentions the ZPL389 campaign. Europe PMC records the license as CC BY-NC-ND, which does not allow this redistribution. |
| The other ~100 papers that cite Ma et al. 2021 | They cite the method. They do not describe IRED-88. |

## Read this before quoting a number

There is one primary experimental paper (Ma et al. 2021). Everything else
here is a review retelling it, and the retellings do not agree:

- Gilio et al. 2022: gram-scale Q194L/S220T/H230Y gives 72% yield and >99% ee.
- Kaličanin et al. 2026: the same scale-up is full conversion, 98% ee (R),
  and 72% yield as the tartrate salt.
- The Ma et al. 2021 abstract, which is the primary source, says full
  conversion, >99% ee (R), and 72% yield.

Kaličanin et al. also name earlier panel members that the shorter reviews
skip: (R)-selective IRED-22 (12% conversion, 97% ee), (S)-selective IRED-13
(77% conversion, >99% ee), and IRED-88-2 (83% conversion, >99% ee (R)).
They say IRED-88 (70% conversion, 30% ee (R)) was kept as the evolution
starting point because both activity and enantioselectivity still needed
work. Treat those panel members as claims from that review until they can
be checked against Ma et al. 2021.
