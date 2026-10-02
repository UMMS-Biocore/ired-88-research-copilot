import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import marimo as mo
    import numpy as np
    import pandas as pd

    from ired_88_research_copilot import data, kb, structure, theme

    theme.apply()

    return alt, data, kb, mo, np, pd, structure, theme


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(f"""
    <div style="background:linear-gradient(135deg, {theme.PRIMARY} 0%, #134e4a 100%);
                border-radius:16px; padding:28px 32px; color:white;">
    <div style="font-size:13px; letter-spacing:2px; opacity:0.85;
                text-transform:uppercase;">AI as a Research Co-Pilot · Live demo</div>
    <h1 style="margin:10px 0 6px 0; font-size:34px; line-height:1.15;">
    The IRED-88 Research Copilot</h1>
    <div style="font-size:15px; opacity:0.92;">
    One enzyme, four data modalities, one question ladder -- in a single repo.</div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An enzyme-engineering campaign produced a deep mutational scan, an
    enantioselectivity table, a 1.9 A crystal structure, and a set of
    engineered variants. Around it sits a small **knowledge base** of six
    papers. This demo runs the round-trip between all four modalities --
    and asks one question on the way:

    > #### Where do activity-improving mutations of the enzyme IRED-88 come from -- and could we have seen them coming?
    """)
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(f"""
    <span style="background:{theme.PRIMARY};color:white;padding:3px 12px;
    border-radius:12px;font-size:12px;font-weight:600">Q1 / 6 · THE DATA</span>

    # Which single mutations improve IRED-88?

    The deep mutational scan measured nearly all ~6,000 possible single
    mutants of the 304-residue enzyme. `mean` is the batch-adjusted
    activity (paper SI-002); `count` is how many times that mutant was
    measured across plates.
    """)
    return


@app.cell
def _(data, structure):
    singles = data.extract_single_mutants(data.load_si002())
    _si002 = data.load_si002()
    wt_mean = float(_si002[_si002["mutation"].isna()]["mean"].iloc[0])
    wt_n = int(_si002[_si002["mutation"].isna()]["count"].iloc[0])
    median_mean = float(singles["mean"].median())
    best = singles.nlargest(1, "mean").iloc[0]
    _crystal = structure.load_crystal_structure()
    distances = {
        resnum: structure.min_ligand_distance(_crystal, resnum)
        for resnum in _crystal.observed_resnums
    }
    return best, distances, median_mean, singles, wt_mean, wt_n


@app.cell
def _(best, median_mean, mo, wt_mean, wt_n):
    stat_row = mo.hstack(
        [
            mo.stat(
                value=f"{wt_mean:.3f}",
                label="wild type",
                caption=f"reference row, n={wt_n:,}",
            ),
            mo.stat(
                value=f"{median_mean:.3f}", label="median mutant", caption="most hurt"
            ),
            mo.stat(
                value=f"{best['mean']:.3f}",
                label=f"best mutant ({best['mutation']})",
                caption="21x the median",
            ),
        ],
        justify="space-between",
    )
    stat_row
    return


@app.cell(hide_code=True)
def _(alt, mo, singles):
    heatmap = (
        alt.Chart(
            singles,
            title="The deep mutational scan: activity of every measured single mutant",
        )
        .mark_rect()
        .encode(
            x=alt.X("pos:O", title="Sequence position").axis(labels=False, ticks=False),
            y=alt.Y("mut_aa:O", title="Mutant residue", sort="descending"),
            color=alt.Color(
                "mean:Q",
                title="Activity",
                scale=alt.Scale(scheme="viridis"),
                legend=alt.Legend(orient="left"),
            ),
            tooltip=[alt.Tooltip("mutation", title="Mutant"), "mean", "count"],
        )
        .properties(width=860, height=340)
    )
    mo.vstack([heatmap])
    return


@app.cell(hide_code=True)
def _(alt, singles, theme, wt_mean):
    _top15 = singles.nlargest(15, "mean")
    top_chart = (
        alt.Chart(
            _top15, title=f"Top 15 single mutants -- wild type sits at {wt_mean:.3f}"
        )
        .mark_bar()
        .encode(
            x=alt.X("mutation:N", sort="-y", title=None),
            y=alt.Y("mean:Q", title="Activity"),
            color=alt.condition(
                "datum.mean > 0.6", alt.value(theme.PRIMARY), alt.value("#9fb8c8")
            ),
            tooltip=["mutation", "mean", "count"],
        )
        .properties(width=720, height=260)
    )
    top_chart
    return


