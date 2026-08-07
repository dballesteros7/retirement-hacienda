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
DANE = {'el_colegio': '25245', 'villa_de_leyva': '15407', 'tunja': '15001',
        'arcabuco': '15051', 'santa_sofia': '15690', 'gachantiva': '15293',
        'sachica': '15638', 'sutamarchan': '15762', 'tena': '25797',
        'la_mesa': '25386', 'san_antonio_del_tequendama': '25645'}
