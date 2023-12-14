chrome.tabs.onActivated.addListener((activeInfo) => {
  const url = chrome.tabs.get(activeInfo.tabId).url;
  const timestamp = Date.now();
  logData({ url, timestamp });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete') {
    const url = tab.url;
    const timestamp = Date.now();
    logData({ url, timestamp });
  }
});

function logData(data) {
  chrome.storage.local.get('log', (result) => {
    const log = result.log || [];
    log.push(data);
    chrome.storage.local.set({ log });
  });
}
