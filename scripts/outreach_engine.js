// Grayscale Outreach Desk & Tracking Engine v3.5
// Full CRUD: Add, Edit, Delete, Persistence, Filtering, Dynamic Metrics, Conversion Analytics, Export/Import
// Pure mathematical grayscale, zero emojis, zero gradients, light and dark mode

const svgIcons = {
    search: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
    clear: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
    sun: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>',
    moon: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>',
    external: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>',
    copy: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>',
    check: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    draft: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>',
    analytics: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>',
    download: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>',
    upload: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>',
    calendar: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
    linkedin: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    plus: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    edit: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>',
    trash: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>',
    reset: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 2v6h6M21.5 22v-6h-6"/><path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.2"/></svg>',
    table: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>',
    cards: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
    more: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="1.5"></circle><circle cx="19" cy="12" r="1.5"></circle><circle cx="5" cy="12" r="1.5"></circle></svg>',
    resume: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>',
    database: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>'
};

// 10 Pipeline Stages
const PIPELINE_STAGES = [
    'To Contact',
    'Connection Sent',
    'Accepted',
    'DM Sent',
    'Email Sent',
    'Followed Up',
    'Replied',
    'Interview',
    'Offer',
    'Archived'
];

// Helper Functions
function escapeOutreachHtml(value) {
    return String(value ?? '').replace(/[&<>"']/g, ch => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[ch]));
}

function safeOutreachHref(value) {
    try {
        const url = new URL(value);
        return ['https:', 'http:'].includes(url.protocol) ? url.href : '';
    } catch {
        return '';
    }
}

// Storage Keys & Unified State Management
const STORAGE_KEYS = {
    COMPANIES: 'target_startups_companies_v2',
    STATES: 'target_startups_states_v2',
    LEGACY_COMPANIES: 'custom_companies_data',
    LAST_SAVED: 'target_startups_last_saved',
    THEME: 'theme_preference',
    VIEW_MODE: 'layout_view_mode',
    FILTER_PILL: 'filter_pill',
    FILTER_STATUS: 'filter_status',
    SORT_ORDER: 'sort_order'
};

function storageGet(key) {
    try { return localStorage.getItem(key); }
    catch { return null; }
}

function storageSet(key, value) {
    try {
        localStorage.setItem(key, value);
        return true;
    } catch (e) {
        console.warn('LocalStorage save error for key:', key, e);
        return false;
    }
}

function storageDelete(key) {
    try {
        localStorage.removeItem(key);
        return true;
    } catch {
        return false;
    }
}

function getStorageUsageInfo() {
    let totalBytes = 0;
    try {
        for (let i = 0; i < localStorage.length; i++) {
            const k = localStorage.key(i);
            const val = localStorage.getItem(k);
            if (val) totalBytes += (k.length + val.length) * 2;
        }
    } catch {}
    const kb = (totalBytes / 1024).toFixed(1);
    return `${kb} KB`;
}

let _masterStatesCache = null;

function getMasterStatesMap() {
    if (_masterStatesCache) return _masterStatesCache;
    const raw = storageGet(STORAGE_KEYS.STATES);
    if (raw) {
        try {
            _masterStatesCache = JSON.parse(raw) || {};
            return _masterStatesCache;
        } catch {}
    }
    _masterStatesCache = {};
    return _masterStatesCache;
}

function updateMasterStateForId(id, state) {
    const map = getMasterStatesMap();
    map[String(id)] = state;
}

let _persistTimeout = null;

function debouncedPersistAllData() {
    clearTimeout(_persistTimeout);
    _persistTimeout = setTimeout(() => {
        persistAllData(true);
    }, 200);
}

function persistAllData(showIndicator = true) {
    if (!window.companyData) return;
    try {
        const json = JSON.stringify(window.companyData);
        storageSet(STORAGE_KEYS.COMPANIES, json);
        storageSet(STORAGE_KEYS.LEGACY_COMPANIES, json); // Legacy backward compatibility
        
        const masterMap = getMasterStatesMap();
        storageSet(STORAGE_KEYS.STATES, JSON.stringify(masterMap));
        
        const nowIso = new Date().toISOString();
        storageSet(STORAGE_KEYS.LAST_SAVED, nowIso);

        if (showIndicator) {
            updateStorageIndicator(true);
        }
    } catch (e) {
        console.error('LocalStorage persist error:', e);
    }
}

function getTodayIso() {
    return new Date().toISOString().split('T')[0];
}

function addDaysIso(isoDateStr, days) {
    try {
        const d = new Date(isoDateStr || getTodayIso());
        d.setDate(d.getDate() + days);
        return d.toISOString().split('T')[0];
    } catch {
        return getTodayIso();
    }
}

function daysDiff(d1Str, d2Str) {
    try {
        const d1 = new Date(d1Str);
        const d2 = new Date(d2Str);
        return Math.floor((d2 - d1) / (1000 * 60 * 60 * 24));
    } catch {
        return 0;
    }
}

function outreachToast(message) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    toast.innerText = message;
    toast.classList.add('show');
    clearTimeout(toast._timeout);
    toast._timeout = setTimeout(() => toast.classList.remove('show'), 2200);
}

async function copyOutreachText(value, triggerButton) {
    try {
        await navigator.clipboard.writeText(value);
        feedbackCopyButton(triggerButton);
        outreachToast('Copied to clipboard.');
    } catch {
        const temp = document.createElement('textarea');
        temp.value = value;
        document.body.appendChild(temp);
        temp.select();
        const copied = document.execCommand('copy');
        temp.remove();
        if (copied) {
            feedbackCopyButton(triggerButton);
            outreachToast('Copied to clipboard.');
        } else {
            outreachToast('Clipboard access unavailable.');
        }
    }
}

function feedbackCopyButton(btn) {
    if (!btn) return;
    const originalText = btn.innerHTML;
    btn.innerHTML = `${svgIcons.check} Copied!`;
    btn.classList.add('btn-copied');
    setTimeout(() => {
        btn.innerHTML = originalText;
        btn.classList.remove('btn-copied');
    }, 1800);
}

// Company List Persistence & State Management
function initCompanyData() {
    let loadedData = null;

    // 1. Try modern v2 data from LocalStorage
    const rawV2 = storageGet(STORAGE_KEYS.COMPANIES);
    if (rawV2) {
        try {
            const parsed = JSON.parse(rawV2);
            if (Array.isArray(parsed) && parsed.length > 0) {
                loadedData = parsed;
            }
        } catch (e) {
            console.error('Error parsing STORAGE_KEYS.COMPANIES', e);
        }
    }

    // 2. Try legacy custom_companies_data
    if (!loadedData) {
        const rawLegacy = storageGet(STORAGE_KEYS.LEGACY_COMPANIES);
        if (rawLegacy) {
            try {
                const parsed = JSON.parse(rawLegacy);
                if (Array.isArray(parsed) && parsed.length > 0) {
                    loadedData = parsed;
                }
            } catch (e) {
                console.error('Error parsing legacy custom_companies_data', e);
            }
        }
    }

    // 3. Fall back to base companies list embedded in HTML
    if (!loadedData) {
        if (typeof companies !== 'undefined' && Array.isArray(companies)) {
            loadedData = JSON.parse(JSON.stringify(companies));
        } else {
            loadedData = [];
        }
    }

    window.companyData = loadedData;

    // 4. Merge any individual saved states into window.companyData
    const masterMap = getMasterStatesMap();
    window.companyData.forEach(comp => {
        const sId = String(comp.id);
        const state = getCompanyState(comp.id);
        if (state) {
            comp.outreach_status = state.status || comp.outreach_status || 'To Contact';
            comp.connection_sent_date = state.connection_sent_date || comp.connection_sent_date || '';
            comp.connection_accepted_date = state.connection_accepted_date || comp.connection_accepted_date || '';
            comp.dm_sent_date = state.dm_sent_date || comp.dm_sent_date || '';
            comp.email_sent_date = state.email_sent_date || comp.email_sent_date || '';
            comp.followup_due_date = state.followup_due_date || comp.followup_due_date || '';
            comp.last_touched_date = state.last_touched_date || comp.last_touched_date || '';
            comp.custom_notes = state.custom_notes || comp.custom_notes || '';
            comp.custom_signal = state.custom_signal || comp.custom_signal || '';
            comp.custom_observation = state.custom_observation || comp.custom_observation || '';
            comp.selected_proof = state.selected_proof || comp.selected_proof || '';
            comp.contact_verified = (state.contact_verified !== undefined) ? state.contact_verified : Boolean(comp.contact_verified);
            masterMap[sId] = state;
        }
    });

    // Save unified synchronized data to LocalStorage
    persistAllData(false);
    updateStorageIndicator(false);
}

function saveCustomCompaniesList() {
    if (!window.companyData) return;
    persistAllData(true);
    updateDynamicMetrics();
    render();
}

function getCompanyState(id) {
    const sId = String(id);
    const masterMap = getMasterStatesMap();
    if (masterMap[sId]) {
        return masterMap[sId];
    }

    const raw = storageGet('comp_state_' + id);
    if (raw) {
        try {
            const parsed = JSON.parse(raw);
            if (parsed && typeof parsed === 'object') {
                masterMap[sId] = parsed;
                return parsed;
            }
        } catch {}
    }

    const comp = (window.companyData && window.companyData.find(c => String(c.id) === sId)) ||
                 (typeof companies !== 'undefined' && companies.find(c => String(c.id) === sId)) || {};

    const legacyStatus = storageGet('status_comp_' + id);
    const legacyVerified = storageGet('contact_verified_' + id);

    const fallbackState = {
        status: legacyStatus || comp.outreach_status || 'To Contact',
        connection_sent_date: comp.connection_sent_date || '',
        connection_accepted_date: comp.connection_accepted_date || '',
        dm_sent_date: comp.dm_sent_date || '',
        email_sent_date: comp.email_sent_date || '',
        followup_due_date: comp.followup_due_date || '',
        last_touched_date: comp.last_touched_date || '',
        custom_notes: comp.custom_notes || '',
        custom_signal: comp.custom_signal || '',
        custom_observation: comp.custom_observation || '',
        selected_proof: comp.selected_proof || comp.recommended_proof || "NimitAI 317s->117s Pipeline Win",
        contact_verified: legacyVerified !== null ? (legacyVerified === 'true') : Boolean(comp.contact_verified)
    };

    masterMap[sId] = fallbackState;
    return fallbackState;
}

function saveCompanyState(id, state, shouldPersist = true) {
    const sId = String(id);
    updateMasterStateForId(sId, state);

    // Save individual legacy keys for maximum compatibility
    storageSet('comp_state_' + id, JSON.stringify(state));
    storageSet('status_comp_' + id, state.status);
    if (state.contact_verified !== undefined) {
        storageSet('contact_verified_' + id, String(state.contact_verified));
    }
    
    // Also update company object in memory
    const comp = window.companyData && window.companyData.find(c => String(c.id) === sId);
    if (comp) {
        comp.outreach_status = state.status;
        comp.connection_sent_date = state.connection_sent_date;
        comp.connection_accepted_date = state.connection_accepted_date;
        comp.dm_sent_date = state.dm_sent_date;
        comp.email_sent_date = state.email_sent_date;
        comp.followup_due_date = state.followup_due_date;
        comp.last_touched_date = state.last_touched_date;
        comp.custom_notes = state.custom_notes;
        comp.custom_signal = state.custom_signal;
        comp.custom_observation = state.custom_observation;
        comp.selected_proof = state.selected_proof;
        comp.contact_verified = state.contact_verified;
    }

    updateDynamicMetrics();

    if (shouldPersist) {
        debouncedPersistAllData();
    }
}

function updateCompanyStatus(id, newStatus) {
    const state = getCompanyState(id);
    state.status = newStatus;
    const today = getTodayIso();

    // Auto-populate dates based on stage transitions
    if (newStatus === 'Connection Sent') {
        if (!state.connection_sent_date) state.connection_sent_date = today;
        state.last_touched_date = today;
        state.followup_due_date = addDaysIso(today, 7);
    } else if (newStatus === 'Accepted') {
        if (!state.connection_accepted_date) state.connection_accepted_date = today;
        state.last_touched_date = today;
    } else if (newStatus === 'DM Sent') {
        if (!state.dm_sent_date) state.dm_sent_date = today;
        state.last_touched_date = today;
        state.followup_due_date = addDaysIso(today, 5);
    } else if (newStatus === 'Email Sent') {
        if (!state.email_sent_date) state.email_sent_date = today;
        state.last_touched_date = today;
        state.followup_due_date = addDaysIso(today, 5);
    } else if (newStatus === 'Followed Up') {
        state.last_touched_date = today;
        state.followup_due_date = addDaysIso(today, 5);
    } else if (['Replied', 'Interview', 'Offer', 'Archived'].includes(newStatus)) {
        state.last_touched_date = today;
        state.followup_due_date = '';
    }

    saveCompanyState(id, state, true);
    outreachToast(`Status: ${newStatus}`);
    
    // Refresh modal if open
    const modalSelect = document.getElementById('modal-status-select');
    if (modalSelect && modalSelect.dataset.compId === String(id)) {
        modalSelect.value = newStatus;
        updateModalDateDisplay(state);
    }

    // Refresh row in table
    const rowSelect = document.querySelector(`.status-select[data-id="${id}"]`);
    if (rowSelect) {
        rowSelect.value = newStatus;
    }

    // Update row date display
    const dateCell = document.querySelector(`.date-sub[data-date-id="${id}"]`);
    if (dateCell) {
        dateCell.innerText = formatDateBadge(state);
    }
}

function formatDateBadge(state) {
    const today = getTodayIso();
    if (state.followup_due_date) {
        const isOverdue = state.followup_due_date < today;
        const isToday = state.followup_due_date === today;
        const prefix = isOverdue ? 'Overdue' : (isToday ? 'Due today' : 'Due');
        return `${prefix}: ${state.followup_due_date}`;
    }
    if (state.last_touched_date) {
        return `Touched: ${state.last_touched_date}`;
    }
    return '';
}

// Proof Options for 80-120 Word Cold Email
const PROOF_SNIPPETS = {
    "NimitAI 317s->117s Pipeline Win": "cut an LLM pipeline from 317s to 117s (63% reduction) and migrated 20GB+ production data at NimitAI",
    "Code Sage AST Engine": "built Code Sage, an AST-driven static analysis engine for automated code quality and security audits",
    "Notovo LangGraph Memory": "built Notovo, an agentic memory and structured note synthesis engine powered by LangGraph",
    "OceanRAG Retrieval": "built high-throughput multi-modal retrieval pipelines with sub-second vector search indexing",
    "TTS Audio Analysis": "built full-stack speech analysis and TTS pitch workflows for Prep War Room"
};

// Dynamic Metrics & Filter Pill Counts
function updateDynamicMetrics() {
    if (!window.companyData) return;
    const comps = window.companyData;
    const today = getTodayIso();

    let tierACount = 0;
    let tierBCount = 0;
    let tierCCount = 0;
    let inPipelineCount = 0;
    let followupsDueCount = 0;
    let activeRepliedCount = 0;
    let delhiCount = 0;
    let remoteCount = 0;

    comps.forEach(c => {
        const state = getCompanyState(c.id);
        const st = state.status || c.outreach_status || 'To Contact';
        
        if (c.tier === 'Tier A') tierACount++;
        else if (c.tier === 'Tier B') tierBCount++;
        else tierCCount++;

        const loc = (c.work_model_location || '').toLowerCase();
        if (/delhi|noida|gurgaon/.test(loc)) delhiCount++;
        if (loc.includes('remote')) remoteCount++;

        if (st !== 'To Contact' && st !== 'Archived') {
            inPipelineCount++;
        }

        if (['Replied', 'Interview', 'Offer'].includes(st)) {
            activeRepliedCount++;
        }

        const isFollowupDue = state.followup_due_date && state.followup_due_date <= today;
        const isStale = state.last_touched_date && daysDiff(state.last_touched_date, today) >= 5 && !['Replied', 'Interview', 'Offer', 'Archived'].includes(st);
        
        if (['Connection Sent', 'DM Sent', 'Email Sent', 'Followed Up'].includes(st) && (isFollowupDue || isStale)) {
            followupsDueCount++;
        }
    });

    const elTotal = document.getElementById('metric-total');
    if (elTotal) elTotal.innerText = comps.length;

    const elTierA = document.getElementById('metric-tier-a');
    if (elTierA) elTierA.innerText = tierACount;

    const elTierB = document.getElementById('metric-tier-b');
    if (elTierB) elTierB.innerText = tierBCount;

    const elPipeline = document.getElementById('metric-pipeline');
    if (elPipeline) elPipeline.innerText = inPipelineCount;

    const elFollowups = document.getElementById('metric-followups');
    if (elFollowups) elFollowups.innerText = followupsDueCount;

    const elReplied = document.getElementById('metric-replied');
    if (elReplied) elReplied.innerText = activeRepliedCount;

    const pipelineStat = document.getElementById('pipeline-stat');
    if (pipelineStat) {
        pipelineStat.innerText = `${inPipelineCount} / ${comps.length} In Pipeline`;
    }

    // Dynamic counts on filter buttons
    updateFilterPillCount('all', `All (${comps.length})`);
    updateFilterPillCount('tierA', `Tier A (${tierACount})`);
    updateFilterPillCount('tierB', `Tier B (${tierBCount})`);
    updateFilterPillCount('tierC', `Tier C (${tierCCount})`);
    updateFilterPillCount('today', `Today (${followupsDueCount})`);
    updateFilterPillCount('pipeline', `In Pipeline (${inPipelineCount})`);
    updateFilterPillCount('delhi', `Delhi-NCR (${delhiCount})`);
    updateFilterPillCount('remote', `Remote (${remoteCount})`);
}

function updateFilterPillCount(filterKey, text) {
    const btn = document.querySelector(`.filter-btn[data-filter="${filterKey}"]`);
    if (btn) btn.innerText = text;
}

// Conversion Dashboard Calculation
function renderConversionDashboard() {
    if (!window.companyData) return;
    const comps = window.companyData;

    let connSent = 0;
    let connAccepted = 0;
    let dmSent = 0;
    let emailSent = 0;
    let repliedTotal = 0;
    let repliedLinkedin = 0;
    let repliedEmail = 0;
    let interviews = 0;
    let offers = 0;

    let tierStats = {
        'Tier A': { total: 0, contacted: 0, replied: 0 },
        'Tier B': { total: 0, contacted: 0, replied: 0 },
        'Tier C': { total: 0, contacted: 0, replied: 0 }
    };

    comps.forEach(c => {
        const state = getCompanyState(c.id);
        const st = state.status || c.outreach_status || 'To Contact';
        const tier = c.tier || 'Tier C';

        if (tierStats[tier]) tierStats[tier].total++;

        const isContacted = st !== 'To Contact';
        if (isContacted) {
            if (tierStats[tier]) tierStats[tier].contacted++;
        }

        if (state.connection_sent_date || ['Connection Sent', 'Accepted', 'DM Sent'].includes(st)) {
            connSent++;
        }
        if (state.connection_accepted_date || ['Accepted', 'DM Sent'].includes(st)) {
            connAccepted++;
        }
        if (state.dm_sent_date || st === 'DM Sent') {
            dmSent++;
        }
        if (state.email_sent_date || st === 'Email Sent') {
            emailSent++;
        }
        if (['Replied', 'Interview', 'Offer'].includes(st)) {
            repliedTotal++;
            if (tierStats[tier]) tierStats[tier].replied++;
            if (state.dm_sent_date && !state.email_sent_date) repliedLinkedin++;
            else repliedEmail++;
        }
        if (['Interview', 'Offer'].includes(st)) interviews++;
        if (st === 'Offer') offers++;
    });

    const acceptRate = connSent > 0 ? ((connAccepted / connSent) * 100).toFixed(1) : '0.0';
    const emailReplyRate = emailSent > 0 ? ((repliedEmail / emailSent) * 100).toFixed(1) : '0.0';
    const dmReplyRate = dmSent > 0 ? ((repliedLinkedin / dmSent) * 100).toFixed(1) : '0.0';
    const interviewRate = repliedTotal > 0 ? ((interviews / repliedTotal) * 100).toFixed(1) : '0.0';

    const modalBody = document.getElementById('analytics-modal-body');
    if (!modalBody) return;

    modalBody.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 20px;">
            <div class="analytics-card">
                <div class="analytics-label">LinkedIn Acceptance</div>
                <div class="analytics-val">${acceptRate}%</div>
                <div class="analytics-sub">${connAccepted} accepted of ${connSent} sent</div>
            </div>
            <div class="analytics-card">
                <div class="analytics-label">Email Reply Rate</div>
                <div class="analytics-val">${emailReplyRate}%</div>
                <div class="analytics-sub">${repliedEmail} replies of ${emailSent} sent</div>
            </div>
            <div class="analytics-card">
                <div class="analytics-label">LinkedIn DM Reply Rate</div>
                <div class="analytics-val">${dmReplyRate}%</div>
                <div class="analytics-sub">${repliedLinkedin} replies of ${dmSent} sent</div>
            </div>
            <div class="analytics-card">
                <div class="analytics-label">Interview Conversion</div>
                <div class="analytics-val">${interviewRate}%</div>
                <div class="analytics-sub">${interviews} interviews / ${offers} offers</div>
            </div>
        </div>

        <h4 style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin: 18px 0 10px; color: var(--text-primary);">Conversion Velocity by Tier</h4>
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-bottom: 20px;">
            <thead>
                <tr style="border-bottom: 2px solid var(--border-medium); text-align: left; color: var(--text-muted); font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em;">
                    <th style="padding: 10px 8px;">Tier Group</th>
                    <th style="padding: 10px 8px;">Total</th>
                    <th style="padding: 10px 8px;">Contacted</th>
                    <th style="padding: 10px 8px;">Replied</th>
                    <th style="padding: 10px 8px;">Conversion</th>
                </tr>
            </thead>
            <tbody>
                ${['Tier A', 'Tier B', 'Tier C'].map(t => {
                    const row = tierStats[t];
                    const rate = row.contacted > 0 ? ((row.replied / row.contacted) * 100).toFixed(1) : '0.0';
                    return `
                        <tr style="border-bottom: 1px solid var(--border-subtle);">
                            <td style="padding: 10px 8px; font-weight: 700;">${t}</td>
                            <td style="padding: 10px 8px; font-family: 'JetBrains Mono', monospace;">${row.total}</td>
                            <td style="padding: 10px 8px; font-family: 'JetBrains Mono', monospace;">${row.contacted}</td>
                            <td style="padding: 10px 8px; font-family: 'JetBrains Mono', monospace;">${row.replied}</td>
                            <td style="padding: 10px 8px; font-family: 'JetBrains Mono', monospace; font-weight: 700;">${rate}%</td>
                        </tr>
                    `;
                }).join('')}
            </tbody>
        </table>

        <div style="background: var(--bg-surface-elevated); padding: 14px; border-radius: 8px; border: 1px solid var(--border-subtle); font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
            <strong style="color: var(--text-primary); text-transform: uppercase; letter-spacing: 0.04em;">Target Daily Cadence:</strong><br>
            10 new connection requests + 5 direct DMs + 5 cold emails + all follow-ups due. Pacing prevents LinkedIn restrictions and preserves personal quality. Weekly Sunday review analyzes which hook drove highest replies.
        </div>
    `;

    document.getElementById('analytics-modal').classList.add('open');
}

// 1-Click Export, Import, Clipboard Sync & Backup
function exportTrackerDataJson() {
    if (!window.companyData) return;
    const comps = window.companyData.map(c => {
        const state = getCompanyState(c.id);
        return {
            ...c,
            outreach_status: state.status || c.outreach_status || 'To Contact',
            connection_sent_date: state.connection_sent_date || c.connection_sent_date || '',
            connection_accepted_date: state.connection_accepted_date || c.connection_accepted_date || '',
            dm_sent_date: state.dm_sent_date || c.dm_sent_date || '',
            email_sent_date: state.email_sent_date || c.email_sent_date || '',
            followup_due_date: state.followup_due_date || c.followup_due_date || '',
            last_touched_date: state.last_touched_date || c.last_touched_date || '',
            custom_notes: state.custom_notes || c.custom_notes || '',
            custom_signal: state.custom_signal || c.custom_signal || '',
            custom_observation: state.custom_observation || c.custom_observation || '',
            selected_proof: state.selected_proof || c.selected_proof || '',
            contact_verified: Boolean(state.contact_verified),
            tracker_state: state
        };
    });
    const blob = new Blob([JSON.stringify(comps, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `companies_data.json`;
    a.click();
    URL.revokeObjectURL(url);
    outreachToast('Exported complete companies_data.json backup');
}

async function copyStateToClipboard() {
    if (!window.companyData) return;
    const comps = window.companyData.map(c => {
        const state = getCompanyState(c.id);
        return {
            ...c,
            outreach_status: state.status || c.outreach_status || 'To Contact',
            connection_sent_date: state.connection_sent_date || c.connection_sent_date || '',
            connection_accepted_date: state.connection_accepted_date || c.connection_accepted_date || '',
            dm_sent_date: state.dm_sent_date || c.dm_sent_date || '',
            email_sent_date: state.email_sent_date || c.email_sent_date || '',
            followup_due_date: state.followup_due_date || c.followup_due_date || '',
            last_touched_date: state.last_touched_date || c.last_touched_date || '',
            custom_notes: state.custom_notes || c.custom_notes || '',
            custom_signal: state.custom_signal || c.custom_signal || '',
            custom_observation: state.custom_observation || c.custom_observation || '',
            selected_proof: state.selected_proof || c.selected_proof || '',
            contact_verified: Boolean(state.contact_verified),
            tracker_state: state
        };
    });
    const text = JSON.stringify(comps, null, 2);
    try {
        await navigator.clipboard.writeText(text);
        outreachToast('Copied full JSON state to clipboard!');
    } catch {
        const ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        ta.remove();
        outreachToast('Copied full JSON state to clipboard!');
    }
}

async function restoreStateFromClipboard() {
    try {
        let text = '';
        if (navigator.clipboard && navigator.clipboard.readText) {
            try { text = await navigator.clipboard.readText(); } catch {}
        }
        if (!text || !text.trim().startsWith('[')) {
            text = prompt('Paste your JSON backup data here:');
        }
        if (!text) return;
        applyJsonImportString(text);
    } catch (e) {
        outreachToast('Could not read clipboard. Please use file import.');
    }
}

function applyJsonImportArray(data) {
    if (!Array.isArray(data) || data.length === 0) {
        outreachToast('Invalid backup data format.');
        return;
    }
    window.companyData = data;
    data.forEach(item => {
        if (item.id) {
            const state = item.tracker_state || {
                status: item.outreach_status || item.status || 'To Contact',
                connection_sent_date: item.connection_sent_date || '',
                connection_accepted_date: item.connection_accepted_date || '',
                dm_sent_date: item.dm_sent_date || '',
                email_sent_date: item.email_sent_date || '',
                followup_due_date: item.followup_due_date || '',
                last_touched_date: item.last_touched_date || '',
                custom_notes: item.custom_notes || '',
                custom_signal: item.custom_signal || '',
                custom_observation: item.custom_observation || '',
                selected_proof: item.selected_proof || item.recommended_proof || '',
                contact_verified: Boolean(item.contact_verified)
            };
            saveCompanyState(item.id, state, false);
        }
    });
    persistAllData(true);
    render();
    updateDynamicMetrics();
    renderStorageModalBody();
    outreachToast(`Restored ${data.length} startups to Local Storage!`);
}

function applyJsonImportString(jsonStr) {
    try {
        const parsed = JSON.parse(jsonStr);
        applyJsonImportArray(parsed);
    } catch {
        outreachToast('Import failed: invalid JSON format.');
    }
}

function exportTrackerDataCsv() {
    if (!window.companyData) return;
    const comps = window.companyData;
    const headers = [
        "id", "company_name", "tier", "total_score", "status", "career_email",
        "contact_name", "contact_role", "website", "domain_sector", "work_model_location",
        "funding_stage_investors", "employee_count", "nalin_tech_fit_hook", "warm_intro_path",
        "linkedin_url", "career_page_url", "connection_sent_date", "connection_accepted_date",
        "dm_sent_date", "email_sent_date", "followup_due_date", "last_touched_date", "custom_notes"
    ];

    let csvRows = [headers.join(",")];

    comps.forEach(c => {
        const state = getCompanyState(c.id);
        const row = [
            c.id,
            `"${(c.company_name || '').replace(/"/g, '""')}"`,
            c.tier || 'Tier C',
            c.total_score || 0,
            state.status || c.outreach_status || 'To Contact',
            `"${(c.career_email || '').replace(/"/g, '""')}"`,
            `"${(c.contact_name || '').replace(/"/g, '""')}"`,
            `"${(c.contact_role || '').replace(/"/g, '""')}"`,
            `"${(c.website || '').replace(/"/g, '""')}"`,
            `"${(c.domain_sector || '').replace(/"/g, '""')}"`,
            `"${(c.work_model_location || '').replace(/"/g, '""')}"`,
            `"${(c.funding_stage_investors || '').replace(/"/g, '""')}"`,
            `"${(c.employee_count || '').replace(/"/g, '""')}"`,
            `"${(c.nalin_tech_fit_hook || '').replace(/"/g, '""')}"`,
            `"${(c.warm_intro_path || '').replace(/"/g, '""')}"`,
            `"${(c.linkedin_url || '').replace(/"/g, '""')}"`,
            `"${(c.career_page_url || '').replace(/"/g, '""')}"`,
            state.connection_sent_date || c.connection_sent_date || '',
            state.connection_accepted_date || c.connection_accepted_date || '',
            state.dm_sent_date || c.dm_sent_date || '',
            state.email_sent_date || c.email_sent_date || '',
            state.followup_due_date || c.followup_due_date || '',
            state.last_touched_date || c.last_touched_date || '',
            `"${(state.custom_notes || c.custom_notes || '').replace(/"/g, '""')}"`
        ];
        csvRows.push(row.join(","));
    });

    const blob = new Blob([csvRows.join("\n")], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `target_companies_${getTodayIso()}.csv`;
    a.click();
    URL.revokeObjectURL(url);
    outreachToast('Exported CSV tracker.');
}

