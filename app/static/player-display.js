const playerDisplay = document.querySelector("[data-public-state-url]");

function escapeText(value) {
  return String(value ?? "");
}

function clearElement(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}

function appendTextElement(parent, tagName, className, text) {
  const element = document.createElement(tagName);
  if (className) {
    element.className = className;
  }
  element.textContent = escapeText(text);
  parent.appendChild(element);
  return element;
}

function renderScene(sceneRoot, scene) {
  clearElement(sceneRoot);
  if (!scene) {
    appendTextElement(sceneRoot, "p", "eyebrow", "Player Display");
    appendTextElement(sceneRoot, "h1", null, "Aurex Corp VTT");
    appendTextElement(sceneRoot, "p", "muted", "Waiting for public session state.");
    return;
  }

  if (scene.image && scene.image.url) {
    const image = document.createElement("img");
    image.className = "scene-image";
    image.src = scene.image.url;
    image.alt = escapeText(scene.title);
    sceneRoot.appendChild(image);
  }
  appendTextElement(sceneRoot, "p", "eyebrow", "Scene");
  appendTextElement(sceneRoot, "h1", null, scene.title);
  if (scene.description) {
    appendTextElement(sceneRoot, "p", "scene-description", scene.description);
  }
}

function renderTrackerValue(root, tracker) {
  const value = document.createElement("p");
  value.className = "tracker-value";

  if (tracker.display_mode === "label_color") {
    const swatch = document.createElement("span");
    swatch.className = "tracker-color";
    swatch.style.backgroundColor = escapeText(tracker.display?.color);
    value.appendChild(swatch);
    appendTextElement(value, "span", null, tracker.display?.label);
  } else if (tracker.display_mode === "label") {
    value.textContent = escapeText(tracker.display?.label);
  } else if (tracker.display_mode === "number_label") {
    appendTextElement(value, "span", null, tracker.display?.value);
    appendTextElement(value, "span", "tracker-subvalue", tracker.display?.label);
  } else {
    value.textContent = escapeText(tracker.display?.value);
  }

  root.appendChild(value);
}

function renderTrackers(trackersRoot, trackers) {
  clearElement(trackersRoot);
  if (!Array.isArray(trackers) || trackers.length === 0) {
    trackersRoot.hidden = true;
    return;
  }

  trackersRoot.hidden = false;
  for (const tracker of trackers) {
    const article = document.createElement("article");
    article.className = "player-tracker";
    article.dataset.trackerId = escapeText(tracker.id);
    appendTextElement(article, "p", "tracker-label", tracker.label);
    renderTrackerValue(article, tracker);
    trackersRoot.appendChild(article);
  }
}

function setWarningVisible(warning, visible) {
  if (!warning) {
    return;
  }
  warning.hidden = !visible;
}

function preserveScroll(callback) {
  const scrollX = window.scrollX;
  const scrollY = window.scrollY;
  callback();
  window.scrollTo(scrollX, scrollY);
}

function updateCountdown(countdown, seconds) {
  if (countdown) {
    countdown.textContent = String(seconds);
  }
}

function startPlayerRefresh(root) {
  if (!root) {
    return;
  }

  const publicStateUrl = root.dataset.publicStateUrl;
  const intervalMs = Number.parseInt(root.dataset.refreshIntervalMs || "5000", 10);
  const sceneRoot = root.querySelector("[data-player-scene]");
  const trackersRoot = root.querySelector("[data-player-trackers]");
  const warning = root.querySelector("[data-refresh-warning]");
  const countdown = root.querySelector("[data-refresh-countdown]");
  let retryTimer = null;

  function scheduleNextRefresh(delayMs = intervalMs) {
    window.setTimeout(refreshPublicState, delayMs);
  }

  function startRetryCountdown() {
    window.clearInterval(retryTimer);
    let remaining = Math.ceil(intervalMs / 1000);
    updateCountdown(countdown, remaining);
    setWarningVisible(warning, true);
    retryTimer = window.setInterval(() => {
      remaining -= 1;
      updateCountdown(countdown, Math.max(remaining, 0));
      if (remaining <= 0) {
        window.clearInterval(retryTimer);
      }
    }, 1000);
  }

  async function refreshPublicState() {
    try {
      const response = await window.fetch(publicStateUrl, { headers: { Accept: "application/json" } });
      if (!response.ok) {
        throw new Error("Public state request failed.");
      }
      const publicState = await response.json();
      preserveScroll(() => {
        renderScene(sceneRoot, publicState.scene);
        renderTrackers(trackersRoot, publicState.trackers);
      });
      window.clearInterval(retryTimer);
      setWarningVisible(warning, false);
    } catch (error) {
      startRetryCountdown();
    } finally {
      scheduleNextRefresh();
    }
  }

  scheduleNextRefresh();
}

startPlayerRefresh(playerDisplay);
