"""Preserve the A3 poster as a vector page in the rendered report PDF.

Usage: python tools/finalize_report.py /absolute/path/rendered-report.pdf
Requires pypdf and reportlab. Render and review the DOCX before this step.
"""
from io import BytesIO
from pathlib import Path
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parents[1]
source = PdfReader(sys.argv[1])
poster = PdfReader(ROOT / "docs/Spotify_Clayton_A3_Poster.pdf").pages[0]
assert len(source.pages) == 21, "Re-check the contents page after layout changes."
width, height = float(poster.mediabox.width), float(poster.mediabox.height)
overlay = BytesIO()
canvas = Canvas(overlay, pagesize=(width, height))
canvas.setFont("Helvetica", 9)
canvas.drawRightString(width - 28, 15, "9")
canvas.save()
overlay.seek(0)
poster.merge_page(PdfReader(overlay).pages[0])
writer = PdfWriter()
for index, page in enumerate(source.pages):
    writer.add_page(poster if index == 8 else page)
writer.add_metadata({"/Title": "LDCW6123 Group 13 Spotify and Physical Music Project",
                     "/Subject": "Clayton model and Music Discovery Assistant"})
output = ROOT / "docs/LDCW6123_Spotify_Project.pdf"
with output.open("wb") as stream:
    writer.write(stream)
print(f"Created {output}: 21 pages, including the original A3 poster page.")
