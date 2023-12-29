document.addEventListener("click", function(event) {
    const element = {
      type: "click",
      target: {
        tag: event.target.tagName,
        class: event.target.className,
        id: event.target.id
      }
    };
  
    chrome.runtime.sendMessage({
      action: "logBehavior",
      data: element
    });
  });
  