# Netflix Innovation Life Cycle and Movie Discovery Assistant

LDCW6123, Trimester 2620, Group 13. Group leader: Aziel Tan Zheng Chuan (261UC240LY).

Part 1 examines Netflix DVD-by-mail and its competition with physical video rental stores using Christensen's disruptive innovation model. Part 2 is an offline C++17 movie discovery demonstration with a fictional catalogue. It uses transparent rules, rather than Netflix's proprietary recommendation algorithm.

## Build and run

From this project directory, with a C++17 compiler installed:

```sh
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o movie_assistant
./movie_assistant
```

On Windows with MinGW, use `-o movie_assistant.exe`, then run `movie_assistant.exe` in Command Prompt or `./movie_assistant.exe` in PowerShell.

Select genre (1-3), mood (1-3) and duration (1-2). The programme recommends a title, describes it, explains the actual matches, and offers another search. Whole-line validation rejects text, decimals, trailing letters, blank entries and out-of-range numbers. EOF exits cleanly.

Genre is required. Mood adds two points, duration adds one point. Equal scores select the first title in catalogue order. No mood or duration match is guaranteed; the output explains only preferences actually matched. A missing genre in a future catalogue is handled without dereferencing a null pointer.

## Reproduce the tests

Python 3 and a C++17 compiler are needed for automated tests; Python is not needed to run the programme itself.

```sh
sh test.sh
```

Or on Windows:

```sh
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o movie_assistant.exe
python tests/test_program.py movie_assistant.exe
```

There are 35 checks. `assets/test_results.csv` contains individual input, expected result, actual result and status. The test script rewrites the results when run. The demo transcript is `assets/program_output.txt`; the invalid-input example is `assets/invalid_output.txt`.

## Restore and continue the actual Git history

```sh
git clone development_history.bundle Netflix_Project_work
cd Netflix_Project_work
git log --oneline --graph --all
```

The supplied history records AI-assisted preparation and revision. It is not evidence of student authorship. Each member should review the content, make genuine changes where needed, test them and commit their own real work. Do not rename previous commit authors or create misleading backdated commits. After changes, regenerate the report's Git log and evidence.

```sh
git add src/main.cpp
git commit -m "Describe the actual change made"
git log --oneline --graph --all > assets/git_history.txt
git bundle create development_history.bundle --all
```

## Contents

- `src/main.cpp`: the programme.
- `tests/test_program.py` and `test.sh`: reproducible checks.
- `assets/`: updated source, programme-output, Git and test evidence.
- `docs/`: report, poster, cover/declarations, references, presentation and editable submission details.
- `PRESENTATION_SCRIPT.md`: complete six-person recording script.
- `AI_DISCLOSURE.txt`: assistance disclosure.
- `SUBMISSION_CHECKLIST.md`: outstanding personal and upload actions.
- `tools/`: reproducible document and evidence builders, when included.

The final PDF must contain a working OneDrive video link and a working source-code/Git-history link. Signatures, declarations of personal contribution, recording and Turnitin reports must be supplied by the group. See the checklist before submission.
