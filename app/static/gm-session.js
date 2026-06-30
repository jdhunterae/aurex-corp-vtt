function showDuplicateWarning(form, asset) {
  let warning = form.querySelector(".duplicate-warning");
  if (!warning) {
    warning = document.createElement("p");
    warning.className = "duplicate-warning";
    form.insertBefore(warning, form.querySelector("button"));
  }
  warning.textContent = `This appears to match ${asset.display_name} (${asset.id}). Choose whether to reuse it or keep a separate copy, then submit again.`;
}

async function previewUpload(form) {
  const fileInput = form.querySelector('input[name="image"]');
  if (!fileInput || !fileInput.files.length) {
    return null;
  }
  const data = new FormData();
  data.append("image", fileInput.files[0]);
  const response = await fetch(form.dataset.previewUrl, { method: "POST", body: data });
  if (!response.ok) {
    return null;
  }
  return response.json();
}

async function previewDownload(form) {
  const urlInput = form.querySelector('input[name="url"]');
  if (!urlInput || !urlInput.value) {
    return null;
  }
  const response = await fetch(form.dataset.previewUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url: urlInput.value }),
  });
  if (!response.ok) {
    return null;
  }
  return response.json();
}

function attachDuplicatePreview(selector, previewFn) {
  const form = document.querySelector(selector);
  if (!form) {
    return;
  }
  form.addEventListener("submit", async (event) => {
    if (form.dataset.duplicateAcknowledged === "true") {
      return;
    }
    event.preventDefault();
    const result = await previewFn(form);
    if (result && result.duplicate) {
      form.dataset.duplicateAcknowledged = "true";
      showDuplicateWarning(form, result.duplicate);
      return;
    }
    form.dataset.duplicateAcknowledged = "true";
    form.submit();
  });
}

attachDuplicatePreview(".asset-upload-form", previewUpload);
attachDuplicatePreview(".asset-download-form", previewDownload);
