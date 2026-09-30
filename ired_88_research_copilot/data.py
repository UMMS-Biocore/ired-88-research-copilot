"""Data loading utilities for the IRED-88 research copilot.

All tabular data come from the supporting information of:

    Ma, E. J.; Siirola, E.; Moore, C.; et al. "Machine-Directed Evolution of an
    Imine Reductase for Activity and Stereoselectivity." ACS Catal. 2021, 11
    (20), 12433-12445. DOI: 10.1021/acscatal.1c02786

The CSVs live in ``data/raw/`` and are used only for workshop/demo purposes;
cite the paper for any external use of the raw tables.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

import pandas as pd
from pyprojroot import here

RAW_DATA_DIR: Path = here() / "data" / "raw"
EXTERNAL_DATA_DIR: Path = here() / "data" / "external"

#: A singlemutation notation, e.g. ``A111C`` (wild-type residue, position,
#: mutant residue) or ``A111*`` (nonsense mutation).
MUTATION_PATTERN = re.compile(r"^([A-Z])(\d+)([A-Z*])$")

SI002_FILENAME = "cs1c02786_si_002.csv"
SI003_FILENAME = "cs1c02786_si_003.csv"
WT_FASTA_FILENAME = "ired88_wt.fasta"


def load_si002() -> pd.DataFrame:
    """Load per-mutation activity summaries (paper SI table 2).

    :returns: DataFrame with columns ``mutation``, ``mean``, ``alpha``,
        ``date``, ``hash``, ``ratio``, ``count``, ``beta``. ``mean`` is the
        batch-adjusted mean activity; ``count`` is the number of measurements.
    """
    return pd.read_csv(RAW_DATA_DIR / SI002_FILENAME, index_col=0)


def load_si003() -> pd.DataFrame:
    """Load enantioselectivity (R enantiomeric excess) measurements.

    :returns: DataFrame with columns ``mutation``, ``r_enantiomeric_excess``,
        ``ratio`` (fractional conversion), and ``experiment`` (one of DMS,
        EPPCR1-3, ML, SGM, LowN, FragLib).
    """
    return pd.read_csv(RAW_DATA_DIR / SI003_FILENAME, index_col=0)


def load_wildtype_sequence() -> str:
    """Return the 304-residue wild-type IRED-88 protein sequence.

    The sequence is read from ``data/external/ired88_wt.fasta``, written by
    ``scripts/fetch_data.py`` from the sequence published in the paper's
    supporting information. It is numbered 1-304 without the N-terminal
    expression tag used for crystallization.

    :returns: One-letter protein sequence of wild-type IRED-88.
    """
    lines = (EXTERNAL_DATA_DIR / WT_FASTA_FILENAME).read_text().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def extract_single_mutants(activities: pd.DataFrame) -> pd.DataFrame:
    """Filter a activities table down to strict single mutants.

    :param activities: A table with a ``mutation`` column, e.g. from
        :func:`load_si002`.
    :returns: Copy of the input containing only rows whose ``mutation``
        matches ``A111C``-style notation, plus parsed ``wt_aa``, ``pos``,
        and ``mut_aa`` columns.
    """
    is_single = activities["mutation"].str.match(MUTATION_PATTERN, na=False)
    singles = activities[is_single].copy()
    parsed = singles["mutation"].str.extract(MUTATION_PATTERN)
    singles["wt_aa"] = parsed[0]
    singles["pos"] = parsed[1].astype(int)
    singles["mut_aa"] = parsed[2]
    return singles


def summarize_by_position(singles: pd.DataFrame) -> pd.DataFrame:
    """Aggregate single-mutant measurements to one row per sequence position.

    :param singles: Single-mutant table from :func:`extract_single_mutants`.
    :returns: DataFrame indexed by ``pos`` with the mean activity per position
        (column ``mean_activity``) and the number of mutants measured
        (column ``n_mutants``).
    """
    return singles.groupby("pos").agg(
        mean_activity=("mean", "mean"), n_mutants=("mutation", "count")
    )


def mask_positions(singles: pd.DataFrame, positions: Iterable[int]) -> pd.DataFrame:
    """Simulate a library gap by dropping all measurements at some positions.

    :param singles: Single-mutant table from :func:`extract_single_mutants`.
    :param positions: Positions to mask (1-based, matching the ``pos``
        column).
    :returns: Copy of the input with every row whose ``pos`` is in
        ``positions`` removed.
    """
    return singles[~singles["pos"].isin(set(positions))].copy()


def split_combination(mutation: str) -> list[str]:
    """Split a combination mutation string into its component mutations.

    :param mutation: Mutation string such as ``"Q194L; S220T; H230Y"``.
    :returns: Component mutation tokens, e.g. ``["Q194L", "S220T",
        "H230Y"]``. A plain single mutation returns a one-element list.
    """
    return [token.strip() for token in mutation.split(";") if token.strip()]
