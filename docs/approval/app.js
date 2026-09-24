"use strict";

const OWNER = "lionsprideemb-tech";
const REPO = "Pokemon-moves";
const BRANCH = "main";
const RAW = "https://raw.githubusercontent.com/" + OWNER + "/" + REPO + "/" + BRANCH + "/";
const GITHUB = "https://github.com/" + OWNER + "/" + REPO;
const STORAGE_KEY = "pokemon-moves-approval-v1";

const animationManifests = [
  "manifests/ELITE_REDUX_DS_ANIMATION_PASS_01.csv",
  "manifests/VANGUARD_DS_ANIMATION_PASS_02.csv",
  "manifests/REJUVENATION_DS_ANIMATION_PASS_03.csv",
  "manifests/REBORN_DS_ANIMATION_PASS_04.csv",
  "manifests/URANIUM_DS_ANIMATION_PASS_05.csv",
  "manifests/INSURGENCE_DS_ANIMATION_PASS_06.csv",
  "manifests/CLOVER_DS_ANIMATION_PASS_07.csv",
  "manifests/OPALO_DS_ANIMATION_PASS_08.csv",
  "manifests/SAGE_DS_ANIMATION_PASS_09.csv",
  "manifests/UNTAMED_DS_ANIMATION_PASS_10.csv",
  "manifests/ARMONIA_DS_ANIMATION_PASS_11.csv"
];

const state = {
  moves: [],
  filtered: [],
  selectedId: null,
  reviews: loadReviews(),
  previews: {},
  auditDetails: {},
  translations: {},
  filters: {
    search: "",
    source: "",
    type: "",
    category: "",
    animation: "",
    review: "",
    sort: "name"
  }
};

const el = {};

document.addEventListener("DOMContentLoaded", init);

