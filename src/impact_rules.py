"""Reglas interpretables para clasificación multietiqueta del impacto público."""

from __future__ import annotations

IMPACT_KEYWORDS = {
    "notoriedad_publica": [
        "reconocimiento",
        "visibilidad",
        "programacion",
        "medios",
        "presencia cultural",
        "institucional",
    ],
    "cohesion_social": [
        "vecinal",
        "comunidad",
        "participacion",
        "mediacion",
        "intergeneracional",
        "talleres",
    ],
    "transformacion_territorial": [
        "barrio",
        "entorno urbano",
        "regeneracion",
        "revitalizacion",
        "territorio",
    ],
    "fortalecimiento_sector_cultural": [
        "artistas",
        "programacion",
        "residencias",
        "formacion",
        "ecosistema",
    ],
    "derechos_culturales": [
        "acceso",
        "accesible",
        "inclusion",
        "colectivos",
        "publicos",
    ],
    "influencia_publica": [
        "institucional",
        "agenda publica",
        "debate",
        "politicas culturales",
        "reconocimiento institucional",
    ],
}


def classify_text(text: str) -> list[str]:
    """Clasifica un texto con lógica multietiqueta basada en palabras clave."""
    lowered = text.lower()
    labels: list[str] = []
    for label, keywords in IMPACT_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            labels.append(label)
    return labels
