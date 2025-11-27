"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """

    import os
    import pandas as pd

    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df = pd.read_csv(input_file, sep=";", index_col=0)

    df.dropna(inplace=True)

    columnas_texto = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    accent_map = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u",
        "ñ": "n",
    }

    for col in columnas_texto:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower()

            for acc, non_acc in accent_map.items():
                df[col] = df[col].str.replace(acc, non_acc, regex=False)

            df[col] = df[col].str.replace("_", " ", regex=False)
            df[col] = df[col].str.replace("-", " ", regex=False)
            df[col] = df[col].str.replace(".", "", regex=False)

            df[col] = df[col].str.replace(r"\s+", " ", regex=True)
            df[col] = df[col].str.strip()

    if "monto_del_credito" in df.columns:
        df["monto_del_credito"] = (
            df["monto_del_credito"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace(" ", "", regex=False)
            .astype(float)
        )

    if "comuna_ciudadano" in df.columns:
        df["comuna_ciudadano"] = pd.to_numeric(
            df["comuna_ciudadano"], errors="coerce"
        )

    if "estrato" in df.columns:
        df["estrato"] = df["estrato"].astype(str).astype(int)

    if "fecha_de_beneficio" in df.columns:
        df["fecha_de_beneficio"] = pd.to_datetime(
            df["fecha_de_beneficio"],
            dayfirst=True,
            errors="coerce",
        )

    df.drop_duplicates(inplace=True)

    df.to_csv(output_file, sep=";", index=False)