async function init() {
  cacheElements();
  bindEvents();
  setLoading(true);

  try {
    const masterText = await fetchText(RAW + "manifests/community_moves.csv");
    const masterRows = csvToObjects(masterText);

    const manifestResults = await Promise.all(
      animationManifests.map(async function(path) {
        try {
          const txt = await fetchText(RAW + path);
          return { path: path, rows: csvToObjects(txt) };
        } catch (err) {
          return { path: path, rows: [], error: String(err) };
        }
      })
    );

    const animById = {};
    manifestResults.forEach(function(result) {
      result.rows.forEach(function(row) {
        if (!row.move_id) return;
        animById[row.move_id] = Object.assign({}, animById[row.move_id] || {}, row, {
          animation_manifest_path: result.path
        });
      });
    });

    try {
      const previewData = await fetchJson("./previews.json");
      state.previews = previewData.moves || {};
    } catch (err) {
      state.previews = {};
    }

    try {
      const auditData = await fetchJson("./audit_details.json");
      state.auditDetails = auditData.moves || {};
    } catch (err) {
      state.auditDetails = {};
    }

    try {
      const translationData = await fetchJson("./translations.json");
      state.translations = translationData.moves || {};
    } catch (err) {
      state.translations = {};
    }

    state.moves = masterRows.map(function(row) {
      const overlay = animById[row.move_id] || {};
      const audit = state.auditDetails[row.move_id] || {};
      const translation = state.translations[row.move_id] || {};
      return normalizeMove(row, overlay, audit, translation);
    });

    buildFilterOptions();
    applyFilters();

    const hashId = decodeURIComponent((location.hash || "").replace(/^#/, ""));
    const preferred = state.moves.some(function(m) { return m.move_id === hashId; }) ? hashId : null;
    selectMove(preferred || (state.filtered[0] && state.filtered[0].move_id));
    updateDashboard();
  } catch (err) {
    showFatal(err);
  } finally {
    setLoading(false);
  }
}

function cacheElements() {
  [
    "totalCount","reviewedCount","approvedCount","animationApprovedCount","remainingCount",
    "progressText","progressBar","searchInput","sourceFilter","typeFilter","categoryFilter",
    "animationFilter","reviewFilter","sortSelect","visibleCount","moveList","detailPanel",
    "emptyState","moveDetail","prevBtn","nextBtn","positionText","sourceBadge","moveName",
    "moveId","typePill","categoryPill","mechanicsAuditBadge","coreGrid","effectsGrid",
    "sourceGrid","animationStateBadge","animationPreview","animationGrid","animationLinks",
    "reviewNotes","saveState","exportJsonBtn","exportCsvBtn","importInput"
  ].forEach(function(id) { el[id] = document.getElementById(id); });
}

function bindEvents() {
  el.searchInput.addEventListener("input", function(e) {
    state.filters.search = e.target.value.trim().toLowerCase();
    applyFilters();
  });
  el.sourceFilter.addEventListener("change", filterHandler("source"));
  el.typeFilter.addEventListener("change", filterHandler("type"));
  el.categoryFilter.addEventListener("change", filterHandler("category"));
  el.animationFilter.addEventListener("change", filterHandler("animation"));
  el.reviewFilter.addEventListener("change", filterHandler("review"));
  el.sortSelect.addEventListener("change", function(e) {
    state.filters.sort = e.target.value;
    applyFilters();
  });

  el.moveList.addEventListener("click", function(e) {
    const button = e.target.closest("[data-move-id]");
    if (button) selectMove(button.dataset.moveId);
  });

  el.prevBtn.addEventListener("click", function() { moveSelection(-1); });
  el.nextBtn.addEventListener("click", function() { moveSelection(1); });

  document.querySelectorAll(".segmented").forEach(function(group) {
    group.addEventListener("click", function(e) {
      const button = e.target.closest("button[data-value]");
      if (!button || !state.selectedId) return;
      const kind = group.dataset.group;
      const review = getReview(state.selectedId);
      if (kind === "move") review.move = button.dataset.value;
      if (kind === "animation") review.animation = button.dataset.value;
      review.updated_at = new Date().toISOString();
      state.reviews[state.selectedId] = review;
      saveReviews();
      renderReviewControls();
      renderMoveList();
      updateDashboard();
    });
  });

  let noteTimer = null;
  el.reviewNotes.addEventListener("input", function(e) {
    if (!state.selectedId) return;
    const review = getReview(state.selectedId);
    review.notes = e.target.value;
    review.updated_at = new Date().toISOString();
    state.reviews[state.selectedId] = review;
    clearTimeout(noteTimer);
    el.saveState.textContent = "Saving…";
    noteTimer = setTimeout(function() {
      saveReviews();
      el.saveState.textContent = "Saved automatically on this device.";
      renderMoveList();
      updateDashboard();
    }, 250);
  });

  el.exportJsonBtn.addEventListener("click", exportReviewsJson);
  el.exportCsvBtn.addEventListener("click", exportReviewsCsv);
  el.importInput.addEventListener("change", importReviews);
}

function filterHandler(key) {
  return function(e) {
    state.filters[key] = e.target.value;
    applyFilters();
  };
}

async function fetchText(url) {
  const response = await fetch(url, { cache: "no-store" });
  if (!response.ok) throw new Error("Could not load " + url + " (" + response.status + ")");
  return response.text();
}

async function fetchJson(url) {
  const response = await fetch(url, { cache: "no-store" });
  if (!response.ok) throw new Error("Could not load " + url);
  return response.json();
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let value = "";
  let quoted = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') {
        value += '"';
        i++;
      } else if (ch === '"') {
        quoted = false;
      } else {
        value += ch;
      }
    } else {
      if (ch === '"') {
        quoted = true;
      } else if (ch === ",") {
        row.push(value);
        value = "";
      } else if (ch === "\n") {
        row.push(value.replace(/\r$/, ""));
        rows.push(row);
        row = [];
        value = "";
      } else {
        value += ch;
      }
    }
  }

  if (value.length || row.length) {
    row.push(value.replace(/\r$/, ""));
    rows.push(row);
  }
  return rows;
}

function csvToObjects(text) {
  const rows = parseCsv(text);
  if (!rows.length) return [];
  const headers = rows[0];
  return rows.slice(1).filter(function(row) {
    return row.some(function(v) { return String(v || "").trim() !== ""; });
  }).map(function(row) {
    const obj = {};
    headers.forEach(function(h, i) { obj[h] = row[i] == null ? "" : row[i]; });
    return obj;
  });
}

