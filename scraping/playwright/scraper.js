const { chromium } = require('playwright');

const cookies = [
    {
        "name": "access_token",
        "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJmZDcyYTZhMS0yZDk2LTQ2ZWUtOTZlNS02MThmYTQ3MTA0OGUiLCJhY2NvdW50VHlwZSI6ImVtYWlsIiwiaWF0IjoxNzIzMjEzNjEzLCJleHAiOjE3MjU4MDU2MTN9.iu1pnv5BGI26myzTGcHEe7VUWu3CuvcxmxOQ4Tvadek",
        "domain": "zealy.io",
        "path": "/"
    },
    {
        "name": "user_metadata",
        "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJmZDcyYTZhMS0yZDk2LTQ2ZWUtOTZlNS02MThmYTQ3MTA0OGUiLCJpYXQiOjE3MjMyMTM2MTMsImV4cCI6MTcyNTgwNTYxM30.igxE4n7pFuMnUera0lYniO1K23sGyk1zUM1BcFg86BQ",
        "domain": "zealy.io",
        "path": "/"
    }
];

(async () => {
  try {
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();

    context.addCookies(cookies);

    const page = await context.newPage();
    await page.goto('https://zealy.io/my-communities');

    time.sleep(10);
    // console.log('Page title:', await page.title());
    await browser.close();
  } catch (error) {
    console.error('Error launching browser:', error);
  }
})();
