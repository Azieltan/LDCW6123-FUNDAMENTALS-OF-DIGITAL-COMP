# Spotify and Physical Music Clayton Model

LDCW6123, Trimester 2620, Group 13. Group leader: Aziel Tan Zheng Chuan (261UC240LY).

Part 1 is an A3 poster and report applying Clayton Christensen's model to Spotify streaming and CD listening. The graph uses delivered digital audio fidelity as one conceptual performance metric. The yellow CD path is close to level because its format is fixed; the green Spotify path begins with compressed streaming and reaches an available Premium lossless option in 2025. The red and purple dashed lines show demanding and less demanding listeners on this metric. A separate blue callout identifies on-demand access and discovery. The graph is not a revenue plot or measured fidelity series. Physical music persists, and a strict disruptive classification remains debatable.

The structure was checked side by side against `Clayton Disruptive Model Template (1).pptx`, `Claytons_Disruptive Model sample 1.pdf` and `TOPIC 6A (1).pdf` page 20 and explanation pages 25–27. The review is documented in `qa/GRAPH_SPEC.md` and `qa/side_by_side.png`. Superseded Netflix documents are retained under `legacy_netflix/` only as history; the root `docs/` contains the Spotify version.

Part 2 is a self-contained **Music Discovery Assistant**. It demonstrates searchable digital-music discovery using 12 fictional tracks and artists. It does not connect to Spotify, use its API, access an account or claim to replicate its proprietary recommendations.

## Compile and run

```sh
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o music_assistant
./music_assistant
```

On Windows with MinGW, use `-o music_assistant.exe` and run that executable. The programme needs no Python or internet connection.

Choose genre (Pop, Electronic or Acoustic), mood (Calm, Energetic or Reflective), and track duration (up to 4 minutes or longer). A matching genre is required; matching mood adds two points and matching duration adds one. Equal scores retain the first track in catalogue order. The explanation lists only preferences that actually matched. Whole-line input validation rejects text, decimals, trailing letters, blank and out-of-range values. EOF exits cleanly, and a future catalogue lacking a genre receives a safe fallback.

## Reproduce evidence

Python 3 and a C++17 compiler are needed for automated tests. Pillow is also needed for screenshot generation. On a POSIX terminal:

```sh
sh test.sh
python3 tools/build_evidence.py
```

The 35 black-box checks cover all 18 preference combinations, eight invalid inputs, four EOF points, repeat queries, whitespace, bounds, fallback and mood priority. `assets/test_results.csv` is written by the test script after real executions. Output transcripts and code/output captures are generated from the compiled programme, and Git history evidence is generated from the actual repository.

## Rebuild the documents

The builder needs the Codex primary Python runtime (or an environment with python-docx, reportlab, Pillow and pypdf), plus Poppler and LibreOffice for rendering and review. From the project directory:

```sh
sh test.sh
python3 tools/build_evidence.py
python3 tools/build_documents.py
```

To make the combined PDF after reviewing the rendered Word file, export `docs/LDCW6123_Spotify_Project.docx` to a temporary PDF with LibreOffice or Word, then run `python3 tools/finalize_report.py /absolute/path/to/that-export.pdf`. The helper replaces page 9 with the original A3 poster and checks the expected 21-page layout. Inspect all pages again after changes to declarations or links.

`docs/Spotify_Clayton_A3_Poster.pdf` is the standalone A3 poster. `docs/LDCW6123_Spotify_Project.docx` is the editable 21-page report with original assessment form, six blank personal declarations, contents, A3 poster and Part 2 evidence. `docs/LDCW6123_Spotify_Project.pdf` is the reviewed PDF. `docs/REFERENCES.md` and `PRESENTATION_SCRIPT.md` provide the references and suggested six-person script; the latter also has a PDF version. The active Spotify builder reuses tested coversheet and Word layout helpers from `legacy_netflix/tools/build_documents.py`; it does not call that archived Netflix poster or report builder.

The existing `.git` history deliberately retains earlier Netflix work. New revisions are committed honestly; previous commits are not evidence of student authorship. `development_history.bundle` can restore the Git repository with `git clone development_history.bundle Spotify_Project_work`. `docs/submission_details.json` preserves the group data and manual fields.

Before submission, confirm the class section, actual individual contributions and signatures, source/Git link, OneDrive recording link, Turnitin reports, and final PDF filename required by the tutor. See `SUBMISSION_CHECKLIST.md`. The group must personally review the academic claims and code.
