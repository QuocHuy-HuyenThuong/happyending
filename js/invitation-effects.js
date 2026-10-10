(function () {
  const mapUrl = "https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3733.214096009219!2d105.903496!3d20.660867!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMjDCsDM5JzM5LjEiTiAxMDXCsDU0JzEyLjYiRQ!5e0!3m2!1svi!2s!4v1791613159006!5m2!1svi!2s";

  function replaceMapUrl(frame) {
    if (frame.src.includes("maps/embed/v1/place") && frame.src !== mapUrl) {
      frame.src = mapUrl;
    }
  }

  function scan(node) {
    if (node instanceof HTMLIFrameElement) replaceMapUrl(node);
    node.querySelectorAll?.("iframe").forEach(replaceMapUrl);
  }

  document.querySelectorAll("iframe").forEach(replaceMapUrl);

  new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type === "attributes") replaceMapUrl(mutation.target);
      else mutation.addedNodes.forEach(scan);
    }
  }).observe(document, {
    childList: true,
    subtree: true,
    attributes: true,
    attributeFilter: ["src"]
  });
})();
