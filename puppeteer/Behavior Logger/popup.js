document.getElementById('download-log').addEventListener('click', () => {
    chrome.storage.local.get('log', (result) => {
      const log = result.log;
      const data = JSON.stringify(log);
      const blob = new Blob([data], { type: 'application/json' });
      const filename = 'app.log';
      chrome.downloads.download({ url: window.URL.createObjectURL(blob), filename });
    });
  });
  