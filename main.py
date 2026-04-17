from pathlib import Path
import shutil

src = Path("/path/to/tms_tiles")
dst = Path("/path/to/xyz_tiles")

for z_dir in src.iterdir():
    if not z_dir.is_dir() or not z_dir.name.isdigit():
        continue
    z = int(z_dir.name)

    for x_dir in z_dir.iterdir():
        if not x_dir.is_dir() or not x_dir.name.isdigit():
            continue
        x = x_dir.name

        for tile in x_dir.glob("*.png"):
            if not tile.stem.isdigit():
                continue
            y_tms = int(tile.stem)
            y_xyz = (1 << z) - 1 - y_tms

            out_dir = dst / str(z) / x
            out_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(tile, out_dir / f"{y_xyz}.png")