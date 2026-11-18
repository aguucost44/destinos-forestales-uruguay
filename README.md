# Celulosa y madera uruguaya: destinos de exportación 2015–2025

Análisis de los destinos de la celulosa y la madera exportadas por Uruguay, con datos de UN Comtrade. Retoma una pregunta abierta de mi tesis de maestría sobre certificación forestal y EUDR: cuánto pesa hoy Europa como mercado y qué tan rápido está cambiando la geografía de los compradores.

**Lectura rápida:** [Nota de análisis (PDF, 2 páginas)](nota/Nota_celulosa_destinos_Costa.pdf)
**Detalle y código:** [`analisis_destinos_forestales.ipynb`](analisis_destinos_forestales.ipynb)

![Destinos de la celulosa](figuras/celulosa_destinos.png)

## Resultados

- La Unión Europea pasó de recibir 52–56 % del valor de la celulosa entre 2016 y 2022 a cerca del 32 % en 2025. China volvió al primer lugar (39 %) y Estados Unidos subió de casi cero a 9 %.
- Aun así, Europa sigue comprando entre USD 800 y 1.100 millones por año, así que la EUDR mantiene su peso como condición de acceso.
- La concentración de compradores (IHH) vuelve a subir desde 2023: baja la dependencia de un marco regulatorio y sube la dependencia de un único comprador.
- Un punto metodológico: la celulosa casi no aparece en las estadísticas aduaneras que Uruguay informa, porque las plantas operan en zonas francas. Para medirla uso datos espejo, es decir, lo que declaran los países importadores.

## Estructura

```
├── nota/                                   nota de análisis en PDF
├── analisis_destinos_forestales.ipynb      análisis completo
├── src/descarga_comtrade.py                descarga desde la API pública de Comtrade
├── data/                                   datos procesados (CSV)
└── figuras/                                gráficos
```

## Reproducir

```bash
pip install -r requirements.txt
python src/descarga_comtrade.py      # opcional, vuelve a bajar los datos
jupyter notebook analisis_destinos_forestales.ipynb
```

Los datos espejo están en valores CIF y 2025 es preliminar. Los límites y los próximos pasos están al final del notebook.

Agustín Costa · [LinkedIn](https://linkedin.com/in/agustín-costa-b66b66206)
