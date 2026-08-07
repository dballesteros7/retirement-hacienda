"""Shared config for the Hacienda geospatial analysis (Phase 1).
All coordinates (lat, lon) in WGS84 degrees. AOIs as (lat_min, lat_max, lon_min, lon_max).
"""

# --- Reference points (lat, lon) ---
POINTS = {
    # municipal seats
    "el_colegio":      (4.5797, -74.4442),
    "villa_de_leyva":  (5.6339, -73.5250),
    "tunja":           (5.5353, -73.3678),
    # destinations
    "bog_eldorado":    (4.7016, -74.1469),   # El Dorado Intl airport
    "bogota_center":   (4.6118, -74.0817),
    "paipa_airport":   (5.7659, -73.1069),   # Juan José Rondón (intermittent domestic)
    # hospitals (approx; REPS-registered facilities)
    "hosp_lamesa_II":       (4.6300, -74.4640),  # ESE Pedro León Álvarez Díaz (Nivel II)
    "hosp_tunja_III":       (5.5410, -73.3560),  # Hosp. Univ. San Rafael (Nivel III)
    "hosp_villaleyva_I":    (5.6360, -73.5230),  # ESE San Francisco (Nivel I)
    # Ricaurte wet NE flank & dry SW (candidate sectors)
    "arcabuco":        (5.7597, -73.4372),
    "santa_sofia":     (5.7133, -73.6019),
    "gachantiva":      (5.7558, -73.5478),
    "sachica":         (5.5847, -73.5447),
    "sutamarchan":     (5.6206, -73.6206),
    "iguaque_laguna":  (5.6850, -73.4560),   # páramo water source, ~3800 m
    # Tequendama candidate sectors
    "la_mesa":         (4.6320, -74.4620),
    "tena":            (4.6558, -74.3906),
    "san_antonio_tequendama": (4.6167, -74.3500),
}

# --- Areas of interest: (lat_min, lat_max, lon_min, lon_max) ---
AOIS = {
    "el_colegio":     (4.48, 4.66, -74.55, -74.34),   # municipality + Tequendama corridor
    "villa_de_leyva": (5.55, 5.78, -73.63, -73.44),   # town + dry SW + wet NE Iguaque flank
    "tunja":          (5.47, 5.60, -73.43, -73.30),   # lighter comparator
}

# --- Copernicus GLO-30 DEM tiles (public AWS Open Data, no key) ---
DEM_TILES = {
    "N04_W075": "https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N04_00_W075_00_DEM/Copernicus_DSM_COG_10_N04_00_W075_00_DEM.tif",
    "N05_W074": "https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N05_00_W074_00_DEM/Copernicus_DSM_COG_10_N05_00_W074_00_DEM.tif",
}
# which tile covers each AOI
AOI_TILE = {"el_colegio": "N04_W075", "villa_de_leyva": "N05_W074", "tunja": "N05_W074"}

WGS = "EPSG:4326"
UTM18N = "EPSG:32618"   # local projected CRS for slope/area (m)

# Buildable-land slope thresholds (degrees)
SLOPE_BUILDABLE = 15.0      # <=15 deg: readily buildable
SLOPE_MARGINAL = 25.0       # 15-25 deg: buildable with earthworks; >25 hard/unsafe