@app.cell(hide_code=True)
def _(alt, mo, pd, singles, theme):
    _by_position = (
        singles.groupby("pos")
        .agg(mean_activity=("mean", "mean"), n=("mutation", "count"))
        .reset_index()
    )
    boundary_df = pd.DataFrame(
        {
            "pos": [12, 301],
            "label": ["first residue in crystal", "last residue in crystal"],
        }
    )
    position_chart = (
        alt.Chart(
            _by_position,
            title="Per-position mean activity -- note the peaks at both ends",
        )
        .mark_line(point=True, color=theme.PRIMARY)
        .encode(
            x=alt.X("pos:Q", title="Sequence position"),
            y=alt.Y("mean_activity:Q", title="Mean activity at position"),
            tooltip=["pos", "mean_activity", "n"],
        )
        .properties(width=860, height=240)
    )
    boundaries = (
        alt.Chart(boundary_df)
        .mark_rule(color=theme.MUTED, strokeDash=[5, 4])
        .encode(x="pos:Q", tooltip=["label:N"])
    )
    mo.vstack([position_chart + boundaries])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explore it yourself

    Drag through positions and watch the 19 possible mutations at each.
    Try position **220** -- the DMS's most-replicated lead -- and
    position **296**, buried in the tail the crystal cannot see.
    """)
    return


@app.cell
def _(mo):
    position_slider = mo.ui.slider(
        start=2, stop=304, value=220, label="Sequence position", show_value=True
    )
    position_slider
    return (position_slider,)


@app.cell(hide_code=True)
def _(alt, distances, mo, position_slider, singles, structure):
    pos_selected = position_slider.value
    at_position = singles[singles["pos"] == pos_selected].sort_values("mut_aa")
    explorer_chart = (
        alt.Chart(
            at_position,
            title=f"Position {pos_selected}: activity of each mutant residue",
        )
        .mark_bar()
        .encode(
            x=alt.X("mut_aa:N", title="Mutant residue", sort=None),
            y=alt.Y("mean:Q", title="Activity", scale=alt.Scale(domain=[0, 0.8])),
            color=alt.Color(
                "mean:Q",
                scale=alt.Scale(scheme="viridis"),
                legend=None,
            ),
            tooltip=["mutation", "mean", "count"],
        )
        .properties(width=640, height=240)
    )
    explorer_note = mo.callout(
        mo.md(
            f"""
            Position {pos_selected} is
            **{structure.site_class(distances.get(pos_selected))}** in the
            crystal structure. Best mutation here:
            **{at_position.nlargest(1, "mean")["mutation"].iloc[0]}**
            (mean {at_position["mean"].max():.3f}).
            """
        ),
        kind="neutral",
    )
    mo.vstack([explorer_note, explorer_chart])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            r"""
            ### Answer -- Q1

            - The two strongest single mutants are **A296I** (mean 0.712,
              measured 7 times) and **S220T** (mean 0.678, measured **685**
              times -- re-measured heavily as the lead hit). Both
              beat the median mutant by >20x.
            - Beneficial positions are **scattered across the whole
              sequence**: near the N-terminus (6, 26, 57), mid-sequence
              (154-177, 212, 218-220, 243-247), and at the very C-terminal
              end (296, 302-304).
            - Positions **302-304** -- the last three residues -- average
              0.126 / 0.177 / 0.170 against a 0.031 median. Remember them:
              Q2 shows what the crystal structure cannot see there.
            """
        ),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(
        f"""
        <span style="background:{theme.DISTAL};color:white;padding:3px 12px;
        border-radius:12px;font-size:12px;font-weight:600">Q2 / 6 · THE STRUCTURE</span>

        # Are the hits where the structure says they should be?

        A structure turns a list of positions into *mechanism*. We have the
        IRED-88 crystal structure (PDB **7OG3**, 1.9 A, NADP cofactor bound).
        The question for enzyme engineering: do the activity-improving
        mutations cluster at the active site, near it, or far away?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **A numbering detail that matters here:** 7OG3's ATOM records are
        numbered by the wild-type protein sequence, so PDB residue number =
        DMS position. The crystal resolves positions **12-301**; positions
        **1-11** and **302-304** are disordered and have no coordinates.
        Every distance below is measured in the protein's coordinate frame
        to the bound NADP cofactor.
        """
    )
    return


@app.cell
def _(data, structure):
    _crystal = structure.load_crystal_structure()
    ligand_distances = {
        resnum: structure.min_ligand_distance(_crystal, resnum)
        for resnum in _crystal.observed_resnums
    }
    singles_q2 = data.extract_single_mutants(data.load_si002())
    by_position = (
        singles_q2.groupby("pos").agg(mean_activity=("mean", "mean")).reset_index()
    )
    by_position["site_class"] = by_position["pos"].map(
        lambda p: structure.site_class(ligand_distances.get(p))
    )
    return by_position, ligand_distances, singles_q2


@app.cell(hide_code=True)
def _(alt, by_position, mo, theme):
    class_colors = [
        theme.ACTIVE_SITE,
        theme.SECOND_SHELL,
        theme.DISTAL,
        theme.UNRESOLVED,
    ]
    class_chart = (
        alt.Chart(
            by_position,
            title="Per-position mean activity, colored by distance to the NADP cofactor",
        )
        .mark_bar(size=3)
        .encode(
            x=alt.X("pos:Q", title="Sequence position"),
            y=alt.Y("mean_activity:Q", title="Mean activity at position"),
            color=alt.Color(
                "site_class:N",
                sort=theme.SITE_CLASS_ORDER,
                scale=alt.Scale(domain=theme.SITE_CLASS_ORDER, range=class_colors),
                title="Site class",
            ),
            tooltip=["pos", "mean_activity", "site_class"],
        )
        .properties(width=860, height=280)
    )
    legend_note = mo.md(
        r"""
        <span style="color:{red};font-weight:600">red</span> = active site
        (&lt; 6 A) · <span style="color:{amber};font-weight:600">amber</span> =
        second shell (6-12 A) ·
        <span style="color:{blue};font-weight:600">blue</span> = distal
        (&gt; 12 A) · <span style="color:{grey};font-weight:600">grey</span> =
        no coordinates
        """.format(
            red=theme.ACTIVE_SITE,
            amber=theme.SECOND_SHELL,
            blue=theme.DISTAL,
            grey=theme.UNRESOLVED,
        )
    )
    mo.vstack([legend_note, class_chart])
    return (class_chart,)


@app.cell(hide_code=True)
def _(ligand_distances, mo, singles_q2, structure):
    _top15 = singles_q2.nlargest(15, "mean").copy()
    _top15["site class"] = _top15["pos"].map(
        lambda p: structure.site_class(ligand_distances.get(p))
    )
    _top15["in crystal"] = _top15["pos"].map(lambda p: p in ligand_distances)
    top_table = mo.ui.table(
        _top15[["mutation", "pos", "mean", "count", "site class", "in crystal"]],
        page_size=15,
        selection=None,
    )
    annotated_md = mo.md(r"""## The top 15, annotated""")
    mo.vstack([annotated_md, top_table])
    return (top_table,)


