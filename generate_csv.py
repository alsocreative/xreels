import os
import csv
import urllib.parse

base_url = "https://gitlab.com/SH20RAJ/xreels/-/raw/main/"

files = []
# Walk specifically in the reels directory
for root, dirs, filenames in os.walk('reels'):
    for filename in filenames:
        if filename.endswith('.mp4'):
            # Get path relative to the current working directory (which should be the repo root)
            rel_dir = os.path.relpath(root, '.')
            rel_path = os.path.join(rel_dir, filename)
            # Ensure forward slashes for URLs even on Windows (though user is on Mac)
            rel_path_fwd = rel_path.replace(os.sep, '/')
            files.append(rel_path_fwd)

# Sort for consistent order
files.sort()

with open('reels.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['sno', 'caption', 'videoUrl', 'uploaded']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for idx, f in enumerate(files, start=1):
        # Construct URL. We do NOT quote the path parts because the user requested "raw urls"
        # and standard web servers might handle spaces/chars, but typically in this repo format 
        # based on the example, simple concatenation is expected. 
        # Example: reels/dirtyrepub/dirty_myne... -> https://gitlab.../reels/dirtyrepub/...
        # User example does NOT show url encoding (e.g. %20), so we will concatenate directly.
        url = base_url + f
        
        writer.writerow({
            'sno': idx,
            'caption': '', # Empty by default
            'videoUrl': url,
            'uploaded': 'FALSE'
        })

print(f"Generated reels.csv with {len(files)} entries.")
