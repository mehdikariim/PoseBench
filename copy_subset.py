import csv, shutil, pathlib, sys

id_file   = "docs/gpcr_target_list.csv"
src_root  = pathlib.Path("data/original")
dst_root  = pathlib.Path("data/test_cases/gpcr_subset")

dst_root.mkdir(parents=True, exist_ok=True)

with open(id_file, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pdb = row["pdb_id"].strip().upper()
        match = next(src_root.rglob(f"{pdb}.pdb"), None)
        if match:
            src_dir = match.parent
            dst_dir = dst_root / pdb
            dst_dir.mkdir(exist_ok=True)
            for file in src_dir.glob("*"):
                if file.suffix.lower() in (".pdb", ".sdf", ".mol", ".mol2"):
                    shutil.copy(file, dst_dir / file.name)
            print(f"copied {pdb}")
        else:
            print(f"NOT found: {pdb}", file=sys.stderr)