@app.cell(hide_code=True)
def _(alt, by_position, mo, pd, theme):
    top50 = set(by_position.nlargest(50, "mean_activity")["pos"])
    all_classes = by_position["site_class"].value_counts().rename("all positions")
    top_classes = (
        by_position[by_position["pos"].isin(top50)]["site_class"]
        .value_counts()
        .rename("top 50 positions")
    )
    class_df = pd.concat([all_classes, top_classes], axis=1).fillna(0).astype(int)
    class_long = class_df.reset_index().melt(
        "site_class", var_name="group", value_name="n"
    )
    enrichment_chart = (
        alt.Chart(
            class_long, title="Where the top-50 positions sit, against all positions"
        )
        .mark_bar()
        .encode(
            x=alt.X("group:N", title=None, sort=["all positions", "top 50 positions"]),
            y=alt.Y("n:Q", title="Number of positions"),
            color=alt.Color(
                "site_class:N",
                sort=theme.SITE_CLASS_ORDER,
                scale=alt.Scale(
                    domain=theme.SITE_CLASS_ORDER,
                    range=[
                        theme.ACTIVE_SITE,
                        theme.SECOND_SHELL,
                        theme.DISTAL,
                        theme.UNRESOLVED,
                    ],
                ),
                title="Site class",
            ),
            xOffset="site_class:N",
            tooltip=["group", "site_class", "n"],
        )
        .properties(width=520, height=300)
    )
    enrichment_md = mo.md(
        r"""
        ## The enrichment test

        If activity improvements came from active-site chemistry, the top-50
        positions should be red. They are not: **zero of the top 50** are
        active-site positions. The improvement signal lives in distal
        positions -- and in the grey band the crystal cannot see.
        """
    )
    mo.vstack([enrichment_md, enrichment_chart])
    return (enrichment_chart,)


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            r"""
            ### Answer -- Q2

            - **None of the top-50 positions are within 6 A of the NADP
              cofactor**; only 8 sit in the 6-12 A second shell. The rest are
              distal (32) or invisible to the crystal -- **10 of the 13
              unresolved positions land in the top 50**.
            - The famous lead **S220T** sits >12 A from the cofactor by atom
              distance, yet the literature calls it "the mouth of the active
              site cleft". Distance-to-cofactor is not distance-to-substrate:
              the *substrate* binds in a cleft whose entrance S220 guards.
            - The top hit **A296I** is resolved (position 296), but hot
              positions **302-304** have no coordinates at all.
            - Engineering implication: beneficial mutations act through
              **access, dynamics, and stability** -- not direct chemistry.
            """
        ),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(f"""
    <span style="background:{theme.KB};color:white;padding:3px 12px;
    border-radius:12px;font-size:12px;font-weight:600">Q3 / 6 · THE KNOWLEDGE BASE</span>

    # What does prior work already know about our top hits?

    `kb/papers/` holds one markdown note per paper: YAML frontmatter for
    structure, prose for claims. This is what makes the repo a *research
    copilot* rather than a folder of data -- analysis questions can be
    answered not just from numbers, but from what the literature already
    established, searched programmatically via
    `ired_88_research_copilot/kb.py`.
    """)
    return


@app.cell
def _(kb):
    notes = kb.load_all_notes()
    return (notes,)


