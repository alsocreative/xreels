# Dopa Meme Project

This project contains scripts to manage media files and generate URL lists for JSDelivr.

## Scripts

### 1. Generate URLs
Generates a text file containing JSDelivr URLs for all files in a specified directory.

**Usage:**
```bash
npm run generate-urls <directory_path>
```
**Example:**
```bash
npm run generate-urls reels/dirtyfolder
```
This will create a file named `dirtyfolder_urls.txt` containing URLs for all files in that directory.

### 2. Filter URLs
Filters out image files (jpg, png, etc.) from a generated URL list text file. This modifies the file in place.

**Usage:**
```bash
npm run filter-urls <file_path>
```
**Example:**
```bash
npm run filter-urls dirtyfolder_urls.txt
```
This will remove all image URLs from `dirtyfolder_urls.txt`.
