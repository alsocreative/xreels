const fs = require('fs');
const path = require('path');

const directory = process.argv[2];

if (!directory) {
    console.error('Please provide a directory path as an argument. Example: npm run generate-urls reels/absotutecinema');
    process.exit(1);
}

const fullPath = path.resolve(directory);

if (!fs.existsSync(fullPath)) {
    console.error(`Directory not found: ${directory}`);
    process.exit(1);
}

const baseUrl = 'https://cdn.jsdelivr.net/gh/alsocreative/xreels@main/';
const folderName = path.basename(fullPath);
const outputFileName = `${folderName}_urls.txt`;

try {
    const files = fs.readdirSync(fullPath);
    const allFiles = files.filter(file => !file.startsWith('.')); // Exclude hidden files like .DS_Store

    if (allFiles.length === 0) {
        console.log('No files found in the directory.');
        process.exit(0);
    }

    // Ensure we use forward slashes for the URL path
    // We use the directory argument provided by the user to build the URL path
    const urlPath = directory.split(path.sep).join('/');

    // Remove leading/trailing slashes to ensure clean URL concatenation
    const cleanUrlPath = urlPath.replace(/^\/+|\/+$/g, '');

    const urls = allFiles.map(file => {
        return `${baseUrl}${cleanUrlPath}/${file}`;
    });

    fs.writeFileSync(outputFileName, urls.join('\n'));
    console.log(`Successfully created ${outputFileName} with ${urls.length} URLs.`);

} catch (err) {
    console.error('Error processing directory:', err);
}