@app.cell(hide_code=True)
def _(mo, notes, pd):
    notes_df = pd.DataFrame(
        [
            {
                "note": note.path.name,
                "year": note.year,
                "title": note.title[:72] + ("..." if len(note.title) > 72 else ""),
                "tags": ", ".join(note.tags[:4]),
            }
            for note in notes
        ]
    )
    notes_block = mo.vstack(
        [
            mo.md(r"""## The six notes in the KB"""),
            mo.ui.table(notes_df, page_size=6, selection=None),
        ]
    )
    notes_block
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ask the KB anything

    Edit the query below -- the search re-runs as you type. Terms are
    matched against every note's title, tags, and body; notes matching
    more distinct terms rank higher.
    """)
    return


@app.cell
def _(mo):
    kb_query = mo.ui.text(
        value="S220 active site mouth stereoselectivity",
        label="KB query",
        full_width=True,
    )
    kb_query
    return (kb_query,)


@app.cell(hide_code=True)
def _(kb, kb_query, mo, notes):
    def render_hit(note, score, query):
        """Render one KB hit as an accordion entry.

        :param note: The matched :class:`~ired_88_research_copilot.kb.KBNote`.
        :param score: Match score from ``kb.search_notes``.
        :param query: The query that produced the hit.
        :returns: An accordion element for this hit.
        """
        plural = "s" if score != 1 else ""
        body = mo.md(
            f"> {kb.snippet_for(note, query)}\n\n"
            f"Source file: `kb/papers/{note.path.name}`"
        )
        return mo.accordion(
            {f"**{note.citation}** (matched {score} term{plural})": body},
            lazy=True,
        )

    query_text = kb_query.value
    ranked_hits = kb.search_notes(notes, query_text)
    if ranked_hits:
        hit_blocks = [
            render_hit(note, score, query_text) for note, score in ranked_hits[:3]
        ]
    else:
        hit_blocks = [
            mo.callout(
                mo.md(
                    f"**No note matches `{query_text}`.** The KB's silence is a "
                    "result too: it means prior published work (as captured "
                    "here) has nothing to say about this query."
                ),
                kind="warn",
            )
        ]
    mo.vstack(
        [
            mo.md(
                f"### Results for `{query_text}` "
                f"({len(ranked_hits)} of {len(notes)} notes matched)"
            )
        ]
        + hit_blocks
    )
    return


@app.cell(hide_code=True)
def _(kb, mo, notes):
    a296_hits = kb.search_notes(notes, "A296I")
    mo.callout(
        mo.md(
            f"""
            A **{len(a296_hits)}-note silence**: querying the KB for
            **A296I** -- the strongest DMS hit -- returns nothing. No prior
            work (as captured here) has interpreted this mutation. That is a
            genuine open question, not a failure of the KB. The KB tells us
            what is *known*; what to do about the unknown is Q4's job
            (structure prediction) -- and ultimately the lab's. Try it in
            the query box above.
            """
        ),
        kind="neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            r"""
            ### Answer -- Q3

            - The KB explains the #2 DMS hit: **S220T** was independently
              interpreted as "at the mouth of the active site cleft",
              restricting access of the wrong substrate conformer and lifting
              ee from 30% to 96% (Gilio et al. 2022, reading Ma et al. 2021).
              Our distance-to-cofactor analysis called S220 "distal"; the KB
              corrects the *interpretation*, not the geometry.
            - The KB warns that **linear additivity holds outside the active
              site** but breaks down inside it -- a falsifiable claim that
              Q5 will test against the data.
            - It documents the engineered winner (**Q194L/S220T/H230Y**,
              99% ee) and the ML-guided alternative (M129L/A156S/Y177W).
            - The KB is **silent on A296I**. Prior work ends where this demo
              begins.
            """
        ),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(
        f"""
        <span style="background:{theme.SECOND_SHELL};color:white;padding:3px 12px;
        border-radius:12px;font-size:12px;font-weight:600">Q4 / 6 · THE PREDICTION</span>

        # What does structure prediction see that the crystal cannot?

        The crystal resolves positions 12-301. Q1 found beneficial mutations
        at positions 302-304 (and 1-11) -- which have **no experimental
        coordinates**. ESMFold predicted all 304 residues from sequence alone
        (`data/external/ired88_esmfold.pdb`, regenerable with
        `scripts/predict_structure_esmfold.py`).

        The rule for this notebook: **validate where truth exists first**;
        only then trust -- cautiously -- what prediction says where it
        doesn't.
        """
    )
    return


@app.cell
def _(np, pd, structure):
    crystal = structure.load_crystal_structure()
    predicted = structure.load_predicted_structure()
    global_rmsd = structure.ca_rmsd(predicted, crystal)
    _aligned, target, resnums = structure.superposed_ca(predicted, crystal)
    deviation = pd.Series(
        np.sqrt(((_aligned - target) ** 2).sum(axis=1)), index=resnums
    )
    n_shared = len(resnums)
    return crystal, deviation, global_rmsd, n_shared, predicted, resnums, target


@app.cell(hide_code=True)
def _(global_rmsd, mo, n_shared):
    validation_stats = mo.hstack(
        [
            mo.stat(
                value=f"{global_rmsd:.2f} A",
                label="global C-alpha RMSD",
                caption=f"over {n_shared} shared residues",
            ),
            mo.stat(
                value="same fold",
                label="verdict",
                caption="usable as hypothesis generator",
            ),
        ],
        justify="space-between",
    )
    mo.vstack(
        [
            mo.md(r"""## Step 1 -- validate where the crystal exists"""),
            validation_stats,
            mo.md(
                f"""
                Superposing the prediction onto the crystal gives a global
                C-alpha RMSD of **{global_rmsd:.2f} A** over the {n_shared}
                shared residues: the same fold, with local flexibility. Safe
                to use as a hypothesis generator.
                """
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(alt, mo, pd, deviation, resnums):
    distance_df = pd.DataFrame({"pos": resnums, "deviation": deviation})
    deviation_chart = (
        alt.Chart(
            distance_df,
            title="Per-residue C-alpha deviation: ESMFold prediction vs. crystal",
        )
        .mark_area(color="#3b6ea5", opacity=0.25)
        .encode(
            x=alt.X("pos:Q", title="Sequence position"),
            y=alt.Y("deviation:Q", title="C-alpha deviation (A)"),
        )
        .properties(width=860, height=200)
    )
    deviation_line = (
        alt.Chart(distance_df)
        .mark_line(color="#3b6ea5")
        .encode(x="pos:Q", y="deviation:Q")
    )
    deviation_md = mo.md(
        r"""
        The flexible **loop around 207-222 and 242-243** deviates most --
        exactly the neighborhood of the S220 lead and the 243 cluster from
        Q1. Hypothesis to carry forward: those positions tune a mobile
        region.
        """
    )
    mo.vstack(
        [
            deviation_chart + deviation_line,
            deviation_md,
        ]
    )
    return (deviation_chart,)


@app.cell
def _(np, structure):
    bfactor_by_position = structure.per_residue_bfactors(
        structure.load_predicted_structure()
    )
    plddt = {p: value * 100 for p, value in bfactor_by_position.items()}
    core_plddt = float(np.mean([plddt[p] for p in range(12, 302)]))
    nterm_plddt = float(np.mean([plddt[p] for p in range(1, 12)]))
    tail_plddt = [round(plddt[p]) for p in (302, 303, 304)]
    return core_plddt, nterm_plddt, plddt, tail_plddt


@app.cell
def _(core_plddt, mo, nterm_plddt, tail_plddt):
    confidence_stats = mo.hstack(
        [
            mo.stat(
                value=f"{core_plddt:.0f}",
                label="pLDDT, resolved region",
                caption="positions 12-301",
            ),
            mo.stat(
                value=f"{nterm_plddt:.0f}",
                label="pLDDT, invisible N-term",
                caption="positions 1-11",
            ),
            mo.stat(
                value=" / ".join(str(p) for p in tail_plddt),
                label="pLDDT, invisible C-tail",
                caption="positions 302-304",
            ),
        ],
        justify="space-between",
    )
    confidence_stats
    return (confidence_stats,)


@app.cell(hide_code=True)
def _(alt, mo, pd, plddt):
    plddt_df = pd.DataFrame({"pos": list(plddt), "plddt": list(plddt.values())})
    plddt_df["region"] = plddt_df["pos"].map(
        lambda p: (
            "resolved in crystal (12-301)" if 12 <= p <= 301 else "invisible to crystal"
        )
    )
    plddt_chart = (
        alt.Chart(plddt_df, title="ESMFold per-residue confidence (pLDDT)")
        .mark_line()
        .encode(
            x=alt.X("pos:Q", title="Sequence position"),
            y=alt.Y("plddt:Q", title="pLDDT", scale=alt.Scale(domain=[0, 100])),
            color=alt.Color("region:N", title=None),
            tooltip=["pos", "plddt"],
        )
        .properties(width=860, height=220)
    )
    plddt_md = mo.md(
        r"""
        The confidence dip over the C-tail is the model flagging its own
        uncertainty exactly where the crystallographers found no density.
        The N-terminus stays confident -- a reminder that
        disorder-in-crystal and low-prediction-confidence are not the same
        thing.
        """
    )
    mo.vstack([plddt_md, plddt_chart])
    return (plddt_chart,)


@app.cell(hide_code=True)
def _(crystal, mo, np, pd, plddt, predicted, structure):
    common = [
        r for r in predicted.observed_resnums if r in set(crystal.observed_resnums)
    ]
    ca_pred = np.array([structure._ca_coord(predicted, r) for r in common])
    ca_xtal = np.array([structure._ca_coord(crystal, r) for r in common])
    center_p, center_c = ca_pred.mean(axis=0), ca_xtal.mean(axis=0)
    rotation = structure.kabsch_transform(ca_pred - center_p, ca_xtal - center_c)
    ligand = crystal.ligand_coords
    tail_rows = []
    for _pos in (296, 302, 303, 304):
        ca = structure._ca_coord(predicted, _pos)
        moved = (ca - center_p) @ rotation + center_c
        tail_rows.append(
            {
                "position": _pos,
                "in crystal?": "yes" if _pos in crystal.residues else "no",
                "pLDDT": round(plddt[_pos]),
                "A to NADP (predicted, crystal frame)": f"{np.sqrt(((ligand - moved) ** 2).sum(axis=1)).min():.0f}",
            }
        )
    tail_df = pd.DataFrame(tail_rows)
    mo.vstack(
        [
            mo.md(
                r"""
                ## Step 2 -- only then, read the blind spots

                In the predicted model the last residues leave the fold and
                point **away from the active site**: superposed into the
                crystal frame, positions 302-304 sit ~28-30 A from NADP.
                A296I -- the top DMS hit -- is *inside* the resolved region,
                about 2.3 A from its crystal position.
                """
            ),
            tail_df,
        ]
    )
    return (tail_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            r"""
            ### Answer -- Q4

            - **Validation first:** the prediction reproduces the crystal
              fold at 2.36 A global RMSD -- safe to use as a hypothesis
              generator in unresolved regions.
            - The invisible C-tail (302-304) is predicted at **moderate
              confidence (71-82)** and **~28-30 A from the active site**,
              pointing out of the fold. The DMS says mutating it helps;
              prediction says it is not making direct active-site contact.
              Testable story: the tail modulates stability or solubility
              rather than chemistry.
            - The largest prediction-vs-crystal deviations sit in the
              **loop around 207-243** -- S220's neighborhood. Prediction and
              DMS agree that this region is *mobile and important*; neither
              can name the mechanism alone.
            - Structure prediction did not "solve" the question. It narrowed
              it and sharpened what to test next.
            """
        ),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(
        f"""
        <span style="background:{theme.SYNERGY};color:white;padding:3px 12px;
        border-radius:12px;font-size:12px;font-weight:600">Q5 / 6 · THE COMBINATIONS</span>

        # Doubles and triples: additive or epistatic?

        Q3's knowledge base made a falsifiable claim: linear additivity
        explains why combining mutations works **outside** the active site,
        while active-site mutations combine less predictably (Gilio et al.
        2022, reading the Ma et al. 2021 results). Q2 gave us the site
        classes to test exactly that. The combination data -- every
        engineered variant with its measured conversion -- live in SI-003.
        """
    )
    return


@app.cell
def _(data):
    si002 = data.load_si002()
    si003 = data.load_si003()
    singles_q5 = data.extract_single_mutants(si002)
    return si002, si003, singles_q5


@app.cell(hide_code=True)
def _(alt, mo, si003):
    strategy_chart = (
        alt.Chart(
            si003,
            title="Every engineered variant: conversion vs. R-enantiomeric excess, by strategy",
        )
        .mark_circle(size=70, opacity=0.8)
        .encode(
            x=alt.X(
                "ratio:Q",
                title="Fractional conversion",
                scale=alt.Scale(domain=[0, 1]),
            ),
            y=alt.Y(
                "r_enantiomeric_excess:Q",
                title="R-enantiomeric excess",
                scale=alt.Scale(domain=[0, 1]),
            ),
            color=alt.Color("experiment:N", title="Strategy"),
            tooltip=["mutation", "experiment", "ratio", "r_enantiomeric_excess"],
        )
        .properties(width=740, height=400)
    )
    mo.vstack([strategy_chart])
    return (strategy_chart,)


@app.cell(hide_code=True)
def _(data, mo, np, si002, si003, singles_q5):
    shared = si003[si003["mutation"].str.match(r"^[A-Z]\d+[A-Z*]$", na=False)].merge(
        singles_q5[["mutation", "mean"]], on="mutation", how="inner"
    )
    slope, intercept = np.polyfit(shared["mean"], shared["ratio"], 1)
    residuals = shared["ratio"] - (slope * shared["mean"] + intercept)
    _wt_mean = float(si002[si002["mutation"].isna()]["mean"].iloc[0])
    wt_ratio = float(slope * _wt_mean + intercept)
    single_lookup = singles_q5.set_index("mutation")["mean"].to_dict()
    calibration_md = mo.md(
        f"""
        ## One scale for everything

        Additivity needs singles and combos on the same scale. The two
        tables summarize the same assay differently: SI-002 `mean`
        (activity) vs. SI-003 `ratio` (fractional conversion). For the
        {len(shared)} single mutants present in both, they track tightly
        (r = {np.corrcoef(shared["mean"], shared["ratio"])[0, 1]:.3f},
        residual sd {residuals.std():.3f}), so a linear bridge is
        legitimate -- and it puts the wild type at conversion
        {wt_ratio:.3f}.
        """
    )
    mo.vstack([calibration_md])
    return intercept, shared, single_lookup, slope, wt_ratio


@app.cell(hide_code=True)
def _(data, mo, np, si003, single_lookup, slope, intercept, wt_ratio):
    def logit(p):
        p = np.clip(p, 0.01, 0.99)
        return np.log(p / (1 - p))

    combos = si003[si003["mutation"].str.contains(";", na=False)].copy()
    combos["components"] = combos["mutation"].apply(data.split_combination)
    combos["covered"] = combos["components"].apply(
        lambda tokens: all(t in single_lookup for t in tokens)
    )
    covered = combos[combos["covered"]].copy()

    def expected_logit(mutation):
        single_logits = [
            logit(slope * single_lookup[t] + intercept)
            for t in data.split_combination(mutation)
        ]
        return float(
            logit(wt_ratio) + sum(sl - logit(wt_ratio) for sl in single_logits)
        )

    covered["expected_ratio"] = covered["mutation"].apply(
        lambda m: float(1 / (1 + np.exp(-expected_logit(m))))
    )
    covered["epistasis"] = logit(covered["ratio"]) - covered["mutation"].apply(
        expected_logit
    )
    combos_md = mo.md(
        f"""
        ## The additivity model

        For each of the {len(combos)} combinations we sum the components'
        single-mutant effects -- in log-odds space, so expectations cannot
        silently saturate at 1.0:

        **expected = WT odds x (product of each mutation's odds ratio over WT)**

        then compare with measurement. {len(combos) - len(covered)}
        combinations drop out because a component was never cloned as a
        single (the library covered ~81% of sequence space), leaving
        **{len(covered)} testable combinations**.
        """
    )
    mo.vstack([combos_md])
    return covered, expected_logit, logit


@app.cell
def _(covered, mo):
    strategies = ["all"] + sorted(covered["experiment"].unique().tolist())
    strategy_filter = mo.ui.dropdown(
        options=strategies, value="all", label="Show one strategy"
    )
    strategy_filter
    return (strategy_filter,)


@app.cell(hide_code=True)
def _(alt, covered, mo, pd, strategy_filter):
    shown = (
        covered
        if strategy_filter.value == "all"
        else covered[covered["experiment"] == strategy_filter.value]
    )
    corr = shown[["expected_ratio", "ratio"]].corr().iloc[0, 1]
    diagonal_df = pd.DataFrame({"x": [0.0, 1.0]})
    evo_chart = (
        alt.Chart(shown, title="Additive expectation vs. measured conversion")
        .mark_circle(size=60, opacity=0.75)
        .encode(
            x=alt.X(
                "expected_ratio:Q",
                title="Additive expectation (conversion)",
                scale=alt.Scale(domain=[0, 1]),
            ),
            y=alt.Y(
                "ratio:Q",
                title="Measured conversion",
                scale=alt.Scale(domain=[0, 1]),
            ),
            color=alt.Color("experiment:N", title="Strategy"),
            tooltip=["mutation", "experiment", "expected_ratio", "ratio"],
        )
        .properties(width=600, height=430)
    )
    diagonal = (
        alt.Chart(diagonal_df)
        .mark_line(color="#555555", strokeDash=[5, 4])
        .encode(x="x:Q", y="x:Q")
    )
    evo_md = mo.md(
        f"""
        Points **below the diagonal** combine to less than the sum of their
        parts (antagonistic epistasis); **above it**, more (synergy).
        Correlation for the {len(shown)} shown combinations: {corr:.2f}.
        """
    )
    mo.vstack([evo_md, evo_chart + diagonal])
    return (evo_chart,)


@app.cell(hide_code=True)
def _(alt, covered, mo, theme):
    by_experiment = (
        covered.groupby("experiment")["epistasis"]
        .median()
        .rename("median_epistasis")
        .reset_index()
    )
    epi_chart = (
        alt.Chart(by_experiment, title="Median epistasis by strategy (log-odds)")
        .mark_bar()
        .encode(
            x=alt.X("experiment:N", sort="-y", title="Strategy"),
            y=alt.Y(
                "median_epistasis:Q",
                title="Median epistasis (observed - additive, log-odds)",
            ),
            color=alt.Color(
                "median_epistasis:Q",
                scale=alt.Scale(scheme="redblue", domain=[-2, 2]),
                legend=None,
            ),
            tooltip=["experiment", "median_epistasis"],
        )
        .properties(width=600, height=280)
    )
    epi_md = mo.md(
        r"""
        The split that actually shows up is **by strategy**, not by
        active-site composition (only 22 of the combinations even touch an
        active-site residue):

        - the **epPCR lineage** (rounds 2-3, stacked on the S220T backbone)
          is additive-to-synergistic -- its winners *beat* the additive
          expectation;
        - **ML-designed stacks** sit far below additive expectation. Caveat
          before over-reading: 35 of the 91 ML combinations have additive
          expectations above 90% conversion, and nothing in this campaign
          was ever measured above 87% -- the assay saturates, so part of
          that gap is ceiling, not biology.
        """
    )
    mo.vstack([epi_md, epi_chart])
    return (epi_chart,)


@app.cell(hide_code=True)
def _(covered, mo):
    winner = covered[covered["mutation"] == "Q194L; S220T; H230Y"].iloc[0]
    winner_callout = mo.callout(
        mo.md(
            f"""
            **The KB's flagship: `Q194L/S220T/H230Y`** -- additive expectation
            {winner["expected_ratio"]:.3f}, measured **{winner["ratio"]:.3f}**:
            **{winner["epistasis"]:+.2f} log-odds of synergy**. The variant
            that went to gram-scale synthesis of the drug ZPL389 beat the sum
            of its parts.
            """
        ),
        kind="success",
    )
    winner_callout
    return (winner_callout,)


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            r"""
            ### Answer -- Q5

            **Partially additive, honestly conditional.**

            - Where the KB's claim was made -- the epPCR lineage stacked on
              S220T -- combinations are **additive to synergistic**: round-3
              winners match or beat the sum of their single-mutant effects.
              The claim survives where it was born.
            - **ML-designed stacks** fall short of additive expectation. Some
              of that is assay ceiling, but the pattern is consistent enough
              to say: naively stacking individually-good mutations is not a
              design principle.
            - The KB's exact split (active site vs. distal) is **not
              testable** here -- only 22 combinations touch an active-site
              residue. Saying so is part of the analysis.
            - Design implication: combine **distal, well-measured singles
              within one lineage** -- that is where additivity holds -- and
              validate combinations empirically, exactly what this campaign
              did.
            """
        ),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(
        f"""
        <span style="background:{theme.ACTIVE_SITE};color:white;padding:3px 12px;
        border-radius:12px;font-size:12px;font-weight:600">Q6 / 6 · THE STRESS TEST</span>

        # If the DMS had a hole where the literature matters, would we have noticed?

        Saturation-mutagenesis libraries always have gaps: oligo pools fail,
        some positions never clone. So let's **punch a hole in the DMS on
        purpose** -- at exactly the positions the knowledge base talks about
        -- and ask whether the other three modalities could nominate what
        the data lost.
        """
    )
    return


