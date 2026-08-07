"""Phase-1 numeric inputs, captured from cited research (access date 2026-07-19).
Sources are documented in logs/methods_log.md. Nothing here is fabricated;
low-reliability / substituted values are flagged.
"""

# --- Monthly climate normals (IDEAM-anchored). P mm/month, T degC mean; idx 0=Jan..11=Dec ---
NORMALS = {
    'villa_de_leyva': {'elev': 2149,
        'P': [50.2, 71.1, 115.3, 123.0, 106.7, 41.8, 39.7, 40.2, 67.4, 148.9, 119.2, 83.0],
        'T': [16.7, 17.1, 17.2, 17.3, 17.2, 17.1, 16.8, 16.9, 17.0, 16.7, 16.7, 16.6],
        'P_annual': 997, 'T_annual': 16.9, 'lat': 5.633,
        'src': 'IDEAM 1981-2010 normal', 'reliability': 'high'},
    'tunja': {'elev': 2782,
        'P': [18.1, 27.4, 53.5, 81.3, 85.2, 55.0, 49.1, 40.2, 50.0, 86.0, 73.9, 32.8],
        'T': [13.3, 13.6, 13.9, 13.8, 13.5, 12.7, 12.2, 12.3, 12.7, 13.2, 13.4, 13.2],
        'P_annual': 652.5, 'T_annual': 13.1, 'lat': 5.535,
        'src': 'IDEAM UPTC station', 'reliability': 'high'},
    'arcabuco': {'elev': 2600,
        'P': [123.1, 151.3, 221.5, 233.2, 176.8, 72.2, 62.5, 58.2, 107.8, 237.6, 225.9, 156.4],
        'T': [13.9, 14.4, 14.6, 14.6, 14.3, 13.7, 13.2, 13.4, 13.6, 14.0, 14.1, 13.8],
        'P_annual': 1826.5, 'T_annual': 14.0, 'lat': 5.760,
        'src': 'IDEAM + climate-data.org blend', 'reliability': 'med'},   # P +/-15%
    'el_colegio': {'elev': 1100,   # cabecera 990 m, Mesitas ~1200 m
        'P': [70.4, 97.8, 128.1, 127.9, 138.6, 45.7, 36.9, 46.2, 96.5, 141.6, 147.8, 90.8],
        'T': [23.6, 23.7, 23.5, 23.0, 23.0, 23.1, 23.4, 24.1, 23.9, 23.2, 22.8, 23.0],
        'P_annual': 1168.3, 'T_annual': 23.4, 'lat': 4.580,
        'src': 'IDEAM sta. Las Mercedes 810m + La Mesa analog (T lapse-adj)', 'reliability': 'med'},
    'sachica': {'elev': 2150,
        'P': [36, 51, 83, 89, 77, 30, 29, 29, 49, 107, 86, 60],           # SUBSTITUTED
        'T': [17.2, 17.6, 17.7, 17.8, 17.7, 17.6, 17.3, 17.4, 17.5, 17.2, 17.2, 17.1],
        'P_annual': 726, 'T_annual': 17.4, 'lat': 5.585,
        'src': 'SUBSTITUTED: Villa de Leyva x0.72 (dry-SW band)', 'reliability': 'low'},
    # --- Moniquira (added 2026-08-08) ---------------------------------------------------
    # CAUTION on the POMCA subcuenca table: the unit named "Rio Moniquira" (24010214) reads
    # 1127.2 mm/yr, but that is NOT Moniquira's rainfall. That subcuenca has a mean elevation of
    # 2560 m and its child micro-basins include Rio Sachica (2401021408) and Rio Cane
    # (2401021409) - i.e. it is the whole Villa de Leyva / Sachica / Raquira drainage, whose
    # semi-arid highlands (VdL 997, Sachica 726) drag the area-average down. Using 1127 for
    # Moniquira would be a unit-attribution error.
    # The units that actually contain the Moniquira parcels are the low-elevation ones around the
    # town: Qda Agua Blanca (24010213) 1827.6, Dir Q Agua Blanca-R Moniquira (24010230) 1846.5,
    # Dir R Moniquira-R Ubaza (24010231) 1869.6, Rio Ubaza (24010215) 1896.2 -> mean 1860 mm/yr.
    # Cross-check: Arcabuco drains via Rio Pomeca (2401021501, a child of Rio Ubaza 24010215),
    # whose POMCA value 1896.2 agrees with this file's independently-sourced Arcabuco 1826 to 4%.
    # So Arcabuco and Moniquira get near-identical RAIN; what separates them is PET (4.8 C warmer).
    # Monthly SHAPE from climate-data.org Moniquira (1991-2021, bimodal, no dry month) rescaled to
    # the 1860 total. climate-data.org's own magnitude is not used: its Villa de Leyva page reads
    # 1767 mm / 13.4 C against the IDEAM normal 997 mm / 16.9 C (+77% wet, -3.5 C), i.e. its
    # municipal grid points sit too high in this terrain. Other estimates for Moniquira: NASA
    # POWER ~1530 mm, climate-data.org de-biased by the VdL ratio ~1650 mm -> range 1530-1900.
    'moniquira': {'elev': 1700,
        'P': [67.6, 80.3, 128.1, 202.1, 244.8, 184.8, 170.8, 170.8, 198.9, 193.8, 133.9, 84.1],
        'T': [18.5, 18.9, 18.9, 18.9, 19.0, 19.1, 19.0, 19.2, 19.1, 18.6, 18.2, 18.4],
        'P_annual': 1860, 'T_annual': 18.8, 'lat': 5.876,
        'src': 'P: Corpoboyaca POMCA Medio-Bajo Suarez (Consorcio POMCA 2015), mean of the four '
               'hydrographic units containing the Moniquira parcels (24010213/230/231/215) '
               '= 1860 mm/yr, range 1827.6-1896.2; monthly shape climate-data.org 1991-2021 '
               'rescaled to that total. T: 3-source reconciliation at 1700 m (climate-data.org '
               '18.2 / NASA POWER lapse-adj 18.7 / IDEAM-anchored lapse 19.6) -> 18.8',
        'reliability': 'med'},
}
VEREDA_ELEV = {'gachantiva': 2450, 'santa_sofia': 2387, 'sutamarchan': 2000,
               'tena': 1384, 'san_antonio_del_tequendama': 1540, 'la_mesa': 1200}

