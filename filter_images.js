const fs = require('fs');
const path = require('path');

const filePath = process.argv[2];

if (!filePath) {
    console.error('Please provide a file path as an argument. Example: npm run filter-urls dirtyfolder_urls.txt');
    process.exit(1);
}

const fullPath = path.resolve(filePath);

if (!fs.existsSync(fullPath)) {
    console.error(`File not found: ${filePath}`);
    process.exit(1);
}

const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp', '.tiff'];

try {
    const content = fs.readFileSync(fullPath, 'utf8');
    const lines = content.split('\n').filter(line => line.trim() !== '');

    const filteredLines = lines.filter(line => {
        const ext = path.extname(line).toLowerCase();
        return !imageExtensions.includes(ext);
    });

    if (lines.length === filteredLines.length) {
        console.log('No image URLs found to remove.');
    } else {
        const removedCount = lines.length - filteredLines.length;
        fs.writeFileSync(fullPath, filteredLines.join('\n'));
        console.log(`Successfully filtered out ${removedCount} image URLs. Updated ${filePath}.`);
    }

} catch (err) {
    console.error('Error processing file:', err);
}