@app.cell
def _(data, kb):
    notes_q6 = kb.load_all_notes()
    kb_positions = kb.extract_mutation_positions(notes_q6)
    mask_list = sorted(kb_positions)
    singles_q6 = data.extract_single_mutants(data.load_si002())
    masked = data.mask_positions(singles_q6, mask_list)
    return kb_positions, mask_list, masked, notes_q6, singles_q6


@app.cell(hide_code=True)
def _(kb_positions, mo, pd):
    mention_df = pd.DataFrame(
        [
            {
                "position": pos,
                "KB mentions": " · ".join(m.split(" (")[0] for m in mentions),
                "source notes": len(mentions),
            }
            for pos, mentions in kb_positions.items()
        ]
    )
    mask_md = mo.md(
        r"""
        ## The mask, extracted from the knowledge base

        Scanning all six notes for `S220T`-style tokens -- including tokens
        inside combination strings like `Q194L; S220T; H230Y` -- yields the
        KB's cast of characters. No hardcoding anywhere.
        """
    )
    mo.vstack([mask_md, mention_df])
    return (mention_df,)


@app.cell(hide_code=True)
def _(alt, mask_list, masked, mo, pd, singles_q6, theme):
    _by_position = (
        masked.groupby("pos").agg(mean_activity=("mean", "mean")).reset_index()
    )
    full_by_position = (
        singles_q6.groupby("pos").agg(full_mean=("mean", "mean")).reset_index()
    )
    hole_df = pd.DataFrame(
        {"start": [p - 0.5 for p in mask_list], "end": [p + 0.5 for p in mask_list]}
    )
    hole_bands = (
        alt.Chart(hole_df)
        .mark_rect(color=theme.ACTIVE_SITE, opacity=0.18)
        .encode(x="start:Q", x2="end:Q")
    )
    masked_line = (
        alt.Chart(
            _by_position, title="The DMS after masking -- red bands are the blind spot"
        )
        .mark_line(point=True, color=theme.PRIMARY)
        .encode(
            x=alt.X("pos:Q", title="Sequence position"),
            y=alt.Y("mean_activity:Q", title="Mean activity at position"),
        )
        .properties(width=860, height=260)
    )
    ghost_line = (
        alt.Chart(full_by_position)
        .mark_line(color=theme.MUTED, strokeDash=[2, 3], opacity=0.5)
        .encode(x="pos:Q", y="full_mean:Q")
    )
    band_md = mo.md(
        f"""
        {len(singles_q6) - len(masked)} measurements vanish. The grey dashed
        line is the truth we are pretending not to know -- watch what the
        red bands are hiding.
        """
    )
    mo.vstack([band_md, masked_line + ghost_line + hole_bands])
    return (masked_line,)