# --- Published climate-change projection ranges (decision-support; do NOT run a GCM) ---
PROJECTIONS = {
    'note': 'IDEAM dept values are multi-model ENSEMBLE central estimates (behave ~moderate pathway); '
            'scenario spread from CMIP6/AR6 rows. Andes mean-precip = deep uncertainty.',
    'boyaca':       {'dT_2050': 1.6, 'dT_2085': 2.4, 'dP_note': 'VdL/Ricaurte outside the +20-40% nucleus -> ~0 to -10/-20%'},
    'cundinamarca': {'dT_2050': 1.5, 'dT_2085': 2.3, 'dP_note': '+10 to +30% some areas / up to -20% others'},
    'highland_decision_range_dT': (1.4, 3.5),   # 2050s: IDEAM ensemble low -> SSP5-8.5 upper
    'central_planning_dT_2050': (1.5, 2.0),
    'extreme_rainfall': '+26-37% extreme-rain days by 2050; ~2x 100-yr events (CMIP6) -> landslide-relevant (Mesitas)',
    'water_stress_guidance': 'drive water balance with flat-to-declining mean P + higher PET (+1.5-2.4C) + ENSO excursions (El Nino -20 to -60% P)',
}

# --- Seismic (NSR-10) ---
AA_AV = {
    'tunja':          {'Aa': 0.20, 'Av': 0.20, 'zona': 'INTERMEDIA', 'status': 'verified (Tabla A.2.3-2)'},
    'moniquira':      {'Aa': None, 'Av': None, 'zona': 'INTERMEDIA', 'status': 'zone per municipal PDM 2020-2023 ("zona de sismicidad media"); Aa/Av UNVERIFIED (Apendice A-4)'},
    'el_colegio':     {'Aa': None, 'Av': None, 'zona': 'INTERMEDIA', 'status': 'zone confirmed; Aa/Av UNVERIFIED (Apendice A-4), expect 0.15-0.20'},
    'villa_de_leyva': {'Aa': None, 'Av': None, 'zona': 'INTERMEDIA', 'status': 'zone confirmed; Aa/Av UNVERIFIED (Apendice A-4), expect 0.15-0.20'},
}
# Named-fault representative trace points (approx; SGC/Velandia2005). (lat,lon)
FAULTS_NAMED = {
    'Bituima':  [(4.82, -74.55), (4.50, -74.62)],
    'Viani':    [(4.86, -74.58)],
    'Cambao':   [(4.95, -74.82), (4.55, -74.75)],
    'Boyaca':   [(5.45, -73.40), (5.79, -73.22)],
    'Soapaga':  [(5.79, -72.87), (6.00, -72.80)],
}
GEM_FAULTS_URL = 'https://raw.githubusercontent.com/GEMScienceTools/gem-global-active-faults/master/geojson/gem_active_faults_harmonized.geojson'
MPIO_GEOJSON_URL = 'https://raw.githubusercontent.com/santiblanko/colombia.geojson/master/mpio.json'
# DANE municipal codes for our study/candidate municipalities
# NOTE 2026-08-08: santa_sofia was '15690' (= SANTA MARIA, 280.9 km2, Boyaca's Llanos flank) and
# sutamarchan was '15762' (= SORA, 30.4 km2). Both were pulling the wrong polygon into the map.
# Corrected against the source mpio.json: Santa Sofia = 15696 (74.6 km2), Sutamarchan = 15776
# (105.6 km2). Moniquira = 15469 (212.8 km2) added.
DANE = {'el_colegio': '25245', 'villa_de_leyva': '15407', 'tunja': '15001',
        'arcabuco': '15051', 'santa_sofia': '15696', 'gachantiva': '15293',
        'sachica': '15638', 'sutamarchan': '15776', 'tena': '25797',
        'la_mesa': '25386', 'san_antonio_del_tequendama': '25645',
        'moniquira': '15469'}
