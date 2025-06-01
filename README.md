# Map4PNG
Map4PNG is a initiative to build and maintain up-to-date, open, and accessible geographic data for Papua New Guinea (PNG). The project focuses on collecting, verifying, and visualizing village locations, wards, LLGs, districts, and provinces using public data sources, GIS tools, and community input.

## How we will do this
One ward at a time of course. PNG is structured, from top to bottom, as Regions -> Provinces -> Districts -> LLGs -> Wards (see below). The focus of this project is around districts, LLGs, and wards as various restrutures over last decade as primary affected them.

## How PNG is strutured

### 1. Regions
Regions are informal administrative groupings used mainly for cultural, geographical, and statistical purposes. They are not formal governance units under the Constitution but are widely recognized.
PNG Has 4 regions:
* Highlands
* Momase
* Southern
* New Guinea Islands

### 2. Provinces
The primary administrative divisions under PNG's decentralized system of government, with their own provincial governments. there are 22 provinces (20 provinces + National Capital District (NCD) + Autonomous Region of Bougainville (AROB).

### 3. Districts
Subdivisions of provinces that serve as electoral and administrative units. Each district elects a Member of Parliament (MP) to the National Parliament. Districts are the core unit for service delivery funds (e.g., DSIP – District Services Improvement Program)

### 4. Local-Level Governments (LLGs)
Sub-district level administrative units responsible for local governance and service delivery.There are over 300 LLGs (some sources cite 318 or more)

LLG's come in two flavours:
* Urban LLGs
* Rural LLGs

### 5. Wards
The smallest administrative unit in PNG, typically consisting of a village or group of villages. There are over 6,000 wards

## The Process
So when going through the old village data, we will use various methods ranging from desk-review of reports, papers, etc. all over the internet along with some from the PNGEC to attempt to place the village under the right ward.

Apart from that, we also try to estimate the 2025 population of the village. To estimate the 2025 village populations, we applied a compound annual growth formula based on each village's historical growth rate (G_RATE). The projection uses the following formula:

`Projected Population = POP2008 × (1 + G_RATE) ^ Years`
* `POP2008` is the last known population estimate.
* `G_RATE` is the historical growth rate from the 2000–2008 period.
* `Years` is the time span from 2008 to 2025 (i.e., 17 years).

We assume a constant growth rate and do not account for external variables like migration, natural disasters, or policy changes. This method provides a simplified, yet practical estimate for contemporary population distribution mapping.

# How to build

## Requirements
* Python 3.1 (tested on Python 3.13.0)

## Building
Simply run `build.py` in the `scripts` directory. It will then compile all geojson files inside `data/villages_by_prov_dist_llg_ward/` into `build/all_villages.geojson`.

# Sources
1. [PNGSDF](https://mapping.pngsdf.com/)
2. [PNG Electoral Commission – Electoral Boundaries](https://www.pngec.gov.pg/)
3. [National Statistical Office PNG – Population and Administrative Data](https://www.nso.gov.pg/)
4. [OpenStreetMap – Papua New Guinea Map Data](https://www.openstreetmap.org/)
5. [Humanitarian Data Exchange (HDX) – Papua New Guinea Datasets](https://data.humdata.org/dataset?q=Papua+New+Guinea)
6. [UN OCHA – Common Operational Datasets (CODs)](https://data.humdata.org/organization/ocha-fis)
7. [AusMap (Australian National University) – PNG Map Viewer](https://ausnatuni.maps.arcgis.com/apps/webappviewer/index.html?id=0f8ca2194d604900b8a24832565cff1f)
8. [Mapshaper – Online GeoJSON Simplifier and Editor](https://mapshaper.org/)