function importTrackerData(event) {
    const file = event.target.files && event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const content = e.target.result;
            if (file.name.endsWith('.json')) {
                const data = JSON.parse(content);
                applyJsonImportArray(data);
            } else if (file.name.endsWith('.csv')) {
                const lines = content.split('\n');
                let restoredCount = 0;
                for (let i = 1; i < lines.length; i++) {
                    const line = lines[i].trim();
                    if (!line) continue;
                    const parts = line.split(',');
                    const id = parseInt(parts[0], 10);
                    if (!isNaN(id) && parts.length >= 5) {
                        const status = parts[4].replace(/"/g, '').trim();
                        const state = getCompanyState(id);
                        state.status = status;
                        if (parts[17]) state.connection_sent_date = parts[17].replace(/"/g, '').trim();
                        if (parts[18]) state.connection_accepted_date = parts[18].replace(/"/g, '').trim();
                        if (parts[19]) state.dm_sent_date = parts[19].replace(/"/g, '').trim();
                        if (parts[20]) state.email_sent_date = parts[20].replace(/"/g, '').trim();
                        if (parts[21]) state.followup_due_date = parts[21].replace(/"/g, '').trim();
                        if (parts[22]) state.last_touched_date = parts[22].replace(/"/g, '').trim();
                        saveCompanyState(id, state, false);
                        restoredCount++;
                    }
                }
                persistAllData(true);
                render();
                updateDynamicMetrics();
                renderStorageModalBody();
                outreachToast(`Updated ${restoredCount} company states from CSV.`);
            }
        } catch (err) {
            outreachToast('Import failed: invalid file format.');
        }
        event.target.value = '';
    };
    reader.readAsText(file);
}

// Reset List to Initial Dataset
function resetCompanyList() {
    if (confirm('Reset directory back to original 355 verified startups? Custom additions and modifications will be cleared from Local Storage.')) {
        storageDelete(STORAGE_KEYS.COMPANIES);
        storageDelete(STORAGE_KEYS.LEGACY_COMPANIES);
        storageDelete(STORAGE_KEYS.STATES);
        _masterStatesCache = {};

        for (let i = localStorage.length - 1; i >= 0; i--) {
            const key = localStorage.key(i);
            if (key && (key.startsWith('comp_state_') || key.startsWith('status_comp_') || key.startsWith('contact_verified_'))) {
                storageDelete(key);
            }
        }

        if (typeof window.initialCompaniesData !== 'undefined') {
            window.companyData = JSON.parse(JSON.stringify(window.initialCompaniesData));
        } else if (typeof companies !== 'undefined') {
            window.companyData = JSON.parse(JSON.stringify(companies));
        }
        persistAllData(false);
        render();
        updateDynamicMetrics();
        updateStorageIndicator(true);
        renderStorageModalBody();
        outreachToast('Directory reset to original 355 startups in Local Storage.');
    }
}

// Add & Edit Company Modal Handlers
function openAddCompanyModal() {
    document.getElementById('company-form-title').innerText = 'Add New Startup / Company';
    document.getElementById('edit-company-id').value = '';
    document.getElementById('form-company-name').value = '';
    document.getElementById('form-website').value = '';
    document.getElementById('form-domain-sector').value = '';
    document.getElementById('form-employee-count').value = '10-25';
    document.getElementById('form-funding').value = 'Seed $2M';
    document.getElementById('form-location').value = 'Delhi-NCR / Remote';
    document.getElementById('form-contact-name').value = '';
    document.getElementById('form-contact-role').value = 'Founder & CEO';
    document.getElementById('form-email').value = '';
    document.getElementById('form-career-url').value = '';
    document.getElementById('form-linkedin-url').value = '';
    document.getElementById('form-hook').value = '';
    document.getElementById('form-warm-path').value = 'Direct Outreach';
    document.getElementById('form-tier').value = 'Tier B';
    document.getElementById('score-stack').value = '4';
    document.getElementById('score-hiring').value = '4';
    document.getElementById('score-india').value = '5';
    document.getElementById('score-warm').value = '4';
    document.getElementById('score-comp').value = '4';
    updateFormTotalScore();
    document.getElementById('form-status').value = 'To Contact';

    document.getElementById('btn-delete-company').style.display = 'none';
    document.getElementById('company-form-modal').classList.add('open');
    document.body.style.overflow = 'hidden';
}

function openEditCompanyModal(id) {
    if (!window.companyData) return;
    const comp = window.companyData.find(c => String(c.id) === String(id));
    if (!comp) return;
    const state = getCompanyState(id);

    document.getElementById('company-form-title').innerText = `Edit Startup · ${comp.company_name}`;
    document.getElementById('edit-company-id').value = comp.id;
    document.getElementById('form-company-name').value = comp.company_name || '';
    document.getElementById('form-website').value = comp.website || '';
    document.getElementById('form-domain-sector').value = comp.domain_sector || '';
    document.getElementById('form-employee-count').value = comp.employee_count || '';
    document.getElementById('form-funding').value = comp.funding_stage_investors || '';
    document.getElementById('form-location').value = comp.work_model_location || '';
    document.getElementById('form-contact-name').value = comp.contact_name || comp.hiring_decision_maker || '';
    document.getElementById('form-contact-role').value = comp.contact_role || 'Founder & CEO';
    document.getElementById('form-email').value = comp.career_email || '';
    document.getElementById('form-career-url').value = comp.career_page_url || '';
    document.getElementById('form-linkedin-url').value = comp.linkedin_url || '';
    document.getElementById('form-hook').value = comp.nalin_tech_fit_hook || '';
    document.getElementById('form-warm-path').value = comp.warm_intro_path || '';
    document.getElementById('form-tier').value = comp.tier || 'Tier B';
    document.getElementById('score-stack').value = comp.score_stack_fit ?? 4;
    document.getElementById('score-hiring').value = comp.score_hiring_signal ?? 4;
    document.getElementById('score-india').value = comp.score_india_eligibility ?? 5;
    document.getElementById('score-warm').value = comp.score_warm_path ?? 4;
    document.getElementById('score-comp').value = comp.score_comp_likelihood ?? 4;
    updateFormTotalScore();
    document.getElementById('form-status').value = state.status || comp.outreach_status || 'To Contact';

    document.getElementById('btn-delete-company').style.display = 'inline-flex';
    document.getElementById('company-form-modal').classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeCompanyFormModal() {
    const modal = document.getElementById('company-form-modal');
    if (modal) modal.classList.remove('open');
    document.body.style.overflow = '';
}

function updateFormTotalScore() {
    const stack = parseInt(document.getElementById('score-stack').value, 10) || 0;
    const hiring = parseInt(document.getElementById('score-hiring').value, 10) || 0;
    const india = parseInt(document.getElementById('score-india').value, 10) || 0;
    const warm = parseInt(document.getElementById('score-warm').value, 10) || 0;
    const compScore = parseInt(document.getElementById('score-comp').value, 10) || 0;
    const total = stack + hiring + india + warm + compScore;

    const totalEl = document.getElementById('form-total-score-display');
    if (totalEl) totalEl.innerText = `${total}/25`;

    // Auto suggest Tier if adding new
    const idStr = document.getElementById('edit-company-id').value;
    if (!idStr) {
        const tierSelect = document.getElementById('form-tier');
        if (tierSelect) {
            if (total >= 23) tierSelect.value = 'Tier A';
            else if (total >= 20) tierSelect.value = 'Tier B';
            else tierSelect.value = 'Tier C';
        }
    }
}

function handleCompanyFormSubmit(e) {
    if (e) e.preventDefault();
    const idStr = document.getElementById('edit-company-id').value;
    const name = document.getElementById('form-company-name').value.trim();
    let website = document.getElementById('form-website').value.trim();

    if (!name) {
        outreachToast('Please enter a company name.');
        return;
    }
    if (!website) {
        outreachToast('Please enter a website URL.');
        return;
    }
    if (!website.startsWith('http://') && !website.startsWith('https://')) {
        website = 'https://' + website;
    }

    const stack = parseInt(document.getElementById('score-stack').value, 10) || 0;
    const hiring = parseInt(document.getElementById('score-hiring').value, 10) || 0;
    const india = parseInt(document.getElementById('score-india').value, 10) || 0;
    const warm = parseInt(document.getElementById('score-warm').value, 10) || 0;
    const compScore = parseInt(document.getElementById('score-comp').value, 10) || 0;
    const totalScore = stack + hiring + india + warm + compScore;

    const tier = document.getElementById('form-tier').value;
    const status = document.getElementById('form-status').value;
    const contactName = document.getElementById('form-contact-name').value.trim() || 'Founding Team';
    const contactRole = document.getElementById('form-contact-role').value.trim() || 'Founder & CEO';
    const decisionMaker = `${contactName} (${contactRole})`;

    if (idStr) {
        // Edit existing company
        const id = parseInt(idStr, 10);
        const comp = window.companyData.find(c => c.id === id);
        if (comp) {
            comp.company_name = name;
            comp.website = website;
            comp.domain_sector = document.getElementById('form-domain-sector').value.trim() || 'AI Product Engineering';
            comp.employee_count = document.getElementById('form-employee-count').value.trim() || '10-25';
            comp.funding_stage_investors = document.getElementById('form-funding').value.trim() || 'Seed';
            comp.work_model_location = document.getElementById('form-location').value.trim() || 'Remote';
            comp.contact_name = contactName;
            comp.contact_role = contactRole;
            comp.hiring_decision_maker = decisionMaker;
            comp.career_email = document.getElementById('form-email').value.trim() || 'careers@' + website.replace(/^https?:\/\/(www\.)?/, '').split('/')[0];
            comp.career_page_url = document.getElementById('form-career-url').value.trim() || website + '/careers';
            comp.linkedin_url = document.getElementById('form-linkedin-url').value.trim();
            comp.nalin_tech_fit_hook = document.getElementById('form-hook').value.trim();
            comp.warm_intro_path = document.getElementById('form-warm-path').value.trim() || 'Direct Outreach';
            comp.tier = tier;
            comp.total_score = totalScore;
            comp.score_stack_fit = stack;
            comp.score_hiring_signal = hiring;
            comp.score_india_eligibility = india;
            comp.score_warm_path = warm;
            comp.score_comp_likelihood = compScore;

            updateCompanyStatus(id, status);
            saveCustomCompaniesList();
            outreachToast(`Saved updates for ${name}`);

            // Refresh Workbench if open
            if (currentModalComp && currentModalComp.id === id) {
                openOutreachModal(id);
            }
        }
    } else {
        // Add new company
        const maxId = window.companyData.reduce((max, c) => (Number(c.id) > max ? Number(c.id) : max), 0);
        const newId = maxId + 1;

        const newComp = {
            id: newId,
            company_name: name,
            website: website,
            domain_sector: document.getElementById('form-domain-sector').value.trim() || 'AI Product Engineering',
            employee_count: document.getElementById('form-employee-count').value.trim() || '10-25',
            funding_stage_investors: document.getElementById('form-funding').value.trim() || 'Seed',
            work_model_location: document.getElementById('form-location').value.trim() || 'Delhi-NCR / Remote',
            career_page_url: document.getElementById('form-career-url').value.trim() || website + '/careers',
            career_email: document.getElementById('form-email').value.trim() || 'founders@' + website.replace(/^https?:\/\/(www\.)?/, '').split('/')[0],
            contact_name: contactName,
            contact_role: contactRole,
            hiring_decision_maker: decisionMaker,
            nalin_tech_fit_hook: document.getElementById('form-hook').value.trim() || 'High-throughput LLM pipeline orchestration and low-latency API architecture.',
            outreach_status: status,
            tier: tier,
            total_score: totalScore,
            score_stack_fit: stack,
            score_hiring_signal: hiring,
            score_india_eligibility: india,
            score_warm_path: warm,
            score_comp_likelihood: compScore,
            recommended_proof: "NimitAI 317s->117s Pipeline Win",
            linkedin_url: document.getElementById('form-linkedin-url').value.trim() || '',
            contact_email_source: "Direct / User Added",
            warm_intro_path: document.getElementById('form-warm-path').value.trim() || 'Direct Outreach',
            link_audit: {
                id: newId,
                company_name: name,
                website: website,
                career_page_url: document.getElementById('form-career-url').value.trim() || '',
                website_check: { code: 200, final_url: website, detail: "Active HTTP 200", bucket: "ok" },
                career_url_check: { code: 200, final_url: document.getElementById('form-career-url').value.trim() || '', detail: "Active HTTP 200", bucket: "ok" }
            }
        };

        window.companyData.unshift(newComp); // Prepend to top
        updateCompanyStatus(newId, status);
        saveCustomCompaniesList();
        outreachToast(`Added ${name} (#${newId}) to directory`);
    }

    closeCompanyFormModal();
}

function handleDeleteCompany() {
    const idStr = document.getElementById('edit-company-id').value;
    if (!idStr) return;
    const id = parseInt(idStr, 10);
    const comp = window.companyData.find(c => c.id === id);
    if (!comp) return;

    if (confirm(`Remove "${comp.company_name}" from your active directory?`)) {
        window.companyData = window.companyData.filter(c => c.id !== id);
        storageDelete('comp_state_' + id);
        storageDelete('status_comp_' + id);
        saveCustomCompaniesList();
        closeCompanyFormModal();
        if (currentModalComp && currentModalComp.id === id) {
            closeOutreachModal();
        }
        outreachToast(`Removed "${comp.company_name}"`);
    }
}

// Outreach Modal & Draft Generators
let currentModalComp = null;
let currentLinkedInTier = 'free'; // 'free' (200) or 'premium' (300)

function openOutreachModal(id) {
    if (!window.companyData) return;
    const comp = window.companyData.find(c => String(c.id) === String(id));
    if (!comp) return;
    currentModalComp = comp;

    const modal = document.getElementById('outreach-modal');
    const state = getCompanyState(id);

    document.getElementById('modal-comp-name').innerText = comp.company_name;
    document.getElementById('modal-comp-tier').innerText = comp.tier || 'Tier C';
    document.getElementById('modal-comp-score').innerText = `Score: ${comp.total_score || 0}/25`;
    document.getElementById('modal-comp-sector').innerText = comp.domain_sector;
    document.getElementById('modal-comp-location').innerText = comp.work_model_location;
    document.getElementById('modal-comp-contact').innerText = `${comp.contact_name || comp.hiring_decision_maker} (${comp.contact_role || 'Founder'})`;
    document.getElementById('modal-comp-email').innerText = comp.career_email;

    // Score Breakdown
    const scoreBreakdownEl = document.getElementById('modal-score-breakdown');
    if (scoreBreakdownEl) {
        scoreBreakdownEl.innerHTML = `
            <span>Stack Fit: <strong>${comp.score_stack_fit ?? 4}/5</strong></span> · 
            <span>Hiring Signal: <strong>${comp.score_hiring_signal ?? 4}/5</strong></span> · 
            <span>India Eligibility: <strong>${comp.score_india_eligibility ?? 4}/5</strong></span> · 
            <span>Warm Path: <strong>${comp.score_warm_path ?? 4}/5</strong></span> · 
            <span>Comp: <strong>${comp.score_comp_likelihood ?? 4}/5</strong></span>
        `;
    }

    const linkedinLink = document.getElementById('modal-comp-linkedin');
    if (linkedinLink) {
        linkedinLink.href = comp.linkedin_url || `https://www.linkedin.com/search/results/all/?keywords=${encodeURIComponent(comp.company_name)}`;
    }

    const websiteLink = document.getElementById('modal-comp-website');
    if (websiteLink) websiteLink.href = comp.website;

    // Fill inputs from saved state or default
    document.getElementById('input-feature-signal').value = state.custom_signal || extractDefaultFeature(comp);
    document.getElementById('input-observation').value = state.custom_observation || extractDefaultObservation(comp);
    document.getElementById('modal-custom-notes').value = state.custom_notes || '';

    // Proof selector
    const proofSelect = document.getElementById('select-proof');
    if (proofSelect) {
        proofSelect.value = state.selected_proof || comp.recommended_proof || "NimitAI 317s->117s Pipeline Win";
    }

    // Status select
    const statusSelect = document.getElementById('modal-status-select');
    if (statusSelect) {
        statusSelect.dataset.compId = String(id);
        statusSelect.value = state.status || 'To Contact';
    }

    updateModalDateDisplay(state);
    generateAllDrafts();

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeOutreachModal() {
    if (currentModalComp) {
        saveModalNotes(true);
    }
    const modal = document.getElementById('outreach-modal');
    if (modal) modal.classList.remove('open');
    document.body.style.overflow = '';
    currentModalComp = null;
}

function extractDefaultFeature(comp) {
    const hook = comp.nalin_tech_fit_hook || '';
    const sector = comp.domain_sector || '';
    if (sector.includes('Observability') || hook.includes('observability')) return 'telemetry and trace latency';
    if (sector.includes('Voice') || sector.includes('Speech')) return 'real-time voice streaming';
    if (sector.includes('Code') || sector.includes('AST')) return 'AST-based analysis engine';
    if (sector.includes('RAG') || sector.includes('Search')) return 'vector retrieval and reranking';
    if (sector.includes('Agent') || hook.includes('agent')) return 'autonomous agent workflows';
    return comp.company_name + ' platform';
}

function extractDefaultObservation(comp) {
    const hook = comp.nalin_tech_fit_hook || '';
    if (hook.length > 10 && hook.length < 90) return hook;
    return `how your architecture handles sub-second response times`;
}

function updateModalDateDisplay(state) {
    const el = document.getElementById('modal-date-info');
    if (!el) return;
    const parts = [];
    if (state.last_touched_date) parts.push(`Last Touched: ${state.last_touched_date}`);
    if (state.followup_due_date) parts.push(`Follow-up Due: ${state.followup_due_date}`);
    el.innerText = parts.length > 0 ? parts.join(' | ') : 'Pipeline not yet touched';
}

function setLinkedInCharLimit(tier) {
    currentLinkedInTier = tier;
    document.querySelectorAll('.char-limit-tab').forEach(t => {
        t.classList.toggle('active', t.dataset.tier === tier);
    });
    generateLinkedInDraft();
}

function generateAllDrafts() {
    generateLinkedInDraft();
    generateDmDraft();
    generateEmailDraft();
    generateFollowupDraft();
}

function generateLinkedInDraft() {
    if (!currentModalComp) return;
    const name = (currentModalComp.contact_name || currentModalComp.hiring_decision_maker || 'there').split(' ')[0];
    const feature = document.getElementById('input-feature-signal').value.trim() || 'your platform';
    const obs = document.getElementById('input-observation').value.trim() || 'low-latency architecture';
    const limit = currentLinkedInTier === 'free' ? 200 : 300;

    let text = '';
    if (currentLinkedInTier === 'free') {
        text = `Hi ${name}, saw ${currentModalComp.company_name}'s ${feature} and ${obs}. At NimitAI I cut LLM pipelines 317s->117s. Open to connecting?`;
    } else {
        text = `Hi ${name}, saw ${currentModalComp.company_name}'s ${feature} and ${obs}. I build AI products end to end; at NimitAI I cut LLM pipelines from 317s to 117s. Open to connecting about intern / new-grad opportunities?`;
    }

    const txtArea = document.getElementById('draft-linkedin-text');
    txtArea.value = text;

    const charCounter = document.getElementById('linkedin-char-counter');
    const len = text.length;
    charCounter.innerText = `${len}/${limit} chars`;
    charCounter.classList.toggle('char-warning', len > limit);
}

function generateDmDraft() {
    if (!currentModalComp) return;
    const name = (currentModalComp.contact_name || currentModalComp.hiring_decision_maker || 'there').split(' ')[0];
    const feature = document.getElementById('input-feature-signal').value.trim() || 'your platform';

    const text = `Thanks for connecting, ${name}! Really impressed by ${currentModalComp.company_name}'s work on ${feature}.\n\nI built Code Sage (AST code audit engine) and reduced LLM pipeline latency 317s->117s at NimitAI.\n\nAre you taking on interns or early engineers, or is it too early?`;
    
    document.getElementById('draft-dm-text').value = text;
}

function generateEmailDraft() {
    if (!currentModalComp) return;
    const name = (currentModalComp.contact_name || currentModalComp.hiring_decision_maker || 'there').split(' ')[0];
    const feature = document.getElementById('input-feature-signal').value.trim() || 'your platform';
    const obs = document.getElementById('input-observation').value.trim() || 'how your architecture handles throughput';
    const proofKey = document.getElementById('select-proof').value;
    const proofSnippet = PROOF_SNIPPETS[proofKey] || PROOF_SNIPPETS["NimitAI 317s->117s Pipeline Win"];

    const subject = `Quick idea for ${currentModalComp.company_name}'s ${feature}`;
    const body = `Hi ${name},\n\nI was using ${currentModalComp.company_name}'s ${feature} and noticed ${obs}.\n\nI'm Nalin, a final-year AI/DS student who recently ${proofSnippet}. I'd love to help ${currentModalComp.company_name} with ${feature}.\n\nAre you taking interns or early engineers? If it's not the right time, no worries, and I'll happily send a short writeup of what I'd build.\n\nNalin | kumarnalin.me | github.com/nalin`;

    document.getElementById('draft-email-subject').value = subject;
    document.getElementById('draft-email-body').value = body;

    const words = body.split(/\s+/).filter(Boolean).length;
    const wcEl = document.getElementById('email-word-count');
    if (wcEl) {
        wcEl.innerText = `${words} words (Target: 80–120)`;
        wcEl.classList.toggle('char-warning', words > 130);
    }
}

function generateFollowupDraft() {
    if (!currentModalComp) return;
    const name = (currentModalComp.contact_name || currentModalComp.hiring_decision_maker || 'there').split(' ')[0];
    const feature = document.getElementById('input-feature-signal').value.trim() || 'your product';

    const subject = `Re: Quick idea for ${currentModalComp.company_name}'s ${feature}`;
    const body = `Hi ${name},\n\nWanted to share a quick update—I just open-sourced a new optimization pipeline for ${feature}.\n\nWould love to share a 2-minute demo if you're exploring early engineering or intern support this quarter.\n\nBest,\nNalin`;

    document.getElementById('draft-followup-subject').value = subject;
    document.getElementById('draft-followup-body').value = body;
}

// Save Modal Notes & Mark as Sent Actions
function saveModalNotes(quiet = false) {
    if (!currentModalComp) return;
    const id = currentModalComp.id;
    const state = getCompanyState(id);
    state.custom_signal = document.getElementById('input-feature-signal').value;
    state.custom_observation = document.getElementById('input-observation').value;
    state.selected_proof = document.getElementById('select-proof').value;
    state.custom_notes = document.getElementById('modal-custom-notes').value;
    saveCompanyState(id, state, true);
    if (!quiet) {
        outreachToast('Saved research notes to Local Storage.');
    }
}

function markModalStepSent(channel) {
    if (!currentModalComp) return;
    const id = currentModalComp.id;
    saveModalNotes(true);
    if (channel === 'linkedin') {
        updateCompanyStatus(id, 'Connection Sent');
    } else if (channel === 'dm') {
        updateCompanyStatus(id, 'DM Sent');
    } else if (channel === 'email') {
        updateCompanyStatus(id, 'Email Sent');
    } else if (channel === 'followup') {
        updateCompanyStatus(id, 'Followed Up');
    }
}

// Theme Management
function initTheme() {
    const savedTheme = storageGet('theme_preference') || 'dark';
    setTheme(savedTheme, false);
}

function setTheme(theme, showToastNotification = true) {
    document.documentElement.setAttribute('data-theme', theme);
    storageSet('theme_preference', theme);
    updateThemeToggleUI(theme);
    if (showToastNotification) {
        outreachToast(`Theme: ${theme.toUpperCase()}`);
    }
}

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = current === 'dark' ? 'light' : 'dark';
    setTheme(next, true);
}

function updateThemeToggleUI(theme) {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;
    const isDark = theme === 'dark';
    btn.innerHTML = `
        <span class="theme-icon">${isDark ? svgIcons.sun : svgIcons.moon}</span>
        <span class="theme-text">${isDark ? 'Light Mode' : 'Dark Mode'}</span>
    `;
    btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
}

// Local Storage Modal & Live Persistence Indicator
function updateStorageIndicator(justSaved = false) {
    const dot = document.getElementById('storage-status-dot');
    const text = document.getElementById('storage-status-text');
    if (!text) return;

    const lastSaved = storageGet(STORAGE_KEYS.LAST_SAVED);
    let timeStr = 'Saved';
    if (lastSaved) {
        try {
            const d = new Date(lastSaved);
            timeStr = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        } catch {}
    }

    text.innerText = justSaved ? `Saved (${timeStr})` : `Storage: Saved (${timeStr})`;

    if (dot) {
        if (justSaved) {
            dot.classList.add('saved');
            setTimeout(() => dot.classList.remove('saved'), 1000);
        }
    }
}

function openStorageModal() {
    renderStorageModalBody();
    const modal = document.getElementById('storage-modal');
    if (modal) modal.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeStorageModal() {
    const modal = document.getElementById('storage-modal');
    if (modal) modal.classList.remove('open');
    document.body.style.overflow = '';
}

function renderStorageModalBody() {
    const body = document.getElementById('storage-modal-body');
    if (!body) return;

    const comps = window.companyData || [];
    const inPipeline = comps.filter(c => {
        const st = getCompanyState(c.id).status;
        return st && st !== 'To Contact' && st !== 'Archived';
    }).length;

    const withNotes = comps.filter(c => {
        const s = getCompanyState(c.id);
        return Boolean(s.custom_notes || s.custom_signal || s.custom_observation);
    }).length;

    const verified = comps.filter(c => getCompanyState(c.id).contact_verified).length;
    const usage = getStorageUsageInfo();
    const lastSaved = storageGet(STORAGE_KEYS.LAST_SAVED);
    let timeStr = 'Just now';
    if (lastSaved) {
        try {
            timeStr = new Date(lastSaved).toLocaleString();
        } catch {}
    }

    body.innerHTML = `
        <div style="background: var(--bg-surface-elevated); padding: 14px 16px; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 18px; font-size: 13px; line-height: 1.5; color: var(--text-secondary);">
            <strong style="color: var(--text-primary); display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                <span class="storage-dot" style="width: 8px; height: 8px;"></span> Browser Local Storage is Active &amp; Persistent
            </strong>
            All edits (pipeline stages, timestamps, research observations, custom notes, verified contacts, and newly added startups) are saved immediately to your browser's persistent Local Storage. On static hosts like <strong>Vercel</strong>, this ensures 100% of your progress remains intact across page refreshes and visits.
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 10px; margin-bottom: 20px;">
            <div class="analytics-card" style="padding: 12px;">
                <div class="analytics-label">Active Records</div>
                <div class="analytics-val" style="font-size: 20px;">${comps.length}</div>
            </div>
            <div class="analytics-card" style="padding: 12px;">
                <div class="analytics-label">In Pipeline</div>
                <div class="analytics-val" style="font-size: 20px;">${inPipeline}</div>
            </div>
            <div class="analytics-card" style="padding: 12px;">
                <div class="analytics-label">With Notes</div>
                <div class="analytics-val" style="font-size: 20px;">${withNotes}</div>
            </div>
            <div class="analytics-card" style="padding: 12px;">
                <div class="analytics-label">Verified</div>
                <div class="analytics-val" style="font-size: 20px;">${verified}</div>
            </div>
            <div class="analytics-card" style="padding: 12px;">
                <div class="analytics-label">Storage Used</div>
                <div class="analytics-val" style="font-size: 20px;">${usage}</div>
                <div class="analytics-sub">of ~5MB quota</div>
            </div>
        </div>

        <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px; font-family: 'JetBrains Mono', monospace;">
            Last auto-saved: <span style="color: var(--text-primary); font-weight: 600;">${timeStr}</span>
        </div>

        <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin: 16px 0 8px; color: var(--text-muted);">Sync Across Devices &amp; Vercel URLs</h4>
        <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 12px; line-height: 1.4;">
            Because Vercel preview deployments use different domain URLs, you can move your work in 1 click using the clipboard or download a backup file:
        </p>

        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px;">
            <button class="action-btn action-btn-primary" id="modal-copy-clipboard" style="padding: 8px 14px;">
                ${svgIcons.copy} <span>Copy State to Clipboard</span>
            </button>
            <button class="action-btn" id="modal-restore-clipboard" style="padding: 8px 14px;">
                ${svgIcons.draft} <span>Restore from Clipboard</span>
            </button>
            <button class="action-btn" id="modal-download-json" style="padding: 8px 14px;">
                ${svgIcons.download} <span>Download JSON</span>
            </button>
            <button class="action-btn" id="modal-download-csv" style="padding: 8px 14px;">
                ${svgIcons.download} <span>Download CSV</span>
            </button>
            <button class="action-btn" id="modal-import-file" style="padding: 8px 14px;">
                ${svgIcons.upload} <span>Import Backup File</span>
            </button>
        </div>

        <div style="border-top: 1px solid var(--border-subtle); padding-top: 14px; display: flex; justify-content: flex-end;">
            <button class="action-btn btn-danger" id="modal-reset-storage" style="padding: 8px 14px;">
                ${svgIcons.reset} <span>Reset Storage to Default (355 Startups)</span>
            </button>
        </div>
    `;

    document.getElementById('modal-copy-clipboard')?.addEventListener('click', copyStateToClipboard);
    document.getElementById('modal-restore-clipboard')?.addEventListener('click', restoreStateFromClipboard);
    document.getElementById('modal-download-json')?.addEventListener('click', exportTrackerDataJson);
    document.getElementById('modal-download-csv')?.addEventListener('click', exportTrackerDataCsv);
    document.getElementById('modal-import-file')?.addEventListener('click', () => {
        document.getElementById('file-import-input')?.click();
    });
    document.getElementById('modal-reset-storage')?.addEventListener('click', () => {
        resetCompanyList();
        closeStorageModal();
    });
}

// Global Filter & State variables
let activeFilter = 'all';
let activeStatusFilter = 'all';
let currentSort = 'score-desc';
let searchQuery = '';

function render() {
    const tbody = document.getElementById('table-body');
    if (!tbody || typeof window.companyData === 'undefined') return;

    tbody.innerHTML = '';
    const companies = window.companyData;
    const today = getTodayIso();

    let filtered = companies.filter(company => {
        const location = (company.work_model_location || '').toLowerCase();
        const isDelhi = /delhi|noida|gurgaon/.test(location);
        const isRemote = location.includes('remote');
        const state = getCompanyState(company.id);
        const status = state.status || company.outreach_status || 'To Contact';

        // Quick filter pills
        if (activeFilter === 'tierA' && company.tier !== 'Tier A') return false;
        if (activeFilter === 'tierB' && company.tier !== 'Tier B') return false;
        if (activeFilter === 'tierC' && company.tier !== 'Tier C') return false;
        if (activeFilter === 'pipeline' && (status === 'To Contact' || status === 'Archived')) return false;
        if (activeFilter === 'today') {
            const isFollowupDue = state.followup_due_date && state.followup_due_date <= today;
            const isStale = state.last_touched_date && daysDiff(state.last_touched_date, today) >= 5 && !['Replied', 'Interview', 'Offer', 'Archived'].includes(status);
            if (!(['Connection Sent', 'DM Sent', 'Email Sent', 'Followed Up'].includes(status) && (isFollowupDue || isStale))) {
                return false;
            }
        }
        if (activeFilter === 'delhi' && !isDelhi) return false;
        if (activeFilter === 'remote' && !isRemote) return false;

        // Status dropdown filter
        if (activeStatusFilter !== 'all' && status !== activeStatusFilter) return false;

        // Search query
        if (searchQuery) {
            const query = searchQuery.toLowerCase();
            const haystack = [
                company.company_name,
                company.domain_sector,
                company.funding_stage_investors,
                company.work_model_location,
                company.contact_name,
                company.contact_role,
                company.hiring_decision_maker,
                company.nalin_tech_fit_hook,
                company.website,
                company.tier
            ].join(' ').toLowerCase();
            if (!haystack.includes(query)) return false;
        }
        return true;
    });

    // Sorting
    filtered.sort((a, b) => {
        if (currentSort === 'score-desc') return (b.total_score || 0) - (a.total_score || 0);
        if (currentSort === 'score-asc') return (a.total_score || 0) - (b.total_score || 0);
        if (currentSort === 'id-desc') return b.id - a.id;
        if (currentSort === 'id-asc') return a.id - b.id;
        if (currentSort === 'name-asc') return a.company_name.localeCompare(b.company_name);
        if (currentSort === 'name-desc') return b.company_name.localeCompare(a.company_name);
        if (currentSort === 'tier-asc') {
            const order = { 'Tier A': 1, 'Tier B': 2, 'Tier C': 3 };
            return (order[a.tier] || 4) - (order[b.tier] || 4);
        }
        return (b.total_score || 0) - (a.total_score || 0);
    });

    const countShowing = document.getElementById('count-showing');
    if (countShowing) {
        countShowing.innerText = `Showing ${filtered.length} of ${companies.length} records`;
    }

    if (filtered.length === 0) {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td colspan="9" class="empty-state-cell">
                <div class="empty-state">
                    <p class="empty-state-title">No matching company records</p>
                    <p class="empty-state-sub">Try adjusting your search criteria or resetting filters.</p>
                    <button class="filter-btn" id="reset-filters-btn" style="margin-top: 10px;">Reset all filters</button>
                </div>
            </td>
        `;
        tbody.appendChild(tr);
        return;
    }

    const fragment = document.createDocumentFragment();

    filtered.forEach(company => {
        const row = document.createElement('tr');
        const state = getCompanyState(company.id);
        const status = state.status || company.outreach_status || 'To Contact';
        const isDelhi = /delhi|noida|gurgaon/i.test(company.work_model_location || '');
        const locClass = isDelhi ? 'badge-loc-delhi' : 'badge-loc-remote';
        const websiteHref = safeOutreachHref(company.website);
        const careerHref = safeOutreachHref(company.career_page_url);
        const siteCheck = company.link_audit?.website_check;
        const siteOk = siteCheck ? siteCheck.code === 200 : true;

        const tierClass = company.tier === 'Tier A' ? 'badge-tier-a' : (company.tier === 'Tier B' ? 'badge-tier-b' : 'badge-tier-c');
        const dateSubText = formatDateBadge(state);

        row.innerHTML = `
            <td class="col-id">${escapeOutreachHtml(company.id)}</td>
            <td class="company-name-cell">
                <div class="company-name-wrapper">
                    ${websiteHref ? `
                        <a href="${escapeOutreachHtml(websiteHref)}" target="_blank" rel="noopener" class="company-link">
                            <span class="company-title">${escapeOutreachHtml(company.company_name)}</span>
                            ${svgIcons.external}
                        </a>
                    ` : `<span class="company-title">${escapeOutreachHtml(company.company_name)}</span>`}
                    <span class="badge ${tierClass}">${escapeOutreachHtml(company.tier || 'Tier C')}</span>
                    <span class="badge badge-score" title="Breakdown: Stack ${company.score_stack_fit}/5 · Signal ${company.score_hiring_signal}/5 · India ${company.score_india_eligibility}/5 · Warm ${company.score_warm_path}/5 · Comp ${company.score_comp_likelihood}/5">${company.total_score || 0}/25</span>
                </div>
                <div class="audit-label">Contact: ${escapeOutreachHtml(company.contact_name || company.hiring_decision_maker)}</div>
                <span class="audit-badge ${siteOk ? '' : 'badge-alert'}">${siteOk ? 'HTTP 200' : 'Protected/WAF'}</span>
            </td>
            <td><span class="badge badge-sector" title="${escapeOutreachHtml(company.domain_sector)}">${escapeOutreachHtml(company.domain_sector)}</span></td>
            <td>
                <span class="badge ${locClass}" style="margin-bottom: 4px; display: inline-block;">${escapeOutreachHtml(company.work_model_location)}</span>
                <div class="badge badge-size">${escapeOutreachHtml(company.employee_count)} team</div>
            </td>
            <td class="funding-cell">
                <div class="funding-stage">${escapeOutreachHtml(company.funding_stage_investors)}</div>
                <div class="audit-label">${escapeOutreachHtml(company.warm_intro_path || 'Direct Outreach')}</div>
            </td>
            <td class="hook-cell">
                <div class="hook-text">${escapeOutreachHtml(company.nalin_tech_fit_hook)}</div>
            </td>
            <td class="actions-cell">
                <div class="action-stack">
                    <span class="email-text" title="${escapeOutreachHtml(company.career_email)}">${escapeOutreachHtml(company.career_email)}</span>
                    <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                        <button class="btn-copy" data-email="${escapeOutreachHtml(company.career_email)}" data-email-id="${escapeOutreachHtml(company.id)}">
                            ${svgIcons.copy} <span>Copy</span>
                        </button>
                        ${company.linkedin_url ? `
                            <a class="btn-link" href="${escapeOutreachHtml(company.linkedin_url)}" target="_blank" rel="noopener" title="Company LinkedIn">
                                ${svgIcons.linkedin} <span>LinkedIn</span>
                            </a>
                        ` : ''}
                        ${careerHref ? `
                            <a class="btn-link" href="${escapeOutreachHtml(careerHref)}" target="_blank" rel="noopener" title="Careers page">
                                ${svgIcons.external} <span>Careers</span>
                            </a>
                        ` : ''}
                    </div>
                    <label class="email-verify">
                        <input type="checkbox" data-verify-id="${escapeOutreachHtml(company.id)}" ${state.contact_verified ? 'checked' : ''}>
                        <span>Verified contact</span>
                    </label>
                </div>
            </td>
            <td class="status-cell">
                <select class="status-select" data-id="${escapeOutreachHtml(company.id)}" aria-label="Pipeline status">
                    ${PIPELINE_STAGES.map(st => `
                        <option value="${st}" ${status === st ? 'selected' : ''}>${st}</option>
                    `).join('')}
                </select>
                <div class="audit-label date-sub" data-date-id="${escapeOutreachHtml(company.id)}">${escapeOutreachHtml(dateSubText)}</div>
            </td>
            <td style="min-width: 140px;">
                <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                    <button class="draft-btn" data-modal-id="${escapeOutreachHtml(company.id)}" title="Open outreach drafting desk">
                        ${svgIcons.draft} <span>Workbench</span>
                    </button>
                    <button class="btn-copy" data-edit-id="${escapeOutreachHtml(company.id)}" title="Edit company details and scoring">
                        ${svgIcons.edit} <span>Edit</span>
                    </button>
                </div>
            </td>
        `;
        fragment.appendChild(row);
    });

    tbody.appendChild(fragment);
    updateDynamicMetrics();
}

// Event Listeners setup
document.addEventListener('DOMContentLoaded', () => {
    initTheme();

    if (typeof companies !== 'undefined') {
        window.initialCompaniesData = companies;
    }
    initCompanyData();

    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Add Company Button
    const btnAddCompany = document.getElementById('btn-add-company');
    if (btnAddCompany) {
        btnAddCompany.addEventListener('click', openAddCompanyModal);
    }

    // Reset List Button
    const btnResetList = document.getElementById('btn-reset-list');
    if (btnResetList) {
        btnResetList.addEventListener('click', resetCompanyList);
    }

    // Company Form Modal handlers
    const companyForm = document.getElementById('company-form');
    if (companyForm) {
        companyForm.addEventListener('submit', handleCompanyFormSubmit);
    }
    const closeFormModalBtn = document.getElementById('close-form-modal');
    if (closeFormModalBtn) {
        closeFormModalBtn.addEventListener('click', closeCompanyFormModal);
    }
    const cancelFormBtn = document.getElementById('btn-cancel-form');
    if (cancelFormBtn) {
        cancelFormBtn.addEventListener('click', closeCompanyFormModal);
    }
    const deleteCompanyBtn = document.getElementById('btn-delete-company');
    if (deleteCompanyBtn) {
        deleteCompanyBtn.addEventListener('click', handleDeleteCompany);
    }

    // Edit from Workbench header
    const workbenchEditBtn = document.getElementById('btn-edit-from-workbench');
    if (workbenchEditBtn) {
        workbenchEditBtn.addEventListener('click', () => {
            if (currentModalComp) {
                openEditCompanyModal(currentModalComp.id);
            }
        });
    }

    // Score change listeners in company form
    ['score-stack', 'score-hiring', 'score-india', 'score-warm', 'score-comp'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.addEventListener('input', updateFormTotalScore);
    });

    // Analytics Modal triggers
    const analyticsBtn = document.getElementById('btn-analytics');
    if (analyticsBtn) {
        analyticsBtn.addEventListener('click', renderConversionDashboard);
    }
    const closeAnalyticsBtn = document.getElementById('close-analytics-modal');
    if (closeAnalyticsBtn) {
        closeAnalyticsBtn.addEventListener('click', () => {
            document.getElementById('analytics-modal').classList.remove('open');
        });
    }

    // Export & Import
    const btnExportJson = document.getElementById('btn-export-json');
    if (btnExportJson) btnExportJson.addEventListener('click', exportTrackerDataJson);

    const btnExportCsv = document.getElementById('btn-export-csv');
    if (btnExportCsv) btnExportCsv.addEventListener('click', exportTrackerDataCsv);

    const fileInputImport = document.getElementById('file-import-input');
    if (fileInputImport) fileInputImport.addEventListener('change', importTrackerData);

    const btnTriggerImport = document.getElementById('btn-import-trigger');
    if (btnTriggerImport && fileInputImport) {
        btnTriggerImport.addEventListener('click', () => fileInputImport.click());
    }

    // Search and Clear
    const searchInput = document.getElementById('search-input');
    const searchClearBtn = document.getElementById('search-clear-btn');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value.trim();
            if (searchClearBtn) {
                searchClearBtn.style.display = searchQuery ? 'inline-flex' : 'none';
            }
            render();
        });
    }

    if (searchClearBtn) {
        searchClearBtn.addEventListener('click', () => {
            if (searchInput) {
                searchInput.value = '';
                searchQuery = '';
                searchClearBtn.style.display = 'none';
                searchInput.focus();
                render();
            }
        });
    }

    // Restore filter and sort preferences from LocalStorage
    activeFilter = storageGet(STORAGE_KEYS.FILTER_PILL) || 'all';
    activeStatusFilter = storageGet(STORAGE_KEYS.FILTER_STATUS) || 'all';
    currentSort = storageGet(STORAGE_KEYS.SORT_ORDER) || 'score-desc';

    // Filter Buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-filter') === activeFilter);
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            activeFilter = btn.getAttribute('data-filter') || 'all';
            storageSet(STORAGE_KEYS.FILTER_PILL, activeFilter);
            render();
        });
    });

    const statusFilterSelect = document.getElementById('status-filter-select');
    if (statusFilterSelect) {
        statusFilterSelect.value = activeStatusFilter;
        statusFilterSelect.addEventListener('change', (e) => {
            activeStatusFilter = e.target.value;
            storageSet(STORAGE_KEYS.FILTER_STATUS, activeStatusFilter);
            render();
        });
    }

    const sortSelect = document.getElementById('sort-select');
    if (sortSelect) {
        sortSelect.value = currentSort;
        sortSelect.addEventListener('change', (e) => {
            currentSort = e.target.value;
            storageSet(STORAGE_KEYS.SORT_ORDER, currentSort);
            render();
        });
    }

    // View Layout Switcher (Auto / Table / Cards)
    const viewToggleBtns = document.querySelectorAll('.view-toggle-btn');
    const tableContainer = document.querySelector('.table-container');

    function applyViewMode(mode) {
        if (!tableContainer) return;
        tableContainer.classList.remove('cards-mode', 'table-mode');
        if (mode === 'cards') {
            tableContainer.classList.add('cards-mode');
        } else if (mode === 'table') {
            tableContainer.classList.add('table-mode');
        }
        viewToggleBtns.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.view === mode);
        });
        storageSet('layout_view_mode', mode);
    }

    const savedViewMode = storageGet('layout_view_mode') || 'auto';
    applyViewMode(savedViewMode);

    viewToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            applyViewMode(btn.dataset.view);
            const label = btn.dataset.view === 'auto' ? 'Auto Layout' : (btn.dataset.view === 'cards' ? 'Cards View' : 'Table View');
            outreachToast(`Layout: ${label}`);
        });
    });

    // Mobile More Actions Dropdown
    const btnMoreActions = document.getElementById('btn-more-actions');
    const moreActionsMenu = document.getElementById('more-actions-menu');
    if (btnMoreActions && moreActionsMenu) {
        btnMoreActions.addEventListener('click', (e) => {
            e.stopPropagation();
            moreActionsMenu.classList.toggle('open');
        });
        document.addEventListener('click', (e) => {
            if (!moreActionsMenu.contains(e.target) && e.target !== btnMoreActions) {
                moreActionsMenu.classList.remove('open');
            }
        });
    }

    // Storage Modal handlers
    const btnStorageModal = document.getElementById('btn-storage-modal');
    if (btnStorageModal) {
        btnStorageModal.addEventListener('click', openStorageModal);
    }
    const closeStorageModalBtn = document.getElementById('close-storage-modal');
    if (closeStorageModalBtn) {
        closeStorageModalBtn.addEventListener('click', closeStorageModal);
    }
    const storageModal = document.getElementById('storage-modal');
    if (storageModal) {
        storageModal.addEventListener('click', (e) => {
            if (e.target.id === 'storage-modal') closeStorageModal();
        });
    }

    // Workbench Modal listeners
    const closeBtn = document.getElementById('close-modal');
    if (closeBtn) closeBtn.addEventListener('click', closeOutreachModal);

    const modal = document.getElementById('outreach-modal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target.id === 'outreach-modal') closeOutreachModal();
        });
    }

    const formModal = document.getElementById('company-form-modal');
    if (formModal) {
        formModal.addEventListener('click', (e) => {
            if (e.target.id === 'company-form-modal') closeCompanyFormModal();
        });
    }

    const analyticsModal = document.getElementById('analytics-modal');
    if (analyticsModal) {
        analyticsModal.addEventListener('click', (e) => {
            if (e.target.id === 'analytics-modal') analyticsModal.classList.remove('open');
        });
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeOutreachModal();
            closeCompanyFormModal();
            if (analyticsModal) analyticsModal.classList.remove('open');
            closeStorageModal();
        }
    });

    // Inputs inside modal auto-save to Local Storage immediately
    const inputFeature = document.getElementById('input-feature-signal');
    const inputObs = document.getElementById('input-observation');
    const selectProof = document.getElementById('select-proof');
    const modalNotes = document.getElementById('modal-custom-notes');

    if (inputFeature) inputFeature.addEventListener('input', () => { generateAllDrafts(); saveModalNotes(true); });
    if (inputObs) inputObs.addEventListener('input', () => { generateAllDrafts(); saveModalNotes(true); });
    if (selectProof) selectProof.addEventListener('change', () => { generateAllDrafts(); saveModalNotes(true); });
    if (modalNotes) modalNotes.addEventListener('input', () => { saveModalNotes(true); });

    // Flush pending saves on page exit
    window.addEventListener('beforeunload', () => {
        if (_persistTimeout) {
            clearTimeout(_persistTimeout);
            persistAllData(false);
        }
    });

    // LinkedIn Char Limit Tabs
    document.querySelectorAll('.char-limit-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            setLinkedInCharLimit(tab.dataset.tier);
        });
    });

    // Modal Status Select change
    const modalStatusSelect = document.getElementById('modal-status-select');
    if (modalStatusSelect) {
        modalStatusSelect.addEventListener('change', (e) => {
            if (currentModalComp) {
                updateCompanyStatus(currentModalComp.id, e.target.value);
            }
        });
    }

    // Modal "Mark Sent" Buttons
    const btnMarkConn = document.getElementById('btn-mark-conn-sent');
    if (btnMarkConn) btnMarkConn.addEventListener('click', () => markModalStepSent('linkedin'));

    const btnMarkDm = document.getElementById('btn-mark-dm-sent');
    if (btnMarkDm) btnMarkDm.addEventListener('click', () => markModalStepSent('dm'));

    const btnMarkEmail = document.getElementById('btn-mark-email-sent');
    if (btnMarkEmail) btnMarkEmail.addEventListener('click', () => markModalStepSent('email'));

    const btnMarkFollowup = document.getElementById('btn-mark-followup-sent');
    if (btnMarkFollowup) btnMarkFollowup.addEventListener('click', () => markModalStepSent('followup'));

    const btnSaveNotes = document.getElementById('btn-save-notes');
    if (btnSaveNotes) btnSaveNotes.addEventListener('click', () => saveModalNotes(false));

    // Global Delegated click handler
    document.body.addEventListener('click', event => {
        if (event.target.id === 'reset-filters-btn') {
            activeFilter = 'all';
            activeStatusFilter = 'all';
            searchQuery = '';
            if (searchInput) searchInput.value = '';
            if (searchClearBtn) searchClearBtn.style.display = 'none';
            if (statusFilterSelect) statusFilterSelect.value = 'all';
            document.querySelectorAll('.filter-btn').forEach(b => {
                b.classList.toggle('active', b.dataset.filter === 'all');
            });
            render();
            return;
        }

        const modalButton = event.target.closest('[data-modal-id]');
        if (modalButton) {
            openOutreachModal(modalButton.dataset.modalId);
            return;
        }

        const editButton = event.target.closest('[data-edit-id]');
        if (editButton) {
            openEditCompanyModal(editButton.dataset.editId);
            return;
        }

        const emailButton = event.target.closest('[data-email-id]');
        if (emailButton) {
            copyOutreachText(emailButton.dataset.email, emailButton);
            return;
        }

        const copyButton = event.target.closest('[data-copy-target]');
        if (copyButton) {
            const targetEl = document.getElementById(copyButton.dataset.copyTarget);
            const text = targetEl ? (targetEl.value || targetEl.innerText || '').trim() : '';
            if (text) {
                copyOutreachText(text, copyButton);
            } else {
                outreachToast('Field is empty.');
            }
        }
    });

    document.body.addEventListener('change', event => {
        if (event.target.matches('.status-select[data-id]')) {
            updateCompanyStatus(event.target.dataset.id, event.target.value);
            if (activeStatusFilter !== 'all' || activeFilter === 'today' || activeFilter === 'pipeline') {
                render();
            }
        }
        if (event.target.matches('[data-verify-id]')) {
            const id = event.target.dataset.verifyId;
            const state = getCompanyState(id);
            state.contact_verified = event.target.checked;
            storageSet('contact_verified_' + id, String(event.target.checked));
            saveCompanyState(id, state);
            outreachToast(event.target.checked ? 'Contact verified.' : 'Verification removed.');
        }
    });

    render();
    updateDynamicMetrics();
});