@app.cell(hide_code=True)
def _(mask_list, mo, pd, structure):
    _crystal = structure.load_crystal_structure()
    _distances = {
        resnum: structure.min_ligand_distance(_crystal, resnum)
        for resnum in _crystal.observed_resnums
    }
    structure_recovery = pd.DataFrame(
        {
            "position": mask_list,
            "site class": [structure.site_class(_distances.get(p)) for p in mask_list],
        }
    )
    mo.vstack(
        [
            mo.md(
                r"""
                ## Recovery attempt 1 -- the crystal structure

                What would the structure alone say about the missing
                positions?
                """
            ),
            structure_recovery,
            mo.md(
                r"""
                Five of six are distal or second-shell -- exactly the
                "nothing special here" annotation that Q2 showed most top
                hits carry. **Structure alone would not have recovered them.**
                """
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(alt, mask_list, mo, np, pd, structure, theme):
    crystal_pred = structure.load_crystal_structure()
    _predicted = structure.load_predicted_structure()
    _aligned, target_coords, shared_resnums = structure.superposed_ca(
        _predicted, crystal_pred
    )
    ca_deviation = pd.Series(
        np.sqrt(((_aligned - target_coords) ** 2).sum(axis=1)), index=shared_resnums
    )
    dev_df = ca_deviation.reset_index()
    dev_df.columns = ["pos", "deviation"]
    dev_df["masked (KB) position"] = dev_df["pos"].isin(mask_list)
    median_deviation = float(ca_deviation.median())
    dev_chart = (
        alt.Chart(
            dev_df,
            title="Prediction-vs-crystal deviation: mobility as a recovery hint",
        )
        .mark_line(point=True)
        .encode(
            x=alt.X("pos:Q", title="Sequence position"),
            y=alt.Y("deviation:Q", title="C-alpha deviation (A)"),
            color=alt.Color(
                "masked (KB) position:N",
                scale=alt.Scale(
                    domain=[False, True], range=[theme.MUTED, theme.ACTIVE_SITE]
                ),
            ),
            tooltip=["pos", "deviation"],
        )
        .properties(width=860, height=240)
    )
    dev_md = mo.md(
        f"""
        ## Recovery attempt 2 -- structure prediction

        Q4 showed the prediction deviates most around 207-243. Do the masked
        positions stand out in that mobility profile? (Protein-wide median
        deviation: {median_deviation:.2f} A.)
        """
    )
    mo.vstack([dev_md, dev_chart])
    return (dev_chart,)


@app.cell(hide_code=True)
def _(kb, mask_list, mo, notes_q6):
    kb_recovery_hits = kb.search_notes(notes_q6, "S220T ee improvement combination")
    kb_md = mo.md(
        f"""
        ## Recovery attempt 3 -- the knowledge base

        The mask came *from* the KB, so of course the KB "recovers" these
        positions -- **this is a workflow demonstration, not a blind
        test**. The KB is an independent record
        of what the campaign learned, with a different failure mode than the
        data: it searched here and found {len(kb_recovery_hits)} notes
        naming the winners and their mechanisms.
        """
    )
    mo.vstack([kb_md])
    return


@app.cell(hide_code=True)
def _(data, kb_positions, mask_list, mo, pd, singles_q6):
    ranked = singles_q6.sort_values("mean", ascending=False).reset_index(drop=True)
    rank_of = {mutation: i + 1 for i, mutation in enumerate(ranked["mutation"])}
    score_rows = []
    for _pos in mask_list:
        _best = singles_q6[singles_q6["pos"] == _pos].nlargest(1, "mean").iloc[0]
        score_rows.append(
            {
                "position": _pos,
                "best single": _best["mutation"],
                "activity": round(_best["mean"], 3),
                "rank of 4,720": rank_of[_best["mutation"]],
                "KB's named mutation": [
                    m.split(" (")[0] for m in kb_positions[_pos] if "gilio" in m
                ][0],
            }
        )
    score_table = mo.ui.table(pd.DataFrame(score_rows), page_size=6, selection=None)
    mo.vstack(
        [
            mo.md(
                r"""
                ## Unmask and score

                What did the hole actually hide?
                """
            ),
            score_table,
        ]
    )
    return (score_table,)


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            r"""
            ### Answer -- Q6

            - **The hole hid the #2 single mutant of the entire campaign**
              (S220T, rank 2 of 4,720) plus two more top-25 hits (A156G at
              23, Y177W at 25). A silent gap in a library is not a neutral
              event.
            - **Structure alone would not have recovered them.** **Prediction
              gives a real partial signal** (S220 at 4.2 A deviation, Q194 at
              2.7). **The KB recovers all six -- by construction**, and the
              circularity is the caveat.
            - **The reverse case is the counterweight:** A296I -- the #1
              single mutant -- is absent from the KB. Data finds what
              literature lacks; literature recovers what data loses.
            """
        ),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo, theme):
    mo.md(
        f"""
        <div style="background:linear-gradient(135deg, {theme.PRIMARY} 0%, #134e4a 100%);
                    border-radius:16px; padding:26px 30px; color:white;">
        <div style="font-size:12px; letter-spacing:2px; opacity:0.85;
                    text-transform:uppercase;">The overarching question, answered</div>
        <h2 style="margin:10px 0 8px 0; font-size:22px; line-height:1.3;">
        Where do activity-improving mutations of IRED-88 come from -- and
        could we have seen them coming?</h2>
        <div style="font-size:14px; line-height:1.55; opacity:0.95;">
        Mostly <b>not from the active site</b>: they come from distal
        positions, a mobile loop (207-243), and the termini -- tuning access,
        dynamics, and stability rather than chemistry. Could we have seen
        them coming? <b>The DMS finds them</b> (including hits the literature
        never interpreted), <b>the structure filters the naive "mutate the
        active site" prior</b>, <b>the KB explains the leads and recovers
        what a data gap would erase</b>, and <b>prediction extends the
        structure into its blind spots with an honesty score attached</b>.
        No single modality answers the question -- the copilot move is the
        round-trip between all four. In one repo. In six notebooks. In one
        session.</div>
        </div>

        <div style="font-size:12px; color:{theme.MUTED}; margin-top:14px;">
        Built for the "AI as a Research Co-Pilot" course (UMass Chan Medical
        School). Data: supporting information of Ma et al., <i>ACS Catal.</i>
        2021, DOI 10.1021/acscatal.1c02786. Notebooks written with AI
        assistance (Claude + Codex, via the pi harness); every claim traces
        to a cell, a file in this repo, or a KB note.</div>
        """
    )
    return


if __name__ == "__main__":
    app.run()
