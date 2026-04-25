"""Funciones básicas para normalizar nombres de equipamientos y comprobar coincidencias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from unidecode import unidecode


@dataclass(frozen=True)
class EquipmentAlias:
    canonical_name: str
    aliases: tuple[str, ...]


def normalize_text(value: str) -> str:
    """Normaliza un texto para comparaciones simples."""
    return " ".join(unidecode(value.lower()).split())


def match_equipment(text: str, alias_table: Iterable[EquipmentAlias]) -> str | None:
    """Devuelve el nombre canónico si encuentra una coincidencia nominal básica."""
    normalized = normalize_text(text)
    for item in alias_table:
        candidates = (item.canonical_name, *item.aliases)
        if any(normalize_text(candidate) in normalized for candidate in candidates):
            return item.canonical_name
    return None
