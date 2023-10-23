# This code is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
# Copyright © [Point 8 GmbH](https://point-8.de)
import pathlib
from turtle import color

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
from Overview import add_logo
from PIL import Image
from plotly.colors import n_colors

add_logo()

# st.title("Szenariorahmen")
st.markdown("# Szenariorahmen")
(
    tab_a4,
    tab_a11,
    tab_a14,
) = st.tabs(["Abbildung 4", "Abbildung 11", "Abbildung 14"])

with tab_a4:
    st.markdown(
        "### Übersicht über die Verteilung der installierten Leistungen je Energieträger"
    )

    df_c2_a4 = pd.read_excel(
        pathlib.Path(__file__).parent.parent.parent
        / "data/Kapitel_2_Daten_NEP_2037_V2023_2_Entwurf.xlsx",
        sheet_name="Abbildung 4",
        header=2,
        index_col=0,
    ).dropna()
    st.dataframe(df_c2_a4)

    fig = px.bar(
        df_c2_a4,
        barmode="group",
        labels={"value": "Installierte Leistung in GW", "variable": "Szenarien"},
    )
    st.plotly_chart(fig, use_container_width=True)

    red_blue = n_colors("rgb(0, 0, 255)", "rgb(255, 0, 0)", 7, colortype="rgb")

    fig2 = px.bar(
        df_c2_a4.transpose(),
        labels={"value": "Installierte Leistung in GW", "index": "Szenarien"},
    )
    st.plotly_chart(fig2, use_container_width=True)


with tab_a11:
    st.markdown(
        "### Mittlerer, minimaler und maximaler Flexibilitätseinsatz je Tagesstunde in Szenario B 2037"
    )
    df_c2_a11 = pd.read_excel(
        pathlib.Path(__file__).parent.parent.parent
        / "data/Kapitel_2_Daten_NEP_2037_V2023_2_Entwurf.xlsx",
        sheet_name="Abbildung 11",
        skiprows=4,
        index_col=0,
    )
    col_names = [
        "Einheit",
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
    ]
    df_c2_a11.columns = col_names

    st.dataframe(df_c2_a11)

    df_c2_a11_plot = df_c2_a11.drop("Einheit", axis=1).transpose()
    # st.dataframe(df_c2_a11_plot)

    figX, ax = plt.subplots()
    ax.plot(
        df_c2_a11_plot.index,
        df_c2_a11_plot["Flexibilitätseinsatz - Median"],
        ".",
        label="median",
    )
    ax.vlines(
        df_c2_a11_plot.index,
        df_c2_a11_plot["Flexibilitätseinsatz - Minimum"],
        df_c2_a11_plot["Flexibilitätseinsatz - Maximum"],
    )

    for i in range(len(df_c2_a11_plot["Flexibilitätseinsatz - 25%-Quantil"])):
        ax.fill_between(
            [df_c2_a11_plot.index[i] - 0.2, df_c2_a11_plot.index[i] + 0.2],
            df_c2_a11_plot["Flexibilitätseinsatz - 25%-Quantil"].values[i],
            df_c2_a11_plot["Flexibilitätseinsatz - 75%-Quantil"].values[i],
            alpha=0.5,
            color="C1",
        )

    ax.set_xlabel("Stunde des Tages")
    ax.set_ylabel("Flexibilitätseinsatz in GW")
    ax.set_xticks(
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
        ],
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
        ],
    )

    ax2 = ax.twinx()
    ax2.plot(
        df_c2_a11_plot.index,
        df_c2_a11_plot["Marktpreise - Mittelwert"],
        ".--C3",
        label="Marktpreise",
    )
    ax2.set_ylabel("Marktpreis in Euro/MWh", color="C3")
    ax2.tick_params(axis="y", labelcolor="C3")
    st.pyplot(figX)

with tab_a14:
    st.markdown("### Installierte Leistungen je Bundesland im Szenario A 2037")

    df_c2_a14 = pd.read_excel(
        pathlib.Path(__file__).parent.parent.parent
        / "data/Kapitel_2_Daten_NEP_2037_V2023_2_Entwurf.xlsx",
        sheet_name="Abbildung 14",
        skiprows=2,
        index_col=0,
    ).dropna()
    st.dataframe(df_c2_a14)