function normalizeMove(row, overlay, audit, translation) {
  const animationReference = overlay.source_animation_reference ||
    overlay.source_animation_evidence ||
    row.animation_reference || "";

  const animationClass = overlay.ds_animation_class || row.animation_status || "";
  const animationPath = overlay.ds_animation_path || "";
  const dsMoveId = overlay.ds_move_id || "";

  const translatedName = translation.english_name || row.move_name || row.move_id;
  const originalName = translation.original_name || row.move_name || "";

  return Object.assign({}, row, {
    display_name: translatedName,
    original_move_name: originalName,
    name_translation_status: translation.english_name ? "English review translation" : "Source name already used",
    source_animation_reference_audit: animationReference,
    secondary_implementation_evidence: overlay.secondary_implementation_evidence || "",
    ds_animation_class: animationClass,
    ds_animation_path: animationPath,
    ds_move_id: dsMoveId,
    port_action: overlay.port_action || row.ds_portability || "",
    animation_audit_notes: overlay.notes || "",
    animation_manifest_path: overlay.animation_manifest_path || "",
    audit: audit,
    animation_bucket: animationBucket(animationClass, animationReference, animationPath, row.animation_status)
  });
}

function animationBucket(cls, ref, path, original) {
  const all = [cls, ref, path, original].join(" ").toLowerCase();
  if (all.includes("direct hg-engine ds reuse") || all.includes("platinum/base-era ds reuse")) return "DS reuse assigned";
  if (all.includes("cross-engine") || all.includes("gba animation") || all.includes("source-mapped")) return "Source animation needs DS port";
  if (all.includes("explicitly reuses") || /^move_/i.test(ref || "")) return "Referenced animation assigned";
  if (all.includes("no source animation") || all.includes("no battle-animation") || all.includes("mechanics only")) return "No source animation";
  if (all.includes("pending") || all.includes("no direct")) return "Animation selection pending";
  if (ref || path) return "Animation reference available";
  return "Animation selection pending";
}

function buildFilterOptions() {
  fillSelect(el.sourceFilter, unique(state.moves.map(function(m) { return m.source_project; })));
  fillSelect(el.typeFilter, unique(state.moves.map(function(m) { return m.type; })));
  fillSelect(el.animationFilter, unique(state.moves.map(function(m) { return m.animation_bucket; })));
}

function fillSelect(select, values) {
  values.filter(Boolean).sort(localeSort).forEach(function(value) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.appendChild(option);
  });
}

function unique(values) {
  return Array.from(new Set(values));
}

function localeSort(a, b) {
  return String(a).localeCompare(String(b), undefined, { sensitivity: "base" });
}

function applyFilters() {
  const f = state.filters;
  state.filtered = state.moves.filter(function(m) {
    const searchBlob = [
      m.display_name,m.original_move_name,m.move_name,m.move_id,m.source_project,m.type,m.category,m.primary_effect,
      m.secondary_effect,m.tags,m.animation_reference,m.source_animation_reference_audit,
      m.ds_animation_class,m.ds_animation_path,m.notes
    ].join(" ").toLowerCase();

    if (f.search && !searchBlob.includes(f.search)) return false;
    if (f.source && m.source_project !== f.source) return false;
    if (f.type && m.type !== f.type) return false;
    if (f.category && m.category !== f.category) return false;
    if (f.animation && m.animation_bucket !== f.animation) return false;
    if (f.review && !matchesReviewFilter(m.move_id, f.review)) return false;
    return true;
  });

  sortFiltered();
  renderMoveList();
  el.visibleCount.textContent = state.filtered.length + " moves";

  if (state.selectedId && !state.filtered.some(function(m) { return m.move_id === state.selectedId; })) {
    selectMove(state.filtered[0] ? state.filtered[0].move_id : null);
  } else {
    updatePosition();
  }
}

