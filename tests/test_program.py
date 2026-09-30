#!/usr/bin/env python3
"""Black-box regression checks with explicit expected outcomes."""
import csv
import subprocess
import sys
from pathlib import Path

binary = str(Path(sys.argv[1]).resolve())
root = Path(__file__).resolve().parents[1]
results = []

def run(data):
    p = subprocess.run([binary], input=data, capture_output=True, text=True, timeout=3)
    assert p.returncode == 0, p.stderr
    return p.stdout

def record(name, inputs, expected, actual, passed):
    results.append([name, inputs, expected, actual, "PASS" if passed else "FAIL"])
    assert passed, (name, expected, actual)

cases = [
    (1,1,1,"Orbit Station"), (1,1,2,"Tomorrow's Signal"),
    (1,2,1,"Neon Run"), (1,2,2,"Tomorrow's Signal"),
    (1,3,1,"Orbit Station"), (1,3,2,"The Last Satellite"),
    (2,1,1,"Summer Market"), (2,1,2,"Coffee and Clouds"),
    (2,2,1,"Weekend Mix-Up"), (2,2,2,"The Accidental Chef"),
    (2,3,1,"Summer Market"), (2,3,2,"The Accidental Chef"),
    (3,1,1,"Crossing Paths"), (3,1,2,"Crossing Paths"),
    (3,2,1,"Night Shift"), (3,2,2,"Night Shift"),
    (3,3,1,"River Letters"), (3,3,2,"The Long Road Home"),
]
for i,(g,m,l,title) in enumerate(cases,1):
    out=run(f"{g}\n{m}\n{l}\n2\n")
    actual=out.split("Recommendation: ")[1].split(" (")[0]
    record(f"C{i:02}",f"{g}, {m}, {l}; exit 2",title,actual,actual==title)

invalid=["wrong","0","4","-1","1abc","1.5","", "999999999999999999999"]
for i,entry in enumerate(invalid,1):
    out=run(entry+"\n1\n3\n1\n2\n")
    passed="Please enter a whole number from 1 to 3." in out and "Recommendation: Orbit Station" in out
    record(f"I{i:02}",repr(entry)+"; then 1,3,1,2","Reject and recover","Rejected and recovered" if passed else out,passed)

for i,data in enumerate(["", "1\n", "1\n3\n", "1\n3\n1\n"],1):
    out=run(data)
    record(f"E{i:02}",repr(data),"Clean EOF exit","Clean EOF exit" if "Input ended. Goodbye." in out else out,"Input ended. Goodbye." in out)

out=run("2\n1\n2\n1\n1\n2\n1\n2\n")
passed=out.count("Recommendation:")==2 and "Coffee and Clouds" in out and "Neon Run" in out and "Thanks for exploring." in out
record("R01","2,1,2,1; 1,2,1,2","Two recommendations and normal exit","Two recommendations and normal exit" if passed else out,passed)

out=run("  1  \n3\n1\n2\n")
record("W01","spaces around 1; then 3,1,2","Accept surrounding spaces","Orbit Station" if "Recommendation: Orbit Station" in out else out,"Recommendation: Orbit Station" in out)

out=run("1\n3\n3\n1\n7\n2\n")
passed="Please enter a whole number from 1 to 2." in out and "Recommendation: Orbit Station" in out and "Thanks for exploring." in out
record("B01","invalid length 3 and repeat 7","Reject at both menus and recover","Rejected at both menus" if passed else out,passed)

out=run("1\n1\n1\n2\n")
why=out.split("Why: ")[1].split("\n")[0]
passed="Relaxed" not in why and "length preference" in why
record("F01","Sci-Fi, Relaxed, short","Fallback does not claim a mood match",why,passed)

out=run("3\n2\n1\n2\n")
why=out.split("Why: ")[1].split("\n")[0]
passed="Night Shift" in out and "Exciting mood" in why and "length preference" not in why
record("P01","Drama, Exciting, short","Mood priority; no false length claim",why,passed)

(root/"assets").mkdir(exist_ok=True)
with (root/"assets/test_results.csv").open("w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Case","Input","Expected","Actual","Status"])
    writer.writerows(results)
summary=f"{len(results)} black-box checks passed: 18 preference combinations, 8 invalid inputs, 4 EOF cases, repeat, whitespace, menu bounds, fallback and mood priority.\n"
(root/"assets/test_summary.txt").write_text(summary)
print(summary,end="")
