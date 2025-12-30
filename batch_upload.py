import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e}")
        sys.exit(1)

def main():
    BATCH_SIZE = 100
    files_to_add = []

    # 1. Collect all video files, ensuring folder-wise order
    print("Scanning for files...")
    for root, dirs, filenames in os.walk('reels'):
        # sort filenames to ensure consistent order within folder
        filenames.sort() 
        for filename in filenames:
            if filename.endswith('.mp4'):
                full_path = os.path.join(root, filename)
                files_to_add.append(full_path)
    
    # Sort by path to ensure folder-wise grouping
    files_to_add.sort()
    
    total_files = len(files_to_add)
    print(f"Found {total_files} video files.")

    # 2. Process in batches
    for i in range(0, total_files, BATCH_SIZE):
        batch = files_to_add[i:i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = (total_files + BATCH_SIZE - 1) // BATCH_SIZE
        
        print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} files)...")
        
        # Git add
        # Escape spaces if necessary, but subprocess with shell=True handles quotes if we prepare them
        # Safer: use git add with list of files. 
        # Construct command carefully.
        quoted_files = [f'"{f}"' for f in batch]
        add_cmd = f"git add {' '.join(quoted_files)}"
        run_command(add_cmd)
        
        # Git commit
        commit_msg = f"chore: add video batch {batch_num}/{total_batches}"
        run_command(f'git commit -m "{commit_msg}"')
        
        # Git push
        print("Pushing batch...")
        run_command("git push")
        
    print("All batches completed successfully.")

if __name__ == "__main__":
    main()