function sortFiltered() {
  const sort = state.filters.sort;
  state.filtered.sort(function(a, b) {
    if (sort === "source") {
      return localeSort(a.source_project, b.source_project) || localeSort(a.display_name, b.display_name);
    }
    if (sort === "type") {
      return localeSort(a.type, b.type) || localeSort(a.display_name, b.display_name);
    }
    if (sort === "review") {
      return reviewRank(a.move_id) - reviewRank(b.move_id) || localeSort(a.display_name, b.display_name);
    }
    return localeSort(a.display_name, b.display_name);
  });
}

function reviewRank(id) {
  const r = getReview(id);
  const complete = r.move !== "unreviewed" && r.animation !== "unreviewed";
  if (complete) return 3;
  if (r.move !== "unreviewed" || r.animation !== "unreviewed" || r.notes) return 2;
  return 1;
}

function matchesReviewFilter(id, filter) {
  const r = getReview(id);
  if (filter === "unreviewed") return r.move === "unreviewed" || r.animation === "unreviewed";
  if (filter === "move-approved") return r.move === "approved";
  if (filter === "move-revise") return r.move === "revise";
  if (filter === "move-reject") return r.move === "reject";
  if (filter === "animation-approved") return r.animation === "approved";
  if (filter === "animation-change") return r.animation === "change";
  if (filter === "fully-reviewed") return r.move !== "unreviewed" && r.animation !== "unreviewed";
  return true;
}

function renderMoveList() {
  el.moveList.innerHTML = "";
  if (!state.filtered.length) {
    const div = document.createElement("div");
    div.className = "preview-placeholder";
    div.innerHTML = "<strong>No moves match these filters.</strong>Clear a filter or search term.";
    el.moveList.appendChild(div);
    return;
  }

  const frag = document.createDocumentFragment();
  state.filtered.forEach(function(m) {
    const r = getReview(m.move_id);
    const button = document.createElement("button");
    button.className = "move-row" + (state.selectedId === m.move_id ? " active" : "");
    button.dataset.moveId = m.move_id;

    const left = document.createElement("div");
    const name = document.createElement("div");
    name.className = "move-row-name";
    name.textContent = m.display_name || m.move_name || m.move_id;
    const meta = document.createElement("div");
    meta.className = "move-row-meta";
    meta.textContent = [m.type, m.category, shortSource(m.source_project)].filter(Boolean).join(" • ");
    left.appendChild(name);
    left.appendChild(meta);

    const dot = document.createElement("span");
    dot.className = "review-dot " + dotState(r);
    dot.title = reviewSummary(r);

    button.appendChild(left);
    button.appendChild(dot);
    frag.appendChild(button);
  });
  el.moveList.appendChild(frag);
}

