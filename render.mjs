// Render design.html to a 1024x1024 entry.png with headless Chrome.
// The PNG is committed to this repository; the grader never runs this
// script, it only runs main.py. Usage: node render.mjs
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const folder = dirname(fileURLToPath(import.meta.url));
const toolsPackage = new URL('../token-radar-tools/package.json', import.meta.url);
const load = createRequire(toolsPackage);
const puppeteer = load('puppeteer-core');

const chromePath = join(
  process.env.HOME,
  'workspace/makefun/token-radar-tools/chrome/linux-157.0.8103.78/chrome-linux64/chrome',
);
const pageUrl = 'file://' + join(folder, 'design.html');
const outPath = join(folder, 'entry.png');

const browser = await puppeteer.launch({
  executablePath: chromePath,
  headless: 'new',
  args: ['--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1024, height: 1024 });
await page.goto(pageUrl, { waitUntil: 'networkidle0', timeout: 30000 });
await new Promise((resolve) => setTimeout(resolve, 400));
await page.screenshot({ path: outPath, type: 'png' });
await browser.close();
console.log('rendered ' + outPath);
