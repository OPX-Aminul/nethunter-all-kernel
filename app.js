(function () {
  const state = { q: '', status: 'all', feature: 'all', sort: 'recommended', shown: 24, onlyFiles: false };
  const PAGE = 24;
  let DATA = null;
  let filtered = [];

  const $ = (sel) => document.querySelector(sel);
  const list = $('#list');
  const search = $('#search');
  const sort = $('#sort');
  const feature = $('#feature');
  const resultCount = $('#resultCount');
  const loadMore = $('#loadMore');
  const summary = $('#summary');

  const STATUS_LABEL = {
    'Developer claimed': 'Best evidence',
    'Source confirmed': 'Official source',
    'Unverified candidate': 'Unverified',
    'Abandoned': 'Abandoned',
  };
  const STATUS_CLASS = {
    'Developer claimed': 'claimed',
    'Source confirmed': 'official',
    'Unverified candidate': 'unverified',
    'Abandoned': 'abandoned',
  };
  const LEVEL_SHORT = {
    'Developer-reported test': 'tested',
    'Claimed by developer': 'claimed',
    'Source/config evidence': 'source',
    'Unknown': 'unknown',
  };
  const REC_STATUS = {
    'Developer claimed': 'Best evidence',
    'Source confirmed': 'Official source',
    'Unverified candidate': 'Unverified',
    'Abandoned': 'Abandoned',
  };

  function esc(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  function num(n) { return Number(n || 0).toLocaleString('en-US'); }
  function validUrl(url) { return /^https?:\/\//i.test(String(url || '')); }
  function shortRepo(url) {
    return String(url || '').replace(/^https?:\/\/(www\.)?/, '').replace(/\.git$/, '').replace(/\/$/, '');
  }
  function statusBadge(status) {
    return `<span class="badge ${STATUS_CLASS[status] || 'unverified'}">${esc(STATUS_LABEL[status] || status)}</span>`;
  }
  function featureHtml(key, f) {
    const cls = f.level === 'Developer-reported test' ? 'test' : (f.level === 'Claimed by developer' ? 'claim' : '');
    return `<span class="feature ${cls}">${esc(f.label)} <em>${esc(LEVEL_SHORT[f.level] || f.level)}</em></span>`;
  }
  function bootShort(s) {
    if (s === 'Developer-reported boot') return 'reported working';
    if (s === 'Reported not booting') return 'reported failing';
    if (s === 'Compatibility claim') return 'not verified (claim only)';
    return 'not verified';
  }
  function workShort(s) {
    if (s === 'Working (developer-reported)') return 'reported working';
    if (s === 'Reported not working') return 'reported failing';
    if (s === 'Working (claimed)') return 'claimed only';
    return 'not verified';
  }
  function statusLine(v, withNote) {
    const boot = v.bootStatus || 'Not verified';
    const bcls = boot === 'Developer-reported boot' ? 'good' : (boot === 'Reported not booting' ? 'bad' : (boot === 'Compatibility claim' ? 'warn' : 'bad'));
    const work = v.workingStatus || 'Not verified';
    const wcls = work === 'Working (developer-reported)' ? 'good' : (work === 'Reported not working' ? 'bad' : (work === 'Working (claimed)' ? 'warn' : 'bad'));
    const fcls = v.hasFile ? 'good' : (v.releaseCount > 0 ? 'warn' : 'bad');
    const files = v.hasFile ? `${num(v.directFileCount || 0)} direct` : (v.releaseCount > 0 ? 'no kernel file' : 'none');
    const gcls = v.hasGuide ? 'good' : (v.guideStatus === 'Generic guide only' ? 'warn' : 'bad');
    const rcls = v.releaseCount > 0 ? 'good' : (v.releaseCount === 0 ? 'bad' : 'warn');
    const rel = v.releaseCount == null ? 'n/a' : num(v.releaseCount);
    const rom = v.romNote && v.romNote !== 'Not specified' ? v.romNote : 'not specified';
    const note = v.bootNote || 'No boot report found in README/release text.';
    const spans = `<span class="st ${bcls}" title="${esc(note)}">Boot: ${esc(bootShort(boot))}</span>
      <span class="st ${wcls}" title="${esc(note)}">Working: ${esc(workShort(work))}</span>
      <span class="st ${fcls}">Files: ${esc(files)}</span>
      <span class="st ${gcls}">Guide: ${esc(v.guideStatus || 'Unknown')}</span>
      <span class="st ${rcls}" title="${esc(v.releaseSource || '')}">Releases: ${esc(rel)}</span>
      <span class="st rom" title="${esc(v.romNote || '')}">ROM: ${esc(rom)}</span>`;
    return `<div class="statusline">${spans}</div>${withNote ? `<p class="bootnote">${esc(note)}</p>` : ''}`;
  }
  function downloadLabel(device) {
    if (device.zipCount > 0) return 'Download ZIP';
    if (device.imgCount > 0) return 'Download IMG';
    if (device.downloadCount > 0) return 'Download file';
    if (device.releaseUrl) return 'Releases';
    return 'Kali mobile';
  }
  function downloadHref(device) {
    if (state.onlyFiles) {
      const v = (device.variants || []).find((x) => x.hasFile && (validUrl(x.downloadUrl) || validUrl(x.binaryUrl)));
      if (v) return v.downloadUrl || v.binaryUrl;
    }
    if (validUrl(device.downloadUrl)) return device.downloadUrl;
    if (device.recommended && validUrl(device.recommended.downloadUrl)) return device.recommended.downloadUrl;
    return 'https://www.kali.org/get-kali/#kali-mobile';
  }
  function fileKindLabel(kind) {
    return ({ zip: 'ZIP', img: 'IMG', archive: 'TAR', firmware: 'Firmware', modules: 'Modules', recovery: 'Recovery', checksum: 'Checksum', 'other-image': 'Image' })[kind] || 'File';
  }
  function assetButtons(assets, small) {
    const usable = (assets || []).filter((a) => a && a.url && a.kind !== 'checksum');
    if (!usable.length) return '';
    const cls = small ? 'btn small' : 'btn small';
    return usable.slice(0, 8).map((a) => `<a class="${cls}" href="${esc(a.url)}" target="_blank" rel="noopener noreferrer" title="${esc(a.name)}">Download ${esc(fileKindLabel(a.kind))}</a>`).join('');
  }
  function listHtml(items, cls) {
    if (!items || !items.length) return `<p class="vmeta">Not specified.</p>`;
    return `<ul class="${cls || ''}">${items.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`;
  }
  function guideHtml(g) {
    if (!g) return '';
    const methods = (g.method || []).map((m) => `<span class="chip mini">${esc(m)}</span>`).join('');
    const custom = (g.customizations || []).length
      ? `<div class="gcustom">${g.customizations.map((x) => `<span class="chip mini">${esc(x)}</span>`).join('')}</div>`
      : `<p class="vmeta">No customization claims extracted.</p>`;
    return `<section class="guide">
      <div class="ghead">
        <h4>Installation guide</h4>
        <span class="channel">${esc(g.channel || 'Unknown')}</span>
      </div>
      <div class="gmethods">${methods || '<span class="chip mini">Method not specified</span>'}</div>
      <p class="guide-source">${esc(g.source || '')}</p>
      <div class="guide-grid">
        <div>
          <h5>Requirements</h5>
          ${listHtml(g.requirements, 'glist')}
        </div>
        <div>
          <h5>Steps</h5>
          ${g.steps && g.steps.length ? `<ol class="gsteps">${g.steps.map((x) => `<li>${esc(x)}</li>`).join('')}</ol>` : `<p class="vmeta">No steps extracted.</p>`}
        </div>
      </div>
      <h5>Customization / kernel features</h5>
      ${custom}
      ${g.maintainerNotes ? `<h5>Maintainer installation notes</h5><p class="gnotes">${esc(g.maintainerNotes)}</p>` : ''}
      ${(g.warnings || []).length ? `<div class="gwarn">${g.warnings.map((x) => `<p>${esc(x)}</p>`).join('')}</div>` : ''}
    </section>`;
  }

  function matches(device) {
    const q = state.q.trim().toLowerCase();
    if (state.status !== 'all' && device.status !== state.status) return false;
    if (state.feature !== 'all' && !device.features[state.feature]) return false;
    if (state.onlyFiles && !(device.directFileKernels > 0)) return false;
    if (!q) return true;
    const hay = [
      device.device, device.codename, device.manufacturer,
      device.recommended.kernel, device.recommended.repo,
      device.recommended.developer, device.recommended.reason
    ].join(' ').toLowerCase();
    return hay.includes(q);
  }

  function sortDevices(a, b) {
    switch (state.sort) {
      case 'newest':
        return String(b.lastUpdate).localeCompare(String(a.lastUpdate)) || a.device.localeCompare(b.device);
      case 'name':
        return a.device.localeCompare(b.device) || a.codename.localeCompare(b.codename);
      case 'sources':
        return b.sourceCount - a.sourceCount || b.forkCount - a.forkCount || a.device.localeCompare(b.device);
      case 'forks':
        return b.forkCount - a.forkCount || b.sourceCount - a.sourceCount || a.device.localeCompare(b.device);
      case 'files':
        return b.downloadCount - a.downloadCount || b.sourceCount - a.sourceCount || a.device.localeCompare(b.device);
      default:
        return b.score - a.score || a.device.localeCompare(b.device);
    }
  }

  function cardHtml(d) {
    const features = Object.entries(d.features).slice(0, 6).map(([k, f]) => featureHtml(k, f)).join('');
    const featureBlock = features ? `<div class="features">${features}</div>` : '';
    const rec = d.recommended;
    const recRepo = validUrl(rec.repo) ? shortRepo(rec.repo) : 'No public source link';
    const recMeta = [rec.status ? REC_STATUS[rec.status] || rec.status : '', rec.lastUpdate !== 'Unknown' ? 'updated ' + rec.lastUpdate : 'update unknown']
      .filter(Boolean).join(' · ');
    const visibleVariants = state.onlyFiles ? d.variants.filter((v) => v && v.hasFile) : d.variants;
    const variants = visibleVariants.map((v) => {
      const vSource = validUrl(v.sourceUrl);
      const vRelease = validUrl(v.releaseUrl);
      const vFeatures = Object.values(v.features).filter((x) => x && x !== 'Unknown');
      const feat = vFeatures.length ? `<div class="vfeat">${vFeatures.map((x) => `<span>${esc(x)}</span>`).join('')}</div>` : '';
      const quote = v.evidenceQuote ? `<p class="quote">${esc(v.evidenceQuote).slice(0, 420)}</p>` : '';
      const methods = ((v.guide && v.guide.method) || []).map((m) => `<span class="chip mini">${esc(m)}</span>`).join('');
      const fileChips = (v.assets || []).filter((a) => a.kind !== 'checksum').map((a) => `<span class="filechip ${esc(a.kind)}">${esc(fileKindLabel(a.kind))}</span>`).join('');
      return `<div class="variant">
        <div class="vhead"><div><div class="vname">${esc(v.kernel)}</div>
          <div class="vmeta">${esc(v.developer)} · ${esc(v.status)} · ${esc(v.channel || 'Unknown')} · ${esc(v.android)} · ${esc(v.kernelVersion)}</div>
          <div class="vmeta">${esc(v.distribution || 'Unknown')}${v.zipCount ? ` · ${v.zipCount} ZIP` : ''}${v.imgCount ? ` · ${v.imgCount} IMG` : ''}</div>
        </div></div>
        ${statusLine(v, true)}
        ${fileChips ? `<div class="vfeat">${fileChips}</div>` : ''}
        ${methods ? `<div class="vfeat">${methods}</div>` : ''}
        ${feat}
        ${quote}
        <div class="vlinks">
          ${assetButtons(v.assets, true)}
          ${vRelease ? `<a class="btn small" href="${esc(v.releaseUrl)}" target="_blank" rel="noopener noreferrer">Releases</a>` : ``}
          ${vSource ? `<a class="btn small source" href="${esc(v.sourceUrl)}" target="_blank" rel="noopener noreferrer">Source</a>` : ``}
        </div>
      </div>`;
    }).join('');
    return `<article class="card" id="${esc(d.id)}" data-id="${esc(d.id)}">
      <div class="card-head">
        <div>
          <h2>${esc(d.device)}</h2>
          <div class="meta"><span class="code">${esc(d.codename)}</span><span>${esc(d.manufacturer)}</span>${d.kernelCount > 1 ? `<span>${num(d.kernelCount)} kernels</span>` : ''}</div>
        </div>
        ${statusBadge(d.status)}
      </div>
      <div class="stats">
        <div class="stat"><strong>${num(d.sourceCount)}</strong><span>Sources</span></div>
        <div class="stat"><strong>${num(d.forkCount)}</strong><span>Forks</span></div>
        <div class="stat"><strong>${num(state.onlyFiles ? d.directFileKernels : d.kernelCount)}</strong><span>Kernels${state.onlyFiles ? ' with files' : ''}</span></div>
        <div class="stat"><strong>${num(state.onlyFiles ? d.directFileCount : (d.downloadCount || 0))}</strong><span>${state.onlyFiles ? 'Direct files' : 'Files'}</span></div>
      </div>
      <div class="rec">
        <span class="eyebrow">Recommended kernel</span>
        <div class="rec-title">${esc(rec.kernel)}</div>
        <div class="rec-sub">${esc(recRepo)} · ${esc(recMeta)}</div>
        <div class="rec-reason">${esc(rec.reason)}</div>
        ${statusLine(rec, false)}
        ${state.onlyFiles && !rec.hasFile ? '<p class="warnline">Recommended kernel has no direct file. Kernels with direct files are listed below.</p>' : ''}
      </div>
      ${featureBlock}
      <div class="actions">
        <a class="btn primary" href="${esc(downloadHref(d))}" target="_blank" rel="noopener noreferrer">${esc(downloadLabel(d))}</a>
        ${validUrl(d.sourceUrl) ? `<a class="btn source" href="${esc(d.sourceUrl)}" target="_blank" rel="noopener noreferrer">Source code</a>` : `<span class="btn source" aria-disabled="true">No source link</span>`}
        <button class="btn ghost detailsbtn" type="button" data-action="details" aria-expanded="false">Details</button>
      </div>
      <div class="details">
        <h3>Downloads &amp; installation</h3>
        <div class="dlsummary">
          <span><strong>${num(state.onlyFiles ? visibleVariants.length : d.sourceCount)}</strong> ${state.onlyFiles ? 'sources with files' : 'sources'}</span>
          <span><strong>${num(d.buildCount || 0)}</strong> builds with files</span>
          <span><strong>${num(d.zipCount || 0)}</strong> ZIP</span>
          <span><strong>${num(d.imgCount || 0)}</strong> IMG</span>
        </div>
        ${guideHtml(d.guide)}
        <h3 class="builds-title">All kernel builds (${num(visibleVariants.length)}${state.onlyFiles ? ' with direct files' : ''})</h3>
        ${variants || '<p class="vmeta">No variant details available.</p>'}
      </div>
    </article>`;
  }

  function render(reset) {
    filtered = DATA.devices.filter(matches).sort(sortDevices);
    if (reset) state.shown = PAGE;
    const visible = filtered.slice(0, state.shown);
    list.innerHTML = visible.length ? visible.map(cardHtml).join('') : `<div class="empty">No devices match this search. Try a codename, model, or clear the filters.</div>`;
    resultCount.textContent = `${num(filtered.length)} device${filtered.length === 1 ? '' : 's'}${state.onlyFiles ? ' with direct files' : ''}`;
    const filesBtn = $('#onlyFilesBtn');
    if (filesBtn) filesBtn.textContent = state.onlyFiles ? `Direct files only: ON (${num(DATA.stats.directFileDevices || 0)})` : `Direct files only (${num(DATA.stats.directFileDevices || 0)})`;
    loadMore.hidden = state.shown >= filtered.length;
    loadMore.textContent = `Load more devices (${num(Math.max(0, filtered.length - state.shown))} left)`;
  }

  function bindList() {
    list.addEventListener('click', (event) => {
      const button = event.target.closest('[data-action="details"]');
      if (!button) return;
      const card = button.closest('.card');
      const open = card.classList.toggle('is-open');
      button.setAttribute('aria-expanded', String(open));
      button.textContent = open ? 'Hide details' : 'Details';
    });
  }

  function bindControls() {
    let timer = 0;
    search.addEventListener('input', () => {
      clearTimeout(timer);
      timer = setTimeout(() => { state.q = search.value; render(true); }, 90);
    });
    sort.addEventListener('change', () => { state.sort = sort.value; render(true); });
    feature.addEventListener('change', () => { state.feature = feature.value; render(true); });
    const filesBtn = $('#onlyFilesBtn');
    filesBtn.addEventListener('click', () => {
      state.onlyFiles = !state.onlyFiles;
      filesBtn.classList.toggle('is-active', state.onlyFiles);
      filesBtn.setAttribute('aria-pressed', String(state.onlyFiles));
      render(true);
    });
    document.querySelectorAll('#statusFilters .chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('#statusFilters .chip').forEach((x) => x.classList.remove('is-active'));
        chip.classList.add('is-active');
        state.status = chip.dataset.status;
        render(true);
      });
    });
    loadMore.addEventListener('click', () => { state.shown += PAGE; render(false); });
  }

  function renderSummary() {
    const s = DATA.stats;
    summary.innerHTML = [
      `<span><strong>${num(s.devices)}</strong> devices</span>`,
      `<span><strong>${num(s.sources)}</strong> source repos</span>`,
      `<span><strong>${num(s.kernels)}</strong> kernel records</span>`,
      `<span><strong>${num(s.binaryDevices || 0)}</strong> with direct ZIP/IMG</span>`,
      `<span><strong>${num(s.bootReportedDevices || 0)}</strong> with boot reports</span>
      <span><strong>${num(s.notBootingDevices || 0)}</strong> reported not booting</span>`,
      `<span><strong>${num(s.recommended)}</strong> best-evidence devices</span>`,
    ].join('');
    $('#generated').textContent = DATA.generated;
  }

  fetch('data.json')
    .then((r) => { if (!r.ok) throw new Error('data load failed'); return r.json(); })
    .then((data) => {
      DATA = data;
      renderSummary();
      bindControls();
      bindList();
      render(true);
    })
    .catch((err) => {
      list.innerHTML = `<div class="empty">Could not load the dataset. ${esc(err.message)}</div>`;
    });
})();