function shortSource(source) {
  return String(source || "")
    .replace("Pokemon ", "")
    .replace("Pokémon ", "")
    .replace(/ \(.+$/, "");
}

function dotState(r) {
  if (r.move === "reject" || r.move === "revise" || r.animation === "change") return "problem";
  if (r.move !== "unreviewed" && r.animation !== "unreviewed") return "complete";
  if (r.move !== "unreviewed" || r.animation !== "unreviewed" || r.notes) return "partial";
  return "";
}

function reviewSummary(r) {
  return "Move: " + r.move + " | Animation: " + r.animation;
}

function selectMove(id) {
  state.selectedId = id || null;
  renderMoveList();

  if (!id) {
    el.emptyState.classList.remove("hidden");
    el.moveDetail.classList.add("hidden");
    history.replaceState(null, "", location.pathname + location.search);
    return;
  }

  const move = state.moves.find(function(m) { return m.move_id === id; });
  if (!move) return;

  el.emptyState.classList.add("hidden");
  el.moveDetail.classList.remove("hidden");
  history.replaceState(null, "", "#" + encodeURIComponent(id));

  renderMove(move);
  updatePosition();

  if (window.innerWidth <= 820) {
    el.detailPanel.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function moveSelection(delta) {
  if (!state.filtered.length || !state.selectedId) return;
  const idx = state.filtered.findIndex(function(m) { return m.move_id === state.selectedId; });
  const next = Math.max(0, Math.min(state.filtered.length - 1, idx + delta));
  selectMove(state.filtered[next].move_id);
}

function updatePosition() {
  if (!state.selectedId || !state.filtered.length) {
    el.positionText.textContent = "";
    return;
  }
  const idx = state.filtered.findIndex(function(m) { return m.move_id === state.selectedId; });
  el.positionText.textContent = idx >= 0 ? (idx + 1) + " of " + state.filtered.length : "";
  el.prevBtn.disabled = idx <= 0;
  el.nextBtn.disabled = idx < 0 || idx >= state.filtered.length - 1;
}

function renderMove(m) {
  el.sourceBadge.textContent = m.source_project || "Unknown source";
  el.moveName.textContent = m.display_name || m.move_name || m.move_id;
  el.moveId.textContent = m.move_id || "";
  setPill(el.typePill, m.type || "Unknown", "type-" + slug(m.type));
  setPill(el.categoryPill, m.category || "Unknown", "");

  const auditStatus = m.audit ? String(m.audit.status || "").toLowerCase() : "";
  const auditComplete = auditStatus === "complete";
  const auditLabel = auditComplete
    ? "Full mechanics audit complete"
    : auditStatus === "source-limited"
      ? "Blocked: exact source mechanics missing"
      : auditStatus === "source-conflict"
        ? "Blocked: source mechanics conflict"
        : "Full mechanics audit pending";
  el.mechanicsAuditBadge.textContent = auditLabel;
  el.mechanicsAuditBadge.style.borderColor = auditComplete ? "#22c55e" : "#ef4444";

  renderGrid(el.coreGrid, [
    ["English review name", displayValue(m.display_name)],
    ["Original source name", displayValue(m.original_move_name)],
    ["Power", displayValue(m.power)],
    ["Accuracy", displayAccuracy(m.accuracy)],
    ["PP", displayValue(m.pp)],
    ["Type", displayValue(m.type)],
    ["Category", displayValue(m.category)],
    ["Tags / flags", displayValue(m.tags)]
  ]);

  const effects = [
    ["What it does", plainEnglishEffect(m), true]
  ];

  const primarySourceEffect = cleanEffectText(m.primary_effect);
  const secondarySourceEffect = cleanEffectText(m.secondary_effect);
  if (primarySourceEffect && !isInternalEffectText(m.primary_effect) && primarySourceEffect !== plainEnglishEffect(m)) {
    effects.push(["Source catalog effect", primarySourceEffect, true]);
  }
  if (secondarySourceEffect && !isInternalEffectText(m.secondary_effect)) {
    effects.push(["Source catalog secondary effect", secondarySourceEffect, true]);
  }

  if (m.audit && Object.keys(m.audit).length) {
    Object.keys(m.audit).forEach(function(key) {
      if (["status","notes","move_description","effect_text"].includes(key)) return;
      effects.push([prettyKey(key), displayValue(m.audit[key]), String(m.audit[key] || "").length > 80]);
    });
    if (m.audit.move_description) effects.splice(1, 0, ["Move description", m.audit.move_description, true]);
    if (m.audit.notes) effects.push(["Detailed audit notes", m.audit.notes, true]);
  } else {
    effects.push([
      "Detailed mechanics audit",
      "Pending full source verification. This move should not be treated as ready for approval until its effect, priority, targeting, flags, status/stat changes, multihit rules, recoil/drain, switching behavior, and field interactions are written out in plain English.",
      true
    ]);
  }
  renderGrid(el.effectsGrid, effects);

  renderGrid(el.sourceGrid, [
    ["Repository", displayValue(m.source_repo)],
    ["Pinned commit", displayValue(m.source_commit)],
    ["Source data path", displayValue(m.source_data_path), true],
    ["License status", displayValue(m.source_license_status)],
    ["DS portability", displayValue(m.ds_portability), true],
    ["Source notes", displayValue(m.notes), true]
  ]);

  renderAnimation(m);
  renderReviewControls();
}

function renderAnimation(m) {
  el.animationStateBadge.textContent = m.animation_bucket;
  el.animationStateBadge.style.borderColor = animationBadgeColor(m.animation_bucket);

  const assigned = assignedAnimation(m);
  renderGrid(el.animationGrid, [
    ["Assigned / referenced animation", assigned, true],
    ["Source animation status", displayValue(m.animation_status), true],
    ["Animation audit class", displayValue(m.ds_animation_class), true],
    ["DS animation path", displayValue(m.ds_animation_path)],
    ["DS move ID", displayValue(m.ds_move_id)],
    ["Port action", displayValue(m.port_action), true],
    ["Animation audit evidence", displayValue(m.source_animation_reference_audit), true],
    ["Animation audit notes", displayValue(m.animation_audit_notes), true]
  ]);

  renderPreview(m);
  renderAnimationLinks(m);
}

function assignedAnimation(m) {
  if (m.ds_animation_path) {
    return (m.animation_reference || m.source_animation_reference_audit || "DS animation") +
      " → " + m.ds_animation_path;
  }
  if (m.source_animation_reference_audit) return m.source_animation_reference_audit;
  if (m.animation_reference) return m.animation_reference;
  if (m.animation_bucket === "No source animation") return "No source animation assigned";
  return "Pending animation selection";
}

function renderPreview(m) {
  el.animationPreview.innerHTML = "";
  const preview = state.previews[m.move_id];

  if (preview && preview.url) {
    const url = preview.url;
    if ((preview.type || "").toLowerCase() === "video" || /\.(mp4|webm)$/i.test(url)) {
      const video = document.createElement("video");
      video.controls = true;
      video.loop = true;
      video.muted = true;
      video.playsInline = true;
      video.src = url;
      video.setAttribute("aria-label", (m.display_name || m.move_name || m.move_id) + " animation preview");
      el.animationPreview.appendChild(video);
    } else {
      const img = document.createElement("img");
      img.src = url;
      img.alt = (m.display_name || m.move_name || m.move_id) + " animation preview";
      el.animationPreview.appendChild(img);
    }
    if (preview.caption) {
      const caption = document.createElement("div");
      caption.className = "preview-caption";
      caption.textContent = preview.caption;
      el.animationPreview.appendChild(caption);
    }
    return;
  }

  const wrap = document.createElement("div");
  wrap.className = "preview-placeholder";
  const title = document.createElement("strong");
  const body = document.createElement("span");

  if (m.ds_animation_path) {
    title.textContent = "DS animation assigned — visual capture pending";
    body.textContent = "The exact hg-engine/DS script is linked below. A GIF/video preview can be dropped into previews.json when rendered.";
  } else if (m.animation_reference || m.source_animation_reference_audit) {
    title.textContent = "Animation reference assigned — preview pending";
    body.textContent = "The source/reused animation is identified below. Its visual render has not been added to the gallery yet.";
  } else if (m.animation_bucket === "No source animation") {
    title.textContent = "No source animation exists";
    body.textContent = "This move needs a Platinum/hg-engine analog or a new custom DS animation before visual approval.";
  } else {
    title.textContent = "Animation selection pending";
    body.textContent = "No animation has been locked for this move yet.";
  }

  wrap.appendChild(title);
  wrap.appendChild(body);
  el.animationPreview.appendChild(wrap);
}

function renderAnimationLinks(m) {
  el.animationLinks.innerHTML = "";
  const links = [];

  if (m.source_repo && m.source_commit && m.source_data_path) {
    links.push({
      label: "Open move source",
      url: "https://github.com/" + m.source_repo + "/blob/" + m.source_commit + "/" + encodePath(m.source_data_path)
    });
  }

  if (m.ds_animation_path) {
    links.push({
      label: "Open assigned DS animation script",
      url: GITHUB + "/blob/" + BRANCH + "/" + encodePath(m.ds_animation_path)
    });
  }

  if (m.animation_manifest_path) {
    links.push({
      label: "Open animation audit manifest",
      url: GITHUB + "/blob/" + BRANCH + "/" + encodePath(m.animation_manifest_path)
    });
  }

  links.forEach(function(link) {
    const a = document.createElement("a");
    a.href = link.url;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.textContent = link.label;
    el.animationLinks.appendChild(a);
  });
}

function encodePath(path) {
  return String(path || "").split("/").map(encodeURIComponent).join("/");
}

function animationBadgeColor(bucket) {
  if (bucket === "DS reuse assigned") return "#22c55e";
  if (bucket === "Source animation needs DS port") return "#38bdf8";
  if (bucket === "Referenced animation assigned") return "#a78bfa";
  if (bucket === "No source animation") return "#ef4444";
  return "#f59e0b";
}

function renderGrid(container, items) {
  container.innerHTML = "";
  items.forEach(function(item) {
    const div = document.createElement("div");
    div.className = "detail-item" + (item[2] ? " full" : "");
    const label = document.createElement("span");
    label.className = "label";
    label.textContent = item[0];
    const value = document.createElement("div");
    value.className = "value";
    value.textContent = item[1];
    div.appendChild(label);
    div.appendChild(value);
    container.appendChild(div);
  });
}

function setPill(node, text, extraClass) {
  node.textContent = text;
  node.className = "pill" + (extraClass ? " " + extraClass : "");
}

function plainEnglishEffect(m) {
  if (m.audit && m.audit.effect_text) return m.audit.effect_text;

  const primary = cleanEffectText(m.primary_effect);
  const secondary = cleanEffectText(m.secondary_effect);
  const parts = [];

  if (primary) {
    if (/^damage$/i.test(primary)) parts.push("Deals damage.");
    else parts.push(ensureSentence(primary));
  }

  if (secondary && !/^(none|n\/a)$/i.test(secondary)) {
    parts.push(ensureSentence(secondary));
  }

  if (!parts.length) {
    return "Plain-English effect pending full source audit.";
  }

  return parts.join(" ");
}

function isInternalEffectText(value) {
  const text = String(value == null ? "" : value).trim();
  if (!text) return true;
  return /^(EFFECT_|FunctionCode\b|effect code\b|custom[_ ]?behavior\b|custom callback\b|damage\/status logic\b|Rejuvenation effect code\b|Uranium effect code\b|Armonia effect code\b|Filler\b)/i.test(text);
}

function cleanEffectText(value) {
  let text = String(value == null ? "" : value).trim();
  if (!text) return "";

  // Remove internal implementation labels when a human-readable explanation follows.
  text = text.replace(/^FunctionCode\s+[^;]+;\s*/i, "");

  // If the record is only an internal effect code, don't pretend it is user-friendly.
  if (/^(FunctionCode|effect code|custom_behavior)\b/i.test(text)) {
    return "Plain-English effect pending source verification";
  }

  return text;
}

function ensureSentence(text) {
  const t = String(text || "").trim();
  if (!t) return "";
  return /[.!?]$/.test(t) ? t : t + ".";
}

function displayValue(value) {
  const str = String(value == null ? "" : value).trim();
  return str || "Not recorded";
}

function displayAccuracy(value) {
  const str = String(value == null ? "" : value).trim();
  if (!str) return "Not recorded";
  if (str === "0") return "Always / source-specific";
  return str + (/%$/.test(str) ? "" : "%");
}

function prettyKey(key) {
  return String(key).replace(/_/g, " ").replace(/\b\w/g, function(c) { return c.toUpperCase(); });
}

function slug(value) {
  return String(value || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function renderReviewControls() {
  if (!state.selectedId) return;
  const review = getReview(state.selectedId);
  const move = state.moves.find(function(m) { return m.move_id === state.selectedId; });
  const auditReady = !!(move && move.audit && String(move.audit.status || "").toLowerCase() === "complete" && move.audit.approval_ready !== false);

  document.querySelectorAll('.segmented[data-group="move"] button').forEach(function(btn) {
    btn.classList.toggle("active", btn.dataset.value === review.move);
    btn.disabled = !auditReady && btn.dataset.value !== "unreviewed";
    btn.title = auditReady ? "" : "Approval is locked until the move's full mechanics audit is source-complete.";
  });
  document.querySelectorAll('.segmented[data-group="animation"] button').forEach(function(btn) {
    btn.classList.toggle("active", btn.dataset.value === review.animation);
    btn.disabled = !auditReady && btn.dataset.value !== "unreviewed";
    btn.title = auditReady ? "" : "Animation approval is locked until the move's mechanics are fully verified.";
  });

  el.reviewNotes.value = review.notes || "";
  if (!auditReady) {
    el.saveState.textContent = "Approval locked: this move still has unresolved source mechanics. Notes can still be saved.";
  } else {
    el.saveState.textContent = review.updated_at ?
      "Saved automatically. Last changed " + formatDate(review.updated_at) + "." :
      "Saved automatically on this device.";
  }
}

function getReview(id) {
  const existing = state.reviews[id] || {};
  return {
    move: existing.move || "unreviewed",
    animation: existing.animation || "unreviewed",
    notes: existing.notes || "",
    updated_at: existing.updated_at || ""
  };
}

function loadReviews() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch (err) {
    return {};
  }
}

function saveReviews() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.reviews));
}

function updateDashboard() {
  const total = state.moves.length;
  let full = 0;
  let approved = 0;
  let animApproved = 0;

  state.moves.forEach(function(m) {
    const r = getReview(m.move_id);
    if (r.move !== "unreviewed" && r.animation !== "unreviewed") full++;
    if (r.move === "approved") approved++;
    if (r.animation === "approved") animApproved++;
  });

  const remaining = total - full;
  const pct = total ? Math.round((full / total) * 100) : 0;

  el.totalCount.textContent = total;
  el.reviewedCount.textContent = full;
  el.approvedCount.textContent = approved;
  el.animationApprovedCount.textContent = animApproved;
  el.remainingCount.textContent = remaining;
  el.progressText.textContent = pct + "%";
  el.progressBar.style.width = pct + "%";
}

function exportReviewsJson() {
  const payload = {
    schema_version: 1,
    repository: OWNER + "/" + REPO,
    exported_at: new Date().toISOString(),
    move_count: state.moves.length,
    reviews: state.reviews
  };
  downloadBlob(
    JSON.stringify(payload, null, 2),
    "pokemon-move-approvals.json",
    "application/json"
  );
}

function exportReviewsCsv() {
  const rows = [["move_id","english_review_name","original_source_name","source_project","move_decision","animation_decision","notes","updated_at"]];
  state.moves.forEach(function(m) {
    const r = getReview(m.move_id);
    rows.push([m.move_id,m.display_name,m.original_move_name,m.source_project,r.move,r.animation,r.notes,r.updated_at]);
  });
  const csv = rows.map(function(row) {
    return row.map(csvEscape).join(",");
  }).join("\n") + "\n";
  downloadBlob(csv, "pokemon-move-approvals.csv", "text/csv");
}

function csvEscape(value) {
  return '"' + String(value == null ? "" : value).replace(/"/g, '""') + '"';
}

function downloadBlob(content, filename, type) {
  const blob = new Blob([content], { type: type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(function() { URL.revokeObjectURL(url); }, 1000);
}

function importReviews(e) {
  const file = e.target.files && e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function() {
    try {
      const parsed = JSON.parse(reader.result);
      const incoming = parsed.reviews || parsed;
      if (!incoming || typeof incoming !== "object") throw new Error("Invalid review file.");
      state.reviews = Object.assign({}, state.reviews, incoming);
      saveReviews();
      renderMoveList();
      renderReviewControls();
      updateDashboard();
      alert("Reviews imported successfully.");
    } catch (err) {
      alert("Could not import this review file: " + err.message);
    } finally {
      el.importInput.value = "";
    }
  };
  reader.readAsText(file);
}

function formatDate(iso) {
  try {
    return new Date(iso).toLocaleString();
  } catch (err) {
    return iso;
  }
}

function setLoading(on) {
  if (on) {
    el.moveList.innerHTML = '<div class="preview-placeholder"><strong>Loading 519-move library…</strong>Pulling the current master catalog and animation audit manifests from GitHub.</div>';
  }
}

function showFatal(err) {
  el.moveList.innerHTML = "";
  el.emptyState.innerHTML = "<h2>Could not load the approval board</h2><p>" + escapeHtml(String(err)) + "</p>";
  el.emptyState.classList.remove("hidden");
  el.moveDetail.classList.add("hidden");
}

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, function(c) {
    return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];
  });
}
