"""Descarga los datos de UN Comtrade usados en el análisis.

Usa el endpoint público de vista previa de la API de Comtrade (no requiere clave):
  - Exportaciones informadas por Uruguay (reporter 858), capítulo 44 y partidas 4403 y 4407.
  - Datos espejo: importaciones de celulosa (HS 4703) informadas por todos los países
    con Uruguay como origen (partner 858).

Uso:  python src/descarga_comtrade.py
Salida: data/raw/*.csv  (una fila por año, producto y socio)
"""
import time
from pathlib import Path

import pandas as pd
import requests

BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
ANIOS = range(2015, 2026)
SALIDA = Path(__file__).resolve().parents[1] / "data" / "raw"


def consultar(params: dict, reintentos: int = 6) -> list[dict]:
    """Una consulta a la API con reintentos ante límites de frecuencia (HTTP 429)."""
    for _ in range(reintentos):
        r = requests.get(BASE, params=params, timeout=60)
        if r.status_code == 429:
            time.sleep(5)
            continue
        r.raise_for_status()
        return r.json().get("data", [])
    raise RuntimeError(f"Sin respuesta para {params}")


def totales(filas: list[dict]) -> list[dict]:
    """Se queda con los registros agregados (sin desglose por aduana, modo de transporte ni segundo socio)."""
    return [f for f in filas
            if f.get("partner2Code") == 0 and f.get("customsCode") == "C00" and f.get("motCode") == 0]


def main() -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    expo, espejo = [], []
    for anio in ANIOS:  # la vista previa admite un solo período por consulta
        for hs in ["44", "4403", "4407"]:
            filas = consultar({"reporterCode": 858, "period": anio, "cmdCode": hs, "flowCode": "X"})
            expo += [{"anio": anio, "hs": hs, "socio_cod": f["partnerCode"],
                      "valor_usd": f["primaryValue"], "peso_kg": f.get("netWgt")} for f in totales(filas)]
            time.sleep(2.5)
        filas = consultar({"partnerCode": 858, "period": anio, "cmdCode": "4703", "flowCode": "M"})
        espejo += [{"anio": anio, "importador_cod": f["reporterCode"],
                    "valor_usd": f["primaryValue"], "peso_kg": f.get("netWgt")} for f in totales(filas)]
        time.sleep(2.5)
        print(f"{anio}: ok")
    pd.DataFrame(expo).to_csv(SALIDA / "uy_exportaciones_cap44.csv", index=False)
    pd.DataFrame(espejo).to_csv(SALIDA / "espejo_celulosa_4703.csv", index=False)


if __name__ == "__main__":
    main()
