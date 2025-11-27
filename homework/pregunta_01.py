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

    input_path = "files/input/solicitudes_de_credito.csv"
    output_path = "files/output/solicitudes_de_credito.csv"

    df = pd.read_csv(input_path, sep=";", index_col=0)

    # sexo
    df["sexo"] = df["sexo"].str.lower().str.strip()

    # tipo_de_emprendimiento
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.strip()

    # idea_negocio
    idea = df["idea_negocio"].str.lower()
    idea = idea.str.replace("_", " ")
    idea = idea.str.replace("-", " ")
    idea = idea.str.strip()
    df["idea_negocio"] = idea

    # barrio (nota: igual que tu versión, sin strip final)
    barrio = df["barrio"].str.lower()
    barrio = barrio.str.replace("_", " ")
    barrio = barrio.str.replace("-", " ")
    df["barrio"] = barrio

    # estrato y comuna_ciudadano
    df["estrato"] = [int(x) for x in df["estrato"]]
    df["comuna_ciudadano"] = [int(x) for x in df["comuna_ciudadano"]]

    # fecha_de_beneficio (dos formatos posibles)
    fecha_raw = df["fecha_de_beneficio"]
    fecha1 = pd.to_datetime(fecha_raw, format="%d/%m/%Y", errors="coerce")
    fecha2 = pd.to_datetime(fecha_raw, format="%Y/%m/%d", errors="coerce")
    df["fecha_de_beneficio"] = fecha1.combine_first(fecha2)

    # monto_del_credito
    monto = df["monto_del_credito"].astype(str)
    monto = monto.str.replace("$", "")
    monto = monto.str.replace(",", "")
    monto = monto.str.replace(".00", "")
    monto = monto.str.strip()
    df["monto_del_credito"] = monto

    # línea_credito
    linea = df["línea_credito"].str.lower().str.strip()
    linea = linea.str.replace("_", " ")
    linea = linea.str.replace("-", " ")
    linea = linea.str.strip()
    df["línea_credito"] = linea

    # duplicados y nulos
    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, sep=";", index=False)


if __name__ == "__main__":
    pregunta_